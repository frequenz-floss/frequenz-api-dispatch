# Frequenz Dispatch API Release Notes

## Summary

In this release, we have made some changes to the API to improve the user experience and to fix some bugs.

## Upgrading

* The dispatch message was split into into metadata and data.
* `microgrid_id` is required for all requests.
* `id` was renamed to `dispatch_id` in all requests.
* Naming conventions were updated to match API projects.
* The possibility to update the `dry_run` and `type` fields was removed.

## New Features

* Create and Update request now returns the new dispatch object.
* Documentation about authentication and encryption was added.
* Enhanced `payload` documentation.
* Add YEARLY frequency to the recurrence definition.
* Add parameters for pagination and sorting.
* Extended filter parameters for recurrence and end time.

## Bug Fixes

* The field `bymonthdays` the recurrence definition also supports negative values and was updated accordingly.
