# 知识融合 Part C: 配置命令、方案设计、故障运维、特殊场景

> 融合来源: draft-batch-03-04 (K114-K131), draft-batch-03-05 (K132-K156), draft-batch-04 (K157-K172), draft-batch-06 (K270-K310), draft-batch-07 (K250-K265)
> 融合日期: 2026-06-04
> 编号范围: K201-K261
> 去重规则: 同一知识点多批次覆盖时合并为一条，保留所有来源编号

---

## 第十二章：融合计费配置全景

### K201: 融合计费配置五层嵌套模型 `[隐性规则]`
> 来源: K114 (归纳自故障案例1-3)

融合计费配置是五层嵌套结构，任何一层配置错误都导致下游功能异常：

| 层级 | 配置项 | 命令 | 说明 |
|------|--------|------|------|
| L1 计费模式 | CHGMODE | SET CHGMODE | 设为NchfMode才走N40接口 |
| L2 融合计费使能 | CHARGECTRL | SET CHARGECTRL / SET USRPROFCHARGE / SET APNCHARGECTRL | 按用户/APN粒度使能 |
| L3 CHF交互使能 | CHFINIT | SET CHFINIT | 设为SENDREQ才在激活时发Initial |
| L4 RG配置 | URR/URRGROUP | ADD/MOD URR / ADD/MOD URRGROUP | 定义RG和计费方式 |
| L5 Rule绑定 | RULE/PCCPOLICYGRP | ADD/MOD RULE / ADD/MOD PCCPOLICYGRP | 将RG绑定到业务匹配规则 |

---

### K202: 方案一组网与12步配置依赖链 `[方案设计]`
> 来源: K132

未部署NCG方案：网络侧仅SMF，运营商侧部署CHF(OCS)。仅支持融合计费，SGW-C不支持。

**SMF侧配置依赖链（12步顺序）**：
1. SET LICENSESWITCH（License）
2. SET CHARGECTRL（融合计费开关）
3. SET CHGMODE（接口模式=NchfMode）
4. ADD CHARGECHAR / SET GLBCHARGECHAR（计费属性CC）
5. ADD CCT / MOD CCT（融合计费模板）
6. ADD PDUTRIGGER / ADD RGTRIGGER（Trigger交互条件）
7. SET N40APIVER（N40 API版本）
8. SET FAILHANDLING / ADD PDUSCACT / ADD RGRCACT（异常处理）
9. ADD URR / ADD URRGROUP / ADD PCCPOLICYGRP（费率标识三件套）
10. ADD TARIFFGROUP（费率切换，可选）
11. ADD TNFINS / ADD TNFGRP / SET CHFSELECTMODE（CHF选择）
12. SET N40MSGSTG（消息缓存，可选）

**网元协同**：UPF(规则/URR/策略) + PCF(配额/规则/策略) + SMF三方配置必须一致。

---

### K203: 计费License项 `[配置]`
> 来源: K133

| 特性 | License控制项 |
|------|-------------|
| 融合计费 | WSFD-011206 |
| 内容计费 | LKV3W9BCC12 |
| 时长计费 | LKV3W9TBCS12 |
| 流量计费 | LKV3WPVBCS11 |
| 事件计费 | LKV3W9EBCS12 |

命令：SET LICENSESWITCH，必须最先配置。

---

### K204: 融合计费开关配置 `[配置]`
> 来源: K134

优先级：PCF下发 > User Profile(SET USRPROFCHARGE) > DNN(SET APNCHARGECTRL) > 计费属性(ADD CHARGEMETHOD) > 全局(SET CHARGECTRL)

**SET CHARGECTRL关键参数**：
- HOMECONVERGED/VISITCONVERGED/ROAMCONVERGED=ENABLE（对应的ONLINE/OFFLINE必须DISABLE）
- RGAPPLIED：业务申请上报模式（ONLINERGONLY / OFFLINERGONLY / DEFAULT）

**RGAPPLIED约束（隐性规则）**：
- RGAPPLIED=DEFAULT时：URRGROUP中**不能**同时配RG相同的离线和在线URR
- RGAPPLIED=ONLINERGONLY或OFFLINERGONLY时：建议同时配离线和在线URR

---

### K205: 计费接口模式全景 `[配置]`
> 来源: K135, K272, K273, K274, K275, K276, K277

#### 接口选择优先级

计费接口选择有三级优先级（从高到低）：
1. **基于用户漫游属性** (ADD ROAMCHGMODE) — 最高优先级
2. **基于APN/DNN** (ADD APNCHGMODE) — 中等优先级
3. **全局配置** (SET CHGMODE) — 最低优先级（兜底）

策略接口选择有两级优先级：基于APN/DNN > 全局配置。

#### SET CHGMODE按终端和接入类型选择

SET CHGMODE命令通过TMACCTYPE（终端和接入类型）参数区分不同场景：
- **UE5G_RAT5G**：5G终端接入5G网络（SMF场景，典型用NchfMode）
- **UE5G_RAT4G**：5G终端接入4G网络（PGW-C场景，可选NchfMode或GaGyMode）
- **UENON5G_RAT4G**：非5G终端接入4G网络（PGW-C场景，典型用GaGyMode）
- **RAT2G/RAT3G**：2G/3G接入（GGSN场景，典型用GaGyMode）
- **RATNBIOT**：NB-IoT终端接入
- **RATLTEM**：LTE-M终端接入
- **NON_3GPP**：非3GPP网络接入

FORCED参数指定计费接口：NchfMode（融合计费）或GaGyMode（传统离线+在线）。

#### 5GS互操作指示(BY5GSIWKI)

BY5GSIWKI参数控制是否根据对端携带的"5GS Interworking Indication"参数选择计费接口：
- BY5GSIWKI=True时：对端携带"5GS Interworking Indication"为1则选Nchf，为0或未携带则选GaGy
- BY5GSIWKI=False时：不根据互操作指示判断，直接使用FORCED指定的计费接口
- 典型用法：ADD APNCHGMODE中按APN级别配置，5G终端4G接入时根据互操作指示灵活选择

