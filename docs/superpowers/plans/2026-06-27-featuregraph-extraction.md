# FeatureGraph 特性抽取流水线 Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 `FeatureGraph/` 重构一条参考 ConfigTask 半自动化模式的抽取流水线，从特性清单 xlsx + 特性概述 md 13 节，产出对齐三层图谱 schema 的 `features.jsonl` 节点表与 `feature_depends_on` / `feature_conflicts_with` / `feature_requires_license` / `feature_relation_candidates` 边表。

**Architecture:** 复用旧 `feature-graph/step4_extract_l1.py` 的规则解析逻辑（概述识别、13 节解析、依赖/License 解析），移植到 ConfigTask 式 `@step` 装饰器 pipeline：code 步连续跑、预留 `agent=True` + `PAUSE` 机制供后续 category 校准步使用。输出统一 JSONL + 四段式实例键。数据布局统一为 `FeatureGraph/data/{nf}/{version}/`。

**Tech Stack:** Python 3.12、openpyxl（读 xlsx）、PyYAML（pipeline 配置）、pytest（测试）。纯规则抽取，零 LLM 调用（第一版）。

**关键决策（已与用户对齐）：**
1. 长文本字段全进 Feature 节点 `*_raw`（对齐 License 模式，纯规则、零幻觉、可回放）
2. `feature_type`→`feature_category`、`config_required`→`config_relevance`、`parent_feature_id`→`parent_feature_code`（catalog_parent）
3. 第一版覆盖 Feature 节点 + 依赖边 + License 边（不含 decomposes_to→ConfigTask）
4. 网元：UDG 优先跑通，UNC 同套代码 pipeline 加条目

**复用源：** `feature-graph/step4_extract_l1.py`（~1250 行，审计通过率 85.3%）、`feature-graph/step1_extract_features.py`（xlsx seed）、`feature-graph/step2_map_docs.py`（文档归属）。

---

## File Structure

**改造（FeatureGraph 现有）：**
- `FeatureGraph/build_all.py` — 改为 dict ctx + PAUSE 编排 + skip-if-exists + `--rerun`（对齐 ConfigTask）
- `FeatureGraph/builder/steps/registry.py` — 移植 `@step(name, output_file, agent)` + `STEPS`/`PRODUCT_FILE`/`AGENT_STEPS`
- `FeatureGraph/builder/steps/license.py` — 适配新 registry（加 `@step`）
- `FeatureGraph/pipeline.yaml` — 加 UDG/UNC、source/manifest/steps、数据布局统一

**新建（core 纯函数，可单测）：**
- `FeatureGraph/builder/core/seed.py` — xlsx → Feature seed（移植 step1）
- `FeatureGraph/builder/core/overview.py` — 概述md识别 + 13节解析（移植 step4，补 principle/charging 节）
- `FeatureGraph/builder/core/feature.py` — 组装 Feature 节点 + feature_category/config_relevance 推断
- `FeatureGraph/builder/core/dependency.py` — 依赖/互斥解析 + conflict_pair_id + 弱依赖归类（移植 step4）
- `FeatureGraph/builder/core/license_edge.py` — license 边解析 + 与 licenses.jsonl 对齐（移植 step4）
- `FeatureGraph/builder/core/io.py` — JSONL 读写工具（抽公共，license.py 的 load/write_jsonl 迁入）

**新建（steps 胶水）：**
- `FeatureGraph/builder/steps/feature.py` — `@step("feature")` → `features.jsonl`
- `FeatureGraph/builder/steps/dependency.py` — `@step("dependency")` → 3 个边表
- `FeatureGraph/builder/steps/license_edge.py` — `@step("license_edge")` → `feature_requires_license.jsonl`
- `FeatureGraph/builder/steps/verify.py` — `@step("verify")` → 审计报告

**新建（测试）：**
- `FeatureGraph/tests/conftest.py` — GWFD-020301 等 fixture
- `FeatureGraph/tests/test_seed.py` / `test_overview.py` / `test_feature.py` / `test_dependency.py` / `test_license_edge.py` / `test_pipeline.py`

**数据迁移：** `FeatureGraph/data/assets/{nf}/{version}/licenses.jsonl` → `FeatureGraph/data/{nf}/{version}/licenses.jsonl`

**用户约束：** 直接在 master 工作，不开分支/worktree（用户 memory 偏好）。提交遵循 conventional commits，无 Co-Authored-By（用户全局禁用归属）。

---

## Chunk 1: 基础设施（registry + build_all + pipeline + license 适配）

### Task 1: 公共 IO 工具 core/io.py

**Files:**
- Create: `FeatureGraph/builder/core/io.py`
- Test: `FeatureGraph/tests/test_io.py`

- [ ] **Step 1: Write the failing test**

```python
# FeatureGraph/tests/test_io.py
import json
from pathlib import Path
from builder.core.io import load_jsonl, write_jsonl


def test_write_then_load_roundtrip(tmp_path):
    items = [{"id": "a", "v": 1}, {"id": "b", "v": 2}]
    out = tmp_path / "x.jsonl"
    write_jsonl(out, items)
    assert [json.loads(l) for l in out.read_text(encoding="utf-8").splitlines()] == items
    assert load_jsonl(out) == items


def test_load_missing_returns_empty(tmp_path):
    assert load_jsonl(tmp_path / "nope.jsonl") == []


def test_write_creates_parent_dirs(tmp_path):
    out = tmp_path / "a" / "b" / "c.jsonl"
    write_jsonl(out, [{"id": "x"}])
    assert out.exists()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd FeatureGraph && python -m pytest tests/test_io.py -v`
Expected: FAIL（`ModuleNotFoundError: builder.core.io`）

- [ ] **Step 3: Write minimal implementation**

```python
# FeatureGraph/builder/core/io.py
"""JSONL 读写工具（FeatureGraph 公共）。"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable


def load_jsonl(path: str | Path) -> list[dict]:
    fp = Path(path)
    if not fp.exists():
        return []
    with fp.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path: str | Path, items: Iterable[dict]) -> None:
    fp = Path(path)
    fp.parent.mkdir(parents=True, exist_ok=True)
    with fp.open("w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd FeatureGraph && python -m pytest tests/test_io.py -v`
Expected: PASS (3 passed)

- [ ] **Step 5: Commit**

```bash
git add FeatureGraph/builder/core/io.py FeatureGraph/tests/test_io.py
git commit -m "feat(featuregraph): 公共 JSONL IO 工具 core/io.py"
```

---

### Task 2: registry 移植 @step 装饰器 + PAUSE 约定

**Files:**
- Modify: `FeatureGraph/builder/steps/registry.py`（整体重写）

- [ ] **Step 1: Rewrite registry.py（对齐 ConfigTask）**

```python
# FeatureGraph/builder/steps/registry.py
"""Step 注册表。每个 step 是 callable(ctx) -> int | "PAUSE"。

返回值约定：
- int（产出数）：正常完成，build_all 继续下一步
- "PAUSE"：Agent 步的待处理 prompt 输出尚未回填，build_all 打印交接信息后停

agent 步负责 prep→check→ingest，不直接调 LLM；纯文件交接
（prompts 在 data/{nf}/{version}/agent_prompts/{step}，输出在 .../agent_outputs/{step}）。
"""
STEPS: dict[str, callable] = {}
PRODUCT_FILE: dict[str, str] = {}
AGENT_STEPS: set[str] = set()


def step(name: str, output_file: str | None = None, agent: bool = False):
    """装饰器：注册一个 pipeline step。

    Args:
        name: step 名
        output_file: 输出文件名（自动步 skip-if-exists 判定）
        agent: True = Agent 步（build_all 不因输出存在跳过，总执行 prep/check）
    """
    def deco(fn):
        STEPS[name] = fn
        if output_file:
            PRODUCT_FILE[name] = output_file
        if agent:
            AGENT_STEPS.add(name)
        return fn
    return deco


# 触发各 step 模块导入，使 @step 装饰器生效
from . import license  # noqa: E402,F401
```

- [ ] **Step 2: Verify import works**

Run: `cd FeatureGraph && python -c "from builder.steps.registry import STEPS; print(sorted(STEPS))"`
Expected: 打印 `['license']`（其他 step 后续 Chunk 注册）

- [ ] **Step 3: Commit**

```bash
git add FeatureGraph/builder/steps/registry.py
git commit -m "refactor(featuregraph): registry 移植 @step 装饰器与 PAUSE 约定"
```

---

### Task 3: license step 适配新 registry

**Files:**
- Modify: `FeatureGraph/builder/steps/license.py`
- Modify: `FeatureGraph/builder/core/license.py`（load/write_jsonl 改用 core/io）

- [ ] **Step 1: license step 加 @step 装饰器**

```python
# FeatureGraph/builder/steps/license.py
"""Step license: 扫描 License 控制项文档 → licenses.jsonl。"""
from __future__ import annotations

from pathlib import Path

from ..core.license import extract_license_items
from ..core.io import write_jsonl
from ..steps.registry import step


@step("license", output_file="licenses.jsonl")
def run(ctx):
    source = Path(ctx["license_source"])
    out = Path(ctx["data_dir"]) / "licenses.jsonl"
    items = extract_license_items(source, ctx["project_root"], ctx["nf"], ctx["version"])
    write_jsonl(out, items)
    print(f"[license:{ctx['nf']}/{ctx['version']}] {len(items)} License → {out}")
    return len(items)
```

