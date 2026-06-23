# 访问限制场景三层图谱 · 第4层：命令图谱

> **文件定位**：`three-layer-graph/04-command-graph.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §11 命令图谱（§11.3 MMLCommand / §11.4 CommandParameter / §11.5 ConfigObject / §11.6 CommandRule / §11.7 关系）
> **作用**：实例化 **68个MMLCommand**（UDG 48 + UNC 20）+ **41个ConfigObject**（共享18 + 访问限制独有23）+ **14条CommandRule** + ConfigObject间关系边，并完整体现**双轨道+五子轨**动作体系的ConfigObject链
> **数据来源**：`feature-knowledge/cross-feature-analysis.md`（附录B MML命令交叉参考、附录C 配置对象复用矩阵、附录D 典型配置流程、附录E 双轨机制深度对比、附录F POLICYTYPE全景表）

---

## 0. 命令图谱总览

### 0.1 MMLCommand 按产品分布

| 产品 | 命令数 | 说明 |
|------|-------|------|
| UDG | 48 | 用户面执行命令：双轨道+五子轨动作体系（轨道A 五子轨：ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY + 轨道B：URL过滤 CFTEMPLATE/CONTCATEGBIND.ACTION）+ SA特征库 + 三四层/七层过滤 + IPFarm集群 + ICAP互通 + PCC规则与策略6命令 |
| UNC | 20 | 控制面策略命令：PCC骨架（PCRF管理 + 规则/模板绑定链）+ 位置触发（USRLOCATION/USRLOCATIONGRP） |
| **合计** | **68** | — |

> **★ 计数修正说明（U-H-04，P5 修复）**：P5 前声明 "62（UDG 42 + UNC 20）"，但实际 UDG 编号到 CMD-UDG-048，其中 §1.10 的 6 个 PCC 规则与策略命令（RULE/USERPROFILE/RULEBINDING/PCCPOLICYGRP/URR/URRGROUP，CMD-UDG-043~048）此前被误排除在 "主清单42" 之外。P5 修正：这 6 个命令均为正式编号且参与 §6 operates_on 边，统一计入主清单，UDG 42→48、合计 62→68。

### 0.2 ConfigObject 按功能分布

| 功能域 | 对象数 | 关键对象 |
|-------|-------|---------|
| PCC通用规则与用户模板（三场景共享） | 7 | RULE, USERPROFILE, RULEBINDING, USRPROFGROUP, UPBINDUPG, APNUSRPROFG, PCCPOLICYGRP |
| 流过滤（三场景共享） | 6 | FLOWFILTER, FLOWFILTERGRP, FILTER, L7FILTER, FLTBINDFLOWF, PROTBINDFLOWF |
| 三四层/多维扩展（重定向族独有） | 2 | EXTENDEDFILTER, ERRORCODE |
| 计费属性（三场景共享） | 2 | URR, URRGROUP |
| ADC（跨场景共享） | 1 | ADCPARA |
| 业务分类（三场景共享） | 1 | CATEGORYPROP |
| 头增强轨道（访问限制独有） | 1 | HEADEN |
| SMARTREDIRECT轨道（访问限制独有） | 3 | SMARTHTTPREDIR, REDIRAPPENDINFO, DNSOVERWRITING |
| WEBPROXY/Portal轨道（访问限制独有） | 5 | IPFARMGLOBAL, IPFARM, IPFARMSERVER, LOGICINF, BLACKLISTRULE |
| URL过滤轨道（访问限制独有，轨道B） | 10 | VPNINST, ICAPSERVER, ICAPLOCALINFO, ICAPSVRGRP, ICAPSVRBINDISG, CFPROFILE, CFTEMPLATE, CONTCATEGROUP, CONTCATEGBIND, APNCFTEMPLATE/CFPROFBINDCFT |
| 接入控制触发（访问限制独有，UNC侧） | 2 | USRLOCATION, USRLOCATIONGRP |
| 辅助 | 1 | WELLKNOWNPORT |
| **合计** | **41** | — |

### 0.3 CommandRule 按严重级别分布

| severity | 数量 | 说明 |
|----------|------|------|
| critical | 8 | RULENAME跨POLICYTYPE不冲突 / POLICYTYPE决定动作对象链 / 头防欺诈强依赖HEADEN / ICAP Server必需 / URL过滤PERMIT唯一 / FLOWFILTER必须绑定 / 预定义规则名三网元一致 / 引用对象必须已存在 |
| warning | 3 | REFRESHSRV后60秒禁改Filter / HTTPS加密盲区 / RTSP不支持头防欺诈 |
| info | 3 | REFRESHSRV时序 / SET REFRESHSRV必须最后执行 / 双轨可并存 |
| **合计** | **14** | — |

---

## 1. MMLCommand 实例化（68个）

> 编号规则：CMD-UDG-NNN / CMD-UNC-NNN；共享命令沿用通用编号区间，访问限制独有命令按功能族顺序编号。

### 1.1 License与刷新（UDG，4个，三场景共享）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-001` | `SET LICENSESWITCH` | SET | LICENSESWITCH | License开关，全部访问限制特性的前置门控（★ P5 修复 U-M-08：原占位符 `EV-FK-AC-*` 替换为全部 11 个独有特性 EV 列表 + 复用特性 4 个） | active | EV-FK-AC-01, EV-FK-AC-02, EV-FK-AC-04, EV-FK-AC-06, EV-FK-AC-07, EV-FK-AC-08, EV-FK-AC-09, EV-FK-AC-10, EV-FK-AC-11, EV-FK-AC-12, EV-FK-AC-13, EV-FK-AC-14, EV-CA-AC-01 |
| `CMD-UDG-002` | `SET REFRESHSRV` | SET | REFRESHSRV | 策略刷新生效（约60秒PROTBINDFLOWF定时器后完全下发；REFRESHTYPE=ALL/USERPROFILE） | active | EV-FK-AC-04, EV-FK-AC-06, EV-FK-AC-14, EV-CA-AC-01 |
| `CMD-UDG-003` | `LOD SIGNATUREDB` | LOD | SIGNATUREDB | 加载SA特征库（ADC/头增强族/Portal/DNS纠错/防欺诈/URL过滤共用） | active | EV-FK-AC-01, EV-FK-AC-04, EV-FK-AC-12, EV-FK-AC-14 |
| `CMD-UDG-004` | `LOD PARSERDB` | LOD | PARSERDB | 加载协议解析库（头防欺诈显式依赖） | active | EV-FK-AC-09 |

### 1.2 三四层过滤链（UDG，3个，三场景共享）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-005` | `ADD FILTER` | ADD | FILTER | 增加三四层过滤器（5元组，11个独有特性共用） | active | EV-FK-AC-04, EV-FK-AC-06, EV-FK-AC-10, EV-CA-AC-01 |
| `CMD-UDG-006` | `ADD FLOWFILTER` | ADD | FLOWFILTER | 增加流过滤器（组合过滤条件容器） | active | EV-CA-AC-01, EV-FK-AC-02 |
| `CMD-UDG-007` | `ADD FLTBINDFLOWF` | ADD | FLTBINDFLOWF | 增加Filter与FlowFilter绑定 | active | EV-CA-AC-01 |

### 1.3 七层过滤链（UDG，5个，ADC/头增强族/Portal/防欺诈共用）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-008` | `ADD L7FILTER` | ADD | L7FILTER | 增加七层过滤器（URL/Method） | active | EV-FK-AC-04, EV-FK-AC-06, EV-FK-AC-10, EV-FK-AC-09 |
| `CMD-UDG-009` | `ADD PROTBINDFLOWF` | ADD | PROTBINDFLOWF | 增加流过滤器协议绑定（协议+L7FILTER） | active | EV-FK-AC-04, EV-FK-AC-06, EV-FK-AC-09 |
| `CMD-UDG-010` | `ADD EXTENDEDFILTER` | ADD | EXTENDEDFILTER | 增加扩展过滤器（URL/UserAgent/ContentType/ERRORCODE多维，HTTP重定向+DNS纠错共用） | active | EV-FK-AC-12, EV-FK-AC-13 |
| `CMD-UDG-011` | `ADD ERRORCODE` | ADD | ERRORCODE | 增加错误码范围（HTTP错误码GT 400 / DNS错误码EQUAL 3 NXDOMAIN） | active | EV-FK-AC-12, EV-FK-AC-13 |
| `CMD-UDG-012` | `ADD WELLKNOWNPORT` | ADD | WELLKNOWNPORT | 增加知名端口（头防欺诈识别HTTP端口80/8080） | active | EV-FK-AC-09 |

### 1.4 ADC独有（UDG，1个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-013` | `ADD ADCPARA` | ADD | ADCPARA | 增加ADC参数（FLOWINFORPT流信息上报 + ADCHYSTTIMER迟滞定时器） | active | EV-FK-AC-04 |

### 1.5 头增强族独有（UDG，2个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-014` | `ADD HEADEN` | ADD | HEADEN | 增加头增强对象（跨4特性复用：HTTP/HTTPS/RTSP头增强+头防欺诈；含ANTIFRAUD/GRAYLIST内嵌防欺诈） | active | EV-FK-AC-06, EV-FK-AC-07, EV-FK-AC-08, EV-FK-AC-09 |
| `CMD-UDG-015` | `SET BASE64` | SET | BASE64 | base64编码开关（头增强族编码能力控制） | active | EV-FK-AC-06, EV-FK-AC-07, EV-FK-AC-08 |

### 1.6 SMARTREDIRECT轨道（UDG，2个，HTTP智能重定向+DNS纠错共用）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-016` | `ADD SMARTHTTPREDIR` | ADD | SMARTHTTPREDIR | 增加HTTP智能重定向动作策略（L7 HTTP响应改写；绑定EXTENDEDFILTER+ERRORCODE+REDIRAPPENDINFO） | active | EV-FK-AC-13 |
| `CMD-UDG-017` | `ADD REDIRAPPENDINFO` | ADD | REDIRAPPENDINFO | 增加重定向携带信息（MSISDN/IMSI/IMEI；HTTP智能重定向独有） | active | EV-FK-AC-13 |
| `CMD-UDG-018` | `ADD DNSOVERWRITING` | ADD | DNSOVERWRITING | 增加DNS重写动作（含Platform IP；DNS纠错独有；RULE.POLICYNAME指向区分SMARTREDIRECT子类型） | active | EV-FK-AC-12 |

