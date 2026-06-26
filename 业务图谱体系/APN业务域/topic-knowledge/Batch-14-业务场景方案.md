# Batch-14 业务场景方案（9方案）— 第1层 ConfigurationSolution 直接来源

> 业务域: APN(接入与会话管理)
> 本批次定位: 三层图谱第1层 ConfigurationSolution(CS-APN-01~09) 的直接归纳来源
> 配置决策维度: 地址分配方式 × 鉴权方式 × 接入方式 × 地址类型（意图澄清§配置维度澄清顺序）
> 来源证据池: feature-knowledge(37特性) + APN意图澄清知识库(§常见场景方案速查表)
> source_evidence_ids: EV-TK-14（本批次占位，按场景-方案映射条目细分 EV-TK-14-01 ~ EV-TK-14-09）
> 产出日期: 2026-06-22

---

## 0. 9场景 → ConfigurationSolution 映射摘要表

| CS ID | 业务场景 | 地址分配方式 | 鉴权方式 | 接入方式 | 地址类型 | 主特性(feature_id) |
|-------|---------|------------|---------|---------|---------|-------------------|
| CS-APN-01 | 工厂工控访问内网 | UDM 静态分配 | 不透明接入(NON_TRANS) | IPSec 隧道 | IPv4 | WSFD-010502 / IPFD-015004 / WSFD-011305 |
| CS-APN-02 | 智慧农业传感器上报 | UPF 动态(基于APN/DNN) | 透明接入(TRANS_NON_AUTH) | VPN 直连(NAT) | IPv4 | GWFD-010105 |
| CS-APN-03 | 家庭CPE宽带 | UPF 动态(基于SMF) | 透明接入(TRANS_NON_AUTH) | VPN 直连(NAT) | IPv4v6 双栈 | GWFD-010105 / GWFD-020403 |
| CS-APN-04 | VoLTE 语音业务 | SMF 动态分配 | 透明接入(TRANS_NON_AUTH) | VPN 直连 | IPv4v6 双栈 | WSFD-010502 / WSFD-010504 |
| CS-APN-05 | 企业AAA二次鉴权 | RADIUS 分配 | 不透明接入(NON_TRANS) | VPN 或 GRE | IPv4 | WSFD-011305 / WSFD-011306 / IPFD-015002 |
| CS-APN-06 | 传统企业DHCP迁移 | DHCP 分配 | 透明接入(TRANS_NON_AUTH) | VPN 直连 | IPv4 | WSFD-104413 |
| CS-APN-07 | 企业L2TP VPN | LNS 分配 | 不透明接入(NON_TRANS) | L2TP 隧道 | IPv4v6 双栈 | GWFD-020412 / WSFD-104410 |
| CS-APN-08 | 区域化运营管理 | UPF 动态(基于位置区) | 透明接入(TRANS_NON_AUTH) | VPN 直连 | IPv4 | GWFD-020421 |
| CS-APN-09 | 企业双栈 | UPF 动态(基于APN/DNN) | 透明接入(TRANS_NON_AUTH) | IPSec 隧道 | IPv4v6 双栈 | GWFD-010105 / GWFD-020403 / IPFD-015004 |

> 来源: `APN意图澄清知识库.md` §常见场景方案速查表（9场景原文列于表中）[EV-TK-14]
> 维度顺序: 地址分配 → 鉴权 → 接入 → 地址类型（§配置维度澄清顺序表）

---

## 1. CS-APN-01 工厂工控访问内网

### 1.1 业务需求与配置决策

- **业务需求**: 工厂/园区工控设备(PLC、传感器、工控终端)需固定IP访问企业内网服务器，数据经公网传输且必须加密保护，企业AAA对终端二次鉴权。[EV-TK-14-01]
  - 来源: `APN意图澄清知识库.md` §场景1 + §速查表第1行

- **配置决策（4维度）**:
  | 维度 | 决策 | 依据 |
  |------|------|------|
  | 地址分配 | **UDM 静态分配** | 企业设备需固定IP便于识别管理；IP地址在 HSS/UDM 签约时确定（§一1.3 详细决策矩阵） |
  | 鉴权方式 | **不透明接入 NON_TRANS** | 企业 AAA 二次鉴权；用户通过 PCO 携带用户名密码，AAA 服务器鉴权 |
  | 接入方式 | **IPSec 隧道** | 公网传输需加密；IPSec 提供 ESP 加密 + AH/ESP 认证，安全等级最高 |
  | 地址类型 | **IPv4** | 工控设备普遍仅支持 IPv4；兼容性最优 |

### 1.2 涉及特性清单

| 网元 | feature_id | 特性名 | 角色 |
|------|-----------|--------|------|
| UNC(SMF/PGW-C) | **WSFD-010502** | 地址分配方式 | UDM 静态分配配置（POOLTYPE=UDM） |
| UDG(UPF) | GWFD-010104 | 地址分配方式 | 外部地址分配 + 白名单检测（POOLTYPE=EXTERNAL + CHECKIPVALID=ENABLE） |
| UDG(UPF) | **IPFD-015004** | IPSec 功能 | 用户面 IPSec 隧道加密（AH/ESP，IKEv2） |
| UNC(SMF) | IPFD-016000 | IPSec 功能 | C 面对称 IPSec（可选，用于 C 面网管通道加密） |
| UNC(SMF) | **WSFD-011305** | Radius 鉴权接入 | ACCESSMODE=NON_TRANS（不透明接入决策） |
| UNC(SMF) | WSFD-011306 | Radius 功能 | NON_TRANS 必须开启（依赖关系） |

### 1.3 关键MML命令序列骨架（原始MML保留）

