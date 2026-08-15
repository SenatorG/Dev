# Trigger Regression Tests

These examples define intended activation behavior.

## Should trigger

- “Write this paper in Chicago author-date.” → Trigger; use Author-Date; terminal heading `References`.
- “Add Chicago footnotes and a bibliography.” → Trigger; use Notes-Bibliography.
- “Convert these citations to CMOS 17.” → Trigger; preserve requested system if evident from citations, otherwise infer.
- “This document already uses Chicago footnotes. Add two sources.” → Trigger; preserve Notes-Bibliography.
- “Add AI attribution explaining which model and tools were used.” → Trigger provenance behavior even if citation behavior is not needed.

## Should not trigger automatically

- “Summarize these three articles.” → No Chicago formatting unless the user requests source attribution/citations or the surrounding artifact already uses Chicago.
- “Find the best sources on this topic.” → Research may be performed, but do not automatically force Chicago formatting into the response unless requested.
- “Make this paragraph clearer.” → No Chicago behavior unless the paragraph/artifact already uses Chicago or citation preservation is needed.
- “Create a two-slide customer summary.” → Do not append visible AI disclosure merely because AI was used.

## Ambiguous cases

- “Give me inline citations.” → Trigger; if Chicago is explicit elsewhere use Chicago Author-Date. If Chicago is not requested, do not silently label another citation style as Chicago.
- “Add a bibliography.” → Trigger source-list behavior; use Chicago only if Chicago is explicit or established in the artifact/context.