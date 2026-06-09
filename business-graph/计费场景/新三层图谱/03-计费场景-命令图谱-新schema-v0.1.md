# 计费场景命令图谱（新 Schema，v0.1）

> 范围：描述计费场景在新三层图谱 schema 下的命令图谱部分。
> 约束：对象、关系、属性命名尽量服从 `三层图谱Schema-最终版-v0.1.md` 与 `三层图谱本体标准定义.md`。
> 说明：本文件只收敛计费场景闭环中实际用到的命令、参数、配置对象、命令规则和 `TaskCommandOrderEdge`，不扩成全量 MML 命令库。

---

## 0. 适用定义与来源

### 0.1 根定义

- `三层图谱本体标准定义.md`
- `三层图谱Schema-最终版-v0.1.md`
- `计费案例核心概念标准定义.md`

### 0.2 计费场景直接来源

- `business-graph/计费场景/feature-knowledge/GWFD-020301-内容计费.md`
- `business-graph/计费场景/feature-knowledge/GWFD-010171-离线计费.md`
- `business-graph/计费场景/feature-knowledge/GWFD-020300-在线计费.md`
- `business-graph/计费场景/feature-knowledge/GWFD-010173-融合计费.md`
- `business-graph/计费场景/feature-knowledge/GWFD-020306-事件计费.md`
- `business-graph/计费场景/feature-knowledge/WSFD-109002-内容计费.md`
- `business-graph/计费场景/feature-knowledge/WSFD-011206-融合计费.md`
- `business-graph/SKILL/feature/UDG/UPF/GWFD-020301/部署UPF_28493406.md`

### 0.3 命令原始来源

- `business-graph/SKILL/command/UDG/ADD URR.md`
- `business-graph/SKILL/command/UDG/ADD URRGROUP.md`
- `business-graph/SKILL/command/UDG/ADD PCCPOLICYGRP.md`
- `business-graph/SKILL/command/UDG/ADD FILTER.md`
- `business-graph/SKILL/command/UDG/ADD L7FILTER.md`
- `business-graph/SKILL/command/UDG/ADD FLOWFILTER.md`
- `business-graph/SKILL/command/UDG/ADD FLTBINDFLOWF.md`
- `business-graph/SKILL/command/UDG/ADD PROTBINDFLOWF.md`
- `business-graph/SKILL/command/UDG/ADD RULE.md`
- `business-graph/SKILL/command/UDG/ADD USERPROFILE.md`
- `business-graph/SKILL/command/UDG/ADD RULEBINDING.md`
- `business-graph/SKILL/command/UDG/SET URRGRPBINDING.md`
- `business-graph/SKILL/command/UDG/SET REFRESHSRV.md`
- `business-graph/SKILL/command/UNC/ADD URR.md`
- `business-graph/SKILL/command/UNC/ADD URRGROUP.md`
- `business-graph/SKILL/command/UNC/ADD PCCPOLICYGRP.md`
- `business-graph/SKILL/command/UNC/ADD RULE.md`
- `business-graph/SKILL/command/UNC/ADD USERPROFILE.md`
- `business-graph/SKILL/command/UNC/SET URRGRPBINDING.md`
- `business-graph/SKILL/command/UNC/ADD USRPROFGROUP.md`
- `business-graph/SKILL/command/UNC/ADD UPBINDUPG.md`
- `business-graph/SKILL/command/UNC/ADD APN.md`
- `business-graph/SKILL/command/UNC/ADD APNUSRPROFG.md`
- `business-graph/SKILL/command/UNC/SET CHARGECTRL.md`
- `business-graph/SKILL/command/UNC/ADD CCT.md`
- `business-graph/SKILL/command/UNC/ADD SELECTCCTBYCC.md`
- `business-graph/SKILL/command/UNC/SET CHFINIT.md`
- `business-graph/SKILL/command/UNC/ADD PDUTRIGGER.md`
- `business-graph/SKILL/command/UNC/ADD RGTRIGGER.md`
- `business-graph/SKILL/command/UNC/SET RGRESCTRL.md`
- `business-graph/SKILL/command/UNC/SET CTXSTARTRATING.md`
- `business-graph/SKILL/command/UNC/ADD HTTPLEGRP.md`
- `business-graph/SKILL/command/UNC/ADD SBIAPLE.md`
- `business-graph/SKILL/command/UNC/ADD TNFGRP.md`
- `business-graph/SKILL/command/UNC/ADD SELECTCHFGBYCC.md`

---

## 1. 新 schema 对齐范围

本文件保留的新命令图谱对象：

- `MMLCommand`
- `CommandParameter`
- `ConfigObject`
- `CommandRule`
- `TaskCommandOrderEdge`

本文件中的共享引用对象：

- `ConfigTask`
- `SemanticObject`

本文件不重复展开：

- `Feature`
- `SubFeature`
- `FeatureRule`
- `BusinessRule`

这些对象已经分别由业务图谱和特性图谱文档承接。

---

## 2. MMLCommand 集合

### 2.1 UDG / UPF 侧核心命令

| `command_id` | `command_name` | `nf_side` | `command_summary` | `supported_by` |
|---|---|---|---|---|
| `CMD-UDG-ADD-URR` | `ADD URR` | `UDG/UPF` | 新增使用量上报规则，定义 URRID、计费模式、统计类型、RG/SID | `ADD URR.md`, `GWFD-020301-内容计费.md` |
| `CMD-UDG-ADD-URRGROUP` | `ADD URRGROUP` | `UDG/UPF` | 组织上下行 URR，形成可被策略组引用的计费组 | `ADD URRGROUP.md`, `GWFD-020301-内容计费.md` |
| `CMD-UDG-ADD-PCCPOLICYGRP` | `ADD PCCPOLICYGRP` | `UDG/UPF` | 将 URRGROUP 包装成可被 RULE 引用的 PCC 策略组 | `ADD PCCPOLICYGRP.md`, `GWFD-020301-内容计费.md` |
| `CMD-UDG-ADD-FILTER` | `ADD FILTER` | `UDG/UPF` | 新增三四层过滤条件，按 IP、端口、协议识别业务 | `ADD FILTER.md`, `GWFD-020301-内容计费.md` |
| `CMD-UDG-ADD-L7FILTER` | `ADD L7FILTER` | `UDG/UPF` | 新增七层过滤条件，按 URL、Host、Method 等识别业务 | `ADD L7FILTER.md`, `GWFD-020301-内容计费.md` |
| `CMD-UDG-ADD-FLOWFILTER` | `ADD FLOWFILTER` | `UDG/UPF` | 新增流过滤器，作为 L34/L7 条件聚合容器 | `ADD FLOWFILTER.md`, `GWFD-020301-内容计费.md` |
| `CMD-UDG-ADD-FLTBINDFLOWF` | `ADD FLTBINDFLOWF` | `UDG/UPF` | 将 FILTER 绑定到 FLOWFILTER | `ADD FLTBINDFLOWF.md`, `GWFD-020301-内容计费.md` |
| `CMD-UDG-ADD-PROTBINDFLOWF` | `ADD PROTBINDFLOWF` | `UDG/UPF` | 将协议和可选 L7FILTER 绑定到 FLOWFILTER | `ADD PROTBINDFLOWF.md`, `GWFD-020301-内容计费.md` |
| `CMD-UDG-ADD-RULE` | `ADD RULE` | `UDG/UPF` | 将 FLOWFILTER 与 PCCPOLICYGRP 绑定，并配置优先级 | `ADD RULE.md`, `GWFD-020301-内容计费.md` |
| `CMD-UDG-ADD-USERPROFILE` | `ADD USERPROFILE` | `UDG/UPF` | 新增用户模板，作为 RULE 及默认计费的承载容器 | `ADD USERPROFILE.md`, `GWFD-020301-内容计费.md` |
| `CMD-UDG-ADD-RULEBINDING` | `ADD RULEBINDING` | `UDG/UPF` | 将 RULE 绑定到 USERPROFILE | `ADD RULEBINDING.md`, `GWFD-020301-内容计费.md` |
| `CMD-UDG-SET-URRGRPBINDING` | `SET URRGRPBINDING` | `UDG/UPF` | 为 USERPROFILE 设置缺省业务、信令、重定向和 TCP 重传计费组 | `SET URRGRPBINDING.md`, `GWFD-020301-内容计费.md` |
| `CMD-UDG-SET-REFRESHSRV` | `SET REFRESHSRV` | `UDG/UPF` | 刷新 Filter / FilterGroup，使新过滤条件真正生效 | `SET REFRESHSRV.md`, `GWFD-020301-内容计费.md` |

