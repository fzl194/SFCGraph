import json
from wiki.build_wiki_index import build_index, serialize_index, deserialize_index


def test_build_index_basic(sample_assets):
    idx = build_index(sample_assets)
    # 4 个对象 md（命令/配置对象/任务 + 证据）
    assert "command/UDG/20.15.2/ADD-URR.md" in idx.nodes
    assert "configobject/UDG/20.15.2/URR.md" in idx.nodes
    assert "task/UDG/20.15.2/0-00001.md" in idx.nodes
    cmd = idx.nodes["command/UDG/20.15.2/ADD-URR.md"]
    assert cmd.type == "MMLCommand" and cmd.nf == "UDG" and cmd.version == "20.15.2"
    assert ("verb", "ADD") in cmd.group


def test_build_index_id_to_path(sample_assets):
    idx = build_index(sample_assets)
    assert idx.id_to_path["UDG@20.15.2@MMLCommand@ADD URR"] == "command/UDG/20.15.2/ADD-URR.md"


def test_build_index_body_edges_and_reverse(sample_assets):
    idx = build_index(sample_assets)
    cmd = "command/UDG/20.15.2/ADD-URR.md"
    obj = "configobject/UDG/20.15.2/URR.md"
    rels = {(e.dst, e.relation_type, e.resolved) for e in idx.out_edges.get(cmd, ())}
    assert (obj, "operates_on", True) in rels
    # 反链：URR 反引 ADD URR
    assert cmd in idx.reverse.get(obj, ())


def test_build_index_placeholder_unresolved(sample_assets):
    idx = build_index(sample_assets)
    task = "task/UDG/20.15.2/0-00001.md"
    rels = {(e.dst, e.resolved) for e in idx.out_edges.get(task, ())}
    assert ("UDG@20.15.2@ConfigObject@URRGROUP", False) in rels


def test_build_index_frontmatter_derived_edge(sample_assets):
    idx = build_index(sample_assets)
    task = "task/UDG/20.15.2/0-00001.md"
    cmd = "command/UDG/20.15.2/ADD-URR.md"
    rels = {(e.dst, e.relation_type) for e in idx.out_edges.get(task, ())}
    # task.ref -> command（front-matter 派生，与正文"命令"链接去重为 ref_command）
    assert (cmd, "ref_command") in rels


def test_build_index_evidence_node(sample_assets):
    idx = build_index(sample_assets)
    ev = [p for p in idx.nodes if p.startswith("evidence/")]
    assert len(ev) == 1


def test_build_index_feature_parent_edge(sample_assets):
    idx = build_index(sample_assets)
    child = "feature/UDG/20.15.2/GWFD-020351.md"
    parent = "feature/UDG/20.15.2/GWFD-020350.md"
    rels = {(e.dst, e.relation_type, e.resolved) for e in idx.out_edges.get(child, ())}
    assert (parent, "parent", True) in rels


def test_serialize_roundtrip(sample_assets, tmp_path):
    idx = build_index(sample_assets)
    out = tmp_path / "idx.json"
    out.write_text(serialize_index(idx), encoding="utf-8")
    idx2 = deserialize_index(out.read_text(encoding="utf-8"))
    assert set(idx2.nodes) == set(idx.nodes)
    assert idx2.id_to_path == idx.id_to_path
