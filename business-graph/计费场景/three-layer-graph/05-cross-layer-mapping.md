# 计费场景三层图谱 · 第5层：跨层映射关系总表

> **文件定位**：`three-layer-graph/05-cross-layer-mapping.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §12 跨层映射
> **作用**：汇总CS↔Feature/Task、Feature↔Task、Task↔Command/Object/DP的所有跨层边
> **合规要求**：严格避免 §13 禁止关系（CS→ConfigObject直接绑定、Feature→MMLCommand直接绑定等）

---

## 0. 跨层映射总览

| 跨层边类型 | 数量 | 方向 | 说明 |
|-----------|------|------|------|
| CS `uses_feature` | 20 | 业务层→特性层 | 7方案 × 平均3特性 |
| CS `uses_task`（方案闭包级） | 7 | 业务层→任务层 | 每方案一个主Task集 |
| Feature `decomposes_to` ConfigTask | 14 | 特性层→任务层 | 每核心Feature的Task展开 |
| ConfigTask `invokes` MMLCommand | ~50 | 任务层→命令层 | Task调用的MML命令 |
| ConfigTask `targets` SemanticObject/ConfigObject | ~30 | 任务层→业务/命令层 | Task操作的对象 |
| DP `selects` CS | 3 | 业务层内 | 决策点选择方案 |
| DP `sets_value_pattern` | 3 | 业务层→命令层 | 决策点设置参数模式 |

---

## 1. CS → Feature 映射（uses_feature，20条）

> 来源：`01-business-graph.md` §2.2~§2.7 + §8.2

| CS | uses_feature | Feature角色 |
|----|-------------|------------|
| CS-CH-01 离线计费 | GWFD-010171（离线UDG） | 核心：UDG侧离线收集 |
| CS-CH-01 | GWFD-020301（内容计费UDG） | 支撑：URR三件套基础 |
| CS-CH-01 | WSFD-011201（离线UNC） | 核心：UNC侧话单生成+Ga接口 |
| CS-CH-02 在线计费 | GWFD-020300（在线UDG） | 核心：UDG侧Gy/OCS交互 |
| CS-CH-02 | GWFD-020301（内容计费UDG） | 支撑：在线计费基于业务粒度 |
| CS-CH-02 | GWFD-020306（事件计费UDG） | 可选：事件粒度在线计费 |
| CS-CH-03 融合计费 | GWFD-010173（融合UDG） | 核心：UDG侧N40执行 |
| CS-CH-03 | WSFD-011206（融合UNC） | 核心：UNC侧Nchf交互+CCT模板 |
| CS-CH-03 | GWFD-020301（内容计费UDG） | 支撑：依赖内容计费License |
| CS-CH-04 内容计费基础 | GWFD-110101（SA-Basic） | 基础：业务识别前置 |
| CS-CH-04 | GWFD-020301（内容计费UDG） | 核心：UDG侧三件套+FILTER |
| CS-CH-04 | GWFD-020351（PCC基本UDG） | 基础：PCC框架 |
| CS-CH-04 | WSFD-109101（PCC基本UNC） | 基础：UNC侧PCC |
| CS-CH-05 计量形态增强 | GWFD-020302（时长计费UDG） | 核心：DURATION计量 |
| CS-CH-05 | GWFD-020303（流量计费UDG） | 核心：VOLUME计量 |
| CS-CH-05 | GWFD-020306（事件计费UDG） | 核心：EVENT计量 |
| CS-CH-06 配额降速 | GWFD-020300（在线UDG） | 核心：UDG侧配额耗尽执行 |
| CS-CH-06 | GWFD-010173（融合UDG） | 核心：UDG侧N40降速 |
| CS-CH-06 | WSFD-011206（融合UNC） | 核心：UNC侧CHF Notify降速 |
| CS-CH-07 兜底默认 | GWFD-020301（内容计费UDG） | 核心：UDG侧DFTURRGRPNAME兜底 |
| CS-CH-07 | GWFD-020351（PCC基本UDG） | 支撑：USERPROFILE承载兜底 |

---

## 2. CS → ConfigTask 映射（uses_task，方案闭包级，7条）

> 每方案一个主Task集，按方案闭包粒度聚合。

| CS | uses_task（主Task集） | 说明 |
|----|---------------------|------|
| CS-CH-01 离线计费 | T-101, T-006, T-007, T-001, T-002, T-003, T-004, T-104, T-311, T-008 | UDG三件套+CG接口+UNC话单 |
| CS-CH-02 在线计费 | T-101, T-006, T-007, T-001, T-002, T-003, T-004, T-201, T-202, T-203, T-204, T-008 | UDG三件套+DCC链路+Default Quota+配额耗尽 |
| CS-CH-03 融合计费 | T-101, T-301, T-302, T-303, T-304, T-305, T-306, T-307, T-308, T-006, T-007, T-003, T-004, T-005, T-104, T-008 | UNC三联前置+CCT模板+CHF选择+UDG三件套 |
| CS-CH-04 内容计费基础 | T-101, T-102, T-001, T-002, T-103, T-006, T-007, T-003, T-004, T-104, T-008 | SA特征库+三件套+FILTER+绑定 |
| CS-CH-05 计量形态增强 | T-101, T-006(METERINGTYPE配置), T-007, T-003, T-004, T-008 | 计量方式参数化（VOLUME/DURATION/EVENT） |
| CS-CH-06 配额降速 | T-101, T-006, T-007, T-204, T-303, T-003(高优先级降速规则), T-104, T-008 | 配额耗尽触发+降速规则覆盖+DFTURRGRPNAME兜底 |
| CS-CH-07 兜底默认 | T-101, T-104, T-006, T-007, T-004, T-008 | DFTURRGRPNAME+DFTSIGURRGNAME+SPECTRAFURRGRP兜底链 |

---

## 3. Feature → ConfigTask 映射（decomposes_to，14条）

| Feature | decomposes_to | Task集 | 说明 |
|---------|---------------|--------|------|
| GWFD-110101 SA-Basic | T-101, T-102, T-001, T-002, T-103, T-008 | SA基础链：License+特征库+识别条件+协议绑定 |
| GWFD-020351 PCC基本(UDG) | T-101, T-002, T-003, T-004, T-008 | PCC框架：规则+绑定 |
| WSFD-109101 PCC基本(UNC) | T-101, T-003, T-004, T-005 | UNC侧PCC：规则+模板组+APN绑定 |
| GWFD-010171 离线计费(UDG) | T-101, T-006(OFFLINE), T-007, T-001, T-002, T-003, T-004, T-104, T-008 | UDG离线：三件套+过滤器+兜底 |
| WSFD-011201 离线计费(UNC) | T-101, T-301, T-309, T-006, T-007, T-003, T-004, T-005, T-311 | UNC离线：CHGMODE+CC属性+CG接口 |
| GWFD-020300 在线计费(UDG) | T-101, T-006(ONLINE), T-007, T-001, T-002, T-003, T-004, T-201, T-202, T-203, T-204, T-008 | UDG在线：三件套+DCC+Default Quota+耗尽动作 |
| GWFD-010173 融合计费(UDG) | T-101, T-006(双URR:OFFLINE+ONLINE), T-007, T-001, T-002, T-003, T-004, T-104, T-008 | UDG融合：每业务2个URR+三件套 |
| WSFD-011206 融合计费(UNC) | T-101, T-301, T-302, T-303, T-304, T-305, T-306, T-307, T-308, T-309, T-310, T-006, T-007, T-003, T-004, T-005, T-204 | UNC融合：三联前置+CCT+CHF选择+Trigger+异常+缓存（18步链） |
| GWFD-020301 内容计费(UDG) | T-101, T-102, T-001, T-002, T-103, T-006, T-007, T-003, T-004, T-104, T-008 | UDG内容计费：SA+三件套+FILTER+兜底 |
| WSFD-109002 内容计费(UNC) | T-101, T-006, T-007, T-003, T-004, T-005, T-204 | UNC内容计费：三件套+绑定链+配额耗尽 |
| GWFD-020302 时长计费(UDG) | T-101, T-006(METERINGTYPE=DURATION), T-007, T-003, T-004, T-008 | 时长计量：URR参数化DURATION |
| GWFD-020303 流量计费(UDG) | T-101, T-006(METERINGTYPE=VOLUME), T-007, T-003, T-004, T-104, T-008 | 流量计量：URR参数化VOLUME+SPECTRAFURRGRP |
| GWFD-020306 事件计费(UDG) | T-101, T-006(METERINGTYPE=EVENT), T-007, T-003, T-004, T-008 | 事件计量：URR参数化EVENT（三计费点） |
| WSFD-011202 热计费(UNC) | T-101, T-309(CC=0x0100) | 热计费：CC标志位配置 |

---

## 4. ConfigTask → MMLCommand 映射（invokes，~50条核心映射）

| ConfigTask | invokes | MMLCommand | 说明 |
|-----------|---------|-----------|------|
| T-001 | invokes | ADD CATEGORYPROP, ADD FILTER, ADD FILTERIPV6, ADD L7FILTER | 业务分类与过滤条件 |
| T-002 | invokes | ADD FLOWFILTER, ADD FLTBINDFLOWF | 流过滤器组装 |
| T-003 | invokes | ADD RULE | PCC规则（POLICYTYPE=CHARGING） |
| T-004 | invokes | ADD USERPROFILE, ADD RULEBINDING | 用户模板+规则绑定 |
| T-005 | invokes | ADD USRPROFGROUP, ADD UPBINDUPG, ADD APNUSRPROFG | UNC绑定链 |
| T-006 | invokes | ADD URR, ADD URRGROUP | 计费三件套核心 |
| T-007 | invokes | ADD PCCPOLICYGRP | PCC策略组 |
| T-008 | invokes | SET REFRESHSRV | 刷新生效（must_be_last） |
| T-101 | invokes | SET LICENSESWITCH | License前置门控 |
| T-102 | invokes | LOD SIGNATUREDB, LOD PARSERDB | SA特征库加载 |
| T-103 | invokes | ADD PROTBINDFLOWF | 协议绑定（60秒延迟） |
| T-104 | invokes | SET URRGRPBINDING, SET SPECTRAFURRGRP, ADD SPECURRGRPLIST | 兜底URR组 |
| T-201 | invokes | ADD DIAMCONNGRP, ADD DCCTEMPLATE, SET OCSDOWNACTION | DCC链路+OCS对接 |
| T-202 | invokes | ADD CMDRCACT, ADD MSCCRCACT, SET FHBYPASS, SET TXTIMER | 在线异常处理 |
| T-203 | invokes | SET UPDEFAULTQUOTA | Default Quota容灾 |
| T-204 | invokes | ADD QUOTAEXHAUSTACT | 配额耗尽动作 |
| T-301 | invokes | SET CHGMODE, ADD APNCHGMODE, ADD ROAMCHGMODE | 计费接口模式 |
| T-302 | invokes | SET CHARGECTRL, SET USRPROFCHARGE, SET APNCHARGECTRL | 融合计费使能 |
| T-303 | invokes | SET CHFINIT, ADD TNFINS, ADD TNFINSIP, ADD TNFGRP, ADD TNFBINDGRP, ADD SELECTCHFGBYCC, SET GLBDFTCHFGROUP | CHF交互使能+选择链 |
| T-304 | invokes | ADD CCT, ADD SELECTCCTBYCC | CCT模板 |
| T-305 | invokes | ADD PDUTRIGGER, ADD RGTRIGGER | Trigger交互条件 |
| T-306 | invokes | SET N40APIVER | N40 API版本 |
| T-307 | invokes | SET FAILHANDLING, ADD PDUSCACT, ADD RGRCACT, SET CNVRGDCHGPARA | 异常返回码处理 |
| T-308 | invokes | SET N40MSGSTG, SET STGTRIGGER, SET CDRSTORAGECTRL, SET N4CHGMSGCONTROL | 计费消息缓存 |
| T-309 | invokes | ADD CHARGECHAR, SET GLBCHARGECHAR | CC计费属性 |
| T-310 | invokes | ADD FESTIVAL, ADD WEEKDAY, ADD TARIFFGROUP | 费率切换 |
| T-311 | invokes | ADD CG, SET CDRTRANSFER, SET OFCTHRESHOLD, SET CONTAINERTRIGGER | CG接口配置 |

---

## 5. ConfigTask → SemanticObject/ConfigObject 映射（targets）

| ConfigTask | targets SemanticObject | targets ConfigObject |
|-----------|------------------------|---------------------|
| T-001 | SO-CH-01(报文解析), SO-CH-02(协议识别), SO-CH-03(过滤条件) | CATEGORYPROP, FILTER, L7FILTER |
| T-002 | SO-CH-03(过滤条件) | FLOWFILTER, FLTBINDFLOWF |
| T-003 | SO-CH-04(规则语义), SO-CH-06(优先级) | RULE |
| T-004 | SO-CH-07(绑定语义) | USERPROFILE, RULEBINDING |
| T-005 | SO-CH-07(绑定语义) | USRPROFGROUP, UPBINDUPG, APNUSRPROFG |
| T-006 | SO-CH-08(计费语义), SO-CH-09(配额语义) | URR, URRGROUP |
| T-007 | SO-CH-05(策略语义) | PCCPOLICYGRP |
| T-101 | — | — (License全局) |
| T-102 | SO-CH-01(报文解析) | — (SA特征库数据) |
| T-103 | SO-CH-02(协议识别) | PROTBINDFLOWF |
| T-104 | SO-CH-07(绑定), SO-CH-08(计费) | URRGRPBINDING |
| T-201 | SO-CH-10(Ga/Gy协议栈) | DIAMCONNGRP, DCCTEMPLATE, OCSGroup |
| T-202 | SO-CH-09(配额语义), SO-CH-12(诊断) | CMDRCACT, MSCCRCACT |
| T-203 | SO-CH-09(配额语义) | UPDEFAULTQUOTA |
| T-204 | SO-CH-06(优先级), SO-CH-09(配额) | QUOTAEXHAUSTACT |
| T-301 | SO-CH-11(N40/PFCP协议栈) | CHGMODE |
| T-302 | SO-CH-09(配额), SO-CH-11(N40协议栈) | CHARGECTRL, USRPROFCHARGE |
| T-303 | SO-CH-11(N40协议栈) | CHFINIT, TNFGRP, SELECTCHFGBYCC |
| T-304 | SO-CH-09(配额) | CCT |
| T-305 | SO-CH-09(配额), SO-CH-11(N40协议栈) | PDUTRIGGER, RGTRIGGER |
| T-306 | SO-CH-11(N40协议栈) | N40APIVER |
| T-307 | SO-CH-09(配额), SO-CH-12(诊断) | FAILHANDLING, PDUSCACT |
| T-308 | SO-CH-09(配额) | N40MSGSTG |
| T-309 | SO-CH-08(计费语义) | CHARGECHAR |
| T-310 | SO-CH-08(计费语义) | FESTIVAL, WEEKDAY, TARIFFGROUP |
| T-311 | SO-CH-10(Ga/Gy协议栈) | CG |

---

## 6. DecisionPoint 跨层影响（selects / sets_value_pattern）

| DP | 关系 | 目标 | 说明 |
|----|------|------|------|
| DP-CH-01 计费方式选择 | `selects` | CS-CH-01/CS-CH-02/CS-CH-03 | 离线→CS-01；在线→CS-02；融合→CS-03 |
| DP-CH-03 匹配层次选择 | `sets_value_pattern` | URR.FILTER层次 / FLOWFILTER组成 | L34→FILTER；L7→L7FILTER+PROTBINDFLOWF |
| DP-CH-04 配额耗尽动作选择 | `sets_value_pattern` | QUOTAEXHAUSTACT.FACTION | BLOCK/REDIRECT/FORWARD |
| DP-CH-06 计量方式选择 | `sets_value_pattern` | URR.OFFMETERINGTYPE / ONLMETERINGTYPE | VOLUME/DURATION/EVENT |
| DP-CH-07 兜底策略选择 | `sets_value_pattern` | URRGRPBINDING.DFTURRGRPNAME / SPECTRAFURRGRP | 默认URR组/异常费率/全局兜底 |

---

## 7. 端到端链路验证（3条完整路径）

### 7.1 路径A：内容计费（离线）端到端

```
[业务] BD-CH-01 业务感知
  → NS-CH-01 计费场景
    → CS-CH-04 内容计费基础方案
      → DP-CH-03 选择匹配层次（L34+L7混合）
      → DP-CH-05 选择计费粒度（业务级）
      → BR-CH-02 配置链逐层一致性
      → SO-CH-08 计费语义（RG差异化）