### 1.7 WEBPROXY/Portal轨道 — IPFarm集群（UDG，4个，Portal+WebProxy共用）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-019` | `SET IPFARMGLOBAL` | SET | IPFARMGLOBAL | 设置IPFarm全局参数（LBMETHOD负荷分担/HEALTHSUCCLIMIT/HEALTHFAILLIMIT心跳阈值） | active | EV-FK-AC-10, EV-FK-AC-11 |
| `CMD-UDG-020` | `ADD IPFARM` | ADD | IPFARM | 增加IPFarm（重定向服务器集群容器，整机64个） | active | EV-FK-AC-10, EV-FK-AC-11 |
| `CMD-UDG-021` | `ADD IPFARMSERVER` | ADD | IPFARMSERVER | 增加IPFarm服务器（每个IPFarm最多512个IP） | active | EV-FK-AC-10, EV-FK-AC-11 |
| `CMD-UDG-022` | `ADD LOGICINF` | ADD | LOGICINF | 增加逻辑接口（心跳检测+ICAP互通共用；不同IPFarm必须用不同接口） | active | EV-FK-AC-10, EV-FK-AC-11, EV-FK-AC-14 |
| `CMD-UDG-023` | `ADD BLACKLISTRULE` | ADD | BLACKLISTRULE | 增加黑名单规则（WebProxy独有） | active | EV-FK-AC-11 |
| `CMD-UDG-024` | `ADD APN` | ADD | APN | 增加APN配置（Portal/WebProxy/URL过滤共用） | active | EV-FK-AC-10, EV-FK-AC-11, EV-FK-AC-14 |

### 1.8 URL过滤轨道 — ICAP互通前置（UDG，6个，轨道B独立链路）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-025` | `ADD VPNINST` | ADD | VPNINST | 增加VPN实例（ICAP互通专网） | active | EV-FK-AC-14 |
| `CMD-UDG-026` | `ADD ICAPSERVER` | ADD | ICAPSERVER | 增加ICAP服务器（ICAPSERVERTYPE=URL_FILTERING；轨道B必需外部依赖） | active | EV-FK-AC-14 |
| `CMD-UDG-027` | `ADD ICAPLOCALINFO` | ADD | ICAPLOCALINFO | 增加ICAP本端信息（USERAGENT） | active | EV-FK-AC-14 |
| `CMD-UDG-028` | `ADD ICAPSVRGRP` | ADD | ICAPSVRGRP | 增加ICAP服务器组 | active | EV-FK-AC-14 |
| `CMD-UDG-029` | `ADD ICAPSVRBINDISG` | ADD | ICAPSVRBINDISG | 增加ICAP服务器与组绑定 | active | EV-FK-AC-14 |
| `CMD-UDG-030` | `SET CFSRVMODE` | SET | CFSRVMODE | 配置URL过滤业务模式 | active | EV-FK-AC-14 |

### 1.9 URL过滤轨道 — 内容过滤业务（UDG，10个，轨道B核心动作体系）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-031` | `SET APNCFFUNC` | SET | APNCFFUNC | 设置APN内容过滤开关（APN粒度） | active | EV-FK-AC-14 |
| `CMD-UDG-032` | `ADD CFPROFILE` | ADD | CFPROFILE | 增加内容过滤策略 | active | EV-FK-AC-14 |
| `CMD-UDG-033` | `ADD CFTEMPLATE` | ADD | CFTEMPLATE | 增加内容过滤模板（含ACTION=BLOCK/PERMIT/REDIRECT，模板级缺省动作，轨道B核心） | active | EV-FK-AC-14 |
| `CMD-UDG-034` | `SET APNCFTEMPLATE` | SET | APNCFTEMPLATE | 设置APN内容过滤模板绑定 | active | EV-FK-AC-14 |
| `CMD-UDG-035` | `ADD CFPROFBINDCFT` | ADD | CFPROFBINDCFT | 增加内容过滤策略与模板绑定 | active | EV-FK-AC-14 |
| `CMD-UDG-036` | `ADD CONTCATEGROUP` | ADD | CONTCATEGROUP | 增加内容分类组（CATEGORYID） | active | EV-FK-AC-14 |
| `CMD-UDG-037` | `ADD CONTCATEGBIND` | ADD | CONTCATEGBIND | 增加策略与分类组绑定（含ACTION=BLOCK/PERMIT/REDIRECT，分类级精确动作） | active | EV-FK-AC-14 |
| `CMD-UDG-038` | `SET CFCACHEPARA` | SET | CFCACHEPARA | 设置内容过滤缓存参数（减少ICAP交互） | active | EV-FK-AC-14 |
| `CMD-UDG-039` | `SET GLBCFFUNC` | SET | GLBCFFUNC | 设置内容过滤全局开关 | active | EV-FK-AC-14 |
| `CMD-UDG-040` | `ADD CFWHITEURLLST` | ADD | CFWHITEURLLST | 增加URL过滤白名单列表（轨道B白名单机制） | active | EV-FK-AC-14 |
| `CMD-UDG-041` | `ADD CFIPWHITELIST` | ADD | CFIPWHITELIST | 增加内容过滤IP白名单 | active | EV-FK-AC-14 |
| `CMD-UDG-042` | `ADD CFPFSPECACTION` | ADD | CFPFSPECACTION | 增加指定策略特殊场景动作 | active | EV-FK-AC-14 |

### 1.10 PCC规则与策略（UDG，6个，三场景共享）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-043` | `ADD RULE` | ADD | RULE | 增加规则（POLICYTYPE=ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY差异化，双轨道+五子轨决定POLICYNAME指向） | active | EV-FK-AC-04, EV-FK-AC-06, EV-FK-AC-13, EV-CA-AC-01 |
| `CMD-UDG-044` | `ADD USERPROFILE` | ADD | USERPROFILE | 增加用户模板（Portal含CAPMODETHRES captive定时器） | active | EV-FK-AC-10, EV-CA-AC-01 |
| `CMD-UDG-045` | `ADD RULEBINDING` | ADD | RULEBINDING | 增加UserProfile与Rule绑定 | active | EV-CA-AC-01 |
| `CMD-UDG-046` | `ADD PCCPOLICYGRP` | ADD | PCCPOLICYGRP | 增加PCC策略组（绑定URRGROUP；ADC/Portal/WebProxy/URL过滤共用） | active | EV-FK-AC-04, EV-FK-AC-10, EV-FK-AC-11, EV-FK-AC-14 |
| `CMD-UDG-047` | `ADD URR` | ADD | URR | 增加使用量上报规则（ADC/Portal/WebProxy/URL过滤计费属性绑定） | active | EV-FK-AC-04, EV-FK-AC-10, EV-FK-AC-11, EV-FK-AC-14 |
| `CMD-UDG-048` | `ADD URRGROUP` | ADD | URRGROUP | 增加URR组（UPURRNAME1/2/3） | active | EV-FK-AC-04, EV-FK-AC-10, EV-FK-AC-11, EV-FK-AC-14 |

### 1.11 调测验证（UDG，补充命令族）

> 列出关键调测命令（不单独编号入主对象清单，归入LST/DSP/EXP族）；详见 `feature-knowledge/cross-feature-analysis.md` 附录B.1.10。

`LST LICENSESWITCH` / `LST RULE` / `LST RULEBINDING` / `LST USERPROFILE` / `LST FLOWFILTER` / `LST FILTER` / `LST L7FILTER` / `LST HEADEN`（查ANTIFRAUD） / `LST PCCPOLICYGRP` / `LST URRGROUP` / `LST IPFARM` / `LST IPFARMSERVER` / `LST LOGICINF` / `LST SMARTHTTPREDIR` / `LST DNSOVERWRITING` / `LST EXTENDEDFILTER` / `LST CONTCATEGROUP` / `LST ICAPSERVER` / `LST ICAPSVRGRP` / `DSP ICAPSVRSTATUS`（ICAP服务器状态） / `DSP SESSIONINFO`（用户上下文） / `DSP RULECHECK`（WebProxy规则IP版本一致性检查） / `EXP MML`（配置导出）。

---

### 1.12 UNC基础配置（6个，复用PCC骨架）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-001` | `SET LICENSESWITCH` | SET | LICENSESWITCH | License开关，全部UNC访问限制特性前置门控 | active | EV-FK-AC-03, EV-FK-AC-15 |
| `CMD-UNC-002` | `SET PCCFUNC` | SET | PCCFUNC | PCC功能全局设置 | active | EV-FK-AC-03 |
| `CMD-UNC-003` | `SET PCCFAILACTION` | SET | PCCFAILACTION | PCC故障处理策略（CONTINUE/REDIRECT） | active | EV-FK-AC-03 |
| `CMD-UNC-004` | `SET POLICYMODE` | SET | POLICYMODE | 接口模式选择（Gx/N7） | active | EV-FK-AC-03 |
| `CMD-UNC-005` | `SET N7RCVATTRCTRL` | SET | N7RCVATTRCTRL | N7接收属性控制（5G） | active | EV-FK-AC-03 |
| `CMD-UNC-006` | `SET N7SNDATTRCTRL` | SET | N7SNDATTRCTRL | N7发送属性控制（5G） | active | EV-FK-AC-03 |
| `CMD-UNC-007` | `SET FHBYPASS` | SET | FHBYPASS | 紧急旁路 | active | EV-FK-AC-03 |

### 1.13 UNC PCRF管理（4个，三场景共享）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-008` | `ADD PCRF` | ADD | PCRF | PCRF定义（Gx对端或N7 PCF FQDN） | active | EV-FK-AC-03 |
| `CMD-UNC-009` | `ADD PCRFGROUP` | ADD | PCRFGROUP | PCRF组（主备/轮询/百分比/GROUPID+PRIORITY模式） | active | EV-FK-AC-03 |
| `CMD-UNC-010` | `ADD PCRFBINDGRP` | ADD | PCRFBINDGRP | PCRF组绑定 | active | EV-FK-AC-03 |
| `CMD-UNC-011` | `SET DFTGLBPCRFGRP` | SET | DFTGLBPCRFGRP | 缺省全局PCRF组 | active | EV-FK-AC-03 |

