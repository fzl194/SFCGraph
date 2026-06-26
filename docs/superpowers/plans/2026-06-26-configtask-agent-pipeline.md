# ConfigTask Agent Pipeline Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement. Steps use `- [ ]` syntax.

**Goal:** Build a ConfigTask extraction pipeline (3 Agent stages + code verification) that produces config_tasks.jsonl + task_rules.jsonl + decision_points.jsonl from 655 configuration documents.

**Architecture:** Unified pipeline aligned with CommandGraph (pipeline.yaml + build_all.py + step registry). Agent output verified by code at each stage. Progress tracking for resume/no-omission.

**Tech Stack:** Python 3.12, pytest, Agent (subagent dispatch), JSONL I/O.

**Spec:** `docs/superpowers/specs/2026-06-26-configtask-agent-pipeline-design.md`

---

## File Structure

```
ConfigTask/
├── pipeline.yaml                  ← Create: config entry point
├── build_all.py                    ← Create: orchestration
├── builder/
│   ├── __init__.py                 ← Existing
│   ├── constants.py                ← Existing (keep)
│   ├── core/
│   │   ├── __init__.py             ← Existing
│   │   ├── md_reader.py            ← Existing (keep)
│   │   └── commands.py             ← Existing (keep)
│   ├── steps/
│   │   ├── __init__.py             ← Create: auto-import all steps
│   │   ├── registry.py             ← Create: STEPS/PRODUCT_FILE/validate_order
│   │   ├── scan.py                 ← Create: migrate from scripts/scan_corpus.py
│   │   ├── extract_steps.py        ← Create: migrate from scripts/extract_steps.py
│   │   ├── split_tasks.py          ← Create: Agent-1 orchestrator
│   │   ├── verify_split.py         ← Create: split verification
│   │   ├── cluster.py              ← Create: command-set clustering
│   │   ├── merge_fields.py         ← Create: Agent-2 orchestrator
│   │   ├── verify_merge.py         ← Create: merge verification
│   │   ├── extract_rules.py        ← Create: Agent-3 orchestrator
│   │   ├── verify_rules.py         ← Create: rules verification
│   │   └── assemble.py             ← Create: final assembly
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── prompts.py              ← Create: 3 Agent prompt templates
│   │   └── runner.py               ← Create: batch dispatch + progress + retry
│   └── verify/
│       ├── __init__.py
│       ├── completeness.py         ← Create: no-missing/no-duplicate check
│       ├── contiguity.py           ← Create: step_range coverage check
│       └── object_family.py        ← Create: command family coherence check
├── data/
│   ├── corpus_manifest.csv         ← Existing
│   ├── doc_steps.jsonl             ← Existing
│   └── progress/                   ← Create at runtime
├── tests/
│   ├── conftest.py                 ← Create: fixtures
│   ├── test_completeness.py        ← Create: TDD for completeness check
│   ├── test_contiguity.py          ← Create: TDD for contiguity check
│   ├── test_object_family.py       ← Create: TDD for family check
│   └── test_cluster.py             ← Create: TDD for clustering
├── scripts/                         ← Delete after migration
│   ├── scan_corpus.py              ← Delete (migrated to steps/scan.py)
│   └── extract_steps.py            ← Delete (migrated to steps/extract_steps.py)
└── (docs: CONFIGTASK_SCHEMA.md, PIPELINE_DESIGN.md, etc. — keep)
```

---

## Chunk 1: Pipeline Foundation

### Task 1: Create pipeline.yaml + step registry + build_all.py

**Files:**
- Create: `ConfigTask/pipeline.yaml`
- Create: `ConfigTask/builder/steps/__init__.py`
- Create: `ConfigTask/builder/steps/registry.py`
- Create: `ConfigTask/build_all.py`

- [ ] **Step 1: Create pipeline.yaml**

```yaml
# ConfigTask pipeline 配置入口
assets_root: data/assets
project_root: ..

ne:
  UDG:
    20.15.2:
      corpus_root: output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南
      command_graph_dir: CommandGraph/data/assets/UDG/20.15.2
      steps: [scan, extract_steps, split_tasks, verify_split,
              cluster, merge_fields, verify_merge,
              extract_rules, verify_rules, assemble]
      agent_batch_size: 5
  UNC:
    20.15.2:
      corpus_root: output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南
      command_graph_dir: CommandGraph/data/assets/UNC/20.15.2
      steps: [scan, extract_steps, split_tasks, verify_split,
              cluster, merge_fields, verify_merge,
              extract_rules, verify_rules, assemble]
      agent_batch_size: 5
```

- [ ] **Step 2: Create step registry**

```python
# ConfigTask/builder/steps/registry.py
"""Step 注册表。每个 step 是 callable(ctx) -> int(产出数)。"""
STEPS = {}
PRODUCT_FILE = {}  # step_name -> output filename

def step(name, output_file=None):
    """装饰器：注册一个 pipeline step。"""
    def deco(fn):
        STEPS[name] = fn
        if output_file:
            PRODUCT_FILE[name] = output_file
        return fn
    return deco
```

- [ ] **Step 3: Create steps/__init__.py (auto-import)**

```python
# ConfigTask/builder/steps/__init__.py
"""导入所有 step 模块以触发注册。"""
# 代码 steps
from . import scan, extract_steps, cluster, assemble  # noqa: F401
# 核查 steps
from . import verify_split, verify_merge, verify_rules  # noqa: F401
# Agent steps (后续创建)
# from . import split_tasks, merge_fields, extract_rules  # noqa: F401
```

