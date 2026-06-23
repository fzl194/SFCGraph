# 访问限制场景三层图谱 · 第2层：特性图谱

> **文件定位**：`three-layer-graph/02-feature-graph.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §9 特性图谱（§9.3 Feature / §9.5 License / §9.6 FeatureRule / §9.7 FeatureTaskOrderEdge / §9.8 关系）
> **本体参考**：`三层图谱本体标准定义.md`
> **作用**：实例化访问限制场景 19 个 Feature（11 UDG 独有 + 4 UNC 独有接入控制 [WSFD-211001 位置触发 + 4 接入控制辅助] + 4 复用共享，ADC 有 UDG/UNC 两侧） + depends_on 边 + requires_license 边 + FeatureRule + FeatureTaskOrderEdge
>
> **数量说明（U-H-02 修复后）**：访问限制场景 Feature 总数为 **19**（UDG 11 + UNC 8）。原 P4 建模口径"15 = UDG 11 + UNC 4"遗漏 CS-AC-07 `uses_feature` 引用的 4 个 UNC 接入控制辅助特性（WSFD-106003/105003/106005/105006），U-H-02 已在 §1.9 补实例化。历史口径"14 = 11 + 3"将 ADC（UDG 侧 GWFD-020357 + UNC 侧 WSFD-109102）合并计为 1，本文件按产品定义的正式特性编号分别建模，ADC UDG 归入 11 独有、ADC UNC 归入 4 复用。
> **数据来源**：`feature-knowledge/cross-feature-analysis.md`（1603 行，§1 分类 / §3 配置差异 / §4 依赖 / §5 关键发现 / 附录 A-F）、11 个特性知识文件 §0 元数据（对齐 Schema §9.3）、`feature-knowledge/cross-topic-analysis.md` §6.3 CS-AC-07（4 个 UNC 接入控制辅助特性的 uses_feature 清单）

---

## 0. 特性图谱总览

### 0.1 19 Feature 分组（11 UDG 独有 + 4 复用共享 + 4 UNC 接入控制辅助）

> **Feature 计数说明（U-H-02 修复后）**：访问限制场景 Feature 总数 = **19**（UDG 11 独有 + UNC 8 = UNC 位置触发 1 + UNC 接入控制辅助 4 + UNC 复用 PCC/ADC 2）。原 P4 建模时仅实例化 15 个（UDG 11 + UNC 4），CS-AC-07 `uses_feature` 引用的 4 个 UNC 接入控制辅助特性（WSFD-106003/105003/106005/105006）未实例化，导致跨层悬空；U-H-02 已在 §1.9 补全，本表同步更新。

| 分组 | 独有特性 | 复用特性 | 小计 |
|------|---------|---------|------|
| 业务感知层（复用） | — | GWFD-110101 SA-Basic | 1 |
| PCC骨架层（复用） | — | GWFD-020351 PCC基本功能（UDG）、WSFD-109101 PCC基本功能（UNC） | 2 |
| ADC应用检测层 | GWFD-020357 增强的ADC基本功能 | WSFD-109102 ADC基本功能（UNC，复用） | 2 |
| 头增强族 | GWFD-110261 HTTP头增强、GWFD-110262 RTSP头增强、GWFD-110263 HTTPS头增强 | — | 3 |
| 防欺诈层 | GWFD-110401 HTTP头防欺诈 | — | 1 |
| 重定向族 | GWFD-110281 用户Portal、GWFD-110282 WebProxy、GWFD-110283 DNS纠错、GWFD-110284 HTTP智能重定向 | — | 4 |
| URL内容过滤层 | GWFD-110471 URL过滤基本功能 | — | 1 |
| 接入控制触发层（UNC） | WSFD-211001 基于初始接入位置的策略控制 | — | 1 |
| 接入控制辅助层（UNC，U-H-02 补） | WSFD-106003 用户接入控制(AMF)、WSFD-105003 区域漫游限制(AMF)、WSFD-106005 支持ODB(AMF)、WSFD-105006 会话服务区域限制(SMF) | — | 4 |
| **合计** | **15 独有**（10 UDG + 5 UNC） | **4 复用**（SA-Basic / PCC UDG / PCC UNC / ADC UNC，三场景共享） | **19** |

> **复用标注**：4 个复用特性（SA-Basic / PCC-UDG / PCC-UNC / ADC-UNC）为**三场景共享基础设施**，与计费场景、带宽控制场景共用。访问限制场景在复用层之上叠加 15 个独有特性（UDG 10 + UNC 5 = 位置触发 1 + 接入控制辅助 4），形成"共享底座 + UDG 侧细粒度动作层 + UNC 侧粗粒度准入层"的分层架构。

### 0.2 License 总览

| 产品 | License 数 | 说明 |
|------|----------|------|
| UDG | 12 | 独有 10（ADC 1 + 头增强 3 / 重定向 4 / 防欺诈 1 / URL 过滤 1）+ 复用 2（SA-Basic + PCC UDG，三场景共享） |
| UNC | 3 | 独有 1（位置触发）+ 复用 2（PCC UNC + ADC UNC，三场景共享） |
| 无需 License 特性 | 4（★ P5 批次 1 补） | 19 特性中 4 个 UNC 接入控制辅助特性（WSFD-106003/105003/106005/105006）无独立 License 控制项，随 PCC UNC License 或 AMF 基础功能启用；其余 15 特性均有独立 License |

> License 前缀规律：UDG 独有特性统一 `LKV3G5` 前缀；UNC 独有特性为 `LKV2`（独立特性）或 `LKV3W9`（复用 PCC 家族）。

### 0.3 全局字段声明（status）

> **适用范围**：本文件 §1（19 个 Feature）和 §3（15 个 License）所有对象。
> **声明**：除非特别标注，本文件所有 Feature（GWFD/WSFD-*）和 License（LKV*）的 `status` 字段值均为 `active`。
> **依据**：Schema §9.3（Feature.status 必备）和 §9.5（License.status 必备）。访问限制场景所有特性和 License 均处于正式启用状态。
> **例外**：§1.9 的 4 个 UNC 接入控制辅助特性（WSFD-106003/105003/106005/105006）未在独立 License 表列出，`requires_license` 字段值为 —（无独立 License 控制项），`status` 仍为 `active`。

### 0.4 Evidence ID 命名约定

> **访问限制场景统一编号**：`EV-FK-AC-NN`（AC = Access Control，NN = 01~19；01~15 对应附录 A 15 特性索引表序号，16~19 为 P5 批次 3 新增的 4 个 UNC 接入控制辅助特性）。复用特性沿用跨场景共享编号（`EV-FK-01` SA-Basic / `EV-FK-03` PCC-UDG / `EV-FK-17` PCC-UNC / `EV-FK-21` ADC-UNC，与带宽场景一致）。
> **来源标识**：`EV-CA-01` = 访问限制场景跨特性横向分析报告。

---

## 1. Feature 实例化（19 个，★ P5 批次 1 U-H-02 补 4 个 UNC 辅助特性）

### 1.1 业务感知层（复用）

#### GWFD-110101 SA-Basic（业务感知基本功能，三场景共享）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110101` |
| `feature_name` | `SA-Basic` |
| `feature_summary` | L3/L4/L7 业务识别基础引擎，提供 SVC/APP 识别、协议解析、URL 提取能力，是整个访问限制场景所有 L7 动作特性（ADC / 头增强族 / 重定向族 / URL 过滤 / 防欺诈）的数据基础，被 10 个独有特性直接依赖 |
| `feature_group` | `SA_BASE` |
| `parent_feature_id` | —（场景根特性） |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["识别层级(L3/L4/L7)", "特征库版本"]` |
| `first_release` | `UDG 20.0.0` |
| `requires_license` | `LKV3G5SABS01` |
| `key_capabilities` | ① L3/L4 五元组解析（IP/端口/协议）② 协议识别（知名端口 + 签名匹配）③ L7 URL/Method/Response Code/SNI 解析 ④ SVC（业务大类）+ APP（具体应用）标识输出 ⑤ SET REFRESHSRV 策略刷新 ⑥ CP/UP 配置一致性检查 |
| `source_evidence_ids` | `EV-FK-AC-01`, `EV-CA-01` |
| **复用标注** | **三场景共享**（计费 + 带宽控制 + 访问限制），与带宽场景共用 `EV-FK-01` 编号 |

### 1.2 PCC骨架层（复用）

#### GWFD-020351 PCC基本功能（UDG，三场景共享）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020351` |
| `feature_name` | `PCC基本功能` |
| `feature_summary` | UDG 侧 PCC 基础，接收 N4 规则（PDR/FAR/QER/URR/BAR），承载 RULE/USERPROFILE/RULEBINDING/PCCPOLICYGRP 规则体系；**RULE.POLICYTYPE 是访问限制轨道 A 动作类型的核心区分**（ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY），是所有 UDG 侧访问限制特性的动作载体 |
| `feature_group` | `PCC_FRAME` |
| `parent_feature_id` | —（场景根特性） |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["规则来源(动态/预定义/本地)", "有无PCRF", "POLICYTYPE(ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY)"]` |
| `first_release` | `UDG 20.0.0` |
| `requires_license` | `LKV3G5PCCB01` |
| `key_capabilities` | ① 接收 PCRF/PCF 策略（经 N4）② N4 规则体系（PDR/FAR/QER/URR/BAR）③ 动态/预定义/本地规则三种模式 ④ SET REFRESHSRV 策略刷新（PROTBINDFLOWF 60s 延迟）⑤ RULE.POLICYTYPE 差异化动作承载（访问限制核心） |
| `source_evidence_ids` | `EV-FK-AC-02`, `EV-CA-01` |
| **复用标注** | **三场景共享**，与带宽场景共用 `EV-FK-03` 编号 |

#### WSFD-109101 PCC基本功能（UNC，三场景共享）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-109101` |
| `feature_name` | `PCC基本功能` |
| `feature_summary` | UNC（SMF/PGW-C）侧 PCC 基础，接收 PCRF/PCF 的 QCI/5QI/MBR/GBR/ARP 策略，通过 Gx（4G）/N7（5G）接口下发，经 N4 转发给 UDG 执行；是 UNC 侧 WSFD-211001 位置触发的强依赖前置 |
| `feature_group` | `PCC_FRAME` |
| `parent_feature_id` | —（场景根特性） |
| `applicable_nf_map` | `{"UNC": ["SMF", "PGW-C", "AMF", "GGSN"]}` |
| `variant_dimensions` | `["接口(Gx/N7)", "PCRF冗余模式"]` |
| `first_release` | `UNC 20.0.0` |
| `requires_license` | `LKV3W9SPCC11` |
| `key_capabilities` | ① Gx 接口 Diameter 信令（2/3/4G）② N7/N15 服务化接口（5G）③ IP-CAN 会话管理（CCR-I/U/T）④ PCRF 冗余（主备/轮询/百分比 + Failover）⑤ Event Triggers（USAGE_REPORT/QOS_CHANGE/APP_STA/STO 等） |
| `source_evidence_ids` | `EV-FK-AC-03`, `EV-CA-01` |
| **复用标注** | **三场景共享**，与带宽场景共用 `EV-FK-17` 编号 |