```
// ===== UNC 侧：UDM 静态地址池 + 不透明鉴权 =====
// 来源: feature-knowledge/WSFD-010502-地址分配方式.md §5.1 [EV-FK-*]

ADD ADDRPOOL: POOLNAME="pool_industrial_udm", IPVERSION=IPv4, POOLTYPE=UDM, CHECKIPVALID=Enable;
ADD POOLBINDAPN: APN="industrial.apn", POOLNAME="pool_industrial_udm";
ADD SECTION: POOLNAME="pool_industrial_udm", SECTIONNUM=1, IPVERSION=IPv4, V4STARTIP="10.0.0.0", V4ENDIP="10.1.2.3";

ADD ADDRPOOLGRP: POOLGRPNAME="industrial_poolgrp", POOLGRPTYPE=UDM;
ADD POOLBINDGRP: POOLGRPNAME="industrial_poolgrp", POOLNAME="pool_industrial_udm";

ADD UPNODE: NFINSTANCENAME="UPF_Ind_1", ADDRALLOCMODE=INHERIT;
ADD ADDRUPGROUP: UPFGRPNAME="industrial_upfgrp", UPFGRPTYPE=UDM;
ADD UPFBINDGRP: UPFGRPNAME="industrial_upfgrp", UPFID="UPF_Ind_1";
ADD POOLGRPMAP: MAPPINGNAME="ind_mapping01", POOLGRPNAME="industrial_poolgrp", UPFGRPNAME="industrial_upfgrp";

// 鉴权属性：不透明接入（NON_TRANS）
// 来源: feature-knowledge/WSFD-011305-Radius鉴权接入.md §4.3.1
ADD APN: APN="industrial.apn";
SET APNAUTHATTR: APN="industrial.apn", ACCESSMODE=NON_TRANS;

// ===== UDG 侧：外部地址池白名单 + IPSec 隧道 =====
// 来源: feature-knowledge/GWFD-010104-地址分配方式.md §5.1 + IPFD-015004-IPSec功能.md
ADD VPNINST: VPNINSTANCE="vpn_industrial";
ADD POOLGROUP: POOLGRPNAME="poolgroup_ind_ext";
ADD POOL: POOLNAME="industrial_ext_pool", POOLTYPE=EXTERNAL, HASVPN=ENABLE, VPNINSTANCE="vpn_industrial";
ADD SECTION: POOLNAME="industrial_ext_pool", SECTIONNUM=1, IPVERSION=IPV4, V4STARTIP="10.0.0.1", V4ENDIP="10.0.0.254";
ADD POOLBINDGROUP: POOLGROUPNAME="poolgroup_ind_ext", POOLNAME="industrial_ext_pool";
ADD APN: APN="industrial.apn", HASVPN=ENABLE, VPNINSTANCE="vpn_industrial";
SET APNADDRESSATTR: APN="industrial.apn", HOSTROUTEIP=ENABLE;
ADD POOLGRPMAP: MAPPINGNAME="ind_ext_map", APN="industrial.apn", POOLGROUPNAME="poolgroup_ind_ext";

// IPSec 隧道（IKEv2 + ESP + PSK，骨架；完整参数见 IPFD-015004）
// 前置：IPSec 服务已安装、VNRS 与 IPsec 微服务双配
ADD INTERFACE: IFNAME="LoopBack1";
ADD IFIPV4ADDRESS: IFNAME="LoopBack1", IFIPADDR="10.3.3.11", SUBNETMASK="255.255.255.255", ADDRTYPE=main;
// （IPSec SA/IKE/Proposal 命令族，详见 IPFD-015004 §4 激活步骤9种场景）

// 手机下行路由（OSPF 引入 WLR）
ADD L3VPNINST: VRFNAME="vpn_industrial";
ADD VPNINSTAF: VRFNAME="vpn_industrial", AFTYPE=ipv4uni;
ADD OSPF: PROCID=100, VRFNAME="vpn_industrial", SCHEMAROUID="10.10.10.1";
ADD OSPFAREA: PROCID=100, AREAID="0.0.0.0";
ADD OSPFNETWORK: PROCID=100, AREAID="0.0.0.0", IPADDRESS="10.13.21.0", WILDCARDMASK="0.0.0.255";
ADD OSPFIMPORTROUTE: PROCID=100, TOPOID=0, PROTOCOL=wlr;
```

> 关键约束: 基于位置的地址分配与 L2TP VPN 互斥（GWFD-020421 §1.6）；IPSec 与 GRE 源地址不可相同（IPFD-015002 §1.6）。

### 1.4 对应第1层 ConfigurationSolution

- **CS-APN-01**: 配置闭包 = {UDM静态地址池@UNC, 外部地址池白名单@UDG, NON_TRANS鉴权, IPSec隧道, IPv4单栈, OSPF路由发布}
- **关联 DecisionPoint**: DP-ADDR(=UDM) × DP-AUTH(=NON_TRANS) × DP-ACCESS(=IPSec) × DP-IPTYPE(=IPv4)
- **关联 BusinessRule**: BR-固定IP需求 → UDM分配; BR-公网传输加密 → IPSec; BR-企业AAA二次鉴权 → NON_TRANS+Radius

---

## 2. CS-APN-02 智慧农业传感器上报

### 2.1 业务需求与配置决策

- **业务需求**: 电力/水务/燃气/农业大量传感器上报数据到云平台；设备仅上报不访问内网；地址自动获取；SIM卡合法即可接入。[EV-TK-14-02]
  - 来源: `APN意图澄清知识库.md` §场景2 + §速查表第2行

- **配置决策**:
  | 维度 | 决策 | 依据 |
  |------|------|------|
  | 地址分配 | **UPF 动态分配（基于 APN/DNN）** | 按 APN 业务类型管理地址池（§一1.4 三种子场景对比） |
  | 鉴权方式 | **透明接入 TRANS_NON_AUTH** | SIM 卡合法直接接入，无需 AAA |
  | 接入方式 | **VPN 直连（NAT）** | 仅上报数据，通过 NAT 转换访问 Internet |
  | 地址类型 | **IPv4** | 物联网模组普遍 IPv4，兼容性最优 |

### 2.2 涉及特性清单

| 网元 | feature_id | 特性名 | 角色 |
|------|-----------|--------|------|
| UDG(UPF) | **GWFD-010105** | 用户面地址分配 | 基于 APN/DNN 本地地址池动态分配（LOCAL 类型） |
| UDG(UPF) | GWFD-010104 | 地址分配方式 | 母特性，路由发布（OSPF） |
| UNC(SMF) | WSFD-011305 | Radius 鉴权接入 | ACCESSMODE=TRANS_NON_AUTH（不开启 Radius 功能） |

### 2.3 关键MML命令序列骨架（原始MML保留）

```
// 来源: feature-knowledge/GWFD-010105-用户面地址分配.md §5.1（基于APN/DNN分配地址完整脚本）[EV-FK-*]

// 配置 VPN 实例。
ADD L3VPNINST: VRFNAME="vpn_iot";
ADD VPNINSTAF: VRFNAME="vpn_iot", AFTYPE=ipv4uni, VRFRD=100:1;

// 基于 APN 使能地址分配属性。
ADD VPNINST: VPNINSTANCE="vpn_iot";
ADD APN: APN="iot.agri.apn", HASVPN=ENABLE, VPNINSTANCE="vpn_iot";
SET APNADDRESSATTR: APN="iot.agri.apn", SUPPORTIPV4=ENABLE, SUPPORTIPV6=DISABLE;

// 配置本地地址池（LOCAL 类型）。
ADD POOL: POOLNAME="iot_pool_v4", POOLTYPE=LOCAL, HASVPN=ENABLE, VPNINSTANCE="vpn_iot";
ADD SECTION: POOLNAME="iot_pool_v4", SECTIONNUM=1, IPVERSION=IPV4, V4STARTIP="10.20.1.1", V4ENDIP="10.20.1.254";

// 配置地址池绑定到地址池组。
ADD POOLGROUP: POOLGRPNAME="iot_poolgroup";
ADD POOLBINDGROUP: POOLGROUPNAME="iot_poolgroup", POOLNAME="iot_pool_v4";

// 配置 APN 与地址池组的映射关系（基于 APN/DNN）。
ADD POOLGRPMAP: MAPPINGNAME="iot_map", APN="iot.agri.apn", POOLGROUPNAME="iot_poolgroup";

// 配置地址分配规则（单级优先级，仅 APN 维度）。
SET IPALLOCRULE: FIRSTRULESW=ENABLE, FIRSTRULE=APN-1&LOCATION-0&SMF-0, SECONDRULESW=DISABLE, THIRDRULESW=DISABLE;

// 配置手机下行路由。
ADD OSPF: PROCID=100, VRFNAME="vpn_iot", SCHEMAROUID="10.20.20.1", LSAARRMAXINTV=1000, LSAARRSTARINTV=500, LSAARRHLDINTV=500;
ADD OSPFAREA: PROCID=100, AREAID="0.0.0.0";
ADD OSPFNETWORK: PROCID=100, AREAID="0.0.0.0", IPADDRESS="10.13.21.0", WILDCARDMASK="0.0.0.255";
ADD OSPFIMPORTROUTE: PROCID=100, TOPOID=0, PROTOCOL=wlr;

// UNC 侧：透明接入（无需 AAA）。
ADD APN: APN="iot.agri.apn";
SET APNAUTHATTR: APN="iot.agri.apn", ACCESSMODE=TRANS_NON_AUTH;
```

> 调试验证: `DSP SESSIONINFO:QUERYTYPE=IMSI,IMSI="..."` 应显示 `IPv4 Address type = UPF ALLOC IP ADDRESS`（区别于外部地址分配的 EXTERNAL ALLOC）。

### 2.4 对应第1层 ConfigurationSolution

