# Phase 5 参考文件：APN 配置生成

## ⚠ 阶段执行约束（必须遵守）

**本文件仅用于 Phase 5。执行本文件内容前必须满足以下前置条件，否则 STOP：**

1. **用户必须已确认参数表**：必须已通过 GATE-2（用户在 Phase 4 明确确认了参数表）。如果用户未确认参数，**STOP**，回到 Phase 4 等待用户确认。没有例外。
2. **方案和参数必须已确定**：必须有 Phase 1 输出的匹配结果（场景/方案/5 维度决策点）、Phase 2 产出的 `xxx方案.md`，以及 Phase 3 产出的完整 `xxxLLD.md`（必要时附 `xxx规划数据表.md`）。缺少任何一个，**STOP**，回到对应阶段补全。
3. **本阶段完成后进入 Phase 6 核查**：生成配置后必须经过 Phase 6 核查和 Phase 6.5 用户确认（GATE-3），不得直接交付给用户。

---

> 本文件定义 APN 开通场景 Phase 5 的 pipeline 要求、输出模板和排序规则。
> 业务知识（参数映射、特殊场景处理规则、参数语义）由 Agent 从图谱和知识库动态加载。
> **通用约束**引用 `../../common/通用配置规则.md`（动网保守、跨网元协同、License 前置、按依赖顺序生成），本文件不复述。

---

## 1. Pipeline 步骤

### Step 1: 加载配置规则

**必须加载**：
- `../../common/通用配置规则.md` — 通用约束（动网保守、License 前置、按依赖顺序生成、参数枚举禁凭记忆）
- `04-command-graph.md` §1 MMLCommand + §5 核心命令参数表 — 确认参数枚举值
- `04-command-graph.md` §4 CommandRule（CR-APN-01~18） — 了解命令级约束
- `03-task-layer.md` §1~§9 ConfigTask + TaskCommandOrderEdge — 确认命令排序
- `kb/03-地址池体系参数.md` + `kb/04-地址分配规则与三级优先级.md` — 地址池参数与规则字符串

**按接入方式维度额外加载**：
- 接入方式=GRE → `kb/07-GRE隧道接入.md`
- 接入方式=IPSec → `kb/08-IPSec隧道接入.md`
- 接入方式=L2TP → `kb/09-L2TP接入.md` + `kb/05-U+C不对称与跨侧一致性.md`
- 鉴权=TRANS_AUTH/NON_TRANS → `kb/06-Radius鉴权链.md`
- 地址类型=IPv6/双栈 → `kb/10-双栈与IPv6承载.md`

### Step 2: 按模板生成命令

根据 4 维度决策（地址分配 × 鉴权 × 接入方式 × 地址类型）的组合，决定生成范围。APN 是单场景但维度组合多样，按维度累加生成。

### Step 3: 按排序规则排列命令

见 §4 排序规则（通用依赖顺序原则引用 `../../common/通用配置规则.md` §5）。

### Step 4: 自检

**必须加载**：
- `01-business-graph.md` §4 BusinessRule（BR-APN-01~16） — 确认业务约束已满足
- `04-command-graph.md` §4 CommandRule（CR-APN-01~18） — 确认命令级约束已满足
- `03-task-layer.md` §10 TaskRule（TR-APN-01~13） — 确认任务级约束已满足

---

## 2. UDG（UPF）侧输出模板

### 2.1 通用前置（License + VPN + APN 实例）