### 1.3 ADC应用检测层

#### GWFD-020357 增强的ADC基本功能（UDG）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020357` |
| `feature_name` | `增强的ADC基本功能` |
| `feature_summary` | UDG 侧 ADC，基于 SA 的 L7 DPI 引擎检测应用，通过 PGW-C/SMF 将应用标识、流信息及 APP_STA/APP_STO 事件上报 PCRF/PCF，触发动态 PCC 策略；不匹配时兜底阻塞，是 L7 动态访问限制的"应用感知层"横切依赖 |
| `feature_group` | `ADC` |
| `parent_feature_id` | `GWFD-020351 PCC基本功能`（ADC 在 PCC 基础上扩展 L7 检测） |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"], "UNC": ["PGW-C", "SMF"], "PCF": ["PCRF", "PCF"]}` |
| `variant_dimensions` | `["检测事件(APP_STA/APP_STO)", "动作策略组(策略类型为ADC的独立rule / 复用策略类型为PCC的rule)", "PCRF规则下发方式(预定义规则 / 动态规则携带TDF-Application-Identifier)", "协议类型(HTTP / FTP / RTSP等SA支持的协议)", "流信息上报开关(FLOWINFORPT=ENABLE/DISABLE)", "POLICYTYPE轨道(A-ADC独立 / A-PCC复用)"]` |
| `first_release` | `UDG 20.1.0` |
| `requires_license` | `LKV3G5ADCF01` |
| `key_capabilities` | ① SA L7 DPI 引擎应用检测 ② APPLICATION_START/STOP 事件上报（Gx）③ APP_STA/STO 事件上报（N7）④ ADCPARA 参数配置（FLOWINFORPT + ADCHYSTTIMER）⑤ FLOWFILTERNAME/appid 全网一致性要求 ⑥ 兜底阻塞机制（业务流匹配不上所有 PCC rule 时 UDG 阻塞） |
| `source_evidence_ids` | `EV-FK-AC-04`, `EV-CA-01` |
| **复用标注** | ADC 在带宽/计费/访问限制三场景均出现，但 UDG 侧编号一致，复用 |

#### WSFD-109102 ADC基本功能（UNC，复用）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-109102` |
| `feature_name` | `ADC基本功能` |
| `feature_summary` | UNC 侧 ADC，转发 PCRF/PCF 应用检测事件，承载管理，三策略组（Normal/Start/Stop），FLOWFILTER + ADCPARA 三网元一致性 |
| `feature_group` | `ADC` |
| `parent_feature_id` | `WSFD-109101 PCC基本功能（UNC）` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `variant_dimensions` | `["接口(Gx/N7)"]` |
| `first_release` | `UNC 20.5.0` |
| `requires_license` | `LKV2BADCF01` |
| `key_capabilities` | ① 三策略组（Normal/Start/Stop）② FLOWFILTER + ADCPARA 三网元一致性 ③ 承载管理（专载建立/更新/释放）④ PCRF/PCF 应用检测事件转发 |
| `source_evidence_ids` | `EV-FK-AC-05`, `EV-CA-01` |
| **复用标注** | **三场景共享**，与带宽场景共用 `EV-FK-21` 编号 |

### 1.4 头增强族

#### GWFD-110261 HTTP头增强

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110261` |
| `feature_name` | `HTTP头增强` |
| `feature_summary` | 对 HTTP 报文头做内容增强，将 MSISDN/IMSI/IMEI/APN/MSIP 等用户信息以 `<字段前缀名称: 字段值>` 格式插入 HTTP 扩展字段，传递给 Web Server；带内（in-band）信息传递机制；POLICYTYPE=HEADEN 独立于 PCC/SMARTREDIRECT，**与头防欺诈强耦合** |
| `feature_group` | `HEADEN` |
| `parent_feature_id` | —（配置树无独立父节点；业务归属"智能策略控制功能 → 头增强控制"分支） |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `variant_dimensions` | `["协议类型(HTTP1.x，不支持HTTP2.0)", "插入字段(MSISDN/IMSI/IMEI/APN/MSIP/SGSNIP/GGSNIP/ULI/RAT/CHGCHAR/Roaming/USERDEF/User-Profile-alias/SESSIONID/TIMESTAMP/UPIPV4/UPIPV6/MULTIPARA/RANDNUM等25类)", "加密算法(NONE/MD5/RC4/AES-128/AES-256/RSA-1024/RSA-2048/SHA-256)", "编码方式(base64/ASCII/INHERIT)", "触发方式(基于特定IP/基于特定URL/基于HTTP协议)", "过滤层级(三四层FILTER vs 七层L7FILTER+PROTBINDFLOWF)", "是否启用头防欺诈(ADD HEADEN ANTIFRAUD=ENABLE，强耦合GWFD-110401)", "灰名单模式(GRAYLIST=ENABLE只防欺诈不插入)", "POLICYTYPE轨道(A-HEADEN，RULE直接引用HEADEN对象)", "拼接字段数量(v02起支持MULTIPARA 3字段×4参数)"]` |
| `first_release` | `UDG 20.0.0`（v02 = `20.10.0` 多参数拼接） |
| `requires_license` | `LKV3G5HTHE01` |
| `key_capabilities` | ① HTTP 扩展字段插入（HTTP1.x only）② 25 类字段 + 7 种加密算法 ③ base64/ASCII 编码 ④ MULTIPARA 多参数拼接（v02）⑤ 与头防欺诈共用 HEADEN 对象（ANTIFRAUD/GRAYLIST 内嵌）⑥ 依赖 SA-Basic + SA-Web Browsing + SA-Mobile（MMS 场景） |
| `source_evidence_ids` | `EV-FK-AC-06`, `EV-CA-01` |

#### GWFD-110262 RTSP头增强

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110262` |
| `feature_name` | `RTSP头增强` |
| `feature_summary` | HTTP 头增强的 RTSP 协议变体，对 RTSP 报文头做内容增强传递给 Streaming Server；RTSP 扩展机制与 HTTP 基本相同（`<字段前缀名称: 字段值>`）；**不支持头防欺诈（族内唯一例外）** |
| `feature_group` | `HEADEN` |
| `parent_feature_id` | —（同 HTTP 头增强归属分支） |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `variant_dimensions` | `["协议类型(RTSP，仅基于TCP；不支持RTSP over HTTP)", "插入字段(与HTTP头增强基本一致)", "RTSP请求类型(Setup/Play/Pause/Teardown/Options/Describe 6类)", "加密算法(NONE/MD5/RC4/AES-128/AES-256/RSA-1024/RSA-2048/SHA-256)", "编码方式(base64/ASCII/INHERIT)", "触发方式(基于特定IP/基于特定URL/基于RTSP协议)", "过滤层级(三四层FILTER vs 七层L7FILTER+PROTBINDFLOWF PROTOCOLNAME=rtsp)", "是否启用头防欺诈(不支持，与HTTP/HTTPS差异)", "POLICYTYPE轨道(A-HEADEN)", "拼接字段数量(v02起支持MULTIPARA)"]` |
| `first_release` | `UDG 20.0.0`（v02 = `20.10.0` 多参数拼接） |
| `requires_license` | `LKV3G5RTHE01` |
| `key_capabilities` | ① RTSP 扩展字段插入（仅 TCP）② RTSP 请求类型匹配（6 类）③ 加密算法 + 编码能力同 HTTP ④ MULTIPARA 多参数拼接（v02）⑤ 依赖 SA-Basic + SA-Streaming（仅需 2 项 SA）⑥ **不支持 RTSP over HTTP / 不支持头防欺诈** |
| `source_evidence_ids` | `EV-FK-AC-07`, `EV-CA-01` |

#### GWFD-110263 HTTPS头增强

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110263` |
| `feature_name` | `HTTPS头增强` |
| `feature_summary` | HTTPS 报文头增强，将用户信息插入到 **SSL 报文头的 Extension 字段内**（TLS 握手 Client Hello），按 TLS 协议 **TLV（Type-Length-Value）格式**组织，而非 HTTP 文本格式；依赖 HTTP2.0 Host 识别（HTTPS 加密） |
| `feature_group` | `HEADEN` |
| `parent_feature_id` | —（同 HTTP 头增强归属分支） |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `variant_dimensions` | `["协议类型(TLS1.0/1.1/1.2/1.3)", "插入字段(MSISDN/IMSI/IMEI/APN/MSIP/SGSNIP/GGSNIP/ULI/RAT/CHGCHAR/Roaming/USERDEF/User-Profile-alias/SESSIONID/TIMESTAMP/UPIPV4/UPIPV6/RANDNUM等24类，无MULTIPARA)", "插入位置(SSL报文头Extension字段内，TLV格式)", "加密算法(NONE/MD5/RC4/AES-128/AES-256/SHA-256，无RSA)", "编码方式(base64/ASCII/INHERIT + Byte837十六进制编码)", "触发方式(基于特定IP/基于特定SNI/基于HTTPS协议)", "TLS Type值(TLSTYPEVAL + SUBTLSTYPEVAL，HTTPS独有)", "是否启用头防欺诈(支持，与HTTP头增强一致)", "灰名单模式(GRAYLIST=ENABLE只防欺诈不插入)", "POLICYTYPE轨道(A-HEADEN，RULE直接引用TLSHEADEN对象)"]` |
| `first_release` | `UDG 20.0.0` |
| `requires_license` | `LKV3G5HTSE01` |
| `key_capabilities` | ① SSL Extension 字段 TLV 格式插入 ② 24 类字段（无 MULTIPARA）③ 6 种加密算法（无 RSA）④ Byte837 十六进制编码 ⑤ TLS Type 值配置（TLSTYPEVAL）⑥ 依赖 SA-Basic + SA-Web Browsing + SA-Mobile + **HTTP2.0 Host 识别** ⑦ 支持头防欺诈 |
| `source_evidence_ids` | `EV-FK-AC-08`, `EV-CA-01` |

### 1.5 防欺诈层

#### GWFD-110401 HTTP头防欺诈

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110401` |
| `feature_name` | `HTTP头防欺诈` |
| `feature_summary` | HTTP 头增强动作执行**之前**的检测前置层：检测用户报文 HTTP 头是否已存在插入字段、取值是否正确、是否冗余，纠正欺诈字段或清理冗余字段；**不独立产生动作**，内嵌于 HEADEN 对象（ANTIFRAUD/GRAYLIST 参数）；**强耦合依赖 HTTP 头增强（License 82209786 + 82209777 双开）** |
| `feature_group` | `ANTIFRAUD` |
| `parent_feature_id` | —（业务归属"智能策略控制功能 → HTTP头防欺诈"分支） |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `variant_dimensions` | `["模式(插入+防欺诈双开 / 灰名单仅防欺诈不插入)", "ANTIFRAUD开关(ADD HEADEN ANTIFRAUD=ENABLE/DISABLE，内嵌于HTTP头增强命令)", "GRAYLIST开关(ADD HEADEN GRAYLIST=ENABLE 灰名单模式)", "触发方式(基于三四层特征 / 基于七层特征)", "过滤条件(FILTER三四层 vs L7FILTER URL+METHODTYPE+PROTBINDFLOWF)", "防欺诈字段类型(MSISDN/IMSI/APN/MSIP等，需为非标准HTTP头域名)", "POLICYTYPE轨道(A-HEADEN，共用HTTP头增强的动作机制)", "执行顺序控制(软参BIT1030控制防欺诈是否在头增强前执行)"]` |
| `first_release` | `UDG 20.0.0` |
| `requires_license` | `LKV3G5HHAS01` |
| `key_capabilities` | ① 字段存在性检测（不存在→正常插入；存在→进一步验证）② 取值正确性验证（不正确→纠正为正确值）③ 冗余字段清理（删除多余，保留一个）④ 灰名单模式（GRAYLIST=ENABLE 仅防欺诈不插入）⑤ 仅支持 HTTP/HTTPS，RTSP 不支持（族内唯一例外）⑥ **强耦合 License 依赖**：必须与 HTTP 头增强（82209777）双开 |
| `source_evidence_ids` | `EV-FK-AC-09`, `EV-CA-01` |