### 2.2 UNC / SMF 侧核心命令

| `command_id` | `command_name` | `nf_side` | `command_summary` | `supported_by` |
|---|---|---|---|---|
| `CMD-UNC-ADD-URR` | `ADD URR` | `UNC/SMF` | 新增控制面 URR，定义 ONLINERG/RG/SID 与计费统计方式 | `UNC/ADD URR.md`, `WSFD-109002-内容计费.md` |
| `CMD-UNC-ADD-URRGROUP` | `ADD URRGROUP` | `UNC/SMF` | 组织控制面上下行 URR 组合 | `UNC/ADD URRGROUP.md`, `WSFD-109002-内容计费.md` |
| `CMD-UNC-ADD-PCCPOLICYGRP` | `ADD PCCPOLICYGRP` | `UNC/SMF` | 配置控制面 PCC 策略组，承接 URRGROUP 和 QoS/FUP 属性 | `UNC/ADD PCCPOLICYGRP.md`, `WSFD-109002-内容计费.md` |
| `CMD-UNC-ADD-RULE` | `ADD RULE` | `UNC/SMF` | 配置控制面 Rule，匹配 PCF/PCRF 下发的预定义规则并引用 PCC 策略组 | `UNC/ADD RULE.md`, `WSFD-109002-内容计费.md` |
| `CMD-UNC-ADD-USERPROFILE` | `ADD USERPROFILE` | `UNC/SMF` | 新增控制面用户模板 | `UNC/ADD USERPROFILE.md`, `WSFD-109002-内容计费.md` |
| `CMD-UNC-SET-URRGRPBINDING` | `SET URRGRPBINDING` | `UNC/SMF` | 为 USERPROFILE 绑定缺省计费属性 | `UNC/SET URRGRPBINDING.md`, `WSFD-109002-内容计费.md` |
| `CMD-UNC-ADD-USRPROFGROUP` | `ADD USRPROFGROUP` | `UNC/SMF` | 新增用户模板组，用于 APN/DNN 选择 | `UNC/ADD USRPROFGROUP.md`, `WSFD-109002-内容计费.md` |
| `CMD-UNC-ADD-UPBINDUPG` | `ADD UPBINDUPG` | `UNC/SMF` | 将 USERPROFILE 绑定到 USRPROFGROUP，并附带选择条件 | `UNC/ADD UPBINDUPG.md`, `WSFD-109002-内容计费.md` |
| `CMD-UNC-ADD-APN` | `ADD APN` | `UNC/SMF` | 新增 APN / DNN 实例 | `UNC/ADD APN.md`, `WSFD-109002-内容计费.md` |
| `CMD-UNC-ADD-APNUSRPROFG` | `ADD APNUSRPROFG` | `UNC/SMF` | 将 USRPROFGROUP 绑定到 APN / DNN | `UNC/ADD APNUSRPROFG.md`, `WSFD-109002-内容计费.md` |
| `CMD-UNC-SET-CHARGECTRL` | `SET CHARGECTRL` | `UNC/SMF` | 控制在线/离线/融合计费总开关 | `SET CHARGECTRL.md`, `WSFD-011206-融合计费.md` |
| `CMD-UNC-ADD-CCT` | `ADD CCT` | `UNC/SMF` | 新增融合计费模板 CCT | `ADD CCT.md`, `WSFD-011206-融合计费.md` |
| `CMD-UNC-ADD-SELECTCCTBYCC` | `ADD SELECTCCTBYCC` | `UNC/SMF` | 按 CC 选择 CCT 模板 | `ADD SELECTCCTBYCC.md`, `WSFD-011206-融合计费.md` |
| `CMD-UNC-SET-CHFINIT` | `SET CHFINIT` | `UNC/SMF` | 配置 CCT 激活时是否向 CHF 发起交互 | `SET CHFINIT.md`, `WSFD-011206-融合计费.md` |
| `CMD-UNC-ADD-PDUTRIGGER` | `ADD PDUTRIGGER` | `UNC/SMF` | 配置 PDU 会话级 Trigger 上报方式 | `ADD PDUTRIGGER.md`, `WSFD-011206-融合计费.md` |
| `CMD-UNC-ADD-RGTRIGGER` | `ADD RGTRIGGER` | `UNC/SMF` | 配置 RG 级 Trigger 上报方式 | `ADD RGTRIGGER.md`, `WSFD-011206-融合计费.md` |
| `CMD-UNC-SET-RGRESCTRL` | `SET RGRESCTRL` | `UNC/SMF` | 配置 RG 老化和超规格处理动作 | `SET RGRESCTRL.md`, `WSFD-011206-融合计费.md` |
| `CMD-UNC-SET-CTXSTARTRATING` | `SET CTXSTARTRATING` | `UNC/SMF` | 配置用户激活时发往 OCS/CHF 的初始计费属性 | `SET CTXSTARTRATING.md`, `WSFD-011206-融合计费.md` |
| `CMD-UNC-ADD-HTTPLEGRP` | `ADD HTTPLEGRP` | `UNC/SMF` | 新增 HTTP 本端实体组 | `ADD HTTPLEGRP.md`, `WSFD-011206-融合计费.md` |
| `CMD-UNC-ADD-SBIAPLE` | `ADD SBIAPLE` | `UNC/SMF` | 新增服务化接口本端实体 | `ADD SBIAPLE.md`, `WSFD-011206-融合计费.md` |
| `CMD-UNC-ADD-TNFGRP` | `ADD TNFGRP` | `UNC/SMF` | 新增目标 NF 组，例如 CHF 组 | `ADD TNFGRP.md`, `WSFD-011206-融合计费.md` |
| `CMD-UNC-ADD-SELECTCHFGBYCC` | `ADD SELECTCHFGBYCC` | `UNC/SMF` | 按 CC 选择主备 CHF 组 | `ADD SELECTCHFGBYCC.md`, `WSFD-011206-融合计费.md` |

---

## 3. ConfigObject 集合

### 3.1 UDG / UPF 侧配置对象

| `config_object_id` | `config_object_name` | `object_scope` | `object_summary` | `supported_by` |
|---|---|---|---|---|
| `OBJ-UDG-URR` | `URR` | `UDG/UPF` | 使用量上报规则对象，承载 URRID、计费模式、统计方式、RG/SID | `GWFD-020301-内容计费.md`, `ADD URR.md` |
| `OBJ-UDG-URRGROUP` | `URRGROUP` | `UDG/UPF` | 使用量上报规则组对象，组织上下行在线/离线 URR | `GWFD-020301-内容计费.md`, `ADD URRGROUP.md` |
| `OBJ-UDG-PCCPOLICYGRP` | `PCCPOLICYGRP` | `UDG/UPF` | PCC 策略组对象，将 URRGROUP 转成可被 Rule 引用的计费策略 | `GWFD-020301-内容计费.md`, `ADD PCCPOLICYGRP.md` |
| `OBJ-UDG-FILTER` | `FILTER` | `UDG/UPF` | 三四层过滤器对象 | `GWFD-020301-内容计费.md`, `ADD FILTER.md` |
| `OBJ-UDG-L7FILTER` | `L7FILTER` | `UDG/UPF` | 七层过滤器对象 | `GWFD-020301-内容计费.md`, `ADD L7FILTER.md` |
| `OBJ-UDG-FLOWFILTER` | `FLOWFILTER` | `UDG/UPF` | 流过滤器对象，承接 L34/L7 组合匹配 | `GWFD-020301-内容计费.md`, `ADD FLOWFILTER.md` |
| `OBJ-UDG-RULE` | `RULE` | `UDG/UPF` | 规则对象，将 FLOWFILTER 与 PCCPOLICYGRP 绑定 | `GWFD-020301-内容计费.md`, `ADD RULE.md` |
| `OBJ-UDG-USERPROFILE` | `USERPROFILE` | `UDG/UPF` | 用户模板对象，承接 Rule 和默认计费组 | `GWFD-020301-内容计费.md`, `ADD USERPROFILE.md` |
| `OBJ-UDG-URRGRPBINDING` | `URRGRPBINDING` | `UDG/UPF` | 用户模板默认计费绑定对象 | `GWFD-020301-内容计费.md`, `SET URRGRPBINDING.md` |
| `OBJ-UDG-REFRESHSRV` | `REFRESHSRV` | `UDG/UPF` | 过滤配置刷新动作对象 | `GWFD-020301-内容计费.md`, `SET REFRESHSRV.md` |