注意：`extract_license_items` 签名不变；删掉文件内本地 `write_jsonl`（改用 core/io）。

- [ ] **Step 2: core/license.py 删除本地 jsonl 读写，保留解析**

删除 `core/license.py` 中 `load_jsonl` / `write_jsonl` 两个函数（已迁至 core/io），其余解析逻辑不变。

- [ ] **Step 3: Verify license step 注册**

Run: `cd FeatureGraph && python -c "from builder.steps.registry import STEPS, PRODUCT_FILE; print('license' in STEPS, PRODUCT_FILE.get('license'))"`
Expected: `True licenses.jsonl`

- [ ] **Step 4: Commit**

```bash
git add FeatureGraph/builder/steps/license.py FeatureGraph/builder/core/license.py
git commit -m "refactor(featuregraph): license step 适配 @step + 公共 IO"
```

---

### Task 4: build_all.py 改造（dict ctx + PAUSE + skip + rerun）

**Files:**
- Modify: `FeatureGraph/build_all.py`（整体重写）

- [ ] **Step 1: Rewrite build_all.py（对齐 ConfigTask 编排）**

```python
# FeatureGraph/build_all.py
"""FeatureGraph pipeline 编排入口（半自动：自动步连续跑，Agent 步遇 PAUSE 停）。

用法:
  python build_all.py UDG 20.15.2                     # 全量（自动步 skip-if-exists）
  python build_all.py UDG 20.15.2 feature             # 只跑某步（显式单步不 skip）
  python build_all.py UDG 20.15.2 dependency --rerun GWFD-020301

模型：code → Agent(prep→PAUSE) → [填输出] → code(ingest) → ...
Agent 步不调 LLM，只把 prompt 写到 data/{nf}/{version}/agent_prompts/{step}/ 然后 PAUSE；
调 Agent 把输出写到 .../agent_outputs/{step}/ 后重跑本命令即续。
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from builder.steps.registry import STEPS, PRODUCT_FILE, AGENT_STEPS  # noqa: E402


def make_ctx(config: dict, nf: str, version: str) -> dict:
    here = pathlib.Path(__file__).parent
    ne = dict(config["ne"][nf][version])
    project_root = (here / config["project_root"]).resolve()
    license_source = ne.pop("license_source", None)
    if license_source:
        license_source = str((project_root / license_source).resolve())
    return {
        "nf": nf,
        "version": version,
        "project_root": project_root,
        "data_dir": here / "data" / nf / version,  # 网元×版本 隔离
        "license_source": license_source,
        **ne,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="FeatureGraph pipeline")
    ap.add_argument("nf", help="网元 (UDG/UNC)")
    ap.add_argument("version", help="版本 (20.15.2)")
    ap.add_argument("step", nargs="?", default=None, help="只跑某步（显式单步不 skip）")
    ap.add_argument("--rerun", default=None, help="重跑指定 feature_code/doc")
    args = ap.parse_args(argv)

    config = yaml.safe_load((HERE / "pipeline.yaml").read_text(encoding="utf-8"))
    if nf not in config["ne"] or version not in config["ne"][nf]:
        print(f"未配置 {nf}@{version}，检查 pipeline.yaml")
        return 1
    ctx = make_ctx(config, args.nf, args.version)
    if args.rerun:
        ctx["rerun_target"] = args.rerun

    single = args.step is not None
    steps_to_run = [args.step] if single else config["ne"][nf][version]["steps"]
    ctx["data_dir"].mkdir(parents=True, exist_ok=True)

    paused_at = None
    for s in steps_to_run:
        if s not in STEPS:
            print(f"{nf}@{version} {s}: 跳过（未实现）")
            continue
        if paused_at and s in AGENT_STEPS:
            print(f"  跳过 agent 步 {s}（前置 {paused_at} 待回填）")
            break
        # 全量跑：自动步输出已存在则 skip（快速续跑）；Agent 步总执行
        if not single and s not in AGENT_STEPS and not args.rerun:
            out = PRODUCT_FILE.get(s)
            if out and (ctx["data_dir"] / out).exists():
                print(f"{nf}@{version} {s}: 跳过（{out} 已存在）")
                continue

        result = STEPS[s](ctx)
        if result == "PAUSE":
            paused_at = s
            print(f"\n[PAUSE] @{s}：Agent 输出待回填 → data/{nf}/{version}/agent_outputs/{s}/<key>.json")
        else:
            print(f"{nf}@{version} {s}: {result}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Verify build_all runs (license step)**

先准备 pipeline.yaml（Task 5），再：
Run: `cd FeatureGraph && python build_all.py UDG 20.15.2 license`
Expected: license step 跑通，产出 `data/UDG/20.15.2/licenses.jsonl`

- [ ] **Step 3: Commit**

```bash
git add FeatureGraph/build_all.py
git commit -m "refactor(featuregraph): build_all 支持 PAUSE/skip/rerun（对齐 ConfigTask）"
```

---

### Task 5: pipeline.yaml 改造（数据布局统一 + UDG/UNC）

**Files:**
- Modify: `FeatureGraph/pipeline.yaml`
- 数据迁移: `data/assets/{nf}/{version}/licenses.jsonl` → `data/{nf}/{version}/licenses.jsonl`

- [ ] **Step 1: Rewrite pipeline.yaml**

```yaml
# FeatureGraph/pipeline.yaml — 换网元/版本只改这里
# data_dir 自动按 网元/版本 隔离（data/{nf}/{version}）
project_root: ..

ne:
  UDG:
    20.15.2:
      corpus_root: output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南
      license_source: output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG License描述
      manifest: FeatureGraph/UDG 20.15.2 特性清单 01.xlsx
      manifest_sheets: [1, 2]
      steps: [license, feature, dependency, license_edge, verify]
  UNC:
    20.15.2:
      corpus_root: output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南
      license_source: output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC License描述
      manifest: feature-graph/UNC 20.15.2 特性清单 01.xlsx
      manifest_sheets: [2, 3]
      steps: [license, feature, dependency, license_edge, verify]
```

> 说明：UDG manifest 直接放 `FeatureGraph/` 下（Task 6 软链或拷贝），UNC 复用 feature-graph 下既有 xlsx。`manifest_sheets` 为 step1 的 sheet 索引。

- [ ] **Step 2: Migrate existing licenses.jsonl**

Run:
```bash
mkdir -p FeatureGraph/data/UDG/20.15.2
mv FeatureGraph/data/assets/UDG/20.15.2/licenses.jsonl FeatureGraph/data/UDG/20.15.2/licenses.jsonl
```
（UNC 暂无 licenses 产物，跳过）

- [ ] **Step 3: Verify pipeline config loads + license step**

Run: `cd FeatureGraph && python build_all.py UDG 20.15.2 license`
Expected: `[license:UDG/20.15.2] 187 License → data/UDG/20.15.2/licenses.jsonl`（187 来自旧产物）

- [ ] **Step 4: Commit**

```bash
git add FeatureGraph/pipeline.yaml FeatureGraph/data/UDG/20.15.2/licenses.jsonl
git rm -r FeatureGraph/data/assets 2>/dev/null || true
git commit -m "refactor(featuregraph): pipeline.yaml 数据布局统一为 data/{nf}/{version}"
```

---

### Task 6: 拷贝 UDG 特性清单 xlsx 到 FeatureGraph

**Files:**
- Copy: `feature-graph/UDG 20.15.2 特性清单 01.xlsx` → `FeatureGraph/UDG 20.15.2 特性清单 01.xlsx`

- [ ] **Step 1: Copy manifest**

Run:
```bash
cp "feature-graph/UDG 20.15.2 特性清单 01.xlsx" "FeatureGraph/UDG 20.15.2 特性清单 01.xlsx"
```

- [ ] **Step 2: Commit**

```bash
git add "FeatureGraph/UDG 20.15.2 特性清单 01.xlsx"
git commit -m "chore(featuregraph): 引入 UDG 特性清单 xlsx 作为抽取种子"
```

---

## Chunk 2: Feature 节点抽取（seed + overview + feature + step）

### Task 7: core/seed.py — xlsx → Feature seed

**Files:**
- Create: `FeatureGraph/builder/core/seed.py`
- Test: `FeatureGraph/tests/test_seed.py`

移植 `step1_extract_features.py` 的 `extract_from_sheet` + `build_csv_fields`，去掉 CSV 输出，直接返回 dict 列表；NF 列配置参数化。

- [ ] **Step 1: Write the failing test（用 fixture 小 xlsx 或 mock）**

```python
# FeatureGraph/tests/test_seed.py
import openpyxl
from pathlib import Path
from builder.core.seed import extract_seed, UDG_NF_COLUMNS


def _make_xlsx(tmp_path):
    wb = openpyxl.Workbook()
    ws = wb.active
    # 模拟特性清单表头+目录行+叶子行
    ws.append(["特性编号", "特性名称", "GGSN(2G&3G)", "S/PGW-U(4G)", "S/PGW-U(5G NSA)", "UPF(5G)", "NB-IoT"])
    ws.append(["NFV基本特性", "", "", "", "", "", ""])        # section 行
    ws.append(["GWFD-000101", "云化分布式软件架构", "目录", "M", "M", "M", "M"])
    ws.append(["GWFD-000102", "微服务架构", "", "M", "M", "M", "M"])
    p = tmp_path / "m.xlsx"
    wb.save(p)
    return p


