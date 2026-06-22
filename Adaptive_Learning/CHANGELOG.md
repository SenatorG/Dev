# CHANGELOG — Myhill Adaptive Learning Coach

## v2.8 — 2026-03-30

### Summary

Bug fix: Enablement Session (and potentially Collateral) evaluations were being skipped due to guard clause context contamination. When Step 4 fired its guard clause for a non-Customer-Conversation input, its output text — "[Detected scenario type] detected — evaluation produced in the applicable section." — was misread by subsequent steps as evidence that the evaluation had already been completed, causing them to fire their own guard clauses and skip the actual evaluation.

### Problem

When a user submitted an enablement/internal transcript:

1. Step 3 correctly classified the input as "Enablement Session"
2. Step 4 (Customer Conversation) correctly fired its guard clause, outputting: "Enablement Session detected — evaluation produced in the applicable section."
3. Step 5 (Enablement Session) read Step 4's output, interpreted "evaluation produced in the applicable section" as meaning the enablement evaluation was already done, and fired its own guard clause — skipping the evaluation entirely

The same bug could affect Collateral inputs (Steps 4 and 5 both outputting "Collateral detected — evaluation produced..." could cause Step 6 to skip).

### What Changed

#### Steps 4, 5, 6 — Guard clause output text reworded

Changed the guard clause output from:

> "[Detected scenario type] detected — evaluation produced in the applicable section."

To:

> "This step evaluates [Step's own scenario type] only — skipping. Input classified as [detected scenario type]."

The new wording makes each skipped step self-identify ("This step evaluates X only — skipping") so there is no ambiguity about what was or wasn't produced. The prior wording placed the detected scenario type at the front of the sentence followed by "evaluation produced," which downstream steps misread as a completed evaluation.

### Character Budget (v2.8)

| Step | Chars | Limit | Headroom |
|---|---|---|---|
| Step 0 (Read Document — User Input) | 0 | 8,000 | 8,000 |
| Step 1 (Think — Document Intake) | 307 | 8,000 | 7,693 |
| Step 2 (Read Document — Reference Rubric) | 206 | 8,000 | 7,794 |
| Step 3 (Think — Persona + Scenario Detection) | 6,022 | 8,000 | 1,978 |
| Step 4 (Respond — Customer Conversation) | 6,275 | 8,000 | 1,725 |
| Step 5 (Respond — Enablement Session) | 6,234 | 8,000 | 1,766 |
| Step 6 (Respond — Collateral) | 2,781 | 8,000 | 5,219 |
| Step 7 (Plan & Execute — Resource Bibliography) | 4,885 | 8,000 | 3,115 |

### Testing Notes

- **Primary test:** Submit an enablement/internal transcript. Verify Step 4 outputs "This step evaluates Customer Conversations only — skipping. Input classified as Enablement Session." and Step 5 produces the full enablement evaluation (not a skip message).
- **Collateral test:** Submit a collateral asset. Verify Steps 4 and 5 both output skip messages and Step 6 produces the full collateral evaluation.
- **Customer Conversation test:** Submit a customer transcript. Verify Step 4 produces the full evaluation and Steps 5 and 6 output skip messages. (Regression check — this path was working before.)
- **Step 7 context recovery:** Verify Step 7's bibliography still correctly identifies the active scenario from the evaluation output, not from skip messages.

---

## v2.7 — 2026-03-27

### Summary

Risk mitigation pass addressing P1 and P3 issues identified during agent review. Recovered ~1,500 chars of headroom in Steps 4 and 5 by merging duplicated EVALUATION METHOD + OUTPUT FORMAT sections. Added context recovery to Step 7 to route around Glean's Think-step context propagation bug. Improved guard clause UX, resolved a broken export promise, fixed guard rail step reference, added evidence rule anchors and persona anchors to all Respond steps for context propagation resilience, and resolved the deferred Chat Message Trigger question.

### What Changed

#### Steps 4 & 5 — Merged EVALUATION METHOD + OUTPUT FORMAT into EVALUATION & OUTPUT

The prior design described evaluation work twice: once as numbered method steps, once as output format sections. These mapped 1:1. Merged into a single EVALUATION & OUTPUT section where each output section is both the analysis task and the format directive. No evaluation criteria, competencies, or output sections were removed.