#### V-SMF和I-SMF的计费模式

SET CHGMODE中与SMF角色相关的参数：
- **FORVSMFONLY**：UNC作为V-SMF时的计费模式，典型配置NchfMode
- **ISMFCHGSW**：I-SMF是否支持计费，典型配置DISABLE（I-SMF不进行计费）

#### 基于PCF实例标识决策接口(ADD PCCCHGMODEBYPCFID)

当需要基于PCF实例标识调整用户最终使用的计费/策略接口时使用：
- 以SET CHGMODE或ADD APNCHGMODE为初选结果
- 在此基础上决策：是否由N40回落GaGy，或由GaGy升级为N40
- 策略接口类型：N7（5G PCF）或Gx（4G PCRF）
- 计费接口类型：INHERIT（继承初选结果）或指定N40/GaGy

#### SET POLICYMODE策略接口选择

- FORCED=Npcf：使用5G PCF（N7服务化接口）
- FORCED=Gx：使用4G PCRF（Diameter接口）
- PCFRESELBYPCFID：是否基于PCF实例标识决策策略接口类型
- 典型配置：5G终端4G接入和非5G终端4G接入用Npcf，2G/3G/NB-IoT/LTE-M/非3GPP用Gx

#### 2/3/4/5G共存网络典型配置

| 接入场景 | UNC角色 | 计费接口 | 策略接口 |
|----------|---------|---------|---------|
| 5G终端+5G接入 | SMF | NchfMode | Npcf |
| 5G终端+4G接入 | PGW-C | 按互操作指示选Nchf/GaGy | Npcf |
| 非5G终端+4G接入 | PGW-C | GaGyMode | Npcf或Gx |
| 2G/3G接入 | GGSN | GaGyMode | Gx |
| NB-IoT/LTE-M | GGSN/PGW-C | GaGyMode或NchfMode | Gx或Npcf |

---

### K206: CC属性配置全景 `[配置]`
> 来源: K136, K259, K260, K261

#### CC标准取值

| 取值 | 含义 |
|------|------|
| 0x0100 | 热计费(Hot Billing) |
| 0x0200 | 统一费率(Flat Rate) |
| 0x0400 | 预付费(Prepaid) |
| 0x0800 | 普通计费(Normal Billing) |

#### CC四级优先级

| 优先级 | 来源 | 说明 |
|--------|------|------|
| 1（最高） | UserProfile下的配置 | 用户级配置 |
| 2 | APN/DNN下的配置 | 接入点级配置 |
| 3 | 全局配置 | 全局默认 |
| 4（最低） | normal（普通计费） | 兜底默认 |

如果高级别参数没有配置，则依次向下使用低一级别的参数取值。

CC来源优先级补充：RADIUS Server下发 > User Profile > DNN > 全局 > normal(默认)

命令：SET GLBCHARGECHAR(全局) / ADD CHARGECHAR(CC实例) / SET USRPROFCHARGE(绑定UP) / SET APNCHARGECTRL(绑定DNN)

#### 本地CC与签约CC的选择控制

本地CC与签约CC的选择受两类命令控制，核心参数为HOMESGSN、ROAMSGSN、VISITSGSN（分别控制本地、漫游、拜访用户）：

| 场景 | 控制命令 | ENABLE含义 | DISABLE含义 |
|------|----------|-----------|------------|
| 基于UserProfile/APN/DNN配置CC | ADD CHARGECHAR | 使用签约下发的CC | 使用本地配置的CC |
| 基于全局配置CC | SET GLBCHARGECHAR | 使用签约下发的CC | 使用本地基于全局配置的CC |

决策逻辑：先按四级优先级确定本地CC，再根据HOMESGSN/ROAMSGSN/VISITSGSN的ENABLE/DISABLE决定是否用签约CC覆盖本地CC。

#### 各网络制式下签约CC的来源网元

| 网络制式 | UNC角色 | 签约CC来源 |
|----------|---------|-----------|
| 5G | SMF | UDM下发 |
| 4G（SP合设） | SGW-C + PGW-C | 左侧MME携带（MME从HSS获取） |
| 4G（SP分离，UNC=SGW-C） | SGW-C | 左侧MME携带 |
| 4G（SP分离，UNC=PGW-C） | PGW-C | 左侧SGW-C携带 |
| 2/3G | GGSN | 左侧SGSN携带 |

规律：4G网络中签约CC统一由左侧MME/SGW-C携带；5G由UDM下发；2/3G由SGSN携带。

---

### K207: 融合计费模板(CCT)配置 `[配置]`
> 来源: K137

CCT模板粒度优先级：User Profile > DNN > 计费属性(CC) > global(整机)

**ADD CCT关键参数**：
- QHT：配额空闲时间门限(秒)
- VQT/TQT/UQT：流量/时间/事件阈值触发百分比
- VT：在线配额有效时长(分)
- PDUVOLUMELIMIT/PDUTIMELIMIT：PDU级阈值
- RGVOLUMELIMIT/RGTIMELIMIT：RG(业务)级阈值
- MAXSVCCONTAINER：最大业务容器数
- FUATERMINATE：最终配额动作终结方式

绑定：ADD SELECTCCTBYCC(CC粒度) / SET APNCHARGECTRL(DNN粒度) / SET USRPROFCHARGE(UP粒度)

---

### K208: Trigger配置 `[配置]`
> 来源: K138

**SET CHFINIT**：PDU会话建立时是否与CHF交互
- CHFINIT=SENDREQ：激活时发送Initial
- CCRINITRGNUM：初始RG个数
- RGSOURCE：RG来源（DEFAULT / CTXSTARTRATING）

