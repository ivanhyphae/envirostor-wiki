You are writing a wiki article for the Caltrans Modesto Soil Stockpiles remediation case file (SR 132, Stanislaus County, CA). The audience is project staff, regulatory reviewers, and legal/liability counsel — people who need accurate, specific, site-grounded information, not textbook definitions.

Concept: {{.ConceptName}}
Sources: {{.Sources}}
Related concepts: {{.RelatedList}}

{{if .ExistingArticle}}
## Existing article (update or expand with new source material):
{{.ExistingArticle}}
{{end}}

{{if .SourceContext}}
## Relevant source material:
{{.SourceContext}}
{{end}}

{{if .Learnings}}
## Learnings from previous compilations (follow these):
{{.Learnings}}
{{end}}

Write a wiki article grounded in the project record. The article should be useful to someone reviewing the case file — cite specific values, dates, document names, and agency decisions where the sources support it.

Adapt the article structure to what this concept actually is. Use whichever sections apply:

## Overview
What this entity is and its role in this project. For a contaminant: what it is, why it matters here. For a monitoring location: where it is, what it monitors. For a regulatory decision: what was decided, by whom, when. For a remedial action: what was done and why. Keep this brief — the detail belongs below.

## Site record
The documented facts from project sources: concentrations with units and dates, spatial distribution, exceedances relative to applicable thresholds, trends over time, verification results, approval conditions, volumes, phases. Be specific. Use the names and identifiers that appear in the record (MW-5, DTSC, barium 760 mg/kg, MCL 1,000 µg/L, Phase 1 2019–2020, etc.).

## Regulatory status
Applicable standards (MCLs, screening levels, background thresholds, action levels), the agencies that set or enforce them, and whether the project is currently in compliance, subject to conditions, or pending further action.

## Open items
Unresolved issues, pending deliverables, contested claims, or required future actions documented in the sources. Omit if nothing is open.

## See also
Related concepts as [[wikilinks]]:
{{range .RelatedConcepts}}- [[{{.}}]]
{{end}}

Do NOT include YAML frontmatter — it will be added automatically.

At the very end of your response, add exactly one line assessing your confidence:
Confidence: high, medium, or low

Keep under {{.MaxTokens}} tokens. Every factual claim should be traceable to the source documents. Do not fill gaps with general knowledge — if the sources don't say it, omit it or flag it as not documented.
