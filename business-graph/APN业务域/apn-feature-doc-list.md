# APN业务域特性文档清单

> 业务域: APN(接入与会话管理)
> 从 `feature-graph/data/UDG_feature_files.csv` 和 `UNC_feature_files.csv` 提取
> 共 37 个特性(配置树11 + T1核心补全26),按6大类组织(APN基础/地址分配/鉴权计费/接入方式/网元选择/接入控制)
> 特性来源: `APN配置树.md`(专家梳理的配置树叶子节点)

## 总览

| # | 特性ID | 特性名称 | 产品 | 类别 | 文件数 | 优先级 | 说明 |
|---|--------|---------|------|------|--------|--------|------|
| 1 | GWFD-010101 | 会话管理 | UDG | APN基础 | 16 | ★核心 | 会话管理基础(UPF侧,PDU会话建立/释放) |
| 2 | WSFD-010501 | 会话管理 | UNC | APN基础 | 8 | ★核心 | 会话管理基础(SMF侧,PDU会话建立/释放) |
| 3 | WSFD-010503 | 多PDN/PDU功能 | UNC | APN基础 | 5 | ★核心 | 支持多PDN/PDU并发会话 |
| 4 | WSFD-010400 | 用户数据管理 | UNC | APN基础 | 7 | ★核心 | 用户签约数据管理(UDM/UDR交互) |
| 5 | WSFD-106203 | 别名APN | UNC | APN基础 | 10 | ★核心 | 别名APN/虚拟APN(APN聚合与重定向) |
| 6 | GWFD-010105 | 用户面地址分配 | UDG | 地址分配 | 10 | ★核心 | UPF分配:基于APN/DNN、基于SMF |
| 7 | GWFD-010104 | 地址分配方式 | UDG | 地址分配 | 6 | ★核心 | 用户面地址分配方式总览(配置树补全) |
| 8 | GWFD-020421 | 基于位置的地址分配 | UDG | 地址分配 | 5 | ★核心 | UPF分配:基于位置区(需License LKV3G5LBAA01) |
| 9 | GWFD-010108 | 用户面地址自动检测 | UDG | 地址分配 | 5 | 辅助 | UPF地址探测可靠性(PING/DNS/Tracert) |
| 10 | GWFD-010107 | 静态地址用户路由冗余 | UDG | 地址分配 | 9 | 辅助 | 静态地址用户路由冗余保护 |
| 11 | GWFD-020412 | L2TP VPN | UDG | 地址分配 | 15 | ★核心 | LNS分配(UPF侧,L2TP隧道PPP协商) |
| 12 | WSFD-010502 | 地址分配方式 | UNC | 地址分配 | 5 | ★核心 | SMF分配/UDM静态/Radius/DHCP分配 |
| 13 | WSFD-010504 | 控制面地址分配方式 | UNC | 地址分配 | 2 | ★核心 | 控制面地址分配方式(SMF侧) |
| 14 | WSFD-104410 | L2TP VPN | UNC | 地址分配 | 5 | ★核心 | LNS分配(SMF侧,L2TP隧道PPP协商) |
| 15 | WSFD-107021 | 静态地址用户路由冗余 | UNC | 地址分配 | 5 | 辅助 | 静态地址用户路由冗余保护(SMF侧) |
| 16 | GWFD-020403 | IPv4v6双栈接入 | UDG | 地址分配 | 5 | ★核心 | IPv4v6双栈接入(配置树遗漏补全)★ |
| 17 | WSFD-104002 | IPv4v6双栈接入 | UNC | 地址分配 | 12 | ★核心 | IPv4v6双栈接入(SMF侧)★ |
| 18 | GWFD-020401 | IPv6承载上下文 | UDG | 地址分配 | 5 | ★核心 | IPv6承载上下文管理 |
| 19 | WSFD-104001 | IPv6承载上下文 | UNC | 地址分配 | 16 | ★核心 | IPv6承载上下文管理(SMF侧) |
| 20 | GWFD-020406 | IPv6 Prefix Delegation | UDG | 地址分配 | 12 | ★核心 | IPv6前缀代理(PD) |
| 21 | WSFD-104004 | IPv6前缀代理 | UNC | 地址分配 | 8 | ★核心 | IPv6前缀代理(SMF侧) |
| 22 | WSFD-104413 | DHCP功能 | UNC | 地址分配 | 2 | ★核心 | DHCPv4地址分配(SMF作DHCP Client) |
| 23 | WSFD-104005 | DHCPv6地址分配 | UNC | 地址分配 | 2 | ★核心 | DHCPv6地址分配 |
| 24 | WSFD-011305 | Radius鉴权接入 | UNC | 鉴权计费 | 9 | ★核心 | AUTHMODE鉴权方式(透明/透明鉴权/不透明/本地) |
| 25 | WSFD-011306 | Radius功能 | UNC | 鉴权计费 | 12 | ★核心 | Radius服务器配置(透明鉴权/不透明接入时必配) |
| 26 | WSFD-010301 | 鉴权功能 | UNC | 鉴权计费 | 16 | ★核心 | 基础鉴权功能(配置树补全) |
| 27 | WSFD-108007 | 终端二次鉴权 | UNC | 鉴权计费 | 4 | 辅助 | 终端二次鉴权(企业AAA场景) |
| 28 | WSFD-011307 | Radius抄送功能 | UNC | 鉴权计费 | 5 | 辅助 | Radius计费抄送 |
| 29 | IPFD-015002 | GRE | UDG+UNC | 接入方式 | 8 | ★核心 | GRE隧道(SMF+UPF,轻量封装不加密,最多两层嵌套) |
| 30 | IPFD-015004 | IPSec功能 | UDG | 接入方式 | 24 | ★核心 | IPSec隧道(UPF侧,加密+认证) |
| 31 | IPFD-016000 | IPSec功能 | UNC | 接入方式 | 24 | ★核心 | IPSec隧道(SMF侧,加密+认证) |
| 32 | GWFD-020411 | MPLS VPN | UDG | 接入方式 | 9 | ★核心 | MPLS VPN隧道(配置树补全) |
| 33 | WSFD-104411 | MPLS VPN | UNC | 接入方式 | 9 | ★核心 | MPLS VPN隧道(SMF侧) |
| 34 | WSFD-107010 | UPF选择 | UNC | 网元选择 | 1 | ★核心 | SMF为PDU会话选择UPF★ |
| 35 | WSFD-010202 | 基于位置区域对等网元选择 | UNC | 网元选择 | 5 | 辅助 | 基于位置区域的对等网元选择 |
| 36 | WSFD-106003 | 用户接入控制功能 | UNC | 接入控制 | 14 | ★核心 | 用户接入控制(APN接入权限) |
| 37 | GWFD-010151 | 接入控制 | UDG | 接入控制 | 3 | ★核心 | 接入控制(UPF侧) |
| | | **合计** | | | **318** | | |

