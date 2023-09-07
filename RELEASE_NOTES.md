# Frequenz Dispatch API Release Notes

## Summary

This release is mainly about creating a ruleset for recurring dispatches.

## Upgrading

- As part of introducing versioning, the protobuf definitions and generated python code now has the path `frequenz.dispatch.v1`.

## New Features

- Package-based versioning has been introduced.
- Rules for recurring dispatches have been added.
  Examples:
    Every 6 months:
    ```
    message RecurrenceRule {
      Frequency freq = FREQUENCY_MONTHLY;
      uint32 interval = 6;
    }
    ```

    Weekends only:
    ```
    message RecurrenceRule {
      Frequency freq = FREQUENCY_WEEKLY;
      repeated Weekday byweekdays = [WEEKDAY_SATURDAY, WEEKDAY_SUNDAY];
    }
    ```

    Every day at midnight:
    ```
    message RecurrenceRule {
      Frequency freq = FREQUENCY_DAILY;
      repeated uint32 byhours = [0];
    }
    ```

    Nightly, assuming "night" means from 8 PM to 6 AM:
    ```
    message RecurrenceRule {
      Frequency freq = FREQUENCY_DAILY;
      repeated uint32 byhours = [20, 21, 22, 23, 0, 1, 2, 3, 4, 5];
    }
    ```

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
