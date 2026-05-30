# -*- coding: utf-8 -*-
"""Update feature status based on batch 2 reading (报表功能+智能运维功能)."""
import json, sys

sys.stdout.reconfigure(encoding='utf-8')

path = 'D:/mywork/KnowledgeBase/SFCGraph/business-graph/feature_scan_raw.json'
with open(path, 'r', encoding='utf-8') as f:
    features = json.load(f)

# Batch 2 decisions
updates = {
    # 报表功能 - 纳入(直接关联SA/策略控制/计费)
    'GWFD-111283': ('纳入', '智能板协同PCF+CloudUDN进行体验分析、保障策略触发和效果评估闭环，是体验保障场景的数据采集基础'),
    'GWFD-111701': ('纳入', '拥塞小区识别后下发策略控制进行流量优化，与带宽控制(NS-02)和策略控制场景关联'),
    'GWFD-111301': ('纳入', '业务感知基础能力，对报文进行SA识别感知业务，是SA报表数据源'),
    'GWFD-111302': ('纳入', '智能分析记录的流抽样增强，扩展SA采集范围，是业务感知报表基础能力'),
    'GWFD-111303': ('纳入', '阻塞流量上报反映FILTER/RULE规则执行效果，与访问限制(NS-03)场景关联，辅助策略优化'),
    'GWFD-111306': ('纳入', 'VOIP业务分析上报反映VoIP类业务SA识别和统计，与差异化计费(NS-01)和带宽控制(NS-02)场景关联'),
    'GWFD-111307': ('纳入', 'Web业务HTTP解析上报，是SA识别HTTP类业务的报表输出，与业务感知能力关联'),
    'GWFD-111309': ('纳入', 'PCC规则报表直接反映策略控制(PCCPOLICYGRP/RULE)执行效果，与策略控制场景直接关联'),
    'GWFD-111310': ('纳入', 'QUIC协议SA识别，是SA能力的协议扩展，反映业务感知覆盖QUIC的能力'),
    'GWFD-111313': ('纳入', '业务实时分析上报支撑2C套餐验证和2B体验监测，与业务感知闭环关联'),

    # 报表功能 - 排除(纯报表/运维，不直接涉及业务感知配置对象)
    'GWFD-111304': ('排除', '通用TCP/UDP传输层质量统计，属于运维分析特性，不直接涉及业务感知配置对象'),
    'GWFD-111305': ('排除', '用户实时位置分析上报，属于网络可视化特性，不直接涉及业务感知配置对象'),
    'GWFD-111308': ('排除', 'VoLTE语音质量MOS值监测上报，属于运维特性，不直接涉及业务感知配置对象'),
    'GWFD-111311': ('排除', '报表订阅控制机制，属于报表管理基础设施，不直接涉及业务感知配置对象'),
    'GWFD-111312': ('排除', '系统级统计(用户/应用/资源维度)，属于基础运维报表，非业务感知驱动'),
    'GWFD-111315': ('排除', 'VoNR语音质量监测上报，属于运维特性，不直接涉及业务感知配置对象'),

    # 智能运维功能 - 全部排除
    'GWFD-000104': ('排除', '用户面自动化开站部署特性，与业务感知无关'),
    'GWFD-020451': ('排除', '端到端用户跟踪调试工具，属于运维特性'),
    'GWFD-110493': ('排除', '云化性能数据采集(接口流量统计)，属于运维监控'),
    'GWFD-110921': ('排除', 'TWAMP承载网QoS监测协议，属于运维特性'),
    'GWFD-000105': ('排除', '用户面多部件一体化升级，属于版本升级运维特性'),
    'GWFD-110501': ('排除', '基于KPI的自动扩容，属于弹性伸缩运维特性'),
    'GWFD-110502': ('排除', '基于KPI的自动缩容，属于弹性伸缩运维特性'),
    'GWFD-110581': ('排除', 'TCP传输层质量分析辅助问题定位，属于数传问题诊断运维特性'),
    'GWFD-110582': ('排除', 'UDP传输层质量分析辅助问题定位，属于数传问题诊断运维特性'),
    'GWFD-111251': ('排除', 'ISSU在线Pod滚动升级，属于版本升级运维特性'),
    'GWFD-111252': ('排除', '灰度拨测和发布，属于版本升级运维特性'),
    'GWFD-111253': ('排除', '灰度升级无损回退，属于版本升级运维特性'),
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

# Stats
for s in ['纳入', '排除', '未读']:
    c = sum(1 for f in features if f['status'] == s)
    print(f'{s}: {c}')
