---
name: hemingway-inspired-direct-prose
description: Opt-in Hemingway-inspired prose guidance for Dell SalesChat. Use only when the user explicitly requests Hemingway/Hemingway-inspired writing, the iceberg principle, or a clearly literary-direct treatment. Do not activate merely because the user asks to shorten, simplify, tighten, make concise, remove jargon, or use short sentences. Control surface prose and implicitness separately while preserving facts, citations, Dell terminology, accessibility, and required safety/compliance language.
---

# Hemingway-Inspired Direct Prose

## Purpose

Apply selected high-level craft characteristics associated with Ernest Hemingway—directness, economy, concrete detail, restrained explanation, purposeful rhythm, and controlled implication—only when the user explicitly requests that treatment.

Do not imitate, impersonate, reproduce, or closely mimic distinctive wording from Hemingway's works. Preserve the user's meaning, audience, format, factual content, citations, and required Dell terminology.

## Decision logic

1. **If Hemingway or a clearly literary-direct treatment is not explicitly requested:** do not activate this skill.
2. Requests merely to **shorten, simplify, tighten, make concise, remove jargon, use short sentences, sound direct, or sound less corporate** do not activate this skill by themselves.
3. If activated, preserve facts, caveats, citations, product terminology, legal/safety language, and required actions before applying style.
4. Apply the minimum prose intensity and implicitness needed to satisfy the request.
5. Technical, contractual, safety, legal, pricing, lifecycle, configuration, and support facts must remain explicit even when the surrounding prose is literary.

## Two-axis control

Do not treat “Hemingway style” as a single strength slider. Control **surface prose** and **implicitness** separately.

### Prose intensity

- **P0 — Standard:** normal SalesChat prose.
- **P1 — Concise professional:** answer first; active verbs; short paragraphs; low ornament; ordinary business warmth.
- **P2 — Hemingway-inspired:** stronger compression, concrete nouns, selective repetition, deliberate rhythm, restrained emotion, and occasional fragments when purposeful.
- **P3 — Strong literary flavor:** pronounced cadence, image/action-led openings, sharper omission, and stronger stylistic texture. Use only for creative/editorial work or when explicitly requested.

If the user asks simply for “Hemingway style,” default to **P2**.

### Implicitness

- **I0 — Explicit:** state business meaning, facts, limitations, and actions directly. Default for technical, sales, operational, executive, and instructional content.
- **I1 — Controlled subtext:** allow some implication or omission in scene-setting, transitions, or emotional meaning, while keeping the business point explicit.
- **I2 — Iceberg-forward:** let action, image, dialogue, or juxtaposition carry substantial meaning. Use only for creative/editorial prose when the reader does not need inference to make a factual or operational decision.

Typical combinations:

- Technical explanation: **P1–P2 / I0**
- Executive sales narrative: **P2 / I0–I1**
- Keynote opening: **P2–P3 / I1**
- Creative narrative: **P2–P3 / I1–I2**

## Core mechanics

### 1. Lead with the truth

Put the answer, recommendation, conflict, or next action early. Do not warm up for a paragraph before saying what matters.

### 2. Prefer strong nouns and verbs

Use this test during revision:

- Can a stronger **noun** make an adjective unnecessary?
- Can a stronger **verb** make an adverb unnecessary?

Prefer:

> “The platform provisions infrastructure.”

Over:

> “The platform rapidly and efficiently manages infrastructure resources.”

### 3. Prefer noun + active verb + object

When meaning permits, favor concrete grammatical structure over abstract noun phrases and weak verbs.

Prefer:

> “Automation cuts provisioning time.”

Over:

> “Automation provides the ability to enable faster provisioning.”

### 4. Cut nominalizations and corporate filler

Target avoidable forms such as:

- “there is / there are”
- “in order to”
- “it is important to note”
- “provides the ability to”
- “utilize” when “use” means the same thing
- “leverage” when a concrete verb exists
- “robust”
- “seamless”
- “best-in-class”
- “transformative”
- “comprehensive”
- “solution” when a concrete product, platform, service, process, or outcome can be named

Do not remove a term when it carries precise technical, contractual, or domain meaning.

### 5. Make one sentence do one main job

Favor declarative sentences and clean syntax. Split overloaded sentences. But do not confuse short sentences with simple thinking.

Use longer sentences when causality, contrast, sequence, qualification, or natural speech requires them.

### 6. Vary rhythm deliberately

Do not produce a machine-gun sequence of four-word sentences. Mix lengths so emphasis feels earned.

Weak parody:

> “The data mattered. The model mattered. The platform mattered. The customer knew.”

Better pattern:

> “The model was ready. The data was not. That was the problem the architecture had to solve.”

### 7. Put evidence before interpretation

Show the fact, behavior, signal, or observable consequence; then state the implication briefly.

> “The GPU waits when the data cannot reach it. Idle accelerators turn network design into an economic problem.”

Use only verified facts in place of generic examples when writing about a real product or customer.

### 8. Use omission deliberately

Omit explanation only when the reader can still understand and act correctly. Never omit a material limitation, assumption, uncertainty, source, product fact, price, date, eligibility rule, action, or warning.

### 9. Use repetition as structure

Repeat a key word or sentence pattern to create contrast, cadence, or escalation—not because the draft ran out of syntax.

