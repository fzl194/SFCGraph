# 带宽控制场景三层图谱 · 第4层：命令图谱

> **文件定位**：`three-layer-graph/04-command-graph.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §11 命令图谱
> **作用**：实例化55个MMLCommand + 25个ConfigObject + 5个CommandRule + ConfigObject间关系边
> **数据来源**：`feature-knowledge/cross-feature-analysis.md`（附录B MML命令交叉参考、附录C 配置对象复用矩阵）

---

## 0. 命令图谱总览

### 0.1 MMLCommand 按产品分布

| 产品 | 命令数 | 说明 |
|------|-------|------|
| UDG | 30 | 用户面执行命令：BWM三级控制体系 + SA特征库 + PCC执行 + FUP/ADC/Shaping |
| UNC | 25 | 控制面策略命令：PCRF管理 + 规则/模板绑定链 + FUP/ADC/QoS策略 |
| **合计** | **55** | — |

### 0.2 ConfigObject 按功能分布

| 功能域 | 对象数 | 关键对象 |
|-------|-------|---------|
| BWM独有 | 8 | BWMSERVICE, BWMCONTROLLER, BWMUSERGROUP, BWMRULE, BWMRULEGLOBAL, BCSRVLEVELPLY, CATEGORYPROP, APNBINDBWMUSRG |
| PCC通用规则与用户模板 | 7 | RULE, USERPROFILE, RULEBINDING, USRPROFGROUP, UPBINDUPG, APNUSRPROFG, PCCPOLICYGRP |
| 流过滤 | 5 | FLOWFILTER, FLOWFILTERGRP, FILTER, L7FILTER, FLTBINDFLOWF |
| QoS/FUP | 3 | QOSPROP, URR, URRGROUP |
| ADC | 1 | ADCPARA |
| UNC特有 | 5 | PCRF, PCRFGROUP, PCRFBINDGRP, PCCTEMPLATE, APNDEACTQFPLCY |
| **合计** | **29** | — |

---

## 1. MMLCommand 实例化

### 1.1 基础对象与系统配置（UDG，6个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-UDG-001` | `SET LICENSESWITCH` | License开关，全部带宽控制特性的前置门控 | UDG | LICITEM, SWITCH | EV-FK-*, EV-CFA |
| `CMD-UDG-002` | `SET BANDWIDTHMNG` | BWM全局使能开关 | UDG | SWITCH(ENABLE/DISABLE) | EV-FK-110311 |
| `CMD-UDG-003` | `SET REFRESHSRV` | 策略刷新生效（约60秒PROTBINDFLOWF定时器后完全下发） | UDG | REFTYPE | EV-FK-020351, EV-FK-110101, EV-FK-110311 |
| `CMD-UDG-004` | `SET SRVCOMMONPARA` | SA公共参数配置 | UDG | PARANAME, PARAVALUE | EV-FK-110101 |
| `CMD-UDG-005` | `LOD SIGNATUREDB` | 加载SA特征库 | UDG | DBNAME, FILENAME | EV-FK-110101, EV-FK-111600 |
| `CMD-UDG-006` | `LOD PARSERDB` | 加载SA解析库 | UDG | DBNAME, FILENAME | EV-FK-110101 |

### 1.2 BWM三级控制体系（UDG，8个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-UDG-007` | `ADD BWMSERVICE` | BWM服务实例定义（匹配业务类型） | UDG | NAME, BWMSERVICETYPE, PROTOCOLNAME | EV-FK-110311 |
| `CMD-UDG-008` | `ADD BWMCONTROLLER` | BWM控制器（核心参数集，CAR/Shaping模式选择） | UDG | BWMCNAME, CTRLTYPE(CAR/SHAPING), CIR, PIR, CBS, PBS, RATE, QUEDEPTH, GREENACT, YELLOWACT, REDACT | EV-FK-110311 |
| `CMD-UDG-009` | `ADD BWMUSERGROUP` | BWM用户组（用户级/组级分组） | UDG | USERGROUPTYPE, USERGROUPNAME, USERGROUPPRI, USERLEVSRVTYPE | EV-FK-110311, EV-FK-110313 |
| `CMD-UDG-010` | `ADD BWMRULE` | BWM规则（绑定Service+Controller到UserGroup） | UDG | BWMRULETYPE(SUBSCRIBER_SPECIFIC/GROUP_SPECIFIC), BWMSERVICENAME, UPBWMCTRLNAME1, DNBWMCTRLNAME1, BWMRULEPRI | EV-FK-110311, EV-FK-020354, EV-FK-110313 |
| `CMD-UDG-011` | `ADD BWMRULEGLOBAL` | BWM全局规则（整机级业务带宽控制） | UDG | BWMSERVICENAME, UPBWMCTRLNAME1, DNBWMCTRLNAME1 | EV-FK-110311 |
| `CMD-UDG-012` | `ADD BCSRVLEVELPLY` | 业务服务等级策略（智能Shaping各等级整形速率） | UDG | BWMCNAME, SERVICELEVEL, SHAPRATE | EV-FK-110313 |
| `CMD-UDG-013` | `ADD CATEGORYPROP` | 业务分类属性定义 | UDG | CATEGORYPROPNAME, CATEGORYID | EV-FK-110101, EV-FK-110311 |
| `CMD-UDG-014` | `ADD APNBINDBWMUSRG` | APN绑定BWM用户组（按APN/DNN生效） | UDG | APNNAME, BWMUSERGROUPNAME | EV-FK-110311 |