def test_extract_seed_parses_leaf_and_dir(tmp_path):
    feats = extract_seed(_make_xlsx(tmp_path), sheets=[0], nf_columns=UDG_NF_COLUMNS)
    assert len(feats) == 2
    f1, f2 = feats
    assert f1["feature_code"] == "GWFD-000101" and f1["is_directory"] is True
    assert f2["feature_code"] == "GWFD-000102" and f2["is_directory"] is False
    assert f2["parent_feature_code"] == "GWFD-000101"   # 目录父追踪
    assert "GGSN(2G&3G)=M" in f2["nf_support_map"]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd FeatureGraph && python -m pytest tests/test_seed.py -v`
Expected: FAIL（`ModuleNotFoundError`）

- [ ] **Step 3: Write implementation**

```python
# FeatureGraph/builder/core/seed.py
"""从特性清单 xlsx 抽取 Feature seed（移植 step1_extract_features）。

返回 dict 列表，字段对齐 schema：feature_code/name/is_directory/catalog_section/
parent_feature_code/nf_support_map/product_version。
"""
from __future__ import annotations

import re
from pathlib import Path

import openpyxl

FID_RE = re.compile(r"^(GWFD|WSFD|IPFD|NPFD)-(\d{3,6})$")

UDG_NF_COLUMNS = {
    2: "GGSN(2G&3G)", 3: "S/PGW-U(4G)", 4: "S/PGW-U(5G NSA)", 5: "UPF(5G)", 6: "NB-IoT",
}
UNC_NF_COLUMNS = {
    2: "SGSN(2.5&3G)", 3: "GGSN-C(2.5&3G)", 4: "MME(4G)", 5: "S/PGW-C(4G)",
    6: "NB-IoT(4G)", 7: "5G MME(5G NSA)", 8: "5G S/PGW-C(5G NSA)",
    9: "AMF(5G SA)", 10: "SMF(5G SA)", 11: "NRF(5G SA)",
}


def extract_seed(xlsx_path: str | Path, sheets: list[int], nf_columns: dict[int, str]) -> list[dict]:
    """读指定 sheet，返回 Feature seed dict 列表（按 feature_code 去重）。"""
    wb = openpyxl.load_workbook(xlsx_path, read_only=True)
    out: list[dict] = []
    for idx in sheets:
        ws = wb.worksheets[idx]
        out.extend(_extract_sheet(ws, nf_columns))
    wb.close()
    # 去重
    seen, result = set(), []
    for f in out:
        if f["feature_code"] not in seen:
            seen.add(f["feature_code"])
            result.append(f)
    return result


def _extract_sheet(ws, nf_columns: dict[int, str]) -> list[dict]:
    features, current_section, current_parent_fid = [], "", ""
    for row in ws.iter_rows(min_row=1, values_only=True):
        col0 = str(row[0]).strip() if row[0] else ""
        col1 = str(row[1]).strip() if row[1] else ""
        col2 = str(row[2]).strip() if len(row) > 2 and row[2] else ""

        if not FID_RE.match(col0):
            if col0 and not col1 and col0 not in ("E", "N", "M", "-"):
                current_section, current_parent_fid = col0, ""
            continue

        fid, is_dir = col0, (col2 == "目录")
        if is_dir:
            current_parent_fid = fid

        nf_map = {}
        for col_idx, col_name in nf_columns.items():
            val = ""
            if col_idx < len(row) and row[col_idx] is not None:
                val = str(row[col_idx]).strip()
            if val and val != "_":
                nf_map[col_name] = val

        features.append({
            "feature_code": fid,
            "name": col1,
            "is_directory": is_dir,
            "catalog_section": current_section,
            "parent_feature_code": current_parent_fid if not is_dir else "",
            "nf_support_map": "; ".join(f"{k}={v}" for k, v in nf_map.items()),
            "product_version": "20.15.2",
        })
    return features
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd FeatureGraph && python -m pytest tests/test_seed.py -v`
Expected: PASS

- [ ] **Step 5: Verify against real xlsx**

Run: `cd FeatureGraph && python -c "from builder.core.seed import extract_seed, UDG_NF_COLUMNS; f=extract_seed('UDG 20.15.2 特性清单 01.xlsx', [1,2], UDG_NF_COLUMNS); print(len(f), f[0])"`
Expected: ~303 条，首条字段正确

- [ ] **Step 6: Commit**

```bash
git add FeatureGraph/builder/core/seed.py FeatureGraph/tests/test_seed.py
git commit -m "feat(featuregraph): core/seed.py xlsx→Feature seed（移植 step1）"
```

---

### Task 8: core/overview.py — 概述md识别 + 13节解析

**Files:**
- Create: `FeatureGraph/builder/core/overview.py`
- Test: `FeatureGraph/tests/test_overview.py`

移植 `step4_extract_l1.py` 的 `find_overview_md` / `parse_overview_sections` / `extract_*`。**补 `principle_raw` / `charging_raw` 两节**（旧版漏抽）。所有节统一走 `*_raw` 原文保留。

- [ ] **Step 1: Write the failing test**

```python
# FeatureGraph/tests/test_overview.py
from builder.core.overview import parse_sections, SECTION_KEYS, extract_applicable_nf, extract_first_release

SAMPLE = """# GWFD-020301 概述

#### [适用NF](#x)

SGW-U、PGW-U、UPF

#### [定义](#x)

内容计费是包过滤和分析技术。

#### [原理概述](#x)

简单来讲，内容计费就是对不同业务类型使用不同计费策略。

#### [计费与话单](#x)

本特性不涉及计费与话单。

#### [发布历史](#x)

| 特性版本 | 发布版本 | 发布说明 |
| --- | --- | --- |
| 01 | 20.0.0 | 首次发布。 |
"""


def test_parse_sections_keeps_all_13_keys_including_principle_charging():
    sections = parse_sections(SAMPLE)
    assert "适用NF" in sections and "定义" in sections
    assert "原理概述" in sections          # 旧版漏抽，已补
    assert "计费与话单" in sections         # 旧版漏抽，已补


def test_extract_applicable_nf_normalizes():
    sections = parse_sections(SAMPLE)
    assert extract_applicable_nf(sections) == ["SGW-U", "PGW-U", "UPF"]


def test_extract_first_release_from_history():
    sections = parse_sections(SAMPLE)
    assert extract_first_release(sections) == "20.0.0"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd FeatureGraph && python -m pytest tests/test_overview.py -v`
Expected: FAIL

- [ ] **Step 3: Write implementation**

```python
# FeatureGraph/builder/core/overview.py
"""概述md识别 + 13节解析（移植 step4，补 原理概述/计费与话单 节）。

概述md固定 13 节：适用NF/定义/客户价值/应用场景/可获得性/与其他特性的交互/
对系统的影响/应用限制/原理概述/计费与话单/特性规格/遵循标准/发布历史。
全部按 #### [节名](anchor) 锚点拆分。
"""
from __future__ import annotations

import os
import re
from pathlib import Path

SECTION_ANCHOR_RE = re.compile(r"^####\s*\[([^\]]+)\]")
OVERVIEW_SECTIONS = {"定义", "可获得性", "应用场景"}
FEATURE_ID_RE = re.compile(r"^((?:GWFD|WSFD|IPFD|NPFD|SFFD)-\d{3,6})")

# schema 13 节 → *_raw 字段名
SECTION_KEYS = {
    "适用NF": "applicable_nf_raw",
    "定义": "definition_raw",
    "客户价值": "customer_value_raw",
    "应用场景": "application_scenario_raw",
    "可获得性": "availability_raw",
    "与其他特性的交互": "feature_interaction_raw",
    "对系统的影响": "system_impact_raw",
    "应用限制": "restrictions_raw",
    "原理概述": "principle_raw",
    "计费与话单": "charging_raw",
    "特性规格": "spec_raw",
    "遵循标准": "standards_raw",
    "发布历史": "release_history_raw",
}


def parse_sections(content: str) -> dict[str, str]:
    """按 #### [节名] 拆分 → {节名: 节正文}。"""
    sections, current, lines = {}, None, []
    for line in content.split("\n"):
        m = SECTION_ANCHOR_RE.match(line)
        if m:
            if current:
                sections[current] = "\n".join(lines).strip()
            current, lines = m.group(1), []
        elif current:
            lines.append(line)
    if current:
        sections[current] = "\n".join(lines).strip()
    return sections


def collect_raw_fields(sections: dict[str, str]) -> dict[str, str]:
    """13 节 → *_raw 字段，缺节给空串。"""
    return {field: sections.get(name, "") for name, field in SECTION_KEYS.items()}


def is_overview_by_structure(content: str) -> bool:
    found = OVERVIEW_SECTIONS.intersection(set(SECTION_ANCHOR_RE.findall(content)))
    return len(found) >= 2


def classify_doc_type(filename: str, content: str, dir_path: str = "") -> str:
    h1 = (re.search(r"^#\s+(.+)$", content, re.MULTILINE) or [None, ""])[1] if re.search(r"^#\s+(.+)$", content, re.MULTILINE) else ""
    if "概述" in filename:
        return "overview"
    if h1:
        if "激活" in h1 or re.search(r"^配置", h1):
            return "activation"
        if "调测" in h1:
            return "debug"
        if "参考信息" in h1:
            return "reference"
        if "原理" in h1:
            return "principle"
        if "流程" in h1:
            return "flow"
    if "实现原理" in (os.path.basename(dir_path) if dir_path else ""):
        return "principle"
    return "other"


