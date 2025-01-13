# Frequenz Dispatch API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

* The `TargetComponents` message now accepts an optional `type` too. `.components.component_categories` is no longer just a `ComponentCategory` but a new `CategoryAndType` message that has a required `category` (`ComponentCategory`) and an optional `type` (`oneof BatteryType, EVChargerType, InverterType`).

## New Features

- Now specific types of batteries, inverters and EV chargers can be targeted.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