### 1.3 流过滤与业务识别（UDG，5个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-UDG-015` | `ADD FLOWFILTER` | 流过滤器（组合过滤条件容器） | UDG | FLOWFILTERNAME | EV-FK-110101, EV-FK-020351 |
| `CMD-UDG-016` | `ADD FILTER` | L3/L4过滤器（5元组） | UDG | FILTERNAME, PROTTYPE, SRCIP, DSTIP | EV-FK-110101, EV-FK-020351 |
| `CMD-UDG-017` | `ADD L7FILTER` | L7过滤器（URL/UA等应用层字段） | UDG | L7FILTERNAME, DOMAINNAME, URL | EV-FK-110101 |
| `CMD-UDG-018` | `ADD FLTBINDFLOWF` | 过滤器绑定到FlowFilter | UDG | FLOWFILTERNAME, FILTERNAME | EV-FK-020351 |
| `CMD-UDG-019` | `ADD SNSSAI` | 网络切片S-NSSAI绑定 | UDG | SNSSAINAME, SD, SST | EV-FK-110311 |

### 1.4 PCC规则与策略（UDG，6个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-UDG-020` | `ADD RULE` | PCC规则定义 | UDG | RULENAME, POLICYTYPE, PRIORITY, FLOWFILTERNAME, POLICYNAME | EV-FK-110101, EV-FK-020351 |
| `CMD-UDG-021` | `ADD USERPROFILE` | 用户模板（UPTYPE=PCC） | UDG | UPNAME, UPTYPE | EV-FK-110101, EV-FK-020351 |
| `CMD-UDG-022` | `ADD RULEBINDING` | 规则绑定到UserProfile | UDG | UPNAME, RULENAME | EV-FK-110101, EV-FK-020351 |
| `CMD-UDG-023` | `ADD PCCPOLICYGRP` | PCC策略组（绑定URRGROUP） | UDG | PCCPOLICYGRPNAME, URRGROUPNAME | EV-FK-020351 |
| `CMD-UDG-024` | `ADD URR` | 使用量上报规则（FUP流量监控 / QoS事件上报） | UDG | URRID, USAGERPTMODE(ONLINE/MONITORINGKEY/QOS), MEASUREMENTMETHOD, VOLUMETHRESHOLD | EV-FK-020353, EV-FK-110312, EV-FK-020358 |
| `CMD-UDG-025` | `ADD URRGROUP` | URR组（UPURRNAME1/2/3） | UDG | URRGROUPNAME, UPURRNAME1, UPURRNAME2, UPURRNAME3, DFTURRGRPNAME | EV-FK-020353, EV-FK-110312 |

### 1.5 QoS属性与辅助命令（UDG，5个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-UDG-026` | `ADD QOSPROP` | QoS属性（5QI/MBR/GBR/ARP） | UDG | QOSPROPNAME, QOSTYPE(QOS_FLOW_PARA/QOS_BEARER_PARA), FQI, QCIVALUE, MBRUL, MBRDL, GBRUL, GBRDL, ARP | EV-FK-020358, EV-FK-110302 |
| `CMD-UDG-027` | `ADD ADCPARA` | ADC参数（L7应用检测） | UDG | ADCPARANAME, APPNAME, MATCHMODE | EV-FK-020357 |
| `CMD-UDG-028` | `SET APNOSLELBWMSW` | 终端OS BWM差异化开关 | UDG | APNNAME, OSTYPEBWMSW(ENABLE/DISABLE) | EV-FK-110301 |
| `CMD-UDG-029` | `SET APNIDLETIME` | APN级专有QoS Flow空闲定时器 | UDG | APNNAME, DEDQFIDLETIMER | EV-FK-020358 |
| `CMD-UDG-030` | `ADD APNDEACTQFPLCY` | APN级去活QoS Flow策略 | UDG | APNNAME, DEACTPOLICY | EV-FK-020358 |

### 1.6 UNC基础配置（7个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-UNC-001` | `SET LICENSESWITCH` | License开关，全部UNC带宽控制特性前置门控 | UNC | LICENSECODE, SWITCH | EV-FK-*, EV-CFA |
| `CMD-UNC-002` | `SET PCCFUNC` | PCC功能全局设置（含FUP解析格式等） | UNC | MKPARSEFORMAT, FUPSESSIONEXC | EV-FK-109101, EV-FK-109104 |
| `CMD-UNC-003` | `SET APNPCCFUNC` | APN级PCC功能开关 | UNC | APNNAME, PCCSWITCH | EV-FK-109101 |
| `CMD-UNC-004` | `SET PCCFAILACTION` | PCC故障处理策略 | UNC | FACTION(CONTINUE/REDIRECT) | EV-FK-109101 |
| `CMD-UNC-005` | `SET PCCTIMER` | PCC定时器参数 | UNC | TXTIMER, TXTIMERRETRY | EV-FK-109101 |
| `CMD-UNC-006` | `SET POLICYMODE` | 接口模式选择（Gx/N7） | UNC | POLICYMODE | EV-FK-109101 |
| `CMD-UNC-007` | `ADD PCCTEMPLATE` | PCC模板定义 | UNC | TEMPLATENAME, POLICYTYPE | EV-FK-109101 |