def is_direct_child(file_path: str, feature_id: str) -> bool:
    """文件是否直接在特性目录下（移植 step4）。"""
    parent = os.path.dirname(file_path)
    parent_name = os.path.basename(parent)
    filename = os.path.basename(file_path)
    if filename.startswith(feature_id) and FEATURE_ID_RE.match(parent_name) and FEATURE_ID_RE.match(parent_name).group(1) == feature_id:
        return True
    fid_in_parent = FEATURE_ID_RE.match(parent_name)
    if fid_in_parent and fid_in_parent.group(1) == feature_id:
        return True
    # 简化：文件名以 feature_id 开头即可（覆盖主目录扁平放置）
    return filename.startswith(feature_id)


def find_overview_md(feature_id: str, file_paths: list[str], project_root: Path) -> tuple[str | None, list[tuple[str, str]]]:
    """为特性找概述md + 构建全部 doc_assets。返回 (overview_relpath, [(file_path, doc_type)])。

    优先级：1.文件名含'概述' 2.文件名以 fid 开头+直接子 3.仅1文件 4.内容结构验证
    """
    overview_candidates, other_files = [], []
    for fp in file_paths:
        filename = os.path.basename(fp)
        if "概述" in filename:
            overview_candidates.append((1, fp))
        elif filename.startswith(feature_id) and is_direct_child(fp, feature_id):
            overview_candidates.append((2, fp))
        else:
            other_files.append(fp)
    if not overview_candidates and len(file_paths) == 1:
        overview_candidates.append((3, file_paths[0]))
    if not overview_candidates:
        for fp in file_paths:
            abs_fp = project_root / fp if not Path(fp).is_absolute() else Path(fp)
            if abs_fp.exists() and is_overview_by_structure(abs_fp.read_text(encoding="utf-8", errors="ignore")):
                overview_candidates.append((4, fp))
    overview_path = min(overview_candidates, key=lambda x: x[0])[1] if overview_candidates else None

    doc_assets = []
    if overview_path:
        doc_assets.append((overview_path, "overview"))
    for fp in file_paths:
        if fp == overview_path:
            continue
        abs_fp = project_root / fp if not Path(fp).is_absolute() else Path(fp)
        content = abs_fp.read_text(encoding="utf-8", errors="ignore") if abs_fp.exists() else ""
        doc_assets.append((fp, classify_doc_type(os.path.basename(fp), content, os.path.dirname(fp))))
    return overview_path, doc_assets


def extract_applicable_nf(sections: dict[str, str]) -> list[str]:
    """从 适用NF 节归一化；空则回退 可获得性 的涉及NF表。"""
    for key in sections:
        if re.match(r"适\s*用\s*N\s*F", key) and sections[key]:
            return [nf.strip() for nf in re.split(r"[、，,\n]", sections[key]) if nf.strip()]
    # 回退：可获得性 的涉及NF表
    avail = sections.get("可获得性", "")
    in_nf_table = False
    for line in avail.split("\n"):
        parts = [p.strip() for p in line.strip().split("|")]
        parts = [re.sub(r"^\*\*(.+?)\*\*$", r"\1", p) for p in parts if p and p != "---"]
        if not parts:
            continue
        first = parts[0]
        if first in ("涉及NF", "适用NF", "涉及网元", "适用网元"):
            in_nf_table = True
            continue
        if in_nf_table and parts:
            result = [nf.strip() for nf in re.split(r"[、，,\n]", parts[0]) if nf.strip()]
            if result and any("-" in nf or "U" in nf.upper() for nf in result):
                return result
            in_nf_table = False
    return []


def extract_first_release(sections: dict[str, str]) -> str:
    text = sections.get("发布历史", "")
    for line in text.split("\n"):
        if "首次发布" in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 2:
                v = re.sub(r"<[^>]+>", "", parts[1])
                v = re.sub(r"^(UDG|UNC)\s*", "", v)
                v = re.sub(r"\s*及后续版本.*$", "", v)
                return v.strip()
    return ""
```

> 说明：`standards` 结构化解析（旧 `extract_standards`）较大，作为 `extract_standards()` 补在本文件末尾（移植 step4 原函数，返回 `[{category,number,name}]`），Task 9 feature 组装时用。

- [ ] **Step 4: Add extract_standards（移植 step4）**

在 `overview.py` 末尾追加 `extract_standards(sections) -> list[dict]`（原样移植 step4 第 419-509 行，返回 `[{category, number, name}]`）。

- [ ] **Step 5: Run test to verify it passes**

Run: `cd FeatureGraph && python -m pytest tests/test_overview.py -v`
Expected: PASS (3 passed)

- [ ] **Step 6: Commit**

```bash
git add FeatureGraph/builder/core/overview.py FeatureGraph/tests/test_overview.py
git commit -m "feat(featuregraph): core/overview.py 概述识别+13节解析(补原理/计费节)"
```

---

### Task 9: core/feature.py — 组装节点 + category/relevance 推断

**Files:**
- Create: `FeatureGraph/builder/core/feature.py`
- Test: `FeatureGraph/tests/test_feature.py`

- [ ] **Step 1: Write the failing test**

```python
# FeatureGraph/tests/test_feature.py
from builder.core.feature import build_feature_node, infer_feature_category, infer_config_relevance


def _seed(code="GWFD-020301", name="内容计费基本功能", section="年费基本包-智能策略控制&计费基本包"):
    return {"feature_code": code, "name": name, "is_directory": False,
            "catalog_section": section, "parent_feature_code": "", "nf_support_map": "",
            "product_version": "20.15.2"}


def test_build_feature_node_four_part_id_and_raw_fields():
    seed = _seed()
    raws = {"definition_raw": "内容计费...", "applicable_nf_raw": "SGW-U、PGW-U、UPF",
            "principle_raw": "", "charging_raw": ""}
    node = build_feature_node(seed, raws, applicable_nf=["SGW-U", "PGW-U", "UPF"],
                              first_release="20.0.0", standards=[], overview_path="a/b.md", nf="UDG", version="20.15.2")
    assert node["id"] == "UDG@20.15.2@Feature@GWFD-020301"
    assert node["applicable_nf"] == ["SGW-U", "PGW-U", "UPF"]
    assert node["definition_raw"] == "内容计费..."
    assert node["has_overview"] == "yes"


def test_infer_category_by_section():
    assert infer_feature_category("年费基本包-智能策略控制&计费基本包", "计费") == "enhanced"
    assert infer_feature_category("服务化架构功能", "云化分布式软件架构") == "base"
    assert infer_feature_category("可靠性功能", "故障恢复") == "operations"


def test_infer_config_relevance_no_config():
    assert infer_config_relevance(has_activation=False, no_config_needed=True) == "none"
    assert infer_config_relevance(has_activation=True, no_config_needed=False) == "required"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd FeatureGraph && python -m pytest tests/test_feature.py -v`
Expected: FAIL

- [ ] **Step 3: Write implementation**

```python
# FeatureGraph/builder/core/feature.py
"""组装 Feature 节点 + feature_category/config_relevance 推断。

对齐 schema §2.1 三类字段：原始md字段(*_raw) + 抽取归一化字段 + 来源上下文字段。
"""
from __future__ import annotations

# catalog_section 关键词 → feature_category（主锚点）
_SECTION_CATEGORY = [
    (["计费", "策略控制"], "enhanced"),
    (["带宽", "shaping", "流量控制"], "enhanced"),
    (["QoS"], "enhanced"),
    (["接入", "会话"], "protocol"),
    (["地址", "IPv6", "双栈"], "protocol"),
    (["可靠性", "故障", "自愈", "扩容", "缩容"], "operations"),
    (["License"], "operations"),
    (["SFIP", "第三方", "集成"], "integration"),
    (["架构", "服务化", "NFV", "底座", "SA-Basic", "SA框架"], "base"),
]
_DEFINITION_CATEGORY = [
    (["计费", "策略", "过滤"], "enhanced"),
    (["地址分配", "隧道", "接入"], "protocol"),
    (["可靠性", "扩容", "缩容", "自愈"], "operations"),
    (["架构", "分布式", "微服务"], "base"),
]


def infer_feature_category(catalog_section: str, definition: str) -> str:
    """以 catalog_section 为主锚点 + 定义关键词辅助。未命中默认 enhanced。"""
    text = (catalog_section or "") + " " + (definition or "")
    for keywords, cat in _SECTION_CATEGORY:
        if any(kw.lower() in text.lower() for kw in keywords):
            return cat
    for keywords, cat in _DEFINITION_CATEGORY:
        if any(kw in (definition or "") for kw in keywords):
            return cat
    return "enhanced"


def infer_config_relevance(has_activation: bool, no_config_needed: bool) -> str:
    """有激活文档→required；无激活+声明无需配置→none；其余 required（保守）。"""
    if no_config_needed and not has_activation:
        return "none"
    return "required"


