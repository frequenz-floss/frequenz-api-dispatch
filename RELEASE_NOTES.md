# Frequenz Dispatch API Release Notes

## Summary

This update introduces the possibility to target specific types of batteries, inverters and EV chargers.

## Deprecations

* In the `TargetComponents` message, the field `components.component_categories` is now deprecated. See the upgrading section for details.

## Upgrading

* The `TargetComponents` message now accepts an optional `type` too. `.components.component_categories` is now deprecated. Instead `.components.component_categories_types`, a new `CategoryAndType` message that has a required `category` (`ComponentCategory`) and an optional `type` (`oneof BatteryType, EVChargerType, InverterType`) should be used.

## New Features

- Now specific types of batteries, inverters and EV chargers can be targeted.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
