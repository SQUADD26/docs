# Documentazione di Gestione Sala

Sorgenti di [docs.gestionesala.com](https://docs.gestionesala.com), costruito con [Mintlify](https://mintlify.com).

## Cosa c'e'

| Percorso | Contenuto |
| --- | --- |
| `docs.json` | Configurazione: navigazione, colori, logo, menu contestuale |
| `index.mdx`, `guida/` | Guida all'app, una pagina per sezione |
| `api/` | Introduzione all'API, autenticazione, errori, idempotenza, limiti |
| `openapi.yaml` | Specifica OpenAPI 3.1 dell'API pubblica v1: genera il riferimento API |
| `ia/` | llms.txt, Markdown, server MCP, prompt per agenti |
| `logo/`, `favicon.svg`, `og-image.png` | Marchio, copiato dall'app |
| `AGENTS.md` | Regole per chi scrive (persone e agenti) |

## Anteprima locale

```bash
npm i -g mint   # una volta
mint dev        # http://localhost:3000
```

## Controlli

```bash
mint validate
mint broken-links
```

## Aggiornare l'API

1. Modifica `openapi.yaml` quando cambia l'API in `gestionesala-ai` (`src/app/api/v1/`, `src/lib/api-v1/`).
2. Controlla la specifica: `mint validate`.
3. Se cambiano autenticazione, errori, idempotenza o limiti, aggiorna anche le pagine in `api/`.
4. Le pagine del riferimento si rigenerano da sole: non vanno scritte a mano.

## Pubblicazione

Ogni push su `main` pubblica il sito tramite l'app GitHub di Mintlify.