```mml
!-- 1. License 开关（需 License 的维度：双栈/位置/L2TP/IPSec/IPv6承载）
SET LICENSESWITCH:LICITEM="LKV3G5VDSA01",SWITCH=ENABLE;

!-- 2. VPN 实例（IPv4）
ADD L3VPNINST:VRFNAME="{vpn_name}";
ADD VPNINSTAF:VRFNAME="{vpn_name}",AFTYPE=ipv4uni,VRFRD=100:1;
ADD VPNINST:VPNINSTANCE="{vpn_name}";

!-- 2a. VPN 地址族（★双栈/IPv6 必须额外激活 ipv6uni，CR-APN-06）
ADD VPNINSTAF:VRFNAME="{vpn_name_v6}",AFTYPE=ipv6uni,VRFRD=100:2;

!-- 3. APN 实例（跨域共用挂载点）
ADD APN:APN="{apn}",HASVPN=ENABLE,VPNINSTANCE="{vpn_name}";
!-- 双栈场景 HASVPNIPV6 双绑定
ADD APN:APN="{apn}",HASVPN=ENABLE,VPNINSTANCE="{vpn_name}",HASVPNIPV6=ENABLE,VPNINSTANCEIPV6="{vpn_name_v6}";

!-- 4. APN 地址分配属性
SET APNADDRESSATTR:APN="{apn}",SUPPORTIPV4=ENABLE,SUPPORTIPV6=DISABLE;
!-- 双栈 SUPPORTIPV4=ENABLE,SUPPORTIPV6=ENABLE
!-- RADIUS 子方式额外：IGNOREV4POOLID=DISABLE,IGNOREV6POOLID=DISABLE
```

> **参数值必须从 `04-command-graph.md` §5 核心命令参数表获取枚举值，禁止凭记忆填写。**

### 2.2 地址池体系（基于 APN/SMF/LOCATION 三级）

```mml
!-- 5. 地址池（★UDG POOLTYPE 必为 LOCAL，CR-APN-01/04）
ADD POOL:POOLNAME="{pool_name}",POOLTYPE=LOCAL,HASVPN=ENABLE,VPNINSTANCE="{vpn_name}";

!-- 6. 地址段
ADD SECTION:POOLNAME="{pool_name}",SECTIONNUM=1,IPVERSION=IPV4,V4STARTIP="{v4start}",V4ENDIP="{v4end}";
!-- IPv6: IPVERSION=IPV6,V6PREFIXSTART="{v6start}",V6PREFIXEND="{v6end}",V6PREFIXLENGTH=64
!-- PD 模式: V6PREFIXLENGTH<64（CR-APN-05，需 License LKV3G5P6PD01）

!-- 7. 地址池组（双栈需双优先级算法 IPV4ALLOCPRIALG/IPV6ALLOCPRIALG）
ADD POOLGROUP:POOLGRPNAME="{poolgrp_name}",IPV4ALLOCPRIALG=ENABLE;

!-- 8. 地址池绑定到池组（PRIORITY 控制优先级）
ADD POOLBINDGROUP:POOLGROUPNAME="{poolgrp_name}",POOLNAME="{pool_name}",PRIORITY=10;

!-- 9. 池组映射（按粒度组合 APN/SMF/LOCATION）
!-- 基于 APN
ADD POOLGRPMAP:MAPPINGNAME="{map1}",APN="{apn}",POOLGROUPNAME="{poolgrp_name}";
!-- 基于 SMF（需先 ADD CPNODEID + SET IPALLOCBYSMFGLBSW）
ADD CPNODEID:CPNAME="{smf_node}",IPV4NODEID="{smf_ip}";
ADD POOLGRPMAP:MAPPINGNAME="{map2}",SMF="{smf_node}",POOLGROUPNAME="{poolgrp_name}";
!-- 基于位置（需 License LKV3G5LBAA01 + SET IPALLOCBYLOCGLBSW）
ADD LACGROUP:LACGROUPNAME="{lacgrp}";
ADD LACID:LACGROUPNAME="{lacgrp}",LAC={lac};
ADD POOLGRPMAP:MAPPINGNAME="{map3}",LOCATION="{lacgrp}",POOLGROUPNAME="{poolgrp_name}";

!-- 10. 全局三级地址分配规则（★规则字符串严格三段式）
SET IPALLOCRULE:FIRSTRULESW=ENABLE,FIRSTRULE=APN-1&LOCATION-0&SMF-0,SECONDRULESW=DISABLE,THIRDRULESW=DISABLE;
!-- 基于 SMF 子方式额外开全局开关
SET IPALLOCBYSMFGLBSW:SWITCH=ENABLE;
!-- 基于位置子方式额外开全局开关
SET IPALLOCBYLOCGLBSW:IPV4SWITCH=ENABLE,IPV6SWITCH=DISABLE;
```

