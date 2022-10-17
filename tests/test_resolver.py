import pytest

from src.resolver import DependencyResolver

def test_resolver_in_degree():
    views = "tests/data/views/"
    resolver = DependencyResolver(objects_path=views)
    degrees =  resolver.in_degrees(resolver.graph.graph, None)

    assert degrees == {'vw_view_1': 1, 'vw_view_2': 1, 'vw_view_3': 0, 'vw_view_4': 2}

def test_valid_sorting():
    views = "tests/data/views/"
    resolver = DependencyResolver(objects_path=views)

    assert resolver.create_order() == [
        "vw_view_3",
        "vw_view_1",
        "vw_view_2",
        "vw_view_4",
    ]
    assert resolver.drop_order() == [
        "vw_view_4",
        "vw_view_2",
        "vw_view_1",
        "vw_view_3",
    ]


@pytest.mark.skip
# TODO: mock files to add extra view that causes circular dependency
def test_circular_dependency():
    assert False