---

## APN基础特性

### Batch-01: GWFD-010101 会话管理 (UDG/UPF, 16 files) [★核心]

> 会话管理基础(UPF侧,PDU会话建立/释放)

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/2_3G会话管理/GWFD-010101 会话管理（2_3G）特性概述_61678540.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/2_3G会话管理/实现原理/UE_SGSN发起PDP上下文修改流程_61678544.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/2_3G会话管理/实现原理/UE_SGSN发起PDP上下文删除流程_61900183.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/2_3G会话管理/实现原理/UE发起一次PDP上下文激活流程_61678542.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/2_3G会话管理/实现原理/UE发起二次PDP上下文激活流程_61678543.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/4G会话管理/GWFD-010101 会话管理（4G）特性概述_68633827.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/5G会话管理/GWFD-010101 会话管理（5G）特性概述_73618343.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/5G会话管理/实现原理/PDU会话修改（AN发起）_72654737.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/5G会话管理/实现原理/PDU会话修改（PCF发起）_22895266.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/5G会话管理/实现原理/PDU会话修改（UDM发起）_22735962.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/5G会话管理/实现原理/PDU会话修改（UE发起）_22578338.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/5G会话管理/实现原理/PDU会话建立_22418374.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/5G会话管理/实现原理/PDU会话释放（AMF发起）_72735009.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/5G会话管理/实现原理/PDU会话释放（PCF发起）_72934785.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/5G会话管理/实现原理/PDU会话释放（SMF发起）_22418378.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/5G会话管理/实现原理/PDU会话释放（UE发起）_72815297.md
```

---

### Batch-02: WSFD-010501 会话管理 (UNC/SMF, 8 files) [★核心]

> 会话管理基础(SMF侧,PDU会话建立/释放)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010501 会话管理/会话管理（2G&3G）/WSFD-010501 会话管理参考信息_85436072.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010501 会话管理/会话管理（2G&3G）/WSFD-010501 会话管理特性概述（适用于2G&3G）_85436070.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010501 会话管理/会话管理（2G&3G）/实现原理_85436071.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010501 会话管理/会话管理（4G）/WSFD-010501 会话管理特性概述（适用于4G）_73595351.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010501 会话管理/会话管理（4G）/实现原理/APN选择_75597698.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010501 会话管理/会话管理（4G）/实现原理_73595858.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010501 会话管理/会话管理（5G）/WSFD-010501 会话管理特性概述（适用于5G）_48483833.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010501 会话管理/会话管理（5G）/会话管理基本概念_78831488.md
```

---

### Batch-03: WSFD-010503 多PDN/PDU功能 (UNC/SMF, 5 files) [★核心]