### 2.3 接口与下行路由发布

```mml
!-- 11. 接口 IP
ADD INTERFACE:IFNAME="{ifname}";
ADD IPBINDVPN:IFNAME="{ifname}",VPNINSTNAME="{vpn_name}";
ADD IFIPV4ADDRESS:IFNAME="{ifname}",IFIPADDR="{v4addr}",SUBNETMASK="{mask}";

!-- 12. 下行路由发布（OSPF 引入 WLR 用户路由）
ADD OSPF:PROCID=100,VRFNAME="{vpn_name}",SCHEMAROUID="{routerid}";
ADD OSPFAREA:PROCID=100,AREAID="0.0.0.0";
ADD OSPFNETWORK:PROCID=100,AREAID="0.0.0.0",IPADDRESS="{network}",WILDCARDMASK="{wildcard}";
ADD OSPFIMPORTROUTE:PROCID=100,TOPOID=0,PROTOCOL=wlr;
!-- IPv6 场景额外 OSPFv3
ADD OSPFV3:PROCID=101,ROUTERID="{routerid_v6}";
```

### 2.4 接入控制 U 面 QoS（可选，GWFD-010151）

```mml
SET APNQOSATTR:APN="{apn}",CARSHAPESWUL=ENABLE,CARSHAPEUL=CAR,CARSHAPESWDL=ENABLE,CARSHAPEDL=CAR;
```

### 2.5 隧道（按接入方式维度选其一）

**见 §3 隧道模板（GRE/IPSec/L2TP）**。

### 2.6 UDG 策略刷新生效（★必须最后）

```mml
!-- 99. 策略刷新生效（地址分配/隧道/QoS 变更后必须；配置链统一终点）
SET REFRESHSRV:;
```

---

## 3. 隧道输出模板（按接入方式维度选其一）

### 3.1 GRE 隧道（IPFD-015002）

```mml
!-- GRE 源接口（推荐 LoopBack，★不能与 IPSec 源地址相同，CR-APN-12/TR-APN-01）
ADD INTERFACE:IFNAME="LoopBack1";
ADD IFIPV4ADDRESS:IFNAME="LoopBack1",IFIPADDR="{src_ip}",SUBNETMASK="255.255.255.255";

!-- GRE 隧道
ADD GRETUNNEL:TNLNAME="{gre_tnl}",TNLTYPE=gre,SRCTYPE=if_name,SRCIFNAME="LoopBack1",DSTIPADDR="{dst_ip}";

!-- 静态路由引导流量进 Tunnel
ADD SRROUTE:AFTYPE=ipv4,PREFIX="{prefix}",MASKLENGTH={masklen},IFNAME="{gre_tnl}";
```

### 3.2 IPSec 隧道（IPFD-015004，UDG + UNC 对称部署）

```mml
!-- IPSec ACL（★仅源/目的 IP，不支持端口，CR-APN-11）
ADD ACLGROUPIPSEC:ACLGROUPNAME="{acl_grp}";
ADD ACLRULEADV4IPSEC:ACLGROUPNAME="{acl_grp}",SRCIP="{src_seg}",DSTIP="{dst_seg}";

!-- IPSec 安全提议
ADD IPSECPROPOSALIPSEC:PROPOSALNAME="{prop}",ENCAPSULATIONMODE=TUNNEL,SECURITYPROTOCOL=ESP;

!-- IKE 提议与对等体（★DH 组不能为 None，CR-APN-10）
ADD IKEPROPOSAL:PROPOSALNAME="{ike_prop}",AUTHMETHOD=PSK,DHGROUP={dhgroup};
ADD IKEPEER:PEERNAME="{ike_peer}",PRESHAREDKEY="{psk}",EXCHANGEMODE=MAIN,REMOTEADDR="{remote_addr}",VERSION1=FALSE;

!-- IPSec 安全策略（聚合 ACL + Proposal + IKE Peer）
ADD IPSECPOLICY:POLICYNAME="{policy}",SEQ=10,MODE=ISAKMP,ACLGROUPNAME="{acl_grp}";
ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="{policy}",SEQ=10,PROPOSALNAME="{prop}";
ADD ATTACHIKEPEER:POLICYNAME="{policy}",SEQ=10,PEERNAME="{ike_peer}",PRIORITY=10;

!-- 应用策略到 Tunnel 接口
ADD IPSECINTFCFGIPSEC:IFNAME="{ipsec_tnl}",TNLTYPE=IPSEC,POLICYNAME="{policy}";
```

