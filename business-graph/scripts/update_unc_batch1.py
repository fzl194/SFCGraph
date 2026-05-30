# -*- coding: utf-8 -*-
"""Update feature status based on UNC batch 1 (MEC解决方案+QoS功能)."""
import json, sys

sys.stdout.reconfigure(encoding='utf-8')

path = 'D:/mywork/KnowledgeBase/SFCGraph/business-graph/feature_scan_raw.json'
with open(path, 'r', encoding='utf-8') as f:
    features = json.load(f)

updates = {
    # MEC解决方案 - 纳入(本地分流核心特性)
    'WSFD-108002': ('纳入', 'UL CL预定义规则分流控制，SMF基于DNN/位置/DNAI选择ULCL UPF，与本地分流(NS-04)直接关联'),
    'WSFD-223001': ('纳入', '基于小区粒度的UL CL分流，PCF订阅实时位置+PRA区域控制SMF分流，与本地分流(NS-04)直接关联'),
    'WSFD-223003': ('纳入', '漫游场景动态签约分流控制，与本地分流(NS-04)关联'),
    'WSFD-223004': ('纳入', 'AF/NEF动态下发分流规则到SMF，与本地分流(NS-04)关联'),
    'WSFD-223101': ('纳入', '4G侧预定义规则分流策略控制，与本地分流(NS-04)关联'),
    'WSFD-223102': ('纳入', '4G侧AF/PCRF动态下发分流规则，与本地分流(NS-04)关联'),
    'WSFD-228001': ('纳入', '跨域UL CL分流实现2C用户访问2B业务+公网，与本地分流(NS-04)关联'),
    'WSFD-228002': ('纳入', '通用DNN漫游分流，公网+专网双会话，与本地分流(NS-04)关联'),
    'WSFD-228003': ('纳入', '公网/私网业务独立计费，通用DNN漫游+专用DNN分流，与计费(NS-01)+本地分流(NS-04)直接关联'),

    # MEC解决方案 - 排除
    'WSFD-108004': ('排除', 'MEC冗余模式故障保护，属于可靠性特性'),
    'WSFD-108005': ('排除', 'MEC单点模式故障保护，属于可靠性特性'),
    'WSFD-108007': ('排除', '终端二次鉴权，属于安全认证特性'),
    'WSFD-223005': ('排除', 'SMF选择ULCL合一组网，属于基础组网配置'),
    'WSFD-223006': ('排除', '基于DNN插入I-UPF，属于基础组网配置'),

    # QoS功能 - 纳入
    'WSFD-010701': ('纳入', 'QoS基础框架，Diff-Serv模型+3GPP QoS分类，与带宽控制(NS-02)关联'),
    'WSFD-105102': ('纳入', '会话类QoS等级业务承载，VoIP/视频带宽保障，与带宽控制(NS-02)关联'),
    'WSFD-109202': ('纳入', '会话类QOS保证(流分类/带宽控制/高优先级队列)，与带宽控制(NS-02)关联'),
    'WSFD-109203': ('纳入', '本地QOS策略控制，SMF本地QoS规则下发，与带宽控制(NS-02)关联'),

    # QoS功能 - 排除
    'WSFD-010702': ('排除', '背景类/交互类/流类QoS业务承载，属于传统3G QoS分类'),
    'WSFD-010703': ('排除', '增强的QoS特性，属于基础QoS增强'),
    'WSFD-105001': ('排除', 'SGSN QoS覆盖(版本转换)，属于传统2G/3G特性'),
    'WSFD-105002': ('排除', '漫游用户QoS限速，属于漫游QoS配置'),
    'WSFD-105004': ('排除', '逻辑接口DSCP标记配置，属于基础QoS标记'),
    'WSFD-105007': ('排除', '5G到4G QoS映射，属于QoS互操作配置'),
    'WSFD-105101': ('排除', 'PFC(2G Gb模式)，属于传统2G特性'),
    'WSFD-105103': ('排除', '基于用户等级的QCI扩展，属于基础QoS配置'),
    'WSFD-105104': ('排除', '基于IMSI号段的QoS控制，属于基础QoS配置'),
    'WSFD-105105': ('排除', 'PCC模式本地QoS策略控制，属于基础QoS配置'),
    'WSFD-109204': ('排除', 'QCI扩展，属于基础QoS参数扩展'),
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
