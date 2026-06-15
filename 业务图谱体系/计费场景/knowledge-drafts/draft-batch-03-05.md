# Batch 03-05: 方案一(未部署NCG)配置 + 融合计费调测 知识草稿

## 来源文件清单

| # | 文件 | UNC路径 |
|---|------|---------|
| 1 | 方案配置_90839325 | 计费方案部署与调测/方案一：未部署NCG的计费解决方案/ |
| 2 | 配置计费License_90679481 | 同上/SMF配置/ |
| 3 | 配置计费接口模式_55040136 | 同上 |
| 4 | 配置计费方式_90839329 | 同上 |
| 5 | 配置计费属性_90679485 | 同上 |
| 6 | 配置融合计费费率标识_90679537 | 同上 |
| 7 | 配置NCG_CHF(OCS)选择方式_90679549 | 同上/融合计费对接配置/ |
| 8 | 配置N40接口API版本_90839337 | 同上/融合计费模板及交互配置/ |
| 9 | 配置SMF与CHF交互条件_90679489 | 同上 |
| 10 | 配置异常返回码动作_55040172 | 同上 |
| 11 | 配置融合计费模板_55040140 | 同上 |
| 12 | 配置计费消息缓存_90839397 | 同上 |
| 13 | 配置费率切换_90839385 | 同上 |
| 14 | 部署PCF_93408042 | 同上 |
| 15 | 部署UPF_92191005 | 同上 |
| 16 | 调测内容计费_08957400 | 计费方案部署与调测/调测融合计费/ |
| 17 | 调测带配额管理的融合计费_80333080 | 同上 |
| 18 | 调测基于IMSI选择CHF_44969871 | 同上 |

UNC根路径前缀: `网络部署/业务专题/5G Core 计费解决方案/计费解决方案概述/`

---

## 一、方案一配置依赖链

### K132: 方案一组网与配置全景
> 来源: 方案配置_90839325

**方案设计知识**

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

### K133: 计费License项
> 来源: 配置计费License_90679481

**配置知识**

| 特性 | License控制项 |
|------|-------------|
| 融合计费 | WSFD-011206 |
| 内容计费 | LKV3W9BCC12 |
| 时长计费 | LKV3W9TBCS12 |
| 流量计费 | LKV3WPVBCS11 |
| 事件计费 | LKV3W9EBCS12 |

命令：SET LICENSESWITCH，必须最先配置。

---

## 二、计费方式与接口配置

### K134: 融合计费开关配置
> 来源: 配置计费方式_90839329

**配置知识**

优先级：PCF下发 > User Profile(SET USRPROFCHARGE) > DNN(SET APNCHARGECTRL) > 计费属性(ADD CHARGEMETHOD) > 全局(SET CHARGECTRL)

**SET CHARGECTRL关键参数**：
- HOMECONVERGED/VISITCONVERGED/ROAMCONVERGED=ENABLE（对应的ONLINE/OFFLINE必须DISABLE）
- RGAPPLIED：业务申请上报模式（ONLINERGONLY/OFFLINERGONLY/DEFAULT）

**RGAPPLIED约束（隐性规则）**：
- RGAPPLIED=DEFAULT时：URRGROUP中**不能**同时配RG相同的离线和在线URR
- RGAPPLIED=ONLINERGONLY或OFFLINERGONLY时：建议同时配离线和在线URR

### K135: 计费接口模式配置
> 来源: 配置计费接口模式_55040136

**配置知识**

**SET CHGMODE关键参数**：
- TMACCTYPE：终端接入类型（UE5G_RAT5G/UE5G_RAT4G/UENON5G_RAT4G/RAT2G/3G/NBIOT等）
- FORCED：指定计费接口（NchfMode）
- BY5GSIWKI：是否按5GS互操作指示选择

可选粒度：ADD APNCHGMODE(DNN) / ADD ROAMCHGMODE(漫游) / ADD PCCCHGMODEBYPCFID(PCF实例)

优先级：ROAMCHGMODE > APNCHGMODE > SET CHGMODE > PCCCHGMODEBYPCFID

### K136: 计费属性(CC)配置
> 来源: 配置计费属性_90679485

**配置知识**

CC标准取值：
- 0x0100：热计费(Hot Billing)
- 0x0200：统一费率(Flat Rate)
- 0x0400：预付费(Prepaid)
- 0x0800：普通计费(Normal Billing)

CC来源优先级：RADIUS Server下发 > User Profile > DNN > 全局 > normal(默认)

命令：SET GLBCHARGECHAR(全局) / ADD CHARGECHAR(CC实例) / SET USRPROFCHARGE(绑定UP) / SET APNCHARGECTRL(绑定DNN)

---

## 三、融合计费模板与交互配置