- [ ] **Step 4: Create build_all.py**

```python
# ConfigTask/build_all.py
"""ConfigTask pipeline 编排入口。
用法:
  python build_all.py UDG 20.15.2                    # 全量
  python build_all.py UDG 20.15.2 split_tasks         # 只跑某步
  python build_all.py UDG 20.15.2 split_tasks --rerun GWFD-020301  # 重跑某文档
"""
import argparse
import json
import pathlib
import yaml

from builder.steps.registry import STEPS


def make_ctx(config, nf, version):
    """构造 step 上下文。"""
    here = pathlib.Path(__file__).parent
    ne = config["ne"][nf][version]
    return {
        "nf": nf,
        "version": version,
        "project_root": (here / config["project_root"]).resolve(),
        "data_dir": here / "data",
        "assets_root": here / config["assets_root"],
        "command_graph_dir": None,  # 由 ne 填充
        **ne,
    }


def main():
    ap = argparse.ArgumentParser(description="ConfigTask pipeline")
    ap.add_argument("nf", help="网元 (UDG/UNC)")
    ap.add_argument("version", help="版本 (20.15.2)")
    ap.add_argument("step", nargs="?", default=None, help="只跑某步")
    ap.add_argument("--rerun", default=None, help="重跑指定文档/簇")
    args = ap.parse_args()

    config = yaml.safe_load(
        open(pathlib.Path(__file__).parent / "pipeline.yaml", encoding="utf-8")
    )
    ctx = make_ctx(config, args.nf, args.version)
    if args.rerun:
        ctx["rerun_target"] = args.rerun

    steps_to_run = [args.step] if args.step else ctx["steps"]
    for s in steps_to_run:
        if s not in STEPS:
            print(f"  跳过未实现的 step: {s}")
            continue
        n = STEPS[s](ctx)
        print(f"{args.nf}@{args.version} {s}: {n}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Commit**

```bash
cd D:/mywork/KnowledgeBase/SFCGraph
git add ConfigTask/pipeline.yaml ConfigTask/builder/steps/__init__.py ConfigTask/builder/steps/registry.py ConfigTask/build_all.py
git commit -m "feat(configtask): pipeline foundation (pipeline.yaml + registry + build_all)"
```

---

### Task 2: Migrate scan_corpus.py → steps/scan.py

**Files:**
- Create: `ConfigTask/builder/steps/scan.py`
- Delete: `ConfigTask/scripts/scan_corpus.py` (after migration)

- [ ] **Step 1: Create steps/scan.py (migrate logic from scripts/scan_corpus.py)**

```python
# ConfigTask/builder/steps/scan.py
"""Step 0: 扫描语料目录 → corpus_manifest.csv"""
import csv
import re
import pathlib

from builder.steps.registry import step

FEATURE_ID_RE = re.compile(r'((?:GWFD|WSFD|IPFD|NPFD)-\d{6})')


@step("scan", output_file="corpus_manifest.csv")
def run(ctx):
    """扫描 corpus_root 下所有 md，标记 has_task_example/has_operation_steps/has_operation_flow。"""
    root = ctx["project_root"] / ctx["corpus_root"]
    data_dir = ctx["data_dir"]
    data_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for md in root.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        rel = md.relative_to(ctx["project_root"])
        parts = md.relative_to(root).parts
        fid_match = FEATURE_ID_RE.search(str(rel))
        results.append({
            "product": ctx["nf"],
            "feature_id": fid_match.group(1) if fid_match else "",
            "category": parts[0] if parts else "",
            "doc_name": md.stem,
            "has_task_example": "任务示例" in text,
            "has_operation_steps": "操作步骤" in text,
            "has_operation_flow": "操作流程" in text,
            "doc_path": str(rel).replace("\\", "/"),
        })

    out = data_dir / "corpus_manifest.csv"
    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        w.writeheader()
        w.writerows(results)

    n_eligible = sum(1 for r in results if r["has_task_example"] and r["has_operation_steps"])
    print(f"  扫描 {len(results)} md, {n_eligible} 可抽 task")
    return len(results)
```

- [ ] **Step 2: Migrate extract_steps.py → steps/extract_steps.py**

```python
# ConfigTask/builder/steps/extract_steps.py
"""Step 1: 从语料抽步骤三元组 → doc_steps.jsonl"""
import csv
import json
import re
import sys
import pathlib

from builder.steps.registry import step
from builder.core.md_reader import read_sections
from builder.constants import SECTION_STEPS, SECTION_FLOW

_CMD_RE = re.compile(r'\b(ADD|SET|MOD|DEL|RMV|LST|DSP|LOD|SWP|RST|EXP|ACT|DEA)\s+(\w+)\b')
_STEP_START_RE = re.compile(r'^\s*(\d+)\.\s', re.MULTILINE)
_DIFF_KEYWORDS = ("参考部署", "此处仅描述差异", "详细配置请参考", "此处仅描述")