### 1.14 UNC规则与用户模板绑定链（6个，三场景共享）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-012` | `ADD RULE` | ADD | RULE | 规则定义（UNC侧POLICYTYPE=BWM/PCC/QOS/ADC，间接被位置触发特性引用） | active | EV-FK-AC-03, EV-FK-AC-15 |
| `CMD-UNC-013` | `ADD USERPROFILE` | ADD | USERPROFILE | 用户模板 | active | EV-FK-AC-03, EV-FK-AC-15 |
| `CMD-UNC-014` | `ADD RULEBINDING` | ADD | RULEBINDING | 规则绑定到UserProfile | active | EV-FK-AC-03 |
| `CMD-UNC-015` | `ADD USRPROFGROUP` | ADD | USRPROFGROUP | 用户模板组（位置触发特性使用） | active | EV-FK-AC-15 |
| `CMD-UNC-016` | `ADD UPBINDUPG` | ADD | UPBINDUPG | 模板绑定到组（含LOCGROUPNAME位置组字段） | active | EV-FK-AC-15 |
| `CMD-UNC-017` | `MOD UPBINDUPG` | MOD | UPBINDUPG | 修改模板绑定（位置触发场景：UPBINDTYPE=SPECIFIC + LOCGROUPNAME） | active | EV-FK-AC-15 |
| `CMD-UNC-018` | `ADD APNUSRPROFG` | ADD | APNUSRPROFG | APN/DNN绑定用户模板组 | active | EV-FK-AC-15 |

### 1.15 UNC 位置触发独有（2个，访问限制UNC侧独有）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | `status` | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UNC-019` | `ADD USRLOCATION` | ADD | USRLOCATION | 增加用户位置（LOCATIONTYPE=CGI/ECGI/NCGI，覆盖2/3G、4G、5G） | active | EV-FK-AC-15 |
| `CMD-UNC-020` | `ADD USRLOCATIONGRP` | ADD | USRLOCATIONGRP | 增加用户位置组（批量绑定USRLOCATION） | active | EV-FK-AC-15 |

> UNC侧 LST 系列调测命令：`LST USRLOCATION` / `LST USRLOCATIONGRP` / `LST UPBINDUPG` / `LST APNUSRPROFG`。

---

## 2. ConfigObject 实例化（41个）

### 2.1 PCC通用规则与用户模板（7个，三场景共享，沿用通用编号）

| `object_id` | `object_name` | 所属功能 | `object_kind` | `identifier_parameters` | `description` | `source_evidence_ids` |
|-------------|---------------|----------|---------------|------------------------|---------------|----------------------|
| `OBJ-RULE` | RULE | PCC规则（访问限制轨道A五子轨载体） | entity | RULENAME, POLICYTYPE | 访问限制场景POLICYTYPE枚举：ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY；POLICYNAME按POLICYTYPE指向不同动作对象（双轨道+五子轨核心） | EV-FK-AC-04, EV-FK-AC-06, EV-FK-AC-13, EV-FK-AC-11 |
| `OBJ-RULEBINDING` | RULEBINDING | 规则绑定 | binding | USERPROFILENAME, RULENAME | links USERPROFILE to RULE | EV-CA-AC-01 |
| `OBJ-USERPROFILE` | USERPROFILE | 用户模板 | composite | USERPROFILENAME | Portal场景含CAPMODETHRES captive周期；访问限制轨道A五子轨共用 | EV-FK-AC-10, EV-CA-AC-01 |
| `OBJ-USRPROFGROUP` | USRPROFGROUP | 用户模板组 | composite | USERPROFGNAME | UNC侧位置触发绑定载体 | EV-FK-AC-15 |
| `OBJ-UPBINDUPG` | UPBINDUPG | 模板绑定 | binding | USERPROFGNAME, USERPROFILENAME | 含LOCGROUPNAME位置组字段（位置触发独有扩展） | EV-FK-AC-15 |
| `OBJ-APNUSRPROFG` | APNUSRPROFG | APN绑定 | binding | APN, USERPROFGNAME | links APN/DNN to USRPROFGROUP | EV-FK-AC-15 |
| `OBJ-PCCPOLICYGRP` | PCCPOLICYGRP | PCC策略组 | composite | PCCPOLICYGRPNM, URRGROUPNAME | contains URRGROUP；ADC/Portal/WebProxy/URL过滤共用（URL过滤仅作匹配触发，动作不走此对象） | EV-FK-AC-04, EV-FK-AC-10, EV-FK-AC-14 |

### 2.2 流过滤（6个，三场景共享）

| `object_id` | `object_name` | 所属功能 | `object_kind` | `identifier_parameters` | `description` | `source_evidence_ids` |
|-------------|---------------|----------|---------------|------------------------|---------------|----------------------|
| `OBJ-FLOWFILTER` | FLOWFILTER | 流过滤器 | composite | FLOWFILTERNAME | contains FILTER, L7FILTER；11独有特性共用 | EV-CA-AC-01 |
| `OBJ-FLOWFILTERGRP` | FLOWFILTERGRP | 流过滤组（OR关系） | composite | FILTERGRPNAME | contains FLOWFILTER；多条件OR匹配 | EV-CA-AC-01 |
| `OBJ-FILTER` | FILTER | L3/L4过滤 | entity | FILTERNAME, L34PROTTYPE, L34PROTOCOL, SRCIP, DSTIP | belongs_to FLOWFILTER；UDG独有 | EV-CA-AC-01 |
| `OBJ-L7FILTER` | L7FILTER | L7过滤 | entity | L7FILTERNAME, SUBL7FLTNAME, URL, METHODTYPE | belongs_to FLOWFILTER；ADC/头增强族/Portal/防欺诈使用 | EV-FK-AC-04, EV-FK-AC-06, EV-FK-AC-10 |
| `OBJ-FLTBINDFLOWF` | FLTBINDFLOWF | 过滤器绑定 | binding | FLOWFILTERNAME, FILTERNAME | links FILTER to FLOWFILTER | EV-CA-AC-01 |
| `OBJ-PROTBINDFLOWF` | PROTBINDFLOWF | 协议绑定 | binding | FLOWFILTERNAME, PROTOCOLNAME, L7FILTERNAME | links L7FILTER+协议 to FLOWFILTER | EV-FK-AC-04, EV-FK-AC-06 |

### 2.3 三四层/多维扩展（2个，重定向族独有）

| `object_id` | `object_name` | 所属功能 | `object_kind` | `identifier_parameters` | `description` | `source_evidence_ids` |
|-------------|---------------|----------|---------------|------------------------|---------------|----------------------|
| `OBJ-AC-EXTENDEDFILTER` | EXTENDEDFILTER | 扩展过滤器（多维） | entity | EXTFLTNAME, URL, USERAGENT, CONTENTTYPE, URLPOSTFIX | HTTP智能重定向+DNS纠错共用；多维匹配（URL/UA/ContentType/ERRORCODE） | EV-FK-AC-12, EV-FK-AC-13 |
| `OBJ-AC-ERRORCODE` | ERRORCODE | 错误码范围 | entity | ERRORCODENAME, ERRORCODEOP(GT/EQUAL), ERRORCODESTART | HTTP错误码GT 400 / DNS错误码EQUAL 3 (NXDOMAIN)；SMARTREDIRECT轨道触发条件 | EV-FK-AC-12, EV-FK-AC-13 |

### 2.4 计费属性（2个，三场景共享）

| `object_id` | `object_name` | 所属功能 | `object_kind` | `identifier_parameters` | `description` | `source_evidence_ids` |
|-------------|---------------|----------|---------------|------------------------|---------------|----------------------|
| `OBJ-URR` | URR | 使用量上报规则 | entity | URRNAME, URRID, USAGERPTMODE | 访问限制场景用于ADC/Portal/WebProxy/URL过滤的计费属性绑定（非FUP降速主用途） | EV-FK-AC-04, EV-FK-AC-10, EV-FK-AC-14 |
| `OBJ-URRGROUP` | URRGROUP | URR组 | composite | URRGROUPNAME, UPURRNAME1/2/3 | contains URR；belongs_to PCCPOLICYGRP | EV-FK-AC-04, EV-FK-AC-14 |

### 2.5 ADC与业务分类（2个，跨场景共享）

| `object_id` | `object_name` | 所属功能 | `object_kind` | `identifier_parameters` | `description` | `source_evidence_ids` |
|-------------|---------------|----------|---------------|------------------------|---------------|----------------------|
| `OBJ-ADCPARA` | ADCPARA | ADC参数 | entity | FLOWFILTERNAME, FLOWINFORPT, ADCHYSTTIMER | ADC流信息上报+迟滞定时器；ADC独有 | EV-FK-AC-04 |
| `OBJ-CATEGORYPROP` | CATEGORYPROP | 业务分类 | entity | CATEGORYPROPNAME, CATEGORYID | 三场景共享业务分类定义 | EV-FK-AC-01, EV-CA-AC-01 |

### 2.6 头增强轨道（HEADEN族，1个，访问限制独有）

| `object_id` | `object_name` | 所属功能 | `object_kind` | `identifier_parameters` | `description` | `source_evidence_ids` |
|-------------|---------------|----------|---------------|------------------------|---------------|----------------------|
| `OBJ-AC-HEADEN` | HEADEN | 头增强对象（跨协议复用） | entity | HEADERENNAME, DATATYPE(IMSI1/MSISDN1/IMEI1), PREFIXNAME, ENCRYALGORI, PSWDKEY, ANTIFRAUD(ENABLE/DISABLE), GRAYLIST(ENABLE/DISABLE) | 跨4特性复用（HTTP/HTTPS/RTSP头增强+头防欺诈）；variant_dimensions含protocol_type；防欺诈内嵌为前置检测层（非独立动作） | EV-FK-AC-06, EV-FK-AC-07, EV-FK-AC-08, EV-FK-AC-09 |

### 2.7 SMARTREDIRECT轨道（3个，访问限制独有）

