# IPFD-015004 IPSec功能
> EV ID: EV-FK-14 | 引用次数: 3篇初始配置文档

## 本对接场景角色
IPSec功能：对UDG与对端(PE/DC-GW/网管)间的IP报文提供加密/完整性/防重放保护，是VNF侧IP路由对接中『配置IPsec』隧道方案的核心特性(NP卡直连PE/非SDN两类部署)。

## 基础信息
- 特性名: IPSec功能
- NF支持(nf_support_map): GGSN(2G&3G)=M; S/PGW-U(4G)=M; S/PGW-U(5G NSA)=M; UPF(5G)=M; NB-IoT=M
- 类别(feature_category): base
- 配置相关性(config_relevance): required
- 父特性(parent_feature_code): IPFD-015000
- 目录(catalog_section): IP基本特性

## depends_on（依赖特性）
无显式depends_on记录（基础/目录特性）。

## License
无License控制（feature_requires_license.jsonl中无记录）。

## 关联命令与配置对象
- 关联MML命令: (IPsec隧道配置命令，详见『配置IPsec』实例)
- 配置对象: IPsec隧道、安全联盟(SA)、安全策略

## 来源证据
- 特性概述: output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/IPFD-015004 IPSec功能特性概述_61317289.md
- 初始配置与调测引用文档(3篇):
  - 组网路由配置/配置VNF侧IP路由数据（NP卡直连PE）/ (1篇)
  - 组网路由配置/配置VNF侧IP路由数据（无NP卡_非SDN）/ (2篇)