### 1.6 重定向族

#### GWFD-110281 用户Portal

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110281` |
| `feature_name` | `用户Portal` |
| `feature_summary` | 个人门户网站重定向，UDG 对用户 HTTP/WAP Get/Post 报文进行 SA 解析匹配规则后，构造 HTTP 301/302/303 重定向报文，将用户重定向到 IP Farm 中负荷分担选定的 Portal Server；captive/non-captive 模式交替；属 **SMARTREDIRECT 体系（URL 重写级别）** |
| `feature_group` | `REDIRECT` |
| `parent_feature_id` | `GWFD-020351 PCC基本功能`（PCC 触发链父节点） |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `variant_dimensions` | `["工作模式(captive模式/non-captive模式交替)", "重定向动作触发(POLICYTYPE=SMARTREDIRECT 与 PCC 联动)", "IP Farm负荷分担方式(ROUND_ROBIN/LEAST_RECENTLY_USED/LEAST_LOAD)", "HTTP重定向响应码(301/302/303，通过SET SRVCOMMONPARA配置)", "TCP RST拆链行为(软参BIT1473/BIT412控制)", "无法重定向时缺省动作(DEFAULTACT=BLOCK/PASS)", "协议类型(HTTP/WAP1.X/WAP2.0)", "IP版本(IPv4/IPv6)", "动作轨道(A-SMARTREDIRECT体系，L7 URL重写)"]` |
| `first_release` | `UDG 20.0.0` |
| `requires_license` | `LKV3G5CPPT01` |
| `key_capabilities` | ① captive/non-captive 模式交替（CAPMODETHRES）② HTTP 301/302/303 重定向构造 ③ IP Farm 负荷分担（3 种 LBMETHOD）④ ICMP 心跳检测（UP/DOWN 切换）⑤ 全部 DOWN 时 DEFAULTACT=BLOCK ⑥ 依赖 SA-Basic + SA-Web Browsing + SA-Mobile ⑦ **不支持 HTTPS / HTTP2.0** |
| `source_evidence_ids` | `EV-FK-AC-10`, `EV-CA-01` |

#### GWFD-110282 WebProxy

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110282` |
| `feature_name` | `Web Proxy` |
| `feature_summary` | L3 IP NAT 重定向，将用户浏览页面请求**目的 IP 替换为代理服务器 IP**（上行），响应报文**源 IP 还原回 Web 服务器 IP**（下行反向 NAT），对用户透明；通过代理服务器实现网络访问加速或病毒防护；属 **WEBPROXY 独立体系（L3 IP NAT 级别）**，与 Portal（SMARTREDIRECT L7）属不同轨道；**支持 HTTPS / HTTP2.0**（IP NAT 不依赖 L7） |
| `feature_group` | `REDIRECT` |
| `parent_feature_id` | `GWFD-020351 PCC基本功能`（PCC 触发链父节点） |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `variant_dimensions` | `["重定向动作触发(POLICYTYPE=WEBPROXY 与 PCC 联动)", "IP Farm负荷分担方式(ROUND_ROBIN/LEAST_RECENTLY_USED/LEAST_LOAD)", "NAT地址转换方向(上行目的IP→ProxyIP / 下行源IP→WebIP)", "代理服务器检测(ICMP心跳 UP/DOWN)", "无法重定向时缺省动作(报文丢弃/重新选server)", "在线用户server切换(软参BIT596控制)", "多WebProxy策略支持(软参BIT1541控制)", "动作优先级(系统固定优先级 vs Rule PRIORITY)", "IP版本(IPv4/IPv6)", "动作轨道(B-WEBPROXY独立体系，L3 IP NAT)"]` |
| `first_release` | `UDG 20.0.0` |
| `requires_license` | `LKV3G5WEBP01` |
| `key_capabilities` | ① L3 IP NAT 双向地址转换 ② IP Farm 负荷分担 ③ ICMP 心跳检测 ④ BLACKLISTRULE 黑名单规则（独有）⑤ LOGICINF 心跳接口 ⑥ **支持 HTTPS / HTTP2.0** ⑦ 与 IP 重定向区别：WebProxy 转换目的 IP（NAT），IP 重定向直接转发 |
| `source_evidence_ids` | `EV-FK-AC-11`, `EV-CA-01` |

#### GWFD-110283 DNS纠错

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110283` |
| `feature_name` | `DNS纠错` |
| `feature_summary` | **重定向的 DNS 变体（DNS Overwriting / DNS 重写）**，UDG 截获 DNS 服务器返回的失败应答消息，根据策略**构造一个新的 DNS 应答报文**给用户，将域名对应地址设置为第三方 Platform（如搜索引擎）的 IP，引导用户访问；DNS 解析层实现"重定向到指定页面"，介入时机最早（未建 TCP） |
| `feature_group` | `REDIRECT` |
| `parent_feature_id` | —（业务归属"重定向族 → DNS重写"分支，与 GWFD-110284 同属重定向族） |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `variant_dimensions` | `["重定向动作类型(DNS重写/DNS Overwriting)", "触发条件(DNS错误码ERRORCODEOP=EQUAL/GT等)", "策略下发方式(PCRF预定义规则下发 / 本地配置)", "Platform类型(搜索引擎 / 运营商Portal)", "过滤模式(FLOWFILTER单流 / FLOWFILTERGRP流组)", "扩展过滤器逻辑(EXTFLTTYPE AND/OR多域名)", "动作轨道(A-SMARTREDIRECT，POLICYNAME指向DNSOVERWRITING)"]` |
| `first_release` | `UDG 20.0.0` |
| `requires_license` | `LKV3G5DNSO01` |
| `key_capabilities` | ① DNS 响应报文重写（DNS Overwriting）② ERRORCODE 错误码触发（EQUAL 3 NXDOMAIN 等）③ EXTENDEDFILTER 多域名逻辑（AND/OR）④ POLICYTYPE=SMARTREDIRECT + POLICYNAME=DNSOVERWRITING（与 HTTP 智能重定向共用 POLICYTYPE，区分点在 POLICYNAME）⑤ 依赖 SA-Basic + SA-Network Administration（GWFD-110136）+ 内容计费基本功能（GWFD-020301）⑥ 仅 UDP DNS |
| `source_evidence_ids` | `EV-FK-AC-12`, `EV-CA-01` |

#### GWFD-110284 HTTP智能重定向

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110284` |
| `feature_name` | `HTTP智能重定向` |
| `feature_summary` | UDG 修改 HTTP 响应报文，将匹配规则的访问重定向到第三方服务器；多条件触发（URL/UserAgent/ContentType/URLPostfix/ErrorCode 范围 AND 逻辑组合）；构造 302 重定向报文可携带初始请求 URL、MSISDN、IMEI、IMSI、用户 IP 等信息；重定向族的 L7 HTTP 响应层实现 |
| `feature_group` | `REDIRECT` |
| `parent_feature_id` | `GWFD-110101 SA-Basic`（HTTP 解析依赖父节点） |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `variant_dimensions` | `["重定向方式(HTTP响应改写 / 302 Location)", "目标类型(第三方服务器URL)", "触发条件(URL过滤 / user-agent / content-type / url-postfix / error-code范围)", "扩展过滤器组合(AND逻辑多条件)", "重定向携带信息(REQURLFLAG/IMSIFLAG/MSISDNFLAG/IMEIFLAG/IPFLAG)", "规则承载方式(预定义规则 / SMF动态下发)", "动作轨道(A-SMARTREDIRECT，POLICYNAME指向SMARTHTTPREDIR)"]` |
| `first_release` | `UDG 20.0.0` |
| `requires_license` | `LKV3G5SHPR01` |
| `key_capabilities` | ① HTTP 响应报文改写（302 Location）② EXTENDEDFILTER 多维匹配（URL/UserAgent/ContentType/URLPostfix/ErrorCode）③ REDIRAPPENDINFO 携带 MSISDN/IMSI/IMEI/IP ④ SMARTHTTPREDIR 动作策略对象 ⑤ POLICYTYPE=SMARTREDIRECT + POLICYNAME=SMARTHTTPREDIR（与 DNS 纠错共用 POLICYTYPE）⑥ 依赖 SA-Basic + SA-Web Browsing ⑦ **不支持 HTTPS / HTTP2.0** |
| `source_evidence_ids` | `EV-FK-AC-13`, `EV-CA-01` |

### 1.7 URL内容过滤层