### 3.2 UNC / SMF 侧配置对象

| `config_object_id` | `config_object_name` | `object_scope` | `object_summary` | `supported_by` |
|---|---|---|---|---|
| `OBJ-UNC-URR` | `URR` | `UNC/SMF` | 控制面 URR 对象，承载 ONLINERG / RG / SID / 计量方式 | `WSFD-109002-内容计费.md`, `UNC/ADD URR.md` |
| `OBJ-UNC-URRGROUP` | `URRGROUP` | `UNC/SMF` | 控制面 URR 组合对象 | `WSFD-109002-内容计费.md`, `UNC/ADD URRGROUP.md` |
| `OBJ-UNC-PCCPOLICYGRP` | `PCCPOLICYGRP` | `UNC/SMF` | 控制面 PCC 策略组对象 | `WSFD-109002-内容计费.md`, `UNC/ADD PCCPOLICYGRP.md` |
| `OBJ-UNC-RULE` | `RULE` | `UNC/SMF` | 控制面 Rule 对象 | `WSFD-109002-内容计费.md`, `UNC/ADD RULE.md` |
| `OBJ-UNC-USERPROFILE` | `USERPROFILE` | `UNC/SMF` | 控制面用户模板对象 | `WSFD-109002-内容计费.md`, `UNC/ADD USERPROFILE.md` |
| `OBJ-UNC-USRPROFGROUP` | `USRPROFGROUP` | `UNC/SMF` | 用户模板组对象 | `WSFD-109002-内容计费.md`, `UNC/ADD USRPROFGROUP.md` |
| `OBJ-UNC-UPBINDUPG` | `UPBINDUPG` | `UNC/SMF` | 用户模板组到用户模板的绑定对象 | `WSFD-109002-内容计费.md`, `UNC/ADD UPBINDUPG.md` |
| `OBJ-UNC-APN` | `APN` | `UNC/SMF` | APN / DNN 实例对象 | `WSFD-109002-内容计费.md`, `UNC/ADD APN.md` |
| `OBJ-UNC-APNUSRPROFG` | `APNUSRPROFG` | `UNC/SMF` | APN 到用户模板组的绑定对象 | `WSFD-109002-内容计费.md`, `UNC/ADD APNUSRPROFG.md` |
| `OBJ-UNC-CCT` | `CCT` | `UNC/SMF` | 融合计费模板对象 | `WSFD-011206-融合计费.md`, `ADD CCT.md` |
| `OBJ-UNC-SELECTCCTBYCC` | `SELECTCCTBYCC` | `UNC/SMF` | 基于 CC 选择 CCT 的对象 | `WSFD-011206-融合计费.md`, `ADD SELECTCCTBYCC.md` |
| `OBJ-UNC-HTTPLEGRP` | `HTTPLEGRP` | `UNC/SMF` | HTTP 本端实体组对象 | `WSFD-011206-融合计费.md`, `ADD HTTPLEGRP.md` |
| `OBJ-UNC-SBIAPLE` | `SBIAPLE` | `UNC/SMF` | 服务化接口本端实体对象 | `WSFD-011206-融合计费.md`, `ADD SBIAPLE.md` |
| `OBJ-UNC-TNFGRP` | `TNFGRP` | `UNC/SMF` | 目标 NF 组对象，例如主备 CHF 组 | `WSFD-011206-融合计费.md`, `ADD TNFGRP.md` |
| `OBJ-UNC-SELECTCHFGBYCC` | `SELECTCHFGBYCC` | `UNC/SMF` | 基于 CC 选择主备 CHF 的对象 | `WSFD-011206-融合计费.md`, `ADD SELECTCHFGBYCC.md` |
| `OBJ-UNC-CHARGECTRL` | `CHARGECTRL` | `UNC/SMF` | 计费方式控制对象 | `WSFD-011206-融合计费.md`, `SET CHARGECTRL.md` |
| `OBJ-UNC-PDUTRIGGER` | `PDUTRIGGER` | `UNC/SMF` | PDU 会话级 trigger 配置对象 | `WSFD-011206-融合计费.md`, `ADD PDUTRIGGER.md` |
| `OBJ-UNC-RGTRIGGER` | `RGTRIGGER` | `UNC/SMF` | RG 级 trigger 配置对象 | `WSFD-011206-融合计费.md`, `ADD RGTRIGGER.md` |
| `OBJ-UNC-RGRESCTRL` | `RGRESCTRL` | `UNC/SMF` | RG 老化和资源控制对象 | `WSFD-011206-融合计费.md`, `SET RGRESCTRL.md` |
| `OBJ-UNC-CTXSTARTRATING` | `CTXSTARTRATING` | `UNC/SMF` | 用户激活初始计费属性对象 | `WSFD-011206-融合计费.md`, `SET CTXSTARTRATING.md` |

---

## 4. CommandParameter 集合（场景关键参数）

### 4.1 UDG / UPF 侧关键参数

| `parameter_id` | `command_ref` | `parameter_name` | `parameter_role` | `references` |
|---|---|---|---|---|
| `PAR-UDG-URR-URRNAME` | `CMD-UDG-ADD-URR` | `URRNAME` | URR 对象主键名称 | `OBJ-UDG-URR` |
| `PAR-UDG-URR-URRID` | `CMD-UDG-ADD-URR` | `URRID` | 全局唯一计费标识 | `OBJ-UDG-URR` |
| `PAR-UDG-URR-USAGERPTMODE` | `CMD-UDG-ADD-URR` | `USAGERPTMODE` | 在线/离线/监控/QoS 计费模式 | `OBJ-UDG-URR` |
| `PAR-UDG-URR-ONLMETERINGTYPE` | `CMD-UDG-ADD-URR` | `ONLMETERINGTYPE` | 在线统计类型 | `OBJ-UDG-URR` |
| `PAR-UDG-URR-OFFMETERINGTYPE` | `CMD-UDG-ADD-URR` | `OFFMETERINGTYPE` | 离线统计类型 | `OBJ-UDG-URR` |
| `PAR-UDG-URR-RG` | `CMD-UDG-ADD-URR` | `RG` | 费率组标识 | `OBJ-UDG-URR` |
| `PAR-UDG-URR-SID` | `CMD-UDG-ADD-URR` | `SID` | 业务标识 | `OBJ-UDG-URR` |
| `PAR-UDG-URRGROUP-NAME` | `CMD-UDG-ADD-URRGROUP` | `URRGROUPNAME` | URR 组对象名 | `OBJ-UDG-URRGROUP` |
| `PAR-UDG-PCCPOLICYGRP-NAME` | `CMD-UDG-ADD-PCCPOLICYGRP` | `PCCPOLICYGRPNM` | PCC 策略组对象名 | `OBJ-UDG-PCCPOLICYGRP` |
| `PAR-UDG-PCCPOLICYGRP-URRGROUP` | `CMD-UDG-ADD-PCCPOLICYGRP` | `URRGROUPNAME` | 引用 URRGROUP | `OBJ-UDG-URRGROUP` |
| `PAR-UDG-FILTER-NAME` | `CMD-UDG-ADD-FILTER` | `FILTERNAME` | FILTER 对象名 | `OBJ-UDG-FILTER` |
| `PAR-UDG-FILTER-L34PROTO` | `CMD-UDG-ADD-FILTER` | `L34PROTOCOL` | 三四层协议类型 | `OBJ-UDG-FILTER` |
| `PAR-UDG-L7FILTER-NAME` | `CMD-UDG-ADD-L7FILTER` | `L7FILTERNAME` | L7FILTER 对象名 | `OBJ-UDG-L7FILTER` |
| `PAR-UDG-L7FILTER-URL` | `CMD-UDG-ADD-L7FILTER` | `URL/HOST` | 七层匹配内容 | `OBJ-UDG-L7FILTER` |
| `PAR-UDG-FLOWFILTER-NAME` | `CMD-UDG-ADD-FLOWFILTER` | `FLOWFILTERNAME` | FLOWFILTER 对象名 | `OBJ-UDG-FLOWFILTER` |
| `PAR-UDG-FLTBINDFLOWF-FLOWFILTER` | `CMD-UDG-ADD-FLTBINDFLOWF` | `FLOWFILTERNAME` | 引用 FLOWFILTER | `OBJ-UDG-FLOWFILTER` |
| `PAR-UDG-FLTBINDFLOWF-FILTER` | `CMD-UDG-ADD-FLTBINDFLOWF` | `FILTERNAME` | 引用 FILTER | `OBJ-UDG-FILTER` |
| `PAR-UDG-PROTBINDFLOWF-PROTOCOL` | `CMD-UDG-ADD-PROTBINDFLOWF` | `PROTOCOLNAME` | 绑定协议 | `OBJ-UDG-FLOWFILTER` |
| `PAR-UDG-PROTBINDFLOWF-L7FILTER` | `CMD-UDG-ADD-PROTBINDFLOWF` | `L7FILTERNAME` | 引用 L7FILTER | `OBJ-UDG-L7FILTER` |
| `PAR-UDG-RULE-RULENAME` | `CMD-UDG-ADD-RULE` | `RULENAME` | Rule 对象名 | `OBJ-UDG-RULE` |
| `PAR-UDG-RULE-FLOWFILTER` | `CMD-UDG-ADD-RULE` | `FLOWFILTERNAME` | 引用 FLOWFILTER | `OBJ-UDG-FLOWFILTER` |
| `PAR-UDG-RULE-POLICYNAME` | `CMD-UDG-ADD-RULE` | `POLICYNAME` | 引用 PCCPOLICYGRP | `OBJ-UDG-PCCPOLICYGRP` |
| `PAR-UDG-RULE-PRIORITY` | `CMD-UDG-ADD-RULE` | `PRIORITY` | Rule 优先级 | `OBJ-UDG-RULE` |
| `PAR-UDG-UP-NAME` | `CMD-UDG-ADD-USERPROFILE` | `USERPROFILENAME` | 用户模板对象名 | `OBJ-UDG-USERPROFILE` |
| `PAR-UDG-RULEBINDING-UP` | `CMD-UDG-ADD-RULEBINDING` | `USERPROFILENAME` | 引用 USERPROFILE | `OBJ-UDG-USERPROFILE` |
| `PAR-UDG-RULEBINDING-RULE` | `CMD-UDG-ADD-RULEBINDING` | `RULENAME` | 引用 RULE | `OBJ-UDG-RULE` |
| `PAR-UDG-URRGRPBINDING-DFTURR` | `CMD-UDG-SET-URRGRPBINDING` | `DFTURRGRPNAME` | 缺省业务 URR 组 | `OBJ-UDG-URRGROUP` |
| `PAR-UDG-URRGRPBINDING-DFTSIG` | `CMD-UDG-SET-URRGRPBINDING` | `DFTSIGURRGNAME` | 缺省信令 URR 组 | `OBJ-UDG-URRGROUP` |
| `PAR-UDG-REFRESHSRV-TYPE` | `CMD-UDG-SET-REFRESHSRV` | `REFRESHTYPE` | 刷新范围 | `OBJ-UDG-REFRESHSRV` |