**Trigger三级取值**：IMMEDIATE(立即上报) / DEFERRED(延迟上报) / NONREPORT(不上报)

**Session级Trigger (ADD PDUTRIGGER)**：QOSCHG, ULCHG, SRVNDCHG, PLMNCHG, RATCHG, TAICHG, TIMELIMIT, VOLUMELIMIT, EVENTLIMIT, SESSAMBRCHG, ADDUPF

**RG级Trigger (ADD RGTRIGGER)**：额外包含QUOTATHRESHOLD(配额阈值), VT(配额有效时长), QHT(配额保持时长)

**隐性规则**：
- Session级和RG级同一Trigger冲突时，Session级优先。Session级"不上报"时才按RG级生效
- Trigger来源：CHF下发（Response的triggers信元）+ SMF本地配置
- 建议每用户上报间隔>30秒，避免SMF和CHF频繁交互

---

### K209: N40 API版本配置 `[配置]`
> 来源: K139

SET N40APIVER：
- APIVER：版本号（如F30），需与CHF一致
- FEATURE：增强功能集，支持&叠加（NODEFUNC-1, NBIOTCHG-1, LTEMCHG-1, UTRANCHG3GPP-1等）

---

### K210: 异常返回码处理配置 `[配置]`
> 来源: K140

异常处理三粒度：整个用户 > PDU会话 > RG

**SET FAILHANDLING**：
- FHACTION=CONTINUE（放通）/ 其他
- FAILOVERSUP=ENABLE（支持failover）
- TXTIMER：Tx定时器时长(秒)
- HOLDINGTIME：用户保持时长(分)
- CNVCHGRECOVER：融合计费自动恢复开关

**ADD PDUSCACT**：PDU级异常返回码动作（如502→FAILOVER）
**ADD RGRCACT**：RG级异常码动作（如QUOTAMNOTAPPL→BLCK_IMMED_RPT）
**SET CNVRGDCHGPARA**：BADRSPACT=CONTINUE/Terminate，忽略CHF响应信元列表

---

### K211: 费率切换配置 `[配置]`
> 来源: K147

粒度优先级：User Profile > APN > CC > 整机

命令：ADD FESTIVAL(节假日) → ADD WEEKDAY(星期表) → ADD TARIFFGROUP(时间段) → SET N40QUOTACTRL(TCMODE: DEFAULT/DAILY/MONTHLY) → 绑定(SET APNCHARGECTRL或SET USRPROFCHARGE)

约束：CCVALUE不能为0x0200(统一费率)，每DNN/UP只能绑一个费率切换组。

---

### K212: 计费消息缓存配置 `[配置]`
> 来源: K148

场景：主备CHF均故障时SMF缓存计费消息。

前提：SET FAILHANDLING的FHACTION=CONTINUE。此功能为定制能力，要求对端为华为NCG。

命令：SET N40MSGSTG(缓存开关+回放间隔/速率) → SET STGTRIGGER(缓存期间trigger) → SET CNVRGDCHGPARA(CHGDATAREFGEN=SMF) → SET CDRSTORAGECTRL(超期天数) → SET N4CHGMSGCTRL(缓存池扩展)

---

### K213: CHF选择配置全景 `[配置]`
> 来源: K145, K155, K156

#### CHF选择优先级（高到低）

1. ADD SELCHFGBYIMSI（基于IMSI，测试用）
2. ADD SELCHFGBIMSISEG（基于IMSI号段）
3. 基于PCF下发FQDN
4. 基于UDM签约CC
5. 基于标准化NRF服务发现
6. ADD SELECTCHFGBYCC（基于SMF本地CC）

配置命令链：ADD TNFINS(CHF实例) → ADD TNFINSIP(IP) → ADD TNFGRP(CHF组) → ADD TNFBINDGRP(绑定) → SET CHFSELECTMODE → SET GLBDFTCHFGROUP → ADD SELECTCHFGBYCC

#### 基于IMSI选择CHF的三层配置

1. ADD TNFINS(CHF实例) + ADD TNFINSIP(IP) — SRVNAME固定取**NchfConvCharg**
2. ADD TNFGRP(CHF组) + ADD TNFBINDGRP(实例绑定组)
3. ADD SELCHFGBYIMSI(IMSI绑定主备CHF组)

#### IMSI-CHF绑定的实时生效限制 `[隐性规则]`

MOD SELCHFGBYIMSI修改后，已激活用户**不会立即**切换CHF。必须去激活后重新激活才能生效。不支持在线切换CHF。

**建议**：配置缺省CHF组避免选不到CHF。FQDN需与PCF下发一致。

---

## 第十三章：计费三件套配置

### K214: 融合计费三件套配置命令 `[配置]`
> 来源: K141

**ADD URR**(SMF侧)：
- URRNAME, URRID（**SMF和UPF必须一致**）
- USAGERPTMODE：ONLINE / OFFLINE
- ONLCOMPOUNDTYPE/OFFCOMPOUNDTYPE：ONLYRG
- ONLINERG/RG：费率组编号
- ONLMETERINGTYPE/OFFMETERINGTYPE：VOLUME / DURATION / FREE

**ADD URRGROUP**：
- URRGROUPNAME
- UPURRNAME1/DOWNURRNAME1：第1组上下行URR
- UPURRNAME2/DOWNURRNAME2：第2组上下行URR（1/2仅为编号，无优先级语义）

**ADD PCCPOLICYGRP**：
- PCCPOLICYGRPNM, URRGROUPNAME

**ADD RULE**：RULENAME, POLICYTYPE=PCC, PRIORITY, POLICYNAME

**ADD QUOTAEXHAUSTACT**：在线RG配额耗尽后动作（BLOCK / REDIRECT / FORWARD）

---

### K215: UPF侧配置流程 `[配置]`
> 来源: K142

