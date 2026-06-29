# GWFD-020411 MPLS VPN
> EV ID: EV-FK-04 | 引用次数: 5篇初始配置文档

## 本对接场景角色
MPLS VPN：UDG作为PE对接CE/DC-GW承载L3VPN，是VNF侧对接PE/DC-GW的BGP+MPLS VPN组网路由方案的核心特性，贯穿SDN/非SDN/网络加速卡三类部署。

## 基础信息
- 特性名: MPLS VPN
- NF支持(nf_support_map): GGSN(2G&3G)=M; S/PGW-U(4G)=M; S/PGW-U(5G NSA)=M; UPF(5G)=M
- 类别(feature_category): base
- 配置相关性(config_relevance): required
- 父特性(parent_feature_code): GWFD-020410
- 目录(catalog_section): 年费基本包-组网演进基本包

## depends_on（依赖特性）
无显式depends_on记录（基础/目录特性）。

## License
- `LKV3G5MPLS01` MPLS VPN

## 关联命令与配置对象
- 关联MML命令: ADD BGPPEER / ADD BGPVRF / ADD BGPVRFAF / ADD MPLSIF / ADD VPNTARGET / ADD L3VPNINST / ADD VPNINSTAF / SET MPLSSITE
- 配置对象: L3VPN实例(L3VPNINST/VPNINSTAF)、RT(VPNTARGET)、MPLS接口(MPLSIF)、BGP VRF

## 来源证据
- 特性概述: output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN_45030708.md
- 初始配置与调测引用文档(5篇):
  - 组网路由配置/配置VNF侧IP路由数据（NP卡直连PE）/ (1篇)
  - 组网路由配置/配置VNF侧IP路由数据（无NP卡_非SDN）/ (2篇)
  - 组网路由配置/配置VNF侧IP路由数据（网络加速卡直连DC-GW）/ (1篇)
  - 组网路由配置/配置VNF侧IP路由（SDN）/ (1篇)