### 4.2 UNC / SMF 侧关键参数

| `parameter_id` | `command_ref` | `parameter_name` | `parameter_role` | `references` |
|---|---|---|---|---|
| `PAR-UNC-URR-URRNAME` | `CMD-UNC-ADD-URR` | `URRNAME` | URR 对象主键名称 | `OBJ-UNC-URR` |
| `PAR-UNC-URR-URRID` | `CMD-UNC-ADD-URR` | `URRID` | URR 标识 | `OBJ-UNC-URR` |
| `PAR-UNC-URR-USAGERPTMODE` | `CMD-UNC-ADD-URR` | `USAGERPTMODE` | 计费模式 | `OBJ-UNC-URR` |
| `PAR-UNC-URR-OFFCOMPOUNDTYPE` | `CMD-UNC-ADD-URR` | `OFFCOMPOUNDTYPE` | 离线费率标识组成方式 | `OBJ-UNC-URR` |
| `PAR-UNC-URR-ONLCOMPOUNDTYPE` | `CMD-UNC-ADD-URR` | `ONLCOMPOUNDTYPE` | 在线费率标识组成方式 | `OBJ-UNC-URR` |
| `PAR-UNC-URR-RG` | `CMD-UNC-ADD-URR` | `RG` | 离线费率组 | `OBJ-UNC-URR` |
| `PAR-UNC-URR-SID` | `CMD-UNC-ADD-URR` | `SID` | 离线业务标识 | `OBJ-UNC-URR` |
| `PAR-UNC-URR-ONLINERG` | `CMD-UNC-ADD-URR` | `ONLINERG` | 在线费率组 | `OBJ-UNC-URR` |
| `PAR-UNC-URRGROUP-NAME` | `CMD-UNC-ADD-URRGROUP` | `URRGROUPNAME` | URR 组对象名 | `OBJ-UNC-URRGROUP` |
| `PAR-UNC-PCCPOLICYGRP-NAME` | `CMD-UNC-ADD-PCCPOLICYGRP` | `PCCPOLICYGRPNM` | PCC 策略组对象名 | `OBJ-UNC-PCCPOLICYGRP` |
| `PAR-UNC-PCCPOLICYGRP-URRGROUP` | `CMD-UNC-ADD-PCCPOLICYGRP` | `URRGROUPNAME` | 引用 URRGROUP | `OBJ-UNC-URRGROUP` |
| `PAR-UNC-RULE-RULENAME` | `CMD-UNC-ADD-RULE` | `RULENAME` | Rule 对象名 | `OBJ-UNC-RULE` |
| `PAR-UNC-RULE-POLICYNAME` | `CMD-UNC-ADD-RULE` | `POLICYNAME` | 引用 PCCPOLICYGRP | `OBJ-UNC-PCCPOLICYGRP` |
| `PAR-UNC-RULE-PRIORITY` | `CMD-UNC-ADD-RULE` | `PRIORITY` | Rule 优先级 | `OBJ-UNC-RULE` |
| `PAR-UNC-UP-NAME` | `CMD-UNC-ADD-USERPROFILE` | `USERPROFILENAME` | 用户模板对象名 | `OBJ-UNC-USERPROFILE` |
| `PAR-UNC-URRGRPBINDING-DFTURR` | `CMD-UNC-SET-URRGRPBINDING` | `DFTURRGRPNAME` | 缺省 URR 组 | `OBJ-UNC-URRGROUP` |
| `PAR-UNC-UPG-NAME` | `CMD-UNC-ADD-USRPROFGROUP` | `USERPROFGNAME` | 用户模板组对象名 | `OBJ-UNC-USRPROFGROUP` |
| `PAR-UNC-UPBINDUPG-PRIORITY` | `CMD-UNC-ADD-UPBINDUPG` | `PRIORITY` | UserProfile 选择优先级 | `OBJ-UNC-UPBINDUPG` |
| `PAR-UNC-UPBINDUPG-UP` | `CMD-UNC-ADD-UPBINDUPG` | `USERPROFILENAME` | 引用 USERPROFILE | `OBJ-UNC-USERPROFILE` |
| `PAR-UNC-APN-NAME` | `CMD-UNC-ADD-APN` | `APN` | APN / DNN 对象名 | `OBJ-UNC-APN` |
| `PAR-UNC-APNUSRPROFG-APN` | `CMD-UNC-ADD-APNUSRPROFG` | `APN` | 引用 APN | `OBJ-UNC-APN` |
| `PAR-UNC-APNUSRPROFG-UPG` | `CMD-UNC-ADD-APNUSRPROFG` | `USERPROFGNAME` | 引用 USRPROFGROUP | `OBJ-UNC-USRPROFGROUP` |
| `PAR-UNC-CHARGECTRL-HOMECONVERGED` | `CMD-UNC-SET-CHARGECTRL` | `HOMECONVERGED` | 归属地融合计费总开关 | `OBJ-UNC-CHARGECTRL` |
| `PAR-UNC-CCT-NAME` | `CMD-UNC-ADD-CCT` | `CCTMPLTNAME` | CCT 对象名 | `OBJ-UNC-CCT` |
| `PAR-UNC-SELECTCCTBYCC-CCVALUE` | `CMD-UNC-ADD-SELECTCCTBYCC` | `CCVALUE` | CC 选择值 | `OBJ-UNC-SELECTCCTBYCC` |
| `PAR-UNC-SELECTCCTBYCC-CCT` | `CMD-UNC-ADD-SELECTCCTBYCC` | `CCTMPLTNAME` | 引用 CCT | `OBJ-UNC-CCT` |
| `PAR-UNC-CHFINIT-SW` | `CMD-UNC-SET-CHFINIT` | `CHFINIT` | 激活是否与 CHF 交互 | `OBJ-UNC-CCT` |
| `PAR-UNC-PDUTRIGGER-CCT` | `CMD-UNC-ADD-PDUTRIGGER` | `CCTMPLTNAME` | 引用 CCT | `OBJ-UNC-CCT` |
| `PAR-UNC-RGTRIGGER-CCT` | `CMD-UNC-ADD-RGTRIGGER` | `CCTMPLTNAME` | 引用 CCT | `OBJ-UNC-CCT` |
| `PAR-UNC-RGRESCTRL-ONLRGAGESW` | `CMD-UNC-SET-RGRESCTRL` | `ONLRGAGESW` | 在线 RG 老化开关 | `OBJ-UNC-RGRESCTRL` |
| `PAR-UNC-CTXSTARTRATING-UP` | `CMD-UNC-SET-CTXSTARTRATING` | `USERPROFILENAME` | 引用 USERPROFILE | `OBJ-UNC-USERPROFILE` |
| `PAR-UNC-CTXSTARTRATING-URRGROUP` | `CMD-UNC-SET-CTXSTARTRATING` | `CTXRURRGRPNAME1` | 引用 URRGROUP | `OBJ-UNC-URRGROUP` |
| `PAR-UNC-HTTPLEGRP-INDEX` | `CMD-UNC-ADD-HTTPLEGRP` | `INDEX` | HTTP 本端实体组索引 | `OBJ-UNC-HTTPLEGRP` |
| `PAR-UNC-SBIAPLE-HTTPLEGRPIDX` | `CMD-UNC-ADD-SBIAPLE` | `HTTPLEGRPIDX` | 引用 HTTPLEGRP | `OBJ-UNC-HTTPLEGRP` |
| `PAR-UNC-TNFGRP-NAME` | `CMD-UNC-ADD-TNFGRP` | `TNFGRPNAME` | 目标 NF 组名称 | `OBJ-UNC-TNFGRP` |
| `PAR-UNC-SELECTCHFGBYCC-PRIMARY` | `CMD-UNC-ADD-SELECTCHFGBYCC` | `PRIMARYCHFGRP` | 引用主 CHF 组 | `OBJ-UNC-TNFGRP` |
| `PAR-UNC-SELECTCHFGBYCC-SECONDARY` | `CMD-UNC-ADD-SELECTCHFGBYCC` | `SECONDARYCHFGRP` | 引用备 CHF 组 | `OBJ-UNC-TNFGRP` |

