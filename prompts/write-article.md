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

## The record outranks the narrative

This is the most important rule in this prompt, and it overrides everything above. **The demand for a story never licenses inventing one.** If the record does not record a consequence, the article has no consequence. A short article that stops where the evidence stops is correct; a complete-sounding one that supplies the missing links is a fabrication, and in a regulatory case file that is the worst thing you can produce.

Never write that an agency required, requested, ordered, or responded, that a plan was submitted, developed, approved, or implemented, or that anything affected schedule, cost, or risk, unless the source material says so. Do not reason from what usually follows an exceedance. Do not conclude that a finding "prompted regulatory action" because that is what normally happens.

**The same ban applies in the conditional.** Speculation is not rescued by the subjunctive: "an exceedance *would* trigger further investigation", "*could* require remediation", "*potentially* impacting project timelines and costs", "*may* affect long-term liability" are all inventions dressed as caution. Write what the record says happened. If nothing is recorded, write nothing — never a hypothetical consequence.

Use the record's own precision and no more. If it says "December 2023", write December 2023 — never sharpen it to a specific day. If it says concentrations were not reported, do not supply a number. Never state a threshold value the sources do not state. Before you write any date, concentration, or threshold, confirm it appears in the source material above; if you cannot point to it, leave it out.

Here is the difference, using a real case from this project. The record establishes that thallium was detected at low concentrations in stockpile soil in the June 2014 Final FS Report, that it had not been detected in groundwater or in pre-2023 surface water, that March 2023 stormwater sampling did **not** report it above MCLs, and that the December 2023 stormwater event was the first reported MCL exceedance for thallium at the site.

Written as fabrication — every clause below is invented and none of it appears in the record:

> "In stormwater samples collected on March 15, 2023, thallium was detected at 0.00037 mg/L, exceeding the California primary MCL of 0.0001 mg/L by a factor of 3.7. In response, Caltrans was required to submit a remediation plan… impacting project timelines and costs."

Written from the record — the significance was there to be found, and needed no invention:

> "Thallium was detected at low concentrations in stockpile soil in the June 2014 Final FS Report and had not appeared in groundwater or in surface water before 2023. The December 2023 stormwater event is the first reported MCL exceedance for thallium at the site; the March 2023 round did not report it above MCLs. The reports covering it are dated February 2024 and February 2025. Concentrations are not given in the available material."

The second is shorter, carries real significance — a first-ever exceedance in a previously clean constituent — and every clause is traceable. Note that its closing sentence states a limit of the evidence, which is legitimate and different from padding: it qualifies a fact being reported, rather than filling a section with an absence.

Where the record genuinely leaves a chain incomplete on something a reviewer would need — an exceedance with no recorded response, a conditional approval never shown to be satisfied — one plain sentence saying so is worth writing. Do not manufacture such gaps to fill space, and never speculate about what probably happened.

**Stay on the subject.** This article is about {{.ConceptName}} and nothing else. Include project background only where it bears directly on this entity, in a clause, not a paragraph. An article about one monitoring well is about that well — its own results, its own trend, its own exceedances — not about the site's history or the other nine wells. If a sentence would sit equally well in twenty other articles, it does not belong in this one. The narrative you are telling is this entity's narrative.

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
- "This highlights the importance of proper stockpile management and the effectiveness of stormwater controls."
- "These were critical steps in demonstrating compliance and ensuring the protection of environmental receptors."
- "This approval signifies a critical milestone in the project's remediation efforts."
- "These results are a key component of the site characterization."
- "…directly impacting project timelines, costs, and potential long-term liability."

Treat these as a family, not a blocklist: any sentence built from "critical milestone", "key component", "significant step", "underscores", "plays a vital role", or an unrecorded appeal to timelines, costs or liability is the same error wearing different words.

The last two are a particular trap when writing about significance: they sound like impact while asserting nothing. Real significance is specific and checkable — a first-ever exceedance, a condition still unmet, a well that must be destroyed before construction, a threshold that decides whether soil can be reused on site.

Each says nothing a reader did not already know. Replace them with the actual decision, date, condition, or value — or write nothing.

**A fact with no consequence is not enough.** The opposite failure to vacuous prose is a correct, specific statement that leads nowhere:

- "On March 15, 2023, thallium was detected in stormwater at 0.00037 mg/L. This exceeded the California primary MCL of 0.0001 mg/L."

True, precise, and useless on its own — the reader is not told that this is nearly four times the limit, whether it happened once or repeatedly, whether the stormwater left the site, or what anyone did about it. Every exceedance, detection, approval condition, and deadline in an article should be followed through to what it meant for the project, as far as the record carries it.

**Attribute values correctly.** When source material discusses multiple analytes, wells, or entities in the same passage, attribute a value to {{.ConceptName}} only if the text explicitly names it as belonging to that concept. Never carry a number, unit, or threshold over from a different entity mentioned nearby — even one in the same sentence or a related concept's article. If you cannot tell which entity a number belongs to, omit it.

**Take load-bearing facts verbatim.** Every date, document or case number, identifier, quantity, and concentration must come from the source material exactly as written — do not paraphrase a value, round, translate, or reconstruct from memory. Do not embed inline quotations, excerpt markers, or bracketed citation tokens; write plain prose and name documents by title and date where useful.

**Add nothing from outside the record.** No general chemistry, toxicology, health effects, hydrogeology, or "commonly used for…" background. The compound or structure name is sufficient identification.

## Repeated measurements

Writing for narrative does not mean abandoning the data. Where this entity has results across several sampling rounds, those results belong in the article as a table, with the prose explaining what the table shows. Do not summarise a run of measurements away into a generalisation like "concentrations generally remained below thresholds" when the individual values are available — give the values and then say what they mean.

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