### 3.3 L2TP 隧道（GWFD-020412 U 面 LAC 执行 + WSFD-104410 C 面决策）

**UDG 侧（U 面 LAC 执行，★10+ 参数）**：
```mml
!-- L2TP License（仅 UDG 需要，BR-APN-L2TP-CU-ASYM）
SET LICENSESWITCH:LICITEM="LKV3G5L2TP01",SWITCH=ENABLE;

!-- VPN 实例（L2TP 场景）
ADD VPNINST:VPNINSTANCE="vpn_l2tp";

!-- Giif 逻辑接口（L2TP 源端绑定）
ADD LOGICINF:NAME="{giif}",IPVERSION=ipv4,IPV4ADDRESS1="{giif_ip}",IPV4MASK1="{mask}",VPNINSTANCE="vpn_l2tp";

!-- 关闭快速流表（应用限制硬约束）
SET SOFTPARAOFBIT:DT2=BYTE,BYTENUM=671,BYTEPOSITION=7,BYTEVALUE=1;

!-- 方式A：本地配置 L2TP 组
ADD L2TPGROUP:GROUPID=1,DOMAINNAME="{domain}",LOCALNAME="{localname}",LOCALLNSMODE=...,FIRSTLNSIP="{lns_ip}",...;
ADD L2TPCLIENTIP:L2TPGROUPID=1,INTERFACENAME="{giif}";

!-- 方式B：AAA 下发 LNS（与方式A 互斥，CR-APN-14）
ADD L2TPRDSCLIENT:APN="{apn}",INTERFACENAME="{giif}";

!-- ★核心使能命令：SET APNL2TPATTR（U 面 10+ 参数，CR-APN-02）
SET APNL2TPATTR:APN="{apn}",L2TPSWITCH=ENABLE,SUPPORTIPV6=DISABLE,L2TPGROUPID=1,...;

!-- N4 接口加密（可选，★U+C 密钥必须相同，CR-APN-03）
SET L2TPN4KEY:N4KEYVALUE="{key}",CFMN4KEYVALUE="{key}";
```

**UNC 侧（C 面决策，★仅 2 参数，CR-APN-02）**：
```mml
!-- ★C 面决策命令：SET APNL2TPCTRL（仅 APN/L2TPSWITCH 两参数）
SET APNL2TPCTRL:APN="{apn}",L2TPSWITCH=ENABLE;

!-- C 侧 N4 加密（与 UDG L2TPN4KEY 密钥必须相同，CR-APN-03）
SET L2TPKEY:KEYVALUE="{key}",CFMKEYVALUE="{key}";
```

---

## 4. UNC（SMF）侧输出模板

### 4.1 UNC 地址池（仅 UDM 静态签约场景，CS-APN-01/04）

```mml
!-- UNC 地址池（★POOLTYPE 仅 UDM，前缀 ADDRPOOL，CR-APN-01/04）
ADD ADDRPOOL:ADDRPOOLNAME="{addrpool_name}",POOLTYPE=UDM,IPVERSION=IPV4;
ADD SECTION:POOLNAME="{addrpool_name}",SECTIONNUM=1,IPVERSION=IPV4,V4STARTIP="{v4start}";

!-- UNC 地址池组（★命名 ADDRPOOLGRP，绑定 POOLBINDGRP，GRP 非 GROUP）
ADD ADDRPOOLGRP:ADDRPOOLGRPNAME="{addrpoolgrp}";
ADD POOLBINDGRP:ADDRPOOLGRPNAME="{addrpoolgrp}",ADDRPOOLNAME="{addrpool_name}";
ADD POOLBINDAPN:APN="{apn}",ADDRPOOLNAME="{addrpool_name}";
ADD POOLGRPMAP:MAPPINGNAME="{map}",APN="{apn}",ADDRPOOLGRPNAME="{addrpoolgrp}";
```

