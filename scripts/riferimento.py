"""Genera api/riferimento-completo.mdx da openapi.yaml.

Uso: python3 scripts/riferimento.py  (dalla radice del repo, richiede PyYAML)

La pagina mette tutto il riferimento API in MDX, cosi' finisce per intero in
/llms-full.txt. Non modificare la pagina a mano: rigenerala.
"""
import json
import pathlib
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = yaml.safe_load((ROOT / "openapi.yaml").read_text())
comp = spec["components"]


def ref(obj):
    while isinstance(obj, dict) and "$ref" in obj:
        section, name = obj["$ref"].split("/")[-2:]
        obj = comp[section][name]
    return obj


def one_line(text):
    return " ".join((text or "").split())


def type_of(schema):
    schema = ref(schema)
    t = schema.get("type", "object")
    t = " \\| ".join(t) if isinstance(t, list) else t
    if "format" in schema:
        t += f" ({schema['format']})"
    if "enum" in schema:
        t += ": " + ", ".join(f"`{json.dumps(v)}`" if not isinstance(v, str) else f"`{v}`" for v in schema["enum"])
    return t


def fields_table(schema, prefix="", head="Obbligatorio"):
    schema = ref(schema)
    required = set(schema.get("required", []))
    rows = []
    for name, prop in schema.get("properties", {}).items():
        prop = ref(prop)
        req = "sì" if name in required else "no"
        rows.append(f"| `{prefix}{name}` | {type_of(prop)} | {req} | {one_line(prop.get('description'))} |")
        if prop.get("properties"):
            rows += fields_table(prop, f"{prefix}{name}.")[2:]
        if prop.get("items") and ref(prop["items"]).get("properties"):
            rows += fields_table(prop["items"], f"{prefix}{name}[].")[2:]
    return [f"| Campo | Tipo | {head} | Descrizione |", "| --- | --- | --- | --- |"] + rows


def response_schemas(schema):
    schema = ref(schema)
    return [ref(s) for s in schema["oneOf"]] if "oneOf" in schema else [schema]


out = [
    "---",
    'title: "Riferimento completo"',
    'description: "Tutti gli endpoint dell\'API v1 in una pagina: parametri, body, risposte ed errori. Generata da openapi.yaml."',
    'icon: "file-lines"',
    "---",
    "",
    "{/* Generata da scripts/riferimento.py. Non modificare a mano. */}",
    "",
    f"Base URL: `{spec['servers'][0]['url']}`. Autenticazione: header `Authorization: Bearer gsk_...` su ogni richiesta.",
    "Specifica sorgente: [`openapi.yaml`](https://raw.githubusercontent.com/SQUADD26/docs/main/openapi.yaml).",
    "",
]

for path, ops in spec["paths"].items():
    for method, op in ops.items():
        out += [f"## {op['summary']}", "", f"`{method.upper()} {path}`", ""]
        if op.get("x-mint", {}).get("href"):
            out += [f"Pagina con playground: [{op['x-mint']['href']}]({op['x-mint']['href']})", ""]
        for para in op.get("description", "").split("\n\n"):
            if para.strip():
                out += [one_line(para), ""]

        params = [ref(p) for p in op.get("parameters", [])]
        if params:
            out += ["### Parametri", "", "| Nome | Posizione | Tipo | Obbligatorio | Descrizione |", "| --- | --- | --- | --- | --- |"]
            for p in params:
                req = "sì" if p.get("required") else "no"
                out.append(f"| `{p['name']}` | {p['in']} | {type_of(p['schema'])} | {req} | {one_line(p.get('description'))} |")
            out.append("")

        body = op.get("requestBody")
        if body:
            media = body["content"]["application/json"]
            out += ["### Body (JSON)", ""]
            if ref(media["schema"]).get("description"):
                out += [one_line(ref(media["schema"])["description"]), ""]
            out += fields_table(media["schema"]) + [""]
            out += ["```json Esempio di body", json.dumps(media["example"], indent=2, ensure_ascii=False), "```", ""]

        out += ["### Risposte", "", "| Status | Descrizione |", "| --- | --- |"]
        for status, resp in op["responses"].items():
            out.append(f"| `{status}` | {one_line(ref(resp)['description'])} |")
        out.append("")

        ok = next((r for s, r in op["responses"].items() if s in ("200", "201")), None)
        media = ref(ok)["content"]["application/json"]
        out += ["### Campi della risposta", ""]
        for schema in response_schemas(media["schema"]):
            if schema.get("title"):
                out += [f"**{schema['title']}**", ""]
            out += fields_table(schema, head="Sempre presente") + [""]
        examples = [media["example"]] if "example" in media else [e["value"] for e in media.get("examples", {}).values()]
        for ex in examples:
            out += ["```json Esempio di risposta", json.dumps(ex, indent=2, ensure_ascii=False), "```", ""]

out += ["## Oggetto errore", "", "Tutte le risposte di errore hanno questo formato.", ""]
out += fields_table(comp["schemas"]["Error"]) + [""]

(ROOT / "api" / "riferimento-completo.mdx").write_text("\n".join(out))
print("scritto api/riferimento-completo.mdx")
