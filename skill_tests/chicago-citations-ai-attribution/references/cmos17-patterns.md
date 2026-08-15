
## 2. `chicago-citations-ai-attribution/references/cmos17-patterns.md`

```markdown
# CMOS 17 Citation Patterns

Use these as compact patterns, not as permission to fabricate missing fields. Adapt punctuation and fields to the actual source and selected Chicago system.

## Author-Date system

### In-text patterns

- One author: `(Smith 2020, 45)`
- Two authors: `(Smith and Jones 2020, 45–47)`
- Four or more authors: `(Smith et al. 2020, 45)`
- Organization: `(Dell Technologies 2025, 12)`
- Multiple works: `(Chen 2021, 8; Smith 2020, 45)`
- No date: `(Smith n.d., sec. 2)`
- No author: `("Shortened Title" 2023)`
- Same author/year: `(Smith 2024a, 12; Smith 2024b, 7)`

### Reference-list forms

Book:

`Surname, First Name. Year. Title of Book. Edition. Place: Publisher. DOI or URL.`

Journal article:

`Surname, First Name. Year. “Article Title.” Journal Title volume (issue): page range. https://doi.org/...`

Webpage:

`Author or Organization. Year. “Page Title.” Site Name. Month Day. URL.`

Internal company document:

`Author or Organization. Year. “Document Title.” Repository or Platform. Month Day. Stable internal URL.`

## Notes-Bibliography system

### First notes

Book:

`1. First Name Surname, Title of Book (Place: Publisher, Year), page.`

Journal article:

`2. First Name Surname, “Article Title,” Journal Title volume, no. issue (Year): cited page, https://doi.org/... .`

Webpage:

`3. Author or Organization, “Page Title,” Site Name, Month Day, Year, URL.`

Internal company document:

`4. Author or Organization, “Document Title,” Repository or Platform, Month Day, Year, cited locator, stable internal URL.`

### Shortened notes

- `5. Surname, Shortened Book Title, page.`
- `6. Surname, “Shortened Article Title,” page.`
- `7. Organization, “Shortened Document Title,” locator.`

### Bibliography forms

Book:

`Surname, First Name. Title of Book. Edition. Place: Publisher, Year. DOI or URL.`

Journal article:

`Surname, First Name. “Article Title.” Journal Title volume, no. issue (Year): page range. https://doi.org/... .`

Webpage:

`Author or Organization. “Page Title.” Site Name. Month Day, Year. URL.`

Internal company document:

`Author or Organization. “Document Title.” Repository or Platform. Month Day, Year. Stable internal URL.`

## Common source types

### Chapter in an edited book

- Author-Date: `Surname, First Name. Year. “Chapter Title.” In Book Title, edited by Editor Name, page range. Place: Publisher.`
- Bibliography: `Surname, First Name. “Chapter Title.” In Book Title, edited by Editor Name, page range. Place: Publisher, Year.`

### Report or white paper

Treat the named person or organization as author. Include report title, report number when present, issuing body, date, and DOI/URL.

### Presentation or slide deck

Include presenter or organization, presentation title, format/event, date, and stable URL. Use slide numbers as citation locators.

### Video or webinar

Include creator/presenter, title, platform/event, date, duration when useful, and URL. Use timestamps as locators.

### Dataset

Include creator, dataset title, version, repository/publisher, year, and DOI/URL.

### Standards, RFCs, and specifications

Include standards body or author, document identifier/number, title, edition/version when present, date, publisher/standards body, and DOI or canonical URL. Use section/clause numbers as locators when possible.

### Statutes, regulations, and court cases

Follow jurisdiction-specific Chicago/legal conventions rather than forcing a generic book/article pattern. Preserve official reporter, code, docket, regulation, section, court, and date information as applicable. When a legal citation standard is required by the institution, follow that standard instead of Chicago's general pattern.

### Government and legislative documents

Include responsible body, title, document/report number, congress/session or agency series when relevant, date, publication office/repository, and persistent URL.

### SEC filings and corporate regulatory filings

Include company, filing type, filing date, reporting period if material, regulator/database, and canonical filing URL. Use page, item, section, or exhibit locators.

### Earnings calls and investor presentations

Include company, event title/type, date, participant or speaker when relevant, transcript/presentation platform, and stable URL. Use page/slide or transcript section/timestamp where available.

### Conference paper or proceedings contribution

Include author, paper title, conference title, location when relevant, conference dates/year, proceedings/publisher when applicable, page range, DOI, or stable URL.

### Preprint / arXiv

Include author, year, title, repository, identifier/version, and DOI or canonical repository URL. Do not describe a preprint as peer reviewed unless independently verified.

### Patent

Include inventor(s), patent title, jurisdiction and patent number, filing/publication/grant date as appropriate, assignee when useful, and official patent URL.

### Software package or application

Include creator/organization, software title, version materially used, year/date, publisher/repository, and DOI/URL when available. Cite documentation separately when it supplies the claim.

### Git repository / source code

Include author/organization, repository title, version/release/tag or commit hash materially used, hosting platform, date/year if available, and stable repository/release/commit URL. Use file path and line numbers as locators when stable and useful.

### API or technical documentation

Include organization/author, page or endpoint-documentation title, product/documentation set, version when material, date or `n.d.`, and canonical URL. Use section headings or endpoint names as locators.

### AI model, model card, or system card

Prefer the model/system card or official documentation rather than a marketing page. Include responsible organization, model/system name, version/release identifier if verified, document title, date, and canonical URL. Distinguish the model itself from a paper describing it.

### AI-generated material

When institutional policy requires citation of AI output, identify the AI system/provider, model/version only when verified, description or prompt context appropriate to the audience, date of interaction, and retrievability status. Do not invent a share URL or model version. Follow the institution's AI-disclosure rule when it supersedes generic CMOS practice.

### Podcast episode

Include host/creator, episode title, podcast title, publisher/network if relevant, date, duration when useful, platform, and URL. Use timestamps as locators.

### YouTube or hosted transcript

Cite the original video when the transcript merely represents it. If a separately published transcript is itself the source, cite the transcript as a webpage/document and identify the underlying event/video when helpful.

### Image, artwork, photograph, or map

Include creator/cartographer/organization, title or descriptive label, date, medium/type, collection/institution or publisher, accession/catalog number when useful, and stable URL. Cite the source of the digital reproduction separately when material.

### Archival document

Include creator, document title/description, date, collection, box/folder/item identifiers, repository, and location. Use the archive's stable digital identifier or URL when available.

### Email, direct message, interview, or meeting conversation

CMOS normally cites unrecoverable personal communications in text or notes rather than the bibliography/reference list. For an explicit all-cited-sources requirement, add `Personal Communications Cited` and list speaker/sender, recipient or meeting context, communication type, and date, limited to details appropriate for the audience.

## Metadata exceptions

- No author: begin with the title.
- No date: use `n.d.` when appropriate.
- Continuously changing undated page: add an access date when it materially helps retrieval.
- DOI available: format as `https://doi.org/...` and prefer it to another URL.
- Same author and year in author-date: distinguish as `2024a`, `2024b`, and use the same letters in citations and References.
- Repeated author in a CMOS 17 bibliography/reference list: use a 3-em dash only when the target format reliably renders and sorts it; otherwise repeat the name for accessibility and data portability.
- Multiple authors: preserve source order. In terminal entries, invert only the first author's name unless the chosen CMOS pattern requires otherwise.
- Missing optional metadata: omit it rather than fabricate it.
- Conflicting metadata: prefer the source itself, then authoritative publisher/repository metadata; document material ambiguity when it affects identification.