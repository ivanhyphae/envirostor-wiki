---
concept: errata
entity_type: concept
aliases: ["errata sheet", "RDIP errata"]
sources: ["RDIP Errata Acceptance.pdf"]
confidence: high
created_at: 2026-06-04T08:18:50Z
---

## Definition

An **errata** (plural of *erratum*) is a formal correction to a published document, such as a Request for Comments (RFC), standard, specification, or book. In the context of technical standards and protocols, errata are used to rectify errors, omissions, ambiguities, or inconsistencies identified after official publication, without requiring a full revision of the document. The RDIP (RFC Development and Improvement Process) Errata Acceptance process defines rules and procedures for submitting, reviewing, and accepting errata for RFCs.

## How it works

The RDIP Errata Acceptance process operates as a structured workflow to ensure corrections are vetted and applied while maintaining the integrity of the original document. Key steps include:

1. **Submission:** Anyone can submit an erratum via a designated tracking system (e.g., the RFC Errata Page). The submission must identify the RFC, describe the error, and propose a correction.

2. **Verification:** The erratum is reviewed by the RFC Editor or a designated Area Director (AD) for the relevant standardization area. Verification checks:
   - Is the error genuine (not a misunderstanding)?
   - Is the proposed correction technically sound and consistent with the RFC’s intent?
   - Does it conflict with other standards or accepted practices?

3. **Status Classification:** After review, the erratum is assigned one of the following statuses:
   - **Reported:** Initial submission, awaiting review.
   - **Verified:** Confirmed as a valid correction.
   - **Held for Document Update:** Applied but not published until the next revision of the RFC.
   - **Rejected:** Not accepted as a valid erratum (e.g., due to misinterpretation).
   - **Withdrawn:** Submitted but later retracted by the author.

4. **Publication:** Verified errata are published on the RFC Errata page, with a note linking to the original RFC. For standards-track RFCs, errata may be incorporated into future updates (e.g., a bis version).

5. **Metadata:** Each erratum includes the RFC number, section, date, submitter, and a rationale for the correction.

## Variants

While the RDIP process is specific to IETF RFCs, similar errata mechanisms exist in other domains:

- **Book Errata:** Corrections published by publishers (e.g., O'Reilly, Springer) for print or digital editions, often maintained on a webpage.
- **Software Errata:** In open-source project documentation (e.g., Linux man pages), errata are sometimes tracked via bug reports or commit notes.
- **Specification Errata:** For standards bodies like ISO, IEEE, or W3C, errata may be issued as official corrigenda (individual corrections) or amendments (batch updates).
- **Academic Errata:** Journals often publish corrections in subsequent issues, sometimes with a separate "Erratum" section.

## Trade-offs

| Advantage | Limitation |
|-----------|------------|
| **Fixes errors without full revision** – Saves time and effort compared to republishing an entire document. | **Potential for fragmentation** – Multiple errata can clutter a base document, making it harder to find the current state. |
| **Transparent history** – Allows tracking of known issues and resolutions. | **Delayed adoption** – Not all errata are automatically applied; downstream implementations may ignore them. |
| **Community input** – Enables anyone to contribute corrections, enhancing accuracy. | **Quality control** – Incorrect errata submissions (e.g., due to misinterpretation) can waste reviewer time. |
| **Standardized process** – RDIP provides clear rules and statuses, reducing ambiguity. | **Limited applicability** – Errata only correct minor errors; substantial changes still require a new RFC. |

Key considerations:
- Errata are not substitutes for ongoing maintenance; critical errors may prompt a new RFC version.
- Errata acceptance relies on voluntary review, leading to potential backlogs for high-volume RFCs.
- For implementations, relying solely on errata without tracking the corrected standard can cause compliance issues.

## See also

- RFC
- IETF
- RFC Editor
- Corrigendum
- Standard
- Document revision