> 支持多PDN/PDU并发会话

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010503 支持多PDN_PDU功能/WSFD-010503 支持多PDN_PDU功能参考信息_70362993.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010503 支持多PDN_PDU功能/WSFD-010503 支持多PDN_PDU功能特性概述_63778196.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010503 支持多PDN_PDU功能/激活支持多PDN功能（适用于4G）_66843676.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010503 支持多PDN_PDU功能/调测支持多PDN功能（适用于4G）_70780933.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010503 支持多PDN_PDU功能_63776303.md
```

---

### Batch-04: WSFD-010400 用户数据管理 (UNC/SMF, 7 files) [★核心]

> 用户签约数据管理(UDM/UDR交互)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010400 用户数据管理/WSFD-010400 用户数据管理（2G&3G）/WSFD-010400 用户数据管理（适用于2G&3G）参考信息_85436069.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010400 用户数据管理/WSFD-010400 用户数据管理（2G&3G）/实现原理（适用于2G&3G）_85436068.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010400 用户数据管理/WSFD-010400 用户数据管理（2G&3G）/特性概述_85436067.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010400 用户数据管理/WSFD-010400 用户数据管理（4G）/WSFD-010400 用户数据管理（适用于4G）参考信息_18103951.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010400 用户数据管理/WSFD-010400 用户数据管理（4G）/实现原理（适用于4G）_70018152.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010400 用户数据管理/WSFD-010400 用户数据管理（4G）/特性概述_70018151.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010400 用户数据管理/WSFD-010400 用户数据管理（5G）_60374923.md
```

---

### Batch-05: WSFD-106203 别名APN (UNC/SMF, 10 files) [★核心]

> 别名APN/虚拟APN(APN聚合与重定向)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-106203 别名APN/别名APN（适用于GGSN_PGW-C_SMF）/WSFD-106203 别名APN参考信息（适用于GGSN_PGW-C_SMF）_34797882.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-106203 别名APN/别名APN（适用于GGSN_PGW-C_SMF）/WSFD-106203 别名APN特性概述（适应于GGSN_PGW-C_SMF）_34797879.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-106203 别名APN/别名APN（适用于GGSN_PGW-C_SMF）/激活别名APN_34797880.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-106203 别名APN/别名APN（适用于GGSN_PGW-C_SMF）/调测别名APN_34797881.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-106203 别名APN/别名APN（适用于SGSN_MME）/WSFD-106203 别名APN参考信息（适用于SGSN_MME）_68358229.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-106203 别名APN/别名APN（适用于SGSN_MME）/WSFD-106203 别名APN特性概述（适用于SGSN_MME）_68358224.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-106203 别名APN/别名APN（适用于SGSN_MME）/实现原理_68358226.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-106203 别名APN/别名APN（适用于SGSN_MME）/激活别名APN_68358227.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-106203 别名APN/别名APN（适用于SGSN_MME）/调测别名APN_68358228.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-106203 别名APN_64082528.md
```

---

## 地址分配特性

### Batch-06: GWFD-010105 用户面地址分配 (UDG/UPF, 10 files) [★核心]

> UPF分配:基于APN/DNN、基于SMF

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010105 用户面地址分配/GWFD-010105 用户面地址分配参考信息_77284218.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010105 用户面地址分配/GWFD-010105 用户面地址分配特性概述_68664421.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010105 用户面地址分配/实现原理/其他增值功能_87787968.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010105 用户面地址分配/实现原理/地址分配方式_87787955.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010105 用户面地址分配/实现原理/地址分配流程_74936046.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010105 用户面地址分配/激活用户面地址分配/基于APN_DNN分配地址_72547232.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010105 用户面地址分配/激活用户面地址分配/基于RADIUS下发地址池名称分配地址_13796101.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010105 用户面地址分配/激活用户面地址分配/基于SMF+APN_DNN分配地址_87787640.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010105 用户面地址分配/激活用户面地址分配/基于SMF分配地址_87605805.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010105 用户面地址分配/调测用户面地址分配_72547233.md
```

---

### Batch-07: GWFD-010104 地址分配方式 (UDG/UPF, 6 files) [★核心]

> 用户面地址分配方式总览(配置树补全)

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010104 地址分配方式/GWFD-010104 地址分配方式参考信息_77074325.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010104 地址分配方式/GWFD-010104 地址分配方式特性概述_67531788.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010104 地址分配方式/实现原理/地址分配流程_73558472.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010104 地址分配方式/实现原理/用户下行路由生成与发布_96489749.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010104 地址分配方式/激活地址分配方式_71653959.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010104 地址分配方式/调测地址分配方式_71653960.md
```

---

### Batch-08: GWFD-020421 基于位置的地址分配 (UDG/UPF, 5 files) [★核心]

> UPF分配:基于位置区(需License LKV3G5LBAA01)

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-020421 基于位置的地址分配/GWFD-020421 基于位置的地址分配参考信息_02846778.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-020421 基于位置的地址分配/GWFD-020421 基于位置的地址分配特性概述_02846766.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-020421 基于位置的地址分配/激活基于位置的地址分配/基于APN_DNN+位置分配地址_02846776.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-020421 基于位置的地址分配/激活基于位置的地址分配/基于位置分配地址_02846773.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-020421 基于位置的地址分配/调测基于位置的地址分配_02846777.md
```

---

### Batch-09: GWFD-010108 用户面地址自动检测 (UDG/UPF, 5 files) [辅助]

