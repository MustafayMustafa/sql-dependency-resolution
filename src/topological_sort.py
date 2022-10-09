from collections import defaultdict
from typing import List, TypeVar

T = TypeVar("T")


class TopologicalSortMixin:
    """Mixin that provides methods required for topological sorting.
    Sorting is acheived using Khan's algorithm against an adjancey list.
    Constraints:
      - adjancey list represnts a directed acylic graph.
    """

    def in_degrees(self, graph: dict, size: int) -> dict:
        """produce a dict of in-degree counts for each vertex.

        Args:
            graph (dict): adjaceny list representing graph.
            size (int): size of the graph

        Returns:
            dict: key: vertex, value: indegree count
        """
        pass

    def sort(self, graph: dict, size: int) -> List:
        """Return a list with containing the topological ordering of the graph.

        Args:
            graph (dict): adjaceny list representing graph.
            size (int): size of the graph.

        Returns:
            List: topological ordering.
        """