- **CS-APN-02**: 配置闭包 = {UPF本地地址池(LOCAL)@UDG, TRANS_NON_AUTH透明接入, NAT直连, IPv4单栈, OSPF路由发布}
- **关联 DecisionPoint**: DP-ADDR(=UPF-APN) × DP-AUTH(=TRANS_NON_AUTH) × DP-ACCESS(=VPN-NAT) × DP-IPTYPE(=IPv4)
- **关联 BusinessRule**: BR-大量设备动态地址 → UPF本地池; BR-SIM鉴权足够 → 透明接入

---

## 3. CS-APN-03 家庭CPE宽带

### 3.1 业务需求与配置决策

- **业务需求**: 普通移动用户/CPE 终端/家庭网关访问 Internet；地址自动获取；通常不需要二次鉴权；需同时兼容 IPv4/IPv6 终端。[EV-TK-14-03]
  - 来源: `APN意图澄清知识库.md` §场景3 + §速查表第3行

- **配置决策**:
  | 维度 | 决策 | 依据 |
  |------|------|------|
  | 地址分配 | **UPF 动态分配（基于 SMF）** | 按 UPF 设备分配，CU Full Mesh 组网；配置复杂度低（§一1.4） |
  | 鉴权方式 | **透明接入 TRANS_NON_AUTH** | 普通 Internet 访问无需 AAA |
  | 接入方式 | **VPN 直连（NAT）** | 直接访问 Internet |
  | 地址类型 | **IPv4v6 双栈** | 满足 IPv4/IPv6 终端兼容性（§四4.2 决策矩阵） |

### 3.2 涉及特性清单

| 网元 | feature_id | 特性名 | 角色 |
|------|-----------|--------|------|
| UDG(UPF) | **GWFD-010105** | 用户面地址分配 | 基于 SMF 本地地址池分配（ADD CPNODEID + SET IPALLOCBYSMFGLBSW） |
| UDG(UPF) | **GWFD-020403** | IPv4v6 双栈接入 | 双栈地址类型支持 |
| UDG(UPF) | GWFD-010104 | 地址分配方式 | 母特性 |
| UNC(SMF) | WSFD-011305 | Radius 鉴权接入 | ACCESSMODE=TRANS_NON_AUTH |

### 3.3 关键MML命令序列骨架（原始MML保留）

```
// 来源: feature-knowledge/GWFD-010105-用户面地址分配.md §5.2（基于SMF分配地址）+ §5.1双栈扩展 [EV-FK-*]

ADD L3VPNINST: VRFNAME="vpn_broadband";
ADD VPNINSTAF: VRFNAME="vpn_broadband", AFTYPE=ipv4uni, VRFRD=100:1;

ADD VPNINST: VPNINSTANCE="vpn_broadband";
ADD APN: APN="internet.home.apn", HASVPN=ENABLE, VPNINSTANCE="vpn_broadband";
SET APNADDRESSATTR: APN="internet.home.apn", SUPPORTIPV4=ENABLE, SUPPORTIPV6=ENABLE;

// 本地地址池（双栈需配 IPv4 + IPv6 两种 SECTION）
ADD POOL: POOLNAME="bb_pool_v4", POOLTYPE=LOCAL, HASVPN=ENABLE, VPNINSTANCE="vpn_broadband";
ADD SECTION: POOLNAME="bb_pool_v4", SECTIONNUM=1, IPVERSION=IPV4, V4STARTIP="100.64.1.1", V4ENDIP="100.64.1.254";
ADD POOL: POOLNAME="bb_pool_v6", POOLTYPE=LOCAL, HASVPN=ENABLE, VPNINSTANCE="vpn_broadband";
ADD SECTION: POOLNAME="bb_pool_v6", SECTIONNUM=1, IPVERSION=IPV6, V6STARTIP="2001:db8:1::", V6ENDIP="2001:db8:1::ff";

ADD POOLGROUP: POOLGRPNAME="bb_poolgroup";
ADD POOLBINDGROUP: POOLGROUPNAME="bb_poolgroup", POOLNAME="bb_pool_v4";
ADD POOLBINDGROUP: POOLGROUPNAME="bb_poolgroup", POOLNAME="bb_pool_v6";

// 基于 SMF 分配：配置 SMF NodeID + 映射
ADD CPNODEID: CPNAME="smfnode1", IPV4NODEID="10.0.0.1", IPV6NODEID="FC00:1111:1001:0001:0100:1100:0000:0001", FQDNNODEID="consumer.huawei.com";
ADD POOLGRPMAP: MAPPINGNAME="bb_map", SMF="smfnode1", POOLGROUPNAME="bb_poolgroup";

// 基于 SMF 分配规则 + 全局开关
SET IPALLOCRULE: FIRSTRULESW=ENABLE, FIRSTRULE=APN-0&LOCATION-0&SMF-1, SECONDRULESW=DISABLE, THIRDRULESW=DISABLE;
SET IPALLOCBYSMFGLBSW: SWITCH=ENABLE;

// 下行路由
ADD OSPF: PROCID=100, VRFNAME="vpn_broadband", SCHEMAROUID="10.30.30.1";
ADD OSPFAREA: PROCID=100, AREAID="0.0.0.0";
ADD OSPFNETWORK: PROCID=100, AREAID="0.0.0.0", IPADDRESS="10.13.21.0", WILDCARDMASK="0.0.0.255";
ADD OSPFIMPORTROUTE: PROCID=100, TOPOID=0, PROTOCOL=wlr;

// UNC 侧：透明接入。
ADD APN: APN="internet.home.apn";
SET APNAUTHATTR: APN="internet.home.apn", ACCESSMODE=TRANS_NON_AUTH;
```

### 3.4 对应第1层 ConfigurationSolution

- **CS-APN-03**: 配置闭包 = {UPF本地池(IPv4+IPv6双SECTION)@UDG, 基于SMF映射, TRANS_NON_AUTH, NAT直连, IPv4v6双栈}
- **关联 DecisionPoint**: DP-ADDR(=UPF-SMF) × DP-AUTH(=TRANS_NON_AUTH) × DP-ACCESS(=VPN-NAT) × DP-IPTYPE(=IPv4v6)
- **关联 BusinessRule**: BR-按UPF设备分配 → 基于SMF子方式; BR-双栈终端兼容 → IPv4v6

---

## 4. CS-APN-04 VoLTE 语音业务

### 4.1 业务需求与配置决策

- **业务需求**: 运营商 VoLTE/VoNR 业务；IMS 注册和呼叫；需要 SMF 精确寻址；双栈支持。[EV-TK-14-04]
  - 来源: `APN意图澄清知识库.md` §场景4 + §速查表第4行

- **配置决策**:
  | 维度 | 决策 | 依据 |
  |------|------|------|
  | 地址分配 | **SMF 动态分配** | IMS 语音需 SMF 精确寻址；SMF 本地地址池控制面分配（§一1.1 概览表） |
  | 鉴权方式 | **透明接入 TRANS_NON_AUTH** | 运营商直接提供业务，HSS/UDM 已完成鉴权（§三3.2） |
  | 接入方式 | **VPN 直连** | IMS 核心网直连，无需隧道 |
  | 地址类型 | **IPv4v6 双栈** | IMS 语音需双栈支持 SIP 信令与媒体面 |

### 4.2 涉及特性清单

| 网元 | feature_id | 特性名 | 角色 |
|------|-----------|--------|------|
| UNC(SMF) | **WSFD-010502** | 地址分配方式 | SMF 本地地址池分配（POOLTYPE=SMF/LOCAL） |
| UNC(SMF) | **WSFD-010504** | 控制面地址分配方式 | 控制面分配总览 |
| UDG(UPF) | GWFD-010104 | 地址分配方式 | 外部地址分配（接收 SMF 分配的地址 + 白名单 + 路由发布） |
| UNC(SMF) | WSFD-011305 | Radius 鉴权接入 | ACCESSMODE=TRANS_NON_AUTH |