> UPF地址探测可靠性(PING/DNS/Tracert)

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010108 用户面地址自动检测/GWFD-010108 用户面地址自动检测参考信息_04636932.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010108 用户面地址自动检测/GWFD-010108 用户面地址自动检测特性概述_04636902.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010108 用户面地址自动检测/激活用户面地址自动检测_04636908.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010108 用户面地址自动检测/调测用户面地址自动检测_04636931.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010108 用户面地址自动检测_04636901.md
```

---

### Batch-10: GWFD-010107 静态地址用户路由冗余 (UDG/UPF, 9 files) [辅助]

> 静态地址用户路由冗余保护

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010107 静态地址用户路由冗余/GWFD-010107 静态地址用户路由冗余参考信息_19612406.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010107 静态地址用户路由冗余/GWFD-010107 静态地址用户路由冗余特性概述_19612410.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010107 静态地址用户路由冗余/实现原理/主用PGW-U_UPF故障场景_19644452.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010107 静态地址用户路由冗余/实现原理/主用PGW-U_UPF故障恢复场景_19644453.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010107 静态地址用户路由冗余/实现原理/主用PGW-U_UPF正常场景_19644451.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010107 静态地址用户路由冗余/实现原理/静态地址路由冗余叠加UE互访场景_12681278.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010107 静态地址用户路由冗余/激活静态地址用户路由冗余_19612403.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010107 静态地址用户路由冗余/调测静态地址用户路由冗余_19612411.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010107 静态地址用户路由冗余_19612408.md
```

---

### Batch-11: GWFD-020412 L2TP VPN (UDG/UPF, 15 files) [★核心]

> LNS分配(UPF侧,L2TP隧道PPP协商)

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/GWFD-020412 L2TP VPN参考信息_40342151.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/GWFD-020412 L2TP VPN特性概述_40342127.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/实现原理/L2TP去激活流程_19990151.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/实现原理/L2TP查表流程_19990150.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/实现原理/L2TP激活流程_76399675.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/实现原理/L2TP隧道维护流程_32553703.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/激活L2TP VPN/AAA下发L2TP属性方式激活L2TP VPN_41487855.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/激活L2TP VPN/本地配置方式激活L2TP VPN_40342129.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/相关术语/L2TP_51067102.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/相关术语/LAC_51067103.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/相关术语/LNS_51067104.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/相关术语/PPP协议_51525531.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/调测L2TP VPN/调测基于AAA下发L2TP属性方式激活的L2TP VPN_41487857.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/调测L2TP VPN/调测基于本地配置方式激活的L2TP VPN_40342150.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN_40342126.md
```

---

### Batch-12: WSFD-010502 地址分配方式 (UNC/SMF, 5 files) [★核心]

> SMF分配/UDM静态/Radius/DHCP分配

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010502 地址分配方式/WSFD-010502 地址分配方式参考信息_72291445.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010502 地址分配方式/WSFD-010502 地址分配方式特性概述_64915075.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010502 地址分配方式/调测静态地址分配IPv4地址功能_67401513.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010502 地址分配方式/配置静态IP地址网段与UPF的绑定_67401512.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010502 地址分配方式/配置静态地址黑名单_48452479.md
```

---

### Batch-13: WSFD-010504 控制面地址分配方式 (UNC/SMF, 2 files) [★核心]

> 控制面地址分配方式(SMF侧)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010504 控制面地址分配方式/WSFD-010504 控制面地址分配方式参考信息_77813716.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-010504 控制面地址分配方式/特性概述_77654144.md
```

---

### Batch-14: WSFD-104410 L2TP VPN (UNC/SMF, 5 files) [★核心]

> LNS分配(SMF侧,L2TP隧道PPP协商)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104410 L2TP VPN/WSFD-104410 L2TP VPN参考信息_46559217.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104410 L2TP VPN/激活L2TP VPN_46559215.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104410 L2TP VPN/特性概述_46559213.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104410 L2TP VPN/调测L2TP VPN_46559216.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104410 L2TP VPN_46534504.md
```

---

### Batch-15: WSFD-107021 静态地址用户路由冗余 (UNC/SMF, 5 files) [辅助]

> 静态地址用户路由冗余保护(SMF侧)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/分布式网络功能/WSFD-107021 静态地址用户路由冗余/WSFD-107021 静态地址用户路由冗余参考信息_76652609.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/分布式网络功能/WSFD-107021 静态地址用户路由冗余/WSFD-107021 静态地址用户路由冗余特性概述_76652606.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/分布式网络功能/WSFD-107021 静态地址用户路由冗余/激活静态地址用户路由冗余_76652607.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/分布式网络功能/WSFD-107021 静态地址用户路由冗余/调测静态地址用户路由冗余_76652608.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/分布式网络功能/WSFD-107021 静态地址用户路由冗余_76652605.md
```

---

### Batch-16: GWFD-020403 IPv4v6双栈接入 (UDG/UPF, 5 files) [★核心]

> IPv4v6双栈接入(配置树遗漏补全)★

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020403 IPv4v6双栈接入/GWFD-020403 IPv4v6双栈接入参考信息_77078875.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020403 IPv4v6双栈接入/GWFD-020403 IPv4v6双栈接入特性概述_38276179.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020403 IPv4v6双栈接入/激活IPv4v6双栈接入_38276180.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020403 IPv4v6双栈接入/调测IPv4v6双栈接入_38276241.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020403 IPv4v6双栈接入_67108868.md
```

---

### Batch-17: WSFD-104002 IPv4v6双栈接入 (UNC/SMF, 12 files) [★核心]