---

## 5. CommandRule 集合

| `rule_id` | `rule_name` | `rule_scope` | `rule_logic` | `supported_by` |
|---|---|---|---|---|
| `CR-01` | `UDG.URRID全局唯一` | `CMD-UDG-ADD-URR / PAR-UDG-URR-URRID / OBJ-UDG-URR` | UDG 侧 URRID 在所有 URR 内必须唯一，建议从 1000 开始分配 | `ADD URR.md` |
| `CR-02` | `SMF.URRID全局唯一` | `CMD-UNC-ADD-URR / PAR-UNC-URR-URRID / OBJ-UNC-URR` | SMF 侧 URRID 在所有 URR 内必须唯一 | `UNC/ADD URR.md` |
| `CR-03` | `URRGROUP至少绑定一个URR` | `CMD-UDG-ADD-URRGROUP / CMD-UNC-ADD-URRGROUP / OBJ-UDG-URRGROUP / OBJ-UNC-URRGROUP` | 上下行 URR 参数至少要配置一个，否则 URRGROUP 无效 | `ADD URRGROUP.md`, `UNC/ADD URRGROUP.md` |
| `CR-04` | `URRGROUP上下行同位置模式一致` | `CMD-UNC-ADD-URRGROUP / OBJ-UNC-URRGROUP` | 同一编号的上行和下行 URR 使用量上报模式应一致 | `UNC/ADD URRGROUP.md` |
| `CR-05` | `PCC策略组被绑定后不可删除` | `CMD-UDG-ADD-PCCPOLICYGRP / CMD-UNC-ADD-PCCPOLICYGRP / OBJ-UDG-PCCPOLICYGRP / OBJ-UNC-PCCPOLICYGRP` | 被 Rule 或其他对象引用后的 PCCPOLICYGRP 不能直接删除 | `ADD PCCPOLICYGRP.md`, `UNC/ADD PCCPOLICYGRP.md` |
| `CR-06` | `Rule同策略类型按优先级单选` | `CMD-UDG-ADD-RULE / CMD-UNC-ADD-RULE / OBJ-UDG-RULE / OBJ-UNC-RULE` | 同一策略类型多条 Rule 同时命中时按 PRIORITY 选择；值越小优先级越高 | `ADD RULE.md`, `UNC/ADD RULE.md` |
| `CR-07` | `Rule优先级不要并列` | `CMD-UDG-ADD-RULE / CMD-UNC-ADD-RULE / PAR-UDG-RULE-PRIORITY / PAR-UNC-RULE-PRIORITY` | 并列优先级在重启后无法保证先后，建议不同 Rule 使用不同优先级 | `ADD RULE.md`, `UNC/ADD RULE.md` |
| `CR-08` | `UserProfile与Rule规格类型必须一致` | `CMD-UDG-ADD-USERPROFILE / CMD-UDG-ADD-RULEBINDING / CMD-UNC-ADD-USERPROFILE / OBJ-UDG-USERPROFILE / OBJ-UNC-USERPROFILE` | DEFAULT 类型 USERPROFILE 只能绑定 DEFAULT 类型 Rule；规格受限规则同理 | `ADD USERPROFILE.md`, `ADD RULEBINDING.md`, `UNC/ADD USERPROFILE.md` |
| `CR-09` | `UserProfile缺省计费需兜底` | `CMD-UDG-SET-URRGRPBINDING / OBJ-UDG-URRGRPBINDING` | 建议同时配置缺省业务 URR 组和缺省信令 URR 组，否则部分流量可能无法计费 | `SET URRGRPBINDING.md` |
| `CR-10` | `Filter变更后必须刷新` | `CMD-UDG-ADD-FILTER / CMD-UDG-ADD-FLTBINDFLOWF / CMD-UDG-SET-REFRESHSRV / OBJ-UDG-FILTER / OBJ-UDG-REFRESHSRV` | 新增或修改 Filter 以及其间接绑定后，必须执行 SET REFRESHSRV 才能生效 | `ADD FILTER.md`, `ADD FLTBINDFLOWF.md`, `SET REFRESHSRV.md` |
| `CR-11` | `SET REFRESHSRV后30秒内禁止改Filter` | `CMD-UDG-SET-REFRESHSRV / OBJ-UDG-REFRESHSRV` | 刷新后 30 秒内不允许修改 Filter 或被绑定的 IPList | `SET REFRESHSRV.md` |
| `CR-12` | `L7协议与L7FILTER绑定必须匹配` | `CMD-UDG-ADD-PROTBINDFLOWF / PAR-UDG-PROTBINDFLOWF-PROTOCOL / PAR-UDG-PROTBINDFLOWF-L7FILTER` | 如果协议与目标业务不匹配，例如网站是 https 却配置 http，则命中失败 | `ADD PROTBINDFLOWF.md` |
| `CR-13` | `SMF与UPF URR关键参数必须一致` | `OBJ-UDG-URR / OBJ-UNC-URR` | URRID、USAGERPTMODE、OFFMETERINGTYPE、ONLMETERINGTYPE、RG/SID 等跨侧保持一致 | `GWFD-020301-内容计费.md`, `WSFD-109002-内容计费.md` |
| `CR-14` | `SMF与UPF Rule和UserProfile名称必须一致` | `OBJ-UDG-RULE / OBJ-UNC-RULE / OBJ-UDG-USERPROFILE / OBJ-UNC-USERPROFILE` | RULENAME、USERPROFILENAME、POLICYTYPE+POLICYNAME 跨侧保持一致，否则策略无法按预期生效 | `GWFD-020301-内容计费.md`, `WSFD-109002-内容计费.md` |
| `CR-15` | `融合计费CCT按CC选择值不可冲突` | `CMD-UNC-ADD-SELECTCCTBYCC / OBJ-UNC-SELECTCCTBYCC` | CCVALUE 与 MASK 组合不能与已有配置冲突 | `ADD SELECTCCTBYCC.md` |
| `CR-16` | `融合计费CHF组按CC选择值不可冲突` | `CMD-UNC-ADD-SELECTCHFGBYCC / OBJ-UNC-SELECTCHFGBYCC` | CCVALUE 与 MASK 组合不能与已有配置冲突 | `ADD SELECTCHFGBYCC.md` |
| `CR-17` | `融合计费激活交互受CHFINIT控制` | `CMD-UNC-SET-CHFINIT / OBJ-UNC-CCT` | CCT 激活时是否向 CHF 交互由 CHFINIT 控制，SENDREQ/NOTSENDREQ/INITRGTRIGR 三类模式 | `SET CHFINIT.md` |
| `CR-18` | `融合计费RG老化受QHT与RGRESCTRL共同控制` | `CMD-UNC-SET-RGRESCTRL / OBJ-UNC-RGRESCTRL` | RG 老化仅在相关 QHT 场景约束下生效；不同计费模式生效时机不同 | `SET RGRESCTRL.md` |
| `CR-19` | `融合计费初始计费属性必须先有URRGROUP` | `CMD-UNC-SET-CTXSTARTRATING / PAR-UNC-CTXSTARTRATING-URRGROUP / OBJ-UNC-URRGROUP` | CTXSTARTRATING 绑定的初始计费属性必须由已有 URRGROUP 提供 | `SET CTXSTARTRATING.md` |

