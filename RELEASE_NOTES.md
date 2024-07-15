# Frequenz Dispatch API Release Notes

## Summary

In this release, we have made some changes to the API to improve the user experience and to fix some bugs.
This might be the last breaking release, at least I tried hard to make it so.
Fingers crossed.

Note: The API supporting a feature does not mean that the service or client supports it as well, just yet.

## Upgrading

* The dispatch message was split into into metadata and data.
* `microgrid_id` is required for all requests.
* `id` was renamed to `dispatch_id` in all requests.
* Naming conventions were updated to match API projects.
* The possibility to update the `dry_run` and `type` fields was removed.
* The ComponentSelector now can contain multiple component categories.
* Improve description of the `EndCriteria.until` field.

## New Features

* Create and Update request now returns the new dispatch object.
* Documentation about authentication and encryption was added.
* Enhanced `payload` documentation.
* Add RPC streaming methods.
* Add YEARLY frequency to the recurrence definition.
* Add parameters for pagination and sorting.
* Documentation of valid values for `count` and `interval` fields was added.
* Extended `DispatchFilter` to support filtering by `recurrence` and `end_time`.
* Add new field `end_time` to the `DispatchDetail`.

## Bug Fixes

* The field `bymonthdays` the recurrence definition also supports negative values and was updated accordingly.
