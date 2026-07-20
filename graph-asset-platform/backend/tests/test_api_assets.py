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


def test_import_async_returns_job_and_done(tmp_data_dir, monkeypatch):
    """异步导入：上传立即 202 + job_id(processing)；后台完成后 job 变 done。"""
    _setup_service(tmp_data_dir, monkeypatch)
    with TestClient(app) as c:
        r = c.post("/api/v1/import", files={"file": _zip_upload({"a.md": CMD})})
        assert r.status_code == 202, r.text
        body = r.json()
        assert body["status"] == "processing"
        assert body["job_id"]
        # TestClient 会等 BackgroundTasks 执行完再返回响应（同步语义），故此时应已 done
        j = c.get(f"/api/v1/import/jobs/{body['job_id']}").json()
        assert j["status"] == "done"
        assert j["added"] == 1
        assert j["updated"] == 0
        assert j["skipped"] == 0
        assert j["warnings"] == []

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
        assert r2.status_code == 202
        body = r2.json()
        j = c.get(f"/api/v1/import/jobs/{body['job_id']}").json()
        # 同 id 同版本 → updated
        assert j["added"] == 0
        assert j["updated"] == 1
        # 仍是 1 个节点
        assert c.get("/api/v1/stats").json()["object_counts_by_type"]["MMLCommand"] == 1


def test_import_skips_invalid_records_warning(tmp_data_dir, monkeypatch):
    _setup_service(tmp_data_dir, monkeypatch)
    bad = "---\ntype: MMLCommand\n---\nno id here\n"
    with TestClient(app) as c:
        r = c.post("/api/v1/import",
                   files={"file": _zip_upload({"bad.md": bad, "good.md": CMD})})
        assert r.status_code == 202
        body = r.json()
        j = c.get(f"/api/v1/import/jobs/{body['job_id']}").json()
        assert j["added"] == 1
        assert j["skipped"] == 1
        assert any("bad.md" in w for w in j["warnings"])


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



# 多类型样例（命令层 + 特性层 + 业务层）测 /stats UI 层聚合
CMD2 = (
    "---\n"
    "id: alpha@MMLCommand@ADD CMD2\n"
    "type: MMLCommand\n"
    "nf: alpha\n"
    "version: 20.15.2\n"
    "---\n"
    "# ADD CMD2\n"
)
CFG2 = (
    "---\n"
    "id: alpha@ConfigObject@OBJ2\n"
    "type: ConfigObject\n"
    "nf: alpha\n"
    "version: 20.15.2\n"
    "object_kind: profile\n"
    "---\n"
    "# OBJ2\n"
)
FEAT = (
    "---\n"
    "id: alpha@Feature@F-100\n"
    "type: Feature\n"
    "nf: alpha\n"
    "version: 20.15.2\n"
    "---\n"
    "# F-100\n"
)
BD = (
    "---\n"
    "id: BusinessDomain@demo\n"
    "type: BusinessDomain\n"
    "domain: demo\n"
    "---\n"
    "# Demo Domain\n"
)


def test_stats_ui_layer_aggregation(tmp_data_dir, monkeypatch):
    """/stats per_layer 按 UI 层（4 个 Tab）聚合；ConfigObject 与 MMLCommand 合入命令层。"""
    _setup_service(tmp_data_dir, monkeypatch)
    with TestClient(app) as c:
        c.post("/api/v1/import", files={"file": _zip_upload({
            "cmd.md": CMD, "cmd2.md": CMD2, "cfg.md": CFG2,
            "feat.md": FEAT, "bd.md": BD,
        })})
        s = c.get("/api/v1/stats").json()
        per_layer = s["per_layer"]
        # 4 个 UI 层且键名正确
        assert set(per_layer.keys()) >= {"命令层", "特性层", "业务层"}
        # 命令层 = MMLCommand(2) + ConfigObject(1) = 3
        assert per_layer["命令层"] == 3
        assert per_layer["特性层"] == 1
        assert per_layer["业务层"] == 1
        # per_layer_per_nf：命令层 alpha 下 3 个
        assert s["per_layer_per_nf"]["命令层"]["alpha"] == 3
        # per_layer_per_nf_per_version：命令层 alpha 20.15.2 下 3 个
        assert s["per_layer_per_nf_per_version"]["命令层"]["alpha"]["20.15.2"] == 3
        # per_domain：demo 下 1（业务对象；nf 对象无 domain）
        assert s["per_domain"]["demo"] == 1