---

## 6. 关系定义

### 6.1 MMLCommand `operates_on` ConfigObject

| 起点 | 关系 | 终点 |
|---|---|---|
| `CMD-UDG-ADD-URR` | `operates_on` | `OBJ-UDG-URR` |
| `CMD-UDG-ADD-URRGROUP` | `operates_on` | `OBJ-UDG-URRGROUP` |
| `CMD-UDG-ADD-PCCPOLICYGRP` | `operates_on` | `OBJ-UDG-PCCPOLICYGRP` |
| `CMD-UDG-ADD-FILTER` | `operates_on` | `OBJ-UDG-FILTER` |
| `CMD-UDG-ADD-L7FILTER` | `operates_on` | `OBJ-UDG-L7FILTER` |
| `CMD-UDG-ADD-FLOWFILTER` | `operates_on` | `OBJ-UDG-FLOWFILTER` |
| `CMD-UDG-ADD-FLTBINDFLOWF` | `operates_on` | `OBJ-UDG-FLOWFILTER` |
| `CMD-UDG-ADD-PROTBINDFLOWF` | `operates_on` | `OBJ-UDG-FLOWFILTER` |
| `CMD-UDG-ADD-RULE` | `operates_on` | `OBJ-UDG-RULE` |
| `CMD-UDG-ADD-USERPROFILE` | `operates_on` | `OBJ-UDG-USERPROFILE` |
| `CMD-UDG-ADD-RULEBINDING` | `operates_on` | `OBJ-UDG-USERPROFILE` |
| `CMD-UDG-SET-URRGRPBINDING` | `operates_on` | `OBJ-UDG-URRGRPBINDING` |
| `CMD-UDG-SET-REFRESHSRV` | `operates_on` | `OBJ-UDG-REFRESHSRV` |
| `CMD-UNC-ADD-URR` | `operates_on` | `OBJ-UNC-URR` |
| `CMD-UNC-ADD-URRGROUP` | `operates_on` | `OBJ-UNC-URRGROUP` |
| `CMD-UNC-ADD-PCCPOLICYGRP` | `operates_on` | `OBJ-UNC-PCCPOLICYGRP` |
| `CMD-UNC-ADD-RULE` | `operates_on` | `OBJ-UNC-RULE` |
| `CMD-UNC-ADD-USERPROFILE` | `operates_on` | `OBJ-UNC-USERPROFILE` |
| `CMD-UNC-SET-URRGRPBINDING` | `operates_on` | `OBJ-UNC-USERPROFILE` |
| `CMD-UNC-ADD-USRPROFGROUP` | `operates_on` | `OBJ-UNC-USRPROFGROUP` |
| `CMD-UNC-ADD-UPBINDUPG` | `operates_on` | `OBJ-UNC-UPBINDUPG` |
| `CMD-UNC-ADD-APN` | `operates_on` | `OBJ-UNC-APN` |
| `CMD-UNC-ADD-APNUSRPROFG` | `operates_on` | `OBJ-UNC-APNUSRPROFG` |
| `CMD-UNC-SET-CHARGECTRL` | `operates_on` | `OBJ-UNC-CHARGECTRL` |
| `CMD-UNC-ADD-CCT` | `operates_on` | `OBJ-UNC-CCT` |
| `CMD-UNC-ADD-SELECTCCTBYCC` | `operates_on` | `OBJ-UNC-SELECTCCTBYCC` |
| `CMD-UNC-SET-CHFINIT` | `operates_on` | `OBJ-UNC-CCT` |
| `CMD-UNC-ADD-PDUTRIGGER` | `operates_on` | `OBJ-UNC-PDUTRIGGER` |
| `CMD-UNC-ADD-RGTRIGGER` | `operates_on` | `OBJ-UNC-RGTRIGGER` |
| `CMD-UNC-SET-RGRESCTRL` | `operates_on` | `OBJ-UNC-RGRESCTRL` |
| `CMD-UNC-SET-CTXSTARTRATING` | `operates_on` | `OBJ-UNC-CTXSTARTRATING` |
| `CMD-UNC-ADD-HTTPLEGRP` | `operates_on` | `OBJ-UNC-HTTPLEGRP` |
| `CMD-UNC-ADD-SBIAPLE` | `operates_on` | `OBJ-UNC-SBIAPLE` |
| `CMD-UNC-ADD-TNFGRP` | `operates_on` | `OBJ-UNC-TNFGRP` |
| `CMD-UNC-ADD-SELECTCHFGBYCC` | `operates_on` | `OBJ-UNC-SELECTCHFGBYCC` |

### 6.2 CommandParameter `references` ConfigObject

| 起点 | 关系 | 终点 |
|---|---|---|
| `PAR-UDG-PCCPOLICYGRP-URRGROUP` | `references` | `OBJ-UDG-URRGROUP` |
| `PAR-UDG-FLTBINDFLOWF-FLOWFILTER` | `references` | `OBJ-UDG-FLOWFILTER` |
| `PAR-UDG-FLTBINDFLOWF-FILTER` | `references` | `OBJ-UDG-FILTER` |
| `PAR-UDG-PROTBINDFLOWF-L7FILTER` | `references` | `OBJ-UDG-L7FILTER` |
| `PAR-UDG-RULE-FLOWFILTER` | `references` | `OBJ-UDG-FLOWFILTER` |
| `PAR-UDG-RULE-POLICYNAME` | `references` | `OBJ-UDG-PCCPOLICYGRP` |
| `PAR-UDG-RULEBINDING-UP` | `references` | `OBJ-UDG-USERPROFILE` |
| `PAR-UDG-RULEBINDING-RULE` | `references` | `OBJ-UDG-RULE` |
| `PAR-UDG-URRGRPBINDING-DFTURR` | `references` | `OBJ-UDG-URRGROUP` |
| `PAR-UDG-URRGRPBINDING-DFTSIG` | `references` | `OBJ-UDG-URRGROUP` |
| `PAR-UNC-PCCPOLICYGRP-URRGROUP` | `references` | `OBJ-UNC-URRGROUP` |
| `PAR-UNC-RULE-POLICYNAME` | `references` | `OBJ-UNC-PCCPOLICYGRP` |
| `PAR-UNC-URRGRPBINDING-DFTURR` | `references` | `OBJ-UNC-URRGROUP` |
| `PAR-UNC-UPBINDUPG-UP` | `references` | `OBJ-UNC-USERPROFILE` |
| `PAR-UNC-APNUSRPROFG-APN` | `references` | `OBJ-UNC-APN` |
| `PAR-UNC-APNUSRPROFG-UPG` | `references` | `OBJ-UNC-USRPROFGROUP` |
| `PAR-UNC-SELECTCCTBYCC-CCT` | `references` | `OBJ-UNC-CCT` |
| `PAR-UNC-PDUTRIGGER-CCT` | `references` | `OBJ-UNC-CCT` |
| `PAR-UNC-RGTRIGGER-CCT` | `references` | `OBJ-UNC-CCT` |
| `PAR-UNC-CTXSTARTRATING-UP` | `references` | `OBJ-UNC-USERPROFILE` |
| `PAR-UNC-CTXSTARTRATING-URRGROUP` | `references` | `OBJ-UNC-URRGROUP` |
| `PAR-UNC-SBIAPLE-HTTPLEGRPIDX` | `references` | `OBJ-UNC-HTTPLEGRP` |
| `PAR-UNC-SELECTCHFGBYCC-PRIMARY` | `references` | `OBJ-UNC-TNFGRP` |
| `PAR-UNC-SELECTCHFGBYCC-SECONDARY` | `references` | `OBJ-UNC-TNFGRP` |