### 4.3 关键MML命令序列骨架（原始MML保留）

```
// 来源: feature-knowledge/WSFD-010502-地址分配方式.md §5.1（地址池体系，ADDRALLOCMODE=SMF分配）+ GWFD-010104 §5.1（UDG外部地址池白名单）[EV-FK-*]

// ===== UNC 侧：SMF 本地地址池（双栈） =====
ADD ADDRPOOL: POOLNAME="volte_pool_v4", IPVERSION=IPv4, POOLTYPE=SMF, CHECKIPVALID=Enable;
ADD SECTION: POOLNAME="volte_pool_v4", SECTIONNUM=1, IPVERSION=IPv4, V4STARTIP="192.168.10.1", V4ENDIP="192.168.10.254";
ADD ADDRPOOL: POOLNAME="volte_pool_v6", IPVERSION=IPv6, POOLTYPE=SMF, CHECKIPVALID=Enable;
ADD SECTION: POOLNAME="volte_pool_v6", SECTIONNUM=1, IPVERSION=IPv6, V6STARTIP="2001:db8:2::", V6ENDIP="2001:db8:2::ff";

ADD POOLBINDAPN: APN="ims.apn", POOLNAME="volte_pool_v4";
ADD POOLBINDAPN: APN="ims.apn", POOLNAME="volte_pool_v6";

ADD ADDRPOOLGRP: POOLGRPNAME="volte_poolgrp", POOLGRPTYPE=SMF;
ADD POOLBINDGRP: POOLGRPNAME="volte_poolgrp", POOLNAME="volte_pool_v4";
ADD POOLBINDGRP: POOLGRPNAME="volte_poolgrp", POOLNAME="volte_pool_v6";

ADD UPNODE: NFINSTANCENAME="UPF_IMS_1", ADDRALLOCMODE=SMF;
ADD ADDRUPGROUP: UPFGRPNAME="volte_upfgrp", UPFGRPTYPE=SMF;
ADD UPFBINDGRP: UPFGRPNAME="volte_upfgrp", UPFID="UPF_IMS_1";
ADD POOLGRPMAP: MAPPINGNAME="volte_mapping01", POOLGRPNAME="volte_poolgrp", UPFGRPNAME="volte_upfgrp";

// 鉴权属性：透明接入。
ADD APN: APN="ims.apn";
SET APNAUTHATTR: APN="ims.apn", ACCESSMODE=TRANS_NON_AUTH;

// ===== UDG 侧：外部地址池白名单 + 路由发布 =====
// （同 CS-APN-01 的 UDG 外部地址池骨架，POOLTYPE=EXTERNAL + CHECKIPVALID=ENABLE，详见 GWFD-010104 §5.1）
ADD VPNINST: VPNINSTANCE="vpn_ims";
ADD POOLGROUP: POOLGRPNAME="ims_ext_poolgroup";
ADD POOL: POOLNAME="ims_ext_v4", POOLTYPE=EXTERNAL, CHECKIPVALID=ENABLE, HASVPN=ENABLE, VPNINSTANCE="vpn_ims";
ADD SECTION: POOLNAME="ims_ext_v4", SECTIONNUM=1, IPVERSION=IPV4, V4STARTIP="192.168.10.1", V4ENDIP="192.168.10.254";
ADD POOL: POOLNAME="ims_ext_v6", POOLTYPE=EXTERNAL, CHECKIPVALID=ENABLE, HASVPN=ENABLE, VPNINSTANCE="vpn_ims";
ADD SECTION: POOLNAME="ims_ext_v6", SECTIONNUM=1, IPVERSION=IPV6, V6STARTIP="2001:db8:2::", V6ENDIP="2001:db8:2::ff";
ADD POOLBINDGROUP: POOLGROUPNAME="ims_ext_poolgroup", POOLNAME="ims_ext_v4";
ADD POOLBINDGROUP: POOLGROUPNAME="ims_ext_poolgroup", POOLNAME="ims_ext_v6";
ADD APN: APN="ims.apn", HASVPN=ENABLE, VPNINSTANCE="vpn_ims";
SET APNADDRESSATTR: APN="ims.apn", HOSTROUTEIP=ENABLE;
ADD POOLGRPMAP: MAPPINGNAME="ims_ext_map", APN="ims.apn", POOLGROUPNAME="ims_ext_poolgroup";

// 下行路由发布。
ADD OSPF: PROCID=100, VRFNAME="vpn_ims", SCHEMAROUID="10.40.40.1";
ADD OSPFAREA: PROCID=100, AREAID="0.0.0.0";
ADD OSPFNETWORK: PROCID=100, AREAID="0.0.0.0", IPADDRESS="10.13.21.0", WILDCARDMASK="0.0.0.255";
ADD OSPFIMPORTROUTE: PROCID=100, TOPOID=0, PROTOCOL=wlr;
```

### 4.4 对应第1层 ConfigurationSolution

- **CS-APN-04**: 配置闭包 = {SMF本地池(IPv4+IPv6)@UNC, 外部地址池白名单@UDG, TRANS_NON_AUTH, 直连IMS, IPv4v6双栈}
- **关联 DecisionPoint**: DP-ADDR(=SMF) × DP-AUTH(=TRANS_NON_AUTH) × DP-ACCESS(=直连) × DP-IPTYPE(=IPv4v6)
- **关联 BusinessRule**: BR-IMS精确寻址 → SMF分配; BR-双栈语音 → IPv4v6

---

## 5. CS-APN-05 企业 AAA 二次鉴权

### 5.1 业务需求与配置决策

- **业务需求**: 企业 AAA 服务器统一管控用户鉴权和地址分配；支持企业安全策略；ISP/企业对用户权限有要求。[EV-TK-14-05]
  - 来源: `APN意图澄清知识库.md` §速查表第6行 + §三3.2 鉴权方式决策矩阵

- **配置决策**:
  | 维度 | 决策 | 依据 |
  |------|------|------|
  | 地址分配 | **RADIUS 分配** | AAA 服务器在鉴权过程中下发地址（§一1.6 RADIUS分配原理） |
  | 鉴权方式 | **不透明接入 NON_TRANS** | 企业 AAA 二次鉴权，UE 通过 PCO 携带用户名密码 |
  | 接入方式 | **VPN 或 GRE** | 视组网而定，轻度加密用 GRE，无需则 VPN |
  | 地址类型 | **IPv4** | 企业网普遍 IPv4 |

### 5.2 涉及特性清单

| 网元 | feature_id | 特性名 | 角色 |
|------|-----------|--------|------|
| UNC(SMF) | **WSFD-011305** | Radius 鉴权接入 | ACCESSMODE=NON_TRANS（必须开启 Radius 功能） |
| UNC(SMF) | **WSFD-011306** | Radius 功能 | NON_TRANS 强依赖（§3.3 AUTHMODE×Radius 矩阵） |
| UDG(UPF) | **GWFD-010105** | 用户面地址分配 | 基于 RADIUS 下发地址池名子方式（IGNOREV4/V6POOLID=DISABLE） |
| UDG(UPF) | IPFD-015002 | GRE | 可选轻量级隧道 |
| UNC(SMF) | WSFD-011307 | Radius 抄送功能 | 计费抄送链路（可选） |

### 5.3 关键MML命令序列骨架（原始MML保留）