| `object_id` | `object_name` | 所属功能 | `object_kind` | `identifier_parameters` | `description` | `source_evidence_ids` |
|-------------|---------------|----------|---------------|------------------------|---------------|----------------------|
| `OBJ-AC-SMARTHTTPREDIR` | SMARTHTTPREDIR | HTTP智能重定向动作策略 | entity | SMTHTTPREDINAME, SERVERURL, EXTFLTNAME1/2, APPENDINFONAME, BINDErrCODENAME | RULE.POLICYTYPE=SMARTREDIRECT + POLICYNAME指向此对象 → L7 HTTP响应改写 | EV-FK-AC-13 |
| `OBJ-AC-REDIRAPPENDINFO` | REDIRAPPENDINFO | 重定向携带信息 | entity | APPENDINFONAME, REQURLFLAG, IMSIFLAG, IMEIFLAG | 携带MSISDN/IMSI/IMEI；HTTP智能重定向独有 | EV-FK-AC-13 |
| `OBJ-AC-DNSOVERWRITING` | DNSOVERWRITING | DNS重写动作 | entity | DNSOVERWRTNAME, EXTFLTNAME1, SERVERIP1, BINDERRCODENAME | 含Platform IP；RULE.POLICYTYPE=SMARTREDIRECT + POLICYNAME指向此对象 → DNS响应改写（与HTTP重定向共用POLICYTYPE，区分点在POLICYNAME指向） | EV-FK-AC-12 |

### 2.8 WEBPROXY/Portal轨道（5个，访问限制独有）

| `object_id` | `object_name` | 所属功能 | `object_kind` | `identifier_parameters` | `description` | `source_evidence_ids` |
|-------------|---------------|----------|---------------|------------------------|---------------|----------------------|
| `OBJ-AC-IPFARMGLOBAL` | IPFARMGLOBAL | IPFarm全局参数 | entity | SERVERTYPE, LBMETHOD(ROUND_ROBIN/LEAST_RECENTLY_USED/LEAST_LOAD), TIMETHRESHOLD, HEALTHSUCCLIMIT, HEALTHFAILLIMIT | Portal+WebProxy共用；整机级负荷分担+心跳阈值 | EV-FK-AC-10, EV-FK-AC-11 |
| `OBJ-AC-IPFARM` | IPFARM | 重定向服务器集群 | composite | IPFARMNAME, IPVERSION, INTERFACENAME, HEALTHCHECKFLAG | contains IPFARMSERVER；RULE.POLICYTYPE=WEBPROXY + POLICYNAME指向此对象 → L3 IP NAT；整机64个，每个512 IP | EV-FK-AC-10, EV-FK-AC-11 |
| `OBJ-AC-IPFARMSERVER` | IPFARMSERVER | IPFarm服务器 | entity | IPFARMNAME, SERVERIPV4/SERVERIPV6 | belongs_to IPFARM；Portal全DOWN时DEFAULTACT=BLOCK | EV-FK-AC-10, EV-FK-AC-11 |
| `OBJ-AC-LOGICINF` | LOGICINF | 逻辑接口 | entity | NAME, IPVERSION, IPV4ADDRESS1, IPV4MASK1, VPNINSTANCE | 心跳检测（Portal/WebProxy）+ ICAP互通（URL过滤）共用；不同IPFarm必须用不同接口 | EV-FK-AC-10, EV-FK-AC-11, EV-FK-AC-14 |
| `OBJ-AC-BLACKLISTRULE` | BLACKLISTRULE | 黑名单规则 | entity | (WebProxy独有) | WebProxy黑名单匹配 | EV-FK-AC-11 |

### 2.9 URL过滤轨道 — ICAP互通前置（5个，访问限制独有，轨道B独立资源层）

| `object_id` | `object_name` | 所属功能 | `object_kind` | `identifier_parameters` | `description` | `source_evidence_ids` |
|-------------|---------------|----------|---------------|------------------------|---------------|----------------------|
| `OBJ-AC-VPNINST` | VPNINST | VPN实例 | entity | VPNINSTANCE | ICAP互通专网（URL过滤独有） | EV-FK-AC-14 |
| `OBJ-AC-ICAPSERVER` | ICAPSERVER | ICAP服务器 | entity | ICAPSERVERNAME, ICAPSERVERTYPE(URL_FILTERING), ICAPSVRIPTYPE, ICAPSERVERIPV4, VPNINSTANCE | 轨道B必需外部依赖；URL分类数据库提供方 | EV-FK-AC-14 |
| `OBJ-AC-ICAPLOCALINFO` | ICAPLOCALINFO | ICAP本端信息 | entity | ICAPSERVERTYPE, USERAGENT | UDG侧ICAP本端标识 | EV-FK-AC-14 |
| `OBJ-AC-ICAPSVRGRP` | ICAPSVRGRP | ICAP服务器组 | composite | ICAPSVRGRPNAME, ICAPSERVERTYPE | contains ICAPSERVER | EV-FK-AC-14 |
| `OBJ-AC-ICAPSVRBINDISG` | ICAPSVRBINDISG | ICAP服务器与组绑定 | binding | ICAPSVRGRPNAME, ICAPSERVERNAME | links ICAPSERVER to ICAPSVRGRP | EV-FK-AC-14 |

### 2.10 URL过滤轨道 — 内容过滤业务（5个+绑定，访问限制独有，轨道B核心动作体系）

| `object_id` | `object_name` | 所属功能 | `object_kind` | `identifier_parameters` | `description` | `source_evidence_ids` |
|-------------|---------------|----------|---------------|------------------------|---------------|----------------------|
| `OBJ-AC-CFPROFILE` | CFPROFILE | 内容过滤策略 | entity | CFPROFILENAME | 轨道B策略载体；与CONTCATEGBIND共同决定分类级动作 | EV-FK-AC-14 |
| `OBJ-AC-CFTEMPLATE` | CFTEMPLATE | 内容过滤模板 | entity | CFTEMPLATENAME, ICAPSRVGMNAME, ACTION(BLOCK/PERMIT/REDIRECT) | **模板级缺省动作**（轨道B核心对象之一）；RULE不引用此对象，独立于RULE体系 | EV-FK-AC-14 |
| `OBJ-AC-APNCFTEMPLATE` | APNCFTEMPLATE | APN-模板绑定 | binding | APNNAME, CFTEMPLATENAME | links APN to CFTEMPLATE | EV-FK-AC-14 |
| `OBJ-AC-CFPROFBINDCFT` | CFPROFBINDCFT | 策略-模板绑定 | binding | CFTEMPLATENAME, CFPROFILENAME | links CFPROFILE to CFTEMPLATE | EV-FK-AC-14 |
| `OBJ-AC-CONTCATEGROUP` | CONTCATEGROUP | 内容分类组 | entity | CONTCATEGNAME, CATEGORYTYPE(SPECIFIC), CATEGORYID | URL分类ID集合（来自ICAP Server） | EV-FK-AC-14 |
| `OBJ-AC-CONTCATEGBIND` | CONTCATEGBIND | 策略与分类组绑定 | entity | CFPROFILENAME, CONTCATEGNAME, ACTION(BLOCK/PERMIT/REDIRECT) | **分类级精确动作**（轨道B核心对象之一，覆盖CFTEMPLATE模板级缺省） | EV-FK-AC-14 |

### 2.11 接入控制触发（2个，访问限制UNC侧独有）

| `object_id` | `object_name` | 所属功能 | `object_kind` | `identifier_parameters` | `description` | `source_evidence_ids` |
|-------------|---------------|----------|---------------|------------------------|---------------|----------------------|
| `OBJ-AC-USRLOCATION` | USRLOCATION | 用户位置 | entity | LOCATIONNAME, LOCATIONTYPE(CGI/ECGI/NCGI), MCC, MNC, LAC/ECI/NCI | UNC侧位置匹配；覆盖2/3G(CGI)、4G(ECGI)、5G(NCGI) | EV-FK-AC-15 |
| `OBJ-AC-USRLOCATIONGRP` | USRLOCATIONGRP | 用户位置组 | composite | LOCGROUPNAME, LOCATIONNAME | contains USRLOCATION；UPBINDUPG引用此组实现位置触发 | EV-FK-AC-15 |

### 2.12 辅助对象（1个）

| `object_id` | `object_name` | 所属功能 | `object_kind` | `identifier_parameters` | `description` | `source_evidence_ids` |
|-------------|---------------|----------|---------------|------------------------|---------------|----------------------|
| `OBJ-AC-WELLKNOWNPORT` | WELLKNOWNPORT | 知名端口 | entity | IDENPROTNAME, PROTOCOLNAME, PORTOP(EQUAL), STARTPORT, PRIORITY | 头防欺诈识别HTTP端口80/8080 | EV-FK-AC-09 |

---

## 3. ConfigObject 间关系边（contains / refers_to / depends_on / conflicts_with / activates）

> **Schema参考**：§11.7 `ConfigObject contains/refers_to/depends_on/conflicts_with/composed_by/activates ConfigObject`。

### 3.1 通用结构边（三场景共享，沿用带宽场景）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| USERPROFILE | `contains` | RULE | 通过RULEBINDING（含Portal captive绑定） |
| USRPROFGROUP | `contains` | USERPROFILE | 通过UPBINDUPG（含LOCGROUPNAME扩展） |
| PCCPOLICYGRP | `contains` | URRGROUP | PCC策略组包含URR组（ADC/Portal/WebProxy/URL过滤计费属性链） |
| URRGROUP | `contains` | URR | UPURRNAME1/2/3 |
| RULE | `contains` | FLOWFILTER | 规则引用流过滤器（FILTERINGMODE=FLOWFILTER） |
| FLOWFILTER | `contains` | FILTER | 通过FLTBINDFLOWF |
| FLOWFILTER | `contains` | L7FILTER | 通过PROTBINDFLOWF（含协议绑定） |
| FLOWFILTERGRP | `contains` | FLOWFILTER | OR关系组合（多条件OR） |
| RULE | `refers_to` | PCCPOLICYGRP | POLICYTYPE=PCC时POLICYNAME指向（ADC/Portal/WebProxy计费/URL过滤触发） |

### 3.2 ★ 动作轨道A — PCC体系（POLICYTYPE=PCC）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| RULE(POLICYTYPE=PCC) | `refers_to` | PCCPOLICYGRP | POLICYNAME指向PCCPOLICYGRP；ADC/Portal/WebProxy计费规则/URL过滤触发共用 |
| RULE(POLICYTYPE=ADC) | `depends_on` | ADCPARA | ADC规则依赖ADC参数（FLOWINFORPT+ADCHYSTTIMER） |
| PCCPOLICYGRP | `contains` | URRGROUP | （同3.1，轨道A计费属性链） |

