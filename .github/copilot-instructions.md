# Frequenz Dispatch API

**ALWAYS FOLLOW THESE INSTRUCTIONS FIRST. Only fallback to additional search and context gathering if the information in these instructions is incomplete or found to be in error.**

Frequenz Dispatch API is a Python gRPC API package that generates Python code from Protocol Buffer (.proto) files. It provides operations for dispatching microgrid components and automation of electricity management.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Repository Setup and Build Process
- **CRITICAL**: Always update git submodules first:
  - `git submodule update --init` -- takes ~5 seconds. NEVER CANCEL.
- Install system dependencies:
  - `sudo apt update && sudo apt install -y protobuf-compiler python3-protobuf python3-grpcio python3-pytest` -- takes 2-3 minutes. NEVER CANCEL.
- Generate protobuf Python files (REQUIRED for functionality):
  - `protoc --python_out=py/ --proto_path=proto:submodules/frequenz-api-common/proto:submodules/api-common-protos proto/frequenz/api/dispatch/v1/dispatch.proto` -- takes <1 second
  - `protoc --python_out=py/ --proto_path=proto:submodules/frequenz-api-common/proto:submodules/api-common-protos $(find submodules/frequenz-api-common/proto -name "*.proto")` -- takes <1 second
- **When grpcio-tools is available**: Generate gRPC stubs:
  - `python -m grpc_tools.protoc --grpc_python_out=py/ --proto_path=proto:submodules/frequenz-api-common/proto:submodules/api-common-protos proto/frequenz/api/dispatch/v1/dispatch.proto`
- **Network Limitation**: Package installation via pip often fails due to network timeouts. Use system packages where possible.

### Testing
- Run tests: `PYTHONPATH=py python3 -m pytest pytests/ -v` -- takes <1 second. NEVER CANCEL.
- **LIMITATION**: The dispatch_pb2_grpc module requires grpcio-tools which may not be available due to network limitations
- Basic protobuf functionality works with system packages
- Tests location: `pytests/test_dispatch.py`
- **SUCCESS CRITERIA**: The test_package_import should always pass; test_module_import_components requires gRPC tools

### Build Validation
- **CANNOT BUILD**: Full `python -m build` fails due to network connectivity issues with PyPI
- **Alternative**: Manual protobuf generation works as shown above
- **CANNOT INSTALL**: `pip install -e .` and `pip install .[dev]` fail due to network timeouts
- **WORKAROUND**: Use `PYTHONPATH=py` to add the generated code to Python path

### Development Tools Status
- **AVAILABLE**: protoc (libprotoc 3.21.12), python3-protobuf, python3-grpcio, python3-pytest
- **NOT AVAILABLE due to network issues**: nox, black, isort, pylint, mypy, flake8, mkdocs, grpcio-tools
- **TIMING**: All basic operations (submodule update, protobuf generation, tests) complete in seconds

## Validation

- **CRITICAL LIMITATION**: Full validation cannot be performed due to network connectivity preventing package installation
- **MANUAL VALIDATION**: Test protobuf import with: `PYTHONPATH=py python3 -c "from frequenz.api.dispatch import v1; print('Import successful')"`
- **BASIC TESTING**: Run `PYTHONPATH=py python3 -m pytest pytests/test_dispatch.py::test_package_import -v` to verify package import works
- **CANNOT TEST**: gRPC functionality due to missing grpcio-tools
- **CANNOT VALIDATE**: Full CI pipeline locally due to missing nox and other tools

### Validation Scenarios (when full environment is available)
After making any changes to the codebase, ALWAYS run these validation steps:
1. **Protocol Buffer Validation**: `protolint lint proto` -- ensures proto files follow style guidelines
2. **Python Import Test**: `python -c "from frequenz.api.dispatch.v1 import dispatch_pb2, dispatch_pb2_grpc; print('Both imports successful')"` -- verifies generated code works
3. **Full Test Suite**: `nox -s pytest_min` -- runs all unit tests. Takes 1-2 minutes. NEVER CANCEL.
4. **Linting Validation**: `nox -s ci_checks_max` -- runs black, isort, pylint, mypy. Takes 3-5 minutes. NEVER CANCEL.
5. **Documentation Build**: `mkdocs build` -- ensures documentation can be generated without errors
6. **Package Build**: `python -m build` -- creates source and wheel distributions. Takes 1-3 minutes. NEVER CANCEL.

