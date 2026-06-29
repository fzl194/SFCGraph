# NPFD-010014 支持NTP功能
> EV ID: EV-FK-17 | 引用次数: 1篇初始配置文档

## 本对接场景角色
支持NTP功能：UDG从OMC/FusionStage双路同步时间，保障对接信令(证书/Timestamp)与日志时间一致性，是『基础数据配置-配置NTP时间同步』的必备项。

## 基础信息
- 特性名: 支持NTP功能
- NF支持(nf_support_map): GGSN(2G&3G)=M; S/PGW-U(4G)=M; S/PGW-U(5G NSA)=M; UPF(5G)=M; NB-IoT=M
- 类别(feature_category): operations
- 配置相关性(config_relevance): ops_only
- 父特性(parent_feature_code): NPFD-010000
- 目录(catalog_section): 网管特性

## depends_on（依赖特性）
无显式depends_on记录（基础/目录特性）。

## License
无License控制（feature_requires_license.jsonl中无记录）。

## 关联命令与配置对象
- 关联MML命令: (NTP激活与同步配置，详见『激活支持NTP功能』特性指南)
- 配置对象: NTP同步参数、时间源(OMC/FusionStage双路)

## 来源证据
- 特性概述: (无特性概述文档)
- 初始配置与调测引用文档(1篇):
  - 基础数据配置/配置NTP时间同步_53637513.md/ (1篇)
