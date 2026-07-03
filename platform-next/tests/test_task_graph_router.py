"""Task graph router smoke 测试 (TestClient)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from shared.config import load_config
load_config()
from fastapi import FastAPI
from fastapi.testclient import TestClient
from task_graph.router import router

app = FastAPI()
app.include_router(router)
client = TestClient(app)


def test_stats():
    r = client.get("/api/v1/task-graph/stats")
    assert r.status_code == 200
    assert r.json()["total_tasks"] == 201


def test_tasks_layer():
    r = client.get("/api/v1/task-graph/tasks", params={"nf": "UDG", "version": "20.15.2", "layer": "feature"})
    assert r.status_code == 200 and r.json()["total"] == 10


def test_task_detail():
    r = client.get("/api/v1/task-graph/task", params={"nf": "UDG", "version": "20.15.2", "task_id": "2-00002"})
    assert r.status_code == 200
    j = r.json()
    assert "task_relations" in j and "parents" in j and "decision_points" in j


def test_task_tree():
    r = client.get("/api/v1/task-graph/task-tree", params={"task_id": "0-00016"})
    assert r.status_code == 200 and r.json()["center"] == "0-00016"
