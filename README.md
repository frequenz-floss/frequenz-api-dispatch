# Frequenz Dispatch API

[![Build Status](https://github.com/frequenz-floss/frequenz-api-dispatch/actions/workflows/ci.yaml/badge.svg)](https://github.com/frequenz-floss/frequenz-api-dispatch/actions/workflows/ci.yaml)
[![PyPI Package](https://img.shields.io/pypi/v/frequenz-api-dispatch)](https://pypi.org/project/frequenz-api-dispatch/)
[![Docs](https://img.shields.io/badge/docs-latest-informational)](https://frequenz-floss.github.io/frequenz-api-dispatch/)

## Introduction

Frequenz gRPC API to propagate dispatches to microgrids.

Dispatches might include, for example:

* Hard shutdown of a location or an individual microgrid component
* Charging or discharging a battery
* Activation or deactivation of balancing power
* Activation or deactivation of a power plant

Microgrid controllers are expected to regularly query this API to keep up to
date with what resources the cloud wishes them to deploy.

## Contributing

If you want to know how to build this project and contribute to it, please
check out the [Contributing Guide](CONTRIBUTING.md).
