# Frequenz Dispatch API Release Notes

## Summary

- Updated all `frequenz.api.common` imports from `v1` to `v1alpha8`.
- Removed the `TimeIntervalFilter` message, replacing its usage with the new `frequenz.api.common.v1alpha8.types.Interval` type.
- In the `DispatchFilter` message, the `start_time_interval`, `end_time_interval`, and `update_time_interval` fields were updated to use the new `Interval` type.
- In the `TargetComponents` message:
    - The `CategorySet` message's `categories` field was updated to use the new `ElectricalComponentCategory` enum.
    - The `CategoryAndType` message's `category` field was also updated to use the new `ElectricalComponentCategory` enum, and the nested `battery`, `inverter`, and `ev_charger` fields were updated to use their corresponding new types.
- The `ListMicrogridDispatchesRequest` message's `pagination_params` field was updated to use the new `PaginationParams` type.
- The `ListMicrogridDispatchesResponse` message's `pagination_info` field was updated to use the new `PaginationInfo` type.


## Upgrading

<!-- Here goes notes on how to upgrade from previous versions, including deprecations and what they should be replaced with -->

## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
