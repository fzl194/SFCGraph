# 带宽控制场景命令图谱（新 Schema，v0.1）

> 范围：仅描述带宽控制场景（业务感知套餐2）在新三层图谱 schema 下的命令图谱部分。
> 约束：对象、关系、属性命名严格服从 `三层图谱Schema-最终版-v0.1.md` §11 命令图谱 Schema。
> 来源：基于 `cross-feature-analysis.md`（附录B MML命令交叉参考、附录C配置对象复用矩阵、§H.4配置冲突风险）。
> 说明：命令图谱管"命令、参数、配置对象、命令级规则是什么"，不涉及业务编排。

---

## 0. 适用定义与来源

### 0.1 根定义

- `三层图谱本体标准定义.md`
- `三层图谱Schema-最终版-v0.1.md`

### 0.2 直接来源

- `cross-feature-analysis.md`（附录B.1 UDG命令、附录B.2 UNC命令、附录C配置对象复用矩阵、§H.4配置冲突风险矩阵）
- `feature-knowledge/*.md`（24个特性详情，含命令参数）
- `topic-knowledge/Batch-19.md`（BWM命令配置实例）

### 0.3 本文件保留对象

| 对象 | 中文名 | 实例数 |
| --- | --- | --- |
| `MMLCommand` | MML 命令 | ~55（UDG 30 + UNC 25） |
| `ConfigObject` | 配置对象 | ~25 |
| `CommandParameter` | 命令参数 | 核心差异化参数（见§3） |
| `CommandRule` | 命令规则 | 5 |

---

## 1. MMLCommand（按产品分组）