def build_feature_node(seed: dict, raw_fields: dict, *, applicable_nf: list[str],
                       first_release: str, standards: list[dict], overview_path: str | None,
                       nf: str, version: str, has_overview: str = "yes") -> dict:
    """组装单个 Feature 节点（四段式 id + 全部 *_raw + 归一化 + 上下文）。"""
    code = seed["feature_code"]
    has_activation_hint = bool(raw_fields.get("availability_raw", ""))  # 占位；激活文档判定见 step
    category = infer_feature_category(seed.get("catalog_section", ""), raw_fields.get("definition_raw", ""))
    node = {
        # 归一化
        "id": f"{nf}@{version}@Feature@{code}",
        "feature_code": code,
        "name": seed.get("name", ""),
        "is_directory": seed.get("is_directory", False),
        "catalog_section": seed.get("catalog_section", ""),
        "parent_feature_code": seed.get("parent_feature_code", ""),
        "applicable_nf": applicable_nf,
        "nf_support_map": seed.get("nf_support_map", ""),
        "first_release_version": first_release,
        "standards": standards,
        "feature_category": category,
        "config_relevance": "required",  # 默认；step 依据激活文档覆盖
        # 上下文
        "nf": nf,
        "version": version,
        "source_path": overview_path or "",
        "has_overview": has_overview,
    }
    # 原始md字段（13节 *_raw）合并
    node.update(raw_fields)
    return node
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd FeatureGraph && python -m pytest tests/test_feature.py -v`
Expected: PASS (3 passed)

- [ ] **Step 5: Commit**

```bash
git add FeatureGraph/builder/core/feature.py FeatureGraph/tests/test_feature.py
git commit -m "feat(featuregraph): core/feature.py 节点组装+category/relevance推断"
```

---

### Task 10: steps/feature.py — feature step → features.jsonl

**Files:**
- Create: `FeatureGraph/builder/steps/feature.py`
- Modify: `FeatureGraph/builder/steps/registry.py`（末尾加 `from . import feature`）

- [ ] **Step 1: Write feature step**

```python
# FeatureGraph/builder/steps/feature.py
"""Step feature: xlsx seed + 概述md 13节解析 → features.jsonl 节点表。"""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

from ..core.io import write_jsonl
from ..core.seed import extract_seed, UDG_NF_COLUMNS, UNC_NF_COLUMNS
from ..core.overview import find_overview_md, parse_sections, collect_raw_fields, extract_applicable_nf, extract_first_release, extract_standards
from ..core.feature import build_feature_node, infer_config_relevance
from .registry import step

NF_COLUMNS = {"UDG": UDG_NF_COLUMNS, "UNC": UNC_NF_COLUMNS}


def _scan_feature_docs(corpus_root: Path, valid_fids: set[str], project_root: Path) -> dict[str, list[str]]:
    """移植 step2：md 归属到路径上最深层特性。返回 {feature_code: [relpath,...]}。"""
    import re
    pat = re.compile(r"^(GWFD|WSFD|IPFD|NPFD)-(\d{3,6})\s")
    mapping = defaultdict(list)
    for root, dirs, files in os.walk(corpus_root):
        dirs[:] = [d for d in dirs if not d.endswith(".assets")]
        path_fids = []
        for part in Path(root).parts:
            m = pat.match(part)
            if m:
                path_fids.append(f"{m.group(1)}-{m.group(2)}")
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            fid = path_fids[-1] if path_fids else ""
            if not fid:
                m = re.match(r"^(GWFD|WSFD|IPFD|NPFD)-(\d{3,6})", fn)
                fid = f"{m.group(1)}-{m.group(2)}" if m else ""
            if fid and fid in valid_fids:
                rel = str((Path(root) / fn).relative_to(project_root)).replace("\\", "/")
                mapping[fid].append(rel)
    return mapping


import os  # noqa: E402


@step("feature", output_file="features.jsonl")
def run(ctx):
    nf, version = ctx["nf"], ctx["version"]
    project_root = ctx["project_root"]
    manifest = project_root / ctx["manifest"] if not Path(ctx["manifest"]).is_absolute() else Path(ctx["manifest"])
    corpus_root = project_root / ctx["corpus_root"]

    seeds = extract_seed(manifest, ctx.get("manifest_sheets", [1, 2]), NF_COLUMNS[nf])
    valid_fids = {s["feature_code"] for s in seeds if not s["is_directory"]}
    file_map = _scan_feature_docs(corpus_root, valid_fids, project_root)

    nodes, stats = [], {"total": 0, "has_overview_yes": 0, "no_docs": 0, "no_overview": 0}
    for seed in seeds:
        if seed["is_directory"]:
            continue  # 目录特性不入节点表（第一版）
        stats["total"] += 1
        code = seed["feature_code"]
        fps = file_map.get(code, [])
        if not fps:
            node = build_feature_node(seed, {}, applicable_nf=[], first_release="",
                                      standards=[], overview_path=None, nf=nf, version=version, has_overview="no_docs")
            nodes.append(node); stats["no_docs"] += 1; continue

        overview_path, doc_assets = find_overview_md(code, fps, project_root)
        has_activation = any(dt == "activation" for _, dt in doc_assets)
        if not overview_path:
            node = build_feature_node(seed, {}, applicable_nf=[], first_release="",
                                      standards=[], overview_path=None, nf=nf, version=version, has_overview="no_overview")
            nodes.append(node); stats["no_overview"] += 1; continue

        abs_ov = project_root / overview_path if not Path(overview_path).is_absolute() else Path(overview_path)
        content = abs_ov.read_text(encoding="utf-8", errors="ignore") if abs_ov.exists() else ""
        if len(content.strip()) < 50:
            node = build_feature_node(seed, {}, applicable_nf=[], first_release="",
                                      standards=[], overview_path=overview_path, nf=nf, version=version, has_overview="empty")
            nodes.append(node); continue

        sections = parse_sections(content)
        raws = collect_raw_fields(sections)
        no_config = "无需配置" in sections.get("可获得性", "")
        node = build_feature_node(seed, raws,
                                  applicable_nf=extract_applicable_nf(sections),
                                  first_release=extract_first_release(sections),
                                  standards=extract_standards(sections),
                                  overview_path=overview_path, nf=nf, version=version, has_overview="yes")
        node["config_relevance"] = infer_config_relevance(has_activation, no_config)
        nodes.append(node); stats["has_overview_yes"] += 1

    out = Path(ctx["data_dir"]) / "features.jsonl"
    write_jsonl(out, nodes)
    print(f"[feature:{nf}/{version}] {len(nodes)} Feature（overview={stats['has_overview_yes']}, "
          f"no_overview={stats['no_overview']}, no_docs={stats['no_docs']}）→ {out}")
    return len(nodes)
```

- [ ] **Step 2: Register feature step**

在 `registry.py` 末尾 `from . import license` 后加 `from . import feature  # noqa`。

- [ ] **Step 3: Verify step runs**

Run: `cd FeatureGraph && python build_all.py UDG 20.15.2 feature`
Expected: ~220 叶子 Feature，overview≈217，对齐旧抽取报告

- [ ] **Step 4: Spot-check GWFD-020301**

Run: `cd FeatureGraph && python -c "import json; [print(json.dumps(json.loads(l),ensure_ascii=False,indent=1)) for l in open('data/UDG/20.15.2/features.jsonl',encoding='utf-8') if 'GWFD-020301' in l]"`
Expected: `id=UDG@20.15.2@Feature@GWFD-020301`、`applicable_nf=[SGW-U,PGW-U,UPF]`、`principle_raw`/`charging_raw` 非空、`feature_category=enhanced`、`config_relevance=required`

- [ ] **Step 5: Commit**

```bash
git add FeatureGraph/builder/steps/feature.py FeatureGraph/builder/steps/registry.py
git commit -m "feat(featuregraph): feature step xlsx+概述13节→features.jsonl"
```

---

## Chunk 3: 依赖/License 边抽取

### Task 11: core/dependency.py — 依赖/互斥/candidates + conflict_pair_id

**Files:**
- Create: `FeatureGraph/builder/core/dependency.py`
- Test: `FeatureGraph/tests/test_dependency.py`

移植 `step4_extract_l1.py` 的 `extract_feature_dependencies`（4/3/2列 + URL笔误纠正 + 名称模糊匹配），按 schema 拆成 `depends_on`/`conflicts_with`/candidates 三组，补四段式 id 与 conflict_pair_id。

- [ ] **Step 1: Write the failing test**

```python
# FeatureGraph/tests/test_dependency.py
from builder.core.dependency import extract_dependencies, classify_edges

INTERACTION = """| 交互类型 | 相关特性 | 控制项名称 | 交互说明 |
| --- | --- | --- | --- |
| 依赖 | [GWFD-110101 SA-Basic](../GWFD-110101 SA-Basic_x.md) | 82209749 SA-Basic | 必须先开启SA。 |
| 互斥 | [GWFD-020302 基于业务时长](../GWFD-020302_y.md) | 无 | 不能同时使用。 |
"""


def test_extract_dependencies_depends_and_conflict():
    raws = {"feature_interaction_raw": INTERACTION}
    deps = extract_dependencies("GWFD-020301", raws, feature_lookup={})
    assert any(d["target_feature_code"] == "GWFD-110101" and d["raw_type"] == "depends_on" for d in deps)
    assert any(d["target_feature_code"] == "GWFD-020302" and d["raw_type"] == "conflicts_with" for d in deps)


def test_classify_edges_splits_and_adds_pair_id():
    raws = {"feature_interaction_raw": INTERACTION}
    deps = extract_dependencies("GWFD-020301", raws, feature_lookup={})
    edges = classify_edges(deps, nf="UDG", version="20.15.2")
    assert len(edges["depends_on"]) == 1 and len(edges["conflicts_with"]) == 1
    assert edges["conflicts_with"][0]["conflict_pair_id"].startswith("conflict:")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd FeatureGraph && python -m pytest tests/test_dependency.py -v`
