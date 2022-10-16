import pytest

from src.sql_node import BaseSqlNode, ViewNode


def test_raises_exception():
    file_path = "tests/data/test_view.sql"
    with pytest.raises(TypeError) as e:
        node = BaseSqlNode(file_path)

    assert str(e.value) == "Dependency regex pattern not defined"


def test_view_node():
    file_path = "tests/data/test_view.sql"
    node = ViewNode(file_path)

    assert node.dependencies == ["vw_some_view", "vw_some_other_view"]