### 1.1 UDG 侧核心命令（30个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- |
| `CMD-UDG-001` | `SET LICENSESWITCH` | `SET` | `LICENSESWITCH` | License 开关，全部16个UDG特性前置 | `active` | `EV-CFA-§2.3` |
| `CMD-UDG-002` | `SET BANDWIDTHMNG` | `SET` | `BANDWIDTHMNG` | BWM 全局使能开关 | `active` | `EV-FK-110311` |
| `CMD-UDG-003` | `ADD BWMSERVICE` | `ADD` | `BWMSERVICE` | BWM 服务实例定义（业务名/协议） | `active` | `EV-FK-110311`, `EV-TK-19` |
| `CMD-UDG-004` | `ADD BWMCONTROLLER` | `ADD` | `BWMCONTROLLER` | BWM 控制器（CTRLTYPE=CAR/SHAPING + 限速参数） | `active` | `EV-FK-110311`, `EV-CFA-附录F` |
| `CMD-UDG-005` | `ADD BWMUSERGROUP` | `ADD` | `BWMUSERGROUP` | BWM 用户组（SPECIFIC_GROUP/GLOBAL） | `active` | `EV-FK-110311` |
| `CMD-UDG-006` | `ADD BWMRULE` | `ADD` | `BWMRULE` | BWM 规则（BWMRULETYPE + 控制器引用） | `active` | `EV-FK-110311` |
| `CMD-UDG-007` | `ADD BWMRULEGLOBAL` | `ADD` | `BWMRULEGLOBAL` | BWM 全局规则（整机级业务带宽） | `active` | `EV-FK-110311` |
| `CMD-UDG-008` | `ADD BCSRVLEVELPLY` | `ADD` | `BCSRVLEVELPLY` | 业务服务等级策略（智能Shaping的SHAPRATE） | `active` | `EV-FK-110313` |
| `CMD-UDG-009` | `ADD CATEGORYPROP` | `ADD` | `CATEGORYPROP` | 业务分类属性（SA分类） | `active` | `EV-FK-110101`, `EV-FK-110311` |
| `CMD-UDG-010` | `ADD APNBINDBWMUSRG` | `ADD` | `APNBINDBWMUSRG` | APN 绑定 BWM 用户组 | `active` | `EV-FK-110311` |
| `CMD-UDG-011` | `ADD SNSSAI` | `ADD` | `SNSSAI` | 网络切片绑定 | `active` | `EV-FK-110311` |
| `CMD-UDG-012` | `ADD RULE` | `ADD` | `RULE` | PCC 规则定义（RULENAME/POLICYTYPE/PRIORITY） | `active` | `EV-CFA-§2.1` |
| `CMD-UDG-013` | `ADD FLOWFILTER` | `ADD` | `FLOWFILTER` | 流过滤器 | `active` | `EV-CFA-§2.5` |
| `CMD-UDG-014` | `ADD FILTER` | `ADD` | `FILTER` | L3/L4 过滤器 | `active` | `EV-FK-110101` |
| `CMD-UDG-015` | `ADD L7FILTER` | `ADD` | `L7FILTER` | L7 过滤器（UDG独有） | `active` | `EV-FK-110101` |
| `CMD-UDG-016` | `ADD FLTBINDFLOWF` | `ADD` | `FLTBINDFLOWF` | 过滤器绑定到 FlowFilter | `active` | `EV-FK-020351` |
| `CMD-UDG-017` | `ADD USERPROFILE` | `ADD` | `USERPROFILE` | 用户模板（UPTYPE=PCC） | `active` | `EV-CFA-§2.5` |
| `CMD-UDG-018` | `ADD RULEBINDING` | `ADD` | `RULEBINDING` | 规则绑定到 UserProfile | `active` | `EV-CFA-§2.5` |
| `CMD-UDG-019` | `ADD PCCPOLICYGRP` | `ADD` | `PCCPOLICYGRP` | PCC 策略组 | `active` | `EV-FK-020351` |
| `CMD-UDG-020` | `ADD QOSPROP` | `ADD` | `QOSPROP` | QoS 属性（5QI/QCI/MBR/GBR/ARP） | `active` | `EV-FK-020358`, `EV-FK-110302` |
| `CMD-UDG-021` | `ADD URR` | `ADD` | `URR` | 使用量上报规则（USAGERPTMODE/REPORTINGTHRESHOLD） | `active` | `EV-FK-020353`, `EV-CFA-§5.2` |
| `CMD-UDG-022` | `ADD URRGROUP` | `ADD` | `URRGROUP` | URR 组（UPURRNAME1/2/3） | `active` | `EV-FK-020353` |
| `CMD-UDG-023` | `ADD ADCPARA` | `ADD` | `ADCPARA` | ADC 检测参数 | `active` | `EV-FK-020357` |
| `CMD-UDG-024` | `SET SRVCOMMONPARA` | `SET` | `SRVCOMMONPARA` | SA 公共参数 | `active` | `EV-FK-110101` |
| `CMD-UDG-025` | `SET REFRESHSRV` | `SET` | `REFRESHSRV` | 策略刷新生效（约60秒） | `active` | `EV-CFA-§5.5` |
| `CMD-UDG-026` | `LOD SIGNATUREDB` | `LOD` | `SIGNATUREDB` | 加载 SA 特征库 | `active` | `EV-FK-110101`, `EV-FK-111600` |
| `CMD-UDG-027` | `LOD PARSERDB` | `LOD` | `PARSERDB` | 加载 SA 解析库 | `active` | `EV-FK-110101` |
| `CMD-UDG-028` | `SET APNOSLELBWMSW` | `SET` | `APNOSLELBWMSW` | 终端 OS BWM 差异化开关 | `active` | `EV-FK-110301` |
| `CMD-UDG-029` | `SET CUINCONSPOLICY` | `SET` | `CUINCONSPOLICY` | 收敛策略 | `active` | `EV-FK-110101` |
| `CMD-UDG-030` | `ADD USRPROFGROUP` | `ADD` | `USRPROFGROUP` | 用户模板组 | `active` | `EV-CFA-§2.5` |

