# IPFD-014001 支持OSPF
> EV ID: EV-FK-11 | 引用次数: 6篇初始配置文档

## 本对接场景角色
支持OSPF：内部网关动态路由(OSPFv2/v3)，用于UDG与PE/DC-GW三层互通的『动态路由OSPF+BFD组网』方案(IPv4/IPv6)，NP卡直连PE与非SDN两种部署均使用。

## 基础信息
- 特性名: 支持OSPF
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
- 关联MML命令: ADD OSPF / ADD OSPFAREA / ADD OSPFNETWORK / ADD OSPFINTERFACE / ADD OSPFIMPORTROUTE / DSP OSPFPEER
- 配置对象: OSPF进程/区域(OSPFAREA)/接口(OSPFINTERFACE)/邻居

## 来源证据
- 特性概述: output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-014000 路由功能/IPFD-014001 支持OSPF/IPFD-014001 支持OSPF特性概述_61317384.md
- 初始配置与调测引用文档(6篇):
  - 组网路由配置/配置VNF侧IP路由数据（NP卡直连PE）/ (2篇)
  - 组网路由配置/配置VNF侧IP路由数据（无NP卡_非SDN）/ (4篇)
