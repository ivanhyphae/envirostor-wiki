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

When source material discusses multiple analytes, wells, or entities in the same passage, attribute a value to {{.ConceptName}} only if the text explicitly names it as belonging to that concept. Never carry a number, unit, or threshold over from a different entity mentioned nearby — even one in the same sentence or a related concept's article — into this concept's claims. If you can't tell which entity a number belongs to, omit it.

Every specific date, document/case number, identifier (well ID, APN, site code), quantity, concentration, or other load-bearing fact must be taken verbatim from the source material below — do not paraphrase a value, translate, round, or reconstruct it from memory. If the sources do not state a fact exactly, omit it rather than approximating. Do not embed inline quotations, excerpt markers, or bracketed citation tokens in the prose — write plain narrative text and refer to documents by name and date where useful.

Write only what the record supports. Never pad an article to fill a template: omit any section you cannot fill with real content from the sources, and never write a section whose content is a statement that the sources do not address the topic. A short, dense article is correct; a long one padded with "not documented in the provided source material" is not.

Adapt the article structure to what this concept actually is. Use whichever sections apply:

## Overview
This entity's role in this project, grounded only in what the sources establish. For a contaminant: only its role at *this* site — where it was found, at what levels, why it's being tracked here. Do not add general chemistry, toxicology, health effects, or "commonly used for..." background not present in the sources — the compound name is sufficient identification. For a monitoring location: where it is, what it monitors (per the record, not generic hydrogeology). For a regulatory decision: what was decided, by whom, when. For a remedial action: what was done and why. Keep this brief — the detail belongs below.

## Site record
The documented facts from project sources: concentrations with units and dates, spatial distribution, exceedances relative to applicable thresholds, trends over time, verification results, approval conditions, volumes, phases. Be specific. Use the exact names, identifiers, values, and units as they appear in the record for *this* concept (e.g. a well ID like "MW-5", an agency like "DTSC", a phase label like "Phase 1 2019–2020") — never a value borrowed from this instruction's own examples or from a different concept.

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
