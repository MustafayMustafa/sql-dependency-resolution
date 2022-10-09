import pytest

from src.graph import Graph


@pytest.fixture()
def create_graph():
    return Graph()


def test_init_graph(create_graph):
    graph = create_graph

    assert graph.size == 0
    assert graph.graph == {}


def test_repr(create_graph):
    graph = create_graph
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)

    assert repr(graph) == "0 => [1, 2]\n1 => []\n2 => []\n"


def test_add_edge(create_graph):
    graph = create_graph
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)

    assert graph.graph == {0: [1, 2], 1: [], 2: []}
    assert graph.size == 3


def test_graph_str_verticies(create_graph):
    graph = create_graph
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")

    assert graph.graph == {"A": ["B", "C"], "B": ["C"], "C": []}
    assert graph.size == 3