UPF配置5步：
1. ADD URR + ADD URRGROUP（URR组）
2. ADD PCCPOLICYGRP（PCC策略组）
3. ADD FILTER / ADD L7FILTER / ADD FLOWFILTER / ADD FLTBINDFLOWF / ADD PROTBINDFLOWF（过滤规则）
4. ADD RULE + ADD USERPROFILE + ADD RULEBINDING
5. SET URRGRPBINDING + SET SPECTRAFURRGRP（默认URR组）

**隐性规则**：
- FLOWFILTER必须绑定过滤条件，否则匹配失败
- 只绑定L34的Rule优先级应**低于**绑定L7的Rule
- any Rule优先级设最低(如65000)
- **SET REFRESHSRV必须最后执行**，否则Filter变更不生效

---

### K216: SET SPECTRAFURRGRP — 特殊流量计费兜底 `[配置]`
> 来源: K143

SET SPECTRAFURRGRP配置全局缺省URR组，用于：
1. 七层未匹配已转发流量（特殊流量）
2. 无URR配置的业务

当BIT1232软参值=1时特殊流量通过该规则组计费。

---

### K217: 跨网元名称一致性要求汇总 `[隐性规则]`
> 来源: K144

| 配置项 | 一致性要求 | 涉及网元 |
|--------|-----------|----------|
| USERPROFILENAME | 必须一致 | PCF, SMF, UPF |
| RULENAME | 必须一致 | SMF, UPF |
| RULE.POLICYTYPE+POLICYNAME | 必须一致 | SMF, UPF |
| URRID | 必须一致 | SMF, UPF |
| USAGERPTMODE | 必须一致 | SMF, UPF |
| ONLMETERINGTYPE/OFFMETERINGTYPE | 必须一致 | SMF, UPF |
| 配额名称(Quota) | PCF配额名须与CHF侧一致 | PCF, CHF |
| FQDN | SMF的TNFINS.FQDN须与PCF下发一致 | SMF, PCF |

---

### K218: 内容计费验证链 `[方案设计]`
> 来源: K149

内容计费逐级验证链：
1. LST RULEBINDING → UserProfile绑定的RULE
2. LST RULE → RULE绑定的FlowFilter和PCCPOLICYGRP
3. LST PCCPOLICYGRP → PCC策略组绑定的URRGROUP
4. LST URRGROUP → URR组中的上下行URR
5. LST URR → 最终URR的ID和计费模式

七层内容计费还需验证：LST PROTBINDFLOWF → LST FLOWFILTER → LST L7FILTER

---

### K219: 内容计费双License要求 `[配置]`
> 来源: K150

内容计费需**两个**License同时开启：
- UNC侧：LKV3W9BCC12
- UDG侧：LKV3G5BCBC01

两处必须均为ENABLE才能正常使用。

---

### K220: URR ID在PFCP信令中的编码规则 `[原理]`
> 来源: K151

Usage Report中URR ID编码：高位80代表URR是预定义类型（UPF本地配置），低位代表UPF本地URR ID。
示例：0x80000001(2147483649) → 预定义标志 + URR ID=01

调测时需做进制转换对照。

---

### K221: 带配额管理的融合计费E2E调测流程 `[方案设计]`
> 来源: K152

端到端调测关键步骤：
1. 双License检查
2. 用户激活 → 验证Initial消息
3. 验证Initial携带的RG
4. 用户访问新业务 → UPF上报新URR ID → SMF下发Create URR
5. Trigger条件满足 → 验证Update消息
6. 用户去激活 → 验证Termination消息中流量一致性

---

### K222: URRFAILACTION — 新业务无URR时的容灾 `[配置]`
> 来源: K153

UNC未配置新业务URR时，新业务被阻塞。通过`SET URRFAILACTION: RETRYFAILACT=CONTINUE`可放通。
这是一个重要容灾配置，允许计费规则未完全配置时仍保障业务可用性。

---

### K223: 计费三件套修改命令链 `[配置]`
> 来源: K154

新业务配额下发失败时，需执行完整修改链：
```
MOD URR → MOD URRGROUP → MOD PCCPOLICYGRP → MOD RULE
```
体现URR→URRGROUP→PCCPOLICYGRP层级修改顺序，最终通过RULE下发给用户。

---

## 第十四章：PCF策略配置

### K224: PCF下发的计费参数全集(ChargingData) `[原理]`
> 来源: K157

PCF通过ChargingData动作组下发计费参数：

| 参数 | 含义 | 必选 |
|------|------|------|
| chgId | 计费控制策略数据标识 | 必选(1次) |
| meteringMethod | 离线计量方式：DURATION/VOLUME/DURATION_VOLUME/EVENT | 可选 |
| offline | 是否离线计费 | 可选 |
| online | 是否在线计费 | 可选 |
| ratingGroup | 费率组(RG) | 可选 |
| reportingLevel | 上报级别：SER_ID_LEVEL/RAT_GR_LEVEL/SPON_CON_LEVEL | 可选 |
| serviceId | 服务标识(SID) | 可选 |
| sponsorId | 赞助商标识 | 可选 |
| sdfHandl | 在线等待信用响应时是否允许通过 | 可选(仅在线) |

---

### K225: offline/online互斥规则 `[隐性规则]`
> 来源: K158

- offline和online**不能同时为true**，但可同时为false（不计费）
- 优先级：PCF下发 > SMF本地配置
- 两者都不存在或都为false时，使用PDU会话的**默认计费方法**
- sdfHandl仅用于在线计费场景
- meteringMethod为离线专用参数

---

### K226: 三种规则类型与计费信息携带方式 `[原理]`
> 来源: K159