[特性] CS-CH-04 uses_feature
  → GWFD-110101 SA-Basic（业务识别基础）
  → GWFD-020301 内容计费（UDG三件套）
  → GWFD-020351 PCC基本功能（UDG PCC框架）

[任务] GWFD-020301 decomposes_to
  → T-101 License开启（LKV3G5BCBC01）
  → T-102 SA特征库加载
  → T-001 规划业务分类（FILTER/L7FILTER）
  → T-002 配置流过滤器（FLOWFILTER/FLTBINDFLOWF）
  → T-103 配置协议绑定（PROTBINDFLOWF，60秒）
  → T-006 配置URR与URR组 ★ 核心
  → T-007 配置PCC策略组
  → T-003 配置PCC规则（POLICYTYPE=CHARGING）
  → T-004 配置用户模板与规则绑定
  → T-104 配置URR组绑定与兜底（DFTURRGRPNAME）
  → T-008 策略刷新生效（must_be_last）

[命令] T-006 invokes → ADD URR
  → operates_on → ConfigObject: URR
    → 关键参数: URRID, USAGERPTMODE=OFFLINE, OFFMETERINGTYPE=VOLUME, RG
  → constrained_by → CR-01 URRID会话内唯一
  → constrained_by → CR-02 RG值跨侧一致性
  → constrained_by → CR-03 三件套绑定完整性

