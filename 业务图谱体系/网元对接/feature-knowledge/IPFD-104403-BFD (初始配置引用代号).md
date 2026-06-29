# IPFD-104403 BFD (初始配置引用代号)
> EV ID: EV-FK-15 | 引用次数: 3篇初始配置文档

## 本对接场景角色
IPFD-104403为初始配置文档中对BFD特性的引用代号(文档链接实际指向 IPFD-012000 IP可靠性/IPFD-012003 BFD)。仅出现在SDN侧『BGP over静态路由+BFD』三篇(IPv4/IPv4v6/IPv6)，本质=BFD能力在SDN路由方案中的引用。图谱建议以IPFD-012003 BFD为规范节点，本代号作为别名/历史引用证据保留。

## 基础信息
- 特性名: IPFD-104403 (BFD引用代号；规范特性=IPFD-012003 BFD)
- NF支持: 未在features.jsonl登记(引用上下文等同IPFD-012003)
- 类别(feature_category): base / IP基本特性
- 配置相关性(config_relevance): required
- 父特性(parent_feature_code): IPFD-012000 (IP可靠性)

## depends_on（依赖特性）
无显式depends_on记录（基础/目录特性）。

## License
无License控制（feature_requires_license.jsonl中无记录）。

## 关联命令与配置对象
- 关联MML命令: ADD AUTOSCALINGBFD / ADD AUTOSCALINGSRBFD / DSP BFDSESSION (SDN语境)
- 配置对象: SDN BFD(AUTOSCALINGBFD)、SR-BFD(AUTOSCALINGSRBFD)

## 来源证据
- 特性概述: output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-012000 IP可靠性/IPFD-012003 BFD/IPFD-012003 BFD特性概述_61317254.md (规范特性IPFD-012003 BFD概述)
- 初始配置与调测引用文档(3篇):
  - 组网路由配置/配置VNF侧IP路由（SDN）/ (3篇)
