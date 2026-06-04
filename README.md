# SR132 EnviroStor Wiki

Compiled knowledge base for State Route 132 environmental remediation documents.

## Adding New Documents

1. Drop files into `sr132-docs-raw/` (PDF, DOCX, XLSX, PPTX, CSV, MD, etc.)
2. Recompile:
   ```bash
   cd ~/hyphae/hyphae-work/sr132/envirostor-wiki/wiki
   ~/repos/sage-wiki/sage-wiki compile
   ```
3. Rebuild site:
   ```bash
   cd ~/hyphae/hyphae-work/sr132/envirostor-wiki/site
   npx quartz build
   ```

Sage-wiki only processes new/changed files — it remembers what it's already compiled.

### Useful flags

- `--watch` — auto-recompile when files change
- `--estimate` — show cost estimate without compiling
- `--dry-run` — show what would change
- `--batch` — use batch API for 50% cost reduction (async)

## Where Things Live

| What | Path |
|------|------|
| Source docs | `sr132-docs-raw/` |
| Config | `wiki/config.yaml` |
| Wiki output | `wiki/` (concepts, summaries, connections) |
| Home page | `wiki/index.md` |
| Quartz site | `site/` |
| Built website | `site/public/` |

## Schema & Prompts

The compilation is guided by templates in the sage-wiki repo at `~/repos/sage-wiki/internal/prompts/templates/`:

- `extract_concepts.txt` — how concepts are extracted from summaries
- `write_article.txt` — how articles are written per concept
- `summarize_article.txt` / `summarize_paper.txt` — source summarization

Ontology (entity & relation types) is in `~/repos/sage-wiki/internal/ontology/`. Custom types can be added in `wiki/config.yaml` under `ontology:`.

## Local Preview

```bash
cd ~/hyphae/hyphae-work/sr132/envirostor-wiki/site
npx quartz build --serve
```

Opens at `localhost:8080`.