```
// 来源: feature-knowledge/WSFD-011305-Radius鉴权接入.md §4.3 + GWFD-010105 §5.4（基于RADIUS下发地址池名）[EV-FK-*]

// ===== UNC 侧：不透明接入 + Radius 功能前置 =====
ADD APN: APN="enterprise.aaa.apn";
SET APNAUTHATTR: APN="enterprise.aaa.apn", ACCESSMODE=NON_TRANS;
// （前置：ADD RDSSVRGRP / 配置 RADIUS 功能，详见 WSFD-011306；AAA Server 工作正常且鉴权信息已配置）

// ===== UDG 侧：基于 RADIUS 下发地址池名分配地址（关键差异） =====
// 必须配置 IGNOREV4POOLID=DISABLE / IGNOREV6POOLID=DISABLE
ADD VPNINST: VPNINSTANCE="vpn_ent_aaa";
ADD APN: APN="enterprise.aaa.apn", HASVPN=ENABLE, VPNINSTANCE="vpn_ent_aaa";
SET APNADDRESSATTR: APN="enterprise.aaa.apn", SUPPORTIPV4=ENABLE, SUPPORTIPV6=DISABLE, IGNOREV4POOLID=DISABLE, IGNOREV6POOLID=DISABLE;

// 地址池（LOCAL 类型）。
ADD POOL: POOLNAME="ent_aaa_pool", POOLTYPE=LOCAL, HASVPN=ENABLE, VPNINSTANCE="vpn_ent_aaa";
ADD SECTION: POOLNAME="ent_aaa_pool", SECTIONNUM=1, IPVERSION=IPV4, V4STARTIP="172.16.1.1", V4ENDIP="172.16.1.254";
ADD POOLGROUP: POOLGRPNAME="ent_aaa_poolgroup";
ADD POOLBINDGROUP: POOLGROUPNAME="ent_aaa_poolgroup", POOLNAME="ent_aaa_pool";

// APN 与地址池组映射。
ADD POOLGRPMAP: MAPPINGNAME="ent_aaa_map", APN="enterprise.aaa.apn", POOLGROUPNAME="ent_aaa_poolgroup";

// 基于 APN 的地址分配规则（使用 SET APNIPALLOCRULE，ALLOCATTR=LOCAL）。
SET APNIPALLOCRULE: APN="enterprise.aaa.apn", ALLOCATTR=LOCAL, FIRSTRULESW=ENABLE, FIRSTRULE=APN-1&LOCATION-0&SMF-0, SECONDRULESW=DISABLE, THIRDRULESW=DISABLE;

// 地址池名称通配功能（控制 AAA 未下发通配符时是否开启通配）。
SET ADDRESSATTR: V4POOLWILDCARDSW=ENABLE, V6POOLWILDCARDSW=ENABLE;

// 下行路由发布。
ADD OSPF: PROCID=100, VRFNAME="vpn_ent_aaa", SCHEMAROUID="10.50.50.1";
ADD OSPFAREA: PROCID=100, AREAID="0.0.0.0";
ADD OSPFNETWORK: PROCID=100, AREAID="0.0.0.0", IPADDRESS="10.13.21.0", WILDCARDMASK="0.0.0.255";
ADD OSPFIMPORTROUTE: PROCID=100, TOPOID=0, PROTOCOL=wlr;

// 可选：GRE 隧道（轻量级封装，骨架）
// 来源: feature-knowledge/IPFD-015002-GRE.md §5.1
ADD INTERFACE: IFNAME="LoopBack1";
ADD IFIPV4ADDRESS: IFNAME="LoopBack1", IFIPADDR="10.3.3.11", SUBNETMASK="255.255.255.255", ADDRTYPE=main;
ADD GRETUNNEL: TNLNAME="Tunnel_ent", TNLTYPE=gre, SRCTYPE=if_name, SRCIFNAME="LoopBack1", DSTIPADDR="10.4.4.11";
ADD IFIPV4ADDRESS: IFNAME="Tunnel_ent", IFIPADDR="10.10.1.201", SUBNETMASK="255.255.255.0", ADDRTYPE=main;
ADD SRROUTE: AFTYPE=ipv4unicast, PREFIX="10.10.1.202", MASKLENGTH=24, IFNAME="Tunnel_ent";
```

> 关键约束: NON_TRANS 必须开启 Radius 功能（WSFD-011305 §1.6）；IGNOREV4/V6POOLID=DISABLE 是 RADIUS 子方式的硬约束（GWFD-010105 §5.4）。

### 5.4 对应第1层 ConfigurationSolution

- **CS-APN-05**: 配置闭包 = {Radius地址池名下发@UDG(IGNORE_POOLID=DISABLE), NON_TRANS+Radius功能@UNC, 可选GRE隧道, IPv4单栈}
- **关联 DecisionPoint**: DP-ADDR(=RADIUS) × DP-AUTH(=NON_TRANS) × DP-ACCESS(=VPN或GRE) × DP-IPTYPE(=IPv4)
- **关联 BusinessRule**: BR-AAA统一管控 → RADIUS分配+NON_TRANS; BR-轻度加密 → GRE可选

---

## 6. CS-APN-06 传统企业 DHCP 迁移

### 6.1 业务需求与配置决策

- **业务需求**: 企业已有 DHCP 基础设施；复用现有 DHCP 服务器，无需新建地址池；地址由 DHCP 统一管理。[EV-TK-14-06]
  - 来源: `APN意图澄清知识库.md` §速查表第7行 + §一1.1 DHCP/DHCPv6 分配方式

- **配置决策**:
  | 维度 | 决策 | 依据 |
  |------|------|------|
  | 地址分配 | **DHCP 分配** | UNC 作为 DHCP Client 代理用户向外部 DHCP Server 申请地址（§一1.6） |
  | 鉴权方式 | **透明接入 TRANS_NON_AUTH** | 无需 AAA，SIM 卡合法即可 |
  | 接入方式 | **VPN 直连** | 企业内网访问 |
  | 地址类型 | **IPv4** | 传统企业 DHCP 普遍 IPv4 |

### 6.2 涉及特性清单

| 网元 | feature_id | 特性名 | 角色 |
|------|-----------|--------|------|
| UNC(SMF) | **WSFD-104413** | DHCP 功能 | UNC 代理 DHCP 申请（核心） |
| UNC(SMF) | WSFD-010502 | 地址分配方式 | IPV4ALLOCTYPE=DHCP |
| UDG(UPF) | GWFD-010104 | 地址分配方式 | 外部地址池接收 DHCP 分配的地址 |
| UNC(SMF) | WSFD-011305 | Radius 鉴权接入 | ACCESSMODE=TRANS_NON_AUTH |

### 6.3 关键MML命令序列骨架（原始MML保留）

```
// 来源: feature-knowledge/WSFD-104413-DHCP功能.md §5.1（最小可用配置，基于参考信息命令清单+原理）[EV-FK-*]

// 配置 VPN 实例。
ADD VPNINST: VPNNAME="dhcp_vpn";

// 配置 UNC 侧地址池（代理用）。
ADD ADDRPOOL: POOLNAME="dhcp_pool_v4", IPVERSION=IPv4;
ADD AGENTIP: POOLNAME="dhcp_pool_v4", AGENTIP="10.10.0.1";

// 配置外部 DHCP Server 组（主备）。
ADD DHCPSERVERGRP: GROUPNAME="dhcp_group_1";
ADD DHCPSERVER: GROUPNAME="dhcp_group_1", SERVERNAME="dhcp_server_pri", SERVERIP="10.10.0.2", VPNINSTANCE="";
ADD DHCPSERVER: GROUPNAME="dhcp_group_1", SERVERNAME="dhcp_server_sec", SERVERIP="10.10.0.3", VPNINSTANCE="";

// 绑定 DHCP Server 组到 UNC 地址池组。
ADD ADDRPOOLGRP: POOLGRPNAME="dhcp_poolgrp_1";
ADD DHCPBINDPOOLGRP: POOLGRPNAME="dhcp_poolgrp_1", DHCPSERVERGRPNAME="dhcp_group_1";

// APN 配置 + 地址分配方式 = DHCP。
ADD APN: APN="enterprise.dhcp.apn";
SET APNADDRESSATTR: APN="enterprise.dhcp.apn", IPV4ALLOCTYPE=DHCP;

// 可选：DNS / SIP Server 申请。
SET DHCPPARAREQ: DOMAINNAMESERVER=ENABLE, SIPSERVER=ENABLE;

// 地址分配规则（全局）。
SET IPALLOCRULE: FIRSTRULESW=ENABLE, FIRSTRULE=APN-1&LOCATION-0&SMF-0, SECONDRULESW=DISABLE, THIRDRULESW=DISABLE;

// 鉴权属性：透明接入。
SET APNAUTHATTR: APN="enterprise.dhcp.apn", ACCESSMODE=TRANS_NON_AUTH;
```

