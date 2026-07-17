"""assets router 测试：/import /export /imports /stats。

测试隔离：用 monkeypatch 把 service 单例指向 tmp_data_dir 上的 store，
避免污染真实 platform-data。对象名用中立标识（demo/alpha），不耦合具体业务。
"""
import io
import zipfile

from fastapi.testclient import TestClient

from app.index import Index
from app.main import app
from app.registry import Registry
from app.store import Store
import app.service as svc

# 用 type=MMLCommand（注册表内建类型）做中立样例；id 用 alpha 不绑定任何业务域
CMD = (
    "---\n"
    "id: alpha@MMLCommand@ADD DEMO\n"
    "type: MMLCommand\n"
    "nf: alpha\n"
    "version: 20.15.2\n"
    "---\n"
    "# ADD DEMO\n"
)


def _zip_bytes(files: dict) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for name, content in files.items():
            z.writestr(name, content)
    buf.seek(0)
    return buf.getvalue()


def _zip_upload(files: dict):
    """构造 multipart 上传三元组 (filename, file, content_type)。"""
    return ("bundle.zip", _zip_bytes(files), "application/zip")


def _setup_service(tmp_data_dir, monkeypatch):
    """把全局单例重定向到 tmp_data_dir 上的空 store。"""
    s = svc.Service.__new__(svc.Service)
    s.store = Store(tmp_data_dir)
    s.registry = Registry.load_default()
    s.index = Index.build(s.store, s.registry)
    monkeypatch.setattr(svc, "_service", s)
    return s


def test_import_and_stats(tmp_data_dir, monkeypatch):
    _setup_service(tmp_data_dir, monkeypatch)
    with TestClient(app) as c:
        r = c.post("/api/v1/import", files={"file": _zip_upload({"a.md": CMD})})
        assert r.status_code == 200, r.text
        body = r.json()
        assert body["added"] == 1
        assert body["updated"] == 0
        assert body["skipped"] == 0
        assert body["warnings"] == []
        # counts 反映重建后的索引
        assert body["counts"]["MMLCommand"] == 1

        r2 = c.get("/api/v1/stats")
        assert r2.status_code == 200
        stats = r2.json()
        assert stats["object_counts_by_type"]["MMLCommand"] == 1
        assert stats["edge_count"] == 0
        assert "alpha" in stats["nfs"]
        assert stats["versions_per_nf"]["alpha"] == ["20.15.2"]


def test_import_update_same_id_version(tmp_data_dir, monkeypatch):
    _setup_service(tmp_data_dir, monkeypatch)
    with TestClient(app) as c:
        c.post("/api/v1/import", files={"file": _zip_upload({"a.md": CMD})})
        r2 = c.post("/api/v1/import", files={"file": _zip_upload({"b.md": CMD})})
        assert r2.status_code == 200
        body = r2.json()
        # 同 id 同版本 → updated
        assert body["added"] == 0
        assert body["updated"] == 1
        assert body["counts"]["MMLCommand"] == 1  # 仍是 1 个节点


def test_import_skips_invalid_records_warning(tmp_data_dir, monkeypatch):
    _setup_service(tmp_data_dir, monkeypatch)
    bad = "---\ntype: MMLCommand\n---\nno id here\n"
    with TestClient(app) as c:
        r = c.post("/api/v1/import",
                   files={"file": _zip_upload({"bad.md": bad, "good.md": CMD})})
        assert r.status_code == 200
        body = r.json()
        assert body["added"] == 1
        assert body["skipped"] == 1
        assert any("bad.md" in w for w in body["warnings"])


def test_imports_log(tmp_data_dir, monkeypatch):
    _setup_service(tmp_data_dir, monkeypatch)
    with TestClient(app) as c:
        # 空日志 → []
        assert c.get("/api/v1/imports").json() == []
        c.post("/api/v1/import", files={"file": _zip_upload({"a.md": CMD})})
        log = c.get("/api/v1/imports").json()
        assert len(log) == 1
        assert log[0]["added"] == 1
        assert log[0]["updated"] == 0
        assert log[0]["warnings_n"] == 0


def test_export_returns_zip(tmp_data_dir, monkeypatch):
    _setup_service(tmp_data_dir, monkeypatch)
    with TestClient(app) as c:
        c.post("/api/v1/import", files={"file": _zip_upload({"a.md": CMD})})
        r = c.get("/api/v1/export")
        assert r.status_code == 200
        assert r.headers["content-type"].startswith("application/zip")
        assert "attachment" in r.headers.get("content-disposition", "")
        # 解 zip 能看到归一化路径
        z = zipfile.ZipFile(io.BytesIO(r.content))
        names = z.namelist()
        assert "Command/alpha/20.15.2/alpha@MMLCommand@ADD DEMO.md" in names


