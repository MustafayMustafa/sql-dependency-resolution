from typing import List, TypeVar


T = TypeVar("T")


class Graph:
    """This class describes a directed graph, the graph is represented using an adjacency list."""

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        """returns the representation of the graph in a pretty print format.

        Returns:
            str: adjancey list representation.
        """
        pass

    def add_edge(self, u: T, v: T) -> None:
        """add an edge from u to v and store this in the adjancey list.
            Update the size of graph on every insert.

        Args:
            u (T): vertex from.
            v (T): vertex to.
        """
        pass
