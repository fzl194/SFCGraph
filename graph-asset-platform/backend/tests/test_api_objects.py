"""objects router 测试：/objects /objects/{id} /neighbors /md /subgraph。

测试隔离 + 中立命名（demo/alpha/beta），不耦合具体业务。
"""
import io
import zipfile

from fastapi.testclient import TestClient

from app.index import Index
from app.main import app
from app.registry import Registry
from app.store import Store
import app.service as svc

# MMLCommand（注册表内建类型）+ 一条指向 ConfigObject 的边
CMD_EDGES = (
    "---\n"
    "id: alpha@MMLCommand@ADD DEMO\n"
    "type: MMLCommand\n"
    "nf: alpha\n"
    "version: 20.15.2\n"
    "name: add demo command\n"
    "---\n"
    "# ADD DEMO\n"
    "## 边\n"
    "- 操作配置对象: [[alpha@ConfigObject@DEMO_OBJ]]\n"
)
# 同 id 的另一版本（测版本解析）
CMD_V2 = (
    "---\n"
    "id: alpha@MMLCommand@ADD DEMO\n"
    "type: MMLCommand\n"
    "nf: alpha\n"
    "version: 20.16.0\n"
    "---\n"
    "# ADD DEMO v2\n"
)
CFG = (
    "---\n"
    "id: alpha@ConfigObject@DEMO_OBJ\n"
    "type: ConfigObject\n"
    "nf: alpha\n"
    "version: 20.15.2\n"
    "object_kind: profile\n"
    "---\n"
    "# DEMO_OBJ\n"
)


def _setup(tmp_data_dir, monkeypatch, files):
    s = svc.Service.__new__(svc.Service)
    s.store = Store(tmp_data_dir)
    s.registry = Registry.load_default()
    s.index = Index.build(s.store, s.registry)
    # 通过 import_bundle 走归类合并（与真实 /import 同路径）
    from app.bundle import import_bundle
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for name, content in files.items():
            z.writestr(name, content)
    import_bundle(buf.getvalue(), s.store, s.registry)
    s.index = Index.build(s.store, s.registry)
    monkeypatch.setattr(svc, "_service", s)
    return s


# ---------------- /objects ----------------

def test_list_objects_filter_type(tmp_data_dir, monkeypatch):
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES, "b.md": CFG})
    with TestClient(app) as c:
        r = c.get("/api/v1/objects", params={"type": "MMLCommand"})
        assert r.status_code == 200
        rows = r.json()
        assert len(rows) == 1
        assert rows[0]["id"] == "alpha@MMLCommand@ADD DEMO"
        assert "20.15.2" in rows[0]["versions"]


def test_list_objects_search_q(tmp_data_dir, monkeypatch):
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES})
    with TestClient(app) as c:
        # name 含 "add demo"
        r = c.get("/api/v1/objects", params={"q": "add demo"})
        rows = r.json()
        assert any(o["id"] == "alpha@MMLCommand@ADD DEMO" for o in rows)
        # 无关关键字 → 空
        r2 = c.get("/api/v1/objects", params={"q": "zzznope"})
        assert r2.json() == []


def test_list_objects_dedups_versions(tmp_data_dir, monkeypatch):
    # 同 id 两版本 → 列表里只出现一行，versions 聚合两条
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES, "v2.md": CMD_V2})
    with TestClient(app) as c:
        rows = c.get("/api/v1/objects", params={"type": "MMLCommand"}).json()
        assert len(rows) == 1
        assert set(rows[0]["versions"]) == {"20.15.2", "20.16.0"}


# ---------------- /objects/{id} ----------------

def test_get_object_default_latest_version(tmp_data_dir, monkeypatch):
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES, "v2.md": CMD_V2})
    with TestClient(app) as c:
        r = c.get("/api/v1/objects/alpha@MMLCommand@ADD DEMO")  # 不带版本 → 最新
        assert r.status_code == 200
        body = r.json()
        assert body["version"] == "20.16.0"  # 语义化排序最新
        assert set(body["versions"]) == {"20.15.2", "20.16.0"}
        # out_edges 来自最新版本（v2 无边 → 空）；这里只校验结构存在
        assert isinstance(body["out_edges"], list)


def test_get_object_explicit_version_with_out_edges(tmp_data_dir, monkeypatch):
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES, "b.md": CFG})
    with TestClient(app) as c:
        r = c.get("/api/v1/objects/alpha@MMLCommand@ADD DEMO",
                  params={"version": "20.15.2"})
        assert r.status_code == 200
        body = r.json()
        assert body["version"] == "20.15.2"
        assert len(body["out_edges"]) == 1
        assert body["out_edges"][0]["to"] == "alpha@ConfigObject@DEMO_OBJ"
        assert body["out_edges"][0]["relation"] == "操作配置对象"


def test_get_object_missing_version_404_lists_available(tmp_data_dir, monkeypatch):
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES})
    with TestClient(app) as c:
        r = c.get("/api/v1/objects/alpha@MMLCommand@ADD DEMO",
                  params={"version": "9.9.9"})
        assert r.status_code == 404
        body = r.json()
        # spec §8.2：列出可用版本
        assert "20.15.2" in body["detail"]["available_versions"]


def test_get_object_unknown_id_404(tmp_data_dir, monkeypatch):
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES})
    with TestClient(app) as c:
        r = c.get("/api/v1/objects/alpha@MMLCommand@NOPE")
        assert r.status_code == 404


# ---------------- /neighbors ----------------

def test_neighbors_out_and_in(tmp_data_dir, monkeypatch):
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES, "b.md": CFG})
    with TestClient(app) as c:
        # out: ADD DEMO → DEMO_OBJ
        r = c.get("/api/v1/objects/alpha@MMLCommand@ADD DEMO/neighbors")
        assert r.status_code == 200
        body = r.json()
        assert body["center"]["id"] == "alpha@MMLCommand@ADD DEMO"
        assert any(e["to"] == "alpha@ConfigObject@DEMO_OBJ" for e in body["out"])

        # in: DEMO_OBJ 的反链指向 ADD DEMO（版本无关）
        r2 = c.get("/api/v1/objects/alpha@ConfigObject@DEMO_OBJ/neighbors")
        body2 = r2.json()
        assert any(e["from"] == "alpha@MMLCommand@ADD DEMO" for e in body2["in"])


# ---------------- /md ----------------

def test_md_raw(tmp_data_dir, monkeypatch):
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES})
    with TestClient(app) as c:
        r = c.get("/api/v1/objects/alpha@MMLCommand@ADD DEMO/md")
        assert r.status_code == 200
        assert "text/markdown" in r.headers["content-type"]
        assert "ADD DEMO" in r.text
        assert "## 边" in r.text  # raw_md 是原始全文


# ---------------- /subgraph ----------------

def test_subgraph_one_hop(tmp_data_dir, monkeypatch):
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES, "b.md": CFG})
    with TestClient(app) as c:
        r = c.get("/api/v1/subgraph",
                  params={"center": "alpha@MMLCommand@ADD DEMO", "hops": 1})
        assert r.status_code == 200
        body = r.json()
        ids = {n["id"] for n in body["nodes"]}
        assert "alpha@MMLCommand@ADD DEMO" in ids
        assert "alpha@ConfigObject@DEMO_OBJ" in ids
        assert any(e["to"] == "alpha@ConfigObject@DEMO_OBJ" for e in body["edges"])


def test_subgraph_unknown_center_404(tmp_data_dir, monkeypatch):
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES})
    with TestClient(app) as c:
        r = c.get("/api/v1/subgraph", params={"center": "alpha@MMLCommand@NOPE"})
        assert r.status_code == 404