Expected: FAIL

- [ ] **Step 3: Write implementation（移植 step4，schema 化）**

```python
# FeatureGraph/builder/core/dependency.py
"""依赖/互斥/弱语义解析（移植 step4 extract_feature_dependencies）。

输入 Feature 节点的 feature_interaction_raw（"与其他特性的交互"节原文），
返回扁平 dep 列表；classify_edges 再按 schema 拆 depends_on/conflicts_with/candidates
并补四段式 source_id/target_id 与 conflict_pair_id。
"""
from __future__ import annotations

import re

FEATURE_ID_SEARCH_RE = re.compile(r"((?:GWFD|WSFD|IPFD|NPFD|SFFD)-\d{3,6})")
URL_FID_RE = re.compile(r"\([^)]*?((?:GWFD|WSFD|IPFD|NPFD|SFFD)-\d{3,6})[^)]*\)")

WEAK_TYPES = {"affects", "interacts_with", "supports", "other"}


def _lookup_by_name(raw_name: str, feature_lookup: dict) -> str:
    name = raw_name.strip()
    m = re.match(r"\[([^\]]+)\]", name)
    if m:
        name = m.group(1).strip()
    if name in ("NA", "-", "无", "—", "N/A", "不涉及", "无。"):
        return ""
    matches = [fid for fid, fname in feature_lookup.items()
               if fname and (name in fname or fname in name)]
    return matches[0] if len(matches) == 1 else ""


def extract_dependencies(feature_code: str, raw_fields: dict, feature_lookup: dict) -> list[dict]:
    """解析 feature_interaction_raw → 扁平 dep 列表（含 raw_type/desc/control_item）。"""
    text = raw_fields.get("feature_interaction_raw", "")
    if not text or "不涉及" in text:
        return []

    # 检测表头列数
    table_cols = 0
    for line in text.split("\n"):
        parts = [p.strip("*").strip() for p in line.strip().split("|") if p.strip() and p.strip() != "---"]
        if "相关特性" in parts or "交互类型" in parts:
            table_cols = len(parts)
            break

    deps = []
    for line in text.split("\n"):
        parts = [p.strip() for p in line.strip().split("|")]
        parts = [p for p in parts if p and p != "---"]
        if len(parts) < 2:
            continue
        h0, h1 = parts[0].strip("*").strip(), (parts[1].strip("*").strip() if len(parts) > 1 else "")
        if h0 in ("交互类型", "交互") or h1 in ("相关特性", "和其他特性的交互关系"):
            continue

        if len(parts) >= 4:
            dep_type_raw, related, control, desc = parts[0], parts[1], parts[2] if len(parts) > 2 else "", parts[3] if len(parts) > 3 else ""
        elif len(parts) == 3:
            dep_type_raw, related, desc, control = parts[0], parts[1], parts[2], ""
        elif len(parts) == 2:
            dep_type_raw, related, desc, control = "交互", parts[0], parts[1], ""
        else:
            continue

        control = re.sub(r"<[^>]+>", "", re.sub(r"<br\s*/?>", "; ", control)).strip()
        url_m = URL_FID_RE.search(related)
        target = url_m.group(1) if url_m else (FEATURE_ID_SEARCH_RE.search(related).group(1) if FEATURE_ID_SEARCH_RE.search(related) else "")
        if not target and feature_lookup:
            target = _lookup_by_name(related, feature_lookup)
        desc = re.sub(r"<[^>]+>", " ", re.sub(r"<br\s*/?>", " ", desc)).strip()

        dep_type = _normalize_type(dep_type_raw)
        if target == feature_code:
            continue
        if len(dep_type) > 10 and dep_type == dep_type_raw:  # 未映射长句
            continue
        if not target:
            continue
        deps.append({"source_feature_code": feature_code, "target_feature_code": target,
                     "raw_type": dep_type, "description": desc, "control_item": control,
                     "source_type": "overview_explicit"})
    return deps


def _normalize_type(dep_type_raw: str) -> str:
    if dep_type_raw in ("依赖", "必须先开启"):
        return "depends_on"
    if dep_type_raw in ("互斥", "冲突"):
        return "conflicts_with"
    if dep_type_raw in ("影响", "与其他特性的影响", "与其他特性间的影响", "其他可能的影响"):
        return "affects"
    if dep_type_raw in ("被影响", "其他"):
        return "other"
    if "协同" in dep_type_raw:
        return "cooperates_with"
    if dep_type_raw == "支持":
        return "supports"
    if "交互" in dep_type_raw or "关系" in dep_type_raw:
        return "interacts_with"
    return dep_type_raw


def classify_edges(deps: list[dict], nf: str, version: str) -> dict[str, list[dict]]:
    """拆 depends_on / conflicts_with / candidates，补四段式 id + conflict_pair_id。"""
    def src(d): return f"{nf}@{version}@Feature@{d['source_feature_code']}"
    def tgt(d): return f"{nf}@{version}@Feature@{d['target_feature_code']}"

    result = {"depends_on": [], "conflicts_with": [], "candidates": []}
    for d in deps:
        base = {"source_id": src(d), "relation_type": d["raw_type"], "target_id": tgt(d),
                "nf": nf, "version": version, "source_feature_code": d["source_feature_code"],
                "target_feature_code": d["target_feature_code"], "description": d["description"],
                "control_item": d["control_item"], "source_type": d["source_type"],
                "edge_id": f"{src(d)}|{d['raw_type']}|{tgt(d)}"}
        if d["raw_type"] == "depends_on":
            result["depends_on"].append(base)
        elif d["raw_type"] == "conflicts_with":
            pair = sorted([d["source_feature_code"], d["target_feature_code"]])
            base["conflict_pair_id"] = f"conflict:{pair[0]}-{pair[1]}"
            result["conflicts_with"].append(base)
        else:  # cooperates_with 也暂进 candidates 待审，或单列；第一版进 candidates
            base["raw_type"] = d["raw_type"]
            result["candidates"].append(base)
    return result
```

> 注意：`cooperates_with` 第一版进 candidates（弱语义待审），与 schema §3.4 一致；`affects/interacts_with/supports/other` 同。

- [ ] **Step 4: Run test to verify it passes**

Run: `cd FeatureGraph && python -m pytest tests/test_dependency.py -v`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add FeatureGraph/builder/core/dependency.py FeatureGraph/tests/test_dependency.py
git commit -m "feat(featuregraph): core/dependency.py 依赖/互斥/candidates+conflict_pair_id"
```

---

### Task 12: steps/dependency.py — dependency step → 3 边表

**Files:**
- Create: `FeatureGraph/builder/steps/dependency.py`
- Modify: `registry.py`（加 import）

- [ ] **Step 1: Write dependency step**

```python
# FeatureGraph/builder/steps/dependency.py
"""Step dependency: 读 features.jsonl 的 feature_interaction_raw → 解析边表。

输出：feature_depends_on.jsonl / feature_conflicts_with.jsonl / feature_relation_candidates.jsonl
"""
from __future__ import annotations

from pathlib import Path

from ..core.io import load_jsonl, write_jsonl
from ..core.dependency import extract_dependencies, classify_edges
from .registry import step


@step("dependency", output_file="feature_depends_on.jsonl")
def run(ctx):
    nf, version = ctx["nf"], ctx["version"]
    features = load_jsonl(Path(ctx["data_dir"]) / "features.jsonl")
    feature_lookup = {f["feature_code"]: f.get("name", "") for f in features}

    all_depends, all_conflicts, all_candidates = [], [], []
    rerun = ctx.get("rerun_target")
    for f in features:
        if rerun and rerun not in f["feature_code"]:
            continue
        deps = extract_dependencies(f["feature_code"], f, feature_lookup)
        edges = classify_edges(deps, nf, version)
        all_depends += edges["depends_on"]
        all_conflicts += edges["conflicts_with"]
        all_candidates += edges["candidates"]

    # depends_on 去重（同 source/target/type）
    all_depends = _dedup(all_depends)
    all_conflicts = _dedup(all_conflicts)

    data_dir = Path(ctx["data_dir"])
    write_jsonl(data_dir / "feature_depends_on.jsonl", all_depends)
    write_jsonl(data_dir / "feature_conflicts_with.jsonl", all_conflicts)
    write_jsonl(data_dir / "feature_relation_candidates.jsonl", all_candidates)
    print(f"[dependency:{nf}/{version}] depends_on={len(all_depends)} "
          f"conflicts={len(all_conflicts)} candidates={len(all_candidates)}")
    return len(all_depends) + len(all_conflicts)


def _dedup(edges: list[dict]) -> list[dict]:
    seen, out = set(), []
    for e in edges:
        k = e["edge_id"]
        if k not in seen:
            seen.add(k); out.append(e)
    return out