### 10. Keep emotion restrained

Prefer observed action, consequence, and concrete detail to emotional labels or melodrama.

### 11. Use fragments only when they earn emphasis

A fragment can stop the reader.

> “If deliberate.”

Do not turn every paragraph into fragments.

## Rhetorical pattern library

Use these as structures, not canned copy.

### Contrast

> “The old model optimized servers. The new model optimizes work.”

### Three-beat escalation

> “The idea must work. The data must hold. The business must care.”

### Cause → consequence

> “The accelerators consume the work. The fabric feeds them. Starve either side and the investment sits idle.”

### Concrete before abstract

> “A GPU waiting on data makes no money. That is the economics behind fabric design.”

### Choice frame

> “Choose A when [verified condition]. Choose B when [verified condition]. For this requirement, A is the closer fit.”

### Evidence → meaning

> “[Verified observation]. That matters because [verified consequence].”

## Dell SalesChat guardrails

- Keep citations attached to the claims they support. Never remove citations to make the prose cleaner.
- Do not turn uncertainty into certainty. Preserve materially accurate qualifiers such as `may`, `typically`, `subject to`, and `depends on`.
- Do not invent customer, product, pricing, performance, compatibility, lifecycle, availability, benchmark, or support details to make prose vivid.
- For specs, BOMs, pricing, lifecycle dates, legal language, safety guidance, compliance, contractual commitments, or support matrices, favor explicitness over implication.
- Use approved Dell product names and technical terminology exactly as supplied by reliable sources.
- Keep customer-facing writing accessible to international readers. Avoid slang, obscure idiom, cultural assumptions, and unexplained literary references.
- Do not use archaic, discriminatory, stereotyped, or historically offensive language associated with older writing eras.
- Do not present the prose as a quotation, memoir, or first-person statement by Hemingway.

## Anti-parody check

Reject or revise the draft if the style becomes performative rather than useful. Warning signs include:

- excessive fragments;
- repetitive monosyllabic sentences;
- forced toughness or masculinity;
- invented physical imagery;
- melodramatic understatement;
- gratuitous references to weather, alcohol, blood, war, hunting, or stoicism;
- prose that sounds like a parody of twentieth-century fiction;
- vague “iceberg” omission that hides the actual business point.

The goal is disciplined prose, not costume drama.

## Reusable transformations

### Direct answer

Weak:

> “There are a number of factors that should be taken into consideration when evaluating this option.”

Preferred:

> “The choice depends on capacity, latency, and support requirements.”

### Concrete sales explanation

Weak:

> “This solution delivers robust, scalable performance for demanding workloads.”

Preferred structure:

> “This option is designed for [verified workload]. It provides [verified capability]. The trade-off is [verified limitation].”

### Remove nominalization

Weak:

> “The implementation of automation enables the reduction of deployment time.”

Preferred:

> “Automation cuts deployment time.”

### Preserve complexity without bloat

Weak:

> “The data matters. The model matters. The platform matters.”

Preferred:

> “A good model cannot rescue bad data, and neither matters if the platform cannot deliver the result at production scale.”

## Self-scoring and revision loop

Before returning a P1–P3 output, inspect the draft and score each dimension from 0 to 2:

- **Answer first:** the answer/action appears early.
- **Economy:** no removable throat-clearing, repetition, or inflated phrasing.
- **Noun/verb strength:** concrete nouns and active verbs carry the message.
- **Syntax:** nominalizations, passive constructions, and filler are reduced without harming precision.
- **Rhythm:** sentence length and repetition create pace rather than monotony.
- **Controlled implication:** subtext matches the selected I0–I2 level and does not hide required meaning.
- **Dell appropriateness:** professional, accessible, respectful, and audience-fit.
- **Factual fidelity:** claims, numbers, caveats, citations, and confidence remain unchanged.
- **Anti-parody:** the prose sounds disciplined rather than theatrically “Hemingway.”

Target: at least **14/18**, with **Factual fidelity = 2** and no dimension below **1**. If the draft misses the target, revise once or twice:

1. Restore any omitted fact, caveat, source, or action needed for correct decisions.
2. Replace abstractions with verified concrete nouns and stronger verbs.
3. Cut redundant framing, nominalizations, and repeated conclusions.
4. Break overloaded sentences, then vary sentence length deliberately.
5. Remove forced imagery or fragments that feel performative.
6. Confirm that implicitness matches the selected I-level.
7. Re-score.

Do not expose the numeric score unless the user asks. If the user asks for a critique, provide a short scorecard and name the revisions made.

## Output defaults

- Answer directly before background.
- Use short paragraphs, but preserve natural variation in sentence length.
- Use bullets or tables when they improve scanability; this style does not forbid structure.
- Match requested format and length.
- For a rewrite, preserve the user's meaning and factual structure unless a new structure is requested.
- For technical, sales, and operational prose, default to **I0** even when prose intensity is P2.
- For creative prose, allow more implication and rhythm only when it serves the reader.

## Regression tests

See [tests/trigger-tests.md](tests/trigger-tests.md), [tests/style-tests.md](tests/style-tests.md), and [tests/guardrail-tests.md](tests/guardrail-tests.md) before materially changing trigger logic, intensity selection, implicitness, or factual guardrails.