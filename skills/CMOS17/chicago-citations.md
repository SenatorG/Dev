---
name: chicago-citations
description: Applies Chicago Manual of Style 17th Edition citation systems, source validation, bibliography or reference-list construction, and artifact-aware citation mechanics. Use when the user requests Chicago, CMOS, author-date, inline or parenthetical citations, footnotes, endnotes, a bibliography, references, works cited, or an existing artifact uses Chicago.
---

# Chicago Citations

Apply CMOS 17 to the final deliverable when this skill is activated. This skill controls citation style, source validation, citation density, and terminal source lists. Do not decide whether to disclose AI assistance; use the separate AI Provenance skill for that concern.

## Activation and precedence

Activate when the user explicitly requests Chicago or an existing artifact consistently uses Chicago. Do not impose Chicago merely because the work is sourced.

Resolve conflicts in this order:

1. Explicit user instruction.
2. A consistent citation system already present in the artifact.
3. A documented institutional, Dell, publication, or artifact convention.
4. The defaults below.

If the user requests a conversion, normalize the artifact consistently. If the artifact mixes systems and the user did not request conversion, preserve the dominant system and flag the inconsistency.

## Source ledger

Create a ledger for every materially used source. Record only verified information:

* author or responsible organization
* title and subtitle
* container, publication, repository, or platform
* publication, revision, or release date
* edition or version when material
* locator: page, section, paragraph, timestamp, slide, figure, table, item, or file path
* DOI, permalink, canonical URL, or stable internal link
* source type
* access date when useful for a changing or undated source
* retrieval status: retrieved in this task, supplied by the user, or not retrieved
* evidence notes: authority, currency, conflicts, and releasability

A supplied attachment counts as retrieved only if it is readable and actually inspected. A remembered source, unexplained cached value, or search-result snippet does not count.

## Execution protocol

Use retrieval, document-reading, and file-processing tools rather than memory:

1. Inspect the task instructions and identify the exact sources needed.
2. For ZIP, TAR, or similar archives, list members before reading payloads. Read only relevant members. Never execute extracted binaries, scripts, or installers, and never recursively unpack nested archives.
3. Prefer the main source document when a package contains references, tests, or ancillary files. Read companion patterns when they affect formatting.
4. For large sources, retrieve only relevant pages, sections, or members when supported. If a source is unreadable, try one alternate representation, then flag the limitation instead of guessing.
5. Persist the source ledger through drafting and verification.
6. Inspect the final artifact for broken notes, links, headings, tables, source sections, and unsupported citation mechanics.

## Source integrity and validation

Never invent an author, title, date, publisher, edition, version, locator, DOI, URL, or repository identifier.

Every DOI, URL, page, date, and locator printed in the deliverable must trace to a source actually retrieved or supplied for this task. If a field cannot be verified, retrieve the source, omit fields CMOS permits you to omit, or retain the identifiable citation with `[unverified — confirm before publication]` when the uncertainty affects retrieval or attribution.

Never use a search-result snippet, AI summary, citation aggregator, or secondary reference as a substitute for an accessible underlying source. Prefer source metadata over snippets, DOI over generic URL, and canonical document URL over search-result or tracking URL. Deduplicate alternate links or versions unless distinct editions or versions are materially cited.

Validate the source separately from the citation. Confirm that the source supports the claim, the locator points to the relevant passage, the source is fit for the claim, and quotations are exact. For vendor-specific claims, prefer official vendor documentation. When credible sources conflict, represent the disagreement or qualify the claim; do not silently choose one.

For restricted company sources, include only metadata appropriate to the intended audience. Do not expose confidential repository details or unreleasable claims in a customer-facing artifact.

## Select the citation system

* Use Author-Date when the user requests author-date, inline, in-text, or parenthetical citations, or when analytical, scientific, technical, or business prose has no stronger convention.
* Use Notes-Bibliography when the user requests footnotes, endnotes, notes, humanities-style documentation, or source commentary outside the running prose.
* Use the system already present in a consistent artifact unless the user explicitly requests a change.

Terminal headings:

* Author-Date: `References` by default.
* Notes-Bibliography: `Bibliography` by default.
* Use `Works Cited` only when explicitly required.

## Citation density

Use the least intrusive density that preserves traceability:

* Executive: cite material assertions and source-dependent conclusions.
* Standard: cite each materially sourced factual or interpretive claim. One citation may support a short, unambiguous cluster of consecutive sentences.
* Academic: cite substantive factual, analytical, and interpretive claims closely enough for a reader to trace the evidence without guessing.
* Forensic: use locator-level sourcing for nearly every material assertion, quotation, number, or contested interpretation.

Do not cite common knowledge, connective prose, or clearly labeled original analysis merely to create citation volume.

## Citation mechanics

### Author-Date

Use `(Chen 2024, 18–20)` or `Chen (2024, 18–20)`. Place citations before terminal punctuation unless grammar or a block quotation requires otherwise. Separate multiple works with semicolons and order them alphabetically by author or organization, then chronologically when useful.

Use `n.d.` when no date is available. For same-author, same-year works, assign `a`, `b`, and later letters after sorting the works by title, and use the same letters everywhere.

### Notes-Bibliography

Place superscript note numbers after punctuation. Use a full note on first citation and a shortened note thereafter. Use footnotes when the output format supports true footnotes; otherwise use endnotes or numbered notes.

### Terminal source section

Include every formally cited work and no uncited padding. Alphabetize by author surname or responsible organization; alphabetize no-author works by title, ignoring initial articles. Personal communications normally remain in notes or prose rather than the terminal list. If the user explicitly requires an exhaustive terminal list, add `Personal Communications Cited` after the bibliography.

## Output-format behavior

Adapt mechanics to the artifact. Do not simulate unsupported features:

* Markdown: use Markdown footnotes when supported; otherwise use numbered notes or author-date citations.
* HTML: use accessible linked note markers and backlinks when practical.
* DOCX: use true footnotes or endnotes when supported and hanging indents for terminal entries.
* PPTX: use concise on-slide citations or source markers plus full source slides or an appendix.
* Spreadsheet: use a `Sources` sheet, source columns, cell notes/comments, or an appropriate combination.
* Plain chat: use author-date parentheticals or numbered notes rather than pretending to create true footnotes.
* PDF: preserve the source document’s citation mechanics or those of the generating format; do not remove locators during conversion.

## Final verification gate

Do not deliver until all checks pass:

1. The selected citation system is consistent with the precedence rules.
2. Each materially sourced claim has an appropriate citation or note at the point of use.
3. Every citation or note resolves to the correct terminal entry, except allowed personal-communication handling.
4. Every terminal entry is cited and contains no invented metadata.
5. Same-author/same-year letters, heading choice, alphabetical order, title treatment, dates, locators, DOI/URL, and edition/version fields are consistent.
6. Any unresolved metadata, source conflict, releasability issue, or unverified locator is visible in a short `Source notes` section.

### Authorship and AI Assistance

**Author:** Michael Gray

**AI assistance:** Created with Dell SalesChat using an underlying LLM not exposed by the runtime.