### 3.3 ★ 动作轨道D — HEADEN族（POLICYTYPE=HEADEN）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| RULE(POLICYTYPE=HEADEN) | `refers_to` | HEADEN | POLICYNAME指向HEADEN对象名（HTTP/HTTPS/RTSP头增强+头防欺诈共用） |
| HEADEN | `activates` | (头防欺诈检测) | ANTIFRAUD=ENABLE时内嵌防欺诈前置检测；非独立对象（内嵌于HEADEN） |
| HEADEN(ANTIFRAUD=ENABLE) | `depends_on` | HEADEN(头增强主特性) | **强耦合**：启用防欺诈必须开启头增强（License 82209786 + 82209777 双开） |
| HEADEN | `conflicts_with` | (RTSP协议) | 头防欺诈仅支持HTTP/HTTPS，RTSP头增强不支持防欺诈（族内唯一例外） |

### 3.4 ★ 动作轨道C — SMARTREDIRECT（POLICYTYPE=SMARTREDIRECT，HTTP重定向+DNS纠错共用）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| RULE(POLICYTYPE=SMARTREDIRECT) | `refers_to` | SMARTHTTPREDIR | POLICYNAME指向SMARTHTTPREDIR → L7 HTTP响应改写（HTTP智能重定向） |
| RULE(POLICYTYPE=SMARTREDIRECT) | `refers_to` | DNSOVERWRITING | POLICYNAME指向DNSOVERWRITING → DNS响应改写（DNS纠错）；与HTTP重定向共用POLICYTYPE，区分点在POLICYNAME指向 |
| SMARTHTTPREDIR | `contains` | (EXTENDEDFILTER引用) | EXTFLTTYPE1/2 + EXTFLTNAME1/2（多维AND组合） |
| SMARTHTTPREDIR | `contains` | (ERRORCODE引用) | BINDErrCODENAME（HTTP错误码GT 400触发） |
| SMARTHTTPREDIR | `refers_to` | REDIRAPPENDINFO | APPENDINFONAME（携带MSISDN/IMSI/IMEI） |
| DNSOVERWRITING | `contains` | (EXTENDEDFILTER引用) | EXTFLTTYPE1 + EXTFLTNAME1（域名匹配） |
| DNSOVERWRITING | `contains` | (ERRORCODE引用) | BINDERRCODENAME（DNS错误码EQUAL 3 NXDOMAIN触发） |
| SMARTHTTPREDIR | `conflicts_with` | (HTTPS/HTTP2.0协议) | 加密协议不支持HTTP重定向（加密盲区） |

### 3.5 ★ 轨道A WEBPROXY子轨 — WEBPROXY/Portal（POLICYTYPE=WEBPROXY + Portal captive）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| RULE(POLICYTYPE=WEBPROXY) | `refers_to` | IPFARM | POLICYNAME指向IPFARM对象名 → L3 IP NAT重定向到Proxy（WebProxy独有） |
| IPFARM | `contains` | IPFARMSERVER | IPFarm包含多台服务器（整机64 Farm × 512 IP） |
| IPFARM | `depends_on` | LOGICINF | 心跳检测接口（不同IPFarm必须用不同接口） |
| IPFARMGLOBAL | `activates` | IPFARM | 全局LBMETHOD/心跳阈值约束（激活）所有IPFarm实例（★ P5 修复 U-M-10：原 `governs` 非 Schema §11.7 合法 ConfigObject 间关系，改为 `activates`） |
| USERPROFILE(CAPMODETHRES) | `activates` | (Portal captive周期) | Portal captive配置在USERPROFILE（非RULE）；与RULE.POLICYTYPE=PCC协同 |
| IPFARM(Portal全DOWN) | `activates` | (DEFAULTACT=BLOCK) | Portal场景IPFarm全DOWN时缺省动作=BLOCK（兜底阻塞） |
| IPFARM(POLICYTYPE=WEBPROXY) | `contains` | BLACKLISTRULE | WebProxy黑名单规则归属于 IPFARM 体系（★ P5 修复 U-M-11：原 `belongs_to` 非 Schema 合法关系，反向改为 `IPFARM contains BLACKLISTRULE`） |

### 3.6 ★ 轨道B — URL过滤体系（独立动作，CFTEMPLATE/CONTCATEGBIND.ACTION驱动）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| ICAPSVRGRP | `contains` | ICAPSERVER | 通过ICAPSVRBINDISG |
| ICAPSERVER | `depends_on` | VPNINST | ICAP互通专网 |
| ICAPSERVER | `depends_on` | LOGICINF | ICAP互通接口（与Portal/WebProxy心跳检测共用LOGICINF对象类） |
| ICAPSVRGRP | `refers_to` | CFTEMPLATE | CFTEMPLATE.ICAPSRVGMNAME指向ICAP服务器组（模板级动作关联ICAP） |
| CFTEMPLATE | `composed_by` | (CFPROFILE via CFPROFBINDCFT) | 模板与策略绑定 |
| CONTCATEGBIND | `refers_to` | CONTCATEGROUP | 分类级动作绑定到内容分类组（CATEGORYID） |
| CONTCATEGBIND | `refers_to` | CFPROFILE | 分类级动作归属策略（覆盖CFTEMPLATE模板级缺省动作） |
| CFTEMPLATE | `refers_to` | APNCFTEMPLATE | APN级模板绑定 |
| RULE(POLICYTYPE=PCC, URL过滤触发) | `activates` | CFTEMPLATE/CONTCATEGBIND | URL过滤RULE用POLICYTYPE=PCC仅作匹配触发，**实际动作不走PCCPOLICYGRP**，而走CFTEMPLATE/CONTCATEGBIND（轨道A→B混合，建模难点） |
| CFTEMPLATE(ACTION=PERMIT) | `activates` | (独立白名单放行) | 轨道B独有PERMIT（★ P5 修复 U-M-11：原 "(独立白名单机制)" 括号说明非 Schema 关系名，改为 `CFTEMPLATE(ACTION=PERMIT) activates (独立白名单放行)`） |

### 3.7 接入控制触发边（UNC侧）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| USRLOCATIONGRP | `contains` | USRLOCATION | 位置组批量绑定位置（CGI/ECGI/NCGI） |
| UPBINDUPG | `refers_to` | USRLOCATIONGRP | LOCGROUPNAME字段引用位置组（位置触发核心边） |
| APNUSRPROFG | `refers_to` | USRPROFGROUP | APN/DNN绑定用户模板组 |
| USRLOCATION(三网元一致) | `conflicts_with` | (跨网元ULI不一致) | 位置信息CGI/ECGI/NCGI取值需UNC+RAN+PCRF/PCF三处一致 |

### 3.8 跨轨道协议盲区互斥（访问限制场景特有）

> **★ P5 修复说明（U-M-11/U-M-12）**：P5 前本表使用 `(协议友好)` 括号说明，非 Schema §11.7 合法关系名。P5 将其归为说明性注释（不计入 §9 合法边计数），合法 `conflicts_with` 边保留。

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| RULE(POLICYTYPE=HEADEN, HTTP头增强) | `conflicts_with` | (HTTPS/HTTP2.0协议) | HTTP头增强仅支持HTTP1.x（加密盲区） |
| 用户Portal | `conflicts_with` | (HTTPS/HTTP2.0协议) | 加密无法改写HTTP响应 |
| RULE(POLICYTYPE=SMARTREDIRECT, HTTP重定向) | `conflicts_with` | (HTTPS/HTTP2.0协议) | 加密无法获取HTTP响应特征 |
| RULE(POLICYTYPE=WEBPROXY) | _（说明：协议友好，非 Schema 边）_ | HTTPS/HTTP2.0 支持 | WebProxy在L3工作，不受加密影响（IP NAT）——非关系边，归说明性注释 |
| HEADEN(HTTPS头增强, SSL Extension) | _（说明：协议友好，非 Schema 边）_ | HTTPS 部分支持 | HTTPS头增强通过SSL Extension TLV格式部分支持HTTPS——非关系边，归说明性注释 |

---

## 4. CommandRule（14条）

