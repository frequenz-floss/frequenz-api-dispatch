# Frequenz Dispatch API Release Notes

## Summary

This release adds steam boilers to the component categories that can be
targeted by a dispatch.

## Upgrading

- Runtime requirements now start at `frequenz-api-common` 0.8.2,
  `googleapis-common-protos` 1.75.1, `protobuf` 7.36.1, and `grpcio` 1.83.1.
  In particular, protobuf 6 is no longer supported.

## New Features

- Added support for targeting steam boilers by component category.
