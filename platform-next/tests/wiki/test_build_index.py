import json, time
from wiki.build_wiki_index import build_index, serialize_index, deserialize_index, update_incremental


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


def test_task_nf_version_derived_from_id(sample_assets):
    idx = build_index(sample_assets)
    t = idx.nodes["task/UDG/20.15.2/0-00001.md"]
    assert t.type == "Task"
    assert t.nf == "UDG"          # derived from id, not front-matter (front-matter now omits it)
    assert t.version == "20.15.2"


def test_update_incremental_adds_new_file(sample_assets):
    idx = build_index(sample_assets)
    cutoff = time.time()          # 此刻之前的文件不算 changed
    time.sleep(1.3)
    new = sample_assets / "task/UDG/20.15.2/0-99999.md"
    new.write_text(
        "---\nid: UDG@20.15.2@Task@0-99999\ntype: Task\ntask_layer: atom\nname: 新任务\n"
        "ref: UDG@20.15.2@MMLCommand@ADD URR\n---\n# 新任务\n## 命令\n- [ADD URR](command/UDG/20.15.2/ADD-URR.md)\n",
        encoding="utf-8")
    new_idx, n = update_incremental(idx, sample_assets, cutoff)
    assert n == 1                                                # 只重读了新增那一个
    assert "task/UDG/20.15.2/0-99999.md" in new_idx.nodes
    nn = new_idx.nodes["task/UDG/20.15.2/0-99999.md"]
    assert nn.type == "Task" and nn.nf == "UDG" and nn.version == "20.15.2"
    # fm 派生边 ref_command → ADD-URR（经 id_to_path 解析）
    out = new_idx.out_edges.get("task/UDG/20.15.2/0-99999.md", ())
    assert any(e.dst == "command/UDG/20.15.2/ADD-URR.md" and e.relation_type == "ref_command" for e in out)
    # reverse 重建后 ADD-URR 的反链含新 task
    assert "task/UDG/20.15.2/0-99999.md" in new_idx.reverse.get("command/UDG/20.15.2/ADD-URR.md", ())
    # 原节点未丢
    assert "command/UDG/20.15.2/ADD-URR.md" in new_idx.nodes


def test_update_incremental_removes_deleted(sample_assets):
    idx = build_index(sample_assets)
    cutoff = time.time(); time.sleep(1.3)
    (sample_assets / "command/UDG/20.15.2/ADD-URR.md").unlink()
    new_idx, n = update_incremental(idx, sample_assets, cutoff)
    assert n >= 1
    assert "command/UDG/20.15.2/ADD-URR.md" not in new_idx.nodes

