# Frequenz Dispatch API Release Notes

## Summary

## What's Changed

* Renamed component target message types and fields for consistency with monitoring API:
  * `IdSet` → `ElectricalComponentIdSelector`
  * `CategorySet` → `ElectricalComponentCategorySelectorDeprecated`
  * `CategoryTypeSet` → `ElectricalComponentCategorySelector`
  * `CategoryAndType` → `ComponentCategory`
  * `component_categories` → `component_categories_deprecated` (deprecated field)
  * `component_categories_types` → `component_categories`