> IPv4v6双栈接入(SMF侧)★

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104002 IPv4v6双栈接入/IPv4v6双栈接入（2G_3G_4G）/WSFD-104002 IPv4v6双栈接入（2G_3G_4G）参考信息_48043378.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104002 IPv4v6双栈接入/IPv4v6双栈接入（2G_3G_4G）/激活IPv4v6双栈接入特性（适用于PGW-C）_48043380.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104002 IPv4v6双栈接入/IPv4v6双栈接入（2G_3G_4G）/激活IPv4v6双栈接入特性（适用于SGSN_MME）_48043379.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104002 IPv4v6双栈接入/IPv4v6双栈接入（2G_3G_4G）/特性概述_48043389.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104002 IPv4v6双栈接入/IPv4v6双栈接入（2G_3G_4G）/调测IPv4v6双栈接入特性（适用于SGSN_MME）_48043346.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104002 IPv4v6双栈接入/IPv4v6双栈接入（2G_3G_4G）/调测支持静态IPv4v6双栈地址功能（适用于PGW-C）_48043387.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104002 IPv4v6双栈接入/IPv4v6双栈接入（2G_3G_4G）_48043356.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104002 IPv4v6双栈接入/IPv4v6双栈接入（5G）/WSFD-104002 IPv4v6双栈接入（5G）参考信息_48043365.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104002 IPv4v6双栈接入/IPv4v6双栈接入（5G）/激活IPv4v6双栈接入特性_48043372.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104002 IPv4v6双栈接入/IPv4v6双栈接入（5G）/特性概述_48043373.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104002 IPv4v6双栈接入/IPv4v6双栈接入（5G）/调测IPv4v6双栈接入特性_48043390.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104002 IPv4v6双栈接入_48043345.md
```

---

### Batch-18: GWFD-020401 IPv6承载上下文 (UDG/UPF, 5 files) [★核心]

> IPv6承载上下文管理

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020401 IPv6承载上下文/GWFD-020401 IPv6承载上下文参考信息_77077508.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020401 IPv6承载上下文/GWFD-020401 IPv6承载上下文特性概述_38276175.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020401 IPv6承载上下文/激活IPv6承载上下文_38276176.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020401 IPv6承载上下文/调测IPv6承载上下文_38276177.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020401 IPv6承载上下文_67107266.md
```

---

### Batch-19: WSFD-104001 IPv6承载上下文 (UNC/SMF, 16 files) [★核心]

> IPv6承载上下文管理(SMF侧)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文/WSFD-104001 IPv6承载上下文（AMF_SMF）/WSFD-104001 IPv6承载上下文（AMF_SMF）参考信息_48043348.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文/WSFD-104001 IPv6承载上下文（AMF_SMF）/激活IPv6承载上下文特性（AMF_SMF）_48043375.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文/WSFD-104001 IPv6承载上下文（AMF_SMF）/特性概述_48043368.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文/WSFD-104001 IPv6承载上下文（AMF_SMF）/调测IPv6承载上下文特性（AMF_SMF）_48043361.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文/WSFD-104001 IPv6承载上下文（AMF_SMF）_48043357.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文/WSFD-104001 IPv6承载上下文（MME、SGW-C_PGW-C）/WSFD-104001 IPv6承载上下文（MME、SGW-C_PGW-C）参考信息_48043353.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文/WSFD-104001 IPv6承载上下文（MME、SGW-C_PGW-C）/激活IPv6承载上下文特性（适用于MME、SGW-C_PGW-C）_48043351.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文/WSFD-104001 IPv6承载上下文（MME、SGW-C_PGW-C）/特性概述_48043369.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文/WSFD-104001 IPv6承载上下文（MME、SGW-C_PGW-C）/调测IPv6承载上下文特性（适用于MME、SGW-C_PGW-C）_48043381.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文/WSFD-104001 IPv6承载上下文（MME、SGW-C_PGW-C）_48043391.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文/WSFD-104001 IPv6承载上下文（SGSN_GGSN）/WSFD-104001 IPv6承载上下文（SGSN_GGSN）参考信息_48043377.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文/WSFD-104001 IPv6承载上下文（SGSN_GGSN）/激活IPv6承载上下文特性（SGSN_GGSN）_48043366.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文/WSFD-104001 IPv6承载上下文（SGSN_GGSN）/特性概述_48043355.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文/WSFD-104001 IPv6承载上下文（SGSN_GGSN）/调测IPv6承载上下文特性（SGSN_GGSN）_48043374.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文/WSFD-104001 IPv6承载上下文（SGSN_GGSN）_48043384.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IPv6功能/WSFD-104001 IPv6承载上下文_48043347.md
```

---

### Batch-20: GWFD-020406 IPv6 Prefix Delegation (UDG/UPF, 12 files) [★核心]

> IPv6前缀代理(PD)

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation/GWFD-020406 IPv6 Prefix Delegation参考信息_79370035.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation/GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation/实现原理/5GC业务流程_79707829.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation/实现原理/EPC业务流程_79707828.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation/实现原理/GPRS_UMTS业务流程_79707827.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation/激活外部网元地址分配的IPv6 Prefix Delegation功能_80269177.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation/激活本地地址池分配的IPv6 Prefix Delegation功能/基于APN_DNN分配地址_80250128.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation/激活本地地址池分配的IPv6 Prefix Delegation功能/基于SMF+APN_DNN分配地址_80250130.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation/激活本地地址池分配的IPv6 Prefix Delegation功能/基于SMF分配地址_80250129.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation/激活本地地址池分配的IPv6 Prefix Delegation功能/基于位置分配地址_52579205.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation/调测IPv6 Prefix Delegation_79370030.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation_79370033.md
```