#### GWFD-110471 URL过滤基本功能

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110471` |
| `feature_name` | `URL过滤基本功能` |
| `feature_summary` | 基于 ICAP Server 的 URL 分类数据库进行内容过滤，UDG 将用户访问的 URL 通过 ICAP 协议上送 ICAP Server 分析，ICAP Server 返回 Category ID 或直接动作，UDG 本地匹配套餐策略执行 **BLOCK / PERMIT / REDIRECT**；**轨道 B 独立体系**（CFTEMPLATE/CONTCATEGBIND.ACTION 显式指定动作），**唯一显式支持 PERMIT 的特性**；访问限制场景最晚发布的独有特性（UDG 20.10.2） |
| `feature_group` | `URL_FILTER` |
| `parent_feature_id` | `GWFD-020351 PCC基本功能`（PCC 触发链父节点，但动作不走 PCCPOLICYGRP） |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `variant_dimensions` | `["匹配模式(分类匹配模式 / 直接动作模式)", "动作类型(BLOCK阻塞 / PERMIT放行 / REDIRECT重定向)", "协议类型(HTTP/WAP1.X/WAP2.0/HTTPS-非加密QUIC仅SNI)", "粒度(APN级SET APNCFFUNC / 全局SET GLBCFFUNC)", "ICAP Server部署(单机 / 服务器组+主备)", "是否启用本地cache(SET CFCACHEPARA)", "缺省动作来源(CFTEMPLATE.ACTION vs CONTCATEGBIND.ACTION)", "动作轨道(B-URL过滤独立体系，动作不走PCCPOLICYGRP)"]` |
| `first_release` | `UDG 20.10.2` |
| `requires_license` | `LKV3G5UFBF01` |
| `key_capabilities` | ① ICAP REQMOD URL 上送 ② 分类匹配 / 直接动作双模式 ③ CFTEMPLATE 模板级缺省动作（BLOCK/PERMIT/REDIRECT）④ CONTCATEGBIND 分类级精确动作 ⑤ 独立配置体系（VPNInst + ICAP 系列 5 + CF 系列 7 = 13 个独有对象）⑥ **唯一显式 PERMIT**（白名单机制，轨道 A 不具备）⑦ HTTPS 仅 SNI（加密固有限制）⑧ APN 级 / 全局开关 ⑨ CFCACHEPARA 本地缓存减少 ICAP 交互 |
| `source_evidence_ids` | `EV-FK-AC-14`, `EV-CA-01` |

### 1.8 接入控制触发层（UNC）

#### WSFD-211001 基于初始接入位置的策略控制

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-211001` |
| `feature_name` | `基于初始接入位置的策略控制` |
| `feature_summary` | UNC 侧**位置条件触发特性**，根据用户激活时的位置信息（ULI）匹配对应的带宽/访问限制策略；支持动态 PCC（Gx/N7，PCRF/PCF 决策）和本地 PCC（PFCP，GGSN-C/PGW-C/SMF 本地决策）双模式；本身不产生动作，下发的策略由 PGW-U/UPF 执行（可激活 UDG 侧重定向/阻塞/带宽控制） |
| `feature_group` | `ACCESS_CTRL_TRIGGER` |
| `parent_feature_id` | `WSFD-109101 PCC基本功能（UNC）`（强依赖） |
| `applicable_nf_map` | `{"UNC": ["SMF", "PGW-C", "GGSN-C"]}` |
| `variant_dimensions` | `["PCC模式(动态PCC-Gx/N7接口 vs 本地PCC-PFCP接口)", "PCRF/PCF规则类型(动态规则 / 预定义规则 / 无PCRF)", "位置类型(CGI-2/3G / ECGI-4G / NCGI-5G)", "制式(2G/3G/4G/5G)", "是否分时段(灵活时间机制，规则携带时间范围)", "位置兜底(SGSN/MME/AMF未上报ULI时取MCC+MNC)", "决策方(PCRF/PCF vs GGSN-C/PGW-C/SMF本地)", "绑定关系已存在与否(MOD UPBINDUPG vs ADD UPBINDUPG)", "动作轨道(A-PCC体系，UNC侧位置触发)"]` |
| `first_release` | `UNC 20.3.0`（v01 4G PGW-C）/ `UNC 20.7.0`（v02 5G SMF） |
| `requires_license` | `LKV2PCIAL01` |
| `key_capabilities` | ① ULI 位置匹配（CGI/ECGI/NCGI）② 动态 PCC（Gx/N7）+ 本地 PCC（PFCP）双模式 ③ USRLOCATION→USRLOCATIONGRP→UPBINDUPG→APNUSRPROFG→USERPROFILE→带宽规则位置组绑定链 ④ 位置兜底（MCC+MNC）⑤ 灵活时间机制（规则携带时间范围）⑥ **强依赖 PCC（UNC）**：License 82207979 必须同时开启 ⑦ 本地 PCC 场景额外依赖 WSFD-211005 带宽控制（UNC） |
| `source_evidence_ids` | `EV-FK-AC-15`, `EV-CA-01` |

### 1.9 接入控制辅助特性（UNC，4 个，U-H-02 补实例化）

> **修复说明（U-H-02）**：CS-AC-07 接入控制方案的 `uses_feature` 引用了 WSFD-106003/WSFD-105003/WSFD-106005/WSFD-105006 4 个 UNC Feature，但原 02 仅实例化 15 个 Feature（UDG 11 + UNC 4），导致跨层引用悬空。本节补实例化 4 个 UNC 侧接入控制辅助特性（注册阶段 SAR/区域漫游/ODB + 会话阶段服务区域限制），均为 AMF/SMF 侧粗粒度准入控制，与 WSFD-211001 位置触发共同构成 UNC 侧接入控制能力。补全后访问限制场景 Feature 总数 = **19（UDG 11 + UNC 8）**。
> **证据来源**：`feature-knowledge/cross-topic-analysis.md` §6.3 CS-AC-07（uses_feature 清单）+ §3 位置/接入控制章节（SAR/SERV_AREA_CH/ODB 事件触发器）。
> **Evidence ID 约定（★ P5 批次 3 闭环）**：4 个特性尚未单独建档特性知识文件（feature-knowledge/ 无独立 .md），P5 批次 1 曾暂用 `EV-CA-AC-02`（cross-topic-analysis.md）+ `EV-CA-01`（cross-feature-analysis.md）作为 `source_evidence_ids` 占位；**P5 批次 3 已为 4 个特性分配独立 `EV-FK-AC-16~19` 并在 `06-evidence-index.md` §2.8 注册**，path 暂锚定 `cross-topic-analysis.md#§6.3-CS-AC-07`，本节各 Feature 的 `source_evidence_ids` 已同步更新为对应主 ID。后续若为 4 个特性单独建档，仅需更新 06 §2.8 的 path 字段。

#### WSFD-106003 用户接入控制（AMF，SAR 服务区限制）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-106003` |
| `feature_name` | `用户接入控制（AMF）` |
| `feature_summary` | UNC 侧 AMF 注册阶段的**移动接入控制辅助特性**（接入控制辅助特性），基于 SAR（Service Area Restrictions，服务区限制）/RAT/核心网类型对用户执行粗粒度准入决策（拒绝接入或限制业务）；本身在注册阶段执行（不同于 WSFD-211001 会话阶段位置触发），是 CS-AC-07 接入控制方案的组成特性 |
| `feature_group` | `ACCESS_CTRL_AMF` |
| `parent_feature_id` | —（UNC 侧 AMF 独立接入控制能力） |
| `applicable_nf_map` | `{"UNC": ["AMF", "MME"]}` |
| `variant_dimensions` | `["限制级别(系统级/用户级/区域级)", "限制对象(RAT/核心网/号段/单用户/TAI 允许列表/TAI 禁止列表)", "触发事件(LOC_CH/SERV_AREA_CH/PRA_CH/PLMN_CH)", "决策方(UDM 签约 vs AMF 本地配置)"]` |
| `first_release` | `UNC 20.3.0` |
| `requires_license` | —（接入控制辅助特性，未在独立 License 表列出） |
| `key_capabilities` | ① SAR 服务区限制（TAI 允许/禁止列表）② 注册阶段准入决策（接受/拒绝）③ ULI 上报到 PCF ④ 漫游场景 PLMN 判别 |
| `source_evidence_ids` | `EV-FK-AC-16`, `EV-CA-AC-01`（★ P5 批次 3：原占位 EV-CA-AC-02 已替换为独立 EV-FK-AC-16） |
| **复用标注** | 接入控制辅助特性，与 WSFD-211001 协同（前者注册阶段粗粒度，后者会话阶段位置触发） |

#### WSFD-105003 区域漫游限制（AMF）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-105003` |
| `feature_name` | `区域漫游限制（AMF）` |
| `feature_summary` | UNC 侧 AMF 注册阶段的**区域漫游限制辅助特性**（接入控制辅助特性），基于 PLMN/号段/ODB 对用户执行漫游准入决策（如限制非签约区域接入、漫游用户业务限制）；典型场景"区域套餐（只能在 A 市用）、漫游限制、出国引导签约"；本身不产生数据面动作，仅决定是否允许注册/会话建立 |
| `feature_group` | `ACCESS_CTRL_AMF` |
| `parent_feature_id` | —（UNC 侧 AMF 独立接入控制能力） |
| `applicable_nf_map` | `{"UNC": ["AMF", "MME", "UDM"]}` |
| `variant_dimensions` | `["限制维度(PLMN/号段/ODB)", "签约来源(UDM 签约数据 vs AMF 本地配置)", "触发事件(PLMN_CH/PRA_CH)", "限制范围(单用户/号段/区域)"]` |
| `first_release` | `UNC 20.3.0` |
| `requires_license` | —（接入控制辅助特性，未在独立 License 表列出） |
| `key_capabilities` | ① PLMN 漫游判别 ② 号段签约限制 ③ ODB（Operator Determined Barring）闭锁 ④ 区域套餐签约匹配 |
| `source_evidence_ids` | `EV-FK-AC-17`, `EV-CA-AC-01`（★ P5 批次 3：原占位 EV-CA-AC-02 已替换为独立 EV-FK-AC-17） |
| **复用标注** | 接入控制辅助特性，与 WSFD-106003 同属 AMF 注册阶段准入决策 |

#### WSFD-106005 支持 ODB（AMF）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-106005` |
| `feature_name` | `支持 ODB（AMF）` |
| `feature_summary` | UNC 侧 AMF 的**ODB（Operator Determined Barring，运营商决定闭锁）辅助特性**（接入控制辅助特性），支持运营商对单用户/号段执行所有权闭锁（如欠费禁用、违规用户禁用），可作用于注册阶段和会话阶段；典型场景"ODB 欠费禁用、拥塞小区流控" |
| `feature_group` | `ACCESS_CTRL_AMF` |
| `parent_feature_id` | —（UNC 侧 AMF 独立接入控制能力） |
| `applicable_nf_map` | `{"UNC": ["AMF", "MME", "SMF", "UDM"]}` |
| `variant_dimensions` | `["作用阶段(注册阶段/会话阶段)", "闭锁粒度(单用户/号段)", "闭锁类型(全部业务/特定 APN)", "签约来源(UDM 签约 ODB 数据)", "触发事件(ODB 签约变更)"]` |
| `first_release` | `UNC 20.3.0` |
| `requires_license` | —（接入控制辅助特性，未在独立 License 表列出） |
| `key_capabilities` | ① ODB 签约数据查询（UDM）② 注册阶段拒绝接入（ODB 全闭锁）③ 会话阶段限制特定 APN（ODB APN 级）④ 实时生效（UDM 推送变更） |
| `source_evidence_ids` | `EV-FK-AC-18`, `EV-CA-AC-01`（★ P5 批次 3：原占位 EV-CA-AC-02 已替换为独立 EV-FK-AC-18） |
| **复用标注** | 接入控制辅助特性，跨注册/会话两阶段；与 WSFD-105003 区域漫游限制共用 ODB 数据源 |

