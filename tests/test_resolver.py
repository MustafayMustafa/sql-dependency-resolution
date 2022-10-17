import shutil

import pytest
from src.resolver import ViewDependencyResolver
from src.topological_sort import CircularDependencyException


def test_resolver_in_degree():
    views = "tests/data/views/"
    resolver = ViewDependencyResolver(objects_path=views)
    degrees = resolver.in_degrees(resolver.graph.graph, None)

    assert degrees == {"vw_view_1": 1, "vw_view_2": 1, "vw_view_3": 0, "vw_view_4": 2}


def test_valid_sorting():
    views = "tests/data/views/"
    resolver = ViewDependencyResolver(objects_path=views)

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


def test_circular_dependency(tmp_path):
    source_dir = "tests/data/views"
    destination_dir = tmp_path / "sub"
    shutil.copytree(source_dir, destination_dir)

    vw_view_5 = """
    create view vw_view_5 as
    select * 
    from some_table st
    join vw_view_6 sv on
        sv.id = st.id
    """

    vw_view_6 = """
    create view vw_view_5 as
    select * 
    from some_table st
    join vw_view_5 sv on
        sv.id = st.id
    """

    with open(f"{destination_dir}/vw_view_5.txt", "a") as f:
        f.write(vw_view_5)
    with open(f"{destination_dir}/vw_view_6.txt", "a") as f:
        f.write(vw_view_6)

    with pytest.raises(CircularDependencyException) as e:
        resolver = ViewDependencyResolver(objects_path=destination_dir)
        resolver.create_order()
    assert str(e.value) == "Cycle detected"