[证据] 全链路可追溯：
  CS-CH-04 → [EV-KB-001(K013,K020-K022), EV-01-业务图谱, EV-KB-002(K214)]
  GWFD-020301 → [EV-FK-Content-UDG, EV-CFA]
  ADD URR → [EV-FK-Content-UDG, EV-CFA, EV-KB-001]
```

### 7.2 路径B：在线计费端到端

```
[业务] CS-CH-02 在线计费方案
  → DP-CH-04 选择配额耗尽动作（BLOCK/REDIRECT/FORWARD）
  → BR-CH-09 配额降速优先级覆盖
  → SO-CH-09 配额语义（GSU/Final-Unit-Action）
  → SO-CH-10 Ga/Gy协议栈

[特性] CS-CH-02 uses_feature
  → GWFD-020300 在线计费（UDG Gy/OCS）
  → GWFD-020301 内容计费（UDG 基础）
  → GWFD-020306 事件计费（可选）

[任务] GWFD-020300 decomposes_to
  → T-101 License开启（LKV3G5OLCH01）
  → T-006 配置URR（USAGERPTMODE=ONLINE）★ 核心
  → T-007 配置PCC策略组
  → T-001/T-002 过滤条件
  → T-003/T-004 规则与用户模板
  → T-201 配置DCC模板与OCS链路（DIAMCONNGRP/DCCTEMPLATE）
  → T-202 配置在线异常处理（Tx定时器/CCFH）
  → T-203 配置Default Quota容灾
  → T-204 配置配额耗尽动作（QUOTAEXHAUSTACT）
  → T-008 刷新生效

