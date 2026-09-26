# Istruzioni per chi scrive in questo repo

Sito documentazione di **Gestione Sala** (docs.gestionesala.com), costruito con Mintlify. App: https://app.gestionesala.com. Codice dell'app: repo `gestionesala-ai`.

## Struttura

- `docs.json`: configurazione e navigazione (tab Guida, API, IA e agenti).
- `index.mdx`, `guida/`: guida all'app per chi la usa.
- `api/`: pagine scritte a mano sull'API (introduzione, autenticazione, errori, idempotenza, limiti di richiesta). `api/riferimento-completo.mdx` è generata da `scripts/riferimento.py`: non modificarla a mano.
- `openapi.yaml`: specifica OpenAPI 3.1 dell'API pubblica v1. Genera le pagine per endpoint (gruppi per risorsa nella tab API). E' la fonte di verita': le pagine in `api/` non devono contraddirla.
- `ia/`: come dare le docs a un'IA o a un agente.

## Regole

- Tutto in italiano, con accenti veri (è, più, già). Registro tecnico come Stripe o Anthropic: frasi dichiarative, un fatto per frase, nomi di campo esatti in `code`. Vietati metafore, domande retoriche, toni da chat, "semplicemente", "facile".
- Summary di un endpoint: imperativo + risorsa ("Crea una prenotazione"). Descrizione: cosa fa, precondizioni, effetti collaterali, cosa restituisce.
- I casi limite si descrivono come comportamento: "Se non c'è disponibilità, la risposta è `200` con `available: false`".
- Documenta solo cio' che esiste nell'app (ramo `dev` di `gestionesala-ai`). Niente funzioni inventate o future spacciate per reali.
- Usa i termini del glossario (`guida/glossario.mdx`, che viene da `CONTEXT.md` dell'app). A schermo il CRM si chiama **SQUADD**, mai GHL.
- Nomi dei pulsanti in grassetto, come compaiono nell'app: **Crea una chiave**.
- Codice, percorsi, header e campi in `code`.

## Prima di committare

```bash
python3 scripts/riferimento.py
mint validate
mint broken-links
mint openapi-check openapi.yaml
```