### 4.2 Radius 鉴权链（仅 TRANS_AUTH/NON_TRANS，TR-APN-02）

> **级联强依赖**：Radius 功能（011306）→ 鉴权接入（011305）→ 二次鉴权（108007），前级必须先激活（BR-APN-RADIUS-CASCADE）

```mml
!-- 1. Radius VPN 与 Gi 接口（AAA VPN）
ADD VPNINST:VPNINSTANCE="vpn_aaa";
ADD LOGICINF:IFNAME="giif1/0/0",LOGICIP="{auth_gi_ip}";   !-- 鉴权 AAA
ADD LOGICINF:IFNAME="giif1/0/1",LOGICIP="{acct_gi_ip}";   !-- 计费 AAA

!-- 2. Radius 服务器组与服务器（三件套共享对象）
ADD RDSSVRGRP:RDSSVRGRPNAME="{rds_grp}";
ADD RDSSVR:RDSSVRGRPNAME="{rds_grp}",SERVERTYPE=AUTHENTICATION,PRIFLAG=PRIMARY,IPVERSION=ipv4,SERVERIPV4="{auth_srv}";
ADD RDSSVR:RDSSVRGRPNAME="{rds_grp}",SERVERTYPE=ACCOUNTING,PRIFLAG=PRIMARY,IPVERSION=ipv4,SERVERIPV4="{acct_srv}";

!-- 3. APN 级 Radius 绑定
ADD APNRDSSVRGRP:APN="{apn}",RDSSVRGRPNAME="{rds_grp}",PRIFLAG=PRIMARY;
ADD APNRDSCLIENTIP:APN="{apn}",INTFNAME="giif1/0/0",CLIENTTYPE=AUTHENTICATION;

!-- 4. APN 鉴权属性（★ACCESSMODE 4 取值，CR-APN: SET APNAUTHATTR）
SET APNAUTHATTR:APN="{apn}",ACCESSMODE=NON_TRANS,COMMONUSERNAME="{user}",COMMONUSERPASS="{pass}",CFMCOMMUSERPASS="{pass}";
!-- TRANS_AUTH 用 COMMONUSERNAME/PASS；TRANS_NON_AUTH/LOC_AUTH 不依赖 Radius
```

### 4.3 二次鉴权扩展（WSFD-108007，DN-AAA 场景，TR-APN-07 强时序）

```mml
!-- ★强时序：NETWORKINSTVPNMAP 必须前置 → UPFRDSSVR 先于 UPFRDSCLIENTIP（CR-APN-08/09）
ADD UPLIST4RDS:UPLISTNAME="{uplist}",UPINSTANCEID="{upf_id}";
ADD CPGTPUADDR:IPVERSION=ipv4,IPV4ADDR="{gtpu_ip}";
ADD NETWORKINSTVPNMAP:VPNINSTANCE="{upf_vpn}";   !-- 必须先于 UPFRDSSVR/CLIENTIP
ADD UPFRDSSVR:SERVERTYPE=AUTHENTICATION,IPVERSION=ipv4,SERVERIPV4="{dnaa_ip}",UPLISTNAME="{uplist}";   !-- 必须先于 CLIENTIP
ADD UPFRDSCLIENTIP:CLIENTYPE=AUTHENTICATION,IPVERSION=ipv4,UPLISTNAME="{uplist}",VPNINSTANCE="{upf_vpn}",CLIENTIPV4="{client_ip}";   !-- ★必须最后，执行后 SMF 立即触发建链
```

### 4.4 UNC 策略刷新生效（★必须最后）

```mml
SET REFRESHSRV:;
```

---

## 5. 排序规则

### 5.1 UDG（UPF）侧（严格顺序，引用 `03-task-layer.md` TaskCommandOrderEdge）