### 1.7 UNC PCRF管理（4个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-UNC-008` | `ADD PCRF` | PCRF定义（Gx对端或N7 PCF FQDN） | UNC | PCRFID, FQDN, IPADDR, FEATURELIST(UMCH) | EV-FK-109101 |
| `CMD-UNC-009` | `ADD PCRFGROUP` | PCRF组（主备/轮询/百分比/GROUPID+PRIORITY模式） | UNC | PCRFGROUPNAME, SELECTMODE | EV-FK-109101 |
| `CMD-UNC-010` | `ADD PCRFBINDGRP` | PCRF组绑定 | UNC | PCRFGROUPNAME, PCRFID, PRIORITY | EV-FK-109101 |
| `CMD-UNC-011` | `SET DFTGLBPCRFGRP` | 缺省全局PCRF组 | UNC | PCRFGROUPNAME | EV-FK-109101 |

### 1.8 UNC规则与用户模板绑定链（6个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-UNC-012` | `ADD RULE` | 规则定义（POLICYTYPE=BWM/PCC/QOS/ADC） | UNC | RULENAME, POLICYTYPE, PRIORITY, FLOWFILTERNAME, POLICYNAME | EV-FK-211005, EV-FK-109102, EV-FK-109107, EV-FK-211009 |
| `CMD-UNC-013` | `ADD USERPROFILE` | 用户模板 | UNC | UPNAME, UPTYPE | EV-FK-211005, EV-FK-109102, EV-FK-109107, EV-FK-211009 |
| `CMD-UNC-014` | `ADD RULEBINDING` | 规则绑定到UserProfile | UNC | UPNAME, RULENAME | EV-FK-211005, EV-FK-109102, EV-FK-109107, EV-FK-211009 |
| `CMD-UNC-015` | `ADD USRPROFGROUP` | 用户模板组 | UNC | UPGNAME | EV-FK-211005, EV-FK-109107, EV-FK-211009 |
| `CMD-UNC-016` | `ADD UPBINDUPG` | 模板绑定到组 | UNC | UPGNAME, UPNAME | EV-FK-211005, EV-FK-109107, EV-FK-211009 |
| `CMD-UNC-017` | `ADD APNUSRPROFG` | APN绑定用户模板组 | UNC | APNNAME, UPGNAME | EV-FK-211005, EV-FK-109107, EV-FK-211009 |

### 1.9 UNC PCC策略与URR（4个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-UNC-018` | `ADD PCCPOLICYGRP` | PCC策略组（含Monitoring-Key / FUP配置） | UNC | PCCPOLICYGRPNM, URRGROUPNAME, FUPSESSIONEXC | EV-FK-109104, EV-FK-109107, EV-FK-211009 |
| `CMD-UNC-019` | `ADD URR` | URR规则（SMF侧） | UNC | URRNAME, URRID, USAGERPTMODE, VOLUMETHRESHOLD | EV-FK-109107, EV-FK-211009 |
| `CMD-UNC-020` | `ADD URRGROUP` | URR组（SMF侧） | UNC | URRGROUPNAME, UPURRNAME1/2/3 | EV-FK-211009 |
| `CMD-UNC-021` | `ADD QOSPROP` | QoS属性（5G QoS Flow参数 / 2/3/4G承载参数） | UNC | QOSPROPNAME, QOSTYPE, FQI, QCIVALUE, MBRUL, MBRDL, GBRUL, GBRDL, ARP | EV-FK-109107 |

### 1.10 UNC辅助命令（4个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-UNC-022` | `ADD FLOWFILTER` | 流过滤器（ADC场景三网元一致） | UNC | FLOWFILTERNAME | EV-FK-109102 |
| `CMD-UNC-023` | `ADD ADCPARA` | ADC参数（控制面应用检测中继） | UNC | ADCPARANAME, APPNAME, MATCHMODE | EV-FK-109102 |
| `CMD-UNC-024` | `SET APNIDLETIME` | APN级专有QoS Flow空闲定时器 | UNC | APNNAME, DEDQFIDLETIMER | EV-FK-109107 |
| `CMD-UNC-025` | `SET APNREPORTATTR` | APN拥塞上报属性（小区负荷场景） | UNC | APNNAME, CONGESTIONRPT(ENABLE/DISABLE) | EV-FK-211101 |

---

## 2. ConfigObject 实例化（29个）

