# ConfigTask/builder/steps/extract_steps.py
"""Step 1: 从语料抽步骤三元组 → doc_steps.jsonl"""
import csv
import json
import re
import pathlib

from builder.steps.registry import step
from builder.core.md_reader import read_sections
from builder.constants import SECTION_STEPS, SECTION_FLOW

_CMD_RE = re.compile(r'\b(ADD|SET|MOD|DEL|RMV|LST|DSP|LOD|SWP|RST|EXP|ACT|DEA)\s+(\w+)\b')
_STEP_START_RE = re.compile(r'^\s*(\d+)\.\s', re.MULTILINE)
_DIFF_KEYWORDS = ("参考部署", "此处仅描述差异", "详细配置请参考", "此处仅描述")


def _parse_step_triplets(steps_text):
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
        cmds = [c for c in raw_cmds if c not in seen and not seen.add(c)]
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


def _detect_doc_type(cmds, full_text):
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
            triplets = _parse_step_triplets(steps_text)
            if not triplets:
                continue
            all_cmds = [c for t in triplets for c in t["commands"]]
            results.append({
                "doc_path": row["doc_path"],
                "feature_id": row.get("feature_id", ""),
                "product": row.get("product", ""),
                "category": row.get("category", ""),
                "doc_type": _detect_doc_type(all_cmds, md_text),
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