> 文档依据: WSFD-104413 产品文档仅 2 个文件，未提供完整端到端 MML 脚本，本骨架基于参考信息命令清单（9条 MML）+ 原理章节构建（feature-knowledge §5.1 已说明）。

### 6.4 对应第1层 ConfigurationSolution

- **CS-APN-06**: 配置闭包 = {外部DHCP Server组@UNC, IPV4ALLOCTYPE=DHCP, TRANS_NON_AUTH, VPN直连, IPv4单栈}
- **关联 DecisionPoint**: DP-ADDR(=DHCP) × DP-AUTH(=TRANS_NON_AUTH) × DP-ACCESS(=VPN) × DP-IPTYPE(=IPv4)
- **关联 BusinessRule**: BR-复用现有DHCP → DHCP分配; BR-无AAA → 透明接入

---

## 7. CS-APN-07 企业 L2TP VPN

### 7.1 业务需求与配置决策

- **业务需求**: 远程办公/分支机构通过 L2TP 隧道接入企业内网；LNS 服务器验证并分配地址；保证访问安全。[EV-TK-14-07]
  - 来源: `APN意图澄清知识库.md` §速查表第8行 + §一1.1 LNS 分配方式

- **配置决策**:
  | 维度 | 决策 | 依据 |
  |------|------|------|
  | 地址分配 | **LNS 分配** | L2TP 隧道 + LNS PPP 协商分配地址（§一1.6） |
  | 鉴权方式 | **不透明接入 NON_TRANS** | 企业 LNS 验证，UE 通过 PPP 携带账密 |
  | 接入方式 | **L2TP 隧道** | 二层 PPP 隧道，远程办公专用 |
  | 地址类型 | **IPv4v6 双栈** | v02 20.6.0+ 支持 IPv6 用户接入 |

### 7.2 涉及特性清单

| 网元 | feature_id | 特性名 | 角色 |
|------|-----------|--------|------|
| UDG(UPF) | **GWFD-020412** | L2TP VPN | U 面 LAC + PPP 再生 + 隧道封装（需 License LKV3G5L2TP01） |
| UNC(SMF) | **WSFD-104410** | L2TP VPN | C 面对称（AAA 下发 LNS 属性场景） |
| UNC(SMF) | WSFD-011305 | Radius 鉴权接入 | ACCESSMODE=NON_TRANS（AAA 下发 LNS 属性场景必需） |

### 7.3 关键MML命令序列骨架（原始MML保留）

```
// 来源: feature-knowledge/GWFD-020412-L2TPVPN.md §5.1（本地配置方式主备LNS完整脚本）[EV-FK-*]

// 打开本特性的 License 配置开关。
SET LICENSESWITCH: LICITEM="LKV3G5L2TP01", SWITCH=ENABLE;

// 配置 VPN 实例。
ADD VPNINST: VPNINSTANCE="vpn_l2tp";

// 配置 L2TP 组（主备 LNS，LOCALNSMODE=REDUNDANCY）。
ADD L2TPGROUP: GROUPID=1, DOMAINNAME="example.com", LOCALNAME="UPF", AVPHIDDEN=ENABLE, HELLOINTERVALSW=ENABLE, HELLOINTERVAL=120, VPNINSTANCE="vpn_l2tp", LOCALLNSMODE=REDUNDANCY, FIRSTLNSIP="10.10.10.1", FIRSTPWD="0123456", SECONDLNSIP="10.10.10.2", SECONDPWD="0123456", CFMFIRSTPWD="0123456", CFMSECONDPWD="0123456", PPPMAGICNUMBER=ENABLE, MAXSENDWINSIZE=32;

// 配置 L2TP 的缺省参数，使能本地配置方式启用 L2TP。
SET GLOBALL2TP: LOCALNAME="huawei", HELLOINTERVALSW=ENABLE, HELLOINTERVAL=60, RETRYTIMES=3;

// 设置 APN 的 L2TP 相关信息，指定 APN 下绑定 L2TP 组。
ADD APN: APN="apn-l2tp";
SET APNL2TPATTR: APN="apn-l2tp", L2TPSWITCH=ENABLE, SUPPORTIPV6=DISABLE, L2TPGROUPID=1, ICRQ_CALLINGNO=MSISDN, ICCN_AUTH=ENABLE, IPCP_NEGO=ENABLE, DOMAINNAMEACT=ADD_ENABLE_STRIP_DISABLE, DOMAINNAMEPOS=PREFIX;

// 关闭快速流表功能。
SET SOFTPARAOFBIT: DT2=BYTE, BYTENUM=671, BYTEPOSITION=7, BYTEVALUE=1;

// 配置 Giif 接口。
ADD LOGICINF: NAME="giif1/0/0", IPVERSION=IPV4, IPV4ADDRESS1="10.8.20.1", IPV4MASK1="255.255.255.255", VPNINSTANCE="vpn_l2tp";

// 将 L2TP 组绑定指定源端接口。
ADD L2TPCLIENTIP: L2TPGROUPID=1, INTERFACENAME="giif1/0/0";

// PPP 协商参数 + APN PPP 鉴权。
SET PPPCFG: HOSTNAME="UPF", MRU=1500, TIMEOUT=3;
SET APNPPPACCESS: APN="apn-l2tp", AUTHENTICATION=ENABLE;

// 可选：L2TP 业务加密（N4 接口私有信元安全）。
SET L2TPN4KEY: N4KEYVALUE="*****", CFMN4KEYVALUE="*****";

// UNC 侧：不透明接入（AAA 下发 LNS 属性场景，本地配置场景可选）。
SET APNAUTHATTR: APN="apn-l2tp", ACCESSMODE=NON_TRANS;
```

> 双栈支持: SUPPORTIPV6=ENABLE（v02 20.6.0+ 起支持 IPv6 用户接入；v03 20.12.0+ UDG-LNS 隧道支持 IPv6）。
> 关键约束: L2TP 与基于位置的地址分配互斥（GWFD-020421 §1.6）。

### 7.4 对应第1层 ConfigurationSolution

- **CS-APN-07**: 配置闭包 = {L2TP组(主备LNS)@UDG, License LKV3G5L2TP01, NON_TRANS+PPP鉴权, L2TP隧道, IPv4v6双栈}
- **关联 DecisionPoint**: DP-ADDR(=LNS) × DP-AUTH(=NON_TRANS) × DP-ACCESS(=L2TP) × DP-IPTYPE(=IPv4v6)
- **关联 BusinessRule**: BR-远程办公隧道 → L2TP+LNS; BR-PPP鉴权 → NON_TRANS

---

## 8. CS-APN-08 区域化运营管理

### 8.1 业务需求与配置决策