### K137: 融合计费模板(CCT)配置
> 来源: 配置融合计费模板_55040140

**配置知识**

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

### K138: Trigger配置
> 来源: 配置SMF与NCG_CHF(OCS)交互条件_90679489

**配置知识**

**SET CHFINIT**：PDU会话建立时是否与CHF交互
- CHFINIT=SENDREQ：激活时发送Initial
- CCRINITRGNUM：初始RG个数
- RGSOURCE：RG来源（DEFAULT/CTXSTARTRATING）

**Trigger三级取值**：IMMEDIATE(立即上报) / DEFERRED(延迟上报) / NONREPORT(不上报)

**Session级Trigger (ADD PDUTRIGGER)**：QOSCHG, ULCHG, SRVNDCHG, PLMNCHG, RATCHG, TAICHG, TIMELIMIT, VOLUMELIMIT, EVENTLIMIT, SESSAMBRCHG, ADDUPF

**RG级Trigger (ADD RGTRIGGER)**：额外包含QUOTATHRESHOLD(配额阈值), VT(配额有效时长), QHT(配额保持时长)

**隐性规则**：建议每用户上报间隔>30秒，避免SMF和CHF频繁交互。

### K139: N40 API版本配置
> 来源: 配置N40接口的API版本和增强功能集_90839337

**配置知识**

SET N40APIVER：
- APIVER：版本号（如F30），需与CHF一致
- FEATURE：增强功能集，支持&叠加（NODEFUNC-1, NBIOTCHG-1, LTEMCHG-1, UTRANCHG3GPP-1等）

### K140: 异常返回码处理配置
> 来源: 配置异常返回码动作_55040172

**配置知识**

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

## 四、费率标识(内容计费三件套)配置

### K141: 融合计费三件套配置命令
> 来源: 配置融合计费费率标识_90679537

**配置知识**

**ADD URR**(SMF侧)：
- URRNAME, URRID（**SMF和UPF必须一致**）
- USAGERPTMODE：ONLINE/OFFLINE
- ONLCOMPOUNDTYPE/OFFCOMPOUNDTYPE：ONLYRG
- ONLINERG/RG：费率组编号
- ONLMETERINGTYPE/OFFMETERINGTYPE：VOLUME/DURATION/FREE

**ADD URRGROUP**：
- URRGROUPNAME
- UPURRNAME1/DOWNURRNAME1：第1组上下行URR
- UPURRNAME2/DOWNURRNAME2：第2组上下行URR（1/2仅为编号，无优先级语义）

**ADD PCCPOLICYGRP**：
- PCCPOLICYGRPNM, URRGROUPNAME

**ADD RULE**：RULENAME, POLICYTYPE=PCC, PRIORITY, POLICYNAME

**ADD QUOTAEXHAUSTACT**：在线RG配额耗尽后动作（BLOCK/REDIRECT/FORWARD）

### K142: UPF侧配置流程
> 来源: 部署UPF_92191005

**配置知识**

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

### K143: SET SPECTRAFURRGRP — 特殊流量计费兜底
> 来源: 部署UPF_92191005

**配置知识**

SET SPECTRAFURRGRP配置全局缺省URR组，用于：
1. 七层未匹配已转发流量（特殊流量）
2. 无URR配置的业务

当BIT1232软参值=1时特殊流量通过该规则组计费。

---

## 五、跨网元一致性约束

### K144: 跨网元名称一致性要求汇总
> 来源: 部署UPF_92191005, 部署PCF_93408042, 配置融合计费费率标识_90679537

**隐性规则**

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

## 六、CHF选择配置

### K145: CHF选择配置命令链
> 来源: 配置NCG_CHF(OCS)选择方式_90679549

**配置知识**

CHF选择优先级（高到低）：
1. ADD SELCHFGBYIMSI（基于IMSI，测试用）
2. ADD SELCHFGBIMSISEG（基于IMSI号段）
3. 基于PCF下发FQDN
4. 基于UDM签约CC
5. 基于标准化NRF服务发现
6. ADD SELECTCHFGBYCC（基于SMF本地CC）

配置命令链：ADD TNFINS(CHF实例) → ADD TNFINSIP(IP) → ADD TNFGRP(CHF组) → ADD TNFBINDGRP(绑定) → SET CHFSELECTMODE → SET GLBDFTCHFGROUP → ADD SELECTCHFGBYCC

**隐性规则**：建议配置缺省CHF组避免选不到CHF。FQDN需与PCF下发一致。

### K146: PCF侧配置
> 来源: 部署PCF_93408042

**配置知识**

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

## 七、费率切换与消息缓存

### K147: 费率切换配置
> 来源: 配置费率切换_90839385

**配置知识**

