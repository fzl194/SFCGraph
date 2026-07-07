"""旧 feature-graph/data CSV 纳入（预填初值 + 黄金集对照）。

读取历史 step4 抽取的 l1_{nf}_*.csv，作为新流程的输入参考（约束4：旧数据纳入流程）：
- feature_attributes.csv → feature_type/config_required 旧值（categorize Agent 步参考 + 初值预填）
- feature_license.csv → license 黄金集（license_edge step 对照校验覆盖率）
- feature_dependency.csv → 依赖对照（dependency step 对照）

旧值仅作参考与初值，不直接覆盖新 schema 字段；categorize Agent 步负责精细化分类。
"""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


def load_legacy_attributes(legacy_dir: str | Path, nf: str) -> dict[str, dict]:
    """{feature_code: {feature_type, config_required, applicable_nf, first_release_version}}。"""
    path = Path(legacy_dir) / f"l1_{nf.lower()}_feature_attributes.csv"
    if not path.exists():
        return {}
    out: dict[str, dict] = {}
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            fid = row.get("feature_id", "").strip()
            if fid:
                out[fid] = {
                    "feature_type": (row.get("feature_type") or "").strip(),
                    "config_required": (row.get("config_required") or "").strip(),
                    "applicable_nf": (row.get("applicable_nf") or "").strip(),
                    "first_release_version": (row.get("first_release_version") or "").strip(),
                }
    return out


def load_legacy_licenses(legacy_dir: str | Path, nf: str) -> list[dict]:
    """[{feature_code, license_code, license_number, license_name}] 黄金集。"""
    path = Path(legacy_dir) / f"l1_{nf.lower()}_feature_license.csv"
    if not path.exists():
        return []
    out: list[dict] = []
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            out.append({
                "feature_code": (row.get("feature_id") or "").strip(),
                "license_code": (row.get("license_code") or "").strip(),
                "license_number": (row.get("license_number") or "").strip(),
                "license_name": (row.get("license_name") or "").strip(),
            })
    return out


def load_legacy_dependencies(legacy_dir: str | Path, nf: str) -> list[dict]:
    """[{source_feature_code, target_feature_code, dependency_type, description}] 对照。"""
    path = Path(legacy_dir) / f"l1_{nf.lower()}_feature_dependency.csv"
    if not path.exists():
        return []
    out: list[dict] = []
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            out.append({
                "source_feature_code": (row.get("source_feature_id") or "").strip(),
                "target_feature_code": (row.get("target_feature_id") or "").strip(),
                "dependency_type": (row.get("dependency_type") or "").strip(),
                "description": (row.get("description") or "").strip(),
            })
    return out


def load_legacy_file_map(legacy_dir: str | Path, nf: str) -> dict[str, list[str]]:
    """{feature_id: [file_path,...]} —— 历史 step2 特性→全部 md 映射（权威全量清单）。

    新 feature 步的 file_map 主源：比自走语料更全（含部署/激活/参考/原理等全部 md），
    同时兜住自走语料漏扫的少数特性。读 {nf}_feature_files.csv（列 feature_id,product_type,file_path）。
    文件不存在返回 {}。
    """
    path = Path(legacy_dir) / f"{nf.lower()}_feature_files.csv"
    if not path.exists():
        return {}
    out: dict[str, list[str]] = defaultdict(list)
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            fid = (row.get("feature_id") or "").strip()
            fp = (row.get("file_path") or "").strip()
            if fid and fp:
                out[fid].append(fp)
    return dict(out)