#### WSFD-105006 会话服务区域限制（SMF）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-105006` |
| `feature_name` | `会话服务区域限制` |
| `feature_summary` | UNC 侧 SMF 的**会话阶段服务区域限制辅助特性**（接入控制辅助特性），基于签约 SAR/服务区域（Tracking Area）对已建立会话的用户执行区域级业务限制（如限制会话只能在签约区域使用，离开则释放或限速）；与 AMF 侧 WSFD-106003（注册阶段 SAR）互补，前者管注册准入，后者管会话保持 |
| `feature_group` | `ACCESS_CTRL_SMF` |
| `parent_feature_id` | `WSFD-109101 PCC基本功能（UNC）`（SMF 侧 PCC 承载） |
| `applicable_nf_map` | `{"UNC": ["SMF", "PGW-C", "GGSN-C"]}` |
| `variant_dimensions` | `["作用阶段(会话阶段)", "限制维度(SAR/服务区域 Tracking Area)", "触发事件(SERV_AREA_CH/USER_LOCATION_CH)", "限制动作(释放会话/限速/重定向)", "决策方(UDM 签约 vs PCF 决策 vs SMF 本地)"]` |
| `first_release` | `UNC 20.5.0` |
| `requires_license` | —（接入控制辅助特性，未在独立 License 表列出） |
| `key_capabilities` | ① 服务区域（TAI）匹配 ② 会话级 SAR 执行（释放/限速/重定向）③ SERV_AREA_CH 事件触发 ④ 与 WSFD-211001 位置触发协同（前者会话级区域限制，后者位置变化触发策略下发） |
| `source_evidence_ids` | `EV-FK-AC-19`, `EV-CA-AC-01`（★ P5 批次 3：原占位 EV-CA-AC-02 已替换为独立 EV-FK-AC-19） |
| **复用标注** | 接入控制辅助特性，SMF 侧会话阶段；与 AMF 侧 WSFD-106003 互补构成"注册准入 + 会话保持"完整接入控制链 |



---

## 2. Feature depends_on 关系边（17 条）

### 2.1 UDG 侧依赖（14 条）

| 源 Feature | 关系 | 目标 Feature | 依赖类型 | 依赖理由 |
|-----------|------|-------------|----------|----------|
| GWFD-020351 (PCC) | `depends_on` | GWFD-110101 (SA-Basic) | `mandatory` | PCC 前置条件：完成业务感知配置 |
| GWFD-020357 (ADC) | `depends_on` | GWFD-110101 (SA-Basic) | `mandatory` | ADC 基于 SA 执行 L7 业务检测 |
| GWFD-020357 (ADC) | `depends_on` | GWFD-020351 (PCC) | `mandatory` | PCRF/PCF 下发携带 Application ID 的 PCC 规则 |
| GWFD-110261 (HTTP头增强) | `depends_on` | GWFD-110101 (SA-Basic) | `mandatory` | 需对 HTTP 报文解析执行头增强；SA-Basic 是所有 SA 协议解析基础 |
| GWFD-110262 (RTSP头增强) | `depends_on` | GWFD-110101 (SA-Basic) | `mandatory` | 需对 RTSP 报文解析执行头增强 |
| GWFD-110263 (HTTPS头增强) | `depends_on` | GWFD-110101 (SA-Basic) | `mandatory` | 需对 HTTPS 报文解析执行头增强 |
| GWFD-110281 (用户Portal) | `depends_on` | GWFD-110101 (SA-Basic) | `mandatory` | 需对 HTTP/WAP Get/Post 报文 SA 解析匹配规则 |
| GWFD-110282 (WebProxy) | `depends_on` | GWFD-110101 (SA-Basic) | `mandatory` | 需 SA 解析获得 Web Proxy 动作和重定向地址 |
| GWFD-110283 (DNS纠错) | `depends_on` | GWFD-110101 (SA-Basic) | `mandatory` | 需 SA 解析获得 URL + DNS 报文解析 |
| GWFD-110284 (HTTP智能重定向) | `depends_on` | GWFD-110101 (SA-Basic) | `mandatory` | 需 SA 解析和规则匹配 |
| GWFD-110401 (HTTP头防欺诈) | `depends_on` | GWFD-110261 (HTTP头增强) | `mandatory` | **License 强耦合**：启用防欺诈必须开启 HTTP 头增强（82209786 + 82209777 双开）；共用 HEADEN 对象（ANTIFRAUD/GRAYLIST 内嵌） |
| GWFD-110401 (HTTP头防欺诈) | `depends_on` | GWFD-110101 (SA-Basic) | `mandatory` | 需识别和解析 HTTP 报文（SA-Web Browsing） |
| GWFD-110471 (URL过滤) | `depends_on` | GWFD-110101 (SA-Basic) | `mandatory` | 需 SA 解析提取 URL（SA-Web Browsing + SA-Mobile + HTTP2.0 Host 识别） |
| GWFD-110471 (URL过滤) | `depends_on` | GWFD-020351 (PCC) | `mandatory` | RULE 用 POLICYTYPE=PCC 触发 URL 过滤业务（动作虽走轨道 B，但规则承载仍依赖 PCC RULE 体系） |

### 2.2 UNC 侧依赖（3 条）

| 源 Feature | 关系 | 目标 Feature | 依赖类型 | 依赖理由 |
|-----------|------|-------------|----------|----------|
| WSFD-211001 (位置触发) | `depends_on` | WSFD-109101 (PCC UNC) | `mandatory` | **License 强依赖**：PCC 策略下发承载，License 82207979 必须同时开启 |
| WSFD-211001 (位置触发) | `depends_on` | WSFD-211005 (带宽控制 UNC，复用) | `optional` | 本地 PCC 场景（无 PCRF/PCF）时需要带宽控制（UNC）提供规则来源 |
| WSFD-109101 (PCC UNC) | `depends_on` | GWFD-020351 (PCC UDG) | `mandatory` | UNC 通过 N4 向 UDG 下发 PCC 规则，UDG 侧 PCC 承载执行（跨产品 CU 协作） |

### 2.3 UNC 接入控制辅助特性依赖（4 条，U-H-02 补实例化）

> **修复说明（U-H-02）**：§1.9 新增的 4 个 UNC 接入控制辅助特性参与 CS-AC-07 uses_feature 关系，需补 depends_on 边表达与 WSFD-211001 / WSFD-109101 的协同关系。

| 源 Feature | 关系 | 目标 Feature | 依赖类型 | 依赖理由 |
|-----------|------|-------------|----------|----------|
| WSFD-106003 (用户接入控制 AMF) | `depends_on` | WSFD-109101 (PCC UNC) | `mandatory` | AMF 侧准入决策结果通过 PCF/N7 下发，需 PCC UNC 承载；与 WSFD-211001 同属 CS-AC-07 方案 |
| WSFD-105003 (区域漫游限制 AMF) | `depends_on` | WSFD-106003 (用户接入控制 AMF) | `optional` | 区域漫游限制是用户接入控制的子能力，共用 UDM 签约数据源（PLMN/号段/ODB） |
| WSFD-106005 (支持 ODB AMF) | `depends_on` | WSFD-106003 (用户接入控制 AMF) | `optional` | ODB 闭锁是用户接入控制的子能力，共用 UDM 签约 ODB 数据 |
| WSFD-105006 (会话服务区域限制 SMF) | `depends_on` | WSFD-211001 (位置触发) | `mandatory` | SMF 侧会话阶段服务区域限制依赖位置触发特性（USRLOCATION/USRLOCATIONGRP）的位置匹配能力；两者协同构成"注册准入 + 会话保持"完整接入控制链 |

> **辐射中心**：SA-Basic（GWFD-110101）被 **10 个独有特性直接依赖**（UDG 侧全部独有特性 + 头防欺诈）；PCC（GWFD-020351）被 ADC/头防欺诈/URL 过滤/Portal/WebProxy 等 5 个特性依赖（动作载体）。

---

## 3. License 实例化（15 个：UDG 12 + UNC 3）

### 3.1 UDG 侧 License（12 个）

| `license_id` | `license_name` | 对应 Feature | `status` | 复用标注 |
|---------------|----------------|-------------|----------|---------|
| `LKV3G5SABS01` | SA-Basic (82209749) | GWFD-110101 | `active` | **三场景共享**（基础层） |
| `LKV3G5PCCB01` | PCC基本功能 (82209825) | GWFD-020351 | `active` | **三场景共享**（基础层） |
| `LKV3G5ADCF01` | 增强的ADC基本功能 (82200AFK) | GWFD-020357 | `active` | 访问限制独有（ADC UDG 侧） |
| `LKV3G5HTHE01` | HTTP头增强 (82209777) | GWFD-110261 | `active` | 访问限制独有 |
| `LKV3G5RTHE01` | RTSP头增强 (82209778) | GWFD-110262 | `active` | 访问限制独有 |
| `LKV3G5HTSE01` | HTTPS头增强 (82209779) | GWFD-110263 | `active` | 访问限制独有 |
| `LKV3G5HHAS01` | HTTP头防欺诈 (82209786) | GWFD-110401 | `active` | 访问限制独有（**强耦合 LKV3G5HTHE01**） |
| `LKV3G5CPPT01` | 用户Portal (82209780) | GWFD-110281 | `active` | 访问限制独有 |
| `LKV3G5WEBP01` | Web Proxy (82209781) | GWFD-110282 | `active` | 访问限制独有 |
| `LKV3G5DNSO01` | DNS纠错 (82209782) | GWFD-110283 | `active` | 访问限制独有 |
| `LKV3G5SHPR01` | HTTP智能重定向 (82209783) | GWFD-110284 | `active` | 访问限制独有 |
| `LKV3G5UFBF01` | URL过滤基本功能 (82200FCP) | GWFD-110471 | `active` | 访问限制独有（轨道 B 核心） |

### 3.2 UNC 侧 License（3 个）

| `license_id` | `license_name` | 对应 Feature | `status` | 复用标注 |
|---------------|----------------|-------------|----------|---------|
| `LKV3W9SPCC11` | PCC基本功能 (82207979) | WSFD-109101 | `active` | **三场景共享**（基础层，含 SMF/PGW-C 和 AMF） |
| `LKV2BADCF01` | ADC基本功能 (82200BNK) | WSFD-109102 | `active` | **三场景共享**（ADC UNC 侧） |
| `LKV2PCIAL01` | 基于初始接入位置的策略控制 (82200BNQ) | WSFD-211001 | `active` | 访问限制独有（UNC） |

### 3.3 License 依赖链

```
基础 License（必须先开启）
├── UDG: LKV3G5SABS01 (SA-Basic) + LKV3G5PCCB01 (PCC)
└── UNC: LKV3W9SPCC11 (PCC SMF/PGW-C)
        │
        ▼
功能 License（在基础 License 之上叠加）
├── UDG: 9 个功能 License（ADC/头增强族3/头防欺诈/重定向族4/URL过滤）
└── UNC: 2 个功能 License（ADC UNC / 位置触发）

强耦合 License 对：
└── LKV3G5HHAS01 (头防欺诈) + LKV3G5HTHE01 (HTTP头增强) — 必须双开
```

---

## 4. License → Feature 映射（requires_license 边，15 条）

> 每个 Feature 恰好对应 1 个主要 License。License 通过 `SET LICENSESWITCH` 命令开启。