### 1.2 UNC 侧核心命令（25个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- |
| `CMD-UNC-001` | `SET LICENSESWITCH` | `SET` | `LICENSESWITCH` | License 开关，全部8个UNC特性前置 | `active` | `EV-CFA-§2.3` |
| `CMD-UNC-002` | `SET PCCFUNC` | `SET` | `PCCFUNC` | PCC 功能设置（MKPARSEFORMAT等） | `active` | `EV-FK-109101`, `EV-FK-109104` |
| `CMD-UNC-003` | `SET APNPCCFUNC` | `SET` | `APNPCCFUNC` | APN 级 PCC 开关 | `active` | `EV-FK-109101` |
| `CMD-UNC-004` | `ADD PCRF` | `ADD` | `PCRF` | PCRF 定义 | `active` | `EV-FK-109101` |
| `CMD-UNC-005` | `ADD PCRFGROUP` | `ADD` | `PCRFGROUP` | PCRF 组 | `active` | `EV-FK-109101` |
| `CMD-UNC-006` | `ADD PCRFBINDGRP` | `ADD` | `PCRFBINDGRP` | PCRF 组绑定 | `active` | `EV-FK-109101` |
| `CMD-UNC-007` | `SET DFTGLBPCRFGRP` | `SET` | `DFTGLBPCRFGRP` | 缺省 PCRF 组 | `active` | `EV-FK-109101` |
| `CMD-UNC-008` | `SET PCCFAILACTION` | `SET` | `PCCFAILACTION` | PCC 故障处理 | `active` | `EV-FK-109101` |
| `CMD-UNC-009` | `SET PCCTIMER` | `SET` | `PCCTIMER` | PCC 定时器 | `active` | `EV-FK-109101` |
| `CMD-UNC-010` | `ADD PCCTEMPLATE` | `ADD` | `PCCTEMPLATE` | PCC 模板 | `active` | `EV-FK-109101` |
| `CMD-UNC-011` | `ADD RULE` | `ADD` | `RULE` | 规则定义（POLICYTYPE=BWM/PCC/QOS/ADC） | `active` | `EV-FK-211005`, `EV-CFA-§5.1` |
| `CMD-UNC-012` | `ADD USERPROFILE` | `ADD` | `USERPROFILE` | 用户模板 | `active` | `EV-FK-211005` |
| `CMD-UNC-013` | `ADD RULEBINDING` | `ADD` | `RULEBINDING` | 规则绑定 | `active` | `EV-FK-211005` |
| `CMD-UNC-014` | `ADD USRPROFGROUP` | `ADD` | `USRPROFGROUP` | 用户模板组 | `active` | `EV-FK-211005` |
| `CMD-UNC-015` | `ADD UPBINDUPG` | `ADD` | `UPBINDUPG` | 模板绑定到组 | `active` | `EV-FK-211005` |
| `CMD-UNC-016` | `ADD APNUSRPROFG` | `ADD` | `APNUSRPROFG` | APN 绑定用户模板组 | `active` | `EV-FK-211005` |
| `CMD-UNC-017` | `ADD PCCPOLICYGRP` | `ADD` | `PCCPOLICYGRP` | PCC 策略组 | `active` | `EV-FK-109104`, `EV-FK-211009` |
| `CMD-UNC-018` | `ADD URR` | `ADD` | `URR` | URR 规则 | `active` | `EV-FK-109107`, `EV-FK-211009` |
| `CMD-UNC-019` | `ADD URRGROUP` | `ADD` | `URRGROUP` | URR 组 | `active` | `EV-FK-211009` |
| `CMD-UNC-020` | `ADD QOSPROP` | `ADD` | `QOSPROP` | QoS 属性 | `active` | `EV-FK-109107` |
| `CMD-UNC-021` | `ADD FLOWFILTER` | `ADD` | `FLOWFILTER` | 流过滤器 | `active` | `EV-FK-109102` |
| `CMD-UNC-022` | `ADD ADCPARA` | `ADD` | `ADCPARA` | ADC 参数 | `active` | `EV-FK-109102` |
| `CMD-UNC-023` | `SET APNIDLETIME` | `SET` | `APNIDLETIME` | 专有 QoS Flow 空闲定时器 | `active` | `EV-FK-109107` |
| `CMD-UNC-024` | `ADD APNDEACTQFPLCY` | `ADD` | `APNDEACTQFPLCY` | 去活 QoS Flow 策略 | `active` | `EV-FK-109107` |
| `CMD-UNC-025` | `SET APNREPORTATTR` | `SET` | `APNREPORTATTR` | APN 拥塞上报属性（小区负荷） | `active` | `EV-FK-211101` |

