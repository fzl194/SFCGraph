# -*- coding: utf-8 -*-
"""Update feature status based on batch 3 reading (基本接入+语音+IPv6+IP基本)."""
import json, sys

sys.stdout.reconfigure(encoding='utf-8')

path = 'D:/mywork/KnowledgeBase/SFCGraph/business-graph/feature_scan_raw.json'
with open(path, 'r', encoding='utf-8') as f:
    features = json.load(f)

# Batch 3 decisions
updates = {
    # IPv6功能
    'GWFD-020352': ('纳入', 'SA能力的IPv6扩展，对IPv6报文进行业务感知，支持IPv6内容计费/URL重定向/P2P流量控制'),
    'GWFD-020404': ('纳入', 'IPv6/双栈用户在线计费(OCS实时配额管理)，与计费场景(NS-01)关联'),
    'GWFD-020401': ('排除', 'IPv6承载上下文基本管理(PDP/EPS/PDU)，属于基础接入'),
    'GWFD-020402': ('排除', 'N6/Gi/SGi接口IPv6组网配置，属于基础网络配置'),
    'GWFD-020403': ('排除', 'IPv4v6双栈接入基本能力，属于基础接入'),
    'GWFD-020405': ('排除', '逻辑接口支持IPv6配置，属于基础网络配置'),
    'GWFD-020406': ('排除', 'IPv6前缀委派，属于基础地址管理'),

    # 基本接入功能
    'GWFD-010151': ('纳入', '基于带宽使用情况的接入控制，与带宽控制场景(NS-02)关联'),
    'GWFD-010102': ('排除', '路径管理(通信路径故障检测)，属于基础运维'),
    'GWFD-010103': ('排除', '数据转发基本功能，属于基础接入'),
    'GWFD-010104': ('排除', 'IP地址分配方式，属于基础接入'),
    'GWFD-010105': ('排除', '用户面地址分配，属于基础接入'),
    'GWFD-010107': ('排除', '静态地址用户路由冗余，属于可靠性特性'),
    'GWFD-010108': ('排除', '用户面地址自动检测，属于基础运维'),
    'GWFD-010155': ('排除', 'Untrusted Non-3GPP网络用户接入，属于基础接入'),
    'GWFD-020421': ('排除', '基于位置的地址分配，属于基础接入'),
    'GWFD-110910': ('排除', 'Routing Behind MS，属于路由特性'),
    'GWFD-010106': ('排除', '峰值License控制，属于License规格'),

    # 语音功能 - 全部排除(IMS语音基础，不涉及业务感知配置对象)
    'GWFD-020251': ('排除', 'VoLTE IMS语音基础接入，属于语音基本功能'),
    'GWFD-020252': ('排除', 'SRVCC语音连续性，属于语音切换特性'),
    'GWFD-020253': ('排除', 'P-CSCF故障时IMS恢复，属于语音可靠性'),
    'GWFD-020254': ('排除', 'VoLTE业务快速恢复，属于语音可靠性'),
    'GWFD-020281': ('排除', 'VoNR 5G语音基础接入，属于语音基本功能'),
    'GWFD-020282': ('排除', 'EPS Fallback 5G语音回落，属于语音切换特性'),
    'GWFD-112000': ('排除', '双故障Bypass，属于语音可靠性特性'),

    # IP基本特性 - 全部排除(基础网络能力)
    'IPFD-010000': ('排除', '接口与链路基本配置(VLAN子接口)，属于IP基础特性'),
    'IPFD-014000': ('排除', '路由功能(静态路由)，属于IP基础特性'),
    'IPFD-015000': ('排除', 'VPN功能(VRF)，属于IP基础特性'),
    'IPFD-015004': ('排除', 'IPSec安全功能，属于IP基础特性'),
    'IPFD-014007': ('排除', 'L2/L3跟踪调试，属于IP基础特性'),
    'IPFD-015003': ('排除', 'SNMP网管协议，属于IP基础特性'),
}

updated = 0
for f in features:
    fid = f['id']
    if fid in updates:
        status, reason = updates[fid]
        if f['status'] == '未读':
            f['status'] = status
            f['reason'] = reason
            updated += 1

with open(path, 'w', encoding='utf-8') as f:
    json.dump(features, f, ensure_ascii=False, indent=2)

print(f'Updated {updated} features')

for s in ['纳入', '排除', '未读']:
    c = sum(1 for f in features if f['status'] == s)
    print(f'{s}: {c}')