### 2.1 BWM独有对象（8个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | 关键属性 | 包含关系 |
|-------------|---------------|----------|---------------|----------|----------|
| `OBJ-BWMSERVICE` | BWMSERVICE | BWM三级控制 | entity | NAME, BWMSERVICETYPE, PROTOCOLNAME | referred_by BWMRULE |
| `OBJ-BWMCONTROLLER` | BWMCONTROLLER | BWM控制器 | entity | BWMCNAME, CTRLTYPE(CAR/SHAPING), CIR, PIR, CBS, PBS, RATE, QUEDEPTH, GREENACT, YELLOWACT, REDACT, COLORISAWARE, WORKMODE, SRVLEVELSPEC, USERFAIREN | referred_by BWMRULE; **contains** BCSRVLEVELPLY |
| `OBJ-BWMUSERGROUP` | BWMUSERGROUP | BWM用户组 | composite | USERGROUPTYPE, USERGROUPNAME, USERGROUPPRI | **contains** BWMRULE |
| `OBJ-BWMRULE` | BWMRULE | BWM规则 | entity | BWMRULETYPE, BWMSERVICENAME, UPBWMCTRLNAME1, DNBWMCTRLNAME1, BWMRULEPRI | belongs_to BWMUSERGROUP; refers_to BWMSERVICE, BWMCONTROLLER |
| `OBJ-BWMRULEGLOBAL` | BWMRULEGLOBAL | BWM全局规则 | entity | BWMSERVICENAME, UPBWMCTRLNAME1, DNBWMCTRLNAME1 | refers_to BWMSERVICE, BWMCONTROLLER |
| `OBJ-BCSRVLEVELPLY` | BCSRVLEVELPLY | 服务等级策略 | entity | BWMCNAME, SERVICELEVEL, SHAPRATE | belongs_to BWMCONTROLLER |
| `OBJ-CATEGORYPROP` | CATEGORYPROP | 业务分类 | entity | CATEGORYPROPNAME, CATEGORYID | — |
| `OBJ-APNBINDBWMUSRG` | APNBINDBWMUSRG | APN-BWM绑定 | binding | APNNAME, BWMUSERGROUPNAME | links APN to BWMUSERGROUP |

### 2.2 PCC通用规则与用户模板（7个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | 关键属性 | 包含关系 |
|-------------|---------------|----------|---------------|----------|----------|
| `OBJ-RULE` | RULE | PCC规则 | entity | RULENAME, POLICYTYPE(BWM/PCC/QOS/ADC), PRIORITY, FLOWFILTERNAME, POLICYNAME | **contains** FLOWFILTER; refers_to PCCPOLICYGRP |
| `OBJ-RULEBINDING` | RULEBINDING | 规则绑定 | binding | UPNAME, RULENAME | links USERPROFILE to RULE |
| `OBJ-USERPROFILE` | USERPROFILE | 用户模板 | composite | UPNAME, UPTYPE | **contains** RULE (via RULEBINDING) |
| `OBJ-USRPROFGROUP` | USRPROFGROUP | 用户模板组 | composite | UPGNAME | **contains** USERPROFILE (via UPBINDUPG) |
| `OBJ-UPBINDUPG` | UPBINDUPG | 模板绑定 | binding | UPGNAME, UPNAME | links USERPROFILE to USRPROFGROUP |
| `OBJ-APNUSRPROFG` | APNUSRPROFG | APN绑定 | binding | APNNAME, UPGNAME | links APN to USRPROFGROUP |
| `OBJ-PCCPOLICYGRP` | PCCPOLICYGRP | PCC策略组 | composite | PCCPOLICYGRPNAME, URRGROUPNAME, FUPSESSIONEXC | **contains** URRGROUP |

### 2.3 流过滤（5个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | 关键属性 | 包含关系 |
|-------------|---------------|----------|---------------|----------|----------|
| `OBJ-FLOWFILTER` | FLOWFILTER | 流过滤器 | composite | FLOWFILTERNAME | **contains** FILTER, L7FILTER |
| `OBJ-FLOWFILTERGRP` | FLOWFILTERGRP | 流过滤组（OR关系） | composite | FILTERGRPNAME | **contains** FLOWFILTER |
| `OBJ-FILTER` | FILTER | L3/L4过滤 | entity | FILTERNAME, PROTTYPE, SRCIP, DSTIP | belongs_to FLOWFILTER |
| `OBJ-L7FILTER` | L7FILTER | L7过滤 | entity | L7FILTERNAME, DOMAINNAME, URL | belongs_to FLOWFILTER |
| `OBJ-FLTBINDFLOWF` | FLTBINDFLOWF | 过滤器绑定 | binding | FLOWFILTERNAME, FILTERNAME | links FILTER to FLOWFILTER |

### 2.4 QoS/FUP（3个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | 关键属性 | 包含关系 |
|-------------|---------------|----------|---------------|----------|----------|
| `OBJ-QOSPROP` | QOSPROP | QoS属性 | entity | QOSPROPNAME, QOSTYPE, FQI, QCIVALUE, MBRUL, MBRDL, GBRUL, GBRDL, ARP | — |
| `OBJ-URR` | URR | 使用量上报规则 | entity | URRID, USAGERPTMODE, MEASUREMENTMETHOD, VOLUMETHRESHOLD, TIMETHRESHOLD | belongs_to URRGROUP |
| `OBJ-URRGROUP` | URRGROUP | URR组 | composite | URRGROUPNAME, UPURRNAME1/2/3, DFTURRGRPNAME | **contains** URR; belongs_to PCCPOLICYGRP |