> **Schema参考**：§11.6。`governed_by`（反向）：MMLCommand governed_by CommandRule；CommandRule governs MMLCommand/CommandParameter/ConfigObject。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `scope_type` | `scope_ref` | `rule_logic` | `violation_effect` | `severity` | `source_evidence_ids` |
|-----------|-------------|-------------|----------------------|-------------------|-------------|------------|--------------|-------------------|------------|----------------------|
| `CR-AC-01` | RULENAME跨POLICYTYPE不冲突 | `object_reference_rule` | explicit | restriction | object | OBJ-RULE | PCC类型RULENAME值与HEADEN类型RULENAME值不能同名；访问限制场景POLICYTYPE枚举ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY间RULENAME互斥；同名规则可存在于不同POLICYTYPE（如一个HEADEN、一个PCC） | 规则名冲突导致策略覆盖或下发失败 | critical | EV-CA-AC-01, EV-FK-AC-06 |
| `CR-AC-02` | POLICYTYPE决定动作对象链（★双轨道+五子轨核心） | `parameter_dependency` | explicit | config | parameter | ADD RULE.POLICYTYPE | POLICYTYPE=ADC→直接在RULE上(FLOWFILTER)；POLICYTYPE=PCC→POLICYNAME引用PCCPOLICYGRP；POLICYTYPE=HEADEN→POLICYNAME引用HEADEN；POLICYTYPE=SMARTREDIRECT→POLICYNAME引用SMARTHTTPREDIR/DNSOVERWRITING；POLICYTYPE=WEBPROXY→POLICYNAME引用IPFARM；URL过滤RULE虽用POLICYTYPE=PCC但动作不走PCCPOLICYGRP而走CFTEMPLATE/CONTCATEGBIND | POLICYNAME指向错误对象类型导致动作失效 | critical | EV-FK-AC-06, EV-FK-AC-13, EV-FK-AC-11, EV-FK-AC-14 |
| `CR-AC-03` | SMARTREDIRECT两特性共用POLICYTYPE | `semantic_rule` | explicit | config | parameter | ADD RULE.POLICYNAME | POLICYTYPE=SMARTREDIRECT时POLICYNAME指向SMARTHTTPREDIR对象=HTTP智能重定向；指向DNSOVERWRITING对象=DNS纠错；两特性共用同一POLICYTYPE，区分点仅在POLICYNAME指向的对象类型 | POLICYNAME指向错误导致重定向类型错乱 | warning | EV-FK-AC-12, EV-FK-AC-13 |
| `CR-AC-04` | 头防欺诈强依赖头增强（License强耦合） | `precondition_rule` | explicit | restriction | object | OBJ-AC-HEADEN | 启用HTTP头防欺诈（License 82209786）必须同时开启HTTP头增强（License 82209777）；防欺诈通过ADD HEADEN的ANTIFRAUD=ENABLE参数内嵌，不独立产生动作；RTSP头增强不支持防欺诈（族内唯一例外） | 防欺诈独立配置无法生效；RTSP场景防欺诈盲区 | critical | EV-FK-AC-09, EV-FK-AC-06 |
| `CR-AC-05` | ICAP Server必需（URL过滤前置） | `precondition_rule` | explicit | config | object | OBJ-AC-ICAPSERVER | URL过滤（GWFD-110471）启用前必须配置ICAP Server互通链路：VPNINST → LOGICINF → ICAPSERVER → ICAPLOCALINFO → ICAPSVRGRP → ICAPSVRBINDISG；ICAP Server不可用时URL过滤功能失效 | URL过滤无外部分类源，BLOCK/PERMIT/REDIRECT动作均无法执行 | critical | EV-FK-AC-14 |
| `CR-AC-06` | URL过滤PERMIT动作唯一性 | `semantic_rule` | explicit | design | object | OBJ-AC-CFTEMPLATE | 访问限制场景14特性中仅URL过滤（轨道B）显式支持PERMIT（CFTEMPLATE.ACTION=PERMIT 或 CONTCATEGBIND.ACTION=PERMIT）；轨道A的特性"放行"是隐式的（不匹配=放行），无法在策略中显式声明PERMIT | 白名单机制仅在轨道B可用，轨道A场景下显式PERMIT配置无效 | critical | EV-FK-AC-14 |
| `CR-AC-07` | FLOWFILTER必须绑定FILTER | `precondition_rule` | explicit | config | object | OBJ-FLOWFILTER | FLOWFILTER必须通过FLTBINDFLOWF绑定至少一个FILTER才能生效；URL过滤场景还需绑定L7FILTER（通过PROTBINDFLOWF）匹配URL | FLOWFILTER空引用导致规则匹配失败 | critical | EV-CA-AC-01 |
| `CR-AC-08` | RULE必须引用已存在的对象 | `object_reference_rule` | explicit | restriction | object | OBJ-RULE | ADD RULE时POLICYNAME必须引用已存在的PCCPOLICYGRP/HEADEN/SMARTHTTPREDIR/DNSOVERWRITING/IPFARM对象；FLOWFILTERNAME必须引用已存在的FLOWFILTER；先建被引用对象，再建RULE | 引用不存在的对象导致规则下发失败 | critical | EV-CA-AC-01, EV-FK-AC-13 |
| `CR-AC-09` | 预定义规则名三网元一致 | `semantic_rule` | explicit | config | parameter | ADD RULE.RULENAME | 动态PCC场景中RULENAME必须在PCRF/PCF、UNC、UDG三处保持一致；ADC场景FLOWFILTERNAME/appid也需三网元一致；URL过滤的Category ID需UDG+ICAP Server+PCRF/PCF一致；位置触发的CGI/ECGI/NCGI需UNC+RAN+PCRF/PCF一致 | 跨网元规则名不一致导致策略无法匹配，访问限制失效 | critical | EV-FK-AC-04, EV-FK-AC-03, EV-FK-AC-15, EV-FK-AC-14 |
| `CR-AC-10` | HTTPS/HTTP2.0加密协议盲区 | `parameter_mutex` | explicit | restriction | object | OBJ-RULE (POLICYTYPE=HEADEN/SMARTREDIRECT, Portal) | HTTP智能重定向/用户Portal/HTTP头增强不支持HTTPS/HTTP2.0（加密无法解析HTTP内容）；HTTPS头增强通过SSL Extension部分支持HTTPS；WebProxy在L3工作支持HTTPS/HTTP2.0；URL过滤HTTPS场景仅能基于SNI（不能解析完整URL） | 加密场景配置L7动作特性无效；需改用WebProxy/URL过滤SNI/HTTPS头增强 | warning | EV-FK-AC-06, EV-FK-AC-13, EV-FK-AC-10, EV-FK-AC-08 |
| `CR-AC-11` | RTSP不支持头防欺诈 | `parameter_mutex` | explicit | restriction | object | OBJ-AC-HEADEN (RTSP场景) | 头防欺诈仅支持HTTP/HTTPS，RTSP头增强（GWFD-110262）不支持防欺诈；族内唯一例外；RTSP场景需Streaming Server自身认证弥补盲区 | RTSP场景防欺诈配置无效 | warning | EV-FK-AC-07, EV-FK-AC-09 |
| `CR-AC-12` | 配置变更后必须SET REFRESHSRV | `runtime_check_rule` | explicit | ops | command | CMD-UDG-002 | FILTER/L7FILTER/FLOWFILTER/RULE等变更后必须执行SET REFRESHSRV:REFRESHTYPE=ALL/USERPROFILE才能生效；REFRESHTYPE=ALL全量刷新，REFRESHTYPE=USERPROFILE用户模板级刷新（粒度较细） | 配置不生效或部分生效 | info | EV-FK-AC-04, EV-FK-AC-06, EV-FK-AC-14 |
| `CR-AC-13` | REFRESHSRV后60秒禁改Filter | `runtime_check_rule` | explicit | ops | command | CMD-UDG-002 | SET REFRESHSRV后约60秒（PROTBINDFLOWF定时器）策略才完全下发到转发面；此窗口期内修改FILTER/L7FILTER可能导致策略不一致；REFRESHSRV必须是最后执行的命令 | 策略下发不完整或状态不一致 | warning | EV-FK-AC-01, EV-FK-AC-02, EV-CA-AC-01 |
| `CR-AC-14` | 双轨可并存（轨道A + 轨道B） | `semantic_rule` | explicit | design | object | OBJ-RULE + OBJ-AC-CFTEMPLATE | 同一用户业务流可先后被轨道A（PCC体系）和轨道B（URL过滤体系）检查；轨道A处理ADC/头增强/重定向，轨道B处理URL分类过滤；最终动作取决于配置优先级和规则匹配顺序；双轨优先级需查参考信息或现网验证 | 双轨动作冲突时执行结果不确定（已知建模难点） | info | EV-FK-AC-14, EV-CA-AC-01 |

---

## 5. MMLCommand 关键参数集（访问限制场景特有）

### 5.1 ADD RULE（PCC规则核心命令，访问限制轨道A五子轨）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| RULENAME | string | — | 规则名，跨网元一致（CR-AC-01, CR-AC-09） |
| POLICYTYPE | enum | ADC / PCC / HEADEN / SMARTREDIRECT / WEBPROXY | **双轨道+五子轨决定POLICYNAME指向**（CR-AC-02） |
| PRIORITY | int | 0-65535 | 优先级（数字越小越高） |
| FILTERINGMODE | enum | FLOWFILTER | 过滤模式 |
| FLOWFILTERNAME | string | — | 引用FLOWFILTER（CR-AC-07, CR-AC-08） |
| POLICYNAME | string | — | 按POLICYTYPE引用不同对象：ADC=空/PCC=PCCPOLICYGRP/HEADEN=HEADEN对象/SMARTREDIRECT=SMARTHTTPREDIR或DNSOVERWRITING/WEBPROXY=IPFARM（CR-AC-02, CR-AC-03） |
| ADCMUTEFLAG | enum | ENABLE / DISABLE | ADC规则静默上报开关（POLICYTYPE=ADC时使用） |

### 5.2 ADD HEADEN（头增强核心命令，跨4特性复用）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| HEADERENNAME | string | — | 头增强对象名 |
| DATATYPE | enum | IMSI1 / MSISDN1 / IMEI1 等 | 插入的用户信息字段类型 |
| PREFIXNAME | string | — | 字段前缀名（建议非HTTP标准头，如X-msisdn/X-imsi，避免防欺诈失败） |
| ENCRYALGORI | enum | MD5 / RC4 / AES128 / AES256 / RSA1024 / RSA2048 / SHA256 | 加密算法（HTTPS头增强无RSA） |
| PSWDKEY / PSWDKEYCONFIRM | string | — | 密钥（两字段必须一致） |
| ANTIFRAUD | enum | ENABLE / DISABLE | **使能HTTP头防欺诈**（内嵌前置检测；CR-AC-04） |
| GRAYLIST | enum | ENABLE / DISABLE | 灰名单模式（跳过头增强插入） |

### 5.3 ADD SMARTHTTPREDIR（HTTP智能重定向核心命令）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| SMTHTTPREDINAME | string | — | HTTP智能重定向动作策略名（RULE.POLICYNAME指向此） |
| SERVERURL | string | — | 重定向目标URL |
| EXTFLTTYPE1/2 | enum | AND / OR | 扩展过滤器组合逻辑 |
| EXTFLTNAME1/2 | string | — | 引用EXTENDEDFILTER（URL/UserAgent/ContentType多维） |
| APPENDINFONAME | string | — | 引用REDIRAPPENDINFO（携带MSISDN/IMSI/IMEI） |
| BINDErrCODENAME | string | — | 引用ERRORCODE（HTTP错误码GT 400触发） |

### 5.4 ADD DNSOVERWRITING（DNS纠错核心命令）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| DNSOVERWRTNAME | string | — | DNS重写动作名（RULE.POLICYNAME指向此，与SMARTHTTPREDIR共用POLICYTYPE=SMARTREDIRECT） |
| EXTFLTTYPE1 | enum | AND | 扩展过滤器逻辑 |
| EXTFLTNAME1 | string | — | 引用EXTENDEDFILTER（错误域名匹配） |
| SERVERIP1 | string | IP | 第三方Platform IP（DNS响应改写目标） |
| BINDERRCODENAME | string | — | 引用ERRORCODE（DNS错误码EQUAL 3 NXDOMAIN触发） |

