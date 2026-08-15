# Citation Semantics Regression Tests

## Citation density

Text: “The source reports revenue of $10B. It attributes growth to demand in two segments. The company expects the pattern to continue.” All three sentences rely on one source.

Expected: In Standard mode, one citation at the end of the cluster may be sufficient if attribution is unambiguous. Do not force three identical citations.

## Common knowledge

Text: “The United States has fifty states.”

Expected: No citation solely to satisfy an ‘every sentence’ rule.

## Analysis versus evidence

Text: “Taken together, these results suggest the buyer values time-to-deploy more than peak benchmark performance.”

Expected: Cite the underlying results if not already cited nearby. Do not imply that the analytical inference is a direct quotation or explicit conclusion of the source unless it is.

## Source validation

Claim: “Vendor X supports Feature Y on Product Z.”

Expected: Prefer Vendor X's official product/support documentation. A reseller blog with complete metadata is not automatically superior evidence.

## Author-Date heading

Expected: terminal heading is `References` by default, not `Bibliography`.

## Notes-Bibliography heading

Expected: terminal heading is `Bibliography` by default.

## Missing metadata

Source has no publication date.

Expected: use `n.d.` when CMOS permits; never infer a year from page styling, copyright boilerplate, or search snippets.