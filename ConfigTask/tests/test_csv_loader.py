# ConfigTask/tests/test_csv_loader.py
import os
from builder.core.csv_loader import load_configurable_features


def test_filters_and_resolves_path(tmp_path):
    """过滤配置类文档（部署/激活/配置），排除概述；doc_path 解析为绝对路径。"""
    csv = tmp_path / "f.csv"
    # 含 UTF-8 BOM，模拟真实 UDG_feature_files.csv
    csv.write_bytes("﻿feature_id,product_type,file_path\n"
                    "GWFD-1,UDG,output/X/部署UPF_1.md\n"
                    "GWFD-2,UDG,output/X/特性概述_2.md\n"   # 概述，应排除
                    "GWFD-3,UDG,output/X/激活X_3.md\n".encode("utf-8"))
    rows = load_configurable_features(str(csv), project_root=str(tmp_path))
    # 只保留 部署/激活 文档
    assert {r.feature_id for r in rows} == {"GWFD-1", "GWFD-3"}
    # doc_path 解析为绝对路径（file_path 相对 project_root）
    assert rows[0].doc_path == os.path.normpath(str(tmp_path / "output" / "X" / "部署UPF_1.md"))


def test_no_config_docs_returns_empty(tmp_path):
    """无配置类文档时返回空列表。"""
    csv = tmp_path / "f.csv"
    csv.write_bytes("﻿feature_id,product_type,file_path\n"
                    "GWFD-2,UDG,output/X/特性概述_2.md\n".encode("utf-8"))
    rows = load_configurable_features(str(csv), project_root=str(tmp_path))
    assert rows == []
