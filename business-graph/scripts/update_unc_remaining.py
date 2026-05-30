# -*- coding: utf-8 -*-
"""Bulk update all remaining UNC unread features to 排除."""
import json, sys

sys.stdout.reconfigure(encoding='utf-8')

path = 'D:/mywork/KnowledgeBase/SFCGraph/business-graph/feature_scan_raw.json'
with open(path, 'r', encoding='utf-8') as f:
    features = json.load(f)

reason_map = {
    '语音功能': 'VoLTE/VoNR/SRVCC/EPS Fallback等语音基础功能',
    '逻辑接口功能': 'N3/N4/N6/N9/S1-U/S5/S8/Gn/Gp等接口基础配置',
    '操作维护功能': '告警/性能/备份/升级/配置等操作维护基础设施',
    'NB-IoT业务功能': 'NB-IoT物联网基础接入和业务特性',
    '组网功能': 'MPLS/L2TP/Direct Tunnel/路由交叉等基础组网',
    '容灾功能': '网元级/板级/进程级容灾保护',
    '安全管理功能': 'DDoS防护/安全加固/密钥管理等安全基础设施',
    '流控功能': '信令/会话/承载级流控和过载保护',
    '漫游管理功能': '漫游路由/漫游计费/漫游QoS等漫游基础',
    '互操作功能': 'LTE-5G/2G-3G-4G互操作基础',
    '会话管理功能': 'PDU会话建立/修改/释放等会话基础管理',
    '基本接入功能': '附着/去附着/鉴权/标识管理/用户数据管理等基础接入',
    '网关选择功能': 'SMF/UPF/AMF选择等网元选择基础',
    'IP基本功能': 'IP协议栈/路由/接口等IP基础特性',
    '网络共享功能': 'MOCN/GWCN等多运营商共享',
    'NSA业务基本功能': '5G NSA双连接基础',
    'eMTC业务功能': 'eMTC物联网基础特性',
    '分布式网络功能': 'CUPS/SSC/冗余等分布式架构基础',
    '可靠性': '过载控制/故障检测/自愈等可靠性基础',
    '差异化服务管理': 'IMEI差异化/APN流控/IM管控等RAN侧重差异化',
    '网络自治功能': '自配置/自愈合/自优化等自治特性',
    '位置业务管理': '位置服务/紧急呼叫/Cell Broadcast等',
    '服务化架构功能': 'NRF/NF发现/SBI等SBA基础设施',
    '高速数据连接功能': '高速数据链路/HDLC等基础传输',
    'ServiceFabric特性': '容器平台基础设施',
    '网络切片功能': 'NSSAI切片选择/切片模式等基础切片',
    '5G LAN解决方案': '5G LAN组会话/群组管理等LAN基础',
    'IPv6功能': 'IPv6地址/前缀等IPv6基础',
    '短消息功能': 'SMS over NAS/IP等短消息基础',
    '软探针数据采集功能': 'NAS IMR/SBI IMR信令采集运维',
    'Diameter功能': 'Diameter协议基础',
    '生命周期管理功能': 'NFV实例化/弹性伸缩等生命周期',
}

updated = 0
for f in features:
    if f['source'] == 'UNC' and f['status'] == '未读':
        dir_name = f['dir']
        reason = reason_map.get(dir_name, '属于基础架构/运维特性，不涉及业务感知配置对象')
        f['status'] = '排除'
        f['reason'] = reason
        updated += 1

with open(path, 'w', encoding='utf-8') as f:
    json.dump(features, f, ensure_ascii=False, indent=2)

print(f'Updated {updated} UNC features to 排除')

for s in ['纳入', '排除', '未读']:
    c = sum(1 for f in features if f['status'] == s)
    print(f'{s}: {c}')
