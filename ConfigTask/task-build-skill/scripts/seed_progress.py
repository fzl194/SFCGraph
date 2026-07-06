"""派生 UDG 可建特性封闭清单 + 维护 progress.json（跨会话进度真相）。

用法：
  python seed_progress.py UDG 20.15.2          # 初始化/刷新 progress.json（保留已 done/skipped）
  python seed_progress.py UDG 20.15.2 --check  # 只打印计数 + 未终态残留

只读：FeatureGraph/data/legacy/UDG_feature_files.csv, UDG_features.csv, assert/.../index.json
写入：assert/{nf}/{version}/progress.json
"""
import json
import sys
import csv
import collections
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # ConfigTask/
NF = sys.argv[1] if len(sys.argv) > 1 else "UDG"
VER = sys.argv[2] if len(sys.argv) > 2 else "20.15.2"
CHECK = "--check" in sys.argv

FG = ROOT.parent / "FeatureGraph" / "data" / "legacy"
FILES_CSV = FG / f"{NF}_feature_files.csv"
FEAT_CSV = FG / f"{NF}_features.csv"
A = ROOT / "assert" / NF / VER
PROG = A / "progress.json"
INDEX = A / "index.json"

CONFIG_KEYWORDS = ("部署", "激活", "配置")  # 文件名含此才算配置步骤文档


def short_id(fid):
    return fid.split("@")[-1] if fid else ""


def derive_buildable():
    """feature_id -> {name, section, config_files}，仅保留有配置步骤文档的特性"""
    files_by_feat = collections.defaultdict(list)
    with FILES_CSV.open(encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            files_by_feat[r["feature_id"]].append(r["file_path"])
    feat_meta = {}
    if FEAT_CSV.exists():
        with FEAT_CSV.open(encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                feat_meta[r.get("feature_id") or r.get("id", "")] = {
                    "name": r.get("feature_name", ""), "section": r.get("section", "")}
    buildable = {}
    for fid, paths in files_by_feat.items():
        cfg = [p for p in paths if any(k in Path(p).name for k in CONFIG_KEYWORDS)]
        if cfg:
            m = feat_meta.get(fid, {})
            buildable[fid] = {"name": m.get("name", ""), "section": m.get("section", ""),
                              "config_files": cfg}
    return buildable


def existing_built_features():
    """index.json 的 by_feature 键 = 已有 feature task 的特性"""
    if not INDEX.exists():
        return set()
    d = json.loads(INDEX.read_text(encoding="utf-8"))
    return {fid for fid, v in d.get("by_feature", {}).items() if v.get("feature_task")}


def main():
    buildable = derive_buildable()
    built = existing_built_features()

    prev = {}
    if PROG.exists():
        prev = json.loads(PROG.read_text(encoding="utf-8"))

    # 保留既有 skipped / in_progress（人工判断不丢）
    skipped = prev.get("skipped", [])
    skipped_ids = {s["feature_id"] if isinstance(s, dict) else s for s in skipped}
    in_progress = prev.get("in_progress", [])

    done = sorted(set(prev.get("done", [])) | (built & set(buildable)))
    in_prog_ids = {i["feature_id"] if isinstance(i, dict) else i for i in in_progress}
    not_started = sorted(fid for fid in buildable
                         if fid not in done and fid not in skipped_ids and fid not in in_prog_ids)

    # 分批（按 section）
    by_sec = collections.defaultdict(list)
    for fid, m in buildable.items():
        by_sec[m["section"] or "_未分类"].append(fid)
    batches = []
    sec_order = sorted(by_sec, key=lambda s: -len(by_sec[s]))
    for i, sec in enumerate(sec_order, 1):
        feats = by_sec[sec]
        # 批状态：全 done → done；含 in_progress → in_progress；否则 pending
        st = "done" if all(f in done for f in feats) else (
            "in_progress" if any(f in in_prog_ids for f in feats) else "pending")
        batches.append({"id": f"B{i:02d}", "section": sec, "n": len(feats), "status": st})

    prog = {
        "nf_version": f"{NF}@{VER}",
        "buildable_total": len(buildable),
        "done": done,
        "in_progress": in_progress,
        "not_started": not_started,
        "skipped": skipped,
        "batches": batches,
        "last_session": prev.get("last_session", {}),
        "feature_meta": {fid: {"name": m["name"], "section": m["section"],
                               "config_files": m["config_files"]} for fid, m in buildable.items()},
    }

    # 残留检查：可建特性里既非 done 也非 skipped 也非 in_progress
    residual = [fid for fid in buildable
                if fid not in done and fid not in skipped_ids and fid not in in_prog_ids]
    print(f"可建特性总数：{len(buildable)}")
    print(f"  done={len(done)}  in_progress={len(in_progress)}  not_started={len(not_started)}  skipped={len(skipped)}")
    print(f"  批次数：{len(batches)}")
    if CHECK:
        # not_started 即残留（待处理），这是正常的（待建）；真正异常是既不在 done/skipped/in_prog 也不在 not_started —— 不可能，逻辑保证
        print(f"  待处理(not_started)：{len(not_started)}（正常，待逐批构建）")
        print("批次概览：")
        for b in batches:
            print(f"    {b['id']} [{b['status']}] {b['section'][:30]}  ×{b['n']}")
        return

    PROG.write_text(json.dumps(prog, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"progress.json 已写：{PROG.relative_to(ROOT)}")
    print(f"  done 示例：{done[:6]}")


if __name__ == "__main__":
    main()
