# License: MIT
# Copyright © 2023 Frequenz Energy-as-a-Service GmbH

"""Basic tests to check some code is generated."""


def test_package_import() -> None:
    """Test that the package can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api import dispatch

    assert dispatch is not None


def test_module_import() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.dispatch import dispatch_pb2

    assert dispatch_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.dispatch import dispatch_pb2_grpc

    assert dispatch_pb2_grpc is not None


def test_fcr_pq_import() -> None:
    """Test that the FCR prequalification sub module can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.dispatch.fcr import prequalification_pb2

    assert prequalification_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.dispatch.fcr import prequalification_pb2_grpc

    assert prequalification_pb2_grpc is not None