---

## 2. ConfigObject（配置对象）

来源：`cross-feature-analysis.md` 附录C 配置对象复用矩阵。

### 2.1 BWM 独有对象（8个）

| `object_id` | `object_name` | `identifier_parameters` | `object_kind` | `description` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- |
| `OBJ-BWMSERVICE` | `BWMSERVICE` | `BWMSERVICENAME` | `entity` | BWM 业务实例 | `EV-FK-110311` |
| `OBJ-BWMCONTROLLER` | `BWMCONTROLLER` | `BWMCNAME` | `entity` | BWM 控制器（CAR/SHAPING参数） | `EV-FK-110311` |
| `OBJ-BWMUSERGROUP` | `BWMUSERGROUP` | `BWMUSERGROUPNAME` | `composite` | BWM 用户组 | `EV-FK-110311` |
| `OBJ-BWMRULE` | `BWMRULE` | `BWMRULETYPE, BWMSERVICENAME` | `entity` | BWM 规则 | `EV-FK-110311` |
| `OBJ-BWMRULEGLOBAL` | `BWMRULEGLOBAL` | `BWMSERVICENAME` | `entity` | BWM 全局规则 | `EV-FK-110311` |
| `OBJ-BCSRVLEVELPLY` | `BCSRVLEVELPLY` | `BWMCNAME, SERVICELEVEL` | `entity` | 业务服务等级策略 | `EV-FK-110313` |
| `OBJ-CATEGORYPROP` | `CATEGORYPROP` | `CATEGORYPROPNAME` | `entity` | 业务分类属性 | `EV-FK-110101` |
| `OBJ-APNBINDBWMUSRG` | `APNBINDBWMUSRG` | `APNNAME, BWMUSERGROUPNAME` | `binding` | APN 绑定 BWM 用户组 | `EV-FK-110311` |

### 2.2 PCC 通用对象（7个）

| `object_id` | `object_name` | `identifier_parameters` | `object_kind` | `description` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- |
| `OBJ-RULE` | `RULE` | `RULENAME, POLICYTYPE` | `entity` | PCC 规则 | `EV-CFA-§2.1` |
| `OBJ-USERPROFILE` | `USERPROFILE` | `UPNAME` | `composite` | 用户模板 | `EV-CFA-§2.5` |
| `OBJ-RULEBINDING` | `RULEBINDING` | `UPNAME, RULENAME` | `binding` | 规则绑定 | `EV-CFA-§2.5` |
| `OBJ-USRPROFGROUP` | `USRPROFGROUP` | `UPGNAME` | `composite` | 用户模板组 | `EV-CFA-§2.5` |
| `OBJ-UPBINDUPG` | `UPBINDUPG` | `UPGNAME, UPNAME` | `binding` | 模板绑定到组 | `EV-CFA-§2.5` |
| `OBJ-APNUSRPROFG` | `APNUSRPROFG` | `APNNAME, UPGNAME` | `binding` | APN 绑定模板组 | `EV-CFA-§2.5` |
| `OBJ-PCCPOLICYGRP` | `PCCPOLICYGRP` | `PCCPOLICYGRPNAME` | `composite` | PCC 策略组 | `EV-FK-020351` |

### 2.3 过滤对象（5个）

| `object_id` | `object_name` | `identifier_parameters` | `object_kind` | `description` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- |
| `OBJ-FLOWFILTER` | `FLOWFILTER` | `FLOWFILTERNAME` | `composite` | 流过滤器 | `EV-CFA-§2.5` |
| `OBJ-FLOWFILTERGRP` | `FLOWFILTERGRP` | `FILTERGRPNAME` | `composite` | 流过滤组（OR关系） | `EV-TK-18` |
| `OBJ-FILTER` | `FILTER` | `FILTERNAME` | `entity` | L3/L4 过滤器 | `EV-FK-110101` |
| `OBJ-L7FILTER` | `L7FILTER` | `L7FILTERNAME` | `entity` | L7 过滤器 | `EV-FK-110101` |
| `OBJ-FLTBINDFLOWF` | `FLTBINDFLOWF` | `FLOWFILTERNAME, FILTERNAME` | `binding` | 过滤器绑定 | `EV-FK-020351` |