```

- [ ] **Step 2: Register + run**

`registry.py` 加 `from . import dependency  # noqa`。
Run: `cd FeatureGraph && python build_all.py UDG 20.15.2 dependency`
Expected: depends_on≈（UDG 旧值 288 量级），conflicts 含 conflict_pair_id

- [ ] **Step 3: Verify against old data**

Run: `cd FeatureGraph && python -c "import json; d=[json.loads(l) for l in open('data/UDG/20.15.2/feature_depends_on.jsonl',encoding='utf-8')]; print('depends_on',len(d))"`
Expected: 数量接近旧 `l1_udg_feature_dependency.csv` 中 UDG depends_on 行数

- [ ] **Step 4: Commit**

```bash
git add FeatureGraph/builder/steps/dependency.py FeatureGraph/builder/steps/registry.py
git commit -m "feat(featuregraph): dependency step 解析依赖/互斥/候选边表"
```

---

### Task 13: core/license_edge.py + steps/license_edge.py

**Files:**
- Create: `FeatureGraph/builder/core/license_edge.py`
- Create: `FeatureGraph/builder/steps/license_edge.py`
- Test: `FeatureGraph/tests/test_license_edge.py`

移植 `step4_extract_l1.py` 的 `extract_licenses`（多列表格 + 单行 + 纯文本 3 格式），转成 `requires_license` 边（与已成的 `licenses.jsonl` 节点对齐：`target_id` 用 license_code 四段式）。

- [ ] **Step 1: Write the failing test**

```python
# FeatureGraph/tests/test_license_edge.py
from builder.core.license_edge import extract_license_edges_from_feature

AVAIL = """**License** **支持**

本特性对应的License控制项为 "82209822 LKV3G5BCBC01 内容计费基本功能 "。
"""


def test_extract_license_edge_links_feature_to_license():
    raws = {"availability_raw": AVAIL}
    edges = extract_license_edges_from_feature("GWFD-020301", raws, nf="UDG", version="20.15.2")
    assert len(edges) == 1
    e = edges[0]
    assert e["license_code"] == "LKV3G5BCBC01"
    assert e["source_id"] == "UDG@20.15.2@Feature@GWFD-020301"
    assert e["target_id"] == "UDG@20.15.2@License@LKV3G5BCBC01"
    assert e["source_type"] == "feature_overview"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd FeatureGraph && python -m pytest tests/test_license_edge.py -v`
Expected: FAIL

- [ ] **Step 3: Write core/license_edge.py（移植 extract_licenses 的格式识别，输出边）**

```python
# FeatureGraph/builder/core/license_edge.py
"""从 Feature 的 availability_raw 解析 requires_license 边（移植 step4 extract_licenses）。

输出边字段对齐 schema §3.5：source_id(Feature)/target_id(License)/feature_code/license_code/
control_item_id/source_type=feature_overview。License 节点本身来自 licenses.jsonl。
"""
from __future__ import annotations

import re

LICENSE_CELL_RE = re.compile(r"([A-Za-z0-9]{6,12})\s+([A-Za-z0-9_\-]+)\s+(.+)")


def extract_license_edges_from_feature(feature_code: str, raw_fields: dict, *, nf: str, version: str) -> list[dict]:
    text = raw_fields.get("availability_raw", "")
    if not text or ("无需" in text and "License" in text):
        return []

    licenses = _parse_table(text) or _parse_quoted(text) or _parse_plain(text)
    src = f"{nf}@{version}@Feature@{feature_code}"
    edges = []
    for lic in licenses:
        name = (lic.get("license_name") or "").strip().rstrip("|\"'")
        if not name or len(name) < 2 or name in ("License控制项", "License支持"):
            continue
        edges.append({
            "source_id": src, "relation_type": "requires_license",
            "target_id": f"{nf}@{version}@License@{lic['license_code']}",
            "nf": nf, "version": version,
            "feature_code": feature_code, "license_code": lic["license_code"],
            "control_item_id": lic.get("license_number", ""),
            "source_type": "feature_overview",
            "edge_id": f"{src}|requires_license|{nf}@{version}@License@{lic['license_code']}",
        })
    return edges


def _parse_table(text: str) -> list[dict]:
    """License 表格（适用NF/涉及NF/特性 × License控制项，2~3列）。返回 [{license_number,license_code,license_name}] 或 []。"""
    in_table, lic_col, licenses = False, -1, []
    for line in text.split("\n"):
        parts = [p.strip() for p in line.strip().split("|")]
        parts = [p for p in parts if p and p != "---"]
        if not in_table:
            for i, p in enumerate(parts):
                pc = p.strip("*").strip()
                if pc.startswith("License") and len(pc) <= 20:
                    lic_col = i; break
            if lic_col >= 0 and len(parts) >= 2:
                in_table = True
            continue
        if not parts or len(parts) <= lic_col:
            in_table, lic_col = False, -1; continue
        cell = re.sub(r"<br\s*/?>", " ", parts[lic_col].rstrip(" |").strip())
        m = LICENSE_CELL_RE.match(cell)
        if m:
            licenses.append({"license_number": m.group(1), "license_code": m.group(2),
                             "license_name": m.group(3).strip().rstrip(" |")})
        else:
            in_table, lic_col = False, -1
    return licenses


def _parse_quoted(text: str) -> list[dict]:
    m = re.search(r'["“”\'‘’]+([A-Za-z0-9]{6,12})\s+([A-Za-z0-9_\-]+)\s+(.+?)["“”\'‘’]', text, re.MULTILINE)
    if m:
        return [{"license_number": m.group(1), "license_code": m.group(2),
                 "license_name": m.group(3).strip().rstrip("。")}]
    return []


def _parse_plain(text: str) -> list[dict]:
    out = []
    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("|") or not line:
            continue
        m = re.search(r"([A-Za-z0-9]{6,12})\s+([A-Za-z0-9_\-]+)\s+(.+?)(?:\s*[。.]|$)", line)
        if m:
            name = m.group(3).strip().rstrip("。|")
            if name and len(name) > 2:
                out.append({"license_number": m.group(1), "license_code": m.group(2), "license_name": name})
    return out
```

- [ ] **Step 4: Write steps/license_edge.py**

```python
# FeatureGraph/builder/steps/license_edge.py
"""Step license_edge: 读 features.jsonl 的 availability_raw → feature_requires_license.jsonl。"""
from __future__ import annotations

from pathlib import Path

from ..core.io import load_jsonl, write_jsonl
from ..core.license_edge import extract_license_edges_from_feature
from .registry import step


@step("license_edge", output_file="feature_requires_license.jsonl")
def run(ctx):
    nf, version = ctx["nf"], ctx["version"]
    features = load_jsonl(Path(ctx["data_dir"]) / "features.jsonl")
    edges, seen = [], set()
    rerun = ctx.get("rerun_target")
    for f in features:
        if rerun and rerun not in f["feature_code"]:
            continue
        for e in extract_license_edges_from_feature(f["feature_code"], f, nf=nf, version=version):
            if e["edge_id"] not in seen:
                seen.add(e["edge_id"]); edges.append(e)
    out = Path(ctx["data_dir"]) / "feature_requires_license.jsonl"
    write_jsonl(out, edges)
    print(f"[license_edge:{nf}/{version}] {len(edges)} requires_license 边 → {out}")
    return len(edges)
```

- [ ] **Step 5: Register + run**

`registry.py` 加 `from . import license_edge  # noqa`。
Run: `cd FeatureGraph && python -m pytest tests/test_license_edge.py -v && python build_all.py UDG 20.15.2 license_edge`
Expected: 测试 PASS；UDG 边数接近旧 470 量级

- [ ] **Step 6: Commit**

```bash
git add FeatureGraph/builder/core/license_edge.py FeatureGraph/builder/steps/license_edge.py FeatureGraph/tests/test_license_edge.py FeatureGraph/builder/steps/registry.py
git commit -m "feat(featuregraph): license_edge step 概述可获得性→requires_license边"
```

---

## Chunk 4: 审计 + 端到端 + UNC + 文档

### Task 14: steps/verify.py — 审计 step

**Files:**
- Create: `FeatureGraph/builder/steps/verify.py`
- Modify: `registry.py`（加 import）

检查 schema 禁止关系与数据完整性：① Feature 不直连命令/参数/ConfigObject（本层天然满足，留空检）；② depends_on/conflicts 的 target 必须是已存在 Feature；③ requires_license 的 target 必须在 licenses.jsonl；④ 弱依赖未误入核心边表；⑤ 输出审计 md。

- [ ] **Step 1: Write verify step**