```
 1. SET LICENSESWITCH                   (License 前置门控)
 2. ADD L3VPNINST / VPNINST / VPNINSTAF (VPN 实例与地址族，双栈 ipv6uni)
 3. ADD APN                             (APN 跨域共用挂载点)
 4. SET APNADDRESSATTR                  (APN 地址分配属性)
 5. ADD POOL                            (★UDG POOLTYPE=LOCAL)
 6. ADD SECTION                         (地址段，IPv6/PD 参数差异)
 7. ADD POOLGROUP                       (池组，双栈双优先级算法)
 8. ADD POOLBINDGROUP                   (池绑定池组，PRIORITY)
 9. ADD CPNODEID / LACGROUP / TACGROUP  (SMF NodeID / 位置区组)
10. ADD POOLGRPMAP                      (池组映射，按 APN/SMF/LOCATION 组合)
11. SET IPALLOCRULE / APNIPALLOCRULE    (三级规则)
12. SET IPALLOCBYSMFGLBSW / IPALLOCBYLOCGLBSW (子方式全局开关)
13. ADD CONFLICTIP                      (冲突地址，可选)
14. ADD INTERFACE / IPBINDVPN / IFIPV4ADDRESS (接口)
15. ADD OSPF / OSPFIMPORTROUTE / OSPFV3 (下行路由发布)
16. ADD GRETUNNEL / IPSECPOLICY / APNL2TPATTR (隧道，按接入方式)
17. SET APNQOSATTR                      (U 面 QoS，可选)
18. SET REFRESHSRV                      (★策略刷新生效，必须最后)
```

### 5.2 UNC（SMF）侧

```
1. SET LICENSESWITCH                    (License 前置，UNC 侧需 License 的特性)
2. ADD ADDRPOOL / SECTION               (★UNC POOLTYPE=UDM，仅静态签约)
3. ADD ADDRPOOLGRP / POOLBINDGRP / POOLBINDAPN / POOLGRPMAP (池组映射)
4. ADD VPNINST / LOGICINF               (Radius AAA VPN + Gi 接口)
5. ADD RDSSVRGRP / RDSSVR / APNRDSSVRGRP / APNRDSCLIENTIP (Radius 三件套，鉴权场景)
6. SET APNAUTHATTR                      (★ACCESSMODE 4 取值，鉴权场景)
7. ADD UPLIST4RDS / CPGTPUADDR / NETWORKINSTVPNMAP / UPFRDSSVR / UPFRDSCLIENTIP (二次鉴权，★强时序)
8. SET APNL2TPCTRL / SET L2TPKEY        (L2TP C 面决策，仅 2 参数)
9. ADD APNACTNUM                        (并发限制，可选)
10. SET REFRESHSRV                      (★策略刷新生效，必须最后)
```

> **详细依赖链**加载 `03-task-layer.md` §1~§9 的 TaskCommandOrderEdge 确认。

---

## 6. 配置决策指南

以下场景需要 Agent 从图谱/知识库获取业务规则后做出实现决策：

### 6.1 地址分配方式 × POOLTYPE 映射

| DP-APN-ADDR-MODE | UDG POOLTYPE | UNC 是否需 ADDRPOOL | 全局开关 |
|------------------|-------------|---------------------|---------|
| UPF-APN/UPF-SMF/UPF-LOCATION 动态 | LOCAL | 否 | IPALLOCBYSMFGLBSW / IPALLOCBYLOCGLBSW |
| SMF 本地动态 | （U 面 SMF 决策） | 否 | — |
| UDM 静态签约 | （不建池） | ★UDM（UNC 侧） | — |
| RADIUS 下发 | LOCAL（IGNOREV4POOLID=DISABLE） | 否 | — |
| DHCP 代理 | （UNC 代理） | 否 | — |
| LNS (L2TP) | （LNS 分配） | 否 | — |

### 6.2 双栈叠加（CS-APN-03/04/09）

