from pathlib import Path
from wiki.service import WikiService


def _svc(sample_assets: Path, tmp_path: Path) -> WikiService:
    return WikiService(assets_root=sample_assets, index_path=tmp_path / "idx.json")


def test_categories(sample_assets, tmp_path):
    s = _svc(sample_assets, tmp_path)
    cats = s.categories()
    types = {c["type"] for c in cats}
    assert {"MMLCommand", "ConfigObject", "Task"} <= types


def test_group_command_by_category_path(sample_assets, tmp_path):
    s = _svc(sample_assets, tmp_path)
    groups = s.group("MMLCommand", "UDG", "20.15.2")
    keys = {g["key"] for g in groups}
    assert "用户面服务管理/计费控制" in keys


def test_list_in_bucket(sample_assets, tmp_path):
    s = _svc(sample_assets, tmp_path)
    res = s.list_objs("MMLCommand", "UDG", "20.15.2", group_field="category_path", group_value="用户面服务管理/计费控制")
    assert any(i["path"] == "command/UDG/20.15.2/ADD-URR.md" for i in res["items"])


def test_neighborhood_out_and_reverse(sample_assets, tmp_path):
    s = _svc(sample_assets, tmp_path)
    nb = s.neighborhood("command/UDG/20.15.2/ADD-URR.md")
    paths = {n["path"] for n in nb["nodes"] if n.get("path")}
    # 出向：URR 配置对象、0-00001 任务
    assert "configobject/UDG/20.15.2/URR.md" in paths
    assert "task/UDG/20.15.2/0-00001.md" in paths
    assert nb["center"]["path"] == "command/UDG/20.15.2/ADD-URR.md"


def test_neighborhood_placeholder_node(sample_assets, tmp_path):
    s = _svc(sample_assets, tmp_path)
    nb = s.neighborhood("task/UDG/20.15.2/0-00001.md")
    unresolved = [n for n in nb["nodes"] if not n.get("resolved", True)]
    assert any("URRGROUP" in n["name"] for n in unresolved)


def test_search(sample_assets, tmp_path):
    s = _svc(sample_assets, tmp_path)
    res = s.search("URR")
    assert any(r["path"] == "command/UDG/20.15.2/ADD-URR.md" for r in res)