def parse_step_triplets(steps_text):
    """操作步骤段 → [(step_num, step_desc, commands[], raw_text)]"""
    starts = [(m.start(), int(m.group(1))) for m in _STEP_START_RE.finditer(steps_text)]
    triplets = []
    for i, (start, num) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(steps_text)
        block = steps_text[start:end].strip()
        desc_m = re.match(r'\s*\d+\.\s*(.+?)(?:\n|。)', block)
        desc = desc_m.group(1).strip() if desc_m else ""
        raw_cmds = [f"{v} {k}" for v, k in _CMD_RE.findall(block)]
        seen = set()
        cmds = []
        for c in raw_cmds:
            if c not in seen:
                seen.add(c)
                cmds.append(c)
        triplets.append({"step_num": num, "step_desc": desc, "commands": cmds, "raw_text": block})

    # bullet-point fallback
    if not triplets:
        bullet_starts = [(m.start(),) for m in re.finditer(r'^-\s+', steps_text, re.MULTILINE)]
        for i, (start,) in enumerate(bullet_starts):
            end = bullet_starts[i + 1][0] if i + 1 < len(bullet_starts) else len(steps_text)
            block = steps_text[start:end].strip()
            cmds = [f"{v} {k}" for v, k in _CMD_RE.findall(block)]
            if not cmds:
                continue
            seen = set()
            cmds_dedup = [c for c in cmds if c not in seen and not seen.add(c)]
            desc_m = re.match(r'-\s+(.+?)(?:\n|。)', block)
            triplets.append({
                "step_num": i + 1,
                "step_desc": desc_m.group(1).strip() if desc_m else "",
                "commands": cmds_dedup,
                "raw_text": block,
            })
    return triplets


def detect_doc_type(cmds, full_text):
    if cmds and all("LICENSESWITCH" in c for c in cmds):
        return "license_only"
    if any(kw in full_text for kw in _DIFF_KEYWORDS):
        return "difference_only"
    return "standard"


