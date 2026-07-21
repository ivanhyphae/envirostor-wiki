<!-- sage-wiki:skill:start -->
## sage-wiki — project knowledge base

This project (envirostor-wiki) uses sage-wiki as its knowledge layer.
Sources: auto. The wiki contains structured, interlinked
knowledge compiled from your sources.

### When to check the wiki

Before making changes or answering questions, search the wiki first:

- Modifying a component or interface
- Answering "why is it done this way?" or "what's known about X?"
- Making a decision that others should know about
- Touching an area you haven't worked with before
- Looking for related work or prior context

1. Call `wiki_search` with the topic or concept name
2. Read relevant articles with `wiki_read`
3. Use `wiki_ontology_query` to explore relationships and dependencies
4. If search returns uncompiled sources, call `wiki_compile_topic` for richer context
5. Use `wiki_provenance` to trace which sources produced an article

### What to capture

After completing work that produced new knowledge:

- A decision or tradeoff → `wiki_learn` with type "decision"
- A non-obvious finding or gotcha → `wiki_learn` with type "gotcha"
- A pattern or convention → `wiki_learn` with type "convention"
- Rich context from a conversation → `wiki_capture` to extract and index it

### How to query effectively

- Use concept names, not questions: "connection pooling" not "how does connection pooling work?"
- Use `wiki_status` at session start to know what's indexed
- Entity types available: concept, technique, source, claim, artifact, site, contaminant, monitoring_location, sampling_event, remedial_action, monitoring_result, infrastructure, regulatory_decision, responsible_party, regulatory_standard, deliverable, risk, liability, community_concern
- Query relationships: `wiki_ontology_query` with entity ID and relation type
- Relation types: implements, extends, optimizes, contradicts, cites, prerequisite_of, trades_off, derived_from, contaminates, located_at, exceeds, measured_in, remediates, capped_with, migrated_to, approved_by, regulated_by, responsible_for, submitted_to, conditioned_on, supersedes, supports, refutes, based_on, exposes, mitigated_by, raises_concern, restricts
- Filter searches with tags: `wiki_search("topic", tags="tag-name")`

<!-- sage-wiki:skill:end -->