- **业务需求**: 不同城市/区县分配不同网段地址；支持区域化运营、精准营销、区域计费；便于 IP 精细管理。[EV-TK-14-08]
  - 来源: `APN意图澄清知识库.md` §速查表第9行 + §场景"运营商热点覆盖" + §一1.6 基于位置的地址分配原理

- **配置决策**:
  | 维度 | 决策 | 依据 |
  |------|------|------|
  | 地址分配 | **UPF 动态分配（基于位置区）** | 根据 LAC/TAC 位置区分配地址，需 License LKV3G5LBAA01（§一1.4） |
  | 鉴权方式 | **透明接入 TRANS_NON_AUTH** | 运营商直接提供业务 |
  | 接入方式 | **VPN 直连** | 直接访问 Internet |
  | 地址类型 | **IPv4** | 区域化管理普遍 IPv4 |

### 8.2 涉及特性清单

| 网元 | feature_id | 特性名 | 角色 |
|------|-----------|--------|------|
| UDG(UPF) | **GWFD-020421** | 基于位置的地址分配 | 基于 LAC/TAC 位置区组分配（需 License LKV3G5LBAA01） |
| UDG(UPF) | GWFD-010105 | 用户面地址分配 | 母特性（基于位置是子方式） |
| UNC(SMF) | WSFD-011305 | Radius 鉴权接入 | ACCESSMODE=TRANS_NON_AUTH |

### 8.3 关键MML命令序列骨架（原始MML保留）

```
// 来源: feature-knowledge/GWFD-020421-基于位置的地址分配.md §1.4 License + §4 配置规则（基于 GWFD-010105 §5.1 扩展 LOCATION 维度）[EV-FK-*]

// 打开本特性的 License 配置开关（LKV3G5LBAA01 必需）。
SET LICENSESWITCH: LICITEM="LKV3G5LBAA01", SWITCH=ENABLE;

// 配置 VPN 实例。
ADD L3VPNINST: VRFNAME="vpn_regional";
ADD VPNINSTAF: VRFNAME="vpn_regional", AFTYPE=ipv4uni, VRFRD=100:1;
ADD VPNINST: VPNINSTANCE="vpn_regional";

// 基于 APN 使能地址分配属性。
ADD APN: APN="regional.operator.apn", HASVPN=ENABLE, VPNINSTANCE="vpn_regional";
SET APNADDRESSATTR: APN="regional.operator.apn", SUPPORTIPV4=ENABLE, SUPPORTIPV6=DISABLE;

// 配置本地地址池（按区域规划多个池，此处示例区域1）。
ADD POOL: POOLNAME="regional_pool_area1", POOLTYPE=LOCAL, HASVPN=ENABLE, VPNINSTANCE="vpn_regional";
ADD SECTION: POOLNAME="regional_pool_area1", SECTIONNUM=1, IPVERSION=IPV4, V4STARTIP="100.64.101.1", V4ENDIP="100.64.101.254";
ADD POOLGROUP: POOLGRPNAME="regional_poolgroup_area1";
ADD POOLBINDGROUP: POOLGROUPNAME="regional_poolgroup_area1", POOLNAME="regional_pool_area1";

// 配置位置区组（LAC/TAC）并映射到地址池组。
// （ADD LOCATIONGROUP / ADD LOCGRPMAP 等命令，详见 GWFD-020421 §4 激活步骤）
// 示例：LOCATIONGROUP="lac_group_area1" → POOLGROUPNAME="regional_poolgroup_area1"

// 配置地址分配规则（LOCATION 维度使能）。
SET IPALLOCRULE: FIRSTRULESW=ENABLE, FIRSTRULE=APN-0&LOCATION-1&SMF-0, SECONDRULESW=DISABLE, THIRDRULESW=DISABLE;

// 下行路由发布。
ADD OSPF: PROCID=100, VRFNAME="vpn_regional", SCHEMAROUID="10.60.60.1";
ADD OSPFAREA: PROCID=100, AREAID="0.0.0.0";
ADD OSPFNETWORK: PROCID=100, AREAID="0.0.0.0", IPADDRESS="10.13.21.0", WILDCARDMASK="0.0.0.255";
ADD OSPFIMPORTROUTE: PROCID=100, TOPOID=0, PROTOCOL=wlr;

// UNC 侧：透明接入。
SET APNAUTHATTR: APN="regional.operator.apn", ACCESSMODE=TRANS_NON_AUTH;
```

> 关键约束: 基于位置的地址分配与 L2TP VPN 双向互斥（GWFD-020421 §1.6）；必须 License LKV3G5LBAA01；用户移动需重新分配地址（§一1.4 移动性影响）。

### 8.4 对应第1层 ConfigurationSolution

- **CS-APN-08**: 配置闭包 = {本地地址池按LAC/TAC绑定@UDG, License LKV3G5LBAA01, TRANS_NON_AUTH, VPN直连, IPv4单栈}
- **关联 DecisionPoint**: DP-ADDR(=UPF-LOCATION) × DP-AUTH(=TRANS_NON_AUTH) × DP-ACCESS(=VPN) × DP-IPTYPE(=IPv4)
- **关联 BusinessRule**: BR-区域化管理 → 基于位置区; BR-位置互斥L2TP → 场景二选一

---

## 9. CS-APN-09 企业双栈

### 9.1 业务需求与配置决策

- **业务需求**: 企业部署支持 IPv4/IPv6 双栈终端；需同时支持两种协议；公网传输需高安全加密。[EV-TK-14-09]
  - 来源: `APN意图澄清知识库.md` §四地址类型决策 + §二接入方式决策（IPSec 高安全） + §速查表"企业双栈"扩展场景

- **配置决策**:
  | 维度 | 决策 | 依据 |
  |------|------|------|
  | 地址分配 | **UPF 动态分配（基于 APN/DNN）** | 按 APN 业务类型管理双栈地址池 |
  | 鉴权方式 | **透明接入 TRANS_NON_AUTH** | 运营商统一鉴权或 SIM 卡合法即可 |
  | 接入方式 | **IPSec 隧道** | 公网传输需高安全加密，ESP+AH |
  | 地址类型 | **IPv4v6 双栈** | 双栈终端，IPv4+IPv6 并存 |

### 9.2 涉及特性清单

| 网元 | feature_id | 特性名 | 角色 |
|------|-----------|--------|------|
| UDG(UPF) | **GWFD-010105** | 用户面地址分配 | 基于 APN/DNN 双栈本地池分配（IPv4+IPv6 两种 SECTION） |
| UDG(UPF) | **GWFD-020403** | IPv4v6 双栈接入 | 双栈地址类型核心支持 |
| UDG(UPF) | **IPFD-015004** | IPSec 功能 | 用户面 IPSec 隧道加密 |
| UNC(SMF) | WSFD-011305 | Radius 鉴权接入 | ACCESSMODE=TRANS_NON_AUTH |

### 9.3 关键MML命令序列骨架（原始MML保留）