---

### Batch-21: WSFD-104004 IPv6前缀代理 (UNC/SMF, 8 files) [★核心]

> IPv6前缀代理(SMF侧)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104004 IPv6前缀代理/WSFD-104004 IPv6前缀代理参考信息_76459529.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104004 IPv6前缀代理/实现原理/5GC业务流程_59334341.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104004 IPv6前缀代理/实现原理/EPC业务流程_59374325.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104004 IPv6前缀代理/实现原理/GPRS_UMTS业务流程_14374504.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104004 IPv6前缀代理/激活IPv6前缀代理_76459527.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104004 IPv6前缀代理/特性概述_76459525.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104004 IPv6前缀代理/调测IPv6 前缀代理_76459528.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104004 IPv6前缀代理_76459504.md
```

---

### Batch-22: WSFD-104413 DHCP功能 (UNC/SMF, 2 files) [★核心]

> DHCPv4地址分配(SMF作DHCP Client)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-104413 DHCP功能/WSFD-104413 DHCP功能参考信息_61065989.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-104413 DHCP功能/特性概述_60866061.md
```

---

### Batch-23: WSFD-104005 DHCPv6地址分配 (UNC/SMF, 2 files) [★核心]

> DHCPv6地址分配

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-104005 DHCPv6地址分配/WSFD-104005 DHCPv6地址分配参考信息_61255173.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-104005 DHCPv6地址分配/特性概述_61335231.md
```

---

## 鉴权计费特性

### Batch-24: WSFD-011305 Radius鉴权接入 (UNC/SMF, 9 files) [★核心]

> AUTHMODE鉴权方式(透明/透明鉴权/不透明/本地)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/WSFD-011305 Radius鉴权接入参考信息_50176281.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/激活Radius鉴权接入_50176279.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/特性概述_50176278.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/调测Radius鉴权接入/调测本地鉴权接入_95351133.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/调测Radius鉴权接入/调测透明接入_95351130.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/调测Radius鉴权接入/调测透明鉴权接入_95351132.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/调测Radius鉴权接入/调测非透明接入_95351131.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/调测Radius鉴权接入_50176280.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入_50176277.md
```

---

### Batch-25: WSFD-011306 Radius功能 (UNC/SMF, 12 files) [★核心]

> Radius服务器配置(透明鉴权/不透明接入时必配)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/WSFD-011306 Radius功能参考信息_15542176.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/实现原理_31922672.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/激活RADIUS功能/配置RADIUS功能_32909765.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/激活RADIUS功能/配置业务触发RADIUS功能_33000859.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/激活RADIUS功能/配置到AAA Server的数据（单平面+静态路由+BFD组网）_32044985.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/激活RADIUS功能/配置到AAA Server的数据（双平面+OSPF动态路由+BFD组网 ）_31879931.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/激活RADIUS功能/配置到AAA Server的数据（带内组网GRE VPN）_32723577.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/激活RADIUS功能/配置到AAA Server的数据（带外组网GRE VPN）_32050904.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/特性概述_31467848.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/调测业务触发RADIUS功能_32050952.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/调测到AAA Server的数据_32027181.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能_14755851.md
```

---

### Batch-26: WSFD-010301 鉴权功能 (UNC/SMF, 16 files) [★核心]

> 基础鉴权功能(配置树补全)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（2G&3G）/WSFD-010301 鉴权功能（适用于2G&3G）参考信息_85223132.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（2G&3G）/实现原理（适用于2G&3G）_92631697.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（2G&3G）/激活鉴权功能（适用于2G&3G）_82934116.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（2G&3G）/特性概述_85223131.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（2G&3G）/调测鉴权功能（适用于2G&3G）_85369571.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（4G）/WSFD-010301 鉴权功能（适用于4G）参考信息_70014631.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（4G）/实现原理（适用于4G）_70014630.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（4G）/激活鉴权功能（适用于4G）_62847962.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（4G）/特性概述_70014629.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（4G）/调测鉴权功能特性（适用于4G）_72665523.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（5G）/WSFD-010301 鉴权功能（适用于5G）参考信息_66260391.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（5G）/实现原理（适用于5G）_66260580.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（5G）/激活鉴权功能（适用于5G）_66260458.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（5G）/特性概述_60375189.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（5G）/鉴权流程（适用于5G）/5G AKA鉴权_80005829.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/安全管理功能/WSFD-010301 鉴权功能/鉴权功能（5G）/鉴权流程（适用于5G）/EAP AKA'鉴权_79926121.md
```

---

### Batch-27: WSFD-108007 终端二次鉴权 (UNC/SMF, 4 files) [辅助]