### 6.3 ConfigObject 之间的关系边

| 起点 | 关系 | 终点 | 说明 |
|---|---|---|---|
| `OBJ-UDG-URRGROUP` | `contains` | `OBJ-UDG-URR` | URRGROUP 组织多个 URR |
| `OBJ-UDG-PCCPOLICYGRP` | `refers_to` | `OBJ-UDG-URRGROUP` | PCC 策略组引用 URRGROUP |
| `OBJ-UDG-FLOWFILTER` | `contains` | `OBJ-UDG-FILTER` | FLOWFILTER 可绑定 L34 FILTER |
| `OBJ-UDG-FLOWFILTER` | `contains` | `OBJ-UDG-L7FILTER` | FLOWFILTER 可绑定 L7FILTER |
| `OBJ-UDG-RULE` | `refers_to` | `OBJ-UDG-FLOWFILTER` | Rule 引用匹配条件 |
| `OBJ-UDG-RULE` | `refers_to` | `OBJ-UDG-PCCPOLICYGRP` | Rule 引用计费动作 |
| `OBJ-UDG-USERPROFILE` | `contains` | `OBJ-UDG-RULE` | UserProfile 承接多条 Rule |
| `OBJ-UDG-USERPROFILE` | `refers_to` | `OBJ-UDG-URRGROUP` | UserProfile 可引用默认 URR 组 |
| `OBJ-UNC-URRGROUP` | `contains` | `OBJ-UNC-URR` | 控制面 URRGROUP 组织多个 URR |
| `OBJ-UNC-PCCPOLICYGRP` | `refers_to` | `OBJ-UNC-URRGROUP` | 控制面 PCC 策略组引用 URRGROUP |
| `OBJ-UNC-RULE` | `refers_to` | `OBJ-UNC-PCCPOLICYGRP` | 控制面 Rule 引用 PCC 策略组 |
| `OBJ-UNC-USERPROFILE` | `contains` | `OBJ-UNC-RULE` | 控制面 UserProfile 承接多条 Rule |
| `OBJ-UNC-USERPROFILE` | `refers_to` | `OBJ-UNC-URRGROUP` | 控制面 UserProfile 引用默认 URR 组 |
| `OBJ-UNC-USRPROFGROUP` | `contains` | `OBJ-UNC-USERPROFILE` | UserProfileGroup 承接多条 UserProfile 选择项 |
| `OBJ-UNC-APNUSRPROFG` | `refers_to` | `OBJ-UNC-APN` | 绑定 APN |
| `OBJ-UNC-APNUSRPROFG` | `refers_to` | `OBJ-UNC-USRPROFGROUP` | 绑定 UserProfileGroup |
| `OBJ-UNC-SELECTCCTBYCC` | `refers_to` | `OBJ-UNC-CCT` | 通过 CC 选择 CCT |
| `OBJ-UNC-SBIAPLE` | `refers_to` | `OBJ-UNC-HTTPLEGRP` | 服务化接口实体依赖 HTTPLEGRP |
| `OBJ-UNC-SELECTCHFGBYCC` | `refers_to` | `OBJ-UNC-TNFGRP` | 通过 CC 选择主备 CHF 组 |
| `OBJ-UNC-CTXSTARTRATING` | `refers_to` | `OBJ-UNC-USERPROFILE` | 初始计费属性绑定到 UserProfile |
| `OBJ-UNC-CTXSTARTRATING` | `refers_to` | `OBJ-UNC-URRGROUP` | 初始计费属性引用 URRGROUP |

### 6.4 CommandRule `governs` 关系

| 起点 | 关系 | 终点 |
|---|---|---|
| `CR-01` | `governs` | `CMD-UDG-ADD-URR` |
| `CR-02` | `governs` | `CMD-UNC-ADD-URR` |
| `CR-03` | `governs` | `CMD-UDG-ADD-URRGROUP` |
| `CR-03` | `governs` | `CMD-UNC-ADD-URRGROUP` |
| `CR-05` | `governs` | `CMD-UDG-ADD-PCCPOLICYGRP` |
| `CR-05` | `governs` | `CMD-UNC-ADD-PCCPOLICYGRP` |
| `CR-06` | `governs` | `CMD-UDG-ADD-RULE` |
| `CR-06` | `governs` | `CMD-UNC-ADD-RULE` |
| `CR-08` | `governs` | `CMD-UDG-ADD-RULEBINDING` |
| `CR-09` | `governs` | `CMD-UDG-SET-URRGRPBINDING` |
| `CR-10` | `governs` | `CMD-UDG-SET-REFRESHSRV` |
| `CR-12` | `governs` | `CMD-UDG-ADD-PROTBINDFLOWF` |
| `CR-15` | `governs` | `CMD-UNC-ADD-SELECTCCTBYCC` |
| `CR-16` | `governs` | `CMD-UNC-ADD-SELECTCHFGBYCC` |
| `CR-17` | `governs` | `CMD-UNC-SET-CHFINIT` |
| `CR-18` | `governs` | `CMD-UNC-SET-RGRESCTRL` |

---

## 7. ConfigTask 到命令图谱的承接

### 7.1 ConfigTask `invokes` MMLCommand

| 起点 | 关系 | 终点 |
|---|---|---|
| `T-EXEC-001` | `invokes` | `CMD-UDG-ADD-FILTER` |
| `T-EXEC-002` | `invokes` | `CMD-UDG-ADD-FILTER` |
| `T-EXEC-003` | `invokes` | `CMD-UDG-ADD-L7FILTER` |
| `T-EXEC-004` | `invokes` | `CMD-UDG-ADD-FLOWFILTER` |
| `T-EXEC-004` | `invokes` | `CMD-UDG-ADD-FLTBINDFLOWF` |
| `T-EXEC-004` | `invokes` | `CMD-UDG-ADD-PROTBINDFLOWF` |
| `T-EXEC-005` | `invokes` | `CMD-UDG-ADD-URR` |
| `T-EXEC-005` | `invokes` | `CMD-UDG-ADD-URRGROUP` |
| `T-EXEC-005` | `invokes` | `CMD-UDG-ADD-PCCPOLICYGRP` |
| `T-EXEC-008` | `invokes` | `CMD-UDG-ADD-RULE` |
| `T-EXEC-010` | `invokes` | `CMD-UDG-ADD-USERPROFILE` |
| `T-EXEC-010` | `invokes` | `CMD-UDG-ADD-RULEBINDING` |
| `T-EXEC-010` | `invokes` | `CMD-UDG-SET-URRGRPBINDING` |
| `T-EXEC-010` | `invokes` | `CMD-UDG-SET-REFRESHSRV` |
| `T-EXEC-005` | `invokes` | `CMD-UNC-ADD-URR` |
| `T-EXEC-005` | `invokes` | `CMD-UNC-ADD-URRGROUP` |
| `T-EXEC-005` | `invokes` | `CMD-UNC-ADD-PCCPOLICYGRP` |
| `T-EXEC-008` | `invokes` | `CMD-UNC-ADD-RULE` |
| `T-EXEC-010` | `invokes` | `CMD-UNC-ADD-USERPROFILE` |
| `T-EXEC-010` | `invokes` | `CMD-UNC-SET-URRGRPBINDING` |
| `T-EXEC-010` | `invokes` | `CMD-UNC-ADD-USRPROFGROUP` |
| `T-EXEC-010` | `invokes` | `CMD-UNC-ADD-UPBINDUPG` |
| `T-EXEC-010` | `invokes` | `CMD-UNC-ADD-APN` |
| `T-EXEC-010` | `invokes` | `CMD-UNC-ADD-APNUSRPROFG` |
| `T-EXEC-011` | `invokes` | `CMD-UNC-SET-CHARGECTRL` |
| `T-EXEC-012` | `invokes` | `CMD-UNC-ADD-HTTPLEGRP` |
| `T-EXEC-012` | `invokes` | `CMD-UNC-ADD-SBIAPLE` |
| `T-EXEC-012` | `invokes` | `CMD-UNC-ADD-TNFGRP` |
| `T-EXEC-012` | `invokes` | `CMD-UNC-ADD-SELECTCHFGBYCC` |
| `T-EXEC-013` | `invokes` | `CMD-UNC-ADD-CCT` |
| `T-EXEC-013` | `invokes` | `CMD-UNC-ADD-SELECTCCTBYCC` |
| `T-EXEC-013` | `invokes` | `CMD-UNC-SET-CHFINIT` |
| `T-EXEC-013` | `invokes` | `CMD-UNC-ADD-PDUTRIGGER` |
| `T-EXEC-013` | `invokes` | `CMD-UNC-ADD-RGTRIGGER` |
| `T-EXEC-013` | `invokes` | `CMD-UNC-SET-RGRESCTRL` |
| `T-EXEC-013` | `invokes` | `CMD-UNC-SET-CTXSTARTRATING` |