### 2.5 ADC（1个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | 关键属性 |
|-------------|---------------|----------|---------------|----------|
| `OBJ-ADCPARA` | ADCPARA | ADC参数 | entity | ADCPARANAME, APPNAME, MATCHMODE |

### 2.6 UNC特有对象（5个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | 关键属性 | 包含关系 |
|-------------|---------------|----------|---------------|----------|----------|
| `OBJ-PCRF` | PCRF | PCRF实例 | entity | PCRFID, FQDN, IPADDR, FEATURELIST(UMCH) | belongs_to PCRFGROUP |
| `OBJ-PCRFGROUP` | PCRFGROUP | PCRF组 | composite | PCRFGROUPNAME, SELECTMODE | **contains** PCRF |
| `OBJ-PCRFBINDGRP` | PCRFBINDGRP | PCRF组绑定 | binding | PCRFGROUPNAME, PCRFID, PRIORITY | links PCRF to PCRFGROUP |
| `OBJ-PCCTEMPLATE` | PCCTEMPLATE | PCC模板 | entity | TEMPLATENAME, POLICYTYPE | — |
| `OBJ-APNDEACTQFPLCY` | APNDEACTQFPLCY | 去活QoS Flow策略 | entity | APNNAME, DEACTPOLICY(DELAY_RELEASE/IMMEDIATE_RELEASE) | — |

---

## 3. ConfigObject 间关系边（contains/belongs_to）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| BWMUSERGROUP | `contains` | BWMRULE | 用户组包含BWM规则（三级控制：用户级/组级） |
| BWMCONTROLLER | `contains` | BCSRVLEVELPLY | 控制器包含服务等级策略（智能Shaping各等级整形速率） |
| PCCPOLICYGRP | `contains` | URRGROUP | 策略组包含URR组（FUP流量监控核心链路） |
| URRGROUP | `contains` | URR | URR组包含URR（UPURRNAME1/2/3） |
| RULE | `contains` | FLOWFILTER | 规则引用流过滤器 |
| USERPROFILE | `contains` | RULE | 通过RULEBINDING |
| USRPROFGROUP | `contains` | USERPROFILE | 通过UPBINDUPG |
| FLOWFILTER | `contains` | FILTER | 通过FLTBINDFLOWF |
| FLOWFILTER | `contains` | L7FILTER | 通过FLTBINDFLOWF |
| FLOWFILTERGRP | `contains` | FLOWFILTER | OR关系组合 |
| PCRFGROUP | `contains` | PCRF | 通过PCRFBINDGRP（PCRF组包含PCRF实例） |
| BWMRULE | `refers_to` | BWMSERVICE | BWM规则引用BWM服务（业务匹配） |
| BWMRULE | `refers_to` | BWMCONTROLLER | BWM规则引用BWM控制器（控制参数） |
| BWMRULEGLOBAL | `refers_to` | BWMSERVICE | 全局规则引用BWM服务 |
| BWMRULEGLOBAL | `refers_to` | BWMCONTROLLER | 全局规则引用BWM控制器 |
| RULE(POLICYTYPE=ADC) | `depends_on` | ADCPARA | ADC规则依赖ADC参数 |
| RULE(POLICYTYPE=QOS) | `refers_to` | QOSPROP | QOS规则引用QoS属性 |

---

## 4. CommandRule（5条）

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `scope_type` | `scope_ref` | `rule_logic` | `violation_effect` | `severity` | `source_evidence_ids` |
|-----------|-------------|-------------|----------------------|-------------------|-------------|------------|--------------|-------------------|------------|----------------------|
| `CR-BW-01` | RULENAME跨POLICYTYPE不冲突 | `object_reference_rule` | explicit | restriction | object | OBJ-RULE | PCC类型的RULENAME值与QOS类型的RULENAME值不能相同；同名规则可以存在不同POLICYTYPE（如一个BWM、一个CHARGING） | 规则名冲突导致策略覆盖或下发失败 | critical | EV-CFA, EV-FK-211005 |
| `CR-BW-02` | BWMCONTROLLER CTRLTYPE决定参数集 | `parameter_dependency` | explicit | config | parameter | CMD-UDG-008.CTRLTYPE | CTRLTYPE=CAR时需配置CIR/PIR/CBS/PBS（三色标记体系）；CTRLTYPE=SHAPING时需配置RATE/QUEDEPTH（GTS队列体系）；两者参数集互斥 | 参数集不匹配导致控制器无法生效 | critical | EV-FK-110311 |
| `CR-BW-03` | CAR与Shaping不可同对象叠加 | `parameter_mutex` | explicit | restriction | object | OBJ-BWMRULE | 同一业务流（同一BWMSERVICE）不能同时绑定CAR控制器和Shaping控制器；低价值业务用CAR直接丢弃，高价值业务用Shaping缓冲 | 流量被双重控制导致业务中断或性能劣化 | warning | EV-FK-110311, EV-FK-020354 |
| `CR-BW-04` | REFRESHSRV后60秒生效 | `runtime_check_rule` | explicit | ops | command | CMD-UDG-003 | 配置变更后必须执行SET REFRESHSRV；PROTBINDFLOWF定时器约60秒后策略才完全下发到转发面；REFRESHSRV必须是最后执行的命令 | 策略不生效或部分生效 | info | EV-FK-020351, EV-FK-110311 |
| `CR-BW-05` | 预定义规则名全网唯一 | `semantic_rule` | explicit | config | parameter | ADD RULE.RULENAME | 动态PCC场景中RULENAME必须在PCRF/PCF、UNC、UDG三处保持一致；ADC场景FLOWFILTERNAME/appid也需三网元一致 | 跨网元规则名不一致导致策略无法匹配，带宽控制失效 | critical | EV-FK-211005, EV-FK-109102, EV-FK-109107 |

