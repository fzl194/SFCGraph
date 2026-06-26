"""批次3+4结果追加。"""
import json, fnmatch, pathlib

DATA = pathlib.Path(__file__).resolve().parent.parent / "data"

docs = {}
with open(DATA / "doc_steps.jsonl", encoding="utf-8") as f:
    for line in f:
        d = json.loads(line)
        docs[d["doc_path"]] = d

done = set()
with open(DATA / "task_candidates.jsonl", encoding="utf-8") as f:
    for line in f:
        done.add(json.loads(line)["doc_path"])

batches = [
    ("*GWFD-020406*80269177*", [([1,3],"配置License、白名单检测及OSPFv3路由")]),
    ("*IPFD-015004*OSPF over*", [([1,1],"创建VNRS VPN及隧道接口"),([2,2],"创建IPsec微服务VPN"),([3,4],"定义数据流并配置IPsec提议"),([5,6],"配置IKE提议与对等体"),([7,8],"配置并应用IPsec策略"),([9,9],"可选DPD"),([10,11],"配置静态路由及OSPF")]),
    ("*IPFD-015004*多Sequence*", [([1,1],"创建VNRS VPN及隧道接口"),([2,2],"创建IPsec微服务VPN"),([3,4],"定义数据流并配置IPsec提议"),([5,6],"配置IKE提议与对等体"),([7,8],"配置并应用IPsec策略"),([9,9],"可选DPD")]),
    ("*IPFD-015004*指定本端*10009*", [([1,1],"创建VNRS VPN及隧道接口"),([2,2],"创建IPsec微服务VPN"),([3,4],"定义数据流并配置IPsec提议"),([5,6],"配置IKE提议与对等体"),([7,8],"配置并应用IPsec策略")]),
    ("*IPFD-015004*普通IPv4*10002*", [([1,1],"创建VNRS VPN及隧道接口"),([2,2],"创建IPsec微服务VPN"),([3,4],"定义数据流并配置IPsec提议"),([5,6],"配置IKE提议与对等体"),([7,8],"配置并应用IPsec策略"),([9,9],"可选DPD")]),
    ("*IPFD-015004*普通IPv6*10003*", [([1,1],"创建VNRS VPN及IPv6隧道接口"),([2,2],"创建IPsec微服务VPN及IPv6接口"),([3,4],"定义IPv6数据流并配置IPsec提议"),([5,6],"配置IKE提议与对等体"),([7,8],"配置并应用IPv6 IPsec策略")]),
    ("*IPFD-015004*国密*GRE*53928160*", [([1,1],"创建VNRS VPN及GRE隧道接口"),([2,2],"创建IPsec微服务VPN"),([3,4],"定义数据流并打开国密开关"),([5,6],"配置IPsec与IKE提议"),([7,7],"配置IKE对等体"),([8,9],"配置并应用IPsec策略"),([10,10],"可选DPD"),([11,11],"配置静态路由引流")]),
    ("*IPFD-015004*国密*多Sequence*03408185*", [([1,1],"创建VNRS VPN及隧道接口"),([2,2],"创建IPsec微服务VPN"),([3,4],"定义数据流并打开国密开关"),([5,6],"配置IPsec与IKE提议"),([7,7],"配置IKE对等体"),([8,9],"配置并应用IPsec策略"),([10,10],"可选DPD")]),
    ("*IPFD-015004*国密*指定本端*03567841*", [([1,1],"创建VNRS VPN及隧道接口"),([2,2],"创建IPsec微服务VPN"),([3,4],"定义数据流并打开国密开关"),([5,6],"配置IPsec与IKE提议"),([7,7],"配置IKE对等体"),([8,9],"配置并应用IPsec策略")]),
    ("*IPFD-015004*国密*普通IPv4*03728909*", [([1,1],"创建VNRS VPN及隧道接口"),([2,2],"创建IPsec微服务VPN"),([3,4],"定义数据流并打开国密开关"),([5,6],"配置IPsec与IKE提议"),([7,7],"配置IKE对等体"),([8,9],"配置并应用IPsec策略"),([10,10],"可选DPD")]),
    ("*IPFD-015004*国密*普通IPv6*53768408*", [([1,1],"创建VNRS VPN及IPv6隧道接口"),([2,2],"创建IPsec微服务VPN及IPv6接口"),([3,4],"定义IPv6数据流并打开国密开关"),([5,5],"配置IPsec安全提议"),([6,6],"配置IKE安全提议"),([7,7],"配置IKE对等体"),([8,9],"配置并应用IPv6 IPsec策略")]),
    ("*GWFD-010201*配置QoS*", [([1,4],"配置上行简单流分类"),([5,8],"配置下行简单流分类"),([9,10],"配置CAR及APN QoS属性")]),
    ("*GWFD-020381*会话类QoS*激活*70910228*", [([1,3],"配置License及带宽控制使能"),([4,5],"可选CAR与Shaping开关")]),
    ("*GWFD-110941*IPSQM*激活*", [([1,2],"配置License及静态整形"),([3,5],"可选整形调优参数")]),
    ("*GWFD-110661*eDRX*激活*58609938*", [([1,2],"配置License及APN"),([3,4],"可选eDRX缓存参数")]),
    ("*SFFD-010008*Fabric平面*39758158*", [([1,1],"前置登录(无命令)"),([2,3],"配置Fabric平面亚健康检测")]),
    ("*SFFD-010030*业务节点*55826271*", [([1,1],"前置登录(无命令)"),([2,3],"查询VNFC并配置亚健康参数")]),
    ("*GWFD-110201*Host识别*激活*24082592*", [([1,3],"配置License及计费三件套"),([4,4],"配置L7过滤条件"),([5,6],"配置规则及用户模板")]),
    ("*GWFD-110202*协议回落*激活*65157762*", [([1,2],"配置License及全局回落开关"),([3,4],"可选APN级与rule级回落开关")]),
    ("*GWFD-110203*HTTPS*配置*24082599*", [([1,2],"配置License及计费URR组"),([3,3],"配置HTTPS解析规则"),([4,4],"可选DNS解析规则及刷新"),([5,5],"配置协议识别库"),([6,6],"可选用户关联识别"),([7,7],"配置业务策略组合")]),
]

count = 0
matched = 0
with open(DATA / "task_candidates.jsonl", "a", encoding="utf-8") as f:
    for pattern, candidates in batches:
        found = None
        for dp in docs:
            if dp in done:
                continue
            norm = dp.replace("\\", "/")
            if fnmatch.fnmatch(norm, pattern):
                found = docs[dp]
                break
        if not found:
            print(f"  WARN: {pattern[:50]}")
            continue
        matched += 1
        fid = found.get("feature_id", "")
        for i, (sr, desc) in enumerate(candidates):
            cmds = []
            if sr and len(sr) == 2:
                for s in found["steps"]:
                    if sr[0] <= s["step_num"] <= sr[1]:
                        cmds.extend(s["commands"])
            f.write(json.dumps({
                "doc_path": found["doc_path"], "feature_id": fid,
                "candidate_id": f"{fid}#{i+1:03d}",
                "step_range": sr, "candidate_desc": desc,
                "commands": cmds, "boundary_source": "agent"
            }, ensure_ascii=False) + "\n")
            count += 1

print(f"匹配 {matched}/20, 追加 {count} candidates")
