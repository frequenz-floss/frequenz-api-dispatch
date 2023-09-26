# Frequenz Dispatch API Release Notes

## Summary

- End time has been moved to the recurrence rule object, replaced by `duration` on the base dispatch object.

## Upgrading

- Queries that compare against a time interval filter should check for the end time inside the recurrence rule.
- `end_time` has been renamed `until` and is mutually exclusive with `count`.

## New Features

- Introduced a new field `duration`.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