- **Step 4 (Customer Conversation):** 7,524 → 5,924 chars (+1,600 headroom)
- **Step 5 (Enablement Session):** 7,387 → 5,898 chars (+1,489 headroom)

#### Step 7 — Context recovery block added

Replaced `SCENARIO ROUTING / Refer to the scenario classification from Step 3` with `CONTEXT RECOVERY & SCENARIO ROUTING` that determines the active scenario by reading the user-visible Respond step outputs (Steps 4–6) rather than relying on Step 3's Think output, which can silently drop from Glean's context window.

- Scenario detection now checks for "produced a full scoring table" or "produced a full asset classification" in Respond outputs
- Extracts priority gaps, topics, and Top 3 Priorities from the active evaluation for targeted search queries
- Transparent fallback if all context is lost: "⚠️ Evaluation context was not available — the resources below are general Dell ISG materials, not tailored to your specific gaps. Re-run the evaluation for targeted recommendations."
- **Step 7:** ~3,950 → 4,885 chars (3,115 headroom remaining)

#### Steps 4, 5, 6 — Guard clause output improved

Changed guard clause output from `"N/A — see applicable scenario evaluation."` to `"[Detected scenario type] detected — evaluation produced in the applicable section."` — honest, directional, and less likely to confuse users who see two non-active Respond steps fire.

#### Steps 4, 5, 6 — Removed export offer

