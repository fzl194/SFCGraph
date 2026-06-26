# ConfigTask/builder/steps/cluster.py
"""Step 3: 按命令骨架聚 task candidate → task_clusters.jsonl

两轮聚类：
1. 精确匹配（核心命令集相同 = 同簇）
2. Jaccard > 0.7 合并孤立单成员簇

同时修复：只有收尾命令(LICENSESWITCH/REFRESHSRV)的孤儿 candidate 并入同文档相邻 candidate。
"""
import json
from collections import defaultdict
from itertools import combinations

from builder.steps.registry import step

OPTIONAL = {"SET LICENSESWITCH", "SET REFRESHSRV", "MOD USERPROFILE"}


def core_commands(cmds):
    """去掉收尾命令后的核心命令骨架。"""
    return tuple(c for c in cmds if c not in OPTIONAL)


def jaccard(a, b):
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 1.0
    return len(sa & sb) / len(sa | sb)


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

        # 找孤儿（核心命令为空）
        non_orphan = [c for c in cands if core_commands(c["commands"])]
        orphans = [c for c in cands if not core_commands(c["commands"])]

        if not orphans:
            fixed.extend(cands)
            continue

        # 把孤儿的命令并入第一个非孤儿（或如果全是孤儿，合并成一个）
        if non_orphan:
            target = non_orphan[0]
            for o in orphans:
                # 合并命令（追加孤儿的命令到 target）
                target_cmds = list(target["commands"])
                for c in o["commands"]:
                    if c not in target_cmds:
                        target_cmds.append(c)
                target["commands"] = target_cmds
                # 合并 step_range
                if target.get("step_range") and o.get("step_range"):
                    sr = target["step_range"]
                    or_sr = o["step_range"]
                    if sr and or_sr and len(sr) == 2 and len(or_sr) == 2:
                        target["step_range"] = [min(sr[0], or_sr[0]), max(sr[1], or_sr[1])]
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
    """两轮聚类。"""
    # 第一轮：精确匹配
    groups = defaultdict(list)
    for c in candidates:
        key = core_commands(c["commands"])
        groups[key].append(c)

    # 第二轮：Jaccard > 0.7 合并孤立单成员簇
    keys = list(groups.keys())
    merged_keys = set()
    merge_map = {}  # old_key → new_key

    # 找单成员簇
    singletons = {k: v for k, v in groups.items() if len(v) == 1 and len(k) > 0}
    multi = {k: v for k, v in groups.items() if len(v) > 1 or len(k) == 0}

    # 每个单成员尝试与多成员簇合并
    for s_key, s_members in singletons.items():
        best_target = None
        best_score = 0.7  # 阈值
        for m_key in multi:
            if m_key in merged_keys:
                continue
            score = jaccard(s_key, m_key)
            if score > best_score:
                best_score = score
                best_target = m_key
        if best_target:
            merge_map[s_key] = best_target
            multi[best_target].extend(s_members)
            merged_keys.add(s_key)

    # 构建最终簇列表
    final_clusters = []
    cluster_id = 0
    for key, members in multi.items():
        if key in merged_keys:
            continue
        cluster_id += 1
        final_clusters.append({
            "cluster_id": f"cluster-{cluster_id:03d}",
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
        })

    # 未合并的单成员簇
    for key, members in singletons.items():
        if key in merge_map:
            continue
        cluster_id += 1
        final_clusters.append({
            "cluster_id": f"cluster-{cluster_id:03d}",
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
        })

    return final_clusters


@step("cluster", output_file="task_clusters.jsonl")
def run(ctx):
    data_dir = ctx["data_dir"]
    output = data_dir / "task_clusters.jsonl"

    # 读 candidates
    candidates = []
    with open(data_dir / "task_candidates.jsonl", encoding="utf-8") as f:
        for line in f:
            candidates.append(json.loads(line))

    print(f"  输入: {len(candidates)} candidates")

    # 修孤儿
    candidates, merged = fix_orphans(candidates)
    print(f"  修孤儿: 合并 {merged} 个")

    # 聚类
    clusters = cluster(candidates)

    # 写产出
    with open(output, "w", encoding="utf-8") as f:
        for c in clusters:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    # 统计
    from collections import Counter
    size_dist = Counter(c["member_count"] for c in clusters)
    print(f"  产出: {len(clusters)} 簇")
    print(f"  大小分布: {dict(sorted(size_dist.items()))}")

    return len(clusters)
