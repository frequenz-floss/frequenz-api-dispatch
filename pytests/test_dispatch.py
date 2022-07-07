def test_package_import() -> None:
    import fz_api.dispatch as dispatch

    assert dispatch is not None


def test_module_import() -> None:
    import fz_api.dispatch.dispatch_pb2 as dispatch_pb2

    assert dispatch_pb2 is not None

    import fz_api.dispatch.dispatch_pb2_grpc as dispatch_pb2_grpc

    assert dispatch_pb2_grpc is not None
