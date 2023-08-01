# Release notes

- The field `create_time` has been removed from update requests.
- An `update_time` field has been added to the Dispatch object.
- The `type` field has been removed from update requests, to prevent it from being modified after creation.
- `DispatchFilter` has been replaced by `DispatchListRequest` as a parameter for `ListDispatches`.
  - The filter has additionally been re-designed, with fields that lack use cases being removed.
- Removed the ability to update `microgrid_id` on an existing dispatch.
- Removed the HTTP proxy gateway URLs, as these will not be used by the dispatch API.
- Added RPCs for getting and deleting a single dispatch.
