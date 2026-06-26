# ConfigTask/builder/steps/cluster.py
"""Step 3: 按命令骨架聚 task candidate → task_clusters.jsonl

修复：
- candidate_id 全局唯一化（加 doc_path hash）
- fix_orphans 后写回 candidates 文件
- 聚类基于 fix 后的 candidates
"""
import json
import hashlib
from collections import defaultdict

from builder.steps.registry import step

OPTIONAL = {"SET LICENSESWITCH", "SET REFRESHSRV", "MOD USERPROFILE"}


def make_unique_id(candidate):
    """生成全局唯一 candidate_id = feature_id + doc_path hash 前 4 位 + seq。"""
    fid = candidate.get("feature_id", "")
    doc_path = candidate.get("doc_path", "")
    # 从 doc_path 取文件名作为区分
    import os
    doc_hash = hashlib.md5(doc_path.encode()).hexdigest()[:4]
    # 原始 seq（从 candidate_id 提取）
    old_id = candidate.get("candidate_id", "")
    seq = old_id.split("#")[-1] if "#" in old_id else "001"
    return f"{fid}#{doc_hash}#{seq}" if fid else f"UNK#{doc_hash}#{seq}"


def core_commands(cmds):
    return tuple(c for c in cmds if c not in OPTIONAL)


def jaccard(a, b):
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 1.0
    return len(sa & sb) / len(sa | sb) if (sa | sb) else 0.0


def fix_orphans(candidates):
    """把只有收尾命令的孤儿 candidate 并入同文档的相邻 candidate。"""
    by_doc = defaultdict(list)
    for c in candidates:
        by_doc[c["doc_path"]].append(c)

    fixed = []
    merged = 0
    for doc_path, cands in by_doc.items():
        if len(cands) <= 1:
            fixed.extend(cands)
            continue

        non_orphan = [c for c in cands if core_commands(c["commands"])]
        orphans = [c for c in cands if not core_commands(c["commands"])]

        if not orphans:
            fixed.extend(cands)
            continue

        if non_orphan:
            # 按出现顺序，把孤儿命令并入前一个非孤儿
            for o in orphans:
                # 找前一个非孤儿
                target = non_orphan[0]
                # 追加命令（去重）
                for c in o["commands"]:
                    if c not in target["commands"]:
                        target["commands"].append(c)
                # 扩展 step_range
                if target.get("step_range") and o.get("step_range"):
                    sr = target["step_range"]
                    osr = o["step_range"]
                    if sr and osr and len(sr) == 2 and len(osr) == 2:
                        target["step_range"] = [min(sr[0], osr[0]), max(sr[1], osr[1])]
                merged += 1
            fixed.extend(non_orphan)
        else:
            # 全是孤儿 → 合成一个
            merged_cands = cands[0]
            all_cmds = []
            for c in cands:
                all_cmds.extend(c["commands"])
            seen = set()
            merged_cands["commands"] = [c for c in all_cmds if c not in seen and not seen.add(c)]
            fixed.append(merged_cands)
            merged += len(cands) - 1

    return fixed, merged


def cluster(candidates):
    """两轮聚类：精确匹配 + Jaccard > 0.7 合并。"""
    # 第一步：candidate_id 全局唯一化
    for c in candidates:
        c["candidate_id"] = make_unique_id(c)

    # 第二轮：精确匹配
    groups = defaultdict(list)
    for c in candidates:
        key = core_commands(c["commands"])
        groups[key].append(c)

    # 第三轮：Jaccard 合并孤立单成员
    singletons = {k: v for k, v in groups.items() if len(v) == 1 and len(k) > 0}
    multi = {k: v for k, v in groups.items() if len(v) > 1 or len(k) == 0}

    merged_keys = set()
    for s_key, s_members in singletons.items():
        best_target = None
        best_score = 0.7
        for m_key in multi:
            if m_key in merged_keys:
                continue
            score = jaccard(s_key, m_key)
            if score > best_score:
                best_score = score
                best_target = m_key
        if best_target:
            multi[best_target].extend(s_members)
            merged_keys.add(s_key)

    # 构建最终簇列表
    final_clusters = []
    cluster_id = 0

    for key, members in multi.items():
        if key in merged_keys:
            continue
        cluster_id += 1
        final_clusters.append(_make_cluster(cluster_id, key, members))

    for key, members in singletons.items():
        if key in merged_keys:
            continue
        cluster_id += 1
        final_clusters.append(_make_cluster(cluster_id, key, members))

    return final_clusters, candidates


def _make_cluster(cid, key, members):
    return {
        "cluster_id": f"cluster-{cid:03d}",
        "core_commands": list(key) if key else [],
        "member_count": len(members),
        "members": [
            {
                "candidate_id": m["candidate_id"],
                "doc_path": m["doc_path"],
                "feature_id": m.get("feature_id", ""),
                "commands": m["commands"],
                "candidate_desc": m.get("candidate_desc", ""),
            }
            for m in members
        ],
    }


@step("cluster", output_file="task_clusters.jsonl")
def run(ctx):
    data_dir = ctx["data_dir"]
    candidates_path = data_dir / "task_candidates.jsonl"
    output_path = data_dir / "task_clusters.jsonl"

    # 读 candidates
    candidates = []
    with open(candidates_path, encoding="utf-8") as f:
        for line in f:
            candidates.append(json.loads(line))
    print(f"  输入: {len(candidates)} candidates")

    # 修孤儿
    candidates, merged = fix_orphans(candidates)
    print(f"  修孤儿: 合并 {merged} 个")

    # 写回修正后的 candidates（含全局唯一 ID）
    with open(candidates_path, "w", encoding="utf-8") as f:
        for c in candidates:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"  写回 candidates: {len(candidates)} 条（含全局唯一 ID）")

    # 聚类
    clusters, candidates = cluster(candidates)

    # 核查：完整性
    all_cand_ids = set(c["candidate_id"] for c in candidates)
    cluster_cand_ids = set()
    for cl in clusters:
        for m in cl["members"]:
            cluster_cand_ids.add(m["candidate_id"])
    missing = all_cand_ids - cluster_cand_ids
    if missing:
        print(f"  警告: {len(missing)} candidate 遗漏")
    else:
        print(f"  核查通过: {len(all_cand_ids)} candidates 全部入簇")

    # 写产出
    with open(output_path, "w", encoding="utf-8") as f:
        for cl in clusters:
            f.write(json.dumps(cl, ensure_ascii=False) + "\n")

    from collections import Counter
    size_dist = Counter(c["member_count"] for c in clusters)
    print(f"  产出: {len(clusters)} 簇")
    print(f"  大小分布: {dict(sorted(size_dist.items()))}")

    return len(clusters)
