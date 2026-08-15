---
name: chicago-citations-ai-attribution
description: Creates Chicago Manual of Style 17th Edition citations, notes, bibliographies or reference lists, source validation, and defensible AI/provenance attribution for research and artifacts. Use when the user explicitly requests Chicago/CMOS, footnotes, endnotes, author-date citations, bibliography/references, source attribution, or AI/LLM disclosure, or when an existing artifact already uses Chicago and must be preserved.
---

# Chicago Citations and AI Attribution

Apply Chicago Manual of Style, 17th Edition, consistently to the final deliverable. Treat evidence quality, citation correctness, and AI provenance as separate validation problems.

## Decision logic

1. **If no trigger is present:** do not impose Chicago formatting or visible AI attribution merely because sourced content exists.
2. **If an existing artifact already uses Chicago:** preserve its citation system, heading conventions, and note style unless the user asks to change them.
3. **If the user requests Chicago but not a system:** select Notes-Bibliography for humanities-style work and source commentary; select Author-Date when evidence is cited directly in analytical or scientific prose.
4. **If the user explicitly names a system or institutional convention:** follow it even when another system would normally be preferred.
5. **Never sacrifice source accuracy to achieve citation completeness.** If metadata is incomplete, create the most complete defensible citation permitted by CMOS and flag only uncertainty that prevents identification, retrieval, or accurate attribution.

Read [references/cmos17-patterns.md](references/cmos17-patterns.md) when formatting citations, notes, bibliography entries, reference-list entries, or specialized source types.

## Workflow

### 1. Build a source ledger

For every materially used source, record what is available:

- author(s) or responsible organization
- title and subtitle
- container/publication/repository
- publication or revision date
- edition/version
- page, section, paragraph, timestamp, slide, figure, table, or other locator
- DOI, permalink, canonical URL, or stable internal link
- source type
- access date when CMOS or retrievability makes it useful
- evidence-quality notes when authority, currency, or provenance matters

Do not use search-result snippets, AI summaries, citation aggregators, or secondary references as substitutes for an accessible underlying source.

### 2. Validate the source before formatting it

Source validation asks whether the evidence supports the prose. Citation validation asks whether the citation is formatted correctly. Perform both.

For each material source, verify when practical:

- the source actually supports the claim attributed to it;
- the cited locator points to the relevant passage, figure, table, slide, or timestamp;
- the source is authoritative enough for the claim;
- the source is current enough for a time-sensitive claim;
- quoted text is exact and clearly distinguished from paraphrase;
- vendor documentation supports vendor-specific claims rather than being treated as neutral evidence for broader claims.

### 3. Prefer stronger evidence

When multiple sources are available, prefer approximately this hierarchy unless the task calls for another type of evidence:

1. Primary documents, official records, standards, and original data.
2. Peer-reviewed research and authoritative scholarly works.
3. Government, standards-body, university, or institutional publications.
4. Vendor primary documentation for vendor-specific product, architecture, lifecycle, or policy claims.
5. High-quality journalism and established secondary analysis.
6. Reputable trade publications and professional analysis.
7. Blogs, forums, social posts, aggregators, and informal commentary only when they are themselves the evidence or stronger sources are unavailable.

Do not upgrade a weak source merely because it has complete citation metadata.

### 4. Choose the Chicago system

- **Author-Date:** requests for author-date, inline, in-text, or parenthetical Chicago citations.
- **Notes-Bibliography:** requests for footnotes, endnotes, notes, humanities-style documentation, or source commentary outside the running prose.
- Preserve an existing artifact's system unless instructed otherwise.
- Do not mix the two systems unintentionally.

### 5. Choose citation density

Use the least intrusive density that preserves traceability. If the user specifies a density, follow it.

- **Executive:** cite material assertions and source-dependent conclusions, consolidating citations where the relationship is clear.
- **Standard:** cite each materially sourced factual or interpretive claim; one citation may support a short cluster of consecutive sentences when unambiguous.
- **Academic:** cite substantive factual, analytical, and interpretive claims closely enough for a reader to trace the evidence without guessing.
- **Forensic:** use locator-level sourcing for nearly every material assertion, quotation, number, or contested interpretation.

Do **not** cite common knowledge, purely connective prose, the author's own clearly identified analysis, or conclusions that merely synthesize already cited premises unless the conclusion introduces a new source-dependent assertion.

### 6. Cite at the point of use

- Add page, section, paragraph, timestamp, slide, figure, table, or other locator when available and useful.
- Keep citations close enough to the supported claim that attribution is unambiguous.
- When several consecutive sentences depend on the same source, one citation may support the group if no intervening source or claim creates ambiguity.
- Preserve required runtime provenance markers separately from human-readable Chicago citations.

