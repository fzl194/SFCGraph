# IPFD-014002 支持BGP
> EV ID: EV-FK-12 | 引用次数: 17篇初始配置文档

## 本对接场景角色
支持BGP：AS间动态路由，用于UDG与PE/DC-GW的BGP over OSPF/静态路由、BGP+MPLS VPN等对接方案，承载VPNv4/IPv4/IPv6地址族，引用17篇。

## 基础信息
- 特性名: 支持BGP
- NF支持(nf_support_map): GGSN(2G&3G)=M; S/PGW-U(4G)=M; S/PGW-U(5G NSA)=M; UPF(5G)=M; NB-IoT=M
- 类别(feature_category): base
- 配置相关性(config_relevance): required
- 父特性(parent_feature_code): IPFD-014000
- 目录(catalog_section): IP基本特性

## depends_on（依赖特性）
无显式depends_on记录（基础/目录特性）。

## License
无License控制（feature_requires_license.jsonl中无记录）。

## 关联命令与配置对象
- 关联MML命令: SET BGP / ADD BGPPEER / ADD BGPVRF / ADD BGPVRFAF / ADD BGPPEERAF / ADD IMPORTROUTE
- 配置对象: BGP进程/对等体(BGPPEER)/VRF地址族(BGPVRFAF)

## 来源证据
- 特性概述: output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-014000 路由功能/IPFD-014002 支持BGP/IPFD-014002 支持BGP特性概述_61317186.md
- 初始配置与调测引用文档(17篇):
  - 组网路由配置/配置VNF侧IP路由数据（NP卡直连PE）/ (3篇)
  - 组网路由配置/配置VNF侧IP路由数据（无NP卡_非SDN）/ (6篇)
  - 组网路由配置/配置VNF侧IP路由数据（网络加速卡直连DC-GW）/ (4篇)
  - 组网路由配置/配置VNF侧IP路由（SDN）/ (4篇)
