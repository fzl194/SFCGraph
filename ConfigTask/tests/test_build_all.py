# ConfigTask/tests/test_build_all.py
import pathlib
from build_all import make_ctx


def test_make_ctx_passes_feature_id_and_ne_fields():
    cfg = {
        "assets_root": "data/assets",
        "project_root": "..",
        "ne": {"UDG": {"20.15.2": {"feature_csv": "x.csv", "steps": ["select"]}}},
    }
    ctx = make_ctx(cfg, "UDG", "20.15.2", "GWFD-020301")
    assert ctx["nf"] == "UDG"
    assert ctx["version"] == "20.15.2"
    assert ctx["feature_id"] == "GWFD-020301"
    assert ctx["skeleton"] == []
    assert ctx["feature_csv"] == "x.csv"
    assert ctx["steps"] == ["select"]


def test_make_ctx_feature_id_none_means_no_filter():
    cfg = {"assets_root": "data/assets", "project_root": "..",
           "ne": {"UDG": {"20.15.2": {"feature_csv": "x.csv", "steps": []}}}}
    ctx = make_ctx(cfg, "UDG", "20.15.2", None)
    assert ctx["feature_id"] is None


def test_make_ctx_resolves_paths(tmp_path):
    cfg = {"assets_root": "data/assets", "project_root": "..",
           "ne": {"UDG": {"20.15.2": {"feature_csv": "x.csv", "steps": []}}}}
    ctx = make_ctx(cfg, "UDG", "20.15.2", None)
    assert isinstance(ctx["assets_root"], pathlib.Path)
    assert isinstance(ctx["project_root"], pathlib.Path)
    assert ctx["project_root"].is_absolute()  # resolved
