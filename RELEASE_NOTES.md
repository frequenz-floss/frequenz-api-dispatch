# Frequenz Dispatch API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

- Queries that compare against a time interval filter should check for the end time inside the recurrence rule.
- `end_time` has been renamed `until` and is mutually exclusive with `count`.
- Update request handlers should check the field mask for which attributes to update.
- The common api dependency has been udpated so that the `v1` paths for `ComponentCategory` is used.

## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
