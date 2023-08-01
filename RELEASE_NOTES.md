# Release notes

- The field `create_time` has been removed from update requests.
- An `update_time` field has been added to the Dispatch object.
- The `type` field has been removed from update requests, to prevent it from being modified after creation.
- `DispatchFilter` has been replaced by `DispatchListRequest` as a parameter for `ListDispatches`.
  - The filter has additionally been re-designed, with fields that lack use cases being removed.
