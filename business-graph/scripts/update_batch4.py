# -*- coding: utf-8 -*-
"""Update feature status based on batch 4 reading - all remaining UDG features."""
import json, sys

sys.stdout.reconfigure(encoding='utf-8')

path = 'D:/mywork/KnowledgeBase/SFCGraph/business-graph/feature_scan_raw.json'
with open(path, 'r', encoding='utf-8') as f:
    features = json.load(f)

# All remaining UDG unread features are infrastructure/platform, not business-awareness
reason_map = {
    '5G NSA功能': '5G NSA组网属于基础接入架构',
    'IPv6功能': 'IPv6功能描述属于基础网络概述',
    'IP基本特性': 'IP协议栈/可靠性属于IP基础特性',
    'Redcap终端节能管理': 'Redcap终端节能/接入属于终端管理特性',
    'Service Fabric特性（虚机）': 'Service Fabric虚机平台基础设施',
    '分布式网络功能': 'CUPS/SSC/负载上报/集中配置/Full Mesh属于基础网络架构',
    '可靠性功能': '过载控制/故障隔离/可靠性定义属于系统可靠性',
    '基本接入功能': '会话管理/3GPP接入属于基础接入',
    '媒体中继解决方案': '媒体中继属于IMS媒体面基础功能',
    '安全管理功能': 'DDoS防护/安全加固/隐私/密钥属于安全基础设施',
    '性能优化': '软件性能优化/入不转板/规格提升/加速卡属于性能基础设施',
    '支持专用DNN_APN园区终端互访控制': '园区终端互访控制属于基础接入配置',
    '智家随行解决方案': '智网接入属于家庭网络方案',
    '智能转发解决方案': '5G-A高通量会话属于大带宽转发优化',
    '服务化架构功能': '云化分布式/微服务/融合架构属于平台架构',
    '物联网功能': 'NB-IoT/eMTC属于物联网基础接入',
    '生命周期管理功能': '实例化/Scale In/Out/Termination属于NFV运维',
    '移动性管理功能': 'LTE-5G互操作/移动性管理/Proxy UPF属于移动性基础',
    '组网功能': 'MPLS VPN/L2TP VPN/Direct Tunnel/路由交叉属于基础组网',
    '网管特性': '操作维护/可靠性属于网管基础设施',
    '网络质量上报': '黄金指标属于性能监控运维',
    '逻辑接口功能': 'N3/N4/N6/N9/SGi/Gn等接口属于基础接口配置',
}

updated = 0
for f in features:
    if f['source'] == 'UDG' and f['status'] == '未读':
        dir_name = f['dir']
        reason = reason_map.get(dir_name, '属于基础架构/运维特性，不涉及业务感知配置对象')
        f['status'] = '排除'
        f['reason'] = reason
        updated += 1

with open(path, 'w', encoding='utf-8') as f:
    json.dump(features, f, ensure_ascii=False, indent=2)

print(f'Updated {updated} UDG features to 排除')

for s in ['纳入', '排除', '未读']:
    c = sum(1 for f in features if f['status'] == s)
    print(f'{s}: {c}')