def test_export_filter_nf_excludes_other(tmp_data_dir, monkeypatch):
    _setup_service(tmp_data_dir, monkeypatch)
    beta = CMD.replace("alpha@MMLCommand@ADD DEMO", "beta@MMLCommand@ADD DEMO") \
              .replace("nf: alpha", "nf: beta")
    with TestClient(app) as c:
        c.post("/api/v1/import",
               files={"file": _zip_upload({"a.md": CMD, "b.md": beta})})
        r = c.get("/api/v1/export", params={"nf": "alpha"})
        z = zipfile.ZipFile(io.BytesIO(r.content))
        names = z.namelist()
        assert any("alpha" in n for n in names)
        assert all("beta" not in n for n in names)


def test_overview_returns_business_nodes(tmp_data_dir, monkeypatch):
    """overview 返回业务层节点 + 业务结构边；无业务层时退化为层摘要。"""
    _setup_service(tmp_data_dir, monkeypatch)
    # 业务层两段式 id：ObjectType@语义slug（split_id 解析为 type=ObjectType）
    bd = (
        "---\n"
        "id: BusinessDomain@demo\n"
        "type: BusinessDomain\n"
        "domain: demo\n"
        "name: Demo Domain\n"
        "---\n"
        "# Demo Domain\n"
    )
    ns = (
        "---\n"
        "id: NetworkScenario@demo-base\n"
        "type: NetworkScenario\n"
        "domain: demo\n"
        "scenario: base\n"
        "name: Demo Scenario\n"
        "---\n"
        "## 边\n"
        "- belongs_to: [[BusinessDomain@demo]]\n"
    )
    with TestClient(app) as c:
        c.post("/api/v1/import",
               files={"file": _zip_upload({"bd.md": bd, "ns.md": ns, "cmd.md": CMD})})
        r = c.get("/api/v1/overview")
        assert r.status_code == 200
        body = r.json()
        ids = {n["id"] for n in body["nodes"]}
        assert "BusinessDomain@demo" in ids
        assert "NetworkScenario@demo-base" in ids
        # alpha@MMLCommand@... 是 nf 范围 → 不出现在概览
        assert "alpha@MMLCommand@ADD DEMO" not in ids
        # 业务结构边
        assert any(
            e["from"] == "NetworkScenario@demo-base"
            and e["to"] == "BusinessDomain@demo"
            for e in body["edges"]
        )


def test_overview_layer_summary_when_no_business(tmp_data_dir, monkeypatch):
    """业务层为空 → 退化为层摘要（nodes 是 Layer，无 edges）。"""
    _setup_service(tmp_data_dir, monkeypatch)
    with TestClient(app) as c:
        c.post("/api/v1/import", files={"file": _zip_upload({"a.md": CMD})})
        body = c.get("/api/v1/overview").json()
        ids = {n["id"] for n in body["nodes"]}
        assert "Command" in ids  # layer 名称
        assert body["edges"] == []


def test_browse_root_drill_paginate_filter(tmp_data_dir, monkeypatch):
    _setup_service(tmp_data_dir, monkeypatch)
    with TestClient(app) as c:
        c.post("/api/v1/import", files={"file": _zip_upload({"a.md": CMD})})
        # 根：应有 Command 目录（内部 _* 项被隐藏）
        r = c.get("/api/v1/browse")
        assert r.status_code == 200
        assert "Command" in r.json()["dirs"]
        # 钻到叶子目录 → 文件，id 由文件名派生
        r2 = c.get("/api/v1/browse", params={"path": "Command/alpha/20.15.2"})
        body2 = r2.json()
        assert any(f["id"] == "alpha@MMLCommand@ADD DEMO" for f in body2["files"])
        # q 过滤
        r3 = c.get("/api/v1/browse",
                   params={"path": "Command/alpha/20.15.2", "q": "ADD"})
        assert any("ADD" in f["name"] for f in r3.json()["files"])
        # 分页：limit=0 → 空页但 total_files 仍计全量
        r4 = c.get("/api/v1/browse",
                   params={"path": "Command/alpha/20.15.2", "limit": 0})
        assert r4.json()["files"] == []
        assert r4.json()["total_files"] >= 1
        # 不存在目录 → 空
        r5 = c.get("/api/v1/browse", params={"path": "Nope/None"})
        assert r5.json() == {"path": "Nope/None", "dirs": [], "files": [],
                             "total_files": 0, "offset": 0, "limit": 200}
