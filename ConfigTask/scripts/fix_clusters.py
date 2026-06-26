"""修复聚类问题：
1. 命令名规范化（BwmController→BWMCONTROLLER, PCCPOLICYGR→PCCPOLICYGRP）
2. cluster-007 拆分（MOD USERPROFILE 归 USERPROFILE 簇，LICENSESWITCH 独立）
3. IPSec 同语义簇合并（Jaccard > 0.6 多轮迭代合并）
4. cluster-045≡042 合并（命令相同仅顺序差异）
5. 通用命令簇（ADD RULE/USERPROFILE）加 business_domain 标签
"""
import json
import re
from collections import defaultdict

DATA_DIR = __file__.replace("\\", "/").rsplit("/", 1)[0].rsplit("/", 1)[0]
DATA_DIR = DATA_DIR + "/data"

# 命令名规范化映射
CMD_NORMALIZE = {
    "ADD BwmController": "ADD BWMCONTROLLER",
    "ADD PCCPOLICYGR": "ADD PCCPOLICYGRP",
    "ADD PCCPOLICYGR\n": "ADD PCCPOLICYGRP",
    "MOD IMPORTROUTE": "MOD OSPFIMPORTROUTE",
}

# 业务域标签规则（根据 feature_id 或 desc 推断）
DOMAIN_RULES = [
    ("计费", ["计费", "URR", "费率", "在线计费", "离线计费", "融合计费", "内容计费", "时长计费", "流量计费", "事件计费"]),
    ("带宽控制", ["BWM", "带宽", "整形", "Shaping", "码率", "流量管控"]),
    ("访问限制", ["Portal", "Web Proxy", "重定向", "DNS纠错", "URL过滤", "HTTPS", "HTTP"]),
    ("QoS", ["QoS", "流分类", "CAR", "PHB", "DiffServ"]),
    ("地址分配", ["地址分配", "地址池", "POOL", "Prefix Delegation"]),
    ("安全", ["IPsec", "IPSec", "GRE", "ACL", "DDoS", "防欺诈"]),
    ("接入控制", ["接入控制", "APN", "eDRX"]),
    ("语音", ["VoLTE", "VoNR", "SRVCC", "IMS"]),
]


def normalize_cmds(cmds):
    return [CMD_NORMALIZE.get(c, c) for c in cmds]


def infer_domain(member):
    text = (member.get("feature_id", "") + " " + member.get("candidate_desc", "") + " " + " ".join(member.get("commands", [])))
    for domain, keywords in DOMAIN_RULES:
        if any(kw in text for kw in keywords):
            return domain
    return "其他"


def jaccard(a, b):
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 1.0
    return len(sa & sb) / len(sa | sb) if (sa | sb) else 0.0


def core_commands(cmds):
    OPTIONAL = {"SET LICENSESWITCH", "SET REFRESHSRV", "MOD USERPROFILE"}
    return tuple(c for c in cmds if c not in OPTIONAL)


