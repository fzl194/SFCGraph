# APN 业务域 - 跨特性横向分析报告（Stage 3）

> **分析范围**: 37 个 APN 业务域特性（16 UDG + 21 UNC，含 3 个共享特性 IPFD-015002/015004/016000 按 U+C 计数共 37 实例位）
> **分析维度**: 分类总览 / 共性分析 / 配置差异 / 依赖关系 / 关键发现
> **文档目的**: 横向归纳 37 特性，作为 Stage 4 第 2-4 层（MMLCommand / ConfigObject / ConfigTask）的数据源
> **上游输入**: 37 篇 feature-knowledge（§配置/§配置对象/§与其他特性关系/§8 一致性）+ 4 篇 topic-knowledge（已归纳部分，避免重复）
> **下游消费者**: Stage 4 MMLCommand 层（附录 B）/ ConfigObject 层（附录 C）/ TaskCommandOrderEdge（附录 D）

---

## 目录

1. [特性分类总览](#1-特性分类总览)
2. [共性分析](#2-共性分析)
3. [配置差异分析](#3-配置差异分析)
4. [依赖关系分析](#4-依赖关系分析)
5. [关键发现](#5-关键发现)
6. [附录 A: 37 特性索引表](#附录a-37特性索引表)
7. [附录 B: ★MML 命令交叉参考（Stage 4 MMLCommand 层）](#附录b-mml命令交叉参考)
8. [附录 C: ★配置对象复用矩阵（Stage 4 ConfigObject 层）](#附录c-配置对象复用矩阵)
9. [附录 D: ★典型端到端配置流程（Stage 4 TaskCommandOrderEdge）](#附录d-典型端到端配置流程)

---

## 1. 特性分类总览

### 1.1 按功能类别分类（feature_group 6 大类）

> 分类原则来自《归纳-APN底座三维度.md》§0 + 《归纳-四维度决策与机制.md》附录 A + 本报告横向归纳。每个 Feature 节点需标注 `feature_group` 属性。

| feature_group | 特性数 | UDG 侧特性 | UNC 侧特性 | 核心能力 |
|---------------|--------|------------|------------|----------|
| **APN 基础**（会话管理底座） | **5** | GWFD-010101 会话管理(U) | WSFD-010501 会话管理(C)、WSFD-010503 多 PDN/PDU、WSFD-010400 用户数据管理、WSFD-106203 别名 APN | 宿主流程 + 签约数据源 + 并发治理 + APN 映射（纯描述性底座） |
| **地址分配** | **18** | GWFD-010104 总览、GWFD-010105 用户面分配、GWFD-020421 基于位置、GWFD-010107 静态路由冗余、GWFD-010108 地址自动检测、GWFD-020401 IPv6 承载、GWFD-020403 IPv4v6 双栈、GWFD-020406 IPv6 PD | WSFD-010502 地址分配方式、WSFD-010504 控制面地址分配、WSFD-104002 IPv4v6 双栈、WSFD-104001 IPv6 承载、WSFD-104004 IPv6 PD、WSFD-104005 DHCPv6、WSFD-104413 DHCP、WSFD-107010 UPF 选择、WSFD-107021 静态路由冗余(C) | 地址分配来源×类型正交矩阵（6×3），IPv6 承载 License 串联链 |
| **鉴权计费** | **5** | - | WSFD-010301 鉴权功能(AKA)、WSFD-011305 Radius 鉴权接入、WSFD-011306 Radius 功能、WSFD-011307 Radius 抄送、WSFD-108007 终端二次鉴权 | 两套并列鉴权体系 + Radius 三件套级联 |
| **接入方式**（4 隧道） | **5** | IPFD-015002 GRE(U+C)、IPFD-015004 IPSec(UDG)、GWFD-020411 MPLS VPN、GWFD-020412 L2TP VPN | IPFD-016000 IPSec(UNC)、WSFD-104411 MPLS VPN、WSFD-104410 L2TP VPN | 4 隧道对比（GRE/IPSec/MPLS/L2TP）；对称同构 3 + C 决策 U 执行 1 |
| **网元选择** | **2** | - | WSFD-107010 UPF 选择（5G）、WSFD-010202 对等网元选择（Pre-5G） | 代际互补；UPF 三轮筛选 + DNS 域名聚合 |
| **接入控制** | **2** | GWFD-010151 接入控制（U 面带宽流控） | WSFD-106003 用户接入控制功能（C 面接入权限） | ★ 非 C-U 对称（同名不同义） |
| **合计** | **37** | 16 | 21 | |

> **注**：地址分配域 18 个含 WSFD-107010/WSFD-107021 两个网元选择类（因与地址分配强耦合，UPF 选择决定地址分配执行侧）；feature_group 按首要归属，次要归属在附录 A 标注 `cross_group` 字段。

### 1.2 按产品归属分类

| 产品 | 特性数 | 说明 |
|------|--------|------|
| **UDG**（用户面 GGSN-U/PGW-U/UPF） | 16 | 全部 GWFD-01xxxx/02xxxx + IPFD-015002/015004 |
| **UNC**（控制面 SGSN/MME/SMF/PGW-C/AMF/GGSN-C） | 21 | 全部 WSFD-01xxxx/10xxxx/11xxxx + IPFD-016000 |
| **共享特性**（U+C 同名特性，按两侧计） | 3 | IPFD-015002 GRE（U+C 同构）、IPFD-015004+016000 IPSec（U+C 对称）、MPLS VPN（GWFD-020411+WSFD-104411） |

### 1.3 UDG-UNC 配对特性（C-U 协同 8 对）

> C-U 协同模式分类来自《归纳-配置树修正与Stage3待解决项》§2（4 模式）。Stage 4 Feature 节点需标注 `c_u_mode` 属性。

| 序号 | UDG 侧（用户面执行） | UNC 侧（控制面决策） | c_u_mode | 协同机制 |
|------|---------------------|---------------------|----------|----------|
| 1 | GWFD-010101 会话管理(U) | WSFD-010501 会话管理(C) | 决策执行分离 | UNC PFCP/GTP-C 下发 PDR/FAR/URR/QER，UDG 装规则、分配 F-TEID |
| 2 | GWFD-010105 用户面地址分配 | WSFD-010502 地址分配方式 + WSFD-010504 控制面地址分配 | 决策执行分离 | UNC 决策分配源（UDM/Radius/SMF/DHCP），UDG 按 PFCP CHV4/CHV6 真值表执行 |
| 3 | GWFD-020401 IPv6 承载(U) | WSFD-104001 IPv6 承载(C) | 决策执行分离 | UNC 决策+生成 RA，UDG 透传 IPv6 路由广播 |
| 4 | GWFD-020406 IPv6 PD(U) | WSFD-104004 IPv6 PD(C) | 决策执行分离 | UNC 决策前缀，UDG 透传协商（PFCP 解耦） |
| 5 | GWFD-010107 静态路由冗余(U) | WSFD-107021 静态路由冗余(C) | 对称同构 | 两侧均配 ADDRPOOL/POOLGRPMAP + GRE Tunnel，命令前缀差异（U: POOL；C: ADDRPOOL） |
| 6 | GWFD-010151 接入控制(U) | WSFD-106003 接入控制(C) | **非对称（同名不同义）** | U 侧 CAR/Shaping 带宽流控；C 侧签约 ARD/APN/卡类型接入权限 |
| 7 | GWFD-020412 L2TP VPN(U, LAC 执行) | WSFD-104410 L2TP VPN(C, 决策 LNS 参数) | **C 决策 U 执行** | UNC 决策 LNS 参数经 N4 下发，UDG 作 LAC 执行封装+PPP 透传；License C-U 不对称（U 必须 82200BVC，C 无） |
| 8 | IPFD-015002 GRE(U+C) | IPFD-015002 GRE(U+C) 同特性 | 对称同构 | UDG/UNC 两产品均部署同名特性，两侧 ADD GRETUNNEL 对称 |

**对称同构型扩展**（共享特性 U+C）：IPFD-015002 GRE、IPFD-015004(UDG)+016000(UNC) IPSec、GWFD-020411(UDG)+WSFD-104411(UNC) MPLS VPN、GWFD-010107(UDG)+WSFD-107021(UNC) 静态冗余。

### 1.4 滚动发布时间线

| 发布批次 | 首发版本 | 代表特性 |
|----------|----------|----------|
| **第 1 批（5G/4G 基础平台）** | 20.0.0 | GWFD-010101/010104/010105/020401/020403（UDG）、WSFD-010501/010502/010400/106003_B/107010/104001（UNC） |
| **第 2 批（隧道+IPv6 PD）** | 20.2.0 ~ 20.3.2 | GWFD-020411 MPLS、GWFD-020412 L2TP、WSFD-011305/104410/104411、2/3G 补全（GWFD-010101/WSFD-010501 20.3.0/20.3.2） |
| **第 3 批（接入控制+地址扩展）** | 20.5.0 ~ 20.7.0 | GWFD-020406 IPv6 PD、GWFD-020421 基于位置、WSFD-104002/104004/104005/104413 |
| **第 4 批（精细优化）** | 20.8.0+ | WSFD-010504 控制面地址分配、WSFD-108007 终端二次鉴权、WSFD-106003_A v02（20.11.0 RedCap） |

**规律**：5G/4G 首发于 20.0.0，2/3G 后向补全（20.3.0/20.3.2）；隧道类集中 20.2~20.3；IPv6 PD/位置扩展在 20.5~20.7；控制面精细分配与二次鉴权在 20.8+。

---

## 2. 共性分析

### 2.1 共享的 PFCP/N4 接口体系（地址分配 C-U 解耦的核心）

**核心发现**：APN 业务域 37 个特性中 24+ 个直接或间接依赖 PFCP/N4 接口完成 C-U 协同，是地址分配/会话管理/接入控制/接入方式（L2TP）类的统一基础设施。

| 信元/参数 | 用途 | 涉及特性 | 源 |
|-----------|------|----------|----|
| **CHV4/CHV6**（UE IP Address Choose） | 地址分配方式选择（1=用户面分配，0=外部分配） | GWFD-010104/010105、WSFD-010502/010504 | [GWFD-010105 §3.4 真值表] |
| **V4/V6 BIT** | 外部分配地址指示（SMF/Radius/UDM 下发） | GWFD-010105、WSFD-010502 | [GWFD-010104 §3.3] |
| **UP Function Flag ADUP=1** | UDG 地址分配能力上报（恒定） | GWFD-010105、WSFD-010502 | [GWFD-010105 §3.1] |
| **LAC/TAC**（位置信息） | 基于位置地址分配匹配 | GWFD-020421、WSFD-010502 | [GWFD-020421 §3.5] |
| **Framed-Pool**（Radius） | Radius 下发地址池名 | GWFD-010105 子方式4、WSFD-011306、WSFD-010502 | [WSFD-010502 §8.2 #6] |
| **L2TP 私有信元** | L2TP VPN C-U 协同（可用 SET L2TPKEY/L2TPN4KEY 加密） | GWFD-020412、WSFD-104410 | [GWFD-020412 §8.3] |
| **软参 BIT391** | 地址分配方式真值表标准/华为私有切换 | GWFD-010104、GWFD-010105 | [GWFD-010105 §3.4.2] |

### 2.2 共享的地址池体系（UDG 侧 4 种子方式 + UNC 侧 ADDRPOOL）

**核心发现**：UDG 侧 GWFD-010105/020421/020403/020406/010107 共享同一套 `SECTION → POOL(LOCAL) → POOLGROUP → POOLGRPMAP` 基础设施；UNC 侧 WSFD-010502/010504/107021/104413 共享 `SECTION → ADDRPOOL → ADDRPOOLGRP → POOLGRPMAP` 对称体系（命令前缀不对称，见 §3.1）。

**UDG 标准绑定链（5 特性共用）**：
```
ADD SECTION → ADD POOL(POOLTYPE=LOCAL) → ADD POOLGROUP → ADD POOLBINDGROUP
       │
       └── ADD POOLGRPMAP（映射条件：APN / LOCATION / SMF 任意组合）
              │
              └── SET IPALLOCRULE（全局三级规则） / SET APNIPALLOCRULE（APN 级）
```

使用此绑定链的 UDG 特性：GWFD-010104、GWFD-010105、GWFD-020421、GWFD-010107、GWFD-020403、GWFD-020406。

**UNC 标准绑定链（4 特性共用）**：
```
ADD SECTION → ADD ADDRPOOL → ADD ADDRPOOLGRP → ADD POOLBINDGRP
       │
       └── ADD POOLGRPMAP（映射条件）
              │
              └── ADD UPFBINDGRP（绑定 UPF，PRIORITY 控制优先级）
```

使用此绑定链的 UNC 特性：WSFD-010502、WSFD-010504、WSFD-107021、WSFD-104413、WSFD-104005。

### 2.3 共享的 License 使能机制（IPv6 承载 License 串联链）

**核心发现**：IPv6 完整承载需**线性 License 依赖链**，是 APN 业务域最长的依赖路径。License 使能统一通过 `SET LICENSESWITCH:LICITEM="LKV...",SWITCH=ENABLE` 命令。

```
[GWFD-020401 IPv6 承载上下文]  82209828 LKV3G5V6PB01（承载基础设施，必装）
        │
        ▼
[GWFD-020403 IPv4v6 双栈接入]  82209829 LKV3G5VDSA01（双栈能力使能层）
        │
        ▼
[GWFD-020406 IPv6 PD]          82200CKF LKV3G5P6PD01（V6PREFIXLENGTH<64 触发）
        │
        ▼ （UNC 侧对称）
[WSFD-104001] / [WSFD-104002] / [WSFD-104004]  82208006 LKV3W9V6PD11（UNC PD）
```

> 来源：[GWFD-020403 §7.2]、[GWFD-020406 §1.4]、[归纳-四维度 §1.4]

**需 License 的特性清单（13 个）**：
- 地址分配域：GWFD-020401/020403/020406（UDG IPv6 三件套）、WSFD-104001/104004（UNC IPv6 PD）、GWFD-020421（基于位置 82200BAK）
- 接入方式域：GWFD-020411 MPLS（编号待补）、GWFD-020412 L2TP（82200BVC）、WSFD-104411 MPLS UNC（81203325 LKV2MPVPN01）
- 鉴权域：WSFD-108007（82200DSF LKV2SECAA01）
- 接入控制域：WSFD-106003 子特性 B（82206571 LKV2ARD02）
- 网元选择域：WSFD-107010（82209917 LKV2USBL01 + 82200BES LKV2GWUS01 双 License）
- 别名 APN：WSFD-106203（双 License：LKV2ALIASAPN02 SGSN/MME 侧 + LKV2AAPN01 GGSN/PGW-C/SMF 侧）

**无需 License 的特性（24 个）**：纯描述性底座（GWFD-010101/WSFD-010501/010503/010400/010301）、地址分配机制层（GWFD-010104/010105/010107/010108/WSFD-010502/010504）、Radius 三件套之一（WSFD-011305/011306/011307）、接入控制 U 侧（GWFD-010151）、GRE/IPSec（IPFD-015002/015004/016000）、对等网元选择（WSFD-010202）、DHCP（WSFD-104413/104005）、WSFD-106003 子特性 A、UNC IPv6 部分（WSFD-104002）。

### 2.4 共享的 AAA/Radius 协议承载体系（鉴权级联）

**核心发现**：Radius 协议是 APN 业务鉴权的统一承载，4 鉴权方式 × Radius 三件套 + 二次鉴权形成强依赖链。

```
[WSFD-011306 Radius 功能]（协议承载：PAP/CHAP、服务器组、Bypass）
        │ 必须先激活
        ▼
[WSFD-011305 Radius 鉴权接入]（ACCESSMODE 决策：TRANS_AUTH/NON_TRANS 触发）
        │ 必须先激活
        ▼
[WSFD-108007 终端二次鉴权]（DN-AAA 经 UPF N4 GTP-U 隧道转接，License 82200DSF）
        │
        ▼
[WSFD-011307 Radius 抄送]（鉴权/计费消息并行抄送给第三方，共享配置对象 + PRIFLAG=CARBON_COPY）
```

> 来源：[WSFD-108007 §2.2]、[归纳-四维度 §2.3]

### 2.5 共享的 VPN 实例 + 接口 + 路由发布体系（隧道+地址分配共用）

**核心发现**：隧道类（GRE/IPSec/MPLS/L2TP）与地址分配类（010104/010105/020401/020403/020406）共享 VPN 实例 + LoopBack/Tunnel 接口 + 静态路由/OSPF 路由发布基础设施。

**共用配置对象**：
- `ADD VPNINST` / `ADD L3VPNINST` / `ADD VPNINSTAF`：VPN 实例（IPv4/IPv6 地址族）
- `ADD INTERFACE` + `ADD IPBINDVPN` + `ADD IFIPV4ADDRESS`：物理/逻辑接口绑定 VPN
- `ADD SRROUTE` / `ADD SRROUTE6`：静态路由（引导流量进 Tunnel）
- `ADD OSPF` / `ADD OSPFAREA` / `ADD OSPFNETWORK` / `ADD OSPFIMPORTROUTE`：IPv4 侧 WLR 路由发布
- `ADD OSPFV3` / `ADD OSPFV3AREA` / `ADD OSPFV3IMPORTROUTE`：IPv6 侧 WLR 路由发布
- `ADD ROUTEPOLICY` / `ADD ROUTEPOLICYNODE` / `ADD MATCHROUTETYPE`：路由策略

### 2.6 共享的 UPF 属性体系（网元选择 + 地址分配共用）

**核心发现**：WSFD-107010 UPF 选择与 WSFD-010502/010504/107021 地址分配共用 `ADD UPNODE` 命令（同一命令，不同参数维度）。

| 共用对象 | WSFD-107010 用途 | WSFD-010502 用途 |
|----------|------------------|-------------------|
| `ADD UPNODE` | UPF 位置特征 + 分流能力 | `ADDRALLOCMODE=INHERIT` 参数 |
| `ADD PNFPROFILE` | UPF NF 实例属性（WEIGHT/PRIORITY） | 静态 IP 段绑定 UPF 配置 |
| `ADD UPFBINDGRP` | - | 绑定 UPF（PRIORITY 控制优先级） |

> **冲突协调**：静态 IP 段绑定 UPF 与 SMF 主锚点 UPF 选择冲突时，**SMF 选择优先**（FR-APN-SMF主锚点优先）。[WSFD-107010 §3.3]

---

## 3. 配置差异分析

### 3.1 ★ UDG vs UNC 地址池命令前缀不对称（核心 Stage 4 ConfigObject 关键）

**核心发现**：UDG 侧（GWFD-010105）与 UNC 侧（WSFD-010502/010504/107021）的地址池命令**前缀不对称**，是 Stage 4 ConfigObject 节点必须区分建模的关键。

| 配置对象 | UDG 命令（GWFD-010105/010107/020421） | UNC 命令（WSFD-010502/010504/107021） | POOLTYPE 取值差异 |
|----------|----------------------------------------|----------------------------------------|-------------------|
| 地址池 | `ADD POOL`（POOLTYPE=LOCAL） | `ADD ADDRPOOL` | LOCAL（U）vs UDM（C，UNC 仅静态签约用 UDM） |
| 地址段 | `ADD SECTION` | `ADD SECTION` | 一致 |
| 地址池组 | `ADD POOLGROUP` | `ADD ADDRPOOLGRP` | - |
| 地址池绑定组 | `ADD POOLBINDGROUP` | `ADD POOLBINDGRP` | 命名差异（GROUP vs GRP） |
| 地址池组映射 | `ADD POOLGRPMAP` | `ADD POOLGRPMAP` | 一致 |
| UPF 绑定组 | - | `ADD UPFBINDGRP` | UNC 独有 |
| APN 绑定 | - | `ADD POOLBINDAPN` | UNC 独有 |

**Stage 4 建模建议**：ConfigObject 节点需标注 `product_side=UDG/UNC`，POOL 与 ADDRPOOL 分离建模，避免规则匹配混淆。

### 3.2 APNL2TPATTR (U) vs APNL2TPCTRL (C) 不对称（C 决策 U 执行型）

**核心发现**：L2TP VPN 的 C-U 配置对象命名与参数量均不对称，是 C 决策 U 执行模式的典型体现。

| 维度 | UDG 侧 GWFD-020412 | UNC 侧 WSFD-104410 |
|------|---------------------|---------------------|
| 核心配置对象 | `APNL2TPATTR`（SET APNL2TPATTR，10+ 参数） | `APNL2TPCTRL`（SET APNL2TPCTRL，仅 2 参数 APN/L2TPSWITCH） |
| 角色 | LAC 执行（封装+PPP 透传） | 决策（下发 LNS 参数经 N4） |
| License | 必须 82200BVC LKV3G5L2TP01 | 无 |
| 关联对象 | L2TPGROUP/L2TPCLIENTIP/L2TPRDSCLIENT/PPPCFG/GLOBALL2TP/L2TPN4KEY | L2TPKEY（UNC 侧加密） |
| C-U 加密 | `SET L2TPN4KEY`（UDG） | `SET L2TPKEY`（UNC），两端密钥须相同 |

> 来源：[GWFD-020412 §8.1 #1]、[归纳-配置树修正 §1.3]

### 3.3 4 隧道配置对象对比

> 来源：[归纳-四维度 §3.1]

| 维度 | GRE [IPFD-015002] | IPSec [IPFD-015004/016000] | MPLS VPN [GWFD-020411/WSFD-104411] | L2TP VPN [GWFD-020412/WSFD-104410] |
|------|-------------------|----------------------------|-------------------------------------|-------------------------------------|
| **隧道层次** | 三层 | 三层 | 三层（L3VPN） | **二层**（PPP） |
| **封装** | GRE（IP 协议号 47） | AH(51)/ESP(50)+IKE | MPLS 标签（I-L+O-L） | L2TP+PPP |
| **加密** | 否 | 是（ESP） | 否 | 否 |
| **License** | 无 | 无 | 必须（UDG 待补/UNC 81203325） | C-U 不对称（UDG 82200BVC/UNC 无） |
| **核心配置对象** | GRETUNNEL + Tunnel 接口 + LoopBack | ACL→Proposal→IKEPeer→Policy→Tunnel（VNRS+IPsec 双配） | VPN 实例(VRF)+RD+VPN Target+MP-BGP | APNL2TPATTR+L2TPGROUP+PPPCFG |
| **C-U 模式** | 对称同构 | 对称同构 | 对称同构 | **C 决策 U 执行** |
| **文档缺口** | 完整 | 完整 | **9 篇无 MML 脚本**（需命令字典补全） | 完整 |

### 3.4 IPv6 地址族激活差异（VPNINSTAF AFTYPE）

**核心发现**：IPv4 地址分配仅需 IPv4 VPN，IPv6/双栈需额外激活 IPv6 地址族。

| 地址类型 | VPN 配置 | OSPF 进程 |
|----------|----------|-----------|
| IPv4 | ADD VPNINST + ADD L3VPNINST（无 VPNINSTAF 或 AFTYPE=ipv4uni） | ADD OSPF + ADD OSPFIMPORTROUTE PROTOCOL=wlr |
| IPv6 | ADD VPNINSTAF **AFTYPE=ipv6uni ★** | ADD OSPFV3 + ADD OSPFV3IMPORTROUTE PROTOCOL=wlr |
| 双栈 | IPv4 VPN + IPv6 VPN 双实例（HASVPN+HASVPNIPV6） | OSPF + OSPFV3 双进程 |

> 来源：[GWFD-020401 §2.2]、[GWFD-020403 §4.1]

### 3.5 别名 APN 双视角语义反转（命令族命名差异）

**核心发现**：WSFD-106203 同特性 ID 在两套网元下命令族命名不同。

| 网元角色 | 命令族 | License |
|----------|--------|---------|
| SGSN/MME 侧（协商 APN→别名 APN） | `ADD ALIASAPN` | 82207546 LKV2ALIASAPN02 |
| GGSN/PGW-C/SMF 侧（别名 APN→真实 APN） | `ADD APNALIAS` | 82200BNM LKV2AAPN01 |

> 来源：[WSFD-106203 §8.1]、[归纳-APN底座 §1.4]

---

## 4. 依赖关系分析

### 4.1 特性依赖图（depends_on）

```
                  ┌─────────────────────────────────────────────┐
                  │  会话管理根底座（纯描述性，被多特性依赖）       │
                  │  GWFD-010101(U) + WSFD-010501(C)            │
                  └──────────────┬──────────────────────────────┘
                                 │ flow_depends_on
                                 ▼
            ┌────────────────────────────────────────────────────┐
            │  地址分配机制层 GWFD-010105(U) + WSFD-010502(C)     │
            │  + WSFD-010504(C) + GWFD-010104(总览)               │
            └─┬───────────────┬───────────────┬──────────────┬───┘
              │               │               │              │
              ▼               ▼               ▼              ▼
   ┌──────────────┐  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
   │ IPv6 承载链  │  │ 基于位置     │ │ 静态路由冗余 │ │ 地址自动检测 │
   │ 020401→020403│  │ GWFD-020421  │ │ GWFD-010107  │ │ GWFD-010108  │
   │   →020406    │  │ (License)    │ │ ↔WSFD-107021 │ │ (互斥对象)   │
   └──────────────┘  └──────────────┘ └──────────────┘ └──────────────┘
              │
              ▼ IPv6 PD UNC 对称
   ┌─────────────────────────────────────┐
   │ WSFD-104001(C, IPv6 承载)           │
   │  ← strong_depends_on                │
   │ WSFD-104002(C, 双栈) + WSFD-104004  │
   │  (C, PD, 3 条强依赖)                │
   └─────────────────────────────────────┘

            ┌────────────────────────────────────────────────────┐
            │  Radius 鉴权级联链                                  │
            │  WSFD-011306(C, Radius 功能)                       │
            │   → strong_depends_on                              │
            │  WSFD-011305(C, 鉴权接入)                          │
            │   → strong_depends_on                              │
            │  WSFD-108007(C, 二次鉴权)                          │
            │   ← parallel_extends                               │
            │  WSFD-011307(C, 抄送，共享配置对象)                │
            └────────────────────────────────────────────────────┘

            ┌────────────────────────────────────────────────────┐
            │  接入控制非对称（同名不同义，非 C-U 对称）           │
            │  GWFD-010151(U, 带宽流控)  vs  WSFD-106003(C, 权限) │
            │  WSFD-106003 子特性 B → strong_depends_on          │
            │  WSFD-010301(C, 底层 AKA 鉴权，卡类型控制前置)      │
            └────────────────────────────────────────────────────┘
```

### 4.2 核心特性辐射分析

**会话管理根底座（GWFD-010101 + WSFD-010501）辐射范围最大**：

| 依赖特性 | 依赖类型 | 底座提供能力 |
|----------|----------|-------------|
| GWFD-010105 / WSFD-010502 地址分配 | flow_depends_on | PDU/PDN 会话宿主流程 |
| GWFD-020401~020406 IPv6 系列 | flow_depends_on | IPv6 承载会话上下文 |
| WSFD-010503 多 PDN/PDU | inherits + extends | 并发治理层 |
| GWFD-010151 / WSFD-106003 接入控制 | flow_depends_on | 接入时机的会话触发 |
| 全部隧道类（GRE/IPSec/MPLS/L2TP） | flow_depends_on | 隧道内会话承载 |

**IPv6 承载链（GWFD-020401）辐射**：

| 依赖特性 | 依赖类型 | 依据 |
|----------|----------|------|
| GWFD-020403 IPv4v6 双栈 | capability_enables（能力使能层） | [GWFD-020403 §7.2] |
| GWFD-020406 IPv6 PD | strong_depends_on | [GWFD-020406 §1.5] |
| WSFD-104002 / WSFD-104004（UNC 对称） | strong_depends_on（声明矛盾修正） | [归纳-配置树修正 §3.1] |

**Radius 功能（WSFD-011306）辐射**：

| 依赖特性 | 依赖类型 | 共享对象 |
|----------|----------|----------|
| WSFD-011305 Radius 鉴权接入 | strong_depends_on | RDSSVRGRP（服务器组） |
| WSFD-108007 终端二次鉴权 | strong_depends_on | UPFRDSSVR/UPFRDSCLIENTIP |
| WSFD-011307 Radius 抄送 | parallel_extends（共享配置对象） | RDSSVRGRP + PRIFLAG=CARBON_COPY |

### 4.3 依赖声明矛盾清单（8 对，来自《归纳-配置树修正》§3）

> 以下为特性文档声明"不涉及"但实际被强依赖或存在隐性交互的特性对。Stage 4 必须以流程语义为准建模，忽略"不涉及"声明。

| # | 被依赖特性 | 实际依赖方 | 矛盾类型 | Stage 4 建模 |
|---|-----------|-----------|----------|--------------|
| 1 | WSFD-104001 IPv6 承载(C) | WSFD-104002/104004 | 单向依赖声明矛盾 | `strong_depends_on`（忽略"不涉及"） |
| 2 | WSFD-107010 UPF 选择 | WSFD-010502 单向引用 | 单向引用 | `interacts_with`（冲突协调 FR-SMF主锚点优先） |
| 3 | IPFD-015004 IPSec | IPFD-015002 GRE（源地址互斥） | 源地址互斥来自 GRE 文档 | `mutually_exclusive`（源地址维度，FR-GRE-IPSEC-SRC-EXCL） |
| 4 | GWFD-010101 会话管理(U) | GWFD-010105（流程步骤16 引用） | 概述声明无，实现强耦合 | `flow_depends_on`（区分配置/流程依赖） |
| 5 | WSFD-010301 底层 AKA | WSFD-106003 子特性 B（卡类型控制） | 两套鉴权并列互不引用 | `strong_depends_on`（FR-卡类型依赖鉴权） |
| 6 | WSFD-011307 Radius 抄送 | WSFD-011305/011306 | 声明独立但功能强关联 | `parallel_extends`（配置对象共享） |
| 7 | GWFD-020411 MPLS | IGP/MPLS/BGP 基础 | 显式无交互，隐性依赖 | `implicit_depends_on`（元数据标注） |
| 8 | GWFD-020412 L2TP ↔ GWFD-020421 基于位置 | 互斥声明单向（020421 声明，020412 未声明） | 互斥单向 | `mutually_exclusive` 双向（FR-LOC-L2TP-EXCL） |

### 4.4 互斥关系清单（Stage 4 FeatureRule）

| 互斥对 | 互斥维度 | 文档依据 | FeatureRule ID |
|--------|----------|----------|----------------|
| GWFD-020421 ↔ GWFD-020412 | 地址分配主体不同（LNS 远程 vs 位置本地池） | [GWFD-020421 §1.6] | FR-LOC-L2TP-EXCL |
| GWFD-020412 ↔ GWFD-010108 | L2TP 与用户面地址自动检测不可同时应用 | [GWFD-020412 §1.6] | FR-L2TP-ADDRAUTO-EXCL |
| IPFD-015002 ↔ IPFD-015004 | GRE 隧道源地址不能与 IPSec 源地址相同 | [IPFD-015002 §1.10] | FR-GRE-IPSEC-SRC-EXCL |

---

## 5. 关键发现

### 5.1 发现一：纯描述性根底座判定

**核心发现**：GWFD-010101(U) + WSFD-010501(C) 是 APN 域的**纯描述性根底座** —— 无独立 MML 配置命令（仅运维查询 DSP POOLUSAGE/DSP SESSIONINFO + 2/3G 维护命令 PDPAPN）、无 License、无独立配置对象、PDU/PDN/PDP 会话由控制面 PFCP/GTP-C 信令被动触发。

> 来源：[GWFD-010101 §4]、[WSFD-010501 §4]、[归纳-APN底座 §1.1]

### 5.2 发现二：IPv6 承载 License 串联链是地址分配域最长依赖路径

**核心发现**：IPv6 完整承载需 020401→020403→020406 线性 License 依赖链（承载基础设施→双栈能力使能→PD 前缀代理），叠加 UNC 侧 104001/104002/104004 对称链。前缀长度 64 是 PD 分水岭（V6PREFIXLENGTH<64 切换为 PD 模式）。

> 来源：[GWFD-020403 §7.2]、[GWFD-020406 §1.4]、[归纳-四维度 §1.4]

### 5.3 发现三：双栈 = 能力使能层（非父子、非包含）

**核心发现**：GWFD-020403 是能力使能层，不替代 GWFD-010105 的分配机制，而是使能其 IPv4v6 地址类型落地。020403 是 010105 的"双栈特化版本"，Stage 4 Feature 变体维度需建模 `能力层级=使能层/机制层`，License 约束建模为 `FR-DUALSTACK-NEED-LICENSE`（使能方向单向 020403→010105）。

> 来源：[GWFD-020403 §7.2]、[归纳-配置树修正 §1.1]

### 5.4 发现四：接入控制非 C-U 对称（同名不同义）

**核心发现**：GWFD-010151（U 面带宽流控 CAR/Shaping）与 WSFD-106003（C 面接入权限 ARD/APN/卡类型）**机制完全不同，非同一控制目标的 C-U 分工**。Stage 4 必须分别建模为两个独立 Feature 变体（bandwidth_control vs access_permission），不建 `c_u_symmetric` 边。

> 来源：[GWFD-010151 §8]、[WSFD-106003 §8]、[归纳-APN底座 §3.3]

### 5.5 发现五：4 隧道 C-U 模式清晰二分

**核心发现**：接入方式类 4 隧道按 C-U 协同模式清晰二分 —— 对称同构型（GRE/IPSec/MPLS，两侧配置对象与命令对称）vs. C 决策 U 执行型（L2TP，UNC 决策 LNS 参数，UDG 作 LAC 执行）。

> 来源：[归纳-四维度 §3.2]、[归纳-配置树修正 §2]

### 5.6 发现六：别名 APN 双视角语义反转

**核心发现**：WSFD-106203 同特性 ID 在两套网元下映射方向相反、命令族命名不同、License 分离 —— SGSN/MME 侧（协商 APN→别名 APN，DNS 屏蔽，ADD ALIASAPN，LKV2ALIASAPN02）vs. GGSN/PGW-C/SMF 侧（别名 APN→真实 APN，资源归一，ADD APNALIAS，LKV2AAPN01）。Stage 4 建议拆分为两个 Feature 变体节点。

> 来源：[WSFD-106203 §8.1]、[归纳-APN底座 §1.4]

### 5.7 发现七：IPV4ALLOCTYPE/IPV6ALLOCTYPE 实为 PFCP BIT 而非配置参数

**核心发现**：任务要求关注的 `IPV4ALLOCTYPE`/`IPV6ALLOCTYPE` 参数名在两侧产品文档均未显式定义；实际指示 IPv4/IPv6 分配类型的是 PFCP Session Est Req 中的 **CHV4/CHV6/V4/V6 BIT 位组合**。Stage 4 SemanticObject `SO-ADDRESS-POOL` 的 `type` 属性来源应标 `PFCP BIT (CHV4/CHV6/V4/V6)`，不要建模为配置参数。

> 来源：[WSFD-010502 §8.2 #6]、[GWFD-010105 §3.4]、[归纳-配置树修正 §1.4]

### 5.8 引用归纳文件的关键发现汇总

本报告 §5 关键发现直接引用以下 topic-knowledge 文件的结论，避免重复：
- **《归纳-配置树修正与Stage3待解决项.md》**：11 处配置树修正（§1）+ 8 对依赖声明矛盾（§3）+ 10 类文档缺口（§4）+ 12 个待解决问题（§5）
- **《归纳-四维度决策与机制.md》**：6 候选 DecisionPoint（§5.1）+ 4 候选 SemanticObject（§5.2）+ 11 候选 FeatureRule（§5.3）+ 7 个 Stage 3 预留问题（§6）
- **《归纳-APN底座三维度.md》**：6 候选 DP（§4.1）+ 8 候选 SO（§4.2）+ 16 候选 FeatureRule（§4.3）

---

## 附录 A: 37 特性索引表

> Stage 4 Feature 层（业务层 + 特性层）数据源。`source_evidence_ids` 占位 `EV-CA-01`，Stage 5 实例化时映射到各 feature-knowledge 的 `EV-FK-xx`。

| 序号 | feature_id | feature_name | product | feature_group | applicable_nf | license_required | 首发版本 | source_evidence_ids |
|------|-----------|--------------|---------|---------------|---------------|------------------|----------|---------------------|
| 1 | GWFD-010101 | 会话管理(U) | UDG | APN 基础 | SGW-U/PGW-U/UPF | 无 | 20.0.0 | EV-CA-01 |
| 2 | GWFD-010104 | 地址分配方式(总览) | UDG | 地址分配 | SGW-U/PGW-U/UPF | 无 | 20.0.0 | EV-CA-01 |
| 3 | GWFD-010105 | 用户面地址分配 | UDG | 地址分配 | SGW-U/PGW-U/UPF | 无 | 20.0.0 | EV-CA-01 |
| 4 | GWFD-010107 | 静态地址用户路由冗余(U) | UDG | 地址分配 | PGW-U/UPF | 无 | 20.3.0 | EV-CA-01 |
| 5 | GWFD-010108 | 用户面地址自动检测 | UDG | 地址分配 | PGW-U/UPF | 无 | 20.3.0 | EV-CA-01 |
| 6 | GWFD-010151 | 接入控制(U) | UDG | 接入控制 | SGW-U/PGW-U/UPF | 无 | 20.0.0 | EV-CA-01 |
| 7 | GWFD-020401 | IPv6 承载上下文(U) | UDG | 地址分配 | PGW-U/UPF | 82209828 LKV3G5V6PB01 | 20.1.0 | EV-CA-01 |
| 8 | GWFD-020403 | IPv4v6 双栈接入(U) | UDG | 地址分配 | PGW-U/UPF | 82209829 LKV3G5VDSA01 | 20.1.0 | EV-CA-01 |
| 9 | GWFD-020406 | IPv6 Prefix Delegation(U) | UDG | 地址分配 | PGW-U/UPF | 82200CKF LKV3G5P6PD01 | 20.5.0 | EV-CA-01 |
| 10 | GWFD-020411 | MPLS VPN(U) | UDG | 接入方式 | PE | 必须（编号待补） | 20.2.0 | EV-CA-01 |
| 11 | GWFD-020412 | L2TP VPN(U, LAC) | UDG | 接入方式 | PGW-U/UPF | 82200BVC LKV3G5L2TP01 | 20.3.0 | EV-CA-01 |
| 12 | GWFD-020421 | 基于位置的地址分配 | UDG | 地址分配 | PGW-U/UPF | 82200BAK LKV3G5LBAA01 | 20.5.0 | EV-CA-01 |
| 13 | IPFD-015002 | GRE(U+C) | UDG+UNC | 接入方式 | SGW-U/PGW-U/UPF + SGSN/MME/SGW-C | 无 | 20.0.0 | EV-CA-01 |
| 14 | IPFD-015004 | IPSec(UDG) | UDG | 接入方式 | SGW-U/PGW-U/UPF | 无 | 20.0.0 | EV-CA-01 |
| 15 | IPFD-016000 | IPSec(UNC) | UNC | 接入方式 | SGSN/MME/SGW-C | 无 | 20.0.0 | EV-CA-01 |
| 16 | WSFD-010202 | 基于位置区域对等网元选择 | UNC | 网元选择 | SGSN/MME/MSC | 无 | 20.3.0 | EV-CA-01 |
| 17 | WSFD-010301 | 鉴权功能(AKA) | UNC | 鉴权计费 | SGSN/MME/AMF | 无 | 20.0.0 | EV-CA-01 |
| 18 | WSFD-010400 | 用户数据管理 | UNC | APN 基础 | SGSN/MME/SMF/AMF | 无 | 20.0.0 | EV-CA-01 |
| 19 | WSFD-010501 | 会话管理(C) | UNC | APN 基础 | SGSN/MME/SGW-C/PGW-C/SMF/AMF | 无 | 20.0.0 | EV-CA-01 |
| 20 | WSFD-010502 | 地址分配方式(C) | UNC | 地址分配 | GGSN-C/PGW-C/SMF | 无 | 20.0.0 | EV-CA-01 |
| 21 | WSFD-010503 | 多 PDN/PDU 功能 | UNC | APN 基础 | MME/SMF | 无 | 20.0.0 | EV-CA-01 |
| 22 | WSFD-010504 | 控制面地址分配方式 | UNC | 地址分配 | GGSN-C/PGW-C/SMF | 无 | 20.8.0 | EV-CA-01 |
| 23 | WSFD-011305 | Radius 鉴权接入 | UNC | 鉴权计费 | GGSN-C/PGW-C/SMF | 无 | 20.3.2 | EV-CA-01 |
| 24 | WSFD-011306 | Radius 功能 | UNC | 鉴权计费 | GGSN-C/PGW-C/SMF | 无 | 20.0.0 | EV-CA-01 |
| 25 | WSFD-011307 | Radius 抄送功能 | UNC | 鉴权计费 | GGSN-C/PGW-C/SMF | 无 | 20.3.2 | EV-CA-01 |
| 26 | WSFD-104001 | IPv6 承载上下文(C) | UNC | 地址分配 | GGSN-C/PGW-C/SMF | 无（强被依赖） | 20.0.0 | EV-CA-01 |
| 27 | WSFD-104002 | IPv4v6 双栈接入(C) | UNC | 地址分配 | GGSN-C/PGW-C/SMF | 无 | 20.5.0 | EV-CA-01 |
| 28 | WSFD-104004 | IPv6 前缀代理(C) | UNC | 地址分配 | GGSN-C/PGW-C/SMF | 82208006 LKV3W9V6PD11 | 20.5.0 | EV-CA-01 |
| 29 | WSFD-104005 | DHCPv6 地址分配 | UNC | 地址分配 | GGSN-C/PGW-C/SMF | 无 | 20.5.0 | EV-CA-01 |
| 30 | WSFD-104410 | L2TP VPN(C, 决策) | UNC | 接入方式 | GGSN-C/PGW-C/SMF | 无（C-U 不对称） | 20.3.0 | EV-CA-01 |
| 31 | WSFD-104411 | MPLS VPN(C) | UNC | 接入方式 | PE | 81203325 LKV2MPVPN01 | 20.2.0 | EV-CA-01 |
| 32 | WSFD-104413 | DHCP 功能 | UNC | 地址分配 | GGSN-C/PGW-C/SMF | 无 | 20.5.0 | EV-CA-01 |
| 33 | WSFD-106003 | 用户接入控制功能(C) | UNC | 接入控制 | SGSN/MME/AMF | 子特性 B: 82206571 LKV2ARD02；A 无 | 20.0.0 | EV-CA-01 |
| 34 | WSFD-106203 | 别名 APN | UNC | APN 基础 | SGSN/MME + GGSN/PGW-C/SMF | 双：LKV2ALIASAPN02 + LKV2AAPN01 | 20.3.0 | EV-CA-01 |
| 35 | WSFD-107010 | UPF 选择 | UNC | 网元选择 | SMF | 82209917 LKV2USBL01 + 82200BES LKV2GWUS01 | 20.0.0 | EV-CA-01 |
| 36 | WSFD-107021 | 静态地址用户路由冗余(C) | UNC | 地址分配 | PGW-C/SMF | 无 | 20.3.0 | EV-CA-01 |
| 37 | WSFD-108007 | 终端二次鉴权 | UNC | 鉴权计费 | SMF | 82200DSF LKV2SECAA01 | 20.8.0 | EV-CA-01 |

---

## 附录 B: MML 命令交叉参考

> **★ Stage 4 MMLCommand 层数据源**。每条命令标注涉及特性（source feature_id），用于 MMLCommand→Feature 映射边。`source_evidence_ids` 占位 `EV-CA-01`。

### B.1 UDG 侧核心命令（16 特性）

| 命令 | 涉及特性 | 用途 | source_evidence_ids |
|------|----------|------|---------------------|
| SET LICENSESWITCH | GWFD-020401/020403/020406/020412/020421 | License 开关 | EV-CA-01 |
| ADD VPNINST | GWFD-010104/010105/020401/020412/020421、IPFD-015002/015004 | VPN 实例 | EV-CA-01 |
| ADD L3VPNINST | GWFD-010104/010105/020401/020403/020406、IPFD-015004 | L3VPN 实例 | EV-CA-01 |
| ADD VPNINSTAF | GWFD-020401/020403/020406、IPFD-015004 | VPN 地址族（IPv6 需 AFTYPE=ipv6uni） | EV-CA-01 |
| **ADD POOL** | GWFD-010104/010105/010107/020421/020403/020406 | 地址池（POOLTYPE=LOCAL/EXTERNAL） | EV-CA-01 |
| ADD SECTION | GWFD-010104/010105/010107/020421/020403/020406 | 地址段（V4STARTIP/V6PREFIXSTART，V6PREFIXLENGTH<64=PD） | EV-CA-01 |
| ADD POOLGROUP | GWFD-010104/010105/010107/020421/020403/020406 | 地址池组（IPV4ALLOCPRIALG/IPV6ALLOCPRIALG） | EV-CA-01 |
| ADD POOLBINDGROUP | GWFD-010104/010105/010107/020421/020403/020406 | 地址池绑定到池组（PRIORITY） | EV-CA-01 |
| **ADD POOLGRPMAP** | GWFD-010104/010105/010107/020421/020403/020406 | 池组映射（APN/SMF/LOCATION 任意组合） | EV-CA-01 |
| ADD APN | GWFD-010104/010105/010107/010151/020412/020421/020403 | APN/DNN 实例（HASVPN/HASVPNIPV6 双栈） | EV-CA-01 |
| **SET APNADDRESSATTR** | GWFD-010104/010105/020421/020403/020406 | APN 地址分配属性（SUPPORTIPV4/V6/IGNOREV4/V6POOLID/HOSTROUTEIP） | EV-CA-01 |
| SET IPALLOCRULE | GWFD-010105/020421/020406 | 全局三级地址分配规则（FIRSTRULE/SECONDRULE/THIRDRULE） | EV-CA-01 |
| SET APNIPALLOCRULE | GWFD-010105/020421 | APN 级地址分配规则（覆盖全局） | EV-CA-01 |
| ADD CPNODEID | GWFD-010105/020406 | SMF 的 NodeID | EV-CA-01 |
| SET IPALLOCBYSMFGLBSW | GWFD-010105/020406 | 基于 SMF 分配全局开关 | EV-CA-01 |
| SET IPALLOCBYSMFSW | GWFD-010105 | 指定 SMF 分配开关 | EV-CA-01 |
| ADD LACGROUP / ADD LACID | GWFD-020421/020406 | LAC 位置区组 | EV-CA-01 |
| ADD TACGROUP / ADD S1TACID / ADD N2TACID | GWFD-020421 | TAC 位置区组 | EV-CA-01 |
| **SET IPALLOCBYLOCGLBSW** | GWFD-020421 | 基于位置分配全局开关（IPv4/IPv6 分别） | EV-CA-01 |
| SET IPALLOCBYLOCSW | GWFD-020421 | 指定位置区开关（覆盖全局） | EV-CA-01 |
| **ADD ADRLOCWHITELST** | GWFD-020421/020406 | 位置区地址分配白名单（MSISDN） | EV-CA-01 |
| ADD CONFLICTIP / ADD CONFLICTIPV6 | GWFD-010105/020406 | 冲突地址标识 | EV-CA-01 |
| ADD OSPF / ADD OSPFAREA / ADD OSPFNETWORK | GWFD-010104/010105/010107/020421/020403 | IPv4 OSPF 进程 | EV-CA-01 |
| **ADD OSPFIMPORTROUTE** | GWFD-010104/010105/010107/020421/020403 | 引入 WLR 路由（PROTOCOL=wlr） | EV-CA-01 |
| ADD OSPFV3 / ADD OSPFV3AREA / ADD OSPFV3INTERFACE | GWFD-020401/020403/020406 | IPv6 OSPFv3 进程 | EV-CA-01 |
| **ADD OSPFV3IMPORTROUTE** | GWFD-020401/020403/020406 | 引入 WLR 到 OSPFv3 | EV-CA-01 |
| ADD ROUTEPOLICY / ADD ROUTEPOLICYNODE / ADD MATCHROUTETYPE | GWFD-020401/020403/020406 | 路由策略 | EV-CA-01 |
| ADD INTERFACE / ADD IPBINDVPN | GWFD-010107/020401/020403、IPFD-015002/015004 | 接口 + VPN 绑定 | EV-CA-01 |
| ADD IFIPV4ADDRESS / ADD IFIPV6ADDRESS / SET IFIPV6ENABLE | GWFD-010107、IPFD-015002/015004 | 接口 IP 地址 | EV-CA-01 |
| ADD LOGICINF | GWFD-020412 | Giif 逻辑接口 | EV-CA-01 |
| **ADD GRETUNNEL** / MOD GRETUNNEL / RMV GRETUNNEL | IPFD-015002、GWFD-010107 | GRE 隧道（TNLTYPE=gre） | EV-CA-01 |
| **ADD SRROUTE** / ADD SRROUTE6 | GWFD-010107、IPFD-015002/015004 | 静态路由 | EV-CA-01 |
| **SET APNQOSATTR** / LST APNQOSATTR | GWFD-010151 | APN QoS 属性（CARSHAPESWUL/DL + CARSHAPEUL/DL，接入控制核心） | EV-CA-01 |
| MOD APN / LST APN / RMV APN | GWFD-010151 | APN 管理 | EV-CA-01 |
| **SET APNL2TPATTR** / LST APNL2TPATTR | GWFD-020412 | L2TP APN 属性（★U 面核心，10+ 参数） | EV-CA-01 |
| ADD L2TPGROUP / ADD L2TPLNSINFO | GWFD-020412 | L2TP 组（本地配置方式） | EV-CA-01 |
| ADD L2TPCLIENTIP / ADD L2TPRDSCLIENT | GWFD-020412 | L2TP 源端 Giif 绑定 | EV-CA-01 |
| SET GLOBALL2TP | GWFD-020412 | L2TP 缺省属性 | EV-CA-01 |
| SET PPPCFG / SET APNPPPACCESS | GWFD-020412 | PPP 协商 + 鉴权 | EV-CA-01 |
| SET L2TPN4KEY | GWFD-020412 | N4 接口 L2TP 加密密钥（U 侧） | EV-CA-01 |
| SET SOFTPARAOFBIT | GWFD-020412 | 软参（Byte671 bit7 关闭快速流表） | EV-CA-01 |
| **ADD REDUNDRDTIP** | GWFD-010107 | 虚拟 IP（重定向业务流到 GRE Tunnel） | EV-CA-01 |
| **SET REDUNDUSER** | GWFD-010107 | 全局冗余开关（与 ADD POOL REDUNDFUNC 双使能） | EV-CA-01 |
| SET APNREDUNDUPSW | GWFD-010107 | APN 上行报文隧道转发开关（仅备用 UDG） | EV-CA-01 |
| ADD OSPFINTERFACE / MOD OSPFIMPORTROUTE / MOD IMPORTROUTE | GWFD-010107 | 主备 UDG 路由互通 + COST/MED 优先级 | EV-CA-01 |
| ADD VPNINSTANCE / ADD BGPVPNV4ROUTETARGET / ADD BGPVPNV4PEER（★推导，命令字典补全） | GWFD-020411 | MPLS VPN 实例 + MP-BGP（文档缺口，需补全） | EV-CA-01 |
| ADD IPSECPROPOSALIPSEC / ADD IKEPROPOSAL / ADD IKEPEER / ADD IPSECPOLICY / ADD PROPATTACHIPSECPROPOSAL / ADD ATTACHIKEPEER / ADD IPSECINTFCFGIPSEC / SET IKEGLOBALCONFIG | IPFD-015004/016000 | IPSec 安全提议+IKE 对等体+策略+接口配置 | EV-CA-01 |
| ADD ACLGROUPIPSEC / ADD ACLRULEADV4IPSEC | IPFD-015004/016000 | ACL 规则（保护数据流，仅源/目的 IP） | EV-CA-01 |
| ADD INTERFACEIPSEC / ADD IPBINDVPNIPSEC / ADD IFIPV4ADDRESSIPSEC / ADD L3VPNINSTIPSEC / ADD VPNINSTAFIPSEC | IPFD-015004/016000 | IPsec 微服务镜像配置 | EV-CA-01 |
| STR PDNROUTETST / STP PDNROUTETST / DSP PDNTSTRESULT | GWFD-010108 | 地址自动检测运维命令（3 条，无 ADD 配置） | EV-CA-01 |
| DSP POOLUSAGE / DSP SESSIONINFO | GWFD-010101/010105 | 会话管理运维查询（纯描述性底座） | EV-CA-01 |

### B.2 UNC 侧核心命令（21 特性）

| 命令 | 涉及特性 | 用途 | source_evidence_ids |
|------|----------|------|---------------------|
| SET LICENSESWITCH | WSFD-104001/104002/104004/106003_B/106203/107010/108007 | License 开关 | EV-CA-01 |
| **ADD ADDRPOOL** / MOD ADDRPOOL / RMV ADDRPOOL | WSFD-010502/010504/107021/104413/104005/104002/104004 | 地址池（UNC 侧，POOLTYPE 无 LOCAL，仅 UDM 静态） | EV-CA-01 |
| **ADD ADDRPOOLGRP** / ADD ADDRUPGROUP | WSFD-010502/010504/107021/104413/104005 | 地址池组（UNC 侧） | EV-CA-01 |
| ADD POOLBINDGRP / ADD POOLBINDAPN | WSFD-010502/010504/107021/104413/104005 | 地址池绑定（UNC 命名：GRP 非 GROUP） | EV-CA-01 |
| ADD POOLGRPMAP | WSFD-010502/010504/107021/104413/104005 | 池组映射（UNC 侧） | EV-CA-01 |
| ADD SECTION | WSFD-010502/010504/107021/104413/104005/104004 | 地址段 | EV-CA-01 |
| ADD UPFBINDGRP | WSFD-010502/010504/107021 | UPF 绑定（PRIORITY） | EV-CA-01 |
| ADD UPNODE | WSFD-010502/010504/107021/107010 | UPF 节点（位置特征+分流能力 / ADDRALLOCMODE=INHERIT） | EV-CA-01 |
| ADD PNFPROFILE | WSFD-010502/010504/107010/107021 | UPF NF 实例属性（WEIGHT/PRIORITY） | EV-CA-01 |
| ADD PNFDNN / ADD PNFNS / ADD PNFDNAI / ADD PNFUPFINFO | WSFD-107010 | UPF 支持的 DNN/切片/DNAI/EPS 互通 | EV-CA-01 |
| ADD UPAREA / ADD UPAREABINDN2TAI / ADD LOCBINDAREA / ADD PNFSMFSERAREA / ADD PNFTAIRANGE / ADD PNFTAI | WSFD-107010 | UPF 位置区绑定 | EV-CA-01 |
| ADD UPBINDS11 / ADD UPBINDGNGP | WSFD-107010 | SGW-U/PGW-U 接口绑定（S11/GnGp） | EV-CA-01 |
| SET UPSELECTPRI / SET UPSELECTFLAG / SET APNUPSELPLY / SET UPLOADBALANCE | WSFD-107010 | UPF 选择策略次序+开关+负载均衡 | EV-CA-01 |
| SET STATICADDRPARA | WSFD-010502 | 静态 IP 段绑定 UPF | EV-CA-01 |
| ADD BLACKLIST / LST BLACKLIST | WSFD-010502 | 静态地址黑名单 | EV-CA-01 |
| SET IPALLOCRULE / SET APNIPALLOCRULE / SET ADDRESSATTR / SET SOFTPARA | WSFD-010504 | 地址分配规则（UNC 控制面侧） | EV-CA-01 |
| SET IPALLOCBYLOCGLBSW | WSFD-010504 | 基于位置分配全局开关（UNC） | EV-CA-01 |
| SET APNADDRESSATTR / LST APNADDRESSATTR | WSFD-010504/104413/104005/104004 | APN 地址分配属性（UNC） | EV-CA-01 |
| **SET APNAUTHATTR** / LST APNAUTHATTR | WSFD-011305 | APN 鉴权属性（ACCESSMODE 4 种取值，鉴权接入核心） | EV-CA-01 |
| **ADD RDSSVRGRP** / ADD RDSSVR | WSFD-011306/011307 | Radius 服务器组 + 服务器（鉴权级联核心） | EV-CA-01 |
| ADD APNRDSSVRGRP | WSFD-011306/011307 | APN↔Radius 服务器组绑定 | EV-CA-01 |
| ADD APNRDSCLIENTIP | WSFD-011306 | APN Radius Client IP（鉴权/计费） | EV-CA-01 |
| SET APNRDSACCTCTRL | WSFD-011306 | Radius 计费控制（SRVTRIGGER/SUPPORTACCTRSP） | EV-CA-01 |
| SET APNRADIUSATTR | WSFD-011306 | Radius 域名增加/剥离 | EV-CA-01 |
| SET RDSRSPADDRCHK | WSFD-011306 | Radius 响应端口检查 | EV-CA-01 |
| ADD UPLIST4RDS | WSFD-011306/011307/108007 | PGW-U/UPF List（按主锚点 UPF 发送 AAA） | EV-CA-01 |
| SET FHBYPASS | WSFD-011306 | 故障场景一键放通（优先级最高） | EV-CA-01 |
| ADD RULE / ADD USERPROFILE / ADD RULEBINDING / ADD USRPROFGROUP / ADD UPBINDUPG / ADD APNUSRPROFG / ADD PCCPOLICYGRP | WSFD-011306（SRV_TRIGGER 场景） | PCC 规则体系（UNC 共用） | EV-CA-01 |
| ADD FLOWFILTER | WSFD-011306 | 流过滤器（与 UDG 一致） | EV-CA-01 |
| ADD VPNINST / ADD LOGICIP / ADD LOGICINF | WSFD-011306/011307/108007 | UNC 侧 VPN + Gi 逻辑接口 | EV-CA-01 |
| **ADD CPGTPUADDR** | WSFD-108007 | GTP-U 地址（SMF 下发分装 GTPU 报文 IP） | EV-CA-01 |
| **ADD RDSUPFCTRL** | WSFD-108007 | Radius UPF 控制（PREFERENCE/LOCKED） | EV-CA-01 |
| **ADD UPFRDSSVR** | WSFD-108007 | UPF Radius 服务器（DN-AAA，必须先于 UPFRDSCLIENTIP） | EV-CA-01 |
| **ADD UPFRDSCLIENTIP** | WSFD-108007 | UPF Radius 客户端 IP（必须最后执行） | EV-CA-01 |
| ADD NETWORKINSTVPNMAP | WSFD-108007（UPF 侧前置） | UPF VPN 配置（必须先于 UPFRDSSVR/CLIENTIP） | EV-CA-01 |
| **ADD GBARD** / ADD IUARD / ADD S1ARD（+ MOD/RMV/LST） | WSFD-106003 子特性 B | 接入限制参数（2/3/4G 签约 ARD/APN/卡类型） | EV-CA-01 |
| **ADD NGMMSUBDATA** / SET NGMMPROCTRL | WSFD-106003 子特性 A | 5GC 接入限制（AMF 侧移动性限制） | EV-CA-01 |
| **ADD APNALIAS**（+ MOD/RMV/LST） | WSFD-106203 GGSN/PGW-C/SMF 侧 | 别名 APN→真实 APN 映射（资源归一） | EV-CA-01 |
| **ADD ALIASAPN**（+ MOD/RMV/LST） | WSFD-106203 SGSN/MME 侧 | 协商 APN→别名 APN 映射（DNS 屏蔽） | EV-CA-01 |
| SET APNREPORTATTR / SET DEACTIVERATE | WSFD-106203 | APN 报告属性 + 去活速率 | EV-CA-01 |
| ADD APN / LST APN | WSFD-106203 | APN 管理（别名转换前置） | EV-CA-01 |
| **ADD APNACTNUM** / MOD APNACTNUM / RMV APNACTNUM / LST APNACTNUM | WSFD-010503 | 单 APN 并发限制（PDNNUM/IPV4ADDRNUM/IPV6ADDRNUM + PDNCONNREJCAUSE） | EV-CA-01 |
| ADD SMSUBDATA / MOD SMSUBDATA / RMV SMSUBDATA | WSFD-104001/104002/104004 | SM 子表数据（UNC IPv6 承载） | EV-CA-01 |
| SET SMFUNC / MOD GTPCCMPT | WSFD-104001/104002/104004 | SM 功能 + GTP-C 控制 | EV-CA-01 |
| ADD DHCPBINDPOOLGRP | WSFD-104413/104005 | DHCP 池组绑定 | EV-CA-01 |
| ADD DHCPSERVER / ADD DHCPSERVERGRP | WSFD-104413/104005 | DHCP 服务器 + 服务器组 | EV-CA-01 |
| ADD AGENTIP | WSFD-104413/104005 | DHCP Agent IP | EV-CA-01 |
| SET DHCPPARAREQ | WSFD-104413/104005 | DHCP 参数请求 | EV-CA-01 |
| **SET APNL2TPCTRL** / LST APNL2TPCTRL | WSFD-104410 | L2TP APN 控制（★C 面专用，仅 2 参数 APN/L2TPSWITCH） | EV-CA-01 |
| SET L2TPKEY | WSFD-104410 | N4 接口 L2TP 加密密钥（C 侧，与 UDG L2TPN4KEY 相同） | EV-CA-01 |
| SET PFCPPVTEXT / ADD UPCMPT | WSFD-104410 | PFCP 私有扩展 + UP 控制面管理 | EV-CA-01 |
| **ADD AREADNS** / MOD AREADNS / RMV AREADNS / LST AREADNS | WSFD-010202 | 位置区域 DNS 域名定制（LAC/RAC/TAC + ZONESW） | EV-CA-01 |
| ADD DNSN / ADD IPV4DNSH / ADD SGSNDNS | WSFD-010202 | DNS 配置（SGSN/MME） | EV-CA-01 |
| SET MSCSELPLCY | WSFD-010202 | MSC 选择策略（SRVCC 基于 RAI/LAI FQDN） | EV-CA-01 |
| **SET REDUNDUSER** | WSFD-107021 | 静态路由冗余全局开关（UNC 侧） | EV-CA-01 |
| ADD PDPAPN / MOD PDPAPN / RMV PDPAPN / LST PDPAPN | WSFD-010501 | 2/3G PDP APN 维护（会话管理 C 面） | EV-CA-01 |
| SET GBSM / SET IUSM / SET SMPDUCTRL / SET SDCFG / SET SMFUNC / SET CHGCHAR | WSFD-010501 | 2/3G 会话管理维护 | EV-CA-01 |
| ADD GBAUTHCIPH / ADD IUAUTHCIPH / ADD S1USRSECPARA / ADD NGUSRSECPARA（+ MOD/RMV/LST） | WSFD-010301 | 鉴权加密参数（2G/3G/4G/5G AKA 系列） | EV-CA-01 |
| MOD AMDATA | WSFD-010301 | AM 数据修改 | EV-CA-01 |
| SET SDBTMR / SET SYS | WSFD-010400 | 签约数据库定时器 + 系统配置（SUBSTORAG 存储分拆） | EV-CA-01 |
| DSP COMMMTX | WSFD-010301 | 通信上下文查询 | EV-CA-01 |

### B.3 命令统计

| 统计项 | 数量 |
|--------|------|
| UDG 侧独立 MML 命令（去重） | **~62** |
| UNC 侧独立 MML 命令（去重） | **~78** |
| 跨产品共用命令（同名不同参数） | POOL vs ADDRPOOL、POOLGROUP vs ADDRPOOLGRP、POOLBINDGROUP vs POOLBINDGRP、L2TPN4KEY vs L2TPKEY、ADD APN、SET LICENSESWITCH |
| **合计 MML 命令条目（B.1+B.2）** | **~140 条**（含跨产品共用的双计数） |

---

## 附录 C: 配置对象复用矩阵

> **★ Stage 4 ConfigObject 层数据源**。矩阵展示同一配置对象在不同特性中的使用情况（Y=使用，-=不使用）。供 ConfigObject→Feature 映射边。`source_evidence_ids` 占位 `EV-CA-01`。

### C.1 地址分配域核心配置对象复用矩阵

| 配置对象 | GWFD-010104 | GWFD-010105 | GWFD-010107 | GWFD-020421 | GWFD-020401 | GWFD-020403 | GWFD-020406 | WSFD-010502 | WSFD-010504 | WSFD-107021 | WSFD-104413 |
|---------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| POOL（UDG，POOLTYPE=LOCAL/EXTERNAL） | Y | Y | Y | Y | - | Y | Y | - | - | - | - |
| ADDRPOOL（UNC） | - | - | - | - | - | - | - | Y | Y | Y | Y |
| SECTION | Y | Y | Y | Y | - | Y | Y | Y | Y | Y | Y |
| POOLGROUP / ADDRPOOLGRP | Y | Y | Y | Y | - | Y | Y | Y | Y | Y | Y |
| POOLBINDGROUP / POOLBINDGRP | Y | Y | Y | Y | - | Y | Y | Y | Y | Y | Y |
| POOLGRPMAP | Y | Y | Y | Y | - | Y | Y | Y | Y | Y | Y |
| APN（ADD APN） | Y | Y | Y | Y | - | Y | Y | - | Y | - | Y |
| APNADDRESSATTR | Y | Y | - | Y | - | Y | Y | - | Y | - | Y |
| IPALLOCRULE（全局） | - | Y | Y | Y | - | Y | Y | - | Y | - | Y |
| APNIPALLOCRULE（APN 级） | - | Y | - | Y | - | - | Y | - | - | - | - |
| CPNODEID（SMF） | - | Y | - | - | - | - | Y | - | - | - | - |
| IPALLOCBYSMFGLBSW | - | Y | - | - | - | - | Y | - | - | - | - |
| LACGROUP / TACGROUP | - | - | - | Y | - | - | Y | - | - | - | - |
| IPALLOCBYLOCGLBSW | - | - | - | Y | - | - | Y | - | Y | - | - |
| ADRLOCWHITELST | - | - | - | Y | - | - | Y | - | - | - | - |
| CONFLICTIP / CONFLICTIPV6 | - | Y | - | - | - | - | Y | - | - | - | - |
| UPNODE（共用 UPF 选择+地址分配） | - | - | - | - | - | - | - | Y | Y | Y | - |
| PNFPROFILE | - | - | - | - | - | - | - | Y | Y | Y | - |
| UPFBINDGRP | - | - | - | - | - | - | - | Y | Y | Y | - |
| STATICADDRPARA（静态 IP 段绑定 UPF） | - | - | - | - | - | - | - | Y | - | - | - |
| BLACKLIST（静态地址黑名单） | - | - | - | - | - | - | - | Y | - | - | - |

### C.2 隧道类配置对象复用矩阵

| 配置对象 | IPFD-015002 GRE | IPFD-015004/016000 IPSec | GWFD-020411 MPLS | GWFD-020412 L2TP(U) | WSFD-104410 L2TP(C) | GWFD-010107 静态冗余 |
|---------|-----------------|----------------------------|------------------|---------------------|---------------------|----------------------|
| GRETUNNEL | Y | Y（GRE over IPSec） | - | - | - | Y |
| Tunnel 接口（ADD INTERFACE） | Y | Y | - | - | - | Y |
| LoopBack 接口 | Y | Y | - | - | - | - |
| SRROUTE / SRROUTE6 | Y | Y | - | Y | - | Y |
| IPSECPROPOSALIPSEC | - | Y | - | - | - | - |
| IKEPROPOSAL / IKEPEER | - | Y | - | - | - | - |
| IPSECPOLICY | - | Y | - | - | - | - |
| IPSECINTFCFGIPSEC | - | Y | - | - | - | - |
| ACLGROUPIPSEC / ACLRULEADV4IPSEC | - | Y | - | - | - | - |
| VPNINSTANCE / BGPVPNV4PEER（★推导） | - | - | Y（需补全） | - | - | - |
| APNL2TPATTR（U 面） | - | - | - | Y | - | - |
| APNL2TPCTRL（C 面） | - | - | - | - | Y | - |
| L2TPGROUP / L2TPLNSINFO | - | - | - | Y | - | - |
| L2TPCLIENTIP / L2TPRDSCLIENT | - | - | - | Y | - | - |
| PPPCFG / APNPPPACCESS | - | - | - | Y | - | - |
| GLOBALL2TP | - | - | - | Y | - | - |
| L2TPN4KEY（U）/ L2TPKEY（C） | - | - | - | Y | Y | - |
| REDUNDRDTIP | - | - | - | - | - | Y |
| REDUNDUSER | - | - | - | - | - | Y（U+C 共用） |
| APNREDUNDUPSW | - | - | - | - | - | Y（U） |

### C.3 鉴权/Radius/接入控制/网元选择配置对象复用矩阵

| 配置对象 | WSFD-010301 | WSFD-011305 | WSFD-011306 | WSFD-011307 | WSFD-108007 | WSFD-106003 | WSFD-106203 | WSFD-107010 | GWFD-010151 |
|---------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| APNAUTHATTR（ACCESSMODE） | Y（共用） | Y | - | - | - | - | - | - | - |
| RDSSVRGRP（Radius 服务器组） | - | Y（依赖） | Y | Y（共享） | - | - | - | - | - |
| RDSSVR / APNRDSSVRGRP | - | Y（依赖） | Y | Y | - | - | - | - | - |
| APNRDSCLIENTIP | - | - | Y | - | - | - | - | - | - |
| APNRDSACCTCTRL / APNRADIUSATTR | - | - | Y | - | - | - | - | - | - |
| UPLIST4RDS | - | - | Y | Y | Y | - | - | - | - |
| CPGTPUADDR | - | - | - | - | Y | - | - | - | - |
| RDSUPFCTRL / UPFRDSSVR / UPFRDSCLIENTIP | - | - | - | - | Y | - | - | - | - |
| NETWORKINSTVPNMAP（UPF 前置） | - | - | - | - | Y | - | - | - | - |
| FHBYPASS | - | - | Y | - | - | - | - | - | - |
| GBAUTHCIPH / IUAUTHCIPH（AKA 2/3G） | Y | - | - | - | - | Y（子特性 B 卡类型依赖） | - | - | - |
| S1USRSECPARA（AKA 4G） | Y | - | - | - | - | - | - | - | - |
| NGUSRSECPARA（AKA 5G） | Y | - | - | - | - | - | - | - | - |
| GBARD / IUARD / S1ARD（2/3/4G ARD） | - | - | - | - | - | Y（子特性 B） | - | - | - |
| NGMMSUBDATA（5GC 移动性限制） | - | - | - | - | - | Y（子特性 A） | - | - | - |
| NGMMPROCTRL | - | - | - | - | - | Y | - | - | - |
| APNALIAS（GGSN/PGW-C/SMF） | - | - | - | - | - | - | Y | - | - |
| ALIASAPN（SGSN/MME） | - | - | - | - | - | - | Y | - | - |
| APNREPORTATTR / DEACTIVERATE | - | - | - | - | - | - | Y | - | - |
| APNACTNUM（单 APN 并发限制） | - | - | - | - | - | - | - | - | - |
| PNFDNN / PNFNS / PNFDNAI / PNFUPFINFO | - | - | - | - | - | - | - | Y | - |
| UPAREA / UPAREABINDN2TAI / LOCBINDAREA | - | - | - | - | - | - | - | Y | - |
| UPBINDS11 / UPBINDGNGP | - | - | - | - | - | - | - | Y | - |
| UPSELECTPRI / UPSELECTFLAG / APNUPSELPLY / UPLOADBALANCE | - | - | - | - | - | - | - | Y | - |
| AREADNS / DNSN / SGSNDNS | - | - | - | - | - | - | - | -（属 WSFD-010202） | - |
| APNQOSATTR（CARSHAPESWUL/DL） | - | - | - | - | - | - | - | - | Y |

### C.4 配置对象统计

| 统计项 | 数量 |
|--------|------|
| 地址分配域核心 ConfigObject | **~20**（POOL/ADDRPOOL 双侧 + SECTION/POOLGROUP 系列 + APN + 规则开关） |
| 隧道类 ConfigObject | **~22**（GRETUNNEL + IPSec 8 件套 + L2TP U/C 双侧 + MPLS VPN 推导） |
| 鉴权/Radius/接入控制/网元选择 ConfigObject | **~28**（APNAUTHATTR + RDSSVRGRP 系列 + ARD 三代 + NGMMSUBDATA + UPF 选择 11 件套） |
| 会话管理/底座 ConfigObject | **~6**（APNACTNUM + PDPAPN + SMSUBDATA + SDBTMR + 会话查询运维） |
| **合计独立 ConfigObject（去重）** | **~65** |

### C.5 关键复用观察

1. **POOL（UDG）vs ADDRPOOL（UNC）命令前缀不对称** —— Stage 4 ConfigObject 必须分离建模（C.1 矩阵清晰呈现）
2. **ADD APN 是跨域共用挂载点** —— 地址分配 + 接入控制（U 侧 APNQOSATTR 挂 APN）+ 鉴权（C 侧 APNAUTHATTR/APNL2TPCTRL 挂 APN）+ 别名 APN 均依赖
3. **RDSSVRGRP 是 Radius 三件套共享对象** —— WSFD-011306/011305/011307 共享，证明 011307 是 011306 的并行扩展（parallel_extends）
4. **UPNODE 是网元选择+地址分配共用对象** —— WSFD-107010 用位置特征/分流能力参数，WSFD-010502 用 ADDRALLOCMODE=INHERIT
5. **APNL2TPATTR（U，10+ 参数）vs APNL2TPCTRL（C，2 参数）** —— C 决策 U 执行模式的典型不对称
6. **GRETUNNEL 跨 3 特性共用** —— IPFD-015002 GRE + IPFD-015004 GRE over IPSec + GWFD-010107 静态路由冗余（主备 UDG 间 GRE Tunnel）

---

## 附录 D: 典型端到端配置流程

> **★ Stage 4 TaskCommandOrderEdge 数据源**。每个流程含命令顺序（有序步骤），供 ConfigTask→MMLCommand 时序边。`source_evidence_ids` 占位 `EV-CA-01`。

### D.1 UPF 本地地址分配全流程（UDG 侧，基于 APN/DNN）

> 涉及特性：GWFD-010105。基于 [GWFD-010105 §2.2 激活步骤骨架]。

```
步骤 1: VPN 实例准备
  ├── ADD L3VPNINST:VRFNAME="VPN_Internet"
  └── ADD VPNINSTAF:VRFNAME="VPN_Internet",AFTYPE=ipv4uni

步骤 2: APN 配置
  ├── ADD APN:APN="apn-test",HASVPN=ENABLE,VPNINSTANCE="VPN_Internet"
  └── SET APNADDRESSATTR:APN="apn-test",SUPPORTIPV4=ENABLE,SUPPORTIPV6=DISABLE

步骤 3: 地址池配置（★POOLTYPE=LOCAL）
  ├── ADD POOL:POOLNAME="testpool",POOLTYPE=LOCAL,IPVERSION=IPV4,HASVPN=ENABLE,VPNINSTANCE="VPN_Internet"
  ├── ADD SECTION:POOLNAME="testpool",SECTIONNUM=0,IPVERSION=IPV4,V4STARTIP="10.10.1.1",V4ENDIP="10.10.1.254"
  ├── ADD POOLGROUP:POOLGRPNAME="poolgroup1",IPV4ALLOCPRIALG=ENABLE
  └── ADD POOLBINDGROUP:POOLGROUPNAME="poolgroup1",POOLNAME="testpool",PRIORITY=10

步骤 4: 池组映射（基于 APN/DNN 子方式）
  └── ADD POOLGRPMAP:MAPPINGNAME="map1",APN="apn-test",POOLGROUPNAME="poolgroup1"

步骤 5: 地址分配规则（全局三级）
  └── SET IPALLOCRULE:FIRSTRULESW=ENABLE,FIRSTRULE=APN,SECONDRULESW=DISABLE,THIRDRULESW=DISABLE

步骤 6: 下行路由发布（IPv4 OSPF + WLR 引入）
  ├── ADD OSPF:PROCID=100,ROUTERID="10.10.10.1",VRFNAME="VPN_Internet"
  ├── ADD OSPFAREA:PROCID=100,AREAID="0.0.0.1"
  ├── ADD OSPFNETWORK:PROCID=100,AREAID="0.0.0.1",...
  └── ADD OSPFIMPORTROUTE:PROCID=100,PROTOCOL=wlr
```

**关键约束**：UDG 侧 POOLTYPE 必须为 LOCAL（非 EXTERNAL）；APN 的 VPN 与地址池的 VPN 必须一致。

### D.2 IPv4v6 双栈配置全流程（UDG 侧）

> 涉及特性：GWFD-020403（能力使能层）+ GWFD-010105（机制层）+ GWFD-020401（IPv6 承载）。基于 [GWFD-020403 §4.1]。

```
步骤 1: License 使能（★双栈必须）
  ├── SET LICENSESWITCH:LICITEM="LKV3G5V6PB01",SWITCH=ENABLE   (IPv6 承载底座)
  └── SET LICENSESWITCH:LICITEM="LKV3G5VDSA01",SWITCH=ENABLE   (双栈能力使能层)

步骤 2: VPN 双实例（IPv4 + IPv6）
  ├── ADD VPNINST / ADD L3VPNINST（IPv4 VPN）
  └── ADD VPNINSTAF:AFTYPE=ipv6uni ★（IPv6 地址族激活）

步骤 3: 双栈 APN（HASVPN + HASVPNIPV6 双绑定）
  └── ADD APN:APN="apn-ds",HASVPN=ENABLE,VPNINSTANCE="vpn_v4",HASVPNIPV6=ENABLE,VPNINSTANCEIPV6="vpn_v6"

步骤 4: 双池双段（IPv4 池 + IPv6 池并存）
  ├── ADD POOL:POOLNAME="pool_v4",IPVERSION=IPV4,...
  ├── ADD POOL:POOLNAME="pool_v6",IPVERSION=IPV6,...
  ├── ADD SECTION（IPv4 段）
  └── ADD SECTION（IPv6 段，V6PREFIXSTART/V6PREFIXEND/V6PREFIXLENGTH=64）

步骤 5: 双池绑定到同一组（双优先级算法使能）
  ├── ADD POOLGROUP:POOLGRPNAME="pg_ds",IPV4ALLOCPRIALG=ENABLE,IPV6ALLOCPRIALG=ENABLE
  ├── ADD POOLBINDGROUP:POOLGROUPNAME="pg_ds",POOLNAME="pool_v4",PRIORITY=10
  └── ADD POOLBINDGROUP:POOLGROUPNAME="pg_ds",POOLNAME="pool_v6",PRIORITY=10

步骤 6: APN 级双栈属性
  └── SET APNADDRESSATTR:APN="apn-ds",SUPPORTIPV4=ENABLE,SUPPORTIPV6=ENABLE

步骤 7: 池组映射
  └── ADD POOLGRPMAP:MAPPINGNAME="map_ds",APN="apn-ds",POOLGROUPNAME="pg_ds"

步骤 8: 下行路由发布（OSPF + OSPFv3 双进程）
  ├── ADD OSPF + ADD OSPFIMPORTROUTE PROTOCOL=wlr（IPv4）
  └── ADD OSPFV3 + ADD OSPFV3IMPORTROUTE PROTOCOL=wlr（IPv6，★020401 提供）

步骤 9: RA 通告（★020403 独有，010105 未涉及）
  └── UDG 主动下发 Router Advertisement（由 License LKV3G5VDSA01 使能）
```

**关键约束**：V6PREFIXLENGTH=64 是普通 IPv6 单栈地址分配；<64 切换为 IPv6 Prefix Delegation 模式（GWFD-020406）。

### D.3 L2TP-VPN 端到端配置流程（C 决策 U 执行，C-U 不对称）

> 涉及特性：WSFD-104410（C 决策）+ GWFD-020412（U 执行）。基于 [GWFD-020412 §4]、[WSFD-104410 §4]。

```
===== UNC 侧（C 面决策，无 License）=====

步骤 C1: License（C 侧无 License 要求）

步骤 C2: APN 使能 L2TP（★APNL2TPCTRL 仅 2 参数）
  └── SET APNL2TPCTRL:APN="apn-l2tp",L2TPSWITCH=ENABLE

步骤 C3: N4 接口加密（可选，与 UDG L2TPN4KEY 相同）
  └── SET L2TPKEY:KEY="shared_secret"

步骤 C4: PFCP 私有扩展（下发 LNS 参数经 N4）
  └── SET PFCPPVTEXT:...


===== UDG 侧（U 面 LAC 执行，必须 License 82200BVC）=====

步骤 U1: License 使能
  └── SET LICENSESWITCH:LICITEM="LKV3G5L2TP01",SWITCH=ENABLE

步骤 U2: VPN + Giif 接口
  ├── ADD VPNINST
  ├── ADD LOGICINF:IFNAME="giif1/0/0"
  └── ADD APN:APN="apn-l2tp"

步骤 U3: ★APN L2TP 属性（U 面核心，10+ 参数）
  └── SET APNL2TPATTR:APN="apn-l2tp",L2TPSWITCH=ENABLE,SUPPORTIPV6=DISABLE,...

步骤 U4: 本地配置方式 - L2TP 组（LNS 容器）
  ├── ADD L2TPGROUP:L2TPGROUPID=1,DOMAINNAME="...",LNSIP="x.x.x.x",...
  └── ADD L2TPCLIENTIP:L2TPGROUPID=1,INTFNAME="giif1/0/0"

步骤 U4 替代: AAA 下发方式 - Radius LNS
  └── ADD L2TPRDSCLIENT:APN="apn-l2tp",INTFNAME="giif1/0/0",RDSLNSMODE=...

步骤 U5: L2TP 缺省属性 + PPP 协商
  ├── SET GLOBALL2TP:...
  ├── SET PPPCFG:...
  └── SET APNPPPACCESS:APN="apn-l2tp",...

步骤 U6: N4 接口加密（可选，与 UNC L2TPKEY 相同）
  └── SET L2TPN4KEY:KEY="shared_secret"

步骤 U7: 静态路由（引导流量）
  └── ADD SRROUTE:IFNAME="giif1/0/0",...
```

**关键约束**：APNL2TPATTR（U，10+ 参数）≠ APNL2TPCTRL（C，2 参数）；与 GWFD-010108/020482 互斥；不支持 PPP 用户/DHCP 延迟分配/IPv6 PD/NAT。

### D.4 IPSec 隧道配置流程（VNRS 微服务 + IPsec 微服务双配）

> 涉及特性：IPFD-015004（UDG）/ IPFD-016000（UNC），对称同构。基于 [IPFD-015004 §4]。

```
步骤 1: VNRS 微服务 VPN 配置（用户面侧）
  ├── ADD L3VPNINST:VRFNAME="vpn_ipsec"
  ├── ADD VPNINSTAF:VRFNAME="vpn_ipsec",AFTYPE=...
  ├── ADD IPBINDVPN（物理接口绑定 VPN）
  ├── ADD IFIPV4ADDRESS（物理接口 IP）
  └── ADD SRROUTE（静态路由）

步骤 2: VNRS 微服务 IPsec 隧道接口
  ├── ADD INTERFACE:IFNAME="Tunnel1"
  ├── ADD IPSECINTFCFG:IFNAME="Tunnel1",TNLTYPE=IPSEC
  ├── ADD IPBINDVPN（Tunnel 绑定 VPN）
  └── ADD IFIPV4ADDRESS（Tunnel 接口 IP）

步骤 3: IPsec 微服务镜像配置
  ├── ADD L3VPNINSTIPSEC / ADD VPNINSTAFIPSEC
  ├── ADD INTERFACEIPSEC
  ├── ADD IPBINDVPNIPSEC
  └── ADD IFIPV4ADDRESSIPSEC

步骤 4: ACL 规则（定义保护数据流，★仅源/目的 IP）
  ├── ADD ACLGROUPIPSEC:ACLGROUPNAME="acl_ipsec"
  └── ADD ACLRULEADV4IPSEC:ACLGROUPNAME="acl_ipsec",SRCIP="...",DSTIP="..."

步骤 5: 安全提议（封装+协议+算法）
  └── ADD IPSECPROPOSALIPSEC:PROPOSALNAME="prop1",ENCAPSULATIONMODE=TUNNEL,SECURITYPROTOCOL=ESP,...

步骤 6: IKE 提议 + 对等体（★DH 组不能为 None）
  ├── ADD IKEPROPOSAL:PROPOSALNAME="ike_prop1",AUTHMETHOD=PSK,DHGROUP=...,...
  └── ADD IKEPEER:PEERNAME="peer1",PRESHAREDKEY="...",EXCHANGEMODE=MAIN,REMOTEADDR="...",NATTRAVERSAL=...

步骤 7: 安全策略（聚合 ACL+Proposal+IKE Peer）
  ├── ADD IPSECPOLICY:POLICYNAME="policy1",SEQ=10,MODE=ISAKMP,ACLGROUPNAME="acl_ipsec"
  ├── ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="policy1",SEQ=10,PROPOSALNAME="prop1"
  └── ADD ATTACHIKEPEER:POLICYNAME="policy1",SEQ=10,PEERNAME="peer1",PRIORITY=10

步骤 8: 应用策略到 Tunnel 接口
  └── ADD IPSECINTFCFGIPSEC:IFNAME="Tunnel1",TNLTYPE=IPSEC,POLICYNAME="policy1"

步骤 9: IKE 全局配置（DPD + NAT 保活）
  └── SET IKEGLOBALCONFIG:DPDTYPE=...,DPDINTERVAL=...,NATKLI=...
```

**关键约束**：DH 组不能为 None；NAT 穿越仅 ESP 隧道模式；默认 IKEv2（IKEv1 需 MOD IKEPEER VERSION1=FALSE 关闭）；ACL 仅支持源/目的 IP 不支持端口。

### D.5 GRE 隧道配置流程（对称同构，含 GRE over IPSec 场景）

> 涉及特性：IPFD-015002（U+C 同构）。基于 [IPFD-015002 §4]。

```
步骤 1: LoopBack 接口（推荐隧道源）
  ├── ADD INTERFACE:IFNAME="LoopBack1"
  └── ADD IFIPV4ADDRESS:IFNAME="LoopBack1",IFIPADDR="10.3.3.11",SUBNETMASK="255.255.255.255"

步骤 2: ★GRE 隧道（核心）
  └── ADD GRETUNNEL:TNLNAME="Tunnel1",TNLTYPE=gre,SRCTYPE=if_name,SRCIFNAME="LoopBack1",DSTIPADDR="10.4.4.11"

步骤 3: Tunnel 接口 IP
  └── ADD IFIPV4ADDRESS:IFNAME="Tunnel1",IFIPADDR="10.10.1.201",SUBNETMASK="255.255.255.0"

步骤 4: 静态路由（引导流量进 Tunnel）
  └── ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.10.1.202",MASKLENGTH=24,IFNAME="Tunnel1"

步骤 5: 可选特性（MOD GRETUNNEL）
  ├── MOD GRETUNNEL:TNLNAME="Tunnel1",TNLTYPE=gre,CHECKSUMEN=TRUE   (Checksum)
  ├── MOD GRETUNNEL:TNLNAME="Tunnel1",TNLTYPE=gre,GREKEYEN=TRUE,GREKEY="123"   (Key)
  └── MOD GRETUNNEL:TNLNAME="Tunnel1",TNLTYPE=gre,KEEPALVEN=TRUE,KEEPALVPERIOD=5,KEEPALVRETRYCNT=3   (Keepalive)

步骤 6: GRE over IPSec 场景（弥补 IPSec 不支持组播）
  ├── 先建立 GRE 隧道（封装组播/广播报文）
  ├── 再引入 IPSec 加密（叠加 D.4 IPSec 配置）
  └── ★硬约束：GRE 隧道源地址不能与 IPSec 隧道源地址相同（FR-GRE-IPSEC-SRC-EXCL）
```

### D.6 Radius 鉴权配置流程（鉴权级联链）

> 涉及特性：WSFD-011306（Radius 功能）→ WSFD-011305（鉴权接入）→ WSFD-108007（二次鉴权，可选）→ WSFD-011307（抄送，可选）。基于 [WSFD-011306 §4]、[WSFD-011305 §4]、[WSFD-108007 §3]。

```
===== 前置：Radius 功能（WSFD-011306）=====

步骤 R1: VPN + Gi 接口
  ├── ADD L3VPNINST / ADD VPNINSTAF（AAA VPN）
  ├── ADD VPNINST
  ├── ADD LOGICIP + ADD LOGICINF（giif1/0/0 鉴权 AAA / giif1/0/1 计费 AAA，绑定 vpn_aaa）
  └── ADD APN:APN="huawei.com"

步骤 R2: ★Radius 服务器组 + 服务器
  ├── ADD RDSSVRGRP:RDSSVRGRPNAME="isprg"
  └── ADD RDSSVR:RDSSVRGRPNAME="isprg",SERVERTYPE=AUTHENTICATION,PRIFLAG=PRIMARY,PRIORITY=1,...

步骤 R3: APN 级 Radius 绑定
  ├── ADD APNRDSSVRGRP:APN="huawei.com",RDSSVRGRPNAME="isprg"
  ├── ADD APNRDSCLIENTIP:APN="huawei.com",INTFNAME="giif1/0/0",CLIENTTYPE=AUTHENTICATION
  └── ADD APNRDSCLIENTIP:APN="huawei.com",INTFNAME="giif1/0/1",CLIENTTYPE=ACCOUNTING

步骤 R4: Radius 计费控制 + 域名
  ├── SET APNRDSACCTCTRL:APN="huawei.com",SRVTRIGGER=...,SUPPORTACCTRSP=ENABLE
  └── SET APNRADIUSATTR:APN="huawei.com",...


===== 主流程：鉴权接入（WSFD-011305）=====

步骤 A1: ★APN 鉴权属性（ACCESSMODE 4 种取值）
  ├── 透明接入：SET APNAUTHATTR:APN="huawei.com",ACCESSMODE=TRANS_NON_AUTH
  ├── 透明鉴权：SET APNAUTHATTR:APN="huawei.com",ACCESSMODE=TRANS_AUTH,COMMONUSERNAME="huawei123",COMMONUSERPASS="123",CFMCOMMUSERPASS="123"
  ├── 非透明接入：SET APNAUTHATTR:APN="huawei.com",ACCESSMODE=NON_TRANS,...
  └── 本地鉴权：SET APNAUTHATTR:APN="huawei.com",ACCESSMODE=LOC_AUTH,...

步骤 A2: 验证
  └── LST APNAUTHATTR:APN="huawei.com"


===== 扩展 1：终端二次鉴权（WSFD-108007，企业 DN 场景）=====

步骤 S1: License
  └── SET LICENSESWITCH:LICITEM="LKV2SECAA01",SWITCH=ENABLE

步骤 S2: UPF 侧 VPN 前置（★必须先于 UPFRDSSVR/CLIENTIP）
  └── ADD NETWORKINSTVPNMAP（UPF 侧执行）

步骤 S3: GTP-U 地址 + UP List
  ├── ADD CPGTPUADDR:IPVERSION=IPV4,IPV4ADDR="192.168.0.20"
  └── ADD UPLIST4RDS:UPLISTNAME="uplist1",UPINSTANCEID="up1"

步骤 S4: UPF Radius 控制
  └── ADD RDSUPFCTRL:UPLISTNAME="uplist1",UPINSTANCEID="up1",PREFERENCE=1,LOCKED=ENABLE

步骤 S5: ★UPF Radius 服务器（DN-AAA，必须先于 CLIENTIP）
  └── ADD UPFRDSSVR:SERVERTYPE=AUTHENTICATION,IPVERSION=IPV4,SERVERIPV4="192.168.10.2",UPLISTNAME="uplist1"

步骤 S6: ★UPF Radius 客户端 IP（必须最后执行，执行后 SMF 立即触发建链）
  └── ADD UPFRDSCLIENTIP:CLIENTYPE=AUTHENTICATION,IPVERSION=IPV4,UPLISTNAME="uplist1",VPNINSTANCE="vpnInstance1",CLIENTIPV4="192.168.10.1"


===== 扩展 2：Radius 抄送（WSFD-011307，并行扩展，共享配置对象）=====

步骤 C1: 共享 RDSSVRGRP（复用 R2）
步骤 C2: 抄送服务器组
  └── ADD APNRDSSVRGRP:APN="huawei.com",RDSSVRGRPNAME="cc_rg",PRIFLAG=CARBON_COPY
```

**关键约束**：仅 TRANS_AUTH/NON_TRANS 强依赖 Radius 功能；TRANS_NON_AUTH/LOC_AUTH 不调用 Radius；二次鉴权不支持 EAP/Diameter，仅 PAP/CHAP via Radius；直连 AAA 与经 UPF 中转 AAA 的 Radius Server IP 不可相同。

### D.7 UPF 选择配置流程（WSFD-107010，三轮筛选）

> 涉及特性：WSFD-107010。基于 [WSFD-107010 §3.1]。文档缺口：无完整 MML 脚本，以下基于三轮筛选机制推导。

```
步骤 1: UPF NF 实例基础（第一轮筛选输入）
  └── ADD PNFPROFILE:NFINSTANCENAME="upf1",NFTYPE=UPF,WEIGHT=100,PRIORITY=10

步骤 2: UPF 属性配置（第一轮必选条件 7 项）
  ├── ADD PNFDNN:NFINSTANCENAME="upf1",DNN="internet"
  ├── ADD PNFNS:NFINSTANCENAME="upf1",SST=1,SD=1   (★4G 接入 PNFNSINDEX 保持默认 0)
  ├── ADD PNFDNAI:NFINSTANCENAME="upf1",DNAI="..."
  ├── ADD PNFUPFINFO:NFINSTANCENAME="upf1",EPSFUPPORTED=ENABLE
  ├── ADD UPNODE:NFINSTANCENAME="upf1",...   (位置特征+分流能力)
  ├── ADD UPAREA / ADD UPAREABINDN2TAI / ADD LOCBINDAREA
  └── ADD PNFSMFSERAREA / ADD PNFTAIRANGE / ADD PNFTAI

步骤 3: 接口绑定（4G 互操作）
  ├── ADD UPBINDS11（SGW-U 与 S11）
  └── ADD UPBINDGNGP（GGSN/PGW-U 与 Gn/Gp）

步骤 4: 第二轮优选条件（策略次序）
  ├── SET UPSELECTPRI:FIRSTPRIORITY=COMBINED,SECONDPRIORITY=LOCS11PRIORITY
  ├── SET UPSELECTFLAG:PRIORITYFLAG=DISABLE,AMBRUPFFLAG=...,N3UPFAPNFLAG=...,ULISGWFLAG=...
  └── SET APNUPSELPLY:APN="internet",COMBINEPRISTG=...

步骤 5: 第三轮权重 + 负载最终选择
  └── SET UPLOADBALANCE:SWITCH=ENABLE   (UNC 处理 UPF 上报负载信息)
```

**关键约束**：SMF 和 UPF 必须同时为 HUAWEI 设备（FR-APF-同厂商约束）；4G 接入不用切片（PNFNSINDEX=0）；第一轮 7 必选条件全满足无优先级。

### D.8 接入控制配置流程（U 侧带宽流控 + C 侧接入权限，非对称）

> 涉及特性：GWFD-010151（U 侧）+ WSFD-106003（C 侧，双特性合一）。基于 [GWFD-010151 §4]、[WSFD-106003 §3]。

```
===== U 侧：带宽流控（GWFD-010151，无 License）=====

步骤 U1: APN 实例
  └── ADD APN:APN="apn_bw"

步骤 U2: ★APN QoS 属性（接入控制核心，上下行独立）
  └── SET APNQOSATTR:APN="apn_bw",CARSHAPESWUL=ENABLE,CARSHAPEUL=CAR,CARSHAPESWDL=ENABLE,CARSHAPEDL=CAR
      (上下行可分别选 CAR 直接丢弃 / SHAPE 缓存整形)

步骤 U3: 验证
  └── LST APNQOSATTR:APN="apn_bw"


===== C 侧 子特性 A：AMF 移动性限制（5GC，无 License）=====

步骤 CA1: 5GC 接入限制（★NGMMSUBDATA）
  └── ADD NGMMSUBDATA:USER_RANGE=...,IMSIPRE=...,RATRESTRICT=...,CORERESTRICT=...


===== C 侧 子特性 B：SGSN/MME ARD 权限（2/3/4G，需 License 82206571）=====

步骤 CB1: License
  └── SET LICENSESWITCH:LICITEM="LKV2ARD02",SWITCH=ENABLE

步骤 CB2: ★ARD 接入限制（按代际：GBARD 2G/IUARD 3G/S1ARD 4G）
  ├── ADD GBARD:IMSI="...",APNNI="...",CARDTYPE=SIM,ARD=...,CTRLTYPE=ALLOW,CAUSE=...
  ├── ADD IUARD:...
  └── ADD S1ARD:...

步骤 CB3: 卡类型控制前置（★强依赖 WSFD-010301 鉴权功能）
  └── 必须先启用 WSFD-010301（通过鉴权三元组/五元组区分 SIM/USIM）
```

**关键约束**：U 侧配置粒度仅 APN（无法针对单用户）；C 侧本地配置优先于签约；紧急注册跳过；卡类型控制必须先启用 WSFD-010301。

### D.9 别名 APN 配置流程（WSFD-106203，双视角语义反转）

> 涉及特性：WSFD-106203（拆分为两个 Feature 变体）。基于 [WSFD-106203 §4]。

```
===== SGSN/MME 侧（协商 APN→别名 APN，DNS 屏蔽，License LKV2ALIASAPN02）=====

步骤 S1: License
  └── SET LICENSESWITCH:LICITEM="LKV2ALIASAPN02",SWITCH=ENABLE

步骤 S2: ★别名 APN 映射（双条件：IMSI 号段 AND 协商 APN）
  └── ADD ALIASAPN:IMSI_PREFIX="1234",OLDAPN="internet",NEWAPN="alias.internet"


===== GGSN/PGW-C/SMF 侧（别名 APN→真实 APN，资源归一，License LKV2AAPN01）=====

步骤 G1: License
  └── SET LICENSESWITCH:LICITEM="LKV2AAPN01",SWITCH=ENABLE

步骤 G2: APN 前置（转换后 APN 必须已 ADD APN）
  └── ADD APN:APN="real.internet"

步骤 G3: ★别名 APN 映射（5G 先按切片 SST+SD 查，未中再按 ALL_USER）
  └── ADD APNALIAS:SUBRANGE=ALL_USER,ALIASAPN="alias.internet",CONVERTAPN="real.internet",SST=1,SD=1

步骤 G4: 报告属性
  └── SET APNREPORTATTR:...
```

**关键约束**：用户携带错误 APN 时先 APN 纠错（WSFD-106004）再别名转换；SGSN/MME 侧 HLR 无需签约；GGSN/PGW-C/SMF 侧转换后 APN 必须已 ADD APN。

### D.10 端到端流程统计

| 流程编号 | 流程名称 | 涉及特性数 | 命令步骤数 | source_evidence_ids |
|----------|----------|------------|------------|---------------------|
| D.1 | UPF 本地地址分配全流程（UDG） | 1（GWFD-010105） | 6 | EV-CA-01 |
| D.2 | IPv4v6 双栈配置全流程（UDG） | 3（020403+010105+020401） | 9 | EV-CA-01 |
| D.3 | L2TP-VPN 端到端（C 决策 U 执行） | 2（WSFD-104410+GWFD-020412） | C4+U7=11 | EV-CA-01 |
| D.4 | IPSec 隧道配置（VNRS+IPsec 双配） | 2（IPFD-015004/016000） | 9 | EV-CA-01 |
| D.5 | GRE 隧道配置（含 GRE over IPSec） | 1（IPFD-015002） | 6 | EV-CA-01 |
| D.6 | Radius 鉴权配置（级联链） | 4（011306→011305→108007→011307） | R4+A2+S6+C2=14 | EV-CA-01 |
| D.7 | UPF 选择配置（三轮筛选） | 1（WSFD-107010） | 5 | EV-CA-01 |
| D.8 | 接入控制配置（U+C 非对称） | 3（GWFD-010151+WSFD-106003 A/B） | U3+CA1+CB3=7 | EV-CA-01 |
| D.9 | 别名 APN 配置（双视角反转） | 1（WSFD-106203，双变体） | S2+G4=6 | EV-CA-01 |
| **合计** | **9 个端到端流程** | - | **~73 步** | EV-CA-01 |

---

## 附录 E: 版本与计数统计汇总（供 Stage 4 直接引用）

| 类别 | 计数 | 明细 |
|------|------|------|
| **特性总数** | **37** | UDG 16 + UNC 21 |
| **feature_group 分类** | **6 大类** | APN 基础 5 + 地址分配 18 + 鉴权计费 5 + 接入方式 5 + 网元选择 2 + 接入控制 2 |
| **C-U 配对特性** | **8 对** | 决策执行分离 5（会话/地址/IPv6 承载/IPv6 PD/静态冗余）+ 对称同构 4（含共享特性）+ 非对称 2（接入控制/L2TP） |
| **需 License 特性** | **13** | IPv6 三件套（UDG+UNC）+ 基于位置 + MPLS（U+C）+ L2TP U + 二次鉴权 + ARD B + UPF 选择（双）+ 别名 APN（双） |
| **MML 命令条目（附录 B）** | **~140** | UDG ~62 + UNC ~78（含跨产品共用双计数） |
| **独立 ConfigObject（附录 C）** | **~65** | 地址分配 ~20 + 隧道 ~22 + 鉴权/控制/选择 ~28 + 底座 ~6 |
| **端到端配置流程（附录 D）** | **9** | 地址分配/双栈/L2TP/IPSec/GRE/Radius/UPF 选择/接入控制/别名 APN |
| **配置树修正** | **11 处** | 引用《归纳-配置树修正》§1 |
| **依赖声明矛盾** | **8 对** | 引用《归纳-配置树修正》§3 |
| **互斥关系** | **3 对** | LOC-L2TP / L2TP-ADDRAUTO / GRE-IPSec 源地址 |
| **待解决问题（Stage 4 验证）** | **12 个** | 引用《归纳-配置树修正》§5 |

---

**文档版本**：v1.0（Stage 3 跨特性横向分析）
**完成时间**：2026-06-22
**上游来源**：37 篇 feature-knowledge（§配置/§配置对象/§与其他特性关系/§8 一致性）+ 4 篇 topic-knowledge（归纳-配置树修正 / 归纳-四维度 / 归纳-APN底座 / Batch-14 业务场景方案）
**下游消费者**：Stage 4 第 2-4 层（MMLCommand 层 ← 附录 B / ConfigObject 层 ← 附录 C / ConfigTask + TaskCommandOrderEdge ← 附录 D）
**Evidence 占位**：全文件 `EV-CA-01`（Stage 5 实例化时映射到各 feature-knowledge 的 `EV-FK-xx`）