| Feature | `requires_license` | 产品 | 复用 |
|---------|-------------------|------|------|
| GWFD-110101 | `LKV3G5SABS01` | UDG | 共享 |
| GWFD-020351 | `LKV3G5PCCB01` | UDG | 共享 |
| GWFD-020357 | `LKV3G5ADCF01` | UDG | 独有 |
| GWFD-110261 | `LKV3G5HTHE01` | UDG | 独有 |
| GWFD-110262 | `LKV3G5RTHE01` | UDG | 独有 |
| GWFD-110263 | `LKV3G5HTSE01` | UDG | 独有 |
| GWFD-110401 | `LKV3G5HHAS01` | UDG | 独有 |
| GWFD-110281 | `LKV3G5CPPT01` | UDG | 独有 |
| GWFD-110282 | `LKV3G5WEBP01` | UDG | 独有 |
| GWFD-110283 | `LKV3G5DNSO01` | UDG | 独有 |
| GWFD-110284 | `LKV3G5SHPR01` | UDG | 独有 |
| GWFD-110471 | `LKV3G5UFBF01` | UDG | 独有 |
| WSFD-109101 | `LKV3W9SPCC11` | UNC | 共享 |
| WSFD-109102 | `LKV2BADCF01` | UNC | 共享 |
| WSFD-211001 | `LKV2PCIAL01` | UNC | 独有 |

---

## 5. FeatureRule（8 条）

> **Schema §9.6 字段（U-H-05 修复后 12 列齐全）**：rule_id / owner_ref_type（enum: feature/subfeature）/ owner_ref / rule_name / rule_type（合法枚举：dependency_rule / task_selection_rule / naming_rule / consistency_rule / validation_rule / restriction_rule / scope_rule）/ rule_expression_mode（explicit/implicit）/ rule_source_kind（principle/config/design/ops/case/restriction）/ rule_logic / violation_effect / status / source_evidence_ids。
> **扩展字段**：`severity`（critical/warning/info）非 Schema §9.6 FeatureRule 标准字段，参考 Schema §11.6 CommandRule.severity 作为运维分级补充列保留。

| `rule_id` | `owner_ref_type` | `owner_ref` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `rule_logic` | `violation_effect` | `status` | `source_evidence_ids` | `severity` |
|-----------|------------------|-------------|-------------|-------------|------------------------|--------------------|--------------|-------------------|----------|-----------------------|------------|
| `FR-AC-01` | `feature` | 多 Feature（ADC/头增强族/重定向族/防欺诈/URL过滤） | 跨 NF FlowFilter/RULENAME 一致性 | `consistency_rule` | `explicit` | `config` | 凡涉及动态 PCC（PCRF/PCF 下发预定义规则）的特性，RULENAME/appid/FlowFilterName 必须在 UDG + UNC + PCRF/PCF 三网元保持一致；URL 过滤还需 URL 过滤套餐名、Category ID 与 ICAP Server 一致；位置触发需 ULI（CGI/ECGI/NCGI）取值在 UNC + RAN + PCRF/PCF 一致 | 规则名不一致将导致 PCRF/PCF 下发规则无法在 UDG 匹配，访问限制动作失效 | `active` | `EV-FK-AC-04, EV-FK-AC-06, EV-FK-AC-12, EV-FK-AC-14, EV-CA-01` | critical |
| `FR-AC-02` | `feature` | 多 Feature（轨道 A 全部 8 特性） | RULE.POLICYTYPE 决定动作轨道（★双轨机制+五子轨） | `restriction_rule` | `explicit` | `design` | **双轨道 + 五子轨**：轨道 A 以 `RULE.POLICYTYPE` 为动作类型核心区分（5 子轨）：`POLICYTYPE=ADC`（应用检测，直接在 RULE）/ `POLICYTYPE=PCC`（标准 PCC，POLICYNAME→PCCPOLICYGRP）/ `POLICYTYPE=HEADEN`（POLICYNAME→HEADEN 对象）/ `POLICYTYPE=SMARTREDIRECT`（POLICYNAME→SMARTHTTPREDIR 或 DNSOVERWRITING）/ `POLICYTYPE=WEBPROXY`（POLICYNAME→IPFARM）；轨道 B（URL 过滤）RULE 虽用 POLICYTYPE=PCC 但动作走 CFTEMPLATE/CONTCATEGBIND.ACTION（BLOCK/PERMIT/REDIRECT）。同一 RULENAME 值在不同 POLICYTYPE 间**不能重复** | POLICYTYPE 配置错误将导致动作无法生效（如误用 PCC 而实际需 HEADEN）；RULENAME 重复将导致规则冲突 | `active` | `EV-CA-01, EV-FK-AC-02, EV-FK-AC-04` | critical |
| `FR-AC-03` | `feature` | GWFD-110401（头防欺诈）→ GWFD-110261（HTTP头增强） | 头防欺诈强耦合依赖头增强 | `dependency_rule` | `explicit` | `config` | 启用 HTTP 头防欺诈（LKV3G5HHAS01）**必须同时开启** HTTP 头增强（LKV3G5HTHE01）；共用 HEADEN 对象（ANTIFRAUD/GRAYLIST 参数内嵌于 ADD HEADEN 命令）；执行顺序：防欺诈检测 → 字段纠正/冗余清理 → 头增强插入；RTSP 头增强不支持防欺诈（族内唯一例外） | 未双开 License 将导致防欺诈功能不可用；防欺诈未前置将导致欺诈字段被直接插入 | `active` | `EV-FK-AC-09, EV-FK-AC-06, EV-CA-01` | critical |
| `FR-AC-04` | `feature` | GWFD-020357（ADC） | ADC 是 L7 动作特性的横切前置（应用感知层） | `dependency_rule` | `implicit` | `design` | ADC 提供"看见"而非"动作"——所有需要基于应用/URL 做判断的特性（头增强族/重定向族/URL 过滤/头防欺诈）虽不显式强依赖 ADC，但 ADC 是"所有 L7 应用级控制"的事实前置（通过 SA 引擎）；ADC 不匹配规则时兜底阻塞 | 未启用 ADC 时，L7 应用级检测能力受限；但头增强族仅需 SA-Basic + 具体 SA 协议子特性即可工作（非显式强依赖） | `active` | `EV-FK-AC-04, EV-CA-01` | warning |
| `FR-AC-05` | `feature` | 多 Feature（头增强/重定向族大部分） | 动态规则不支持七层（HTTPS/HTTP2.0 限制） | `restriction_rule` | `explicit` | `restriction` | 凡是需要在 L7 解析 HTTP 内容的特性（HTTP 头增强/HTTP 智能重定向/用户 Portal）**不支持 HTTPS / HTTP2.0**；WebProxy 在 L3 工作不受加密影响（支持 HTTPS/HTTP2.0）；HTTPS 头增强通过 SSL Extension（TLV）部分支持；URL 过滤 HTTPS 仅能基于 SNI（加密固有限制） | 对 HTTPS 业务使用 HTTP 头增强/智能重定向/Portal 将不生效；需改用 HTTPS 头增强 / WebProxy / URL 过滤 SNI | `active` | `EV-FK-AC-06, EV-FK-AC-10, EV-FK-AC-13, EV-FK-AC-14, EV-CA-01` | warning |
| `FR-AC-06` | `feature` | GWFD-110283（DNS纠错）+ GWFD-110284（HTTP智能重定向） | 共用 POLICYTYPE=SMARTREDIRECT 区分 | `naming_rule` | `explicit` | `config` | HTTP 智能重定向和 DNS 纠错**共用 POLICYTYPE=SMARTREDIRECT**，区分点在 POLICYNAME 指向对象：HTTP 智能重定向→SMARTHTTPREDIR，DNS 纠错→DNSOVERWRITING；两者共用 EXTENDEDFILTER 和 ERRORCODE 配置对象（但错误码语义不同：HTTP 错误码 vs DNS 错误码如 NXDOMAIN） | POLICYNAME 指向错误对象类型将导致重定向动作类型错误 | `active` | `EV-FK-AC-12, EV-FK-AC-13, EV-CA-01` | warning |
| `FR-AC-07` | `feature` | GWFD-110471（URL过滤） | URL 过滤独立轨道 B（不走 PCCPOLICYGRP） | `restriction_rule` | `explicit` | `design` | URL 过滤的 RULE 虽用 POLICYTYPE=PCC，但实际 BLOCK/PERMIT/REDIRECT 动作**不走 PCCPOLICYGRP**，而走 CFTEMPLATE.ACTION（模板级缺省）和 CONTCATEGBIND.ACTION（分类级精确）；URL 过滤是访问限制场景**唯一显式支持 PERMIT** 的特性（轨道 A 主要是"不做动作"或"做阻塞/重定向"）；依赖外部 ICAP Server（引入独立配置体系） | 将 URL 过滤动作误配在 PCCPOLICYGRP 将不生效；无 ICAP Server 时整个 URL 过滤功能不可用 | `active` | `EV-FK-AC-14, EV-CA-01` | critical |
| `FR-AC-08` | `feature` | GWFD-110281（Portal）+ GWFD-110282（WebProxy） | IP Farm 全部 DOWN 处理差异 | `validation_rule` | `explicit` | `ops` | Portal 和 WebProxy 共享 IP Farm 服务器集群机制（整机 64 个 IP Farm，每个 512 IP），全部 DOWN 时处理不同：**Portal 默认 DEFAULTACT=BLOCK**（阻塞用户），**WebProxy 不做重定向**（业务按原路径走）；告警 ALM-81034/ALM-81035；心跳检测由 HEALTHSUCCLIMIT/HEALTHFAILLIMIT 控制 | Portal 全 DOWN 未配 DEFAULTACT 将默认阻塞；WebProxy 全 DOWN 时业务回退到原始路径（可能非预期） | `active` | `EV-FK-AC-10, EV-FK-AC-09, EV-CA-01` | warning |

---

## 6. FeatureTaskOrderEdge（核心 Feature 的 Task 展开顺序）

> **Schema §9.7 字段**：edge_id / owner_ref_type / owner_ref / from_task_ref / to_task_ref / relation_type（precedes / depends_on / fallback_to / must_be_last）/ condition_ref / requiredness / priority_hint / propagated_context / source_evidence_ids。
> **说明**：详细 Task 定义见 `03-task-layer.md`。task_ref 统一指向 03 权威编号（generic `T-001~T-008` + 独有 `T-AC-101~T-AC-109`），U-H-01 已修复全部旧编号 `T-AC-201~504`。
> **ID 前缀**：FTOE-AC-，顺序编号。访问限制场景 5 个核心 Feature 给出 task 编排边。

### 6.1 GWFD-020357 ADC（UDG 侧配置链，5 条边）

> **Task 编号映射（U-H-01 修复）**：原 `T-AC-007/008/006` 为旧编号，已统一为 generic `T-007/T-008/T-006`；原 `T-AC-101~103` 含义错位（旧 T-AC-101=三四层过滤、T-AC-102=ADC规则、T-AC-103=计费属性），现按 03-task-layer.md 权威定义重新映射（T-AC-101=配置ADC检测参数与规则、T-AC-107=配置PCC动作组/计费属性）。

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `requiredness` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------|----------------------|
| `FTOE-AC-001` | `Feature` | `GWFD-020357` | `T-007` | `T-008` | `precedes` | `required` | `EV-FK-AC-04, EV-CA-01` |
| `FTOE-AC-002` | `Feature` | `GWFD-020357` | `T-008` | `T-002` | `precedes` | `required` | `EV-FK-AC-04, EV-CA-01` |
| `FTOE-AC-003` | `Feature` | `GWFD-020357` | `T-002` | `T-AC-101` | `precedes` | `required` | `EV-FK-AC-04, EV-CA-01` |
| `FTOE-AC-004` | `Feature` | `GWFD-020357` | `T-AC-101` | `T-AC-107` | `precedes` | `required` | `EV-FK-AC-04, EV-CA-01` |
| `FTOE-AC-005` | `Feature` | `GWFD-020357` | `T-AC-107` | `T-006` | `must_be_last` | `required` | `EV-FK-AC-04, EV-CA-01` |