### 5.5 ADD IPFARM / SET IPFARMGLOBAL（重定向服务器集群核心命令）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| IPFARMNAME | string | — | IPFarm名（RULE.POLICYTYPE=WEBPROXY时POLICYNAME指向此） |
| LBMETHOD | enum | ROUND_ROBIN / LEAST_RECENTLY_USED / LEAST_LOAD | 负荷分担方式（默认LEAST_LOAD） |
| HEALTHSUCCLIMIT | int | — | 心跳成功阈值（UP↔DOWN切换） |
| HEALTHFAILLIMIT | int | — | 心跳失败阈值 |
| INTERFACENAME | string | — | 心跳检测接口（不同IPFarm必须用不同接口） |
| HEALTHCHECKFLAG | enum | ENABLE / DISABLE | 心跳检测开关 |
| DEFAULTACT | enum | BLOCK / (放行) | Portal全DOWN时缺省动作=BLOCK（兜底阻塞） |

### 5.6 ADD CFTEMPLATE / ADD CONTCATEGBIND（URL过滤核心命令，轨道B）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| CFTEMPLATENAME | string | — | 内容过滤模板名 |
| ICAPSRVGMNAME | string | — | 引用ICAPSVRGRP（模板关联ICAP） |
| ACTION (CFTEMPLATE) | enum | BLOCK / PERMIT / REDIRECT | **模板级缺省动作**（CR-AC-06，PERMIT仅轨道B） |
| CFPROFILENAME | string | — | 引用CFPROFILE（策略载体） |
| CONTCATEGNAME | string | — | 引用CONTCATEGROUP（分类组） |
| ACTION (CONTCATEGBIND) | enum | BLOCK / PERMIT / REDIRECT | **分类级精确动作**（覆盖CFTEMPLATE模板级缺省） |
| CATEGORYTYPE | enum | SPECIFIC | 分类类型 |
| CATEGORYID | int | — | URL分类ID（来自ICAP Server） |

### 5.7 ADD USRLOCATION / ADD USRLOCATIONGRP（位置触发核心命令，UNC侧）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| LOCATIONNAME | string | — | 位置名 |
| LOCATIONTYPE | enum | CGI / ECGI / NCGI | 位置类型（2/3G=CGI、4G=ECGI、5G=NCGI） |
| MCC | string | — | 移动国家码 |
| MNC | string | — | 移动网络码 |
| LAC / ECI / NCI | string | — | 位置区/小区标识（按LOCATIONTYPE） |
| LOCGROUPNAME | string | — | 位置组名（UPBINDUPG.LOCGROUPNAME引用此） |

---

## 6. MMLCommand `operates_on` ConfigObject 边表

> **Schema参考**：§11.7 `MMLCommand operates_on ConfigObject`。

### 6.1 UDG侧 — 基础与过滤链（12条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| SET LICENSESWITCH (CMD-UDG-001) | LICENSESWITCH | License开关操作（元配置） |
| SET REFRESHSRV (CMD-UDG-002) | 策略刷新 | 触发配置下发到转发面 |
| LOD SIGNATUREDB (CMD-UDG-003) | SIGNATUREDB | 加载SA特征库 |
| LOD PARSERDB (CMD-UDG-004) | PARSERDB | 加载协议解析库 |
| ADD FILTER (CMD-UDG-005) | FILTER | 创建L3/L4过滤器 |
| ADD FLOWFILTER (CMD-UDG-006) | FLOWFILTER | 创建流过滤器 |
| ADD FLTBINDFLOWF (CMD-UDG-007) | FLTBINDFLOWF | 过滤器绑定到FLOWFILTER |
| ADD L7FILTER (CMD-UDG-008) | L7FILTER | 创建L7过滤器 |
| ADD PROTBINDFLOWF (CMD-UDG-009) | PROTBINDFLOWF | 协议+L7FILTER绑定 |
| ADD EXTENDEDFILTER (CMD-UDG-010) | EXTENDEDFILTER | 创建扩展过滤器 |
| ADD ERRORCODE (CMD-UDG-011) | ERRORCODE | 创建错误码范围 |
| ADD WELLKNOWNPORT (CMD-UDG-012) | WELLKNOWNPORT | 创建知名端口 |

### 6.2 UDG侧 — 轨道A五子轨动作对象（12条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD ADCPARA (CMD-UDG-013) | ADCPARA | ADC参数（轨道A-ADC） |
| ADD HEADEN (CMD-UDG-014) | HEADEN | 头增强对象（轨道D，跨4特性） |
| SET BASE64 (CMD-UDG-015) | (HEADEN编码开关) | 头增强编码控制 |
| ADD SMARTHTTPREDIR (CMD-UDG-016) | SMARTHTTPREDIR | HTTP智能重定向动作（轨道C） |
| ADD REDIRAPPENDINFO (CMD-UDG-017) | REDIRAPPENDINFO | 重定向携带信息 |
| ADD DNSOVERWRITING (CMD-UDG-018) | DNSOVERWRITING | DNS重写动作（轨道C，与SMARTHTTPREDIR共用POLICYTYPE） |
| SET IPFARMGLOBAL (CMD-UDG-019) | IPFARMGLOBAL | IPFarm全局参数（轨道B-1） |
| ADD IPFARM (CMD-UDG-020) | IPFARM | 重定向服务器集群（轨道B-1） |
| ADD IPFARMSERVER (CMD-UDG-021) | IPFARMSERVER | IPFarm服务器 |
| ADD LOGICINF (CMD-UDG-022) | LOGICINF | 逻辑接口（心跳+ICAP共用） |
| ADD BLACKLISTRULE (CMD-UDG-023) | BLACKLISTRULE | WebProxy黑名单 |
| ADD APN (CMD-UDG-024) | APN | APN配置 |

### 6.3 UDG侧 — URL过滤轨道B ICAP互通（6条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD VPNINST (CMD-UDG-025) | VPNINST | VPN实例（ICAP专网） |
| ADD ICAPSERVER (CMD-UDG-026) | ICAPSERVER | ICAP服务器（轨道B必需） |
| ADD ICAPLOCALINFO (CMD-UDG-027) | ICAPLOCALINFO | ICAP本端信息 |
| ADD ICAPSVRGRP (CMD-UDG-028) | ICAPSVRGRP | ICAP服务器组 |
| ADD ICAPSVRBINDISG (CMD-UDG-029) | ICAPSVRBINDISG | ICAP服务器与组绑定 |
| SET CFSRVMODE (CMD-UDG-030) | CFSRVMODE | URL过滤业务模式 |

### 6.4 UDG侧 — URL过滤轨道B 内容过滤业务（12条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| SET APNCFFUNC (CMD-UDG-031) | APNCFFUNC | APN内容过滤开关 |
| ADD CFPROFILE (CMD-UDG-032) | CFPROFILE | 内容过滤策略 |
| ADD CFTEMPLATE (CMD-UDG-033) | CFTEMPLATE | 内容过滤模板（含ACTION，轨道B核心） |
| SET APNCFTEMPLATE (CMD-UDG-034) | APNCFTEMPLATE | APN-模板绑定 |
| ADD CFPROFBINDCFT (CMD-UDG-035) | CFPROFBINDCFT | 策略-模板绑定 |
| ADD CONTCATEGROUP (CMD-UDG-036) | CONTCATEGROUP | 内容分类组 |
| ADD CONTCATEGBIND (CMD-UDG-037) | CONTCATEGBIND | 策略-分类组绑定（含ACTION，轨道B核心） |
| SET CFCACHEPARA (CMD-UDG-038) | CFCACHEPARA | 缓存参数 |
| SET GLBCFFUNC (CMD-UDG-039) | GLBCFFUNC | 全局内容过滤开关 |
| ADD CFWHITEURLLST (CMD-UDG-040) | CFWHITEURLLST | URL白名单 |
| ADD CFIPWHITELIST (CMD-UDG-041) | CFIPWHITELIST | IP白名单 |
| ADD CFPFSPECACTION (CMD-UDG-042) | CFPFSPECACTION | 特殊场景动作 |

### 6.5 UDG侧 — PCC规则与策略（6条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD RULE (CMD-UDG-043) | RULE | PCC规则（POLICYTYPE双轨道+五子轨差异化） |
| ADD USERPROFILE (CMD-UDG-044) | USERPROFILE | 用户模板（Portal含CAPMODETHRES） |
| ADD RULEBINDING (CMD-UDG-045) | RULEBINDING | 规则绑定 |
| ADD PCCPOLICYGRP (CMD-UDG-046) | PCCPOLICYGRP | PCC策略组 |
| ADD URR (CMD-UDG-047) | URR | 使用量上报规则 |
| ADD URRGROUP (CMD-UDG-048) | URRGROUP | URR组 |

### 6.6 UNC侧 — 基础与PCRF（11条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| SET LICENSESWITCH (CMD-UNC-001) | LICENSESWITCH | License开关 |
| SET PCCFUNC (CMD-UNC-002) | PCCFUNC | PCC功能全局设置 |
| SET PCCFAILACTION (CMD-UNC-003) | PCCFAILACTION | PCC故障处理 |
| SET POLICYMODE (CMD-UNC-004) | POLICYMODE | 接口模式（Gx/N7） |
| SET N7RCVATTRCTRL (CMD-UNC-005) | N7RCVATTRCTRL | N7接收属性 |
| SET N7SNDATTRCTRL (CMD-UNC-006) | N7SNDATTRCTRL | N7发送属性 |
| SET FHBYPASS (CMD-UNC-007) | FHBYPASS | 紧急旁路 |
| ADD PCRF (CMD-UNC-008) | PCRF | PCRF实例 |
| ADD PCRFGROUP (CMD-UNC-009) | PCRFGROUP | PCRF组 |
| ADD PCRFBINDGRP (CMD-UNC-010) | PCRFBINDGRP | PCRF组绑定 |
| SET DFTGLBPCRFGRP (CMD-UNC-011) | DFTGLBPCRFGRP | 缺省全局PCRF组 |

### 6.7 UNC侧 — 规则/模板绑定链与位置触发（9条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD RULE (CMD-UNC-012) | RULE | UNC侧规则定义 |
| ADD USERPROFILE (CMD-UNC-013) | USERPROFILE | UNC侧用户模板 |
| ADD RULEBINDING (CMD-UNC-014) | RULEBINDING | 规则绑定 |
| ADD USRPROFGROUP (CMD-UNC-015) | USRPROFGROUP | 用户模板组 |
| ADD UPBINDUPG (CMD-UNC-016) | UPBINDUPG | 模板绑定（含LOCGROUPNAME位置组扩展） |
| MOD UPBINDUPG (CMD-UNC-017) | UPBINDUPG | 修改模板绑定（位置触发场景） |
| ADD APNUSRPROFG (CMD-UNC-018) | APNUSRPROFG | APN绑定用户模板组 |
| ADD USRLOCATION (CMD-UNC-019) | USRLOCATION | 用户位置（CGI/ECGI/NCGI） |
| ADD USRLOCATIONGRP (CMD-UNC-020) | USRLOCATIONGRP | 用户位置组 |

