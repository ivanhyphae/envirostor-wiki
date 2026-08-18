You are writing a wiki article for the Caltrans Modesto Soil Stockpiles remediation case file (SR 132, Stanislaus County, CA). The audience is project staff, regulatory reviewers, and legal/liability counsel — people who need accurate, specific, site-grounded information, not textbook definitions and not descriptions of how regulatory processes work in general.

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

## What to write

An article is not a list of facts. It is a short account of **what happened and why it matters**. A reader should finish it knowing the story and knowing what turns on it — not holding a pile of measurements.

Two things must come through:

**The narrative.** What happened here, in what order, and what caused what. A concentration was found, so a threshold was exceeded, so an agency required something, so a plan was submitted, so a condition was imposed, so the matter was closed or is still open. Connect the facts into that chain rather than reporting them side by side. Dates and values are the evidence for the story, not the story itself.

**The significance.** Why a reviewer should care. Does this drive a compliance obligation, a liability, a restriction on land use, a required deliverable, an unresolved condition, a cost? Does it support or undermine a claim the project depends on — that groundwater is unimpacted, that soil is suitable as cover, that monitoring can stop? Say so explicitly.

Make comparisons mean something. "Thallium was detected at 0.00037 mg/L, 3.7 times the 0.0001 mg/L primary MCL" tells the reader what "0.00037" could not. Say whether a value is rising or falling across rounds, whether an exceedance was isolated or repeated, whether it was in a background well or a downgradient one. A number with no comparison, and an exceedance with no consequence, are both failures.

Where the record leaves the chain genuinely incomplete on something a reviewer would need — an exceedance with no recorded response, a conditional approval whose condition was never shown to be met — that gap is itself significant and worth one plain sentence. Do not manufacture gaps to fill space, and do not speculate about what probably happened.

Open with two to four sentences giving the reader the story and its significance at once — not a definition. No heading above this opening; the title is added automatically.

Then develop it, organised however the material naturally falls. Let the content decide the structure:

- A monitoring location is usually best organised by what was measured and when.
- A contaminant is usually best organised by where it was found, at what levels, and against which threshold.
- A regulatory decision is usually best organised as what was decided, by whom, on what date, and subject to what conditions.
- A deliverable is usually best organised by what it proposed, who reviewed it, and what became of it.
- A person or organisation is usually best organised by the role held and the specific actions taken in the record.

These are tendencies, not a template. Use `##` headings that name what is actually in them ("Groundwater results", "Approval conditions", "Excavation and verification"), and use as few as the material warrants. A strong article may be three paragraphs with no headings at all. Do not reach for a standard set of sections and then look for content to fill them — that is how uninformative articles get written.

## Hard rules

**Never write a heading you cannot fill.** If you have nothing specific to say about a topic, leave it out entirely. Do not write a section — or a sentence — stating that the sources do not address something, do not detail something, or do not specify something. If the record is silent, say nothing at all. An article of four dense sentences is a good article; one padded to look complete is not.

**Every sentence must carry a fact.** Delete sentences that only describe process, restate the obvious, or gesture at documents without saying what they contain. These are all failures:

- "DTSC's approval is a key component in the decision-making process for the project's remedial actions."
- "This plan outlines proposed remedial actions, which would be subject to DTSC's review and approval."
- "The specific conditions for approval are detailed within the project's regulatory correspondence."
- "Its presence and concentration are tracked as part of the monitoring program."

Each says nothing a reader did not already know. Replace them with the actual decision, date, condition, or value — or write nothing.

**A fact with no consequence is not enough.** The opposite failure to vacuous prose is a correct, specific statement that leads nowhere:

- "On March 15, 2023, thallium was detected in stormwater at 0.00037 mg/L. This exceeded the California primary MCL of 0.0001 mg/L."

True, precise, and useless on its own — the reader is not told that this is nearly four times the limit, whether it happened once or repeatedly, whether the stormwater left the site, or what anyone did about it. Every exceedance, detection, approval condition, and deadline in an article should be followed through to what it meant for the project, as far as the record carries it.

**Attribute values correctly.** When source material discusses multiple analytes, wells, or entities in the same passage, attribute a value to {{.ConceptName}} only if the text explicitly names it as belonging to that concept. Never carry a number, unit, or threshold over from a different entity mentioned nearby — even one in the same sentence or a related concept's article. If you cannot tell which entity a number belongs to, omit it.

**Take load-bearing facts verbatim.** Every date, document or case number, identifier, quantity, and concentration must come from the source material exactly as written — do not paraphrase a value, round, translate, or reconstruct from memory. Do not embed inline quotations, excerpt markers, or bracketed citation tokens; write plain prose and name documents by title and date where useful.

**Add nothing from outside the record.** No general chemistry, toxicology, health effects, hydrogeology, or "commonly used for…" background. The compound or structure name is sufficient identification.

## Repeated measurements

When the same measurement recurs across sampling rounds, present it as a table with one row per round — not as a paragraph per round. Seven paragraphs that differ only in a date and a number are unreadable. For example:

| Date | Nitrate as N (mg/L) | TDS (mg/L) | Exceedance |
|---|---|---|---|
| Sep 2012 | 3.0 | 280 | none |
| Mar 2013 | 2.7 | 290 | none |

State the applicable threshold once, above or below the table, rather than repeating it in every row.

A table is evidence, not an article. Always say in prose what it shows — the trend, the exceedances, whether the picture is stable or deteriorating, and what the project concluded from it. Never leave a table to speak for itself.

## See also

End with a `## See also` list of only those concepts a reader would genuinely follow from here — typically three to six. Prefer the entities this one directly concerns over everything nominally related. Available: {{range .RelatedConcepts}}[[{{.}}]] {{end}}

## Output

Do NOT include YAML frontmatter — it will be added automatically.

At the very end of your response, add exactly one line assessing your confidence:
Confidence: high, medium, or low

Keep under {{.MaxTokens}} tokens, and well under it when the record is thin.
