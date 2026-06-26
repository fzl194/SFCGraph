# ConfigTask/tests/test_select.py
from builder.steps.select import run


def _ctx(csv_path, project_root, feature_id=None):
    return {"feature_csv": str(csv_path), "project_root": project_root, "feature_id": feature_id}


def _write_csv(tmp_path):
    csv = tmp_path / "f.csv"
    csv.write_bytes("﻿feature_id,product_type,file_path\n"
                    "GWFD-1,UDG,a/部署UPF_1.md\n"
                    "GWFD-2,UDG,b/激活X_2.md\n"
                    "GWFD-3,UDG,c/特性概述_3.md\n".encode("utf-8"))
    return csv


def test_select_no_filter_returns_all_config_docs(tmp_path):
    csv = _write_csv(tmp_path)
    ctx = _ctx(csv, str(tmp_path))
    n = run(ctx)
    assert n == 2  # 部署UPF + 激活X；特性概述被排除
    assert {d.feature_id for d in ctx["feature_docs"]} == {"GWFD-1", "GWFD-2"}


def test_select_single_feature_filters(tmp_path):
    csv = _write_csv(tmp_path)
    ctx = _ctx(csv, str(tmp_path), feature_id="GWFD-1")
    n = run(ctx)
    assert n == 1
    assert ctx["feature_docs"][0].feature_id == "GWFD-1"


def test_select_single_feature_not_found_returns_zero(tmp_path):
    csv = _write_csv(tmp_path)
    ctx = _ctx(csv, str(tmp_path), feature_id="GWFD-999")
    n = run(ctx)
    assert n == 0
    assert ctx["feature_docs"] == []
