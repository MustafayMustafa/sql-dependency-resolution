import pytest

from src.topological_sort import TopologicalSortMixin


@pytest.fixture
def create_graph():
    graph = {0: [1, 2], 1: [], 2: [1, 3], 3: []}
    size = len(graph.keys())

    return (graph, size)


@pytest.fixture
def create_graph_strings():
    graph = {"A": ["B"], "B": [], "C": ["B", "D"], "D": []}
    size = len(graph.keys())

    return (graph, size)


def test_in_degrees(create_graph):
    graph, size = create_graph
    degree_list = TopologicalSortMixin.in_degrees(graph=graph, size=size)

    assert degree_list == {0: 0, 1: 2, 2: 1, 3: 1}


def test_in_degrees_strings(create_graph_strings):
    graph, size = create_graph_strings
    degree_list = TopologicalSortMixin.in_degrees(graph=graph, size=size)

    assert degree_list == {"A": 0, "B": 2, "C": 0, "D": 1}


def test_topological_sort(create_graph):
    graph, size = create_graph
    topological_ordering = TopologicalSortMixin.sort(graph=graph, size=size)

    assert topological_ordering == [0, 2, 1, 3]


def test_topological_sort_strings(create_graph_strings):
    graph, size = create_graph_strings
    topological_ordering = TopologicalSortMixin.sort(graph=graph, size=size)

    assert topological_ordering == ["A", "C", "B", "D"]


def test_cycle_detected():
    graph = {0: [1], 1: [0]}
    size = len(graph.keys())

    with pytest.raises(Exception) as e:
        topological_ordering = TopologicalSortMixin.sort(graph=graph, size=size)
    assert str(e.value) == "Cycle detected"