| 维度 | 动态规则 | 预定义规则 | 本地规则 |
|------|----------|------------|----------|
| 流条件 | PCF配置 | UPF配置 | UPF配置 |
| 流动作 | PCF配置 | UPF配置 | UPF配置 |
| 规则名一致性 | 不需要 | PCF/SMF/UPF三侧一致 | SMF/UPF两侧一致 |
| 业务识别 | 不识别（非定向流） | UPF识别（三四层+七层） | UPF识别 |
| 计费控制 | PCF通过ChargingData下发 | UPF本地配置计费动作 | UPF本地配置 |
| 适用场景 | 非定向流、达量限速 | 定向流（需识别特定业务） | PCF故障降级方案 |

---

### K227: 5G动态规则必配动作组 `[配置]`
> 来源: K160

5G DynamicPccRule完整配置需7种动作类型：
1. FlowDescription（流描述）
2. FlowInformation（流信息）
3. TrafficControlData（flowStatus=enabled，配流描述时必须配）
4. Arp（优先级参数）
5. QoSData（带宽参数：5qi, maxbrUl, maxbrDl）
6. UsageMornitoringData（配额监控键值，业务关联配额时必须通过5G动作组下发）
7. DynamicPccRule（汇总动作）

4G/5G差异：条件组Object选择4G选"IPSession"，5G选"SmfSession"；策略类型4G为"Gx Policy"，5G为"N7 Policy"。

---

### K228: PCF侧配置流程 `[配置]`
> 来源: K146

PCF融合计费配置流程：
1. 配置配额(Quota) — 名称须与CHF侧一致
2. 配额状态映射 — Sy协议状态(0/1/2/5) → UPCF状态(Normal/Level1/Level2/Exhaust)
3. 配置条件组 — 基于QuotaStatus匹配
4. 配置5G动作组 — PredefinedPccRule类型，pccRuleId指定预定义规则名
5. 配置规则 — 类型"5G Smf Pcc Rule"
6. 配置策略 — 策略类型N7 Policy
7. ADD PSUB(用户) + ADD PSRV(签约业务)

前提：N28接口开关已启用(VRM_SYSWITCH设为1/2/3)。

---

## 第十五章：方案设计知识

### K229: 配额类型与触发器 `[原理]`
> 来源: K161

配额类型（PCF用于策略计算）：
- **流量配额**：UPCF统计的用户业务流量
- **在线时长配额**：UPCF统计的在线会话时长
- **时长配额**：SMF上报的时长

**关键触发器**：
- IPCAN_EST：PDU会话建立（必须配置）
- US_RE：使用量状态上报（配额变化触发策略更新）
- SAREA_CH/PRA_CH/SCELL_CH/PLMN_CH：位置变更
- APP_STA/APP_STP：应用类型变更
- TimeRangeChange：时间范围变更

---

### K230: 多业务拆解6步法 `[方案设计]`
> 来源: K162

多业务拆解方法：**抽取 → 合并 → 排查 → 规则类型判断 → 触发器选择 → 业务关系判断**

关键步骤：
- 合并：条件相同的动作合并或动作相同的条件合并
- 排查：确认条件完备（如"配额未耗尽"+"配额耗尽"=全部状态）
- 触发器选择：IPCAN_EST + US_RE（配额变化）+ 可选TimeRangeChange
- 业务互斥：通过互斥组定义多业务间关系（订购互斥/激活互斥）

---

### K231: 基于用户等级的资费差异化控制 `[方案设计]`
> 来源: K163

用户等级→费率/带宽映射：

| 用户等级 | RatingGroup | 上下行带宽 |
|----------|-------------|------------|
| Gold | RG=1 | 100 Mbps |
| Silver | RG=2 | 50 Mbps |
| Normal | RG=3 | 10 Mbps |

PCF配置：3个规则(Rule_Gold/Silver/Normal)，每个规则动作组包含ChargingData(设置ratingGroup) + QoSData(设置带宽)。用户等级变更由业务发放系统通过订阅通知推送。

---

### K232: 多业务场景配额+时间约束组合 `[方案设计]`
> 来源: K164

场景1（基础流量包）：配额未耗尽→10Mbps；配额耗尽→1Mbps+通知。触发器：IPCAN_EST + US_RE

场景2（周末流量包）：配额未耗尽→100Mbps（仅周末）；配额耗尽→终止业务+通知。触发器：IPCAN_EST + US_RE + **TimeRangeChange**

业务互斥：场景2优先级高于场景1，使用"激活+替换"互斥模式。

---

### K233: 配额耗尽重定向完整控制链 `[方案设计]`
> 来源: K165

配额耗尽后完整控制：**限速(1Kbit/s) + 发送提醒通知 + 重定向到充值页面**

**动态规则方案（仅PCF配置）**：
- Rule_Normal：条件=配额未耗尽，动作=QoSData(100Mbit/s)
- Rule_Exhaust：条件=配额耗尽，动作=QoSData(1Kbit/s) + RedirectInformation

**预定义规则方案（PCF+SMF+UPF三方配置）**：
- PCF侧：下发规则名Rule_Normal和up_Exhaust
- SMF侧：识别预定义规则名，配置URR/URRGROUP/PCCPOLICYGRP/RULE
- UPF侧：配置流过滤器+QoS+重定向URL(ADD REDIRECT)+PCCPOLICYGRP+RULE

**隐性规则**：SMF配预定义规则级则UPF配规则级；SMF配规则组级则UPF须配规则组级。配额耗尽场景需用**预定义规则组**。

---

### K234: FUP达量限速配置实例 `[方案设计]`
> 来源: K166

需求：2000MB配额，<100%时10Mbit/s，>=100%时512Kbit/s。

5G配置方案：
- AG_Basic：SessionRuleAction（缺省QoS Flow）
- AG_Basic_Dyn：DynamicPccRule（rule01, maxbr=10000Kbit/s, umId=2001）
- predefinedPccRule01：pccRuleId=Pre_Quota_exhaust（配额耗尽时激活预定义规则）
- 策略：Policy_usage，trigger=US_RE OR IPCAN_EST
- 配额：quota01, MonitorKey=2001, Value=2048000, Slice=100%