[命令] T-204 invokes → ADD QUOTAEXHAUSTACT
  → operates_on → ConfigObject: QUOTAEXHAUSTACT
    → 关键参数: URRID, FACTION(BLOCK/REDIRECT/FORWARD)
  → constrained_by → CR-10 超时阻塞公式
  → impacted_by → DP-CH-04 sets_value_pattern(FACTION)

[证据] CS-CH-02 → [EV-KB-001(K028-K048), EV-KB-001(K037,K043-K045)]
```

### 7.3 路径C：融合计费端到端

```
[业务] CS-CH-03 融合计费方案
  → DP-CH-04 配额耗尽动作
  → DP-CH-08 跨网元一致性策略
  → BR-CH-10 SMF融合计费三联前置约束
  → BR-CH-12 License前置门控
  → SO-CH-09 配额语义
  → SO-CH-11 N40/PFCP协议栈 ★

[特性] CS-CH-03 uses_feature
  → GWFD-010173 融合计费（UDG N40执行）
  → WSFD-011206 融合计费（UNC Nchf交互）
  → GWFD-020301 内容计费（基础License）

[任务] WSFD-011206 decomposes_to（UNC 18步链）
  → T-101 License开启
  → T-301 SET CHGMODE=NchfMode ★ 三联前置之一
  → T-302 SET CHARGECTRL使能 ★ 三联前置之二
  → T-303 SET CHFINIT=SENDREQ + CHF选择链 ★ 三联前置之三
  → T-309 ADD CHARGECHAR CC属性
  → T-304 ADD CCT模板 + SELECTCCTBYCC
  → T-305 ADD PDUTRIGGER/RGTRIGGER
  → T-306 SET N40APIVER
  → T-307 SET FAILHANDLING 异常处理
  → T-308 SET N40MSGSTG 消息缓存
  → T-006~T-005 URR三件套+绑定链

