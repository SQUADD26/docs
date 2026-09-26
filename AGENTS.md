# Istruzioni per chi scrive in questo repo

Sito documentazione di **Gestione Sala** (docs.gestionesala.com), costruito con Mintlify. App: https://app.gestionesala.com. Codice dell'app: repo `gestionesala-ai`.

## Struttura

- `docs.json`: configurazione e navigazione (tab Guida, API, IA e agenti).
- `index.mdx`, `guida/`: guida all'app per chi la usa.
- `api/`: pagine scritte a mano sull'API (autenticazione, errori, idempotenza, limiti).
- `openapi.yaml`: specifica OpenAPI 3.1 dell'API pubblica v1. Genera da sola le pagine del gruppo "Riferimento". E' la fonte di verita': le pagine in `api/` non devono contraddirla.
- `ia/`: come dare le docs a un'IA o a un agente.

## Regole

- Tutto in italiano. Tono asciutto, niente marketing, niente slogan.
- Documenta solo cio' che esiste nell'app (ramo `dev` di `gestionesala-ai`). Niente funzioni inventate o future spacciate per reali.
- Usa i termini del glossario (`guida/glossario.mdx`, che viene da `CONTEXT.md` dell'app). A schermo il CRM si chiama **SQUADD**, mai GHL.
- Nomi dei pulsanti in grassetto, come compaiono nell'app: **Crea una chiave**.
- Codice, percorsi, header e campi in `code`.

## Prima di committare

```bash
mint validate
mint broken-links
```
