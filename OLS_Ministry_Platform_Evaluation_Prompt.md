# OLS Scheduling Software and ChMS Integrations

Copy everything below the line into Grok, Claude, or another research assistant. Ask it to use current web sources, vendor docs, and user reviews—not training-data guesses.

---

You are a parish operations and church-management software analyst. Produce a decision-ready evaluation of ACS Technologies **Ministry Platform** for Our Lady of Sorrows (OLS), a Catholic parish in Northwest Arkansas.

Primary product page: https://www.acstechnologies.com/ministryplatform/

Do not sell the product. Be skeptical, specific, and cite sources (URLs and dates). Flag uncertainty. Distinguish Catholic parish fit from evangelical / large-campus church fit. If Ministry Platform is a poor match, say so and name better options.

## Parish profile

- Parish: Our Lady of Sorrows (OLS), Northwest Arkansas
- Website: https://www.ourladyofsorrowsnwa.org
- Typical Sunday attendance: ~500
- Staff and volunteers are remote-first; every tool must work well off-site
- Users are competent with Microsoft Office and basic web tools. They need **simplicity**, not power-user complexity
- Licensed stack today: **Realm**, **Realm Connect**, and **Realm Accounting** (ACS Technologies / ACS Realm)
- Microsoft 365 is in use
- Realm Connect is **not** user-friendly enough for OLS scheduling and lacks the integrations OLS needs

## Current systems (pain points)

### Scheduling and ministry assignments

| Need | Current tool | Integration with Realm |
| --- | --- | --- |
| Mass intentions | Wix Scheduler | None |
| Adoration | Wix Scheduler | None |
| Altar servers | Excel (pastor-maintained) | None |
| Room bookings | Not yet (parish hall later this year) | N/A |
| Events + volunteer serving | Fragmented | Weak / none |

### Communications and registration

| Need | Current tool | Integration with Realm |
| --- | --- | --- |
| Email | Wix marketing | None / weak |
| SMS | Not using RingCentral or Wix for this, because neither ties to the Realm parishioner database | None |
| Phones | RingCentral | None |
| Parish registration | Custom Jotform: https://www.ourladyofsorrowsnwa.org/register | None |

## Your task

Assess Ministry Platform as a possible replacement or complement for Realm / Realm Connect for scheduling, events, volunteers, rooms, and related communications. Also assess accounting: keep Realm Accounting and integrate, or move accounting onto Ministry Platform.

### 1. Suitability for OLS

For each of the following, say whether Ministry Platform can do it natively, via add-on, via integration, or not at all. Note Catholic-specific needs (Mass intentions, adoration slots, liturgical roles such as altar servers).

- Mass intentions
- Adoration scheduling
- Altar server scheduling
- Room / facility booking (including a future parish hall)
- Events and volunteer serving at events
- Parishioner database as source of truth
- Parish registration (replace or ingest the Jotform flow)
- Email to the parishioner list
- SMS to the parishioner list
- Phone / RingCentral (or equivalent) alignment with the database

Score overall fit for a ~500-attendance, remote, simplicity-first Catholic parish. Call out where Ministry Platform is built for a different size or staffing model.

### 2. APIs and integrations

Evaluate APIs, webhooks, Zapier/Make, SSO, Microsoft 365, Wix, Jotform, RingCentral, and Realm (including Realm Accounting).

For each relevant integration:

- Official vs. community / custom
- What data can move (people, families, giving, events, rooms, volunteers, communications)
- Direction (one-way vs. two-way) and sync reliability
- Typical implementation effort and who must own it
- Known gaps (especially Realm Connect vs. Ministry Platform vs. remaining Wix/Jotform/RingCentral)

State clearly whether OLS can keep Realm as ChMS and use Ministry Platform only for scheduling, or whether a full ChMS migration is required for the product to work.

### 3. Accounting: integrate vs. migrate

Compare:

**A.** Keep **Realm Accounting**; integrate with Ministry Platform (or keep Realm for people + accounting and only add scheduling elsewhere)

**B.** Move off Realm Accounting onto **Ministry Platform accounting** (or ACS accounting that actually sits with Ministry Platform)

Cover chart of accounts / fund accounting for a parish, contribution/pledge posting, diocesan reporting if known, dual-system risk, cutover pain, and a recommendation with conditions.

### 4. Ease of use

Judge against OLS’s bar: remote volunteers, Office-level skill, low training budget.

Cover admin vs. volunteer vs. parishioner-facing UX, mobile, scheduling workflows vs. Realm Connect, typical time-to-competence, and implementation/training load for a parish this size.

### 5. Costs

Estimate (ranges OK; label assumptions):

- Licensing (what it is based on: attendance, records, modules, users)
- Implementation / data migration from Realm, Wix, Excel, Jotform
- Annual support, required ACS services, third-party integration cost
- 3-year TCO vs. staying on Realm + stitching Wix / Jotform / Excel / RingCentral

Note if ACS quotes are not public. Do not invent a precise price.

### 6. User sentiment

Summarize real user sentiment from recent reviews, forums, Catholic/parish case studies, and G2/Capterra/Reddit/Facebook groups where available.

Separate:

- Large evangelical / multi-campus churches
- Catholic parishes and dioceses
- Scheduling / volunteer / rooms specifically
- Accounting specifically
- Support quality and implementation partners

Flag recency. Old ACS “MP” lore is not enough.

## Required output format

1. **Executive recommendation** (1 page): go / no-go / conditional; 3–5 bullets
2. **Fit matrix** for the scheduling, comms, and registration items above
3. **Integration architecture** (keep Realm vs. replace Realm vs. hybrid) with a simple data-flow description
4. **Accounting recommendation** (A, B, or neither) and why
5. **Cost ranges and 3-year TCO** with assumptions
6. **Sentiment summary** with sources
7. **Risks and open questions** OLS must ask ACS before buying
8. **If not Ministry Platform:** 2–4 alternative stacks that better match OLS (include whether staying on Realm and replacing only scheduler/comms is wiser)

## Constraints

- Optimize for **simplicity** and **remote use**, not maximum features
- ~500 Sunday attendance—do not assume a mega-church IT staff
- Catholic liturgical scheduling matters; generic “volunteer teams” may not be enough
- Prefer evidence over brochure language
- Call out vendor lock-in and switching costs from Realm
