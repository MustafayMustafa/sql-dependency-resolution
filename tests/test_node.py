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


def test_dependency_by_from_keyword(tmp_path):
    tmp_dir = tmp_path / "sub"
    tmp_dir.mkdir()
    path = tmp_dir / "vw_view_5.sql"
    
    vw_view_5 = """
    create view vw_view_5 as
    select * 
    from vw_view_3 st
    """
    path.write_text(vw_view_5)

    node = ViewNode(path)
    assert node.dependencies == ["vw_view_3"]
