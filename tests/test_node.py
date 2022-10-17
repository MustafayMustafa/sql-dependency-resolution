import pytest

from src.sql_node import BaseSqlNode, ViewNode


def test_raises_exception():
    file_path = "tests/data/views/vw_view_1.sql"
    with pytest.raises(TypeError) as e:
        node = BaseSqlNode(file_path)

    assert str(e.value) == "Dependency regex pattern not defined"


def test_view_node():
    file_path = "tests/data/views/vw_view_1.sql"
    node = ViewNode(file_path)

    assert node.dependencies == ["vw_view_3"]
