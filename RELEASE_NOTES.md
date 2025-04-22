# Frequenz Dispatch API Release Notes

## Summary

This update introduces the possibility to target specific types of batteries, inverters and EV chargers.

## Deprecations

* In the `TargetComponents` message, the field `components.component_categories` is now deprecated. See the upgrading section for details.

## Changes

*   Renamed several `google.protobuf.Timestamp` fields in Protobuf messages to align with Google API Design Guide naming conventions (`*_time` suffix):
    *   `DispatchMetadata.modification_time` is now `update_time`.
    *   `TimeIntervalFilter.from` is now `from_time`.
    *   `TimeIntervalFilter.to` is now `to_time`.
    *   `RecurrenceRule.EndCriteria.until` is now `until_time`.
    *   **Note:** This is a breaking change for clients using the old field names.

## Upgrading

* The `TargetComponents` message now accepts an optional `type` too. `.components.component_categories` is now deprecated. Instead `.components.component_categories_types`, a new `CategoryAndType` message that has a required `category` (`ComponentCategory`) and an optional `type` (`oneof BatteryType, EVChargerType, InverterType`) should be used.

## New Features

- Now specific types of batteries, inverters and EV chargers can be targeted.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