[命令] T-303 invokes → SET CHFINIT + ADD TNFINS/TNFINSIP/TNFGRP/TNFBINDGRP/SELECTCHFGBYCC
  → operates_on → ConfigObject: CHFINIT, TNFGRP, SELECTCHFGBYCC
  → constrained_by → CR-06 三联前置约束（CHGMODE+CHARGECTRL+CHFINIT）
  → constrained_by → CR-08 跨网元名称一致性

[证据] CS-CH-03 → [EV-KB-001(K001,K101-K121,K201,K202,K105)]
```

---

## 8. 禁止关系检查（§13 合规）

| 禁止关系 | 是否存在 | 说明 |
|---------|---------|------|
| CS → ConfigObject 直接绑定 | ✗ 无 | CS通过uses_feature→Feature→decomposes_to→Task→invokes→Command→operates_on间接到达ConfigObject |
| Feature → MMLCommand 直接绑定 | ✗ 无 | Feature通过decomposes_to→ConfigTask→invokes→MMLCommand间接到达 |
| CS → CommandParameter 直接绑定 | ✗ 无 | CS通过DP.sets_value_pattern间接设置参数 |
| Feature → ConfigObject 直接绑定 | ✗ 无 | Feature通过Task间接操作ConfigObject |
| BusinessRule → CommandRule 直接绑定 | ✗ 无 | BR和CR独立定义，通过共同约束的对象关联 |
| SemanticObject → ConfigObject 直接绑定（非realized_by） | ✗ 无 | SO通过realized_by关系表达，非直接操作 |

> **合规结论**：本图谱严格遵循Schema §13禁止关系约束，所有跨层连接通过标准关系边（uses_feature/decomposes_to/invokes/operates_on）完成。

---

## 9. 跨层一致性检查清单

- [x] 所有CS的uses_feature指向真实存在的Feature（14个）
- [x] 所有Feature的decomposes_to指向真实存在的ConfigTask（28个）
- [x] 所有ConfigTask的invokes指向真实存在的MMLCommand（65个）
- [x] 所有MMLCommand的operates_on指向真实存在的ConfigObject（26个）
- [x] 所有ConfigTask的targets指向真实存在的SemanticObject（12个）或ConfigObject
- [x] 所有DP的selects指向真实存在的CS（7个）
- [x] 路径A/B/C端到端完整：BD→NS→CS→Feature→Task→Command→Object
- [x] 无 §13 禁止关系

---

## 10. 跨层边统计

| 跨层边 | 数量 |
|-------|------|
| CS `uses_feature` | 20 |
| CS `uses_task`（闭包级） | 7 |
| Feature `decomposes_to` ConfigTask | 14 |
| ConfigTask `invokes` MMLCommand | ~50（28 Task × 平均2命令） |
| ConfigTask `targets` SO/ConfigObject | ~28 |
| DP `selects` CS | 3 |
| DP `sets_value_pattern` | 3 |
| **跨层边总计** | **~125** |

---

> 本文件为计费场景三层图谱第5层。第6层证据索引见同目录其他文件。