---

## 5. MMLCommand 关键参数集

### 5.1 ADD BWMCONTROLLER（BWM核心命令）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| BWMCNAME | string | — | 控制器名称 |
| CTRLTYPE | enum | CAR / SHAPING | 控制类型（CR-BW-02：决定后续参数集） |
| CIR | int | kbps | 承诺信息速率（CAR模式，GREEN阈值） |
| PIR | int | kbps | 峰值信息速率（CAR模式，YELLOW/RED边界） |
| CBS | int | bytes | 承诺突发尺寸（CAR模式） |
| PBS | int | bytes | 峰值突发尺寸（CAR模式） |
| RATE | int | kbps | 整形速率（Shaping模式） |
| QUEDEPTH | int | packets | GTS队列深度（Shaping模式） |
| GREENACT | enum | PASS / REMARK / DISCARD | GREEN报文动作 |
| YELLOWACT | enum | PASS / REMARK / DISCARD | YELLOW报文动作 |
| REDACT | enum | PASS / REMARK / DISCARD | RED报文动作 |
| COLORISAWARE | enum | ENABLE / DISABLE | 颜色感知模式 |
| WORKMODE | enum | AUTO / MANUAL | 智能Shaping自动/手动模式 |
| SRVLEVELSPEC | int | — | 服务等级规格数（智能Shaping） |
| USERFAIREN | enum | ENABLE / DISABLE | 用户公平使能（智能Shaping） |
| ASSUREMODE | enum | EXPRATEFIRST / RATEFIRST | 保障模式：体验优先/速率优先（智能Shaping） |
| MAXPKTLOSTRATE | int | — | 最大丢包率（万分之一，智能Shaping AUTO模式） |
| PKTLOSTRATEDTL | int | — | 丢包率差值（智能Shaping AUTO模式） |

### 5.2 ADD BWMRULE（BWM规则核心命令）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| BWMRULETYPE | enum | SUBSCRIBER_SPECIFIC / GROUP_SPECIFIC / GLOBAL | 规则层级（用户级/组级/全局级） |
| BWMSERVICENAME | string | — | 引用BWMSERVICE（业务匹配） |
| UPBWMCTRLNAME1 | string | — | 上行BWM控制器名（引用BWMCONTROLLER） |
| DNBWMCTRLNAME1 | string | — | 下行BWM控制器名（引用BWMCONTROLLER） |
| BWMRULEPRI | int | 0-65535 | 规则优先级（数字越小优先级越高） |
| USERGROUPNAME | string | — | 所属用户组（GROUP_SPECIFIC时必填） |

### 5.3 ADD RULE（PCC规则核心命令，带宽控制场景）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| RULENAME | string | — | 规则名，跨网元一致（CR-BW-01, CR-BW-05） |
| POLICYTYPE | enum | BWM / PCC / QOS / ADC | 策略类型标识（带宽控制场景独有BWM） |
| PRIORITY | int | 0-65535 | 优先级（数字越小越高） |
| FLOWFILTERNAME | string | — | 引用FLOWFILTER |
| POLICYNAME | string | — | 引用PCCPOLICYGRP |

### 5.4 ADD URR（使用量上报规则，FUP核心命令）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| URRID | int | 1-65535 | URR ID，会话内唯一 |
| USAGERPTMODE | enum | ONLINE / MONITORINGKEY / QOS | 上报模式：会话FUP用ONLINE/MONITORINGKEY，业务FUP用MONITORINGKEY，QoS保证用QOS |
| MEASUREMENTMETHOD | enum | VOLUME / DURATION / EVENT | 计量方式 |
| VOLUMETHRESHOLD | int | bytes | 流量阈值（FUP降速触发点） |
| TIMETHRESHOLD | int | seconds | 时长阈值 |

### 5.5 ADD QOSPROP（QoS属性核心命令）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| QOSPROPNAME | string | — | QoS属性名称 |
| QOSTYPE | enum | QOS_FLOW_PARA / QOS_BEARER_PARA | 5G用QOS_FLOW_PARA，2/3/4G用QOS_BEARER_PARA |
| FQI | int | 0-255 | QoS Flow Identifier（5G，QOS_FLOW_PARA时使用） |
| QCIVALUE | int | 1-9 | QCI值（2/3/4G，QOS_BEARER_PARA时使用） |
| MBRUL | int | kbps | 最大比特率-上行 |
| MBRDL | int | kbps | 最大比特率-下行 |
| GBRUL | int | kbps | 保证比特率-上行 |
| GBRDL | int | kbps | 保证比特率-下行 |
| ARP | int | 1-15 | 分配保留优先级 |

