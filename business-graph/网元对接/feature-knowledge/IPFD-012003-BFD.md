# IPFD-012003 BFD
> EV ID: EV-FK-09 | 引用次数: 20篇初始配置文档

## 本对接场景角色
BFD：快速检测链路/IP路由连通故障，几乎贯穿所有VNF侧IP路由组网方案(静态路由+BFD/OSPF+BFD/BGP+BFD)，保障对接PE/DC-GW的路由快速收敛。引用20篇，是可靠性主线。

## 基础信息
- 特性名: BFD
- NF支持(nf_support_map): GGSN(2G&3G)=M; S/PGW-U(4G)=M; S/PGW-U(5G NSA)=M; UPF(5G)=M; NB-IoT=M
- 类别(feature_category): base
- 配置相关性(config_relevance): required
- 父特性(parent_feature_code): IPFD-012000
- 目录(catalog_section): IP基本特性

## depends_on（依赖特性）
无显式depends_on记录（基础/目录特性）。

## License
无License控制（feature_requires_license.jsonl中无记录）。

## 关联命令与配置对象
- 关联MML命令: SET BFD / ADD BFDSESSION / DSP BFDSESSION / ADD AUTOSCALINGBFD(SDN)
- 配置对象: BFD会话(BFDSESSION)、BFD全局(BFD)

## 来源证据
- 特性概述: output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-012000 IP可靠性/IPFD-012003 BFD/IPFD-012003 BFD特性概述_61317254.md
- 初始配置与调测引用文档(20篇):
  - 组网路由配置/配置VNF侧IP路由数据（NP卡直连PE）/ (5篇)
  - 组网路由配置/配置VNF侧IP路由数据（无NP卡_非SDN）/ (10篇)
  - 组网路由配置/配置VNF侧IP路由数据（网络加速卡直连DC-GW）/ (1篇)
  - 组网路由配置/配置VNF侧IP路由（SDN）/ (4篇)
