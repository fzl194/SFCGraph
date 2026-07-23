"""鉴权中间件测试：单一 KEY 门禁；未配 KEY 旁路。

测试默认不设 GAP_API_KEY，故现有 test_api_* 不受影响（中间件旁路）。
本文件显式 monkeypatch config.API_KEY 验证鉴权生效（auth.dispatch 运行时读 config.API_KEY）。
"""
from fastapi.testclient import TestClient

import app.config as config


def _set_key(monkeypatch, key):
    """直接打 config.API_KEY（auth.dispatch 运行时读取，即时生效，无需 reload）。"""
    monkeypatch.setattr(config, "API_KEY", key)


def _clear_key(monkeypatch):
    monkeypatch.setattr(config, "API_KEY", "")


def test_no_key_configured_bypasses(tmp_data_dir, monkeypatch):
    """未配 KEY → 全放行（开发模式）。"""
    _clear_key(monkeypatch)
    from app.main import app
    with TestClient(app) as c:
        r = c.get("/api/v1/names")
        assert r.status_code == 200


def test_missing_header_returns_401(tmp_data_dir, monkeypatch):
    _set_key(monkeypatch, "secret123")
    from app.main import app
    with TestClient(app) as c:
        r = c.get("/api/v1/names")
        assert r.status_code == 401
        assert "api key" in r.json()["detail"]


def test_wrong_header_returns_401(tmp_data_dir, monkeypatch):
    _set_key(monkeypatch, "secret123")
    from app.main import app
    with TestClient(app) as c:
        r = c.get("/api/v1/names", headers={"X-API-Key": "wrong"})
        assert r.status_code == 401


def test_correct_header_passes(tmp_data_dir, monkeypatch):
    _set_key(monkeypatch, "secret123")
    from app.main import app
    with TestClient(app) as c:
        r = c.get("/api/v1/names", headers={"X-API-Key": "secret123"})
        assert r.status_code == 200


def test_non_api_path_not_guarded(tmp_data_dir, monkeypatch):
    """非 /api/ 路径（前端静态、SPA 兜底）不拦截。"""
    _set_key(monkeypatch, "secret123")
    from app.main import app
    with TestClient(app) as c:
        # 根路径 SPA 兜底返回 index.html 或 404，但绝不是 401
        r = c.get("/")
        assert r.status_code != 401