### 2.4 QoS/FUP 对象（3个）

| `object_id` | `object_name` | `identifier_parameters` | `object_kind` | `description` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- |
| `OBJ-QOSPROP` | `QOSPROP` | `QOSPROPNAME, QOSTYPE` | `entity` | QoS 属性 | `EV-FK-020358` |
| `OBJ-URR` | `URR` | `URRID` | `entity` | 使用量上报规则 | `EV-FK-020353` |
| `OBJ-URRGROUP` | `URRGROUP` | `URRGROUPNAME` | `composite` | URR 组 | `EV-FK-020353` |

### 2.5 ADC 对象（1个）

| `object_id` | `object_name` | `identifier_parameters` | `object_kind` | `description` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- |
| `OBJ-ADCPARA` | `ADCPARA` | `ADCPARANAME` | `entity` | ADC 检测参数 | `EV-FK-020357` |

### 2.6 UNC 特有对象（2个）

| `object_id` | `object_name` | `identifier_parameters` | `object_kind` | `description` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- |
| `OBJ-PCRF` | `PCRF` | `PCRFID` | `entity` | PCRF 定义 | `EV-FK-109101` |
| `OBJ-APNDEACTQFPLCY` | `APNDEACTQFPLCY` | `APNNAME` | `entity` | 去活 QoS Flow 策略 | `EV-FK-109107` |

---

## 3. CommandParameter（核心差异化参数）

仅记录带宽控制场景的核心差异化参数，完整参数表见各特性知识文档。

### 3.1 ADD BWMCONTROLLER 核心参数

| `parameter_id` | `command_ref` | `parameter_name` | `data_type` | `required_mode` | `enum_values` | `description` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PARA-BWMC-CTRLTYPE` | `CMD-UDG-004` | `CTRLTYPE` | `enum` | `required` | `CAR, SHAPING` | 控制类型，决定参数集 | `EV-FK-110311`, `EV-CFA-附录F` |
| `PARA-BWMC-CIR` | `CMD-UDG-004` | `CIR` | `int` | `conditional_required` | - | 承诺信息速率（CAR模式必填） | `EV-FK-110311` |
| `PARA-BWMC-PIR` | `CMD-UDG-004` | `PIR` | `int` | `conditional_required` | - | 峰值信息速率（CAR模式必填） | `EV-FK-110311` |
| `PARA-BWMC-CBS` | `CMD-UDG-004` | `CBS` | `int` | `optional` | - | 承诺突发尺寸 | `EV-FK-110311` |
| `PARA-BWMC-PBS` | `CMD-UDG-004` | `PBS` | `int` | `optional` | - | 峰值突发尺寸 | `EV-FK-110311` |
| `PARA-BWMC-RATE` | `CMD-UDG-004` | `RATE` | `int` | `conditional_required` | - | 限速速率（SHAPING模式必填） | `EV-FK-110311` |
| `PARA-BWMC-QUEDEPTH` | `CMD-UDG-004` | `QUEDEPTH` | `int` | `conditional_required` | - | 队列深度（SHAPING模式必填） | `EV-FK-110311` |
| `PARA-BWMC-WORKMODE` | `CMD-UDG-004` | `WORKMODE` | `enum` | `optional` | `AUTO, MANUAL` | 工作模式（智能Shaping用） | `EV-FK-110313` |

### 3.2 ADD BWMRULE 核心参数

| `parameter_id` | `command_ref` | `parameter_name` | `data_type` | `required_mode` | `enum_values` | `description` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PARA-BWMR-TYPE` | `CMD-UDG-006` | `BWMRULETYPE` | `enum` | `required` | `SUBSCRIBER_SPECIFIC, GROUP_SPECIFIC, GLOBAL` | 规则层级类型 | `EV-FK-110311`, `EV-CFA-§3.2` |
| `PARA-BWMR-PRI` | `CMD-UDG-006` | `BWMRULEPRI` | `int` | `required` | - | 规则优先级（降速规则需最高） | `EV-FK-110311`, `EV-CTA-§7.4` |

