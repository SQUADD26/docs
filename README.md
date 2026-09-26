# Documentazione di Gestione Sala

Sorgenti di [docs.gestionesala.com](https://docs.gestionesala.com), costruito con [Mintlify](https://mintlify.com).

## Cosa c'e'

| Percorso | Contenuto |
| --- | --- |
| `docs.json` | Configurazione: navigazione, colori, logo, menu contestuale |
| `index.mdx`, `guida/` | Guida all'app, una pagina per sezione |
| `api/` | Introduzione all'API, autenticazione, errori, idempotenza, limiti di richiesta, riferimento completo (generato) |
| `openapi.yaml` | Specifica OpenAPI 3.1 dell'API v1: genera le pagine per endpoint |
| `scripts/riferimento.py` | Genera `api/riferimento-completo.mdx` da `openapi.yaml` |
| `style.css` | Colore arancio del codice inline e dei badge |
| `ia/` | llms.txt, Markdown, server MCP, prompt per agenti |
| `logo/`, `favicon.png`, `og-image.png` | Marchio `gestionesala.com` con "sala" in gradiente, da `public/brand/logo-primo-avvio.png` dell'app |
| `AGENTS.md` | Regole per chi scrive (persone e agenti) |

## Anteprima locale

```bash
npm i -g mint   # una volta
mint dev --port 3333   # http://localhost:3333
```

## Controlli

```bash
mint validate
mint broken-links
```

## Aggiornare l'API

1. Modifica `openapi.yaml` quando cambia l'API in `gestionesala-ai` (`src/app/api/v1/`, `src/lib/api-v1/`).
2. Rigenera il riferimento completo: `python3 scripts/riferimento.py`.
3. Controlla: `mint validate` e `mint openapi-check openapi.yaml`.
4. Se cambiano autenticazione, errori, idempotenza o limiti, aggiorna anche le pagine in `api/`.
5. Le pagine per endpoint si generano da `openapi.yaml`: non vanno scritte a mano.

## Pubblicazione

Ogni push su `main` pubblica il sito tramite l'app GitHub di Mintlify.