```python
# FeatureGraph/builder/steps/verify.py
"""Step verify: FeatureGraph 数据完整性审计 → audit_report.md。"""
from __future__ import annotations

from pathlib import Path

from ..core.io import load_jsonl
from .registry import step


@step("verify")
def run(ctx):
    nf, version = ctx["nf"], ctx["version"]
    d = Path(ctx["data_dir"])
    features = load_jsonl(d / "features.jsonl")
    licenses = load_jsonl(d / "licenses.jsonl")
    depends = load_jsonl(d / "feature_depends_on.jsonl")
    conflicts = load_jsonl(d / "feature_conflicts_with.jsonl")
    req_lic = load_jsonl(d / "feature_requires_license.jsonl")
    candidates = load_jsonl(d / "feature_relation_candidates.jsonl")

    feat_ids = {f["feature_code"] for f in features}
    lic_ids = {l["id"] for l in licenses}

    dangling_dep = [e for e in depends if e["target_feature_code"] not in feat_ids]
    dangling_conf = [e for e in conflicts if e["target_feature_code"] not in feat_ids]
    dangling_lic = [e for e in req_lic if e["target_id"] not in lic_ids]

    lines = [
        f"# FeatureGraph 审计报告 {nf}@{version}",
        "",
        "## 概要",
        f"- Feature 节点: {len(features)}",
        f"- License 节点: {len(licenses)}",
        f"- depends_on 边: {len(depends)}（悬空 target: {len(dangling_dep)}）",
        f"- conflicts_with 边: {len(conflicts)}（悬空 target: {len(dangling_conf)}）",
        f"- requires_license 边: {len(req_lic)}（未对齐 License 节点: {len(dangling_lic)}）",
        f"- 候选弱关系: {len(candidates)}（不应进核心边表，已隔离）",
        "",
    ]
    if dangling_dep:
        lines.append(f"## depends_on 悬空 target（前20）")
        for e in dangling_dep[:20]:
            lines.append(f"- {e['source_feature_code']} → {e['target_feature_code']}")
        lines.append("")
    if dangling_lic:
        lines.append(f"## requires_license 未对齐 License 节点（前20）")
        for e in dangling_lic[:20]:
            lines.append(f"- {e['feature_code']} → {e['license_code']}")
        lines.append("")

    out = d / "audit_report.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    issues = len(dangling_dep) + len(dangling_conf) + len(dangling_lic)
    print(f"[verify:{nf}/{version}] 悬空/未对齐问题: {issues} → {out}")
    return issues  # 0 = clean
```

- [ ] **Step 2: Register + run full pipeline**

`registry.py` 加 `from . import verify  # noqa`。
Run: `cd FeatureGraph && python build_all.py UDG 20.15.2`
Expected: 全步跑通，verify 打印悬空问题数

- [ ] **Step 3: Commit**

```bash
git add FeatureGraph/builder/steps/verify.py FeatureGraph/builder/steps/registry.py
git commit -m "feat(featuregraph): verify step 数据完整性审计(悬空target/license对齐)"
```

---

### Task 15: 端到端对比旧数据

**Files:** 无（验证任务）

- [ ] **Step 1: Full UDG run**

Run: `cd FeatureGraph && python build_all.py UDG 20.15.2`
Expected: license=187, feature≈220, depends_on≈288量级, requires_license≈470量级, verify 问题可控

- [ ] **Step 2: Compare counts vs old extraction**

| 指标 | 旧值（参考） | 新值目标 |
|---|---|---|
| Feature 叶子 | 220（UDG有文档） | ≈220 |
| depends_on+其他 | 288（UDG dep 行） | depends_on 占大头 |
| requires_license | 470（UDG+UNC） | UDG 单测≈占比 |
| License 节点 | 187 | 187（不变） |

Run 抽查命令核对：
```bash
cd FeatureGraph && for f in features feature_depends_on feature_conflicts_with feature_requires_license feature_relation_candidates; do echo "$f: $(wc -l < data/UDG/20.15.2/$f.jsonl)"; done
```

- [ ] **Step 3: Fix any regression（如某节漏抽、URL笔误未纠正）**

若 verify 报悬空 target 异常多，回到 core/dependency.py 对照 step4 原逻辑排查（尤其 URL_FID_RE / 名称匹配）。

- [ ] **Step 4: Commit（如有修复）**

```bash
git add -A FeatureGraph
git commit -m "fix(featuregraph): 端到端对比旧数据回归修复"
```

---

### Task 16: UNC 接入

**Files:**
- Modify: `FeatureGraph/pipeline.yaml`（UNC 条目已在 Task 5）

- [ ] **Step 1: 确认 UNC corpus_root / license_source / manifest 路径存在**

Run:
```bash
ls "output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南" | head -3
ls "feature-graph/UNC 20.15.2 特性清单 01.xlsx"
```

- [ ] **Step 2: Full UNC run**

Run: `cd FeatureGraph && python build_all.py UNC 20.15.2`
Expected: UNC 特性≈433 有文档，依赖≈419量级，license≈量级

- [ ] **Step 3: Commit UNC 产物（如纳入 git）**

```bash
git add FeatureGraph/data/UNC
git commit -m "feat(featuregraph): UNC 20.15.2 抽取接入"
```

---

### Task 17: 更新 历史 feature-graph 复用审视.md 与 README

**Files:**
- Modify: `FeatureGraph/历史feature-graph复用审视.md`（标注复用已完成）
- Create: `FeatureGraph/README.md`（流水线用法）

- [ ] **Step 1: 在审视.md §6 后补"执行结论"**

标注：seed/overview/dependency/license_edge 代码已移植并 JSONL 化，feature_type→feature_category 等改造已落地，弱依赖隔离为 candidates。

- [ ] **Step 2: Write README.md**

```markdown
# FeatureGraph 特性图谱抽取

从特性清单 xlsx + 特性概述 md 抽取三层图谱特性层对象。

## 用法
    cd FeatureGraph
    python build_all.py UDG 20.15.2            # 全量
    python build_all.py UDG 20.15.2 feature    # 单步
    python build_all.py UDG 20.15.2 dependency --rerun GWFD-020301

## 产物（data/{nf}/{version}/）
- licenses.jsonl / features.jsonl（节点）
- feature_depends_on / feature_conflicts_with / feature_requires_license.jsonl（边）
- feature_relation_candidates.jsonl（弱关系待审）
- audit_report.md

schema 见 `特性层对象与关系定义.md`。
```

- [ ] **Step 3: Commit**

```bash
git add FeatureGraph/历史feature-graph复用审视.md FeatureGraph/README.md
git commit -m "docs(featuregraph): 复用审视结论 + README"
```

---

## 备注：feature_category 口径校准（后续，非阻塞第一版）

第一版 `infer_feature_category` 用 `catalog_section` 关键词映射，准确率有限。后续可选：
- 设 `agent=True` 的 `categorize` 步（参考 ConfigTask Agent 步模型：prep 写 prompt → PAUSE → 回填 → ingest），让 LLM 结合 definition/principle 校准 category
- 或待 ConfigTask 接入后，按 `decomposes_to` 覆盖情况反推 `config_relevance`

本计划不实现此步（YAGNI），仅保留 registry 的 `agent=True`/`PAUSE` 基础设施。

---

## v2 调整（双 reviewer 审查后，2026-06-27）

### A. reviewer 草稿质量修复
- `core/license_edge.py` 补 `_HARDCODED_LICENSES`（WSFD-106201 转置表，否则 0 边而非 4 边）
- `classify_doc_type` 改回 step4 简洁写法（`h1_match = re.search(...); h1 = h1_match.group(1) if h1_match else ""`）
- `steps/feature.py` 的 `import os`/`import re` 提到模块级
- `extract_standards` 给完整代码（移植 step4 三格式）+ 补测试
- `build_feature_node` 删死变量 `has_activation_hint`
- `core/license.py` 删 jsonl 函数时明确"无内部调用者，外部仅 steps/license.py（已重写）"
- `license_edge._parse_table` 丢弃表格 NF 列（边表无需 applicable_nf），注明
- `has_overview` 补 `file_missing` 第 5 态分支
- 边表补 `source_evidence_ids` 选填字段
- Task 15 计数表 470 拆分（UDG≈137 / UNC≈333）

### B. 用户执行约束融入
- **约束2（Agent 断点）**：新增 `categorize` Agent 步（prep→PAUSE→ingest），接管 `feature_category`/`config_relevance` 精细化分类；纯规则 `infer_feature_category` 降级为 prep 初值预填。`classify_relation`（candidates→cooperates_with 升级）列为次优先可后续。
- **约束3（第一批 2-3 个）**：build_all 加 `--sample CODE1,CODE2`，feature/dependency/license_edge/categorize 步尊重过滤。第一批用 `GWFD-020301,GWFD-020302,GWFD-020306`（计费标杆）。
- **约束4（旧数据纳入）**：新增 `core/legacy.py` 读旧 CSV；seed 预填 `feature_type→feature_category` 初值 / `config_required→config_relevance` 初值；categorize prompt 附旧值作参考；license_edge 用旧 `l1_*_feature_license.csv` 做对照校验。
- build_all PAUSE **不 break**（对齐 ConfigTask，尾随 verify 仍跑）。

### C. 新增/调整文件
- 新增 `builder/core/legacy.py`（旧 CSV 读取 + 预填初值 + 对照）
- 新增 `builder/core/categorize.py`（Agent 步 prep/check/ingest）
- 新增 `builder/steps/categorize.py`（`@step("categorize", agent=True)`）
- 新增 `builder/agent/prompts.py`（`CATEGORIZE_PROMPT`）
- pipeline steps 调整：`[license, feature, dependency, license_edge, categorize, verify]`（categorize 在 license_edge 后、verify 前）

### D. 第一批范围（代码优先，不全量）
代码步先全量能力就绪，但**第一批执行用 `--sample` 只跑 3 个特性验证全链路**；categorize Agent 步生成 prompt 后，用这 2-3 个特性回填验证 ingest。全量待第一批通过后再跑。