粒度优先级：User Profile > APN > CC > 整机

命令：ADD FESTIVAL(节假日) → ADD WEEKDAY(星期表) → ADD TARIFFGROUP(时间段) → SET N40QUOTACTRL(TCMODE: DEFAULT/DAILY/MONTHLY) → 绑定(SET APNCHARGECTRL或SET USRPROFCHARGE)

约束：CCVALUE不能为0x0200(统一费率)，每DNN/UP只能绑一个费率切换组。

### K148: 计费消息缓存配置
> 来源: 配置计费消息缓存（融合计费）_90839397

**配置知识**

场景：主备CHF均故障时SMF缓存计费消息。

前提：SET FAILHANDLING的FHACTION=CONTINUE。此功能为定制能力，要求对端为华为NCG。

命令：SET N40MSGSTG(缓存开关+回放间隔/速率) → SET STGTRIGGER(缓存期间trigger) → SET CNVRGDCHGPARA(CHGDATAREFGEN=SMF) → SET CDRSTORAGECTRL(超期天数) → SET N4CHGMSGCTRL(缓存池扩展)

---

## 八、融合计费调测

### K149: 内容计费验证链
> 来源: 调测内容计费_08957400

**方案设计知识**

内容计费逐级验证链：
1. LST RULEBINDING → UserProfile绑定的RULE
2. LST RULE → RULE绑定的FlowFilter和PCCPOLICYGRP
3. LST PCCPOLICYGRP → PCC策略组绑定的URRGROUP
4. LST URRGROUP → URR组中的上下行URR
5. LST URR → 最终URR的ID和计费模式

七层内容计费还需验证：LST PROTBINDFLOWF → LST FLOWFILTER → LST L7FILTER

### K150: 内容计费双License要求
> 来源: 调测内容计费_08957400

**配置知识**

内容计费需**两个**License同时开启：
- UNC侧：LKV3W9BCC12
- UDG侧：LKV3G5BCBC01

两处必须均为ENABLE才能正常使用。

### K151: URR ID在PFCP信令中的编码规则
> 来源: 调测内容计费_08957400

**原理知识**

Usage Report中URR ID编码：高位80代表URR是预定义类型（UPF本地配置），低位代表UPF本地URR ID。
示例：0x80000001(2147483649) → 预定义标志 + URR ID=01

调测时需做进制转换对照。

### K152: 带配额管理的融合计费E2E调测流程
> 来源: 调测带配额管理的融合计费_80333080

**方案设计知识**

端到端调测关键步骤：
1. 双License检查
2. 用户激活 → 验证Initial消息
3. 验证Initial携带的RG
4. 用户访问新业务 → UPF上报新URR ID → SMF下发Create URR
5. Trigger条件满足 → 验证Update消息
6. 用户去激活 → 验证Termination消息中流量一致性

### K153: URRFAILACTION — 新业务无URR时的容灾
> 来源: 调测带配额管理的融合计费_80333080

**配置知识**

UNC未配置新业务URR时，新业务被阻塞。通过`SET URRFAILACTION: RETRYFAILACT=CONTINUE`可放通。
这是一个重要容灾配置，允许计费规则未完全配置时仍保障业务可用性。

### K154: 计费三件套修改命令链
> 来源: 调测带配额管理的融合计费_80333080

**配置知识**

新业务配额下发失败时，需执行完整修改链：
```
MOD URR → MOD URRGROUP → MOD PCCPOLICYGRP → MOD RULE
```
体现URR→URRGROUP→PCCPOLICYGRP层级修改顺序，最终通过RULE下发给用户。

### K155: 基于IMSI选择CHF的配置
> 来源: 调测基于IMSI选择CHF功能_44969871

**配置知识**

三层配置：
1. ADD TNFINS(CHF实例) + ADD TNFINSIP(IP) — SRVNAME固定取**NchfConvCharg**
2. ADD TNFGRP(CHF组) + ADD TNFBINDGRP(实例绑定组)
3. ADD SELCHFGBYIMSI(IMSI绑定主备CHF组)

### K156: IMSI-CHF绑定的实时生效限制
> 来源: 调测基于IMSI选择CHF功能_44969871

**隐性规则**

MOD SELCHFGBYIMSI修改后，已激活用户**不会立即**切换CHF。必须去激活后重新激活才能生效。不支持在线切换CHF。

---

## 知识统计

| 类别 | 数量 |
|------|------|
| 方案设计知识 | 5 (K132, K149, K152) |
| 配置知识 | 16 (K133-K142, K145-K148, K150, K153-K155) |
| 原理知识 | 2 (K151) |
| 隐性规则 | 5 (K134, K142, K144, K146, K156) |
| **合计** | **25条 (K132-K156)** |