- 双栈 = IPv4 VPN + IPv6 VPN 双实例（CR-APN-06: VPNINSTAF AFTYPE=ipv6uni）
- 双栈 = IPv4 POOL + IPv6 POOL 双池双段
- 双栈 = POOLGROUP 双优先级算法 IPV4ALLOCPRIALG + IPV6ALLOCPRIALG
- 双栈 License 串联：LKV3G5V6PB01（承载）→ LKV3G5VDSA01（双栈使能），BR-APN-IPV6-CASCADE

### 6.3 ACCESSMODE × Radius 依赖分支（TR-APN-02）

| ACCESSMODE | 调用 Radius | Radius 三件套 | COMMONUSERNAME/PASS |
|-----------|------------|--------------|---------------------|
| TRANS_NON_AUTH | 否 | 不配置 | 不需要 |
| TRANS_AUTH | 是 | 配置 | 需要（公用） |
| NON_TRANS | 是 | 配置 | 不需要（UE PCO 携带） |
| LOC_AUTH | 否 | 不配置 | 需要（本地） |

### 6.4 GRE over IPSec

GRE-over-IPSec 场景需先建 GRE 再叠加 IPSec，**GRE 源地址不能与 IPSec 源地址相同**（CR-APN-12 / TR-APN-01），用不同 LoopBack 接口分离源地址。

### 6.5 L2TP 本地配置 vs AAA 下发（CR-APN-14）

| 方式 | 命令 | LNS 参数来源 |
|------|------|-------------|
| 方式A 本地配置 | ADD L2TPGROUP + L2TPCLIENTIP | L2TPGROUP 配置 |
| 方式B AAA 下发 | ADD L2TPRDSCLIENT | Radius Access-Accept 下发 |

两者互斥，不可同时配置。SET APNL2TPATTR 方式A 指定 L2TPGROUPID，方式B 指定 RDSLNSMODE。

### 6.6 兜底（多级规则回退）

地址分配三级规则匹配失败时分配失败。需兜底时启用 SECONDRULE/THIRDRULE，规则字符串按维度组合（如 FIRSTRULE=SMF+APN，SECONDRULE=SMF 兜底）。

---

## 7. 注意事项

- 每个参数的枚举值必须从 `04-command-graph.md` §5 核心命令参数表获取，不可自行推断
- **UDG/UNC 命令前缀不对称**是 APN 最高频错误：POOL↔ADDRPOOL、POOLGROUP↔ADDRPOOLGRP、POOLBINDGROUP↔POOLBINDGRP（GRP 非 GROUP）、APNL2TPATTR↔APNL2TPCTRL（CR-APN-01/02，TR-APN-03）
- **POOLTYPE 跨侧差异**：UDG=LOCAL，UNC=UDM（CR-APN-04），两侧同名参数取值集不同
- **双栈 License 串联**：承载→双栈→PD，前级必须先激活（BR-APN-IPV6-CASCADE）
- **V6PREFIXLENGTH 分水岭**：=64 普通 IPv6 单栈，<64 PD 模式（CR-APN-05）
- **L2TP C-U 不对称**：U 侧 10+ 参数 vs C 侧 2 参数；L2TPN4KEY/L2TPKEY 密钥必须相同（CR-APN-02/03）
- **Radius 级联链**：功能→鉴权→二次鉴权，前级必须先激活（BR-APN-RADIUS-CASCADE）
- **二次鉴权强时序**：NETWORKINSTVPNMAP → UPFRDSSVR → UPFRDSCLIENTIP（CR-APN-08/09，TR-APN-07）
- **IPSec IKE DH 组不能为 None**（CR-APN-10），**ACL 仅源/目的 IP 不支持端口**（CR-APN-11）
- **GRE 与 IPSec 源地址互斥**（CR-APN-12 / TR-APN-01）
- **APN 是跨域共用挂载点**：APN 同时被地址分配/鉴权/L2TP/QoS/多PDN 引用，修改必须评估影响范围
- **REFRESHSRV 必须最后**（仅触发下发动作，U+C 各一个）
- **LOC_AUTH 不支持 PPP 用户**（BR-APN-LOC-AUTH-NO-PPP）
- 通用约束（动网保守、License 前置、按依赖顺序生成、跨网元参数一致）引用 `../../common/通用配置规则.md`，本文件不复述