> **Task 说明（按 03-task-layer.md 权威定义）**：T-007=License 开启（SA-Basic + PCC + ADC，generic），T-008=SA 特征库加载（LOD SIGNATUREDB/LOD PARSERDB，generic），T-002=配置流过滤器与绑定（FLOWFILTER/FLTBINDFLOWF，generic），T-AC-101=配置 ADC 检测参数与规则（ADCPARA + ADD RULE:POLICYTYPE=ADC，feature_specific），T-AC-107=配置 PCC 动作组（URR/URRGROUP/PCCPOLICYGRP 含 ADCMUTEFLAG，feature_specific），T-006=SET REFRESHSRV:REFRESHTYPE=ALL（60s 后生效，generic，must_be_last）

### 6.2 GWFD-110261 HTTP头增强 + GWFD-110401 头防欺诈（UDG 侧配置链，6 条边，含防欺诈强耦合）

> **Task 编号映射（U-H-01 修复）**：原 `T-AC-201~204` 在 03-task-layer.md 中无定义，按动作语义重新映射：T-AC-201(三四层+七层过滤)→generic `T-002`；T-AC-202(HEADEN 对象)→feature_specific `T-AC-102`（03 权威定义含 ANTIFRAUD/GRAYLIST 子模式）；T-AC-203(RULE:POLICYTYPE=HEADEN)→generic `T-003`；T-AC-204(头防欺诈子模式)→`T-AC-102` 内部子模式（不独立 Task，见 03 §2 T-AC-102 note）。防欺诈由 `depends_on` 表达强耦合前置（License 双开）。

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `requiredness` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------|----------------------|
| `FTOE-AC-006` | `Feature` | `GWFD-110261` | `T-007` | `T-008` | `precedes` | `required` | `EV-FK-AC-06, EV-CA-01` |
| `FTOE-AC-007` | `Feature` | `GWFD-110261` | `T-008` | `T-002` | `precedes` | `required` | `EV-FK-AC-06, EV-CA-01` |
| `FTOE-AC-008` | `Feature` | `GWFD-110261` | `T-002` | `T-AC-102` | `precedes` | `required` | `EV-FK-AC-06, EV-CA-01` |
| `FTOE-AC-009` | `Feature` | `GWFD-110261` | `T-AC-102` | `T-003` | `precedes` | `required` | `EV-FK-AC-06, EV-CA-01` |
| `FTOE-AC-010` | `Feature` | `GWFD-110401` | `T-007` | `T-AC-102` | `depends_on` | `required` | `EV-FK-AC-09, EV-CA-01` |
| `FTOE-AC-011` | `Feature` | `GWFD-110261` | `T-003` | `T-006` | `must_be_last` | `required` | `EV-FK-AC-06, EV-CA-01` |

> **Task 说明（按 03-task-layer.md 权威定义）**：T-007=License 开启（HTTP 头增强 82209777 + 头防欺诈 82209786 双开，generic，TR-AC-04 强耦合），T-008=SA 特征库 + 协议解析库加载（generic），T-002=配置流过滤器与绑定（FILTER/FLOWFILTER/L7FILTER/PROTBINDFLOWF，generic），T-AC-102=配置头增强对象（ADD HEADEN，含 ANTIFRAUD=ENABLE/GRAYLIST 子模式；头防欺诈检测前置→纠正/清理→插入由 BIT1030 控制顺序，feature_specific），T-003=配置 PCC 规则（ADD RULE:POLICYTYPE=HEADEN，POLICYNAME 指向 HEADEN 对象，generic），T-006=SET REFRESHSRV（generic，must_be_last）。头防欺诈 FTOE-AC-010 以 `depends_on` 表达 License 双开前置（非时序 precedes）。

### 6.3 GWFD-110284 HTTP智能重定向（UDG 侧配置链，4 条边）

> **Task 编号映射（U-H-01 修复）**：原 `T-AC-301~303` 在 03 中无定义，按动作语义重新映射：T-AC-301(EXTENDEDFILTER+ERRORCODE 多条件匹配)→generic `T-001`（规划业务分类与识别条件，输出 EXTENDEDFILTER/ERRORCODE 实例）；T-AC-302(SMARTHTTPREDIR+REDIRAPPENDINFO)→feature_specific `T-AC-103`（03 权威定义）；T-AC-303(RULE:POLICYTYPE=SMARTREDIRECT)→generic `T-003`。

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `requiredness` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------|----------------------|
| `FTOE-AC-012` | `Feature` | `GWFD-110284` | `T-007` | `T-001` | `precedes` | `required` | `EV-FK-AC-13, EV-CA-01` |
| `FTOE-AC-013` | `Feature` | `GWFD-110284` | `T-001` | `T-AC-103` | `precedes` | `required` | `EV-FK-AC-13, EV-CA-01` |
| `FTOE-AC-014` | `Feature` | `GWFD-110284` | `T-AC-103` | `T-003` | `precedes` | `required` | `EV-FK-AC-13, EV-CA-01` |
| `FTOE-AC-015` | `Feature` | `GWFD-110284` | `T-003` | `T-006` | `must_be_last` | `required` | `EV-FK-AC-13, EV-CA-01` |

> **Task 说明（按 03-task-layer.md 权威定义）**：T-007=License 开启（HTTP 智能重定向 82209783，generic），T-001=规划业务分类与识别条件（ADD EXTENDEDFILTER + ADD ERRORCODE，多条件 URL/UserAgent/ContentType/URLPostfix/ErrorCode AND 逻辑，generic），T-AC-103=配置 HTTP 智能重定向（ADD SMARTHTTPREDIR + ADD REDIRAPPENDINFO，POLICYNAME 指向 SMARTHTTPREDIR，feature_specific；TR-AC-02 与 DNS 纠错共用 POLICYTYPE=SMARTREDIRECT），T-003=配置 PCC 规则（ADD RULE:POLICYTYPE=SMARTREDIRECT，generic），T-006=SET REFRESHSRV（generic，must_be_last）

### 6.4 GWFD-110471 URL过滤（UDG 侧配置链，轨道 B，6 条边）

> **Task 编号映射（U-H-01 修复）**：原 `T-AC-401~405` 在 03 中无定义。轨道 B 的 ICAP 互通层 + CF 业务层全部由 feature_specific `T-AC-108`（配置 URL 过滤，ICAP 互通 + CF 模板/分类）承载（03 §3 权威定义，内部 16 条命令编排边见 03 §7.7）；四三层过滤→generic `T-002`；PCC 规则（POLICYTYPE=PCC 仅触发，动作不走 PCCPOLICYGRP）→generic `T-003`；计费属性→feature_specific `T-AC-107`；用户模板绑定→generic `T-004`。原链的"cache + 白名单"并入 T-AC-108 内部（CFCACHEPARA/CFWHITEURLLST/CFIPWHITELIST 均为 T-AC-108 command_refs）。

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `requiredness` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------|----------------------|
| `FTOE-AC-016` | `Feature` | `GWFD-110471` | `T-007` | `T-AC-108` | `precedes` | `required` | `EV-FK-AC-14, EV-CA-01` |
| `FTOE-AC-017` | `Feature` | `GWFD-110471` | `T-AC-108` | `T-002` | `precedes` | `required` | `EV-FK-AC-14, EV-CA-01` |
| `FTOE-AC-018` | `Feature` | `GWFD-110471` | `T-002` | `T-AC-107` | `precedes` | `required` | `EV-FK-AC-14, EV-CA-01` |
| `FTOE-AC-019` | `Feature` | `GWFD-110471` | `T-AC-107` | `T-003` | `precedes` | `required` | `EV-FK-AC-14, EV-CA-01` |
| `FTOE-AC-020` | `Feature` | `GWFD-110471` | `T-003` | `T-004` | `precedes` | `required` | `EV-FK-AC-14, EV-CA-01` |
| `FTOE-AC-021` | `Feature` | `GWFD-110471` | `T-004` | `T-006` | `must_be_last` | `required` | `EV-FK-AC-14, EV-CA-01` |

> **Task 说明（按 03-task-layer.md 权威定义）**：T-007=License 开启（URL 过滤 82200FCP，generic），T-AC-108=配置 URL 过滤（ICAP 互通层 VPNINST→LOGICINF→ICAPSERVER→ICAPLOCALINFO→ICAPSVRGRP→ICAPSVRBINDISG + CF 业务层 APN/CFPROFILE/CFTEMPLATE:ACTION=BLOCK/PERMIT/REDIRECT/CONTCATEGROUP/CONTCATEGBIND + cache/白名单 CFCACHEPARA/CFWHITEURLLST/CFIPWHITELIST，feature_specific；TR-AC-05 ICAP 互通前置，内部 16 条编排边见 03 §7.7），T-002=配置流过滤器与绑定（generic），T-AC-107=配置 PCC 动作组（URR/URRGROUP/PCCPOLICYGRP，feature_specific），T-003=配置 PCC 规则（ADD RULE:POLICYTYPE=PCC 仅触发匹配，动作实际走 CFTEMPLATE/CONTCATEGBIND，generic；TR-AC-03 双轨分离），T-004=配置用户模板与规则绑定（USERPROFILE + RULEBINDING，generic），T-006=SET REFRESHSRV:REFRESHTYPE=USERPROFILE（generic，must_be_last）

### 6.5 WSFD-211001 位置触发（UNC 侧配置链，4 条边）

> **Task 编号映射（U-H-01 修复）**：原 `T-AC-501~504` 在 03 中无定义，按动作语义重新映射：T-AC-501(USRLOCATION+USRLOCATIONGRP)→feature_specific `T-AC-109`（03 §4 权威定义）；T-AC-502(USRPROFGROUP/UPBINDUPG)→generic `T-005`（配置用户模板组与 APN 绑定，UNC 侧 UPBINDUPG 含 LOCGROUPNAME）；T-AC-503(APNUSRPROFG)→`T-005` 内部命令；T-AC-504(本地 PCC 场景的 RULE/USERPROFILE)→generic `T-003`+`T-004`（动态 PCC 场景由 PCRF/PCF 下发，optional）。

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `requiredness` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------|----------------------|
| `FTOE-AC-022` | `Feature` | `WSFD-211001` | `T-007` | `T-AC-109` | `precedes` | `required` | `EV-FK-AC-15, EV-CA-01` |
| `FTOE-AC-023` | `Feature` | `WSFD-211001` | `T-AC-109` | `T-005` | `precedes` | `required` | `EV-FK-AC-15, EV-CA-01` |
| `FTOE-AC-024` | `Feature` | `WSFD-211001` | `T-005` | `T-003` | `depends_on` | `optional` | `EV-FK-AC-15, EV-CA-01` |
| `FTOE-AC-025` | `Feature` | `WSFD-211001` | `T-003` | `T-004` | `depends_on` | `optional` | `EV-FK-AC-15, EV-CA-01` |

