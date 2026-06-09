# 计费场景三层图谱 · 第4层：命令图谱

> **文件定位**：`three-layer-graph/04-command-graph.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §11 命令图谱
> **作用**：实例化65个MMLCommand + 26个ConfigObject + 12个CommandRule + ConfigObject间关系边
> **数据来源**：`feature-knowledge/cross-feature-analysis.md`（附录B MML命令清单、附录C 配置对象清单）、`计费场景统一知识库.md`

---

## 0. 命令图谱总览

### 0.1 MMLCommand 按产品分布

| 产品 | 命令数 | 说明 |
|------|-------|------|
| UDG | 32 | 用户面执行命令 + 核查命令集 |
| UNC | 33 | 控制面配置命令（含融合计费18步链） |
| **合计** | **65** | — |

### 0.2 ConfigObject 按功能分布

| 功能域 | 对象数 | 关键对象 |
|-------|-------|---------|
| 计费核心 | 4 | URR, URRGROUP, PCCPOLICYGRP, URRGRPBINDING |
| 规则与用户模板 | 5 | RULE, RULEBINDING, USERPROFILE, USRPROFGROUP, UPBINDUPG |
| 流过滤与业务识别 | 6 | FILTER, L7FILTER, FLOWFILTER, FLOWFILTERGRP, FLTBINDFLOWF, PROTBINDFLOWF |
| 业务分类 | 1 | CATEGORYPROP |
| 在线计费专属 | 3 | DIAMCONNGRP, DCCTEMPLATE, OCSGroup |
| 融合计费专属 | 4 | CCT, CHARGECHAR, CHGMODE, CHFINIT |
| CHF选择 | 2 | TNFGRP, SELECTCHFGBYCC |
| CG离线 | 1 | CG |
| **合计** | **26** | — |

---

## 1. MMLCommand 实例化

### 1.1 基础对象与系统配置（UDG，5个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 | `source_evidence_ids` |
|--------------|------------------|-------------------|---------|----------|----------------------|
| `CMD-UDG-001` | `SET LICENSESWITCH` | License开关，全部计费特性的前置门控 | UDG | LICITEM, SWITCH | EV-FK-*, EV-CFA |
| `CMD-UDG-002` | `LOD SIGNATUREDB` | 加载SA特征库 | UDG | DBNAME, FILENAME | EV-FK-SA-Basic |
| `CMD-UDG-003` | `LOD PARSERDB` | 加载SA解析库 | UDG | DBNAME, FILENAME | EV-FK-SA-Basic |
| `CMD-UDG-004` | `SET REFRESHSRV` | 策略刷新生效（约60秒完全下发） | UDG | REFTYPE | EV-FK-Content-UDG |
| `CMD-UDG-005` | `SET SRVCOMMONPARA` | SA公共参数配置 | UDG | PARANAME, PARAVALUE | EV-FK-SA-Basic |

### 1.2 流过滤与业务识别（UDG，6个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 |
|--------------|------------------|-------------------|---------|----------|
| `CMD-UDG-006` | `ADD CATEGORYPROP` | 业务分类属性定义 | UDG | CATEGORYPROPNAME, CATEGORYID |
| `CMD-UDG-007` | `ADD FILTER` | L3/L4过滤器（5元组） | UDG | FILTERNAME, PROTTYPE, SRCIP, DSTIP |
| `CMD-UDG-008` | `ADD L7FILTER` | L7过滤器（URL/UA等应用层字段） | UDG | L7FILTERNAME, DOMAINNAME, URL |
| `CMD-UDG-009` | `ADD FLOWFILTER` | 流过滤器（组合过滤条件容器） | UDG | FLOWFILTERNAME |
| `CMD-UDG-010` | `ADD FLTBINDFLOWF` | 过滤器绑定到FlowFilter | UDG | FLOWFILTERNAME, FILTERNAME |
| `CMD-UDG-011` | `ADD PROTBINDFLOWF` | 协议绑定到FlowFilter（需60秒延迟生效） | UDG | FLOWFILTERNAME, PROTNAME |

### 1.3 PCC规则与策略（UDG，4个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 |
|--------------|------------------|-------------------|---------|----------|
| `CMD-UDG-012` | `ADD RULE` | PCC规则定义（POLICYTYPE=CHARGING） | UDG | RULENAME, POLICYTYPE, PRIORITY, FLOWFILTERNAME, POLICYNAME |
| `CMD-UDG-013` | `ADD USERPROFILE` | 用户模板（UPTYPE=PCC） | UDG | UPNAME, UPTYPE |
| `CMD-UDG-014` | `ADD RULEBINDING` | 规则绑定到UserProfile | UDG | UPNAME, RULENAME |
| `CMD-UDG-015` | `ADD PCCPOLICYGRP` | PCC策略组（绑定URRGROUP） | UDG | PCCPOLICYGRPNAME, URRGROUPNAME |

### 1.4 URR计费三件套（UDG，4个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 |
|--------------|------------------|-------------------|---------|----------|
| `CMD-UDG-016` | `ADD URR` | 使用量上报规则 | UDG | URRID, USAGERPTMODE, OFFMETERINGTYPE, ONLMETERINGTYPE, RG, SID, VOLUMETHRESHOLD, TIMETHRESHOLD |
| `CMD-UDG-017` | `ADD URRGROUP` | URR组（UPURRNAME1/2/3） | UDG | URRGROUPNAME, UPURRNAME1, UPURRNAME2, UPURRNAME3, DFTURRGRPNAME |
| `CMD-UDG-018` | `SET URRGRPBINDING` | URR组绑定 | UDG | UPTYPE, UPNAME, URRGROUPNAME |
| `CMD-UDG-019` | `SET SPECTRAFURRGRP` | 特殊流量计费兜底URR组 | UDG | URRGROUPNAME |

### 1.5 计费专属（UDG，3个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 |
|--------------|------------------|-------------------|---------|----------|
| `CMD-UDG-020` | `ADD QUOTAEXHAUSTACT` | 在线RG配额耗尽动作 | UDG | URRID, FACTION(BLOCK/REDIRECT/FORWARD) |
| `CMD-UDG-021` | `SET UPDEFAULTQUOTA` | Default Quota默认配额（OCS不可达容灾） | UDG | DEFAULTQUOTA |
| `CMD-UDG-022` | `SET URRFAILACTION` | 新业务无URR时容灾放通 | UDG | RETRYFAILACT(CONTINUE) |

### 1.6 核查命令集（UDG，10个）

| `command_id` | `command_syntax` | `command_summary` | product |
|--------------|------------------|-------------------|---------|
| `CMD-UDG-023` | `LST RULEBINDING` | 查看规则绑定 | UDG |
| `CMD-UDG-024` | `LST RULE` | 查看规则 | UDG |
| `CMD-UDG-025` | `LST PCCPOLICYGRP` | 查看PCC策略组 | UDG |
| `CMD-UDG-026` | `LST URRGROUP` | 查看URR组 | UDG |
| `CMD-UDG-027` | `LST URR` | 查看URR | UDG |
| `CMD-UDG-028` | `LST PROTBINDFLOWF` | 查看协议绑定 | UDG |
| `CMD-UDG-029` | `LST FLOWFILTER` | 查看流过滤器 | UDG |
| `CMD-UDG-030` | `LST L7FILTER` | 查看L7过滤器 | UDG |
| `CMD-UDG-031` | `LST USERPROFILE` | 查看用户模板 | UDG |
| `CMD-UDG-032` | `LST SPECTRAFURRGRP` | 查看兜底URR组 | UDG |

### 1.7 UNC基础配置（4个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 |
|--------------|------------------|-------------------|---------|----------|
| `CMD-UNC-001` | `SET LICENSESWITCH` | License开关 | UNC | LICENSECODE, SWITCH |
| `CMD-UNC-002` | `SET CHGMODE` | 全局计费接口模式（NchfMode/GaGyMode） | UNC | TMACCTYPE, FORCED(NchfMode/GaGyMode) |
| `CMD-UNC-003` | `ADD APNCHGMODE` | APN级计费接口模式 | UNC | APNNAME, FORCED, BY5GSIWKI |
| `CMD-UNC-004` | `ADD ROAMCHGMODE` | 漫游级计费接口模式 | UNC | ROAMTYPE, FORCED |

### 1.8 UNC融合计费专属（8个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 |
|--------------|------------------|-------------------|---------|----------|
| `CMD-UNC-005` | `SET CHARGECTRL` | 全局融合计费使能 | UNC | HOMECONVERGED, RGAPPLIED |
| `CMD-UNC-006` | `SET USRPROFCHARGE` | UserProfile级计费控制 | UNC | UPNAME, HOMECONVERGED, CCTNAME |
| `CMD-UNC-007` | `SET APNCHARGECTRL` | DNN/APN级计费控制 | UNC | APNNAME, CONVERGEDSW, CCTNAME |
| `CMD-UNC-008` | `SET CHFINIT` | CHF交互使能 | UNC | CHFINIT(SENDREQ), CCRINITRGNUM, RGSOURCE |
| `CMD-UNC-009` | `ADD CHARGECHAR` | CC计费属性实例 | UNC | CCNAME, CCVALUE, HOME/ROAM/VISIT |
| `CMD-UNC-010` | `SET GLBCHARGECHAR` | 全局CC计费属性 | UNC | CCVALUE, HOMESGSN, ROAMSGSN |
| `CMD-UNC-011` | `ADD CCT` | 融合计费模板 | UNC | CCTNAME, QHT, VQT, TQT, VT, PDUVOLUMELIMIT |
| `CMD-UNC-012` | `ADD SELECTCCTBYCC` | 按CC绑定CCT模板 | UNC | CCTNAME, CCNAME |

### 1.9 UNC CHF选择与接入（7个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 |
|--------------|------------------|-------------------|---------|----------|
| `CMD-UNC-013` | `ADD TNFINS` | CHF实例定义 | UNC | SRVNAME(NchfConvCharg), FQDN |
| `CMD-UNC-014` | `ADD TNFINSIP` | CHF实例IP | UNC | TNFNAME, IPADDR |
| `CMD-UNC-015` | `ADD TNFGRP` | CHF组 | UNC | TNFGRPNAME |
| `CMD-UNC-016` | `ADD TNFBINDGRP` | CHF实例绑定到组 | UNC | TNFGRPNAME, TNFNAME |
| `CMD-UNC-017` | `ADD SELECTCHFGBYCC` | 按CC选择CHF组 | UNC | CCNAME, PRIMARYTNFGRP, SECONDARYTNFGRP |
| `CMD-UNC-018` | `SET GLBDFTCHFGROUP` | 全局缺省CHF组 | UNC | TNFGRPNAME |
| `CMD-UNC-019` | `ADD SELCHFGBYIMSI` | 按IMSI选择CHF（测试用） | UNC | IMSI, PRIMARYTNFGRP, SECONDARYTNFGRP |

### 1.10 UNC Trigger与异常处理（8个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 |
|--------------|------------------|-------------------|---------|----------|
| `CMD-UNC-020` | `ADD PDUTRIGGER` | Session级触发器 | UNC | TRIGGERNAME, TRIGGERCAT(IMMEDIATE/DEFERRED/NONREPORT) |
| `CMD-UNC-021` | `ADD RGTRIGGER` | RG级触发器 | UNC | TRIGGERNAME(QUOTATHRESHOLD/VT/QHT), TRIGGERCAT |
| `CMD-UNC-022` | `SET N40APIVER` | N40 API版本 | UNC | APIVER(F30), FEATURE |
| `CMD-UNC-023` | `SET FAILHANDLING` | 全局异常处理 | UNC | FHACTION(CONTINUE), FAILOVERSUP, TXTIMER |
| `CMD-UNC-024` | `ADD PDUSCACT` | PDU级异常返回码动作 | UNC | RESULTCODE, ACTION(FAILOVER/CONTINUE) |
| `CMD-UNC-025` | `ADD RGRCACT` | RG级异常返回码动作 | UNC | RESULTCODE, ACTION |
| `CMD-UNC-026` | `SET CNVRGDCHGPARA` | 融合计费参数 | UNC | BADRSPACT, TIMEROUNDMODE, RPTBASEDONGU |
| `CMD-UNC-027` | `SET N40MSGSTG` | N40消息缓存 | UNC | STGSWITCH(ENABLE), REPLAYINTERVAL |

### 1.11 UNC URR/规则/模板组（6个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 |
|--------------|------------------|-------------------|---------|----------|
| `CMD-UNC-028` | `ADD URR` | URR规则（SMF侧） | UNC | URRNAME, URRID, USAGERPTMODE, ONLINERG |
| `CMD-UNC-029` | `ADD URRGROUP` | URR组（SMF侧） | UNC | URRGROUPNAME, UPURRNAME1/2/3 |
| `CMD-UNC-030` | `ADD PCCPOLICYGRP` | PCC策略组（SMF侧） | UNC | PCCPOLICYGRPNM, URRGROUPNAME |
| `CMD-UNC-031` | `ADD RULE` | 规则定义（SMF侧） | UNC | RULENAME, POLICYTYPE, PRIORITY, POLICYNAME |
| `CMD-UNC-032` | `ADD USERPROFILE` | 用户模板（SMF侧） | UNC | UPNAME |
| `CMD-UNC-033` | `ADD RULEBINDING` | 规则绑定（SMF侧） | UNC | UPNAME, RULENAME |

### 1.12 UNC CG接口（离线计费，4个）

| `command_id` | `command_syntax` | `command_summary` | product | 关键参数 |
|--------------|------------------|-------------------|---------|----------|
| `CMD-UNC-CG1` | `ADD CG` | CG实例（WAL保护） | UNC | CGNAME, IPADDR, WAL |
| `CMD-UNC-CG2` | `SET CDRTRANSFER` | 话单发送（负荷分担算法） | UNC | ALGTYPE(LOADBASED/USERBASED) |
| `CMD-UNC-CG3` | `SET OFCTHRESHOLD` | 离线话单阈值 | UNC | TIMEINTERVAL, VOLUMETHRESHOLD |
| `CMD-UNC-CG4` | `SET CONTAINERTRIGGER` | 话单容器触发条件 | UNC | TRIGGERTYPE, THRESHOLD |

---

## 2. ConfigObject 实例化（26个）

### 2.1 计费核心对象（4个）

| `object_id` | `object_name` | 所属功能 | 关键属性 | 包含关系 |
|-------------|---------------|----------|----------|----------|
| `OBJ-URR` | URR | 计费三件套 | URRID, USAGERPTMODE, OFFMETERINGTYPE, RG | belongs_to URRGROUP |
| `OBJ-URRGROUP` | URRGROUP | 计费三件套 | URRGROUPNAME, UPURRNAME1/2/3, DFTURRGRPNAME | **contains** URR; belongs_to PCCPOLICYGRP |
| `OBJ-PCCPOLICYGRP` | PCCPOLICYGRP | 计费三件套 | PCCPOLICYGRPNAME, URRGROUPNAME | **contains** URRGROUP |
| `OBJ-URRGRPBINDING` | URRGRPBINDING | URR组绑定 | UPNAME, URRGROUPNAME | links USERPROFILE to URRGROUP |

### 2.2 规则与用户模板（5个）

| `object_id` | `object_name` | 所属功能 | 关键属性 | 包含关系 |
|-------------|---------------|----------|----------|----------|
| `OBJ-RULE` | RULE | PCC规则 | RULENAME, POLICYTYPE, PRIORITY | **contains** FLOWFILTER; refers_to PCCPOLICYGRP |
| `OBJ-RULEBINDING` | RULEBINDING | 规则绑定 | UPNAME, RULENAME | links USERPROFILE to RULE |
| `OBJ-USERPROFILE` | USERPROFILE | 用户模板 | UPNAME, UPTYPE | **contains** RULE (via RULEBINDING) |
| `OBJ-USRPROFGROUP` | USRPROFGROUP | 用户模板组 | UPGNAME | **contains** USERPROFILE (via UPBINDUPG) |
| `OBJ-UPBINDUPG` | UPBINDUPG | 模板绑定 | UPGNAME, UPNAME | links USERPROFILE to USRPROFGROUP |

### 2.3 流过滤与业务识别（6个）

| `object_id` | `object_name` | 所属功能 | 关键属性 | 包含关系 |
|-------------|---------------|----------|----------|----------|
| `OBJ-FILTER` | FILTER | L3/L4过滤 | FILTERNAME, PROTTYPE, SRCIP, DSTIP | belongs_to FLOWFILTER |
| `OBJ-L7FILTER` | L7FILTER | L7过滤 | L7FILTERNAME, DOMAINNAME, URL | belongs_to FLOWFILTER |
| `OBJ-FLOWFILTER` | FLOWFILTER | 流过滤器 | FLOWFILTERNAME | **contains** FILTER, L7FILTER |
| `OBJ-FLOWFILTERGRP` | FLOWFILTERGRP | 流过滤组（OR关系） | FILTERGRPNAME | **contains** FLOWFILTER |
| `OBJ-FLTBINDFLOWF` | FLTBINDFLOWF | 过滤器绑定 | FLOWFILTERNAME, FILTERNAME | links FILTER to FLOWFILTER |
| `OBJ-PROTBINDFLOWF` | PROTBINDFLOWF | 协议绑定 | FLOWFILTERNAME, PROTNAME | links Protocol to FLOWFILTER |

### 2.4 业务分类（1个）

| `object_id` | `object_name` | 所属功能 | 关键属性 |
|-------------|---------------|----------|----------|
| `OBJ-CATEGORYPROP` | CATEGORYPROP | 业务分类 | CATEGORYPROPNAME, CATEGORYID |

### 2.5 在线计费专属（3个）

| `object_id` | `object_name` | 所属功能 | 关键属性 |
|-------------|---------------|----------|----------|
| `OBJ-DIAMCONNGRP` | DIAMCONNGRP | Diameter链路组 | SELECTMODE(主备/负荷分担), ENDPOINT |
| `OBJ-DCCTEMPLATE` | DCCTEMPLATE | DCC模板 | SESSIONMODE, CCFH, VALIDTIME, QHT |
| `OBJ-OCSGROUP` | OCSGroup | OCS选择组 | PRIMARYOCS, SECONDARYOCS |

### 2.6 融合计费专属（UNC侧，4个）

| `object_id` | `object_name` | 所属功能 | 关键属性 |
|-------------|---------------|----------|----------|
| `OBJ-CCT` | CCT | 融合计费模板 | CCTNAME, QHT, VQT, TQT, VT, PDUVOLUMELIMIT |
| `OBJ-CHARGECHAR` | CHARGECHAR | CC计费属性 | CCNAME, CCVALUE, HOME, ROAM, VISIT |
| `OBJ-CHGMODE` | CHGMODE | 计费接口模式 | TMACCTYPE, FORCED(NchfMode/GaGyMode) |
| `OBJ-CHFINIT` | CHFINIT | CHF交互使能 | CHFINIT(SENDREQ), CCRINITRGNUM, RGSOURCE |

### 2.7 CHF选择（2个）

| `object_id` | `object_name` | 所属功能 | 关键属性 | 包含关系 |
|-------------|---------------|----------|----------|----------|
| `OBJ-TNFGRP` | TNFGRP | CHF组 | TNFGRPNAME | **contains** TNFINS (via TNFBINDGRP) |
| `OBJ-SELECTCHFGBYCC` | SELECTCHFGBYCC | 按CC选择CHF | CCNAME, PRIMARYTNFGRP, SECONDARYTNFGRP | links CHARGECHAR to TNFGRP |

### 2.8 CG对象（离线，1个）

| `object_id` | `object_name` | 所属功能 | 关键属性 |
|-------------|---------------|----------|----------|
| `OBJ-CG` | CG | 离线计费CG | CGNAME, IPADDR, WAL, PRIORITY |

---

## 3. ConfigObject 间关系边（contains/belongs_to）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| PCCPOLICYGRP | `contains` | URRGROUP | 策略组包含URR组 |
| URRGROUP | `contains` | URR | URR组包含URR（UPURRNAME1/2/3） |
| USERPROFILE | `contains` | RULE | 通过RULEBINDING |
| USRPROFGROUP | `contains` | USERPROFILE | 通过UPBINDUPG |
| RULE | `contains` | FLOWFILTER | 规则引用流过滤器 |
| FLOWFILTER | `contains` | FILTER | 通过FLTBINDFLOWF |
| FLOWFILTER | `contains` | L7FILTER | 通过FLTBINDFLOWF |
| FLOWFILTERGRP | `contains` | FLOWFILTER | OR关系组合 |
| TNFGRP | `contains` | TNFINS | 通过TNFBINDGRP（CHF组包含CHF实例） |

---

## 4. CommandRule（12条）

| `rule_id` | `rule_name` | `rule_type` | `rule_logic` | `severity` | 关联命令 |
|-----------|-------------|-------------|--------------|------------|----------|
| `CR-01` | URRID会话内唯一 | `semantic_rule` | 同一PDU会话内URR ID不能重复（不同业务需分段分配ID空间，如1-99/100+） | critical | ADD URR |
| `CR-02` | RG值跨侧一致性 | `validation_rule` | SMF侧与UPF侧URR的RG（Rating Group）值必须完全一致，否则CHF批价与UPF统计脱节 | critical | ADD URR (UDG+UNC) |
| `CR-03` | 三件套绑定完整性 | `validation_rule` | Rule→PCCPOLICYGRP→URRGROUP→URR 链路必须完整无断裂，任何一环缺失导致计费不生效 | critical | ADD RULE/PCCPOLICYGRP/URRGROUP/URR |
| `CR-04` | REFRESHSRV必须最后执行 | `runtime_check_rule` | SET REFRESHSRV必须在所有FILTER/L7FILTER/FLOWFILTER配置完成后执行，且PROTBINDFLOWF需等待60秒 | warning | SET REFRESHSRV |
| `CR-05` | License前置门控 | `validation_rule` | 计费特性配置前必须先SET LICENSESWITCH开启对应License；内容计费需UNC+UDG双License同时开启 | critical | SET LICENSESWITCH |
| `CR-06` | 三联前置约束（融合计费） | `validation_rule` | 融合计费场景下CHGMODE=NchfMode + CHARGECTRL使能 + CHFINIT=SENDREQ 三项必须全部满足 | critical | SET CHGMODE/CHARGECTRL/CHFINIT |
| `CR-07` | RGAPPLIED与USAGERPTMODE匹配 | `restriction_rule` | URR.USAGERPTMODE必须与用户级RGAPPLIED一致；RGAPPLIED=DEFAULT时URRGROUP中不能同时配相同RG的在线和离线URR | critical | ADD URR/URRGROUP, SET CHARGECTRL |
| `CR-08` | 跨网元名称一致性 | `validation_rule` | USERPROFILENAME/RULENAME/URRID/USAGERPTMODE/METERINGTYPE在SMF与UPF两侧必须一致 | critical | ADD URR/RULE/USERPROFILE (UDG+UNC) |
| `CR-09` | offline/online互斥 | `restriction_rule` | offline和online不能同时为true（PCC规则），可同时为false（不计费）；PCF下发优先级高于SMF本地配置 | warning | ADD RULE |
| `CR-10` | 超时阻塞公式 | `runtime_check_rule` | 在线/融合计费超时时间 = T3RESPONSE × N3REQUEST + 4秒，超时未收到配额更新则UPF阻塞业务 | warning | SET UPPFCPPATH, SET URRFAILACTION |
| `CR-11` | CP/UP一致性检查周期 | `runtime_check_rule` | SMF每30分钟扫描UPF配置，不一致触发ALM-81054告警（UPF侧）和ALM-81026（SMF侧），为配对告警 | info | — |
| `CR-12` | IMSI-CHF绑定不实时切换 | `restriction_rule` | MOD SELCHFGBYIMSI修改后已激活用户不会立即切换CHF，必须去激活后重新激活才生效 | warning | ADD/MOD SELCHFGBYIMSI |

---

## 5. MMLCommand 关键参数集（仅核心差异化参数）

### 5.1 ADD URR（计费核心命令）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| URRID | int | 1-65535 | URR ID，会话内唯一（CR-01） |
| USAGERPTMODE | enum | OFFLINE/ONLINE/MONITORINGKEY | 上报模式：离线/在线/监控 |
| OFFMETERINGTYPE | enum | VOLUME/DURATION/EVENT | 离线计量方式 |
| ONLMETERINGTYPE | enum | VOLUME/DURATION/EVENT | 在线计量方式 |
| RG | int | 1-999 | Rating Group，跨侧一致（CR-02） |
| SID | int | 0-9999 | Service Identifier |
| VOLUMETHRESHOLD | int | 字节数 | 流量阈值 |
| TIMETHRESHOLD | int | 秒 | 时长阈值 |
| DFTQUOTAVOLUME | int | 字节数 | Default Quota（在线） |
| DFTQUOTATIME | int | 秒 | Default Quota时长 |

### 5.2 ADD RULE（PCC规则核心命令）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| RULENAME | string | — | 规则名，跨侧一致（CR-08） |
| POLICYTYPE | enum | CHARGING/QOS/ADC | 计费场景固定CHARGING |
| PRIORITY | int | 0-65535 | 数字越小优先级越高（FR-05） |
| FLOWFILTERNAME | string | — | 引用FLOWFILTER |
| POLICYNAME | string | — | 引用PCCPOLICYGRP |
| OFFLINE | bool | true/false | 离线计费标志（CR-09） |
| ONLINE | bool | true/false | 在线计费标志（CR-09） |

### 5.3 ADD CCT（融合计费模板核心命令）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| CCTNAME | string | — | 融合计费模板名 |
| QHT | int | 字节数 | Quota Holding Threshold（配额保持阈值） |
| VQT | int | 字节数 | Volume Quota Threshold（流量配额阈值） |
| TQT | int | 秒 | Time Quota Threshold（时长配额阈值） |
| VT | int | 字节数 | Volume Threshold（流量阈值，触发上报） |
| PDUVOLUMELIMIT | int | 字节数 | PDU会话流量限制 |

---

## 6. 与带宽场景命令图谱的差异

| 维度 | 计费场景 | 带宽控制场景 |
|------|---------|------------|
| MMLCommand数量 | 65（UDG 32 + UNC 33） | 55（UDG 30 + UNC 25） |
| ConfigObject数量 | 26 | ~26 |
| CommandRule数量 | 12 | 5 |
| 独有命令族 | URR三件套(ADD URR/URRGROUP/PCCPOLICYGRP), 在线计费(DIAMCONNGRP/DCCTEMPLATE), 融合计费18步链(CCT/CHFINIT/CHARGECTRL/TNFGRP), CG接口(ADD CG/CDRTRANSFER) | BWM控制(BWMSERVICE/BWMCONTROLLER/BWMRULE), Shaping, FUP(URR复用), ADC(ADCPARA) |
| 共享命令 | SET LICENSESWITCH, ADD RULE, ADD USERPROFILE, ADD RULEBINDING, ADD PCCPOLICYGRP, ADD FLOWFILTER, ADD FILTER, ADD L7FILTER, ADD FLTBINDFLOWF, ADD PROTBINDFLOWF, SET REFRESHSRV, LOD SIGNATUREDB/PARSERDB | 同左 |
| 共享ConfigObject | RULE, USERPROFILE, RULEBINDING, USRPROFGROUP, UPBINDUPG, APNUSRPROFG, PCCPOLICYGRP, FLOWFILTER, FILTER, L7FILTER, FLTBINDFLOWF, PROTBINDFLOWF, CATEGORYPROP, **URR, URRGROUP** | 同左（含URR/URRGROUP共享） |
| 独有ConfigObject族 | URRGRPBINDING, DIAMCONNGRP, DCCTEMPLATE, CCT, CHARGECHAR, CHGMODE, CHFINIT, TNFGRP, SELECTCHFGBYCC, CG | BWMSERVICE, BWMCONTROLLER, BWMUSERGROUP, BWMRULE, BWMRULEGLOBAL, BCSRVLEVELPLY, APNBINDBWMUSRG |

> URR/URRGROUP是两场景共享的核心计费对象（带宽场景用于FUP，计费场景用于内容计费/在线计费/融合计费），但参数语义不同（带宽场景关注VOLUMETHRESHOLD触发降速；计费场景关注RG/USAGERPTMODE/METERINGTYPE差异化计费）。

---

## 7. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| MMLCommand | 65 | CMD-UDG-001~032 + CMD-UNC-001~033 |
| ConfigObject | 26 | OBJ-URR~OBJ-CG |
| CommandRule | 12 | CR-01~CR-12 |
| ConfigObject contains 边 | 9 | — |
| **命令层对象总计** | **112** | — |

---

> 本文件为计费场景三层图谱第4层。第5层跨层映射、第6层证据索引见同目录其他文件。