> 终端二次鉴权(企业AAA场景)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-108007 终端二次鉴权/WSFD-108007 终端二次鉴权参考信息_24463433.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-108007 终端二次鉴权/WSFD-108007 终端二次鉴权特性概述_73984008.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-108007 终端二次鉴权/激活终端二次鉴权_24743509.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-108007 终端二次鉴权/调测终端二次鉴权_74143640.md
```

---

### Batch-28: WSFD-011307 Radius抄送功能 (UNC/SMF, 5 files) [辅助]

> Radius计费抄送

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011307 支持Radius抄送功能/WSFD-011307 支持Radius抄送功能参考信息_33769359.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011307 支持Radius抄送功能/实现原理_33761637.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011307 支持Radius抄送功能/激活支持RADIUS抄送功能_33769357.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011307 支持Radius抄送功能/特性概述_33741340.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011307 支持Radius抄送功能/调测支持RADIUS抄送功能_33769358.md
```

---

## 接入方式特性

### Batch-29: IPFD-015002 GRE (UDG+UNC/UPF/SMF, 8 files) [★核心]

> GRE隧道(SMF+UPF,轻量封装不加密,最多两层嵌套)

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015000 VPN功能/IPFD-015002 GRE/特性配置/调测GRE_06422611.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-015002 GRE/IPFD-015002 GRE特性概述_61317365.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-015002 GRE/实现原理/GRE报文格式_61317188.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-015002 GRE/实现原理/Keepalive检测_61317267.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-015002 GRE/实现原理/多租户共享GRE隧道_61317217.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-015002 GRE/特性配置/去激活支持GRE_06422612.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-015002 GRE/特性配置/激活支持GRE_06422610.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-015002 GRE/特性配置/调测GRE_84704881.md
```

---

### Batch-30: IPFD-015004 IPSec功能 (UDG/UPF, 24 files) [★核心]

> IPSec隧道(UPF侧,加密+认证)

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/IPFD-015004 IPSec功能特性概述_61317289.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/实现原理/AH和ESP_62244157.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/实现原理/IKE_62256396.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/实现原理/IPsec NAT穿越_62244160.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/实现原理/IPsec可靠性_78460643.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/实现原理/安全联盟（SA）_62244156.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/实现原理/报文封装模式_62256279.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/特性配置/上传IPsec证书_01_10001.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/特性配置/上传国密IPsec证书_53966806.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/特性配置/激活IPsec功能（GRE over IPsec）_01_10006.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/特性配置/激活IPsec功能（IPv4 IPsec主备隧道）_01_10004.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/特性配置/激活IPsec功能（IPv6 IPsec隧道主备方式）_01_10005.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/特性配置/激活IPsec功能（OSPF over IPsec）_01_10007.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/特性配置/激活IPsec功能（多Sequence的IPsec策略）_01_10008.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/特性配置/激活IPsec功能（指定本端接口建立IPsec隧道）_01_10009.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/特性配置/激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/特性配置/激活IPsec功能（普通IPv6 IPsec隧道）_01_10003.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/特性配置/激活国密IPsec支持IKEv1功能（GRE over IPsec）_53928160.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/特性配置/激活国密IPsec支持IKEv1功能（多Sequence的IPsec策略）_03408185.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/特性配置/激活国密IPsec支持IKEv1功能（指定本端接口建立IPsec隧道）_03567841.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/特性配置/激活国密IPsec支持IKEv1功能（普通IPv4 IPsec隧道）_03728909.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/特性配置/激活国密IPsec支持IKEv1功能（普通IPv6 IPsec隧道）_53768408.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/相关术语_88277392.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/调测IPsec功能_61317192.md
```

---

### Batch-31: IPFD-016000 IPSec功能 (UNC/SMF, 24 files) [★核心]

> IPSec隧道(SMF侧,加密+认证)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/IPFD-016000 IPSec功能特性概述_61317289.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/实现原理/AH和ESP_62244157.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/实现原理/IKE_62256396.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/实现原理/IPsec NAT穿越_62244160.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/实现原理/IPsec可靠性_78460643.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/实现原理/安全联盟（SA）_62244156.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/实现原理/报文封装模式_62256279.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/特性配置/上传IPsec证书_83878778.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/特性配置/上传国密IPsec证书_53966806.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/特性配置/激活IPsec功能（GRE over IPsec）_78985535.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/特性配置/激活IPsec功能（IPv4 IPsec主备隧道）_88744738.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/特性配置/激活IPsec功能（IPv6 IPsec隧道主备方式）_53998700.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/特性配置/激活IPsec功能（OSPF over IPsec）_90949389.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/特性配置/激活IPsec功能（多Sequence的IPsec策略）_78985536.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/特性配置/激活IPsec功能（指定本端接口建立IPsec隧道）_78985537.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/特性配置/激活IPsec功能（普通IPv4 IPsec隧道）_61317238.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/特性配置/激活IPsec功能（普通IPv6 IPsec隧道）_78985538.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/特性配置/激活国密IPsec支持IKEv1功能（GRE over IPsec）_53928160.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/特性配置/激活国密IPsec支持IKEv1功能（多Sequence的IPsec策略）_03408185.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/特性配置/激活国密IPsec支持IKEv1功能（指定本端接口建立IPsec隧道）_03567841.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/特性配置/激活国密IPsec支持IKEv1功能（普通IPv4 IPsec隧道）_03728909.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/特性配置/激活国密IPsec支持IKEv1功能（普通IPv6 IPsec隧道）_53768408.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/相关术语_88277392.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-016000 IPSec功能/调测IPsec功能_61317192.md
```

---

### Batch-32: GWFD-020411 MPLS VPN (UDG/UPF, 9 files) [★核心]

> MPLS VPN隧道(配置树补全)

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/BGP_MPLS IPv6 VPN_45030732.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/Hub&Spoke_92069589.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/MPLS VPN的分标签方式_92189833.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/Multi-VPN-Instance CE_45189888.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/VPN GR_92069593.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/VPN NSR_45189892.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/基本概念_92189817.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/跨域VPN_45030728.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN_45030708.md
```

