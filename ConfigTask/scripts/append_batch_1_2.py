"""把批次1+2的 Agent 结果追加到 task_candidates.jsonl。
直接用 Agent 确定的 step_range 从 doc_steps.jsonl 取 commands。
"""
import json
import pathlib
import fnmatch

DATA_DIR = pathlib.Path(__file__).resolve().parent.parent / "data"

# 读 doc_steps
docs = {}
with open(DATA_DIR / "doc_steps.jsonl", encoding="utf-8") as f:
    for line in f:
        d = json.loads(line)
        docs[d["doc_path"]] = d

# 批次1+2 的 Agent 拆分结果（doc_path 匹配模式 → [(step_range, desc), ...]）
results = [
    # 批次1
    ("*GWFD-020401*激活IPv6承载上下文*", [( [1,3], "配置License及VPN实例"), ([4,6], "配置路由策略及节点匹配"), ([7,9], "启动OSPFv3并发布WLR路由")]),
    ("*GWFD-020402*N6_Gi_SGi*激活*", [([1,4], "配置License、VPN实例及外联口IPv6"), ([5,6], "配置IPv6路径MTU及可选静态路由")]),
    ("*GWFD-020406*外部网元地址分配*激活*", [([1,3], "配置License、白名单检测及手机下行OSPFv3路由")]),
    ("*GWFD-020406*基于APN_DNN分配地址_8025*", [([1,2], "配置License及APN/DNN地址分配属性"), ([3,5], "配置地址池组、映射及分配规则"), ([6,6], "配置手机下行OSPFv3路由")]),
    ("*GWFD-020406*基于SMF+APN_DNN*", [([1,2], "配置License及APN/DNN地址分配属性"), ([3,5], "配置地址池组、SMF映射及分配规则"), ([6,7], "配置基于SMF分配开关及OSPFv3路由")]),
    ("*GWFD-020406*基于SMF分配地址_8025*", [([1,2], "配置License及APN/DNN地址分配属性"), ([3,5], "配置地址池组、SMF映射及分配规则"), ([6,7], "配置基于SMF分配开关及OSPFv3路由")]),
    ("*GWFD-020406*基于位置分配地址*", [([1,2], "配置License及APN/DNN地址分配属性"), ([3,6], "配置地址池组及TAC/LAC位置区映射"), ([7,9], "配置分配规则、位置开关及OSPF路由"), ([10,10], "配置位置区分配白名单")]),
    ("*IPFD-012001*去激活QoS复杂流分类*", [([1,8], "去激活QoS复杂流分类(删除流策略/分类/行为)")]),
    ("*IPFD-012001*激活QoS复杂流分类*13119479*", [([1,5], "配置ACL规则组、流行为及流分类"), ([6,8], "配置流策略并应用到接口")]),
    ("*IPFD-012001*调测QoS复杂流分类*", [([1,13], "调测QoS复杂流分类(查询验证)")]),
    # 批次2
    ("*IPFD-012001*去激活QoS简单流分类*", [([1,4], "去激活QoS简单流分类")]),
    ("*IPFD-012001*激活QoS简单流分类*13119472*", [([1,5], "激活QoS简单流分类")]),
    ("*IPFD-012002*去激活支持ACL_06381762*", [([1,5], "去激活ACL(删除规则及组)")]),
    ("*IPFD-012002*激活支持ACL_06381760*", [([1,5], "激活ACL(增加规则及组)")]),
    ("*IPFD-015002*激活支持GRE_06422610*", [([1,3], "配置GRE基础(LoopBack/Tunnel/静态路由)"), ([4,6], "配置GRE可选功能(校验/关键字/Keepalive)")]),
    ("*IPFD-015004*上传IPsec证书_01_10001*", [([1,6], "上传并验证IPsec证书")]),
    ("*IPFD-015004*上传国密IPsec证书*", [([1,6], "上传并验证国密IPsec证书")]),
    ("*IPFD-015004*GRE over IPsec*", [([1,2], "创建VNRS与IPsec微服务VPN及隧道接口"), ([3,3], "定义IPsec保护数据流"), ([4,6], "配置IPsec提议与IKE对等体"), ([7,9], "配置并应用IPsec安全策略"), ([10,10], "配置静态路由引流")]),
    ("*IPFD-015004*IPv4 IPsec主备*", [([1,2], "创建VPN及IPsec隧道接口及引流路由"), ([3,3], "定义IPsec保护数据流"), ([4,6], "配置IPsec提议与IKE对等体"), ([7,9], "配置并应用IPsec安全策略")]),
    ("*IPFD-015004*IPv6 IPsec隧道主备*", [([1,2], "创建VPN及IPv6 IPsec隧道接口及引流路由"), ([3,3], "定义IPv6 IPsec保护数据流"), ([4,6], "配置IPsec提议与IKE对等体"), ([7,8], "配置并应用IPv6 IPsec安全策略")]),
]

# 匹配 doc_path 并追加 candidates
output_file = DATA_DIR / "task_candidates.jsonl"
count = 0
matched = 0

with open(output_file, "a", encoding="utf-8") as f:
    for pattern, candidates in results:
        # 用 fnmatch 找 doc_path
        found_doc = None
        for dp, doc in docs.items():
            normalized = dp.replace("\\", "/")
            if fnmatch.fnmatch(normalized, pattern):
                found_doc = doc
                break
        if not found_doc:
            print(f"  WARN: 未匹配 {pattern}")
            continue
        matched += 1
        fid = found_doc.get("feature_id", "")
        for i, (sr, desc) in enumerate(candidates):
            # 从 doc steps 精确取 commands
            cmds = []
            if sr and len(sr) == 2:
                for s in found_doc["steps"]:
                    if sr[0] <= s["step_num"] <= sr[1]:
                        cmds.extend(s["commands"])
            record = {
                "doc_path": found_doc["doc_path"],
                "feature_id": fid,
                "candidate_id": f"{fid}#{i+1:03d}" if fid else f"BATCH#{count+1:03d}",
                "step_range": sr,
                "candidate_desc": desc,
                "commands": cmds,
                "boundary_source": "agent",
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            count += 1

print(f"匹配 {matched}/{len(results)} 文档, 追加 {count} candidates")