---

## 第十六章：特殊场景

### K235: ULCL多锚点计费全景 `[方案设计]`
> 来源: K167, K168, K262

#### 计费架构

- 主锚点PSA0(Internet) + 辅锚点PSA1(本地DN) + UL CL UPF(分流器，通常与PSA1合设)
- SMF将计费规则通过N4接口分别下发到PSA0和PSA1
- CHF对每个锚点UPF**独立进行配额管理**，每个UPF**独享配额**
- SMF按UPF向CHF申请配额，消息中Multiple Unit Usage携带UPF ID
- **UL CL UPF不计费**：UL CL UPF没有计费规则，仅负责分流

核心原则：UL CL只分流、不计费；计费在锚点UPF按各自的URR独立执行。

#### 系统约束 `[隐性规则]`

- UL CL仅针对5G用户，2/3/4G不支持
- 国漫V-SMF场景下不支持UL CL
- 当前版本仅支持UL CL UPF和辅锚点UPF**合一部署**
- **UL CL方案只支持融合计费**

---

### K236: 3GPP PS Data Off功能 `[原理]`
> 来源: K125

PS Data Off解决UE关闭移动数据开关后网络仍转发下行数据并产生计费的问题。生效需**同时满足三条件**：
1. UE携带3GPP PS Data Off UE Status为activated
2. SMF/PGW-C/GGSN-C配置PSDATAOFFSWITCH=ENABLE
3. 当前业务为**非豁免业务**

核心机制：网络侧通过下发Gate Status=closed的Create QER绑定到PDR上，阻止UPF向UE转发下行数据。

---

### K237: PS Data Off豁免业务与各制式差异 `[方案设计]`
> 来源: K126

**豁免业务**：IMS默认豁免（SET APNIMSATTR/SET GLOBALIMS配置），其他通过ADD EXEMPTSERVICE配置。

**各制式差异**：

| 维度 | 2/3G | 4G | 5G |
|------|------|----|-----|
| UE携带方式 | PCO | PCO | **ePCO** |
| 能力协商 | 需协商 | 需协商 | **不需协商（5G必须支持）** |
| Non-3GPP互操作 | 不涉及 | 切到Non-3GPP时清除status并删QER | 不涉及 |

---

### K238: PS Data Off ULCL场景处理 `[方案设计]`
> 来源: K127

- **I-UPF**：仅通知锚点UPF，不通知I-UPF
- **ULCL**：需同时通知主锚点+辅锚点UPF停止下行转发
- 新辅锚点插入时若data off已activated → 在PFCP Session Establishment Request中直接包含Gate Status=closed的Create QER

---

### K239: 计费暂停功能 `[原理]`
> 来源: K128

计费暂停用于移出网络覆盖区的用户，提高计费准确性。**仅4G支持，5G不支持**。

三个触发场景：
1. **S1 Release（ARRL）**：Release Access Bearers Request中ARRL=1，无线链路异常释放
2. **DDN寻呼失败**：DDN Acknowledge携带失败原因值（排除"Context not found"和"Unable to page UE due to Suspension"）
3. **下行丢包阈值**：SGW-U检测下行丢包达设定阈值后上报

---

### K240: 计费暂停能力协商与配置 `[方案设计]`
> 来源: K129

**协商流程**：SGW-C检查SET SGWCHGPAUSE → Create Session Request中PDN Pause Support Indication=1 → PGW-C检查ADD APNPGWCHGPAUSE(APN级优先)或SET GLBPGWCHGPAUSE(全局) → Response中PDN Pause Enable Indication=1

**PFCP机制**：触发计费暂停时PGW-C向PGW-U下发优先级最高的Create PDR（**不携带URR ID**，表示不计费），停止时下发Remove PDR。

**隐含规则**：计费暂停**只在空闲态生效**，Handover只在连接态，因此不可能同时存在。

---

### K241: 计费暂停互操作场景 `[方案设计]`
> 来源: K130

| 场景 | 处理 |
|------|------|
| PGW-C→GGSN-C | GGSN不支持，需停止计费暂停(Remove PDR) |
| GGSN-C→PGW-C | 重新协商；满足条件时下发丢包检测URR |
| PGW-C→SMF | 5G不支持，需停止计费暂停 |
| SMF→PGW-C | 重新协商；满足条件时下发丢包检测URR |

---

## 第十七章：故障案例与运维

### K242: 故障1 — N40未发送Initial消息 `[故障案例]`
> 来源: K115

- **现象**：SMF未通过N40接口发送Charging Data Request [Initial]消息
- **根因**：(1) 计费模式未配为N40 (2) 融合计费未使能 (3) CHFINIT未设为SENDREQ (4) 无可用CHF (5) N40链路故障
- **排查**：LST CHGMODE → LST CHARGECTRL → LST CCT → LST GLBDFTCHFGROUP → ALM-100072
- **隐含知识**：三层配置必须全部正确：CHGMODE=NchfMode + CHARGECTRL使能 + CHFINIT=SENDREQ

---

### K243: 故障2 — 预申请配额未携带预期RG `[故障案例]`
> 来源: K116

- **现象**：Initial消息中RG缺失或不符合预期
- **根因**：(1) CCRINITRGNUM设置不合理 (2) RGSOURCE设置不合理 (3) RG配置或绑定错误
- **排查**：LST CCT(CCRINITRGNUM/RGSOURCE) → LST URRGROUP → LST URR → LST CTXSTARTRATING
- **隐含知识**：RG来源两种模式：CTXSTARTRATING（显式配置RG）和DEFAULT（按优先级自动获取）。RG绑定链路：URR → URRGROUP → CTXSTARTRATING。

---

### K244: 故障3 — RG计费方式不符合预期 `[故障案例]`
> 来源: K117

