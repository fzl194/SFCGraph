import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from wiki.router import router
from wiki.service import WikiService


@pytest.fixture
def client(sample_assets, tmp_path, monkeypatch):
    svc = WikiService(sample_assets, tmp_path / "idx.json")
    monkeypatch.setattr("wiki.router.get_service", lambda: svc)
    app = FastAPI()
    app.include_router(router)
    return TestClient(app)


def test_categories_endpoint(client):
    r = client.get("/api/v1/wiki/categories")
    assert r.status_code == 200
    types = {c["type"] for c in r.json()}
    assert "MMLCommand" in types


def test_neighborhood_endpoint(client):
    r = client.get("/api/v1/wiki/neighborhood", params={"path": "command/UDG/20.15.2/ADD-URR.md"})
    assert r.status_code == 200
    data = r.json()
    assert data["center"]["path"] == "command/UDG/20.15.2/ADD-URR.md"


def test_md_endpoint(client):
    r = client.get("/api/v1/wiki/md", params={"path": "command/UDG/20.15.2/ADD-URR.md"})
    assert r.status_code == 200
    assert "ADD URR" in r.json()["content"]


def test_md_traversal_blocked(client):
    r = client.get("/api/v1/wiki/md", params={"path": "../../../etc/passwd"})
    assert r.status_code == 404


def test_md_unknown_returns_404(client):
    r = client.get("/api/v1/wiki/md", params={"path": "nope/missing.md"})
    assert r.status_code == 404
