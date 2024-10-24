# Frequenz Dispatch API Release Notes

## Summary

This update focuses on pagination.

## Upgrading

* Updated to the latest common-api which provides slighlty modified pagination messages.
* The `TimeIntervalFilter` is now inclusive on both ends.

## New Features

* Added more detailed documentation on how to use pagination.
* Added `start_immediately` to the create RPC.

## Bug Fixes

* Fixed pagination fields in the response (`pagination_params` -> `pagination_info`)