- **现象**：N40接口RG的在线/离线计费方式与规划不一致
- **根因**：(1) 用户计费方式(RGAPPLIED)设置错误 (2) URR的USAGERPTMODE与用户计费方式不一致
- **排查**：LST CHARGECTRL → LST USRPROFCHARGE → LST URR(USAGERPTMODE)
- **隐含知识**：
  - RGAPPLIED三个取值：ONLINERGONLY、OFFLINERGONLY、DEFAULT（同一N40会话可同时支持在线和离线RG）
  - **URR的USAGERPTMODE必须与用户级别的RGAPPLIED一致，否则不生效**
  - 计费方式可基于User Profile或DNN或CC三种粒度配置

---

### K245: 故障4 — Trigger未上报 `[故障案例]`
> 来源: K118

- **现象**：SMF未向CHF发送Charging Data Request [update]上报Trigger
- **根因**：(1) CHF未下发对应Trigger (2) SMF本地未配置 (3) Session级与RG级冲突
- **排查**：用户跟踪查看CHF Response的triggers → LST PDUTRIGGER → LST RGTRIGGER
- **隐含知识**：
  - Trigger分两级：Session级(PDUTRIGGER)和RG级(RGTRIGGER)
  - **优先级规则**：Session级和RG级同一Trigger冲突时，Session级优先。Session级"不上报"时才按RG级生效
  - Trigger来源：CHF下发（Response的triggers信元）+ SMF本地配置

---

### K246: 故障5 — 主备CHF未生效 `[故障案例]`
> 来源: K119

- **现象**：主CHF故障时SMF未切换到备用CHF
- **根因**：(1) 未配置备用CHF (2) CHF下发FAILOVER_NOT_SUPPORTED (3) SMF本地FAILOVERSUP未使能 (4) 备用CHF链路故障
- **排查**：LST SELECTCHFGBYCC → LST TNFBINDGRP → LST TNFGRP → LST FAILHANDLING
- **隐含知识**：
  - **Failover三要素**：备用CHF已配置 + CHF未指示FAILOVER_NOT_SUPPORTED + SMF本地FAILOVERSUP=ENABLE
  - CHF侧sessionFailover信元具有决定权
  - CHF选择基于CC绑定：SELECTCHFGBYCC → TNFBINDGRP → TNFGRP → TNFINSIP

---

### K247: 故障6 — 业务被放通未上报CHF `[故障案例]`
> 来源: K120

- **现象**：用户数据业务被放通但计费信息被缓存或丢弃
- **根因**：(1) CHF无响应 (2) CHF链路故障 (3) CHF返回异常结果码
- **排查**：用户跟踪消息 → ALM-100072告警
- **隐含知识**："放通"是容错机制，保证业务连续性但牺牲计费准确性。计费消息可能被缓存（等CHF恢复后回放）或丢弃。

---

### K248: 故障7 — 缓存消息未正常回放 `[故障案例]`
> 来源: K121

- **现象**：CHF恢复后SMF缓存消息未回放
- **根因**：(1) 无缓存文件 (2) N40链路不正常 (3) 缓存文件超期 (4) 未达到回放间隔
- **排查**：DSP CDRSTRGINFO → ALM-100072 → ALM-81059(超期告警) → LST N40MSGSTG(回放间隔)
- **隐含知识**：**回放四条件**全部满足才回放：有缓存文件 + 链路正常 + 文件未超期(CDRSTORAGECTRL) + 达到回放间隔(N40MSGSTG)。

---

### K249: 故障8 — CP和UP URR配置不一致 `[故障案例]`
> 来源: K122

- **现象**：ALM-81026(接口信元不一致) + ALM-81054(CP/UP关键配置不一致)
- **根因**：SMF和UPF的URR配置不一致
- **隐含知识**：SMF产生ALM-81026，UPF产生ALM-81054，是配对告警。URR变更必须同步CP和UP。

---

### K250: 故障9 — 计费流量与实际访问流量不一致 `[故障案例]`
> 来源: K123

- **现象**：N40上报的计费流量与用户实际访问流量不一致
- **根因**：(1) 存在免费业务(METERINGTYPE=FREE) (2) PCF动态Rule未指定RG (3) 预定义Rule不绑定RG (4) 欠费场景信令流量丢弃
- **排查**：LST URR(METERINGTYPE) → LST USERPROFILE(FREESER) → LST RULE → LST PCCPOLICYGRP → LST SPECTRAFURRGRP
- **隐含知识**：
  - 免费业务和欠费丢弃是"正常现象"，Rule未绑定RG是"配置错误"
  - Rule→PCCPOLICYGRP→URRGROUP→URR绑定链路任何一环断裂都导致流量不一致
  - 欠费场景信令流量由SPECTRAFURRGRP控制

---

### K251: 故障10 — 用户异常去活诊断体系 `[故障案例]`
> 来源: K124

- **现象**：用户异常去活，Termination消息携带ABNORMAL_RELEASE
- **根因**：周边网元故障，通过diagnostics原因值定位
- **排查**：用户跟踪查看diagnostics字段 → LST N40DIAGTRIGGER

**关键运维知识 — 去活原因值映射表**：

| 原因值 | 指向网元 | 场景 |
|--------|---------|------|
| 12 | GTPC链路 | GTPC链路中断 |
| 21 | UPF | UPF收到Error indication |
| 22 | 对端网元 | 对端重启(recovery IE不匹配) |
| 258 | **CHF** | CHF返回信元不合法 |
| 262 | **CHF** | CHF响应超时 |
| 263 | **CHF** | 主备CHF重发均超时 |
| 302 | **PCF** | PCF无响应 |
| 351 | **UPF** | UPF请求去活 |
| 352 | **UPF** | UPF无响应 |

**原因值258子场景**：请求体类型与返回码不匹配、UPF独享配额模式下CHF未携带uPFID、CHF未携带ResultCode、SMF申请配额但CHF未授权也未指示重定向。

