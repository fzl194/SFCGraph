# -*- coding: utf-8 -*-
"""Update feature status based on batch 1 reading."""
import json, sys

sys.stdout.reconfigure(encoding='utf-8')

path = 'D:/mywork/KnowledgeBase/SFCGraph/business-graph/feature_scan_raw.json'
with open(path, 'r', encoding='utf-8') as f:
    features = json.load(f)

# Batch 1 decisions
updates = {
    # QoS功能
    'GWFD-010201': ('纳入', 'QoS基础框架，Diff-Serv模型是带宽控制场景(NS-02)的用户面执行基础'),
    'GWFD-020101': ('排除', 'Reflective QoS是RAN侧特性，不直接涉及业务感知配置对象'),
    'GWFD-020381': ('纳入', '会话类QoS保证，VoIP/视频场景的带宽保障，与带宽控制场景互补'),
    'GWFD-110941': ('排除', '基站粒度静态整形，是承载网优化特性，非业务感知驱动'),
    'GWFD-010235': ('纳入', '缺省承载GBR保障，通过PCF/SMF规则触发，与策略控制场景关联'),
    # 5G超高带宽系列 - 都是License规格档位，本质相同
    'GWFD-110551': ('排除', 'License规格档位(1G基本)，非功能特性'),
    'GWFD-110552': ('排除', 'License规格档位(1G承载)'),
    'GWFD-110553': ('排除', 'License规格档位(2G基本)'),
    'GWFD-110554': ('排除', 'License规格档位(2G承载)'),
    'GWFD-110555': ('排除', 'License规格档位(5G基本)'),
    'GWFD-110556': ('排除', 'License规格档位(5G承载)'),
    'GWFD-110557': ('排除', 'License规格档位(10G基本)'),
    'GWFD-110558': ('排除', 'License规格档位(10G承载)'),
    'GWFD-110559': ('排除', 'License规格档位(20G基本)'),
    'GWFD-110560': ('排除', 'License规格档位(20G承载)'),
    'GWFD-111401': ('排除', 'License规格档位(1G保障)'),
    'GWFD-111402': ('排除', 'License规格档位(2G保障)'),
    # 计费防欺诈功能
    'GWFD-110404': ('纳入', 'HTTPS业务行为识别通过TLS指纹感知HTTPS业务，是SA识别能力的延伸，直接影响计费与策略控制'),
    'GWFD-110402': ('纳入', 'DNS计费防欺诈，通过DNS识别确保计费准确性，与计费场景(NS-01)相关'),
    'GWFD-110403': ('纳入', 'HTTP计费防欺诈，通过HTTP头增强防篡改确保计费准确性'),
    # 超级互联功能
    'GWFD-020501': ('纳入', '跨域业务访问，2C用户访问2B园区，涉及分流策略，与本地分流场景(NS-04)关联'),
    'GWFD-020502': ('排除', '跨域用户漫游，LBO/SHR场景的漫游路由，属于组网特性'),
    'GWFD-020531': ('纳入', '通用DNN漫游分流，通过SMF建立公网+专网双会话实现分流，与本地分流场景(NS-04)直接关联'),
    # 重点业务体验保障功能
    'GWFD-111286': ('纳入', 'VVIP用户体验保障，通过PCF+NWDAF+SMF+UPF闭环，是业务感知高阶场景'),
    'GWFD-111284': ('纳入', '体验信息采集，通过用户面业务感知识别应用级体验信息，是体验保障的数据源'),
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