@step("extract_steps", output_file="doc_steps.jsonl")
def run(ctx):
    manifest = ctx["data_dir"] / "corpus_manifest.csv"
    output = ctx["data_dir"] / "doc_steps.jsonl"
    results = []

    with open(manifest, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            if row.get("has_task_example") != "True" or row.get("has_operation_steps") != "True":
                continue
            doc_path = ctx["project_root"] / row["doc_path"]
            if not doc_path.exists():
                continue
            md_text = doc_path.read_text(encoding="utf-8", errors="ignore")
            sections = read_sections(md_text)
            steps_text = sections.get(SECTION_STEPS, "")
            if not steps_text:
                continue
            triplets = parse_step_triplets(steps_text)
            if not triplets:
                continue
            all_cmds = [c for t in triplets for c in t["commands"]]
            results.append({
                "doc_path": row["doc_path"],
                "feature_id": row.get("feature_id", ""),
                "product": row.get("product", ""),
                "category": row.get("category", ""),
                "doc_type": detect_doc_type(all_cmds, md_text),
                "has_operation_flow": bool(sections.get(SECTION_FLOW, "")),
                "num_steps": len(triplets),
                "total_commands": len(all_cmds),
                "steps": triplets,
            })

    with open(output, "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"  产出 {len(results)} 份文档的步骤三元组")
    return len(results)
```

- [ ] **Step 3: Create steps/cluster.py (placeholder) + steps/assemble.py (placeholder)**

```python
# ConfigTask/builder/steps/cluster.py
"""Step 3: 按命令集聚类 task candidates → task_clusters.jsonl"""
from builder.steps.registry import step

@step("cluster", output_file="task_clusters.jsonl")
def run(ctx):
    print("  (待实现)")
    return 0
```

```python
# ConfigTask/builder/steps/assemble.py
"""Step 6: 组装最终 JSONL → assets/{nf}/{version}/"""
from builder.steps.registry import step

@step("assemble")
def run(ctx):
    print("  (待实现)")
    return 0
```

- [ ] **Step 4: Delete old scripts + commit**

```bash
cd D:/mywork/KnowledgeBase/SFCGraph
rm -f ConfigTask/scripts/scan_corpus.py ConfigTask/scripts/extract_steps.py
# rmdir scripts/ if empty
git add -A
git commit -m "feat(configtask): 迁移scan/extract_steps到统一pipeline + placeholder steps"
```

- [ ] **Step 5: Smoke test**

```bash
cd ConfigTask
python build_all.py UDG 20.15.2 scan
# Expected: 扫描 N md, M 可抽 task
python build_all.py UDG 20.15.2 extract_steps
# Expected: 产出 N 份文档的步骤三元组
```

---

## Chunk 2: Verification Framework (TDD)

### Task 3: Create verification modules + tests

**Files:**
- Create: `ConfigTask/builder/verify/__init__.py`
- Create: `ConfigTask/builder/verify/completeness.py`
- Create: `ConfigTask/builder/verify/contiguity.py`
- Create: `ConfigTask/builder/verify/object_family.py`
- Create: `ConfigTask/tests/conftest.py`
- Create: `ConfigTask/tests/test_completeness.py`
- Create: `ConfigTask/tests/test_contiguity.py`
- Create: `ConfigTask/tests/test_object_family.py`

- [ ] **Step 1: Write test_completeness.py (TDD - tests first)**

```python
# ConfigTask/tests/test_completeness.py
"""完整性核查：原文档的所有命令都出现在且仅出现在一个 candidate 中。"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from builder.verify.completeness import verify_completeness


def test_all_commands_covered():
    """正确：所有命令都被覆盖"""
    doc = {"steps": [{"commands": ["ADD URR", "ADD RULE"]}]}
    candidates = [{"commands": ["ADD URR"]}, {"commands": ["ADD RULE"]}]
    errors = verify_completeness(doc, candidates)
    assert errors == []


def test_missing_command():
    """错误：遗漏 ADD FILTER"""
    doc = {"steps": [{"commands": ["ADD URR", "ADD RULE", "ADD FILTER"]}]}
    candidates = [{"commands": ["ADD URR"]}, {"commands": ["ADD RULE"]}]
    errors = verify_completeness(doc, candidates)
    assert len(errors) == 1
    assert "ADD FILTER" in errors[0]


def test_duplicate_command():
    """错误：ADD URR 出现在两个 candidate 中"""
    doc = {"steps": [{"commands": ["ADD URR", "ADD RULE"]}]}
    candidates = [{"commands": ["ADD URR", "ADD RULE"]}, {"commands": ["ADD URR"]}]
    errors = verify_completeness(doc, candidates)
    assert any("重复" in e or "duplicate" in e.lower() for e in errors)


def test_empty_doc():
    """边界：空文档"""
    doc = {"steps": [{"commands": []}]}
    candidates = []
    errors = verify_completeness(doc, candidates)
    assert errors == []
```

- [ ] **Step 2: Implement completeness.py to pass tests**

```python
# ConfigTask/builder/verify/completeness.py
"""完整性核查：命令无遗漏、无重复。"""
from collections import Counter


def verify_completeness(doc, candidates):
    """检查所有命令被覆盖且仅出现一次。

    Args:
        doc: {"steps": [{"commands": [...]}, ...]}
        candidates: [{"commands": [...]}, ...]
    Returns:
        list[str]: 错误消息列表（空 = 通过）
    """
    # 原文档的所有命令
    all_cmds = []
    for s in doc.get("steps", []):
        all_cmds.extend(s.get("commands", []))
    expected = Counter(all_cmds)

    # candidates 里的命令
    actual = Counter()
    for c in candidates:
        actual.update(c.get("commands", []))

    errors = []
    # 遗漏
    for cmd, count in expected.items():
        if actual[cmd] < count:
            errors.append(f"命令遗漏: {cmd} (期望 {count}, 实际 {actual[cmd]})")
    # 重复
    for cmd, count in actual.items():
        if cmd in expected and count > expected[cmd]:
            errors.append(f"命令重复: {cmd} (期望 {expected[cmd]}, 实际 {count})")
    return errors
```

- [ ] **Step 3: Run tests**

```bash
cd ConfigTask
python -m pytest tests/test_completeness.py -v
# Expected: 4 passed
```

- [ ] **Step 4: Write test_contiguity.py**

```python
# ConfigTask/tests/test_contiguity.py
"""连续性核查：step_range 覆盖 [1, N] 无重叠无缺口。"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from builder.verify.contiguity import verify_contiguity


def test_full_coverage():
    """正确：步骤 1-5 被 [1,2] [3,5] 覆盖"""
    candidates = [{"step_range": [1, 2]}, {"step_range": [3, 5]}]
    total_steps = 5
    errors = verify_contiguity(candidates, total_steps)
    assert errors == []


def test_gap():
    """错误：步骤 3 缺口"""
    candidates = [{"step_range": [1, 2]}, {"step_range": [4, 5]}]
    total_steps = 5
    errors = verify_contiguity(candidates, total_steps)
    assert any("3" in e for e in errors)


def test_overlap():
    """错误：步骤 2 重叠"""
    candidates = [{"step_range": [1, 2]}, {"step_range": [2, 5]}]
    total_steps = 5
    errors = verify_contiguity(candidates, total_steps)
    assert any("重叠" in e or "overlap" in e.lower() for e in errors)


def test_single_candidate():
    """边界：1 个 candidate 覆盖全部"""
    candidates = [{"step_range": [1, 11]}]
    total_steps = 11
    errors = verify_contiguity(candidates, total_steps)
    assert errors == []
```

- [ ] **Step 5: Implement contiguity.py**

```python
# ConfigTask/builder/verify/contiguity.py
"""连续性核查：step_range 连续覆盖。"""


def verify_contiguity(candidates, total_steps):
    """检查 step_range 覆盖 [1, total_steps] 无重叠无缺口。

    Args:
        candidates: [{"step_range": [start, end], ...}, ...]
        total_steps: 原文档总步数
    Returns:
        list[str]: 错误消息列表
    """
    if not candidates:
        return [] if total_steps == 0 else [f"无 candidate 但有 {total_steps} 步"]

    covered = set()
    errors = []
    for c in candidates:
        sr = c.get("step_range")
        if not sr or len(sr) != 2:
            errors.append(f"无效 step_range: {sr}")
            continue
        start, end = sr
        for n in range(start, end + 1):
            if n in covered:
                errors.append(f"步骤重叠: {n}")
            covered.add(n)

    # 缺口
    for n in range(1, total_steps + 1):
        if n not in covered:
            errors.append(f"步骤缺口: {n}")

    return errors
```

- [ ] **Step 6: Write test_object_family.py + implement**

```python
# ConfigTask/tests/test_object_family.py
"""对象族核查：一个 candidate 内最大族占比 ≥ 50%。"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from builder.verify.object_family import classify_family, verify_family_coherence


def test_classify():
    assert classify_family("ADD URR") == "URR"
    assert classify_family("ADD URRGROUP") == "URR"
    assert classify_family("ADD PCCPOLICYGRP") == "URR"
    assert classify_family("ADD FILTER") == "FILTER"
    assert classify_family("ADD L7FILTER") == "FILTER"
    assert classify_family("ADD FLOWFILTER") == "FILTER"
    assert classify_family("ADD RULE") == "RULE"
    assert classify_family("ADD USERPROFILE") == "PROFILE"
    assert classify_family("SET LICENSESWITCH") == "LICENSE"
    assert classify_family("SET REFRESHSRV") == "REFRESH"
    assert classify_family("ADD OSPFV3") == "OSPF"


def test_coherent_family():
    """正确：全 FILTER 族"""
    cmds = ["ADD FILTER", "ADD L7FILTER", "ADD FLOWFILTER"]
    warnings = verify_family_coherence(cmds)
    assert warnings == []


def test_mixed_family():
    """可疑：URR + FILTER 混族"""
    cmds = ["ADD URR", "ADD URRGROUP", "ADD FILTER", "ADD L7FILTER"]
    warnings = verify_family_coherence(cmds)
    assert len(warnings) > 0


def test_license_merged_ok():
    """正确：LICENSE + 实际命令（LICENSE 是收尾，不拆族）"""
    cmds = ["SET LICENSESWITCH", "ADD APN", "SET APNQOSATTR"]
    warnings = verify_family_coherence(cmds)
    assert warnings == []
```

```python
# ConfigTask/builder/verify/object_family.py
"""对象族核查：命令按对象关键字分组。"""
import re

# 对象族映射（从实证归纳）
_FAMILY_MAP = {
    # URR 族
    "URR": "URR", "URRGROUP": "URR", "PCCPOLICYGRP": "URR", "PCCACTIONPROP": "URR",
    "URRGRPBINDING": "URR", "SPECURRGRPLIST": "URR", "URRFAILACTION": "URR",
    # FILTER 族
    "FILTER": "FILTER", "FILTERIPV6": "FILTER", "L7FILTER": "FILTER",
    "FLOWFILTER": "FILTER", "FLOWFILTERGRP": "FILTER",
    "FLTBINDFLOWF": "FILTER", "PROTBINDFLOWF": "FILTER",
    # RULE 族
    "RULE": "RULE", "RULEBINDING": "RULE",
    # PROFILE 族
    "USERPROFILE": "PROFILE", "RULEBINDING_PROFILE": "PROFILE",
    # POOL 族
    "POOL": "POOL", "SECTION": "POOL", "POOLGROUP": "POOL",
    "POOLBINDGROUP": "POOL", "POOLGRPMAP": "POOL",
    # VPN 族
    "VPNINST": "VPN", "L3VPNINST": "VPN", "VPNINSTAF": "VPN",
    "IPBINDVPN": "VPN",
    # OSPF 族
    "OSPF": "OSPF", "OSPFAREA": "OSPF", "OSPFNETWORK": "OSPF",
    "OSPFV3": "OSPF", "OSPFV3AREA": "OSPF", "OSPFV3INTERFACE": "OSPF",
    "OSPFV3IMPORTROUTE": "OSPF", "OSPFIMPORTROUTE": "OSPF",
    # BWM 族
    "BWMCONTROLLER": "BWM", "BWMRULE": "BWM", "BWMUSERGROUP": "BWM",
    "BWMSERVICE": "BWM", "BWMRULEGLOBAL": "BWM",
    # 收尾类（不参与族判定）
    "LICENSESWITCH": "LICENSE", "REFRESHSRV": "REFRESH",
}

_IGNORE_FAMILIES = {"LICENSE", "REFRESH"}


def classify_family(command):
    """命令名 → 对象族。"""
    # 提取对象关键字 (VERB OBJECT → OBJECT)
    parts = command.split(None, 1)
    if len(parts) < 2:
        return "OTHER"
    obj = parts[1].strip()
    return _FAMILY_MAP.get(obj, "OTHER")


def verify_family_coherence(commands):
    """检查一个 candidate 的命令是否主要属于同一族。

    Args:
        commands: ["ADD URR", "ADD URRGROUP", ...]
    Returns:
        list[str]: 警告消息（空 = 一致）
    """
    from collections import Counter
    families = Counter()
    for cmd in commands:
        fam = classify_family(cmd)
        if fam not in _IGNORE_FAMILIES:
            families[fam] += 1

    total = sum(families.values())
    if total == 0:
        return []

    max_family, max_count = families.most_common(1)[0]
    ratio = max_count / total

    if ratio < 0.5:
        return [f"对象族分散: 最大族 {max_family} 占比 {ratio:.0%}, 族分布 {dict(families)}"]
    return []
```

- [ ] **Step 7: Run all verification tests**

```bash
cd ConfigTask
python -m pytest tests/ -v
# Expected: all passed
```

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "feat(configtask): verification framework (completeness + contiguity + object_family) with TDD tests"
```

---

## Chunk 3: Agent Runner + Verify Steps

### Task 4: Create agent/runner.py (batch dispatch + progress + retry)

**Files:**
- Create: `ConfigTask/builder/agent/__init__.py`
- Create: `ConfigTask/builder/agent/runner.py`

- [ ] **Step 1: Create agent/runner.py**

```python
# ConfigTask/builder/agent/runner.py
"""Agent 批量调度 + 进度管理 + 失败重试。

核心逻辑：
1. 读全量输入
2. 读 progress（已处理）
3. 过滤 todo = 全量 - 已成功
4. 分批调 Agent
5. 每批过核查
6. 成功标记 ok，失败标记 fail
7. 最终断言无遗漏
"""
import json
import pathlib


def load_progress(ctx, step_name):
    """加载进度文件。"""
    progress_dir = ctx["data_dir"] / "progress"
    progress_dir.mkdir(parents=True, exist_ok=True)
    path = progress_dir / f"{step_name}.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def save_progress(ctx, step_name, progress):
    """保存进度文件。"""
    progress_dir = ctx["data_dir"] / "progress"
    progress_dir.mkdir(parents=True, exist_ok=True)
    path = progress_dir / f"{step_name}.json"
    path.write_text(json.dumps(progress, ensure_ascii=False, indent=2), encoding="utf-8")


def run_agent_step(ctx, step_name, input_items, agent_fn, verify_fn, key_field="doc_path"):
    """执行一个 Agent step（批量调度 + 核查 + 进度管理）。

    Args:
        ctx: pipeline 上下文
        step_name: step 名称（用于 progress 文件）
        input_items: 全量输入列表（每项是一个 dict）
        agent_fn: callable(batch: list) -> dict(output_key -> output_value)
        verify_fn: callable(input_item, output_value) -> list[str](errors)
        key_field: 输入项的唯一标识字段

    Returns:
        list: 所有成功产出
    """
    progress = load_progress(ctx, step_name)

    # 如果指定了 rerun，清除该目标的进度
    if "rerun_target" in ctx:
        target = ctx["rerun_target"]
        keys_to_clear = [k for k in progress if target in k]
        for k in keys_to_clear:
            del progress[k]

    # 过滤出未处理的
    all_keys = [item[key_field] for item in input_items]
    todo = [item for item in input_items if progress.get(item[key_field]) != "ok"]

    if not todo:
        ok = sum(1 for v in progress.values() if v == "ok")
        print(f"  {step_name}: 全部已完成 ({ok}/{len(all_keys)})")
        return []

    batch_size = ctx.get("agent_batch_size", 5)
    results = []

    for i in range(0, len(todo), batch_size):
        batch = todo[i:i + batch_size]
        batch_keys = [item[key_field] for item in batch]
        print(f"  {step_name}: 处理批次 {i//batch_size + 1} ({len(batch)} 项): {batch_keys[:3]}...")

        # 调 Agent
        agent_output = agent_fn(batch)

        # 逐项核查
        for item in batch:
            key = item[key_field]
            output = agent_output.get(key)
            if output is None:
                progress[key] = "fail"
                print(f"    FAIL {key}: Agent 未返回结果")
                continue

            errors = verify_fn(item, output)
            hard_errors = [e for e in errors if e.startswith("HARD:")]
            if hard_errors:
                progress[key] = "fail"
                print(f"    FAIL {key}: {hard_errors}")
            else:
                progress[key] = "ok"
                results.append(output)
                if errors:
                    print(f"    WARN {key}: {errors}")

        save_progress(ctx, step_name, progress)

    # 最终断言
    ok_count = sum(1 for v in progress.values() if v == "ok")
    fail_count = sum(1 for v in progress.values() if v == "fail")
    total = len(all_keys)

    if fail_count > 0:
        print(f"  {step_name}: {fail_count} 项失败，下轮自动重试")
    if ok_count + fail_count < total:
        print(f"  {step_name}: 警告 - {total - ok_count - fail_count} 项未处理")

    return results
```

- [ ] **Step 2: Create verify_split.py / verify_merge.py / verify_rules.py (wire up verification)**

```python
# ConfigTask/builder/steps/verify_split.py
"""Step 2 核查：对 Agent-1 产出做完整性/连续性/对象族检查。"""
import json

from builder.steps.registry import step
from builder.verify.completeness import verify_completeness
from builder.verify.contiguity import verify_contiguity
from builder.verify.object_family import verify_family_coherence


def verify_candidate(doc, candidates):
    """对单份文档的 candidates 做全维度核查。

    Returns:
        list[str]: 错误列表（HARD: 前缀 = 硬约束失败）
    """
    errors = []

    # 硬约束：完整性
    comp_errors = verify_completeness(doc, candidates)
    errors.extend(f"HARD: {e}" for e in comp_errors)

    # 硬约束：连续性
    total_steps = doc.get("num_steps", 0)
    cont_errors = verify_contiguity(candidates, total_steps)
    errors.extend(f"HARD: {e}" for e in cont_errors)

    # 硬约束：非空
    for i, c in enumerate(candidates):
        if not c.get("commands"):
            errors.append(f"HARD: candidate[{i}] 无命令")

    # 软约束：对象族
    for i, c in enumerate(candidates):
        fam_warnings = verify_family_coherence(c.get("commands", []))
        errors.extend(f"WARN: candidate[{i}] {w}" for w in fam_warnings)

    return errors


@step("verify_split")
def run(ctx):
    """核查 task_candidates.jsonl。"""
    doc_steps_path = ctx["data_dir"] / "doc_steps.jsonl"
    candidates_path = ctx["data_dir"] / "task_candidates.jsonl"

    if not candidates_path.exists():
        print("  跳过：task_candidates.jsonl 不存在")
        return 0

    # 读 doc_steps
    docs = {}
    with open(doc_steps_path, encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            docs[d["doc_path"]] = d

    # 读 candidates，按 doc_path 分组
    doc_candidates = {}
    with open(candidates_path, encoding="utf-8") as f:
        for line in f:
            c = json.loads(line)
            doc_candidates.setdefault(c["doc_path"], []).append(c)

    # 逐文档核查
    total_errors = 0
    for doc_path, doc in docs.items():
        candidates = doc_candidates.get(doc_path, [])
        errors = verify_candidate(doc, candidates)
        if errors:
            hard = [e for e in errors if e.startswith("HARD:")]
            if hard:
                print(f"  FAIL {doc_path}: {hard}")
                total_errors += len(hard)

    if total_errors == 0:
        print(f"  核查通过: {len(docs)} 份文档")
    else:
        print(f"  核查失败: {total_errors} 个硬约束错误")

    return total_errors
```

```python
# ConfigTask/builder/steps/verify_merge.py
"""Step 4 核查：对 Agent-2 产出做命令覆盖/参数完整/binding 覆盖检查。"""
from builder.steps.registry import step


@step("verify_merge")
def run(ctx):
    print("  (待实现)")
    return 0
```

```python
# ConfigTask/builder/steps/verify_rules.py
"""Step 5 核查：对 Agent-3 产出做规则来源/DecisionPoint 检查。"""
from builder.steps.registry import step


@step("verify_rules")
def run(ctx):
    print("  (待实现)")
    return 0
```

- [ ] **Step 3: Update steps/__init__.py to import verify steps**

```python
# ConfigTask/builder/steps/__init__.py
from . import scan, extract_steps, cluster, assemble  # noqa: F401
from . import verify_split, verify_merge, verify_rules  # noqa: F401
```

- [ ] **Step 4: Smoke test pipeline**

```bash
cd ConfigTask
python build_all.py UDG 20.15.2 scan
python build_all.py UDG 20.15.2 extract_steps
python build_all.py UDG 20.15.2 verify_split
# Expected: scan + extract_steps 正常, verify_split 跳过（task_candidates.jsonl 不存在）
python -m pytest tests/ -v
# Expected: all passed
```

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat(configtask): agent runner + verify steps (split/merge/rules) wired up"
```

---

## Chunk 4: Agent-1 Split Tasks (验证用最小实现)

### Task 5: Create agent/prompts.py + split_tasks.py

**Files:**
- Create: `ConfigTask/builder/agent/prompts.py`
- Create: `ConfigTask/builder/steps/split_tasks.py`
- Update: `ConfigTask/builder/steps/__init__.py` (uncomment split_tasks)

> **注意**：这一步的 Agent 调用通过 Agent 工具（subagent dispatch）实现，不是直接调 LLM API。split_tasks.py 构造输入 → 调 Agent → 解析输出。实际 Agent 调用在 build_all.py 运行时由执行者（人或 subagent-driven-development）触发。

- [ ] **Step 1: Create prompts.py with Agent-1 prompt template**

```python
# ConfigTask/builder/agent/prompts.py
"""Agent prompt 模板。"""

SPLIT_TASKS_PROMPT = """你是 ConfigTask 拆分 Agent。下面是 {n_docs} 份配置文档的步骤清单，请逐份拆分成 task candidate。

【task 定义】一个 task = 一组连续步骤，共同完成一个可命名的配置动作（如"配置计费动作链"）。

【拆分信号】（按优先级）
1. 配置对象族切换：命令操作的对象从 URR 族变成 FILTER 族 = 不同 task
   对象族参考：URR族={{URR,URRGROUP,PCCPOLICYGRP}} / FILTER族={{FILTER,L7FILTER,FLOWFILTER,FLTBINDFLOWF,PROTBINDFLOWF}} / RULE族={{RULE}} / PROFILE族={{USERPROFILE,RULEBINDING}} / POOL族={{POOL,SECTION,POOLGROUP,POOLBINDGROUP}} / VPN族={{VPNINST,L3VPNINST,VPNINSTAF}} / OSPF族={{OSPF,OSPFAREA,OSPFNETWORK}} / BWM族={{BWMCONTROLLER,BWMRULE,BWMUSERGROUP}}
2. step_desc 语义切换：描述从"配置过滤条件"变成"添加规则" = 不同 task
3. 收尾命令：SET REFRESHSRV / SET LICENSESWITCH 不单独成 task，并入相邻段
4. 可选步骤：扩展前段语义 → 并入；独立功能 → 单独

【输出格式】对每份文档，输出 JSON：
{{
  "{doc_key}": [
    {{
      "step_range": [1, 2],
      "candidate_desc": "配置计费动作链",
      "commands": ["ADD URR", "ADD URRGROUP", "ADD PCCPOLICYGRP"]
    }}
  ]
}}

【关键规则】
- 所有步骤必须被覆盖（step_range 的并集 = [1, 总步数]，不遗漏不重叠）
- SET LICENSESWITCH 并入第一个实际配置 task
- SET REFRESHSRV 并入前一个 task
- 1-2 步的简单文档通常就是 1 个 task
- 纯 RMV 删除类如果意图一致，合成 1 个 task

【输入数据】
{input_json}
"""


MERGE_FIELDS_PROMPT = """你是 ConfigTask 合并 Agent。下面是一个 task 簇（{n_members} 个配置案例），请确证合并并抽取字段。
（详细 prompt 见 spec §4.2）
"""


EXTRACT_RULES_PROMPT = """你是 ConfigTask 规则抽取 Agent。下面是一个 ConfigTask + 命令图谱 notes，请抽取 TaskRule 和 DecisionPoint。
（详细 prompt 见 spec §5.2）
"""
```

- [ ] **Step 2: Create split_tasks.py (Agent-1 orchestrator)**

```python
# ConfigTask/builder/steps/split_tasks.py
"""Step 2: Agent 拆 task（per-doc, 每批 agent_batch_size 份）。

这个 step 的实际执行：
1. 读 doc_steps.jsonl
2. 分批（progress 管理）
3. 构造 Agent prompt（prompts.py）
4. 调 Agent（通过 subagent dispatch 或手动）
5. 解析输出
6. 写 task_candidates.jsonl

注意：Agent 调用由执行者触发。本文件负责输入构造 + 输出解析 + 进度管理。
"""
import json

from builder.steps.registry import step
from builder.agent.runner import run_agent_step, load_progress, save_progress


def build_agent_input(batch):
    """构造 Agent 输入 JSON。"""
    docs = []
    for doc in batch:
        docs.append({
            "doc_path": doc["doc_path"],
            "feature_id": doc.get("feature_id", ""),
            "num_steps": doc["num_steps"],
            "steps": [
                {"step_num": s["step_num"], "step_desc": s["step_desc"], "commands": s["commands"]}
                for s in doc["steps"]
            ],
        })
    return docs


def parse_agent_output(raw_output, batch):
    """解析 Agent 输出 → candidates 列表。

    Agent 输出格式: {doc_path: [{step_range, candidate_desc, commands}, ...]}
    """
    if isinstance(raw_output, str):
        # 尝试提取 JSON
        import re
        json_match = re.search(r'\{.*\}', raw_output, re.DOTALL)
        if json_match:
            raw_output = json.loads(json_match.group())

    results = {}
    for doc in batch:
        doc_path = doc["doc_path"]
        candidates_raw = raw_output.get(doc_path, [])
        candidates = []
        for i, c in enumerate(candidates_raw):
            candidates.append({
                "doc_path": doc_path,
                "feature_id": doc.get("feature_id", ""),
                "candidate_id": f"{doc.get('feature_id', 'UNKNOWN')}#{i+1:03d}",
                "step_range": c.get("step_range"),
                "candidate_desc": c.get("candidate_desc", ""),
                "commands": c.get("commands", []),
                "boundary_source": "agent",
            })
        results[doc_path] = candidates
    return results


@step("split_tasks", output_file="task_candidates.jsonl")
def run(ctx):
    """Agent-1: 拆 task。"""
    from builder.agent.prompts import SPLIT_TASKS_PROMPT
    from builder.steps.verify_split import verify_candidate

    # 读全量输入
    doc_steps_path = ctx["data_dir"] / "doc_steps.jsonl"
    all_docs = []
    with open(doc_steps_path, encoding="utf-8") as f:
        for line in f:
            all_docs.append(json.loads(line))

    # 读已有产出（续跑模式：追加到已有文件）
    output_path = ctx["data_dir"] / "task_candidates.jsonl"
    existing = []
    if output_path.exists():
        with open(output_path, encoding="utf-8") as f:
            existing = [json.loads(l) for l in f]

    # 用 runner 执行
    def agent_fn(batch):
        """这个函数在实际执行时由 Agent 工具替代。
        构造 prompt → 调 Agent → 返回解析后的 dict。
        """
        input_data = build_agent_input(batch)
        prompt = SPLIT_TASKS_PROMPT.format(
            n_docs=len(batch),
            doc_key=batch[0]["doc_path"] if batch else "",
            input_json=json.dumps(input_data, ensure_ascii=False, indent=2),
        )
        # 注意：实际 Agent 调用由执行者触发
        # 执行者看到 prompt → 用 Agent 工具调 → 把返回结果传回 parse_agent_output
        raise NotImplementedError(
            "Agent 调用需由执行者触发。请用 Agent 工具发送以下 prompt：\n" + prompt
        )

    def verify_fn(doc, candidates):
        return verify_candidate(doc, candidates)

    results = run_agent_step(
        ctx, "split_tasks", all_docs, agent_fn, verify_fn, key_field="doc_path"
    )

    # 写产出（追加模式）
    all_candidates = existing + [c for doc_cands in results for c in doc_cands]
    with open(output_path, "w", encoding="utf-8") as f:
        for c in all_candidates:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    return len(all_candidates)
```

- [ ] **Step 3: Update __init__.py**

```python
# ConfigTask/builder/steps/__init__.py
from . import scan, extract_steps, cluster, assemble  # noqa: F401
from . import verify_split, verify_merge, verify_rules  # noqa: F401
from . import split_tasks  # noqa: F401
```

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "feat(configtask): Agent-1 split_tasks orchestrator + prompt template"
```

---

## Chunk 5: Remaining Steps (cluster + merge_fields + extract_rules + assemble)

> 这部分的实现模式与 Chunk 4 相同（prompt + orchestrator + verify）。在 Chunk 1-4 验证通过后，按 spec §3-§6 逐个实现。

### Task 6: cluster.py implementation
### Task 7: merge_fields.py (Agent-2) implementation
### Task 8: extract_rules.py (Agent-3) implementation
### Task 9: assemble.py implementation

（每个 Task 的结构同 Task 5：prompt 模板 + orchestrator + verify 接线。具体 prompt 见 spec。）

---

## Execution Notes

1. **Agent 调用方式**：pipeline 中的 `agent_fn` 是占位符。实际执行时，`split_tasks.py` 会构造 prompt 并 raise NotImplementedError，执行者看到 prompt 后用 Agent 工具（subagent dispatch）调 Agent，把返回结果写回 JSONL 文件。然后重跑 `python build_all.py UDG 20.15.2 verify_split` 核查。

2. **批量执行 Agent-1**：655 份文档 ÷ 5/批 = 131 批。每批用 Agent 工具调一次，结果追加到 task_candidates.jsonl，progress 自动记录。

3. **TDD 流程**：每个 Agent step 之前先跑核查代码（verify_split/verify_merge/verify_rules）。核查代码有测试覆盖（test_completeness/test_contiguity/test_object_family），确保核查本身正确。

4. **断点续跑**：progress/split_tasks.json 记录每份文档的状态。重跑时自动跳过已成功的文档。失败文档自动重试。`--rerun GWFD-020301` 可强制重跑指定文档。