### 3.3 ADD URR 核心参数

| `parameter_id` | `command_ref` | `parameter_name` | `data_type` | `required_mode` | `enum_values` | `description` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PARA-URR-ID` | `CMD-UDG-021` | `URRID` | `int` | `required` | - | URR ID（会话内唯一） | `EV-FK-020353` |
| `PARA-URR-MODE` | `CMD-UDG-021` | `USAGERPTMODE` | `enum` | `required` | `ONLINE, OFFLINE, MONITORINGKEY, QOS` | 上报模式（决定用途） | `EV-FK-020353`, `EV-CFA-§5.2` |
| `PARA-URR-THRESH` | `CMD-UDG-021` | `REPORTINGTHRESHOLD` | `int` | `optional` | - | 上报阈值（FUP配额） | `EV-FK-020353` |

### 3.4 ADD RULE 核心参数

| `parameter_id` | `command_ref` | `parameter_name` | `data_type` | `required_mode` | `enum_values` | `description` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PARA-RULE-NAME` | `CMD-UDG-012`/`CMD-UNC-011` | `RULENAME` | `string` | `required` | - | 规则名（三网元一致） | `EV-CFA-§5.7` |
| `PARA-RULE-PTYPE` | `CMD-UNC-011` | `POLICYTYPE` | `enum` | `required` | `BWM, PCC, QOS, ADC, CHARGING` | 策略类型（UNC侧关键标识） | `EV-CFA-§5.1`, `EV-CFA-§5.6` |
| `PARA-RULE-PRI` | `CMD-UDG-012`/`CMD-UNC-011` | `PRIORITY` | `int` | `required` | - | 优先级 | `EV-CFA-§5.1` |

### 3.5 ADD QOSPROP 核心参数