```
// 来源: feature-knowledge/GWFD-010105-用户面地址分配.md §5.1（双栈扩展）+ IPFD-015004-IPSec功能.md [EV-FK-*]

ADD L3VPNINST: VRFNAME="vpn_dualstack";
ADD VPNINSTAF: VRFNAME="vpn_dualstack", AFTYPE=ipv4uni, VRFRD=100:1;

ADD VPNINST: VPNINSTANCE="vpn_dualstack";
ADD APN: APN="enterprise.dualstack.apn", HASVPN=ENABLE, VPNINSTANCE="vpn_dualstack";
SET APNADDRESSATTR: APN="enterprise.dualstack.apn", SUPPORTIPV4=ENABLE, SUPPORTIPV6=ENABLE;

// 本地地址池（双栈必须配 IPv4 + IPv6 两种 SECTION）。
ADD POOL: POOLNAME="ds_pool_v4", POOLTYPE=LOCAL, HASVPN=ENABLE, VPNINSTANCE="vpn_dualstack";
ADD SECTION: POOLNAME="ds_pool_v4", SECTIONNUM=1, IPVERSION=IPV4, V4STARTIP="10.100.1.1", V4ENDIP="10.100.1.254";
ADD POOL: POOLNAME="ds_pool_v6", POOLTYPE=LOCAL, HASVPN=ENABLE, VPNINSTANCE="vpn_dualstack";
ADD SECTION: POOLNAME="ds_pool_v6", SECTIONNUM=1, IPVERSION=IPV6, V6STARTIP="2001:db8:100::", V6ENDIP="2001:db8:100::ff";

ADD POOLGROUP: POOLGRPNAME="ds_poolgroup";
ADD POOLBINDGROUP: POOLGROUPNAME="ds_poolgroup", POOLNAME="ds_pool_v4";
ADD POOLBINDGROUP: POOLGROUPNAME="ds_poolgroup", POOLNAME="ds_pool_v6";

// APN 与地址池组映射（基于 APN/DNN）。
ADD POOLGRPMAP: MAPPINGNAME="ds_map", APN="enterprise.dualstack.apn", POOLGROUPNAME="ds_poolgroup";

// 地址分配规则（单级优先级，仅 APN 维度）。
SET IPALLOCRULE: FIRSTRULESW=ENABLE, FIRSTRULE=APN-1&LOCATION-0&SMF-0, SECONDRULESW=DISABLE, THIRDRULESW=DISABLE;

// IPSec 隧道（IKEv2 + ESP，双栈场景，骨架）。
// 前置：IPSec 服务已安装、VNRS 与 IPsec 微服务双配
ADD INTERFACE: IFNAME="LoopBack1";
ADD IFIPV4ADDRESS: IFNAME="LoopBack1", IFIPADDR="10.3.3.11", SUBNETMASK="255.255.255.255", ADDRTYPE=main;
// （IPSec SA/IKE/Proposal 命令族，IPv4 IPsec + IPv6 IPsec 双栈，详见 IPFD-015004 §4）

// 下行路由发布。
ADD OSPF: PROCID=100, VRFNAME="vpn_dualstack", SCHEMAROUID="10.70.70.1";
ADD OSPFAREA: PROCID=100, AREAID="0.0.0.0";
ADD OSPFNETWORK: PROCID=100, AREAID="0.0.0.0", IPADDRESS="10.13.21.0", WILDCARDMASK="0.0.0.255";
ADD OSPFIMPORTROUTE: PROCID=100, TOPOID=0, PROTOCOL=wlr;

// UNC 侧：透明接入。
SET APNAUTHATTR: APN="enterprise.dualstack.apn", ACCESSMODE=TRANS_NON_AUTH;
```

> 关键约束: 双栈需为同一地址池或不同地址池补配 IPv4+IPv6 两种 SECTION（GWFD-010105 §6.4 排查表）；IPSec IPv6 支持 v02 20.8.0+（IPFD-015004 §1.3）。

### 9.4 对应第1层 ConfigurationSolution

- **CS-APN-09**: 配置闭包 = {UPF本地双栈池(IPv4+IPv6)@UDG, IPSec隧道(IKEv2+ESP), TRANS_NON_AUTH, IPv4v6双栈}
- **关联 DecisionPoint**: DP-ADDR(=UPF-APN) × DP-AUTH(=TRANS_NON_AUTH) × DP-ACCESS(=IPSec) × DP-IPTYPE(=IPv4v6)
- **关联 BusinessRule**: BR-双栈终端 → IPv4v6; BR-高安全加密 → IPSec

---

## 10. 批次总结与三层图谱映射

### 10.1 source_evidence_ids 占位映射

| Evidence ID | 来源 |
|-------------|------|
| EV-TK-14 | 本批次总占位（9方案归纳） |
| EV-TK-14-01 ~ EV-TK-14-09 | 各场景方案条目（见各 §1.1~§9.1） |
| 引用的 EV-FK-* | feature-knowledge 各特性文档的原始证据ID（GWFD-010105/010104/020421/020412、WSFD-010502/011305/104413、IPFD-015002/015004 等） |

### 10.2 9方案决策维度分布统计

| 决策维度 | 取值 | 涉及CS |
|---------|------|--------|
| 地址分配 | UDM静态 | CS-APN-01 |
| | UPF-APN/DNN | CS-APN-02, CS-APN-09 |
| | UPF-SMF | CS-APN-03 |
| | UPF-LOCATION | CS-APN-08 |
| | SMF本地 | CS-APN-04 |
| | RADIUS | CS-APN-05 |
| | DHCP | CS-APN-06 |
| | LNS(L2TP) | CS-APN-07 |
| 鉴权方式 | TRANS_NON_AUTH(透明) | CS-APN-02~04, CS-APN-06, CS-APN-08~09 |
| | NON_TRANS(不透明) | CS-APN-01, CS-APN-05, CS-APN-07 |
| 接入方式 | VPN直连(NAT) | CS-APN-02~04, CS-APN-06, CS-APN-08 |
| | IPSec隧道 | CS-APN-01, CS-APN-09 |
| | GRE隧道 | CS-APN-05(可选) |
| | L2TP隧道 | CS-APN-07 |
| 地址类型 | IPv4单栈 | CS-APN-01~02, CS-APN-05~06, CS-APN-08 |
| | IPv4v6双栈 | CS-APN-03~04, CS-APN-07, CS-APN-09 |

### 10.3 三层图谱映射预告（Stage 3-4 输入）

| 本批次产出 | → 三层图谱对象 |
|-----------|--------------|
| 9方案配置闭包 | **第1层 ConfigurationSolution**: CS-APN-01 ~ CS-APN-09（本批次直接来源） |
| 4维度决策矩阵 | **第1层 DecisionPoint**: DP-ADDR / DP-AUTH / DP-ACCESS / DP-IPTYPE |
| 场景业务规则 | **第1层 BusinessRule**: BR-固定IP / BR-公网加密 / BR-企业AAA / BR-区域化 / BR-双栈 等 |
| 涉及特性清单 | **第2层 Feature**: 9方案涉及的 UDG/UNC 双侧特性（依赖 Batch-01~13 的特性提取） |
| MML命令序列 | **第3层 ConfigTask**: 各 CS 对应的配置任务序列（命令族） |

### 10.4 关键发现与待验证问题

1. **C-U 协同普遍性**: 9方案中 8 个涉及 UDG(UPF) + UNC(SMF) 双侧配置（仅 CS-APN-04 SMF 分配主在 UNC），Stage 3 需重点验证 C-U 命令族对称性。
2. **License 触发点**: CS-APN-07(L2TP, LKV3G5L2TP01)、CS-APN-08(基于位置, LKV3G5LBAA01) 两个方案需 License；其余 7 方案无 License 门槛。
3. **互斥约束**: CS-APN-07(L2TP) 与 CS-APN-08(基于位置) 双向互斥，不可在同一 APN 同时部署；CS-APN-01/09(IPSec) 与 GRE 隧道源地址不可相同。
4. **鉴权-地址联动**: NON_TRANS 方式（CS-APN-01/05/07）必须开启 Radius 功能（WSFD-011306）；RADIUS 地址分配（CS-APN-05）必须 IGNOREV4/V6POOLID=DISABLE。
5. **双栈配置要点**: CS-APN-03/04/07/09 四方案均需为本地地址池配置 IPv4+IPv6 两种 SECTION；IPSec IPv6 支持 v02 20.8.0+。
6. **DHCP 文档缺口**: CS-APN-06 的 WSFD-104413 产品文档仅 2 文件无完整 MML 脚本，本批次骨架基于命令清单+原理构建，Stage 3 如有完整脚本应补充对照。