### 7. Create the correct terminal source section

- **Notes-Bibliography:** use `Bibliography` unless the user or institution requires another heading.
- **Author-Date:** use `References` or `Reference List`; prefer `References` unless an existing artifact specifies otherwise.
- Include every formally cited work and no uncited padding.
- Alphabetize by author surname or responsible organization; alphabetize no-author works by title, ignoring initial articles.
- Personal communications normally remain in text or notes. If the user explicitly requires every cited source to appear in a terminal list, add `Personal Communications Cited` after the bibliography or references.

### 8. Validate both directions

Before delivery:

- every citation or note maps to the correct source entry;
- every bibliography/reference entry is cited, except explicitly separated personal communications or source lists requested for another purpose;
- author names, years, title forms, editions, and locators agree across citations and source entries;
- same-author/same-year disambiguation is consistent;
- URLs and DOIs identify the source actually used.

## Citation behavior

### Author-Date

Use parenthetical citations such as `(Chen 2024, 18–20)` or integrate the author into the sentence as `Chen (2024, 18–20)`. Place the citation before terminal punctuation unless grammar or a block quotation requires otherwise. Separate multiple sources with semicolons and order them consistently.

Use `References` as the terminal heading by default.

### Notes-Bibliography

Insert superscript note numbers after punctuation. Use a full note on first citation and a shortened note thereafter unless the artifact or publishing system requires another convention. Use footnotes by default when the output format supports true footnotes; otherwise use endnotes or another faithful note representation.

Use `Bibliography` as the terminal heading by default.

## Output-format intelligence

Adapt the citation mechanics to the artifact rather than simulating capabilities the format does not reliably support.

- **DOCX:** use true footnotes/endnotes when supported; apply hanging indents to bibliography/reference entries.
- **HTML:** use linked note markers and backlinks when practical; keep source links accessible.
- **Markdown:** use Markdown footnotes when the renderer supports them; otherwise use numbered notes.
- **PPTX:** use concise on-slide citations or source markers and one or more full source slides/appendix pages; avoid dense footnotes that become unreadable.
- **Spreadsheet:** use a dedicated `Sources` sheet, source columns, cell notes/comments, or a combination appropriate to the workbook.
- **Plain chat/text:** prefer author-date parentheticals or numbered notes rather than pretending to create real footnotes.
- **PDF:** preserve the citation mechanics of the source document or generating format; do not degrade locators during conversion.

## Source integrity

- Never invent an author, date, title, publisher, page, DOI, URL, model name, model version, repository, or edition.
- Prefer metadata from the source itself over snippets or third-party citation pages.
- Use the most specific stable locator available: DOI before a generic URL; canonical document link before a search-results link.
- Deduplicate alternate links or versions of the same work unless distinct editions/versions are materially cited.
- Use `n.d.` only when no date is available and CMOS permits it.
- Preserve non-English titles, capitalization conventions, names, and diacritics accurately.
- For restricted company sources, include only metadata appropriate for the artifact's intended audience; do not expose confidential repository details unnecessarily.
- If metadata remains incomplete, omit fields CMOS permits to be omitted rather than guessing.

## Bibliography/reference quality check

Verify:

- names and author order;
- title capitalization and italics/quotation marks;
- publication/container information;
- edition/version where material;
- dates;
- page ranges or locators;
- DOI/URL correctness;
- hanging indents when supported;
- alphabetical order;
- correct terminal heading for the selected Chicago system.

## AI and provenance attribution

Visible AI attribution is **not automatically required for every artifact**. Add visible disclosure when:

- the user requests it;
- institutional, academic, company, or publication policy requires it;
- the artifact's purpose is to document AI assistance or provenance; or
- the existing artifact already contains a provenance block that should be preserved or updated.

Otherwise, do not clutter customer-facing or executive artifacts with visible AI disclosure solely because this skill was used. When supported and useful, provenance may instead be retained in document metadata, notes, an appendix, repository metadata, or a dedicated provenance record.

When visible attribution is required, use an appropriate form such as:

```markdown
---

### Authorship and AI Assistance

**Author:** [verified active user's full name or `SalesChat user`]

**AI system:** Dell SalesChat

**Model:** [verified exact model/version, verified family, or `underlying LLM not exposed by the runtime`]

**Research/tools:** [material search, retrieval, connector, code, or artifact-generation tools when disclosure is requested or policy requires it]

**Generated:** [verified date/time when appropriate]

**Last materially revised:** [verified date/time when appropriate]