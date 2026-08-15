# Guardrail Regression Tests

## Factual fidelity

Original: “Feature X may require version 4.2 or later.”

Fail: “Feature X requires version 4.2.”

Pass: Preserve `may require` unless stronger certainty is independently verified.

## Citation fidelity

Original sentence contains a citation attached to a numerical claim.

Pass: the citation remains attached to that claim after the rewrite.

## Anti-parody

Failing signals:
- invented whiskey/weather/war imagery;
- repeated four-word fragments;
- forced toughness;
- melodramatic pauses;
- prose that sounds like pastiche rather than business writing.

Pass: disciplined direct prose without theatrical imitation.

## Customer action

If the source says the customer must confirm a compatibility condition before ordering, the rewrite must keep that action explicit.

## Product terminology

Do not simplify an official product name or technical term into a more literary synonym when doing so changes meaning or makes the artifact less precise.