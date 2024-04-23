# Frequenz Dispatch API Release Notes

## Upgrading

- Queries that compare against a time interval filter should check for the end time inside the recurrence rule.
- `end_time` has been renamed `until` and is mutually exclusive with `count`.
- Update request handlers should check the field mask for which attributes to update.
- The common api dependency has been udpated so that the `v1` paths for `ComponentCategory` is used.