> **Task 说明（按 03-task-layer.md 权威定义）**：T-007=License 开启（位置触发 82200BNQ + PCC UNC 82207979 强依赖，generic），T-AC-109=配置位置条件策略（ADD USRLOCATION[CGI/ECGI/NCGI] + ADD USRLOCATIONGRP，feature_specific；TR-AC-08 动态 PCC 场景跳过此 Task），T-005=配置用户模板组与 APN 绑定（USRPROFGROUP + MOD UPBINDUPG[含 LOCGROUPNAME] + ADD APNUSRPROFG，generic），T-003=配置 PCC 规则（generic，仅本地 PCC 场景，optional），T-004=配置用户模板与规则绑定（generic，仅本地 PCC 场景，optional）。动态 PCC 场景（有 PCRF/PCF）规则由 N7/Gx 下发，T-003/T-004 跳过（FTOE-AC-024/025 = `optional`）

> **FTOE 统计**：5 个核心 Feature × 25 条编排边。License 开启（generic `T-007`）为所有链路起点，SET REFRESHSRV（generic `T-006`，must_be_last）为 UDG 侧链路终点；UNC 侧位置触发链终点为 APN 绑定（generic `T-005`），本地 PCC 场景额外接 generic `T-003`+`T-004`（optional）。所有 task_ref 均指向 03-task-layer.md 权威定义（generic `T-001~T-008` + 独有 `T-AC-101~T-AC-109`），无旧编号 `T-AC-201~504` 残留（U-H-01 已修复）。

---

## 7. 关系边汇总（Schema §9.8）

| 关系类型 | 数量 | 说明 |
|---------|------|------|
| `has_subfeature` | 0 | 访问限制场景无 SubFeature（产品定义上所有有正式特性编号的都是 Feature） |
| `depends_on` | 21 | UDG 侧 14 + UNC 侧 3 + UNC 接入控制辅助 4（U-H-02 补） |
| `requires_license` | 15 | UDG 12 + UNC 3（1:1 映射；4 个接入控制辅助特性无独立 License） |
| `constrained_by`（FeatureRule） | 8 | FR-AC-01 ~ FR-AC-08 |
| `orchestrates`（FeatureTaskOrderEdge） | 25 | FTOE-AC-001 ~ FTOE-AC-025（5 个核心 Feature，U-H-01 修复后 task_ref 全部指向 03 权威编号） |
| `decomposes_to`（Feature→ConfigTask） | 19 | 见 `05-cross-layer-mapping.md`（U-H-02 后需同步补 4 条 UNC 辅助特性的 Task 映射） |
| `uses_semantic_object` | — | 见 `05-cross-layer-mapping.md`（FILTER/FLOWFILTER/RULE/HEADEN/CFTEMPLATE 等） |
| `has_decision` | — | 见 `03-task-layer.md`（如轨道选择、PCC 模式选择） |
| `supported_by`（EvidenceSource） | 19 | EV-FK-AC-01 ~ EV-FK-AC-15（复用特性沿用跨场景编号）+ EV-FK-AC-16 ~ EV-FK-AC-19（4 个 UNC 接入控制辅助特性，★ P5 批次 3 独立分配，06 §2.8 注册，path 暂锚定 cross-topic-analysis.md §6.3） |
| **特性层对象总计** | **19 Feature + 15 License + 8 FeatureRule + 25 FTOE = 67 对象 + 69 关系边** | — |

---

## 8. 与计费 / 带宽控制场景特性图谱的对比

| 维度 | 计费场景 | 带宽控制场景 | 访问限制场景 |
|------|---------|------------|------------|
| Feature 数量 | 14（UDG 9 + UNC 5） | 24（UDG 16 + UNC 8） | 19（UDG 11 + UNC 8 = 位置触发 1 + 接入控制辅助 4 + 复用 PCC/ADC 2；11 UDG 独有 + 5 UNC 独有 + 4 复用，U-H-02 补实例化） |
| 独有特性数 | 11 | 21 | 15（UDG 11 + UNC 5，含 4 个接入控制辅助特性） |
| 核心特性族 | 计费三件套（URR/URRGROUP/PCCPOLICYGRP）+ 协议栈（Ga/Gy/N40） | BWM 三级控制体系（BWMSERVICE/BWMCONTROLLER/BWMUSERGROUP/BWMRULE） | **双轨动作机制**：轨道 A（POLICYTYPE 四值 ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY）+ 轨道 B（URL 过滤 CFTEMPLATE/CONTCATEGBIND） |
| 独有 Feature | GWFD-010171/010173/020300/020302/020303/020306, WSFD-011201/011202/011206/109002 | GWFD-110311/110312/110313/020354/020357/020358/020359/110301/110302/110331/110332/020305, WSFD-211005/109104/211009/109107/109102/109108/211101 | GWFD-020357(ADC)/110261/110262/110263(头增强族)/110401(防欺诈)/110281/110282/110283/110284(重定向族)/110471(URL过滤), WSFD-211001(位置触发)+WSFD-106003/105003/106005/105006(接入控制辅助 4，U-H-02 补) |
| 共享 Feature | GWFD-110101(SA-Basic), GWFD-020351/WSFD-109101(PCC) | 同左 | 同左 + WSFD-109102(ADC UNC) |
| License 数量 | 11（4 个无需 License） | 24（全部需 License） | 15（15 个独立特性需 License，UDG 12 + UNC 3；4 个接入控制辅助特性无独立 License） |
| 依赖链核心 | SA-Basic→PCC→内容计费→[在线/离线/融合/计量增强] | SA-Basic→PCC→BWM→[Shaping/FUP/QoS/ADC/无线优化] | **SA-Basic→PCC→[ADC/头增强族/重定向族/URL过滤/防欺诈]**（ADC 是 L7 横切前置） |
| 特性辐射中心 | SA-Basic（8 个依赖）+ PCC（全依赖） | SA-Basic（12 个依赖）+ PCC（22/24 依赖） | **SA-Basic（10 个独有依赖）+ PCC（5 个依赖，动作载体）+ ADC（L7 横切前置）** |
| 独有 FeatureRule | 9 条（计费三件套约束 + RGAPPLIED + QCT 优先级 + 事件计费点） | 5 条（BWM 层级 + 智能Shaping 依赖 + POLICYTYPE 侧别 + FUP SA 依赖 + URR 模式） | **8 条**（跨 NF 一致性 + POLICYTYPE 双轨+五子轨 + 头防欺诈强耦合 + ADC 横切 + HTTPS 限制 + SMARTREDIRECT 共用 + URL 过滤独立轨道 + IPFarm 全 DOWN） |
| UDG-UNC 配对 | 6 对 | 8 对 | **1 对**（ADC UDG↔UNC；位置触发为 UNC 独有；其余 10 独有特性全在 UDG） |
| Task 链复杂度 | 52 条 FTOE（5 个核心 Feature） | 25 条 FTOE（5 个核心 Feature） | **25 条 FTOE**（5 个核心 Feature：ADC/头增强+防欺诈/HTTP 重定向/URL 过滤/位置触发） |
| TaskCommandOrderEdge 数（03 内部） | 12 | 16 | **59**（§7 内部 50 + §8 跨 Task 9，U-H-07 修正，原误写 32） |
| 核心架构区别 | 计量方式 + 计费方式二维扩展 | 控制机制多维度扩展（限速/整形/GBR/FUP/DSCP/码率/位置） | **动作轨道双轨制**（PCC 隐式 vs URL 过滤显式 PERMIT）+ **协议层多轨重定向**（DNS/L3-IPNAT/L7-HTTP） |

> 三场景共享 SA-Basic 和 PCC 框架基础。计费场景在内容计费基础上向"计量方式 + 计费方式"扩展；带宽场景在 PCC 基础上向"控制机制"维度扩展；**访问限制场景在 PCC 基础上向"动作类型"维度扩展**，核心架构是**双轨动作机制**（轨道 A PCC 体系隐式动作 + 轨道 B URL 过滤显式 PERMIT），并涵盖阻塞/头增强/重定向三大动作语义。

---

## 9. 对象计数汇总

> **计数说明（U-H-02 修复后）**：Feature 总数从 15 修正为 **19**（补 4 个 UNC 接入控制辅助特性）；License 仍为 15（4 个接入控制辅助特性无独立 License）；requires_license 边仍为 15；depends_on 边从 17 增至 21（补 4 条 UNC 接入控制辅助特性的依赖边，详见 §2.3）。

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| Feature | 19 | UDG 11: GWFD-110101/020351/020357/110261/110262/110263/110401/110281/110282/110283/110284/110471 + UNC 8: WSFD-109101/109102/211001 + WSFD-106003/105003/106005/105006（4 个接入控制辅助，U-H-02 补） |
| License | 15 | UDG: LKV3G5*(12) ; UNC: LKV3W9*(1) + LKV2*(2) |
| FeatureRule | 8 | FR-AC-01 ~ FR-AC-08 |
| depends_on 边 | 21 | UDG 14 + UNC 7（3 原有 + 4 接入控制辅助） |
| requires_license 边 | 15 | UDG 12 + UNC 3 |
| FTOE 边 | 25 | FTOE-AC-001 ~ FTOE-AC-025 |
| **特性层对象总计** | **67 对象 + 69 关系边** | — |

### 9.1 复用共享特性标注情况

| 特性 | 复用场景 | License | 备注 |
|------|---------|---------|------|
| GWFD-110101 SA-Basic | 计费 + 带宽 + 访问限制（三场景） | LKV3G5SABS01 | 业务感知基础，访问限制 10 个独有特性直接依赖 |
| GWFD-020351 PCC基本功能（UDG） | 计费 + 带宽 + 访问限制（三场景） | LKV3G5PCCB01 | 动作载体，RULE.POLICYTYPE 差异化 |
| WSFD-109101 PCC基本功能（UNC） | 计费 + 带宽 + 访问限制（三场景） | LKV3W9SPCC11 | UNC 侧策略接收，位置触发强依赖 |
| WSFD-109102 ADC基本功能（UNC） | 计费 + 带宽 + 访问限制（三场景） | LKV2BADCF01 | ADC UNC 侧，三网元一致性 |

> 访问限制场景在 4 个三场景共享基础设施之上叠加 11 个独有特性（头增强族 3 + 重定向族 4 + 防欺诈 1 + ADC UDG 1 + URL 过滤 1 + 位置触发 1），形成"共享底座 + 独有动作层"的分层架构。

---

> 本文件为访问限制场景三层图谱第 2 层。第 1 层业务图谱见 `01-business-graph.md`，第 3 层任务原子层、第 4 层命令图谱、第 5 层跨层映射、第 6 层证据索引见同目录其他文件。