**关键参数**：SET CNVRGDCHGPARA的BADRSPACT=CONTINUE时允许CHF异常时业务继续而非去活。

---

### K252: 计费告警速查表 `[运维]`
> 来源: K289, K290, K291, K292, K293, K294

| 告警ID | 名称 | 级别 | 适用NF | 核心含义 | 关键处理 |
|--------|------|------|--------|----------|----------|
| 82000 | 计费中心长时间未取话单 | 紧急 | NCG | PULL模式下计费中心未取话单 | 配置分发/备份任务；磁盘剩余400MB停止接收 |
| 100417 | UPF中转RADIUS无响应 | 重要 | SMF/GW-C/GGSN | SMF通过UPF中转RADIUS链路断 | MOD RDSSVRGRP调重发参数 |
| 100530 | 融合计费用户放通不计费 | 次要 | SMF/GW-C/GGSN | CHF故障+缓存关闭导致放通 | 开启SET N40MSGSTG缓存；分析话统维度 |
| 100630 | 在线计费定时器过载流控 | 重要 | SMF/GW-C/GGSN | 在线计费定时器拥塞(VT/NPT/Tx) | 等10分钟自动恢复，否则联系支持 |
| 81020 | RADIUS计费服务器无响应 | 重要 | SMF/GW-C/GGSN | UNC直连RADIUS链路断 | SET APNRDSACCTCTRL可设CONTINUE |
| 100682 | 计费网元设备故障 | 重要 | SMSF | NCG设备故障 | 查NCG对应告警 |
| 100683 | 计费网元业务状态异常 | 重要 | SMSF | NCG业务异常 | 查NCG对应告警 |

**ALM-100530处理要点**：
- 核心关联命令：SET CNVRGDCHGPARA(CONTINUEALARM=ENABLE) + SET N40MSGSTG(STGSWITCH=ENABLE)
- 话统分析维度：无可用CHF / CHF无响应 / 结果码错误 / 信元错误 导致的放通次数
- 建议：现网应开启话单缓存功能以避免CHF故障时放通不计费

---

### K253: 信令跟踪 — 5G计费问题定位 `[运维]`
> 来源: K295

5G计费问题定位流程：
1. 建立用户跟踪，查看是否上报**EMS_CtfErrorRpt**消息
2. 打开EMS_CtfErrorRpt消息，解析关键字段：
   - **ChargingID**：计费编号
   - **AnonymizeSupi**：匿名化用户永久标识
   - **PduSessionId**：PDU会话编号
   - **RptErrorInfo**：错误原因描述
   - **Details**：定位详细信息
   - **Suggestion**：错误处理建议
3. 根据原因和建议处理，重新拨测验证

---

### K254: 信令跟踪 — 5G策略问题定位 `[运维]`
> 来源: K296

5G策略问题定位流程：
1. 建立用户跟踪，查看是否上报**EMS_SmpolicyErr**消息
2. 打开EMS_SmpolicyErr消息，解析关键字段：
   - **AnonymizedSupi**：匿名化用户永久标识
   - **PdusessionId**：PDU会话编号
   - **Rattype**：无线接入类型
   - **PcfInstanceId**：PCF实例标识
   - **EmsErrInfo**：错误原因描述
   - **Suggestion**：错误处理建议
3. 根据原因和建议处理，重新拨测验证

---

### K255: N40接口链路状态检查 `[运维]`
> 来源: K131

SMF和CHF之间N40接口链路状态检查步骤：
1. 执行`DSP SBILINKSTATUS`命令，选择对端NF类型为NFTypeCHF，检查链路状态是否为"正常"
2. 查看是否存在ALM-100072（目的NF服务不可达，对端网元类型为CHF）告警
3. 不符合预期时收集告警、日志、配置信息联系技术支持

---

## 知识统计

| 章 | 标题 | 编号范围 | 数量 |
|----|------|----------|------|
| 第十二章 | 融合计费配置全景 | K201-K213 | 13 |
| 第十三章 | 计费三件套配置 | K214-K223 | 10 |
| 第十四章 | PCF策略配置 | K224-K228 | 5 |
| 第十五章 | 方案设计知识 | K229-K234 | 6 |
| 第十六章 | 特殊场景 | K235-K241 | 7 |
| 第十七章 | 故障案例与运维 | K242-K255 | 14 |
| **合计** | | K201-K255 | **55** |

### 融合去重记录

| 新编号 | 合并来源 | 融合说明 |
|--------|----------|----------|
| K205 | K135 + K272 + K273 + K274 + K275 + K276 + K277 | 计费接口模式：K135基础定义 + K272优先级 + K273终端类型 + K274互操作指示 + K275 V/I-SMF + K276 PCF实例 + K277策略模式 |
| K206 | K136 + K259 + K260 + K261 | CC属性：K136标准取值 + K259四级优先级 + K260本地/签约选择 + K261制式来源 |
| K213 | K145 + K155 + K156 | CHF选择：K145选择优先级 + K155 IMSI三层配置 + K156实时生效限制 |
| K235 | K167 + K168 + K262 | ULCL计费：K167独立配额 + K168系统约束 + K262架构原理 |
| K252 | K289 + K290 + K291 + K292 + K293 + K294 | 7个告警条目合入速查表，K291(ALM-100530)补充处理要点 |

### 按类型统计

| 类型 | 数量 | 编号 |
|------|------|------|
| [配置] | 22 | K203, K204, K205, K207, K208, K209, K210, K211, K212, K213, K214, K215, K216, K219, K222, K223, K227, K228 |
| [原理] | 8 | K220, K224, K226, K229, K236, K239 |
| [方案设计] | 12 | K202, K218, K221, K230, K231, K232, K233, K234, K235, K237, K238, K240, K241 |
| [隐性规则] | 4 | K201, K217, K225 |
| [故障案例] | 10 | K242-K251 |
| [运维] | 3 | K252, K253, K254, K255 |