Removed "Close by asking if the user would like an exportable document for their manager or mentor." from all three Respond steps. Glean re-enters the flow from the top on every user message (rule #7), so a "yes" response would restart the evaluation flow rather than produce an export. Eliminates a broken promise.

#### Step 3 — Rubric precedence rule added

Added: "If the reference rubric from Step 2 provides more detailed or conflicting criteria for a level, defer to the Step 2 rubric as the authoritative source. Use the definitions below as fallback only." Resolves dual-source conflict between the SharePoint rubric (Step 2) and the inline rubric definitions (Step 3), while preserving the inline definitions as a fallback if the SharePoint URL breaks.

- **Step 3:** 5,830 → 6,022 chars (1,978 headroom)

#### Step 3 — Guard rail step reference fixed

Changed "If no document content was loaded in the previous step" to "If no document content was loaded in Steps 0 or 1." The prior wording referenced "the previous step" which is Step 2 (the SharePoint rubric loader) — meaning the guard rail would never trigger since Step 2 always loads content.

#### Steps 4, 5, 6 — Evidence rule anchors added

Added anti-inflation rules directly to each Respond step's EVALUATION & OUTPUT section: "Score only what is observable — if no evidence exists for a competency, mark N/A. Do not inflate: 101 with flashes of 201 is 101." Previously these rules existed only in Step 3 (Think), which can silently drop from Glean's context window. Now enforced redundantly in every evaluation step.

#### Steps 4, 5, 6 — Persona anchors added

Added a one-line persona anchor to each Respond step: "You are an Executive Coaching Assessor — a Senior Sales Coach and Executive Buyer Proxy. Score against the rubric, not vibes." Previously the full persona definition existed only in Step 3 (Think). If Think output dropped from context, the Respond steps had tone directives but no evaluator identity. Now the core persona survives independently.

#### Resolved — Chat Message Trigger question (deferred since v2.1)

Confirmed: no separate Chat Message Trigger is required. The Read Document step (Step 0) acts as the activation trigger when a user adds collateral and clicks continue. Updated the v2.1 changelog entry from "Deferred" to "Resolved (v2.7)."

### Character Budget (v2.7)

| Step | Chars | Limit | Headroom |
|---|---|---|---|
| Step 0 (Read Document — User Input) | 0 | 8,000 | 8,000 |
| Step 1 (Think — Document Intake) | 307 | 8,000 | 7,693 |
| Step 2 (Read Document — Reference Rubric) | 206 | 8,000 | 7,794 |
| Step 3 (Think — Persona + Scenario Detection) | 6,022 | 8,000 | 1,978 |
| Step 4 (Respond — Customer Conversation) | 6,181 | 8,000 | 1,819 |
| Step 5 (Respond — Enablement Session) | 6,155 | 8,000 | 1,845 |
| Step 6 (Respond — Collateral) | 2,741 | 8,000 | 5,259 |
| Step 7 (Plan & Execute — Resource Bibliography) | 4,885 | 8,000 | 3,115 |

### Testing Notes

- **Guard clause UX:** Submit each scenario type and verify the two non-active Respond steps output "[Scenario] detected — evaluation produced in the applicable section." with no additional content.
- **Context recovery:** Verify Step 7's bibliography references specific gaps from the evaluation, not generic Dell resources. If possible, test with a long evaluation that might stress Glean's context window.
- **Rubric precedence:** If the SharePoint rubric contains criteria that differ from Step 3's inline definitions, verify the evaluation follows the SharePoint version.
- **Merged EVALUATION & OUTPUT:** Verify output structure matches prior versions — same 6 sections in same order for Customer Conversation and Enablement Session. No sections dropped.
- **Export removal:** Verify Steps 4, 5, 6 no longer ask about exportable documents.
- **Guard rail:** Submit without a document and verify the agent returns the "I need a document to evaluate" message rather than attempting to evaluate the rubric.
- **Evidence anchors:** Compare scoring behavior with v2.6 — scores should not inflate. Look for N/A markings on competencies with no evidence.
- **Persona anchors:** Verify the evaluation tone remains direct and rubric-anchored across all three scenario types. Compare with v2.6 output for tone consistency.

---

## v2.6 — 2026-03-25

### Summary

Step 7 (Plan & Execute — Resource Index) updated to frame the output as a "curated resource bibliography in the style of the Chicago Manual of Style" instead of a "curated resource index." No changes to search logic, resource categories, formatting rules, staleness checks, or any other steps.

### What Changed

- **Step 7 opening line:** "curated resource index" → "curated resource bibliography in the style of the chicago manual of style"
- **Spacing:** Minor whitespace adjustments throughout Step 7 (no content impact)

### Character Budget (v2.6)

| Step | Chars | Limit | Headroom |
|---|---|---|---|
| Step 0 (Read Document — User Input) | 0 | 8,000 | 8,000 |
| Step 1 (Think — Document Intake) | 307 | 8,000 | 7,693 |
| Step 2 (Read Document — Reference Rubric) | 206 | 8,000 | 7,794 |
| Step 3 (Think — Persona + Scenario Detection) | 5,830 | 8,000 | 2,170 |
| Step 4 (Respond — Customer Conversation) | 7,524 | 8,000 | 476 |
| Step 5 (Respond — Enablement Session) | 7,387 | 8,000 | 613 |
| Step 6 (Respond — Collateral) | 2,525 | 8,000 | 5,475 |
| Step 7 (Plan & Execute — Resource Bibliography) | ~3,950 | 8,000 | ~4,050 |

### Testing Notes

- Verify the bibliography framing produces Chicago-style citations rather than a simple link list.
- All other behavior unchanged from v2.5.

---

## v2.5 — 2026-03-24

### Summary

Two feature additions: (1) Conversation/session flow and quality recommendations for transcript scenarios, and (2) a new Plan & Execute step that searches for and presents a Chicago-style resource index tailored to the evaluation results. Resources are categorized, annotated with evaluation-specific relevance, and flagged if older than 12 months.

### What Changed

#### New Step 7 — Plan & Execute (Resource Index)

Added a final step (Step 7) using Plan & Execute with both Brave web search and company corpus search enabled. This step reads the scenario classification from Step 3 and the evaluation output from Steps 4–6 to build a curated resource index.

**Scenario-aware search:**
- Transcripts (Customer Conversation / Enablement Session): searches for resources that address rubric gaps, flow/quality issues, and weak competency areas identified in the evaluation.
- Collateral: searches for resources that fill content gaps, complement the evaluated asset, and provide models at the next rubric level.

**Three resource categories:**
1. Customer-Facing Collateral — assets to deploy directly in customer engagements.
2. Internal-Use Collateral — enablement, learning paths, deep-dives for the user's own development.
3. External References — public Dell resources, analyst materials, industry frameworks.

**Chicago-style format:** Each entry includes author (if available), resource title with inline clickable URL, source/platform, date, and a 1-sentence annotation tying the resource to a specific evaluation finding.

**Staleness check:** Resources with a visible publication or last-modified date older than 12 months are prefixed with "⚠️ OLDER COLLATERAL — PLEASE VERIFY". No date = no label (no guessing).

**Guard rails:** No fabricated resources (search-found only), 5–10 resources total, Dell internal prioritized over generic external, "No additional resources found" when search returns limited results.

#### Flow & Quality sections (carried from v2.4 draft)

Details below under the v2.4 heading — these changes were developed in the same session.

### Character Budget (v2.5)

| Step | Chars | Limit | Headroom |
|---|---|---|---|
| Step 0 (Read Document — User Input) | 0 | 8,000 | 8,000 |
| Step 1 (Think — Document Intake) | 307 | 8,000 | 7,693 |
| Step 2 (Read Document — Reference Rubric) | 206 | 8,000 | 7,794 |
| Step 3 (Think — Persona + Scenario Detection) | 5,830 | 8,000 | 2,170 |
| Step 4 (Respond — Customer Conversation) | 7,524 | 8,000 | 476 |
| Step 5 (Respond — Enablement Session) | 7,387 | 8,000 | 613 |
| Step 6 (Respond — Collateral) | 2,525 | 8,000 | 5,475 |
| Step 7 (Plan & Execute — Resource Index) | 3,914 | 8,000 | 4,086 |

### Testing Notes

- Verify that search results are relevant to the specific gaps identified in the evaluation, not generic Dell resources.
- Verify that inline links are clickable and resolve correctly (especially company corpus links).
- Verify the staleness label appears on older resources and does not appear when no date is available.
- Check that the resource index distinguishes between transcript and collateral scenarios (different search focus, different annotation framing).
- Steps 4 and 5 remain tight on headroom (476 and 613 chars). Future additions require trimming.

---

## v2.4 — 2026-03-24

### Summary

Feature addition: Conversation/session flow and quality recommendations for both transcript scenarios (Customer Conversation and Enablement Session). User-requested feature — the agent now analyzes how the discussion moved as a whole and provides specific recommendations to improve flow, pacing, and conversational control in a way that directly impacts rubric scores. Collateral evaluation is unchanged.

### What Changed

#### New evaluation step and output section in Steps 4 and 5

**Customer Conversation (Step 4):**
- Evaluation Method: New step 7 — "Conversation Flow & Quality." Analyzes overall discussion structure: where the conversation built momentum, where it stalled or lost direction. Provides specific recommendations for pacing, transitions, topic sequencing, and conversational control, each tied to a transcript moment.
- Output Format: New Section 5 — "Conversation Flow & Quality." Structured as: current flow issue → recommended change → expected rubric impact. Links each recommendation to the competency it would improve.
- Top 3 Priorities moved from Section 5 → Section 6.

**Enablement Session (Step 5):**
- Evaluation Method: New step 7 — "Session Flow & Quality." Analyzes overall session structure: where the session built understanding and engagement, where it stalled or became one-way lecture. Provides specific recommendations for pacing, topic transitions, audience engagement timing, and facilitation control, each tied to a session moment.
- Output Format: New Section 5 — "Session Flow & Quality." Same structured format as Customer Conversation, adapted for teaching context.
- Top 3 Priorities moved from Section 5 → Section 6.

**Collateral (Step 6):** No changes.

### Character Budget (v2.4)

| Step | Chars | Limit | Headroom |
|---|---|---|---|
| Step 0 (Read Document — User Input) | 0 | 8,000 | 8,000 |
| Step 1 (Think — Document Intake) | 307 | 8,000 | 7,693 |
| Step 2 (Read Document — Reference Rubric) | 206 | 8,000 | 7,794 |
| Step 3 (Think — Persona + Scenario Detection) | 5,830 | 8,000 | 2,170 |
| Step 4 (Respond — Customer Conversation) | 7,524 | 8,000 | 476 |
| Step 5 (Respond — Enablement Session) | 7,387 | 8,000 | 613 |
| Step 6 (Respond — Collateral) | 2,525 | 8,000 | 5,475 |

### Testing Notes

- Steps 4 and 5 are now tight on headroom (476 and 613 chars respectively). Future additions to these steps will require trimming existing content.
- Verify that the new Section 5 output is distinct from Missed Opportunities (Section 3) and Key Moments (Section 2) — flow analysis should focus on the mechanics of how the conversation moved, not rehash individual moments.
- Verify that rubric impact links in the flow recommendations are specific (e.g., "improves A2 Discovery & Synthesis from 201→301") rather than generic.

---

## v2.3 — 2026-03-24

### Summary

Structural fix: Read Document steps in Glean cannot have accompanying instruction text. Moved Step 0's document intake instructions into a new Think step, shifting all subsequent steps down by one.

### What Changed

#### Architecture: 6 steps → 7 steps

| | v2.2 | v2.3 |
|---|---|---|
| Total steps | 6 (Steps 0–5) | 7 (Steps 0–6) |
| Read Document steps | 2 (Steps 0, 1) | 2 (Steps 0, 2) |
| Think steps | 1 (Step 2) | 2 (Steps 1, 3) |
| Respond steps | 3 (Steps 3, 4, 5) | 3 (Steps 4, 5, 6) |

#### Step-by-step breakdown (v2.3)

- **Step 0 — Read Document (User Input):** No instruction text (Glean constraint — Read Document steps cannot have accompanying instructions).
- **Step 1 — Think (Document Intake):** Instruction text previously in Step 0. Identifies URLs/file links from user message, retrieves content via Glean Document Reader, or flags that no documents were loaded.
- **Step 2 — Read Document (Reference Rubric):** Unchanged. Loads 101-401 reference rubric from SharePoint.
- **Step 3 — Think (Persona + Scenario Detection):** Unchanged from v2.2 Step 2. Persona definition, auto-detect scenario, sales stage, rubric levels, evidence rules.
- **Step 4 — Respond (Customer Conversation):** Unchanged from v2.2 Step 3. Guard clause references Step 3 (was Step 2).
- **Step 5 — Respond (Enablement Session):** Unchanged from v2.2 Step 4. Guard clause references Step 3 (was Step 2).
- **Step 6 — Respond (Collateral):** Unchanged from v2.2 Step 5. Guard clause references Step 3 (was Step 2).

### Glean Constraint Discovered

**Read Document steps cannot have instruction text.** The Glean Agent Builder does not allow accompanying instructions in Read Document step types. Any processing instructions for retrieved documents must go in a separate Think step.

### Testing Notes

- No content changes — this is a structural reorganization only. All evaluation logic, competencies, guard clauses, and output formats are identical to v2.2.
- Verify that the Think step (Step 1) correctly processes the document content retrieved by Step 0.

---

## v2.2 — 2026-03-24

### Summary

Split the single Respond step into 3 scenario-specific Respond steps to fix scenario bleed, deepen feedback for Customer Conversations and Enablement Sessions, and focus Collateral evaluation on practical utility.

### Problem

In testing, a Customer Conversation transcript was scored using Collateral competencies (B3 Champion Enablement Assets, C1 Customer-Facing Collateral, C2 Competitive/Objection Collateral). The v2.1 instruction "Apply ONLY the competency set matching the detected scenario type" was not being followed — the LLM mixed evaluation frameworks because all three were visible in a single step.

### What Changed

#### Architecture: 4 steps → 6 steps

| | v2.1 | v2.2 |
|---|---|---|
| Total steps | 4 | 6 |
| Respond steps | 1 (all scenarios) | 3 (one per scenario) |
| Scenario isolation | Instruction-based ("apply ONLY...") | Structural (hard guard clause per step) |

#### Step-by-step breakdown (v2.2)

- **Step 0 — Read Document:** Unchanged. Ingests user-provided document.
- **Step 1 — Read Document:** Unchanged. Loads 101-401 reference rubric.
- **Step 2 — Think:** Minor update — classification now explicitly notes it determines which evaluation step (3, 4, or 5) activates. Multi-type classification activates multiple steps.
- **Step 3 — Respond (Customer Conversation):** Guard clause + expanded evaluation. New sections: Key Moments (3-5 specific moments with commentary), Missed Opportunities (what should have been said/done), behavioral scripts in priorities. Competencies include look-fors and red flags per area.
- **Step 4 — Respond (Enablement Session):** Guard clause + expanded evaluation. New sections: Teaching Effectiveness (specific teaching moments), Monday Morning Test (will behavior actually change?), session design changes in priorities. Competencies include look-fors and red flags.
- **Step 5 — Respond (Collateral):** Guard clause + shorter, focused evaluation. Three sections only: Asset Classification (type, rubric level, sales stage), Strengths & Gaps, Best Use in Customer Conversations. No performance-review tone — practical tool assessment.

### Key Design Decisions

1. **Hard guard clauses** replace soft "apply ONLY" instructions. Each Respond step begins with: "If the scenario detected in Step 2 is not [X], respond with exactly: 'N/A — see applicable scenario evaluation.' and stop." This eliminates scenario bleed structurally.

2. **Customer Conversation and Enablement get deeper feedback:** Expanded evaluation method with specific moments, missed opportunities (conversations) / teaching effectiveness (enablement), and behavioral scripts. Output sections increased from 3 to 5.

3. **Collateral gets focused, shorter feedback:** Trimmed from full rubric evaluation to 3 practical sections — what level is it, what's good/missing, and exactly how to use it in customer conversations.

4. **Multi-type inputs preserved:** Guard clauses include "and does not include [X] as part of a multi-type classification" so ambiguous inputs still activate multiple evaluation steps.

### Character Budget (v2.2)

| Step | Chars | Limit | Headroom |
|---|---|---|---|
| Step 0 (Read Document — User Input) | 307 | 8,000 | 7,693 |
| Step 1 (Read Document — Reference Rubric) | 206 | 8,000 | 7,794 |
| Step 2 (Think) | 5,830 | 8,000 | 2,170 |
| Step 3 (Respond — Customer Conversation) | 6,448 | 8,000 | 1,552 |
| Step 4 (Respond — Enablement Session) | 6,189 | 8,000 | 1,811 |
| Step 5 (Respond — Collateral) | 2,525 | 8,000 | 5,475 |

### Testing Notes

- Glean executes all steps sequentially. Two of the three Respond steps will hit their guard clause and output only "N/A — see applicable scenario evaluation." Verify in-platform that the substantive evaluation is clearly surfaced and the N/A responses don't confuse the output.
- Retest with a Customer Conversation transcript to confirm no Collateral competencies appear.
- Test with a Collateral asset to confirm the shorter, focused format is useful.

---

## v2.1 — 2026-03-23

### Summary

Hardening pass on v2. Fixes 5 risks and gaps identified during review: collateral rubric alignment, empty-document guard rail, collateral stage inference, step numbering, and tone restoration.

### Fixes Applied

1. **Collateral rubric level overlays added:** Every rubric level (101–401) in the Think step now includes a "For collateral:" reframe alongside the existing "For enablement:" overlay. This ensures the LLM scores collateral against asset-quality criteria ("does this asset enable the user to operate at this level?") rather than person-performance criteria ("can this person do X?"). Previously the LLM had to bridge this mismatch on its own.

2. **Guard rail for empty document input:** Think step now checks whether document content was loaded. If no content is present, the agent responds with a request for a document link instead of attempting a hallucinated evaluation.

3. **Collateral-specific sales stage inference:** Added explicit mapping from asset types to sales process stages — discovery briefs/intro decks = Discovery, challenge/gap analysis = Analysis, blueprints/POV plans/demo scenarios = Design, battlecards/objection matrices/executive approval aids = Defend. Multi-stage assets are noted and evaluated across applicable stages.

4. **Step numbering corrected:** Fixed headers from 0, 2, 3, 4 → 0, 1, 2, 3 (Step 1 was skipped after removing Chat Message Triggers in the prior revision).

5. **Closing tone anchor restored:** "You are not here to be liked. You are here to make the next call, the next workshop, and the next POV materially better." added back to end of Respond step (had been cut during 8K character trimming in v2).

### Resolved (v2.7)

- **Chat Message Trigger question:** Confirmed — no separate trigger is required. The Read Document step (Step 0) acts as the trigger when a user adds collateral and clicks continue.

### Character Budget (v2.1)

| Step | Chars | Limit | Headroom |
|---|---|---|---|
| Step 0 (Read Document — User Input) | 307 | 8,000 | 7,693 |
| Step 1 (Read Document — Reference Rubric) | 206 | 8,000 | 7,794 |
| Step 2 (Think) | 6,158 | 8,000 | 1,842 |
| Step 3 (Respond) | 7,622 | 8,000 | 378 |

---

## v2 — 2026-03-23

### Summary

Complete rebuild of the Adaptive Learning Coach agent from a 27-step branching architecture to a 4-step linear flow. Eliminates all branching, removes massive content duplication, fixes the Glean re-entry bug, and improves evaluation quality across all three scenario types.

### What Changed

#### Architecture: 27 steps → 4 steps

| | v1 | v2 |
|---|---|---|
| Total steps | 27 | 4 |
| Branch steps | 1 (3 paths of 7 steps each) | 0 |
| Rubric levels written | 3× | 1× (with enablement + collateral overlays) |
| Evaluation method written | 3× | 1× |
| Output format written | 3× | 1× |
| Scenario detection | User selects via 3 Chat Message Triggers | LLM auto-detects from document content |

#### Step-by-step breakdown (v2)

- **Step 0 — Read Document:** Ingests user-provided document (transcript, collateral, or enablement session via URL/file link).
- **Step 1 — Read Document:** Loads the 101–401 Tech Office Perspective reference rubric from SharePoint.
- **Step 2 — Think:** Persona definition, guard rail for empty input, auto-detect scenario type, sales process stage (with collateral-specific inference), rubric levels with enablement and collateral overlays, evidence grounding rules.
- **Step 3 — Respond:** Full competency sets for all three scenarios, evaluation method, and output format.

### Bug Fix: Glean Branch Re-entry

**Problem:** v1 used a Branch step (Step 4) to route to one of three scenario paths. Glean re-enters the flow from the top on every user message. Follow-up interactions broke routing because user replies did not match any branch condition — the same class of bug found in the Myhill Testing Agent v1.

**Fix:** Eliminated branching entirely. A single Think step auto-detects the scenario type from the document content, and a single Respond step contains all three competency sets with clear delimiters (`═══ IF CUSTOMER CONVERSATION ═══`, etc.) so the LLM applies only the relevant set.

### Quality Improvements

1. **Enablement rubric levels restored:** v1 Branch 2 had teaching-oriented reframes of each rubric level (e.g., "Can teach the audience how to leverage..." vs. "Can run structured discovery..."). v2 embeds "For enablement:" overlays at every level (101–401) in the Think step so the LLM scores teaching effectiveness, not just personal performance.

2. **No more lazy cross-references:** v1's consolidation initially used shortcuts like "Same 4 competencies as above, but scored on teaching quality." v2 spells out all 4 competencies explicitly under every scenario to prevent the LLM from shortcutting under long-context pressure.

3. **Collateral scenario fully expanded:** The Collateral path's Section A (Customer Conversations) now has all 4 competencies with asset-specific evaluation questions, rather than a single vague sentence.

4. **Customer Conversation Sections B and C restored:** Section B (Enablement) now has 3 explicit sub-competencies (clarity, translation, champion enablement). Section C (Collateral) now has 3 sub-categories (customer-facing, competitive/objection, evaluation/workshop) matching v1 detail.

5. **Multi-type input handling:** v1 had no guidance for ambiguous inputs. v2 instructs the LLM to "err on including more competency sections from each relevant type" when inputs span multiple scenario types.

6. **Evidence grounding rules:** Explicit instruction to treat all inputs as evidence against the rubric, with N/A marking for unobservable competencies and anti-inflation rules moved into the Think step.

7. **Sales process stage identification:** Discovery → Analysis → Design → Defend framework included in Think step to contextualize evaluations within the sales cycle.

### Character Budget (v2 initial, before v2.1 hardening)

| Step | Chars | Limit | Headroom |
|---|---|---|---|
| Step 0 (Read Document) | 329 | 8,000 | 7,671 |
| Step 1 (Read Document) | 206 | 8,000 | 7,794 |
| Step 2 (Think) | 4,867 | 8,000 | 3,133 |
| Step 3 (Respond) | 7,500 | 8,000 | 500 |