def main():
    # 1. 读 candidates，规范化命令名
    candidates = []
    with open(f"{DATA_DIR}/task_candidates.jsonl", encoding="utf-8") as f:
        for line in f:
            c = json.loads(line)
            c["commands"] = normalize_cmds(c["commands"])
            candidates.append(c)

    # 2. 读现有 clusters，提取所有 member 信息
    old_clusters = []
    with open(f"{DATA_DIR}/task_clusters.jsonl", encoding="utf-8") as f:
        for line in f:
            old_clusters.append(json.loads(line))

    # 3. 收集所有 member（规范化命令）
    all_members = []
    for cl in old_clusters:
        for m in cl["members"]:
            m["commands"] = normalize_cmds(m["commands"])
            m["business_domain"] = infer_domain(m)
            all_members.append(m)

    # 4. 处理 cluster-007（空核心命令）
    # 分离：MOD USERPROFILE 归 USERPROFILE 类，LICENSESWITCH 独立
    non_empty = [m for m in all_members if core_commands(m["commands"])]
    empty = [m for m in all_members if not core_commands(m["commands"])]

    # 把空命令 member 按其原始命令分组
    license_only = [m for m in empty if all(c == "SET LICENSESWITCH" for c in m["commands"])]
    other_empty = [m for m in empty if not all(c == "SET LICENSESWITCH" for c in m["commands"])]

    # other_empty 的命令追加到同 doc_path 的非空 member
    for oe in other_empty:
        doc = oe["doc_path"]
        target = next((m for m in non_empty if m["doc_path"] == doc), None)
        if target:
            for c in oe["commands"]:
                if c not in target["commands"]:
                    target["commands"].append(c)
        else:
            # 没有同文档非空 member，加入 license_only 作为独立
            license_only.append(oe)

    # 5. 重新聚类（基于规范化后的命令）
    # 第一轮：精确匹配
    groups = defaultdict(list)
    for m in non_empty:
        key = core_commands(m["commands"])
        groups[key].append(m)

    # 第二轮：多轮 Jaccard > 0.6 合并
    changed = True
    while changed:
        changed = False
        keys = list(groups.keys())
        for i in range(len(keys)):
            if keys[i] not in groups:
                continue
            for j in range(i + 1, len(keys)):
                if keys[j] not in groups:
                    continue
                score = jaccard(keys[i], keys[j])
                if score >= 0.6:
                    # 合并 j → i
                    groups[keys[i]].extend(groups[keys[j]])
                    del groups[keys[j]]
                    changed = True

    # 第三轮：单成员簇 Jaccard > 0.5 合并到多成员
    multi = {k: v for k, v in groups.items() if len(v) > 1}
    singles = {k: v for k, v in groups.items() if len(v) == 1}

    for s_key, s_members in list(singles.items()):
        best_target = None
        best_score = 0.5
        for m_key in multi:
            score = jaccard(s_key, m_key)
            if score > best_score:
                best_score = score
                best_target = m_key
        if best_target:
            multi[best_target].extend(s_members)
            del singles[s_key]

    # 6. License-only member 作为一个特殊簇
    license_members = []
    seen_docs = set()
    for m in license_only:
        if m["doc_path"] not in seen_docs:
            license_members.append(m)
            seen_docs.add(m["doc_path"])

    # 7. 构建最终簇列表
    final = []
    cid = 0

    # 非空簇
    for key in sorted(multi.keys(), key=lambda k: -len(multi[k])):
        cid += 1
        members = multi[key]
        # 推断主业务域
        domains = [m.get("business_domain", "其他") for m in members]
        from collections import Counter
        domain_counter = Counter(domains)
        primary_domain = domain_counter.most_common(1)[0][0]
        all_domains = list(set(domains))

        final.append({
            "cluster_id": f"cluster-{cid:03d}",
            "core_commands": list(key),
            "member_count": len(members),
            "business_domains": all_domains if len(all_domains) > 1 else [primary_domain],
            "primary_domain": primary_domain,
            "cross_domain": len(all_domains) > 1,
            "members": [{"candidate_id": m["candidate_id"], "doc_path": m["doc_path"],
                        "feature_id": m["feature_id"], "commands": m["commands"],
                        "candidate_desc": m.get("candidate_desc", ""),
                        "business_domain": m.get("business_domain", "其他")}
                       for m in members],
        })

    # 未合并的单成员簇
    for key, members in singles.items():
        cid += 1
        m = members[0]
        final.append({
            "cluster_id": f"cluster-{cid:03d}",
            "core_commands": list(key),
            "member_count": 1,
            "business_domains": [m.get("business_domain", "其他")],
            "primary_domain": m.get("business_domain", "其他"),
            "cross_domain": False,
            "members": [{"candidate_id": m["candidate_id"], "doc_path": m["doc_path"],
                        "feature_id": m["feature_id"], "commands": m["commands"],
                        "candidate_desc": m.get("candidate_desc", ""),
                        "business_domain": m.get("business_domain", "其他")}],
        })

    # License-only 簇
    if license_members:
        cid += 1
        final.append({
            "cluster_id": f"cluster-{cid:03d}",
            "core_commands": ["SET LICENSESWITCH"],
            "member_count": len(license_members),
            "business_domains": list(set(infer_domain(m) for m in license_members)),
            "primary_domain": "其他",
            "cross_domain": True,
            "members": [{"candidate_id": m["candidate_id"], "doc_path": m["doc_path"],
                        "feature_id": m["feature_id"], "commands": m["commands"],
                        "candidate_desc": m.get("candidate_desc", ""),
                        "business_domain": infer_domain(m)}
                       for m in license_members],
        })

    # 8. 写产出
    with open(f"{DATA_DIR}/task_clusters.jsonl", "w", encoding="utf-8") as f:
        for cl in final:
            f.write(json.dumps(cl, ensure_ascii=False) + "\n")

    # 9. 核查
    all_member_ids = set()
    for cl in final:
        for m in cl["members"]:
            all_member_ids.add(m["candidate_id"])

    from collections import Counter as CCounter
    size_dist = CCounter(cl["member_count"] for cl in final)
    cross_count = sum(1 for cl in final if cl.get("cross_domain"))
    print(f"修复后: {len(final)} 簇, {len(all_member_ids)} members")
    print(f"大小分布: {dict(sorted(size_dist.items()))}")
    print(f"跨业务域簇: {cross_count}")
    print(f"License-only 簇: {len(license_members)} members")

    # 写审查文件
    with open(f"{DATA_DIR}/cluster_audit.md", "w", encoding="utf-8") as f:
        f.write(f"# 簇审查清单（修复后 {len(final)} 簇）\n\n")
        for cl in sorted(final, key=lambda x: -x["member_count"]):
            cross = " ⚡跨域" if cl.get("cross_domain") else ""
            domains = "/".join(cl.get("business_domains", []))
            f.write(f"## {cl['cluster_id']} ({cl['member_count']}人) [{domains}]{cross}\n")
            f.write(f"- 核心命令: {cl['core_commands'][:5]}\n")
            for m in cl["members"][:3]:
                f.write(f"  - {m['candidate_id']}: {m['candidate_desc'][:30]} | {m['feature_id']} | {m['business_domain']}\n")
            if cl["member_count"] > 3:
                f.write(f"  - ... ({cl['member_count']-3} more)\n")
            f.write("\n")


if __name__ == "__main__":
    main()