---

### Batch-33: WSFD-104411 MPLS VPN (UNC/SMF, 9 files) [★核心]

> MPLS VPN隧道(SMF侧)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104411 MPLS VPN/BGP_MPLS IPv6 VPN_45033532.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104411 MPLS VPN/Hub&Spoke_45192696.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104411 MPLS VPN/MPLS VPN的分标签方式_92192637.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104411 MPLS VPN/Multi-VPN-Instance CE_92072389.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104411 MPLS VPN/VPN GR_45192700.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104411 MPLS VPN/VPN NSR_92072393.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104411 MPLS VPN/基本概念_92192633.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104411 MPLS VPN/跨域VPN_45033528.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104411 MPLS VPN_45033524.md
```

---

## 网元选择特性

### Batch-34: WSFD-107010 UPF选择 (UNC/SMF, 1 files) [★核心]

> SMF为PDU会话选择UPF★

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/分布式网络功能/WSFD-107010 UPF选择_10789013.md
```

---

### Batch-35: WSFD-010202 基于位置区域对等网元选择 (UNC/SMF, 5 files) [辅助]

> 基于位置区域的对等网元选择

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-010202 基于位置区域的对等网元选择/WSFD-010202 基于位置区域的对等网元选择参考信息_66344717.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-010202 基于位置区域的对等网元选择/实现原理_66344714.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-010202 基于位置区域的对等网元选择/激活基于位置区域的对等网元选择_66344715.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-010202 基于位置区域的对等网元选择/特性概述_66344712.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-010202 基于位置区域的对等网元选择/调测基于位置区域的对等网元选择_66344716.md
```

---

## 接入控制特性

### Batch-36: WSFD-106003 用户接入控制功能 (UNC/SMF, 14 files) [★核心]

> 用户接入控制(APN接入权限)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-106003 用户接入控制功能/用户接入控制功能（适用于AMF）/WSFD-106003 用户接入控制功能（适用于AMF）参考信息_48552639.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-106003 用户接入控制功能/用户接入控制功能（适用于AMF）/激活用户接入控制功能特性（适用于AMF）_48552637.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-106003 用户接入控制功能/用户接入控制功能（适用于AMF）/特性概述_48552635.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-106003 用户接入控制功能/用户接入控制功能（适用于AMF）/用户接入控制功能（适用于AMF）实现原理/典型场景下接入控制实现原理_48748810.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-106003 用户接入控制功能/用户接入控制功能（适用于AMF）/用户接入控制功能（适用于AMF）实现原理/本地配置与签约数据的优先级_48748809.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-106003 用户接入控制功能/用户接入控制功能（适用于AMF）/用户接入控制功能（适用于AMF）实现原理/移动性接入限制信息更新_48748811.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-106003 用户接入控制功能/用户接入控制功能（适用于AMF）/调测用户接入控制功能特性（适用于AMF）_48552638.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-106003 用户接入控制功能/用户接入控制功能（适用于SGSN、MME）/WSFD-106003 用户接入控制功能（适用于SGSN、MME）参考信息_68527097.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-106003 用户接入控制功能/用户接入控制功能（适用于SGSN、MME）/激活用户接入控制功能特性（适用于SGSN、MME）_64082494.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-106003 用户接入控制功能/用户接入控制功能（适用于SGSN、MME）/特性概述_68358176.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-106003 用户接入控制功能/用户接入控制功能（适用于SGSN、MME）/用户接入控制功能（适用于SGSN、MME）实现原理_68358178.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-106003 用户接入控制功能/用户接入控制功能（适用于SGSN、MME）/调测用户接入控制功能特性（适用于SGSN、MME）_68358180.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-106003 用户接入控制功能/用户接入控制功能（适用于SGSN、MME）_64082493.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/基本接入功能/WSFD-106003 用户接入控制功能_48552633.md
```

---

### Batch-37: GWFD-010151 接入控制 (UDG/UPF, 3 files) [★核心]

> 接入控制(UPF侧)

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010151 接入控制/GWFD-010151 接入控制参考信息_75667084.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010151 接入控制/GWFD-010151 接入控制特性概述_69675200.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010151 接入控制/激活接入控制_69675201.md
```

---