### 5.6 ADD ADCPARA（ADC参数核心命令）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| ADCPARANAME | string | — | ADC参数名称 |
| APPNAME | string | — | 应用名称（如YouTube, BitTorrent） |
| MATCHMODE | enum | EXACT / FUZZY | 匹配模式 |

---

## 6. 与计费场景命令图谱的差异

| 维度 | 计费场景 | 带宽控制场景 |
|------|---------|------------|
| MMLCommand数量 | 87（UDG 41 + UNC 46） | 55（UDG 30 + UNC 25） |
| ConfigObject数量 | 55 | 29 |
| CommandRule数量 | 14 | 5 |
| 独有命令族 | URR三件套(ADD URR/URRGROUP/PCCPOLICYGRP), 在线计费(DIAMCONNGRP/DCCTEMPLATE), 融合计费18步链(CCT/CHFINIT/CHARGECTRL/TNFGRP), CG接口(ADD CG/CDRTRANSFER) | BWM控制(ADD BWMSERVICE/BWMCONTROLLER/BWMUSERGROUP/BWMRULE/BWMRULEGLOBAL), Shaping(CTRLTYPE=SHAPING), 智能Shaping(ADD BCSRVLEVELPLY), FUP(URR复用), ADC(ADCPARA) |
| 共享命令 | SET LICENSESWITCH, ADD RULE, ADD USERPROFILE, ADD RULEBINDING, ADD PCCPOLICYGRP, ADD FLOWFILTER, ADD FILTER, ADD L7FILTER, ADD FLTBINDFLOWF, SET REFRESHSRV, LOD SIGNATUREDB/PARSERDB | 同左 |
| 共享ConfigObject | RULE, USERPROFILE, RULEBINDING, USRPROFGROUP, UPBINDUPG, APNUSRPROFG, PCCPOLICYGRP, FLOWFILTER, FILTER, L7FILTER, FLTBINDFLOWF, CATEGORYPROP, **URR, URRGROUP** | 同左（含URR/URRGROUP共享） |
| 独有ConfigObject族 | URRGRPBINDING, DIAMCONNGRP, DCCTEMPLATE, CCT, CHARGECHAR, CHGMODE, CHFINIT, TNFGRP, SELECTCHFGBYCC, CG | BWMSERVICE, BWMCONTROLLER, BWMUSERGROUP, BWMRULE, BWMRULEGLOBAL, BCSRVLEVELPLY, APNBINDBWMUSRG, PCRFGROUP, PCRFBINDGRP, PCCTEMPLATE, APNDEACTQFPLCY |
| POLICYTYPE枚举差异 | CHARGING（计费独有） | BWM（带宽控制独有）、PCC、QOS、ADC |
| URR用途差异 | RG/USAGERPTMODE/METERINGTYPE差异化计费 | VOLUMETHRESHOLD触发降速（FUP），QOS模式触发专载事件上报 |

> URR/URRGROUP是两场景共享的核心配置对象（带宽场景用于FUP流量监控与降速触发，计费场景用于内容计费/在线计费/融合计费），但参数语义不同。RULE通过POLICYTYPE区分策略类型：计费场景固定CHARGING，带宽控制场景使用BWM/PCC/QOS/ADC四种类型。

---

## 7. MMLCommand `operates_on` ConfigObject 边表

> **Schema参考**：§11.7 `MMLCommand operates_on ConfigObject`。列出核心命令与配置对象的操作关系。

### 7.1 UDG侧（17条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| SET LICENSESWITCH (CMD-UDG-001) | LICENSESWITCH | License开关操作 |
| SET BANDWIDTHMNG (CMD-UDG-002) | BWM全局状态 | BWM全局使能（元配置） |
| SET REFRESHSRV (CMD-UDG-003) | 策略刷新 | 触发配置下发到转发面 |
| LOD SIGNATUREDB (CMD-UDG-005) | SIGNATUREDB | 加载SA特征库 |
| LOD PARSERDB (CMD-UDG-006) | PARSERDB | 加载SA解析库 |
| ADD BWMSERVICE (CMD-UDG-007) | BWMSERVICE | 创建BWM服务实例 |
| ADD BWMCONTROLLER (CMD-UDG-008) | BWMCONTROLLER | 创建BWM控制器 |
| ADD BWMUSERGROUP (CMD-UDG-009) | BWMUSERGROUP | 创建BWM用户组 |
| ADD BWMRULE (CMD-UDG-010) | BWMRULE | 创建BWM规则 |
| ADD BWMRULEGLOBAL (CMD-UDG-011) | BWMRULEGLOBAL | 创建BWM全局规则 |
| ADD BCSRVLEVELPLY (CMD-UDG-012) | BCSRVLEVELPLY | 创建服务等级策略 |
| ADD CATEGORYPROP (CMD-UDG-013) | CATEGORYPROP | 创建业务分类属性 |
| ADD APNBINDBWMUSRG (CMD-UDG-014) | APNBINDBWMUSRG | APN绑定BWM用户组 |
| ADD FLOWFILTER (CMD-UDG-015) | FLOWFILTER | 创建流过滤器 |
| ADD FILTER (CMD-UDG-016) | FILTER | 创建L3/L4过滤器 |
| ADD L7FILTER (CMD-UDG-017) | L7FILTER | 创建L7过滤器 |
| ADD FLTBINDFLOWF (CMD-UDG-018) | FLTBINDFLOWF | 过滤器绑定到FLOWFILTER |

