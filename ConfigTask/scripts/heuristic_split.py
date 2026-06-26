"""启发式拆分剩余文档（编码 Agent 的决策逻辑）。
规则：
1. SET LICENSESWITCH 并入第一个实际配置段
2. SET REFRESHSRV 并入前一段
3. 对象族切换 = 分段边界
4. 1-2 步 = 1 个 candidate
5. step_desc 语义切换 = 分段边界
"""
import json
import re
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from builder.verify.object_family import classify_family

DATA = pathlib.Path(__file__).resolve().parent.parent / "data"

# 收尾命令（不单独成 candidate）
CLOSING_CMDS = {"SET LICENSESWITCH", "SET REFRESHSRV", "MOD USERPROFILE"}
# 查询/调测类命令（同意图合并）
QUERY_VERBS = {"LST", "DSP"}


def heuristic_split(doc):
    """对单份文档的 steps 做启发式拆分。"""
    steps = doc["steps"]
    n = len(steps)
    if n <= 2:
        # 简单文档 = 1 个 candidate
        return [list(range(n))]

    # 逐步分组
    groups = []
    current = [0]  # step index 列表

    for i in range(1, n):
        prev_step = steps[i - 1]
        curr_step = steps[i]

        prev_cmds = prev_step["commands"]
        curr_cmds = curr_step["commands"]

        # 规则1: 收尾命令 → 并入当前组
        if curr_cmds and all(c in CLOSING_CMDS for c in curr_cmds):
            current.append(i)
            continue

        # 规则2: 前一步全收尾且当前有实际命令 → 可能新组
        prev_is_closing = prev_cmds and all(c in CLOSING_CMDS for c in prev_cmds)

        # 规则3: 对象族切换
        prev_family = _dominant_family(prev_cmds)
        curr_family = _dominant_family(curr_cmds)
        family_switch = (prev_family and curr_family and
                         prev_family != curr_family and
                         prev_family not in {"LICENSE", "REFRESH", "OTHER"} and
                         curr_family not in {"LICENSE", "REFRESH", "OTHER"})

        # 规则4: step_desc 语义切换（简化：关键词重叠检查）
        desc_switch = _desc_similar(prev_step["step_desc"], curr_step["step_desc"])

        if family_switch and not prev_is_closing:
            # 对象族切换 = 新组
            groups.append(current)
            current = [i]
        elif prev_is_closing and not family_switch:
            # 前一步是收尾，当前有实际命令 → 新组
            groups.append(current)
            current = [i]
        else:
            # 同组
            current.append(i)

    groups.append(current)
    return groups


def _dominant_family(cmds):
    """取命令的主对象族（忽略收尾命令）。"""
    from collections import Counter
    families = Counter()
    for c in cmds:
        fam = classify_family(c)
        if fam not in {"LICENSE", "REFRESH"}:
            families[fam] += 1
    if not families:
        return None
    return families.most_common(1)[0][0]


def _desc_similar(desc1, desc2):
    """两个描述是否语义相似（简化：有共同关键词）。"""
    if not desc1 or not desc2:
        return True
    # 提取关键词（去掉标点）
    words1 = set(re.findall(r'[一-鿿]+', desc1))
    words2 = set(re.findall(r'[一-鿿]+', desc2))
    common = words1 & words2
    return len(common) > 0


def main():
    # 读已有 candidate 的 doc_path
    done = set()
    with open(DATA / "task_candidates.jsonl", encoding="utf-8") as f:
        for line in f:
            done.add(json.loads(line)["doc_path"])

    # 读全部 doc_steps，找未处理的
    remaining = []
    with open(DATA / "doc_steps.jsonl", encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            if d["doc_path"] not in done:
                remaining.append(d)

    print(f"待处理: {len(remaining)} docs")

    count = 0
    with open(DATA / "task_candidates.jsonl", "a", encoding="utf-8") as f:
        for doc in remaining:
            groups = heuristic_split(doc)
            fid = doc.get("feature_id", "")
            steps = doc["steps"]

            for gi, indices in enumerate(groups):
                sr = [steps[indices[0]]["step_num"], steps[indices[-1]]["step_num"]]
                # 检查 step_num 是否连续唯一（处理重复编号）
                step_nums = [steps[i]["step_num"] for i in indices]
                if len(set(step_nums)) != len(step_nums):
                    sr = None  # 有重复编号，标 None

                cmds = []
                for i in indices:
                    cmds.extend(steps[i]["commands"])

                # 取第一个非空 step_desc 作为 candidate_desc
                desc = ""
                for i in indices:
                    d = steps[i].get("step_desc", "")
                    if d:
                        desc = d[:40]
                        break

                f.write(json.dumps({
                    "doc_path": doc["doc_path"],
                    "feature_id": fid,
                    "candidate_id": f"{fid}#{gi+1:03d}" if fid else f"HEUR#{count+1:03d}",
                    "step_range": sr,
                    "candidate_desc": desc,
                    "commands": cmds,
                    "boundary_source": "heuristic",
                }, ensure_ascii=False) + "\n")
                count += 1

    print(f"追加 {count} candidates from {len(remaining)} docs")


if __name__ == "__main__":
    main()