| `parameter_id` | `command_ref` | `parameter_name` | `data_type` | `required_mode` | `enum_values` | `description` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PARA-QP-TYPE` | `CMD-UDG-020`/`CMD-UNC-020` | `QOSTYPE` | `enum` | `required` | `QOS_FLOW_PARA, QOS_BEARER_PARA` | QoS类型（5G/4G区分） | `EV-FK-020358`, `EV-FK-109107` |
| `PARA-QP-FQI` | `CMD-UDG-020`/`CMD-UNC-020` | `FQI` | `int` | `conditional_required` | - | QoS Flow Identifier（5G） | `EV-FK-020358` |
| `PARA-QP-QCI` | `CMD-UDG-020`/`CMD-UNC-020` | `QCIVALUE` | `int` | `conditional_required` | - | QCI 值（2/3/4G） | `EV-FK-020358` |
| `PARA-QP-GBRUL` | `CMD-UDG-020`/`CMD-UNC-020` | `GBRUL` | `int` | `optional` | - | 保证比特率（上行） | `EV-FK-020358` |
| `PARA-QP-GBRDL` | `CMD-UDG-020`/`CMD-UNC-020` | `GBRDL` | `int` | `optional` | - | 保证比特率（下行） | `EV-FK-020358` |

---

## 4. ConfigObject 间关系边

来源：Schema §11.7 + `cross-feature-analysis.md` 附录C。

| 起点 | 关系 | 终点 | 说明 | `source_evidence_ids` |
| --- | --- | --- | --- | --- |
| `OBJ-BWMUSERGROUP` | `contains` | `OBJ-BWMRULE` | BWM用户组包含规则 | `EV-FK-110311` |
| `OBJ-PCCPOLICYGRP` | `contains` | `OBJ-URRGROUP` | PCC策略组包含URR组（FUP场景） | `EV-FK-020353` |
| `OBJ-RULE` | `contains` | `OBJ-FLOWFILTER` | 规则包含流过滤器 | `EV-CFA-§2.5` |
| `OBJ-USERPROFILE` | `contains` | `OBJ-RULE` | 用户模板包含规则（通过RULEBINDING） | `EV-CFA-§2.5` |
| `OBJ-USRPROFGROUP` | `contains` | `OBJ-USERPROFILE` | 用户模板组包含模板（通过UPBINDUPG） | `EV-CFA-§2.5` |
| `OBJ-FLOWFILTER` | `contains` | `OBJ-FILTER` | 流过滤器包含L3/L4过滤器（通过FLTBINDFLOWF） | `EV-FK-110101` |
| `OBJ-FLOWFILTER` | `contains` | `OBJ-L7FILTER` | 流过滤器包含L7过滤器（通过FLTBINDFLOWF） | `EV-FK-110101` |
| `OBJ-URRGROUP` | `composed_by` | `OBJ-URR` | URR组由URR组合（UPURRNAME1/2/3） | `EV-FK-020353` |
| `OBJ-BWMRULE` | `refers_to` | `OBJ-BWMCONTROLLER` | BWM规则引用控制器（UPBWMCTRLNAME1） | `EV-FK-110311` |
| `OBJ-BWMRULE` | `refers_to` | `OBJ-BWMSERVICE` | BWM规则引用业务 | `EV-FK-110311` |
| `OBJ-RULE(ADC)` | `depends_on` | `OBJ-ADCPARA` | ADC规则依赖ADC参数 | `EV-FK-020357` |
| `OBJ-RULE(QOS)` | `refers_to` | `OBJ-QOSPROP` | QOS规则引用QoS属性 | `EV-FK-020358` |

---

## 5. CommandRule

5 条命令级规则，来源：`cross-feature-analysis.md` §H.4 配置冲突风险矩阵。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `scope_type` | `scope_ref` | `rule_logic` | `violation_effect` | `severity` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `CR-BW-01` | RULENAME 跨 POLICYTYPE 不冲突 | `object_reference_rule` | `explicit` | `restriction` | `object` | `OBJ-RULE` | PCC类型与QOS类型的 RULENAME 不能相同；BWM与CHARGING可同名 | 规则创建冲突或匹配混乱 | `critical` | `EV-CFA-§5.1`, `EV-CFA-§H.4` |
| `CR-BW-02` | URR ID 会话内唯一 | `semantic_rule` | `explicit` | `restriction` | `object` | `OBJ-URR` | 同一会话内 URR ID 不能重复（会话FUP与业务FUP需分段，如1-99/100+） | URR分配冲突，流量统计错误 | `critical` | `EV-CFA-§H.4` |
| `CR-BW-03` | CAR与Shaping不可同对象叠加 | `parameter_mutex` | `explicit` | `restriction` | `object` | `OBJ-BWMRULE` | 同一业务流不能同时做 CAR 和 Shaping | 控制逻辑冲突 | `warning` | `EV-CFA-§H.4`, `EV-CFA-附录F` |
| `CR-BW-04` | REFRESHSRV 后60秒生效 | `runtime_check_rule` | `explicit` | `ops` | `command` | `CMD-UDG-025` | SET REFRESHSRV 后约60秒（PROTBINDFLOWF定时器）策略才完全下发 | 验证时策略尚未生效，误判配置失败 | `info` | `EV-CFA-§5.5` |
| `CR-BW-05` | BWMCONTROLLER.CTRLTYPE 决定参数集 | `parameter_dependency` | `explicit` | `config` | `parameter` | `PARA-BWMC-CTRLTYPE` | CTRLTYPE=CAR 用 CIR/PIR/CBS/PBS；CTRLTYPE=SHAPING 用 RATE/QUEDEPTH | 参数缺失或冗余，配置失败 | `critical` | `EV-FK-110311`, `EV-CFA-附录F` |

---

## 6. 命令图谱关系边汇总

| 起点 | 关系 | 终点 | 数量 |
| --- | --- | --- | --- |
| `MMLCommand` | `has_parameter` | `CommandParameter` | 核心参数见§3 |
| `MMLCommand` | `operates_on` | `ConfigObject` | 见§1命令对应对象 |
| `CommandParameter` | `references` | `ConfigObject` | 见§3 |
| `ConfigObject` | `contains/refers_to/depends_on/...` | `ConfigObject` | 见§4 |
| `CommandRule` | `governs` | `MMLCommand/CommandParameter/ConfigObject` | 见§5 |
