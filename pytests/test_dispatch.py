# License: MIT
# Copyright © 2023 Frequenz Energy-as-a-Service GmbH

"""Basic tests to check some code is generated."""


def test_package_import() -> None:
    """Test that the package can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.dispatch import v1

    assert v1 is not None


def test_module_import_components() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.dispatch.v1 import dispatch_pb2

    assert dispatch_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.dispatch.v1 import dispatch_pb2_grpc

    assert dispatch_pb2_grpc is not None


def test_steam_boiler_target_round_trip() -> None:
    """Test that steam boiler category targets keep their wire value."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha8.microgrid.electrical_components import (
        electrical_components_pb2,
    )
    from frequenz.api.dispatch.v1 import dispatch_pb2 as dispatch_proto

    category = electrical_components_pb2.ELECTRICAL_COMPONENT_CATEGORY_STEAM_BOILER
    assert category == 19

    target = dispatch_proto.TargetComponents(
        component_categories_types=dispatch_proto.TargetComponents.CategoryTypeSet(
            categories=[
                dispatch_proto.TargetComponents.CategoryAndType(category=category)
            ]
        )
    )

    parsed = dispatch_proto.TargetComponents.FromString(target.SerializeToString())
    assert parsed == target
    assert parsed.component_categories_types.categories[0].category == 19