### 7.2 TaskCommandOrderEdge

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `condition_ref` | `propagated_context` | `supported_by` |
|---|---|---|---|---|---|---|---|
| `TCE-001` | `T-EXEC-005` | `CMD-UDG-ADD-URR` | `CMD-UDG-ADD-URRGROUP` | `precedes` | - | URRNAME / URRID / RG/SID | `GWFD-020301-内容计费.md`, `部署UPF_28493406.md` |
| `TCE-002` | `T-EXEC-005` | `CMD-UDG-ADD-URRGROUP` | `CMD-UDG-ADD-PCCPOLICYGRP` | `precedes` | - | URRGROUPNAME | `GWFD-020301-内容计费.md`, `部署UPF_28493406.md` |
| `TCE-003` | `T-EXEC-004` | `CMD-UDG-ADD-FLOWFILTER` | `CMD-UDG-ADD-FLTBINDFLOWF` | `precedes` | - | FLOWFILTERNAME | `GWFD-020301-内容计费.md`, `部署UPF_28493406.md` |
| `TCE-004` | `T-EXEC-004` | `CMD-UDG-ADD-FLOWFILTER` | `CMD-UDG-ADD-PROTBINDFLOWF` | `precedes` | `DP-03` | FLOWFILTERNAME | `GWFD-020301-内容计费.md`, `部署UPF_28493406.md` |
| `TCE-005` | `T-EXEC-008` | `CMD-UDG-ADD-RULE` | `CMD-UDG-ADD-USERPROFILE` | `produces_input_for` | - | RULENAME | `部署UPF_28493406.md` |
| `TCE-006` | `T-EXEC-010` | `CMD-UDG-ADD-USERPROFILE` | `CMD-UDG-ADD-RULEBINDING` | `precedes` | - | USERPROFILENAME | `GWFD-020301-内容计费.md` |
| `TCE-007` | `T-EXEC-010` | `CMD-UDG-ADD-RULEBINDING` | `CMD-UDG-SET-URRGRPBINDING` | `precedes` | - | USERPROFILENAME / RULENAME | `GWFD-020301-内容计费.md` |
| `TCE-008` | `T-EXEC-010` | `CMD-UDG-SET-URRGRPBINDING` | `CMD-UDG-SET-REFRESHSRV` | `must_be_last` | - | Filter / UserProfile 已完成 | `GWFD-020301-内容计费.md`, `GWFD-010171-离线计费.md` |
| `TCE-009` | `T-EXEC-005` | `CMD-UNC-ADD-URR` | `CMD-UNC-ADD-URRGROUP` | `precedes` | - | URRNAME / RG/SID | `WSFD-109002-内容计费.md` |
| `TCE-010` | `T-EXEC-005` | `CMD-UNC-ADD-URRGROUP` | `CMD-UNC-ADD-PCCPOLICYGRP` | `precedes` | - | URRGROUPNAME | `WSFD-109002-内容计费.md` |
| `TCE-011` | `T-EXEC-010` | `CMD-UNC-ADD-USERPROFILE` | `CMD-UNC-SET-URRGRPBINDING` | `precedes` | - | USERPROFILENAME | `WSFD-109002-内容计费.md` |
| `TCE-012` | `T-EXEC-010` | `CMD-UNC-ADD-USRPROFGROUP` | `CMD-UNC-ADD-UPBINDUPG` | `precedes` | - | USERPROFGNAME | `WSFD-109002-内容计费.md` |
| `TCE-013` | `T-EXEC-010` | `CMD-UNC-ADD-APN` | `CMD-UNC-ADD-APNUSRPROFG` | `precedes` | - | APN | `WSFD-109002-内容计费.md` |
| `TCE-014` | `T-EXEC-012` | `CMD-UNC-ADD-HTTPLEGRP` | `CMD-UNC-ADD-SBIAPLE` | `precedes` | `DP-00` | HTTPLEGRPIDX | `WSFD-011206-融合计费.md` |
| `TCE-015` | `T-EXEC-012` | `CMD-UNC-ADD-TNFGRP` | `CMD-UNC-ADD-SELECTCHFGBYCC` | `precedes` | `DP-00` | TNFGRPNAME | `WSFD-011206-融合计费.md` |
| `TCE-016` | `T-EXEC-013` | `CMD-UNC-ADD-CCT` | `CMD-UNC-ADD-SELECTCCTBYCC` | `precedes` | `DP-01` | CCTMPLTNAME | `WSFD-011206-融合计费.md` |
| `TCE-017` | `T-EXEC-013` | `CMD-UNC-ADD-CCT` | `CMD-UNC-SET-CHFINIT` | `precedes` | `DP-01` | CCTMPLTNAME | `WSFD-011206-融合计费.md` |
| `TCE-018` | `T-EXEC-013` | `CMD-UNC-SET-CHFINIT` | `CMD-UNC-ADD-PDUTRIGGER` | `precedes` | `DP-01` | CCT 激活交互方式 | `WSFD-011206-融合计费.md` |
| `TCE-019` | `T-EXEC-013` | `CMD-UNC-ADD-PDUTRIGGER` | `CMD-UNC-ADD-RGTRIGGER` | `precedes` | `DP-01` | Trigger 模板 | `WSFD-011206-融合计费.md` |
| `TCE-020` | `T-EXEC-013` | `CMD-UNC-ADD-RGTRIGGER` | `CMD-UNC-SET-RGRESCTRL` | `precedes` | `DP-01` | RG trigger 行为 | `WSFD-011206-融合计费.md` |
| `TCE-021` | `T-EXEC-013` | `CMD-UNC-SET-RGRESCTRL` | `CMD-UNC-SET-CTXSTARTRATING` | `precedes` | `DP-01` | RG 老化与初始请求策略 | `WSFD-011206-融合计费.md` |

---

## 8. 当前边界结论

基于新 schema，计费场景的命令图谱边界明确为：

1. **保留**
   - `MMLCommand`
   - `CommandParameter`
   - `ConfigObject`
   - `CommandRule`
   - `TaskCommandOrderEdge`

2. **承接方式**
   - 通过 `ConfigTask invokes MMLCommand` 接住特性图谱下沉的 task
   - 通过 `CommandParameter references ConfigObject` 承接对象引用
   - 通过 `ConfigObject` 之间的边承接对象依赖、包含和绑定关系

3. **不再放回业务或特性图谱**
   - `ConfigObject`
   - `CommandParameter`
   - `MMLCommand`
   - 命令级删除、唯一性、刷新、引用约束

---

## 9. 对前两份文档的反向补强建议

命令图谱收口后，前两份文档还需要做两类回补：

1. **回补业务图谱**
   - `BusinessRule` 中明显属于命令级的约束，后续应逐步下沉到 `CommandRule`
   - `ConfigurationSolution -> uses_task` 需要和本文件的 `TaskCommandOrderEdge` 一起核对

2. **回补特性图谱**
   - `ConfigTask` 的目标语义应和本文件的 `ConfigObject` 再做一次对齐
   - `FeatureRule` 与 `CommandRule` 之间还可继续拆层，减少“跨侧一致性”规则的重复承载

