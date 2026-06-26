# ConfigTask/builder/core/csv_loader.py
"""读 feature_files.csv → 过滤配置类文档 → 解析绝对路径。"""
import csv
import os
from dataclasses import dataclass

from builder.constants import CONFIG_DOC_PREFIXES


@dataclass
class FeatureDoc:
    feature_id: str
    product_type: str
    doc_path: str  # 绝对路径（file_path 相对 project_root 解析）


def load_configurable_features(csv_path, project_root):
    """读 CSV，只保留配置类文档（文件名以 部署/激活/配置 开头），doc_path 解析为绝对路径。

    Args:
        csv_path: feature_files.csv 路径
        project_root: SFCGraph 根，file_path 相对它解析
    Returns:
        list[FeatureDoc]
    """
    out = []
    # utf-8-sig 自动去除真实 CSV 开头的 UTF-8 BOM
    with open(csv_path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            fname = os.path.basename(row["file_path"])
            if fname.startswith(CONFIG_DOC_PREFIXES):
                abs_path = os.path.normpath(os.path.join(project_root, row["file_path"]))
                out.append(FeatureDoc(row["feature_id"], row["product_type"], abs_path))
    return out