### Manual Testing Scenarios
Test actual functionality by exercising the API:
- Import and inspect the generated protobuf messages: `python -c "from frequenz.api.dispatch.v1.dispatch_pb2 import *; print(dir())"`
- Verify protobuf serialization works: Create a dispatch message, serialize it, and deserialize it
- **ALWAYS** test import after regenerating protobuf files

## Common Tasks

### Repository Structure
```
/home/runner/work/frequenz-api-dispatch/frequenz-api-dispatch/
├── .github/                    # GitHub workflows and templates
│   └── workflows/ci.yaml      # Main CI pipeline
├── proto/                     # Protocol buffer source files
│   └── frequenz/api/dispatch/v1/dispatch.proto
├── py/                        # Generated Python code location
│   └── frequenz/api/dispatch/ # Generated modules
├── submodules/                # Git submodules
│   ├── api-common-protos/     # Google common protobuf types
│   └── frequenz-api-common/   # Frequenz common API definitions
├── pytests/                   # Test files
├── docs/                      # Documentation source
├── pyproject.toml            # Project configuration
├── noxfile.py               # Nox session configuration (needs network)
└── mkdocs.yml               # Documentation configuration
```

### Key Files Content

#### pyproject.toml (main project config)
- Python 3.11+ required
- Uses setuptools, setuptools_scm, frequenz-repo-config for build
- Dependencies: frequenz-api-common, googleapis-common-protos, protobuf, grpcio
- Development tools: black, isort, pylint, mypy, pytest, mkdocs

#### noxfile.py
```python
from frequenz.repo.config import RepositoryType, nox
nox.configure(RepositoryType.API)
```

#### .github/workflows/ci.yaml
- Runs protolint on proto files
- Uses nox for testing with Python 3.11 and 3.12
- Tests on amd64 and arm architectures
- Builds and tests package installation
- Publishes documentation to GitHub Pages
- Creates GitHub releases for tags

### Expected Workflow (when network is available)
1. `git submodule update --init` -- 5 seconds. NEVER CANCEL.
2. `python -m pip install .[dev]` -- includes all dev dependencies. Can take 2-5 minutes due to package compilation. NEVER CANCEL.
3. `python -m build` -- build distribution packages. Takes 1-3 minutes. NEVER CANCEL.
4. `nox` -- run all tests and checks. Takes 10-20 minutes total. NEVER CANCEL.
   - `nox -s ci_checks_max` -- linting and type checking. Takes 3-5 minutes.
   - `nox -s pytest_min` -- run tests. Takes 1-2 minutes.
5. `mkdocs serve` -- preview documentation. Starts in 30-60 seconds.
6. `protolint lint proto` -- lint protocol buffer files. Takes <10 seconds.
   - Install: `curl -LO https://github.com/yoheimuta/protolint/releases/download/v0.53.0/protolint_0.53.0_Linux_x86_64.tar.gz && tar -xzf protolint_0.53.0_Linux_x86_64.tar.gz && sudo mv protolint /usr/local/bin/`

### Network-Limited Workaround Workflow
1. `git submodule update --init` -- 5 seconds
2. `sudo apt install -y protobuf-compiler python3-protobuf python3-grpcio python3-pytest`
3. Generate protobuf files manually (see commands above)
4. `PYTHONPATH=py python3 -m pytest pytests/ -v` -- <1 second
5. **NOTE**: Many development tools unavailable, use basic Python syntax checking

### Important Notes
- **NEVER CANCEL**: In normal circumstances, `nox` can take 15+ minutes, `python -m build` can take 2+ minutes
- **TIMING ESTIMATES**: With network access, expect 15-30 minutes for full build and test cycle
- **FIREWALL LIMITATION**: Current environment has PyPI connectivity issues preventing normal pip operations
- **CRITICAL**: Always run `git submodule update --init` before any other operations
- **GENERATED CODE**: The py/ directory contains generated Python code from protobuf files
- **TEST DEPENDENCIES**: Basic tests work with system packages, full test suite requires pip-installed dependencies

### Proto File Workflow
- Protocol buffer definitions are in `proto/frequenz/api/dispatch/v1/dispatch.proto`
- Common types come from submodules (frequenz-api-common, api-common-protos)
- Use `protolint lint proto` to validate proto files (when protolint is available)
- Generated Python files go in `py/frequenz/api/dispatch/v1/`

### Development Limitations in Current Environment
- Cannot run full linting (black, isort, pylint, mypy)
- Cannot build documentation (mkdocs)
- Cannot run nox sessions
- Cannot install packages via pip due to network timeouts
- Cannot generate gRPC stubs (requires grpcio-tools)
- **WORKAROUND**: Use system packages and manual protobuf generation for basic functionality