### 7.2 UDG侧 PCC/URR/QoS（8条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD SNSSAI (CMD-UDG-019) | SNSSAI | 网络切片S-NSSAI绑定 |
| ADD RULE (CMD-UDG-020) | RULE | PCC规则 |
| ADD USERPROFILE (CMD-UDG-021) | USERPROFILE | 用户模板 |
| ADD RULEBINDING (CMD-UDG-022) | RULEBINDING | 规则绑定 |
| ADD PCCPOLICYGRP (CMD-UDG-023) | PCCPOLICYGRP | PCC策略组 |
| ADD URR (CMD-UDG-024) | URR | 使用量上报规则 |
| ADD URRGROUP (CMD-UDG-025) | URRGROUP | URR组 |
| ADD QOSPROP (CMD-UDG-026) | QOSPROP | QoS属性 |

### 7.3 UDG侧辅助（3条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD ADCPARA (CMD-UDG-027) | ADCPARA | ADC参数 |
| SET APNOSLELBWMSW (CMD-UDG-028) | APN级BWM OS开关 | 终端OS差异化BWM开关 |
| ADD APNDEACTQFPLCY (CMD-UDG-030) | APNDEACTQFPLCY | 去活QoS Flow策略 |

### 7.4 UNC侧基础与PCRF（7条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| SET LICENSESWITCH (CMD-UNC-001) | LICENSESWITCH | License开关操作 |
| SET PCCFUNC (CMD-UNC-002) | PCCFUNC | PCC功能全局设置 |
| SET APNPCCFUNC (CMD-UNC-003) | APNPCCFUNC | APN级PCC功能 |
| ADD PCRF (CMD-UNC-008) | PCRF | PCRF实例定义 |
| ADD PCRFGROUP (CMD-UNC-009) | PCRFGROUP | PCRF组 |
| ADD PCRFBINDGRP (CMD-UNC-010) | PCRFBINDGRP | PCRF组绑定 |
| SET DFTGLBPCRFGRP (CMD-UNC-011) | GLBDFTPCRFGRP | 缺省全局PCRF组 |

### 7.5 UNC侧规则/模板/URR/QoS（11条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD RULE (CMD-UNC-012) | RULE | 规则定义（POLICYTYPE=BWM/PCC/QOS/ADC） |
| ADD USERPROFILE (CMD-UNC-013) | USERPROFILE | 用户模板 |
| ADD RULEBINDING (CMD-UNC-014) | RULEBINDING | 规则绑定 |
| ADD USRPROFGROUP (CMD-UNC-015) | USRPROFGROUP | 用户模板组 |
| ADD UPBINDUPG (CMD-UNC-016) | UPBINDUPG | 模板绑定到组 |
| ADD APNUSRPROFG (CMD-UNC-017) | APNUSRPROFG | APN绑定用户模板组 |
| ADD PCCPOLICYGRP (CMD-UNC-018) | PCCPOLICYGRP | PCC策略组 |
| ADD URR (CMD-UNC-019) | URR | URR规则（SMF侧） |
| ADD URRGROUP (CMD-UNC-020) | URRGROUP | URR组（SMF侧） |
| ADD QOSPROP (CMD-UNC-021) | QOSPROP | QoS属性 |
| ADD FLOWFILTER (CMD-UNC-022) | FLOWFILTER | 流过滤器 |

### 7.6 UNC侧辅助（4条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD ADCPARA (CMD-UNC-023) | ADCPARA | ADC参数 |
| SET APNIDLETIME (CMD-UNC-024) | APNIDLETIME | 专有QoS Flow空闲定时器 |
| SET APNREPORTATTR (CMD-UNC-025) | APNREPORTATTR | APN拥塞上报属性 |
| ADD PCCTEMPLATE (CMD-UNC-007) | PCCTEMPLATE | PCC模板 |

---

## 8. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| MMLCommand | 55 | CMD-UDG-001~030 + CMD-UNC-001~025 |
| ConfigObject | 29 | OBJ-BWMSERVICE~OBJ-APNDEACTQFPLCY |
| CommandRule | 5 | CR-BW-01~CR-BW-05 |
| ConfigObject contains/refers_to 边 | 17 | BWM体系4 + PCC体系4 + 过滤体系5 + PCRF体系1 + BWM引用4 + 依赖1 |
| operates_on 边 | 50 | UDG侧28 + UNC侧22 |
| **命令层对象总计** | **~156** | — |

---

> 本文件为带宽控制场景三层图谱第4层。第5层跨层映射、第6层证据索引见同目录其他文件。
