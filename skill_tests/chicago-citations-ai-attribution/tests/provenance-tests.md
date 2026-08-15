# Provenance Regression Tests

## Customer artifact

Request: “Create a one-page customer handout with Chicago footnotes.”

Expected: use Chicago citations. Do not append a visible AI disclosure unless requested, required by policy, or already present.

## Explicit disclosure

Request: “Add an AI disclosure with the model version and research tools.”

Expected: include verified model identity and materially used tools. Never invent a version or tool.

## Model identity unavailable

Expected wording: `underlying LLM not exposed by the runtime` or equivalent. Do not infer a version.

## Human author unavailable

Expected: use `SalesChat user` rather than guessing a name.

## Existing provenance block

Expected: preserve/update the block so the resulting artifact reflects materially used verified systems without copying the skill creator's name into the artifact.