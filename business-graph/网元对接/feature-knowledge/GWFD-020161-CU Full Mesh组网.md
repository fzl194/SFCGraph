# GWFD-020161 CU Full Mesh组网
> EV ID: EV-FK-03 | 引用次数: 1篇初始配置文档

## 本对接场景角色
CU Full Mesh组网：C面(SMF/SGW-C/PGW-C)与U面(UPF/SGW-U/PGW-U)在N4/Sx接口全互联，支持多对多解耦对接。是N4接口配置对接SMF时的组网前提，决定C/U面偶联拓扑。

## 基础信息
- 特性名: CU Full Mesh组网
- NF支持(nf_support_map): GGSN(2G&3G)=M; S/PGW-U(4G)=M; S/PGW-U(5G NSA)=M; UPF(5G)=M; NB-IoT=M
- 类别(feature_category): base
- 配置相关性(config_relevance): required
- 父特性(parent_feature_code): GWFD-020160
- 目录(catalog_section): 年费基本包-分布式解决方案基本包

## depends_on（依赖特性）
- `GWFD-010224` N4/Sx接口 PFCP协议

## License
- `LKV3G5CUFM01` CU Full Mesh组网

## 关联命令与配置对象
- 关联MML命令: ADD LOGICINF (N4if) / SET UPINFO / ADD VPNINST
- 配置对象: N4偶联、C/U面对接关系、Full Mesh拓扑

## 来源证据
- 特性概述: output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/分布式网络功能/GWFD-020161 CU Full Mesh组网/GWFD-020161 CU Full Mesh组网特性概述_72866256.md
- 初始配置与调测引用文档(1篇):
  - 组网对接配置/配置业务接口数据/ (1篇)