---

## 7. CommandRule `governs` 关系（反向：MMLCommand governed_by CommandRule）

> **Schema参考**：§11.7 `CommandRule governs MMLCommand/CommandParameter/ConfigObject`。下表为治理映射。

| CommandRule | governs -> 作用对象 | 说明 |
|-------------|--------------------|------|
| CR-AC-01 | ADD RULE (CMD-UDG-043, CMD-UNC-012).RULENAME | 跨POLICYTYPE RULENAME唯一性 |
| CR-AC-02 | ADD RULE.POLICYTYPE / POLICYNAME | 双轨道+五子轨动作对象链决定 |
| CR-AC-03 | ADD RULE(POLICYTYPE=SMARTREDIRECT).POLICYNAME | SMARTREDIRECT两子类型区分 |
| CR-AC-04 | ADD HEADEN (CMD-UDG-014).ANTIFRAUD | 头防欺诈强依赖头增强 |
| CR-AC-05 | ADD ICAPSERVER / ICAPSVRGRP 系列 (CMD-UDG-026~029) | ICAP Server前置必需 |
| CR-AC-06 | ADD CFTEMPLATE.ACTION / ADD CONTCATEGBIND.ACTION | PERMIT动作唯一性 |
| CR-AC-07 | ADD FLOWFILTER / FLTBINDFLOWF (CMD-UDG-006, 007) | FLOWFILTER必须绑定FILTER |
| CR-AC-08 | ADD RULE.POLICYNAME / FLOWFILTERNAME | RULE引用对象存在性 |
| CR-AC-09 | ADD RULE.RULENAME (跨UDG/UNC) | 预定义规则名三网元一致 |
| CR-AC-10 | ADD RULE(POLICYTYPE=HEADEN/SMARTREDIRECT) / USERPROFILE(Portal) | 加密协议盲区互斥 |
| CR-AC-11 | ADD HEADEN(RTSP场景).ANTIFRAUD | RTSP不支持防欺诈 |
| CR-AC-12 | SET REFRESHSRV (CMD-UDG-002) | 配置变更后刷新生效 |
| CR-AC-13 | SET REFRESHSRV (CMD-UDG-002) + FILTER/L7FILTER变更窗口 | 60秒禁改Filter |
| CR-AC-14 | RULE + CFTEMPLATE/CONTCATEGBIND（并存） | 双轨可并存 |

---

## 8. 与计费/带宽场景命令图谱的差异

| 维度 | 计费场景 | 带宽控制场景 | 访问限制场景 |
|------|---------|------------|------------|
| MMLCommand数量 | 87 | 55 | **68**（P5 修正：原 62，含 UDG 48 = 主清单含 PCC 规则与策略 6 命令 + UNC 20） |
| ConfigObject数量 | 55 | 29 | **41** |
| CommandRule数量 | 14 | 5 | **14** |
| 独有命令族 | URR三件套/在线计费/融合计费18步链/CG接口 | BWM三级控制/Shaping/智能Shaping/FUP(URR复用)/ADC | **双轨道+五子轨动作体系**：轨道A 五子轨（ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY）+ 轨道B（URL过滤 CFTEMPLATE/CONTCATEGBIND.ACTION 独立动作） |
| 共享命令 | SET LICENSESWITCH, ADD RULE, ADD USERPROFILE, ADD RULEBINDING, ADD PCCPOLICYGRP, ADD FLOWFILTER, ADD FILTER, ADD L7FILTER, ADD FLTBINDFLOWF, SET REFRESHSRV, LOD SIGNATUREDB/PARSERDB | 同左 | 同左（三场景共享通用骨架） |
| 共享ConfigObject | RULE, USERPROFILE, RULEBINDING, USRPROFGROUP, UPBINDUPG, APNUSRPROFG, PCCPOLICYGRP, FLOWFILTER, FILTER, L7FILTER, FLTBINDFLOWF, CATEGORYPROP, URR, URRGROUP | 同左（含URR/URRGROUP） | 同左 + **PROTBINDFLOWF, EXTENDEDFILTER, ERRORCODE**（重定向族多维匹配扩展） |
| POLICYTYPE枚举差异 | CHARGING | BWM/PCC/QOS/ADC | **ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY**（轨道A 五子轨，CR-AC-02） |
| 核心架构发现 | 计费三件套(URR→URRGROUP→PCCPOLICYGRP) | BWM三级控制(BWMSERVICE→BWMCONTROLLER→BWMUSERGROUP→BWMRULE) | **双轨道+五子轨动作机制**：轨道A（PCC体系，RULE.POLICYTYPE 五子轨隐式驱动）vs 轨道B（URL过滤体系，CFTEMPLATE/CONTCATEGBIND.ACTION 显式驱动） |
| PERMIT支持 | 不适用（计费无放行概念） | 不显式支持 | **仅轨道B显式支持PERMIT**（CR-AC-06） |

> **三场景共享骨架**：SET LICENSESWITCH / ADD RULE / ADD USERPROFILE / ADD RULEBINDING / ADD PCCPOLICYGRP / ADD FLOWFILTER / ADD FILTER / ADD L7FILTER / ADD FLTBINDFLOWF / SET REFRESHSRV / LOD SIGNATUREDB/PARSERDB / ADD URR / ADD URRGROUP / ADD ADCPARA / ADD CATEGORYPROP。访问限制场景的差异化体现在：(1) RULE.POLICYTYPE枚举扩展为轨道A 五子轨5值；(2) 独有双轨道动作对象族（HEADEN/SMARTREDIRECT族/IPFarm族/ICAP+CF族）；(3) UNC侧独有位置触发对象（USRLOCATION/USRLOCATIONGRP）。

---

## 9. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| MMLCommand | **68** | CMD-UDG-001~048（48 个，含 PCC 规则与策略 6 命令 043~048） + CMD-UNC-001~020（20 个） |
| ConfigObject | 41 | 共享18（OBJ-RULE等通用） + 访问限制独有23（OBJ-AC-*） |
| CommandRule | 14 | CR-AC-01 ~ CR-AC-14 |
| ConfigObject contains/refers_to/depends_on/conflicts_with/activates 边 | 39 | 通用结构9 + 轨道A(PCC)3 + 轨道D(HEADEN)4 + 轨道C(SMARTREDIRECT)8 + 轨道B-1(WEBPROXY/Portal)7 + 轨道B-2(URL过滤)10 + 接入控制4 + 协议盲区互斥(归入conflicts_with，含在上述边) |
| operates_on 边 | 65 | UDG侧45（基础过滤12 + 五子轨动作对象12 + ICAP互通6 + 内容过滤12 + PCC规则策略6 - 重复APN等微调）+ UNC侧20 |
| **命令层对象总计** | **~227** | — |

### 9.1 双轨道+五子轨 ConfigObject 链完整度核查

| 轨道 | 入口 | POLICYTYPE | POLICYNAME指向 | 关系链完整度 |
|------|------|-----------|---------------|------------|
| 轨道A (PCC体系，PCC子轨) | FILTER→FLOWFILTER→RULE | PCC | PCCPOLICYGRP → URRGROUP → URR | ✅ 完整（§3.1 + §3.2） |
| 轨道A (ADC子轨) | FILTER→FLOWFILTER→RULE | ADC | (直接在RULE) + ADCPARA | ✅ 完整（§3.2） |
| 轨道A (HEADEN子轨) | FILTER→FLOWFILTER→RULE | HEADEN | HEADEN（含ANTIFRAUD/GRAYLIST） | ✅ 完整（§3.3） |
| 轨道A (SMARTREDIRECT子轨) | EXTENDEDFILTER+ERRORCODE→SMARTHTTPREDIR/DNSOVERWRITING←RULE | SMARTREDIRECT | SMARTHTTPREDIR 或 DNSOVERWRITING | ✅ 完整（§3.4） |
| 轨道A (WEBPROXY子轨) | FILTER→FLOWFILTER→RULE + IPFARM→IPFARMSERVER | WEBPROXY | IPFARM | ✅ 完整（§3.5） |
| 轨道B (URL过滤体系，独立动作) | ICAP链 + CFTEMPLATE/CONTCATEGBIND.ACTION | PCC（仅触发） | PCCPOLICYGRP（仅匹配），实际动作走CFTEMPLATE/CONTCATEGBIND | ✅ 完整（§3.6） |
| 接入控制触发 | USRLOCATION→USRLOCATIONGRP→UPBINDUPG→USRPROFGROUP→APNUSRPROFG | (UNC侧，不直接产生动作) | (位置触发，策略下发到UDG执行) | ✅ 完整（§3.7） |

> **★ 口径统一说明（U-M-01，P5 修复）**：P5 前 §9.1 使用 "轨道A/B-1/B-2/C/D" 五轨命名，与 §3.5 "轨道B-1 WEBPROXY/Portal"、§3.6 "轨道B-2 URL过滤" 混用。P5 统一为权威口径：**双轨道（轨道A PCC体系 / 轨道B URL过滤体系）+ 轨道A 内五子轨（ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY）**。原 "轨道B-1 WEBPROXY/Portal" 实为轨道A 的 WEBPROXY 子轨（RULE.POLICYTYPE=WEBPROXY 隐式驱动），现归入轨道A；原 "轨道C SMARTREDIRECT / 轨道D HEADEN" 同理归入轨道A 五子轨。

---

> 本文件为访问限制场景三层图谱第4层。第5层跨层映射、第6层证据索引见同目录其他文件。**双轨道+五子轨动作机制**（轨道A PCC体系五子轨：ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY + 轨道B URL过滤体系 CFTEMPLATE/CONTCATEGBIND.ACTION 独立动作）是本场景区别于计费/带宽场景的核心架构，详见 `feature-knowledge/cross-feature-analysis.md` §5.1 和附录E。
