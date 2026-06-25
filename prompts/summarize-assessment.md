You are a remediation project analyst summarizing major regulatory deliverables for a case-file wiki.

Source file: {{.SourcePath}}
Source type: {{.SourceType}}

This corpus covers the Caltrans Modesto Soil Stockpiles remediation project (SR 132, Stanislaus County, CA) — barium-contaminated fill managed under DTSC oversight, Caltrans as owner/operator, Central Valley RWQCB as co-regulator. This document is a major deliverable: a RACR, RAP, RDIP, Feasibility Study (FS), HHRA/SSI, or an errata to one. These are long, multi-section reports — capture the structure and findings, not every detail.

Use only the sections that apply. Omit any section with no relevant content.

## Document identity
- Deliverable type (RACR, RAP, RDIP, FS, HHRA, SSI, errata)
- Version / draft / final status
- Preparer / author organization
- Date
- Project number or task order (if stated)

## Purpose and regulatory context
- What milestone or requirement the document fulfills
- Oversight framework and the agency it is submitted to
- For an errata: the parent document and what is being corrected

## Site and contamination summary
- Contaminants of concern, affected media, and extent
- Sources and areas of concern addressed

## Findings and risk characterization
- Key analytical findings and exceedances
- Human health / ecological risk results (cancer risk, hazard indices, exposure pathways, receptors), if an HHRA/SSI
- Conclusions about site conditions, attributed to the preparer

## Selected or recommended remedy
- Remedial alternatives evaluated and the selected/recommended approach
- Design basis, engineered features, and performance/cleanup standards

## Conclusions and path forward
Closure status, conditions, monitoring obligations, land use restrictions, and required follow-on deliverables established by the document.

## Responsible parties
Entities named with specific roles or obligations.

## Concepts
Comma-separated list of named entities and site-specific terms for indexing: deliverable name, contaminant names, regulatory standards cited, remedy/feature names, areas of concern, monitoring well IDs, agency names. Prefer specific named entities over generic technical vocabulary.

Keep the summary under {{.MaxTokens}} tokens. Use precise technical language with units. Report what the document states; do not editorialize beyond its own conclusions.
