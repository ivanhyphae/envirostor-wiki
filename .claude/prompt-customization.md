# Prompt customization — envirostor-wiki

## What was done (2026-06-10)

Replaced the default sage-wiki prompt templates with domain-specific versions
for the Caltrans Modesto Soil Stockpiles (SR 132) remediation corpus.

### Root cause of the academic framing problem

sage-wiki's template selection logic is:
  `templateName := "summarize_" + content.Type`

The extract package hard-codes two type values:
- `.pdf` files → type `"paper"` → uses `summarize_paper.txt` ("academic paper")
- everything else → type `"article"` → uses `summarize_article.txt` ("research assistant / methodology / results")

Both built-in templates use academic research framing (Key claims / Methodology /
Results / Limitations). The `write_article.txt` default frames concepts as CS/ML
reference entries (Definition / How it works / Variants / Trade-offs).

The four existing prompts in `prompts/` (extract_claims_and_risks.md, etc.)
had good domain content but **wrong filenames** — sage-wiki's LoadFromDir maps
filenames to template slot names, and those four names don't correspond to any
slot the pipeline ever calls. They were silently ignored.

### Files created/replaced in prompts/

| File | Slot it overrides | Purpose |
|------|-------------------|---------|
| `summarize-paper.md` | `summarize_paper.txt` | All PDFs — regulatory docs, monitoring reports, approval letters, workplans, RACRs |
| `summarize-article.md` | `summarize_article.txt` | Markdown/non-PDF sources |
| `write-article.md` | `write_article.txt` | Concept articles — site-contextualized, not textbook-style |
| `extract-concepts.md` | `extract_concepts.txt` | Extracts named project entities, not generic scientific vocabulary |

The four old misnamed files (extract_claims_and_risks.md, extract_monitoring_data.md,
extract_regulatory_decisions.md, extract_site_characterization.md) are left in place
— they don't cause harm, and their content informed the new prompts.

### Key design decisions

**summarize-paper.md**: Sections are conditional (omit if not applicable).
The document identity section anchors every summary to what type of regulatory
document this is and who wrote it for whom. No "Methodology / Results" framing.
The "Claims" section asks for attribution and whether each claim is supported/
contested — important for the trust/verification pipeline.

**write-article.md**: Instructs the LLM to adapt structure to entity type rather
than forcing every concept into the same frame. The "Site record" section replaces
"How it works" — it asks for specific values, dates, document references from the
project record. Explicit instruction: "if the sources don't say it, omit it" —
prevents the LLM from filling gaps with general knowledge (as happened with the
chromium article, which became a general chemistry reference).

**extract-concepts.md**: Provides a positive list of strong candidate types
(monitoring wells, named contaminants, specific deliverables, named responsible
parties) and an explicit negative list (don't extract generic methods or broad
science terms). This should stop extraction of "ICP-MS", "Brownfields/Redevelopment",
"hydraulic gradient" etc. as standalone concepts.

### To recompile with new prompts

The diff that determines what recompiles is based on `.manifest.json` file hashes.
Sources with unchanged hashes are silently skipped regardless of any flags.
`--fresh` only skips the `.sage/compile-state.json` interrupt-resume checkpoint.
`--no-cache` only disables LLM prompt caching (Anthropic cache_control). Neither
touches the manifest or wiki.db.

To fully recompile all sources with the new prompts:

```bash
cd /home/ivanh/hyphae/hyphae-work/sr132/envirostor-wiki
rm .manifest.json
rm .sage/wiki.db
rm -rf wiki/summaries/ wiki/concepts/
sage-wiki compile
```

`wiki.db` is a derived cache (FTS5, vectors, ontology, compile_items) and will be
fully rebuilt. The manifest is recreated from scratch. All 114 sources will be treated
as new and processed with the new prompts.
