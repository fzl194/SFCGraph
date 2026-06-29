# GWFD-010234 Single IP
> EV ID: EV-FK-02 | 引用次数: 5篇初始配置文档

## 本对接场景角色
Single IP：UDG融合部署(SGW-U/PGW-U/UPF)时让多类业务逻辑接口(N3/S1-U、S5-P/S8-P/N9a、S5-S/S8-S/N9c、N4等)复用一个IP地址。是N4/Pa/Sc/Sa各类业务接口数据配置的必备前置特性，直接决定接口IP规划与逻辑接口命名。

## 基础信息
- 特性名: Single IP
- NF支持(nf_support_map): GGSN(2G&3G)=M; S/PGW-U(4G)=M; S/PGW-U(5G NSA)=M; UPF(5G)=M; NB-IoT=M
- 类别(feature_category): base
- 配置相关性(config_relevance): none
- 父特性(parent_feature_code): GWFD-010220
- 目录(catalog_section): 2/3/4G/5G业务基本特性

## depends_on（依赖特性）
无显式depends_on记录（基础/目录特性）。

## License
无License控制（feature_requires_license.jsonl中无记录）。

## 关联命令与配置对象
- 关联MML命令: ADD LOGICINF / LST LOGICINF / SET UPINFO / ADD VPNINST
- 配置对象: 逻辑接口(LOGICINF: N4if/Saif/Paif/Scif)、SingleIP地址复用

## 来源证据
- 特性概述: output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/逻辑接口功能/GWFD-010234 Single IP_24082251.md
- 初始配置与调测引用文档(5篇):
  - 了解组网架构/逻辑接口介绍_68634155.md/ (1篇)
  - 组网对接配置/配置业务接口数据/ (4篇)
