# 计费场景三层图谱 · 第2层：特性图谱

> **文件定位**：`three-layer-graph/02-feature-graph.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §9 特性图谱
> **本体参考**：`三层图谱本体标准定义.md`
> **作用**：实例化计费场景14个Feature + depends_on边 + requires_license边 + FeatureRule + FeatureTaskOrderEdge
> **数据来源**：`feature-knowledge/cross-feature-analysis.md`（580行）、14个特性知识文件（8,311行）

---

## 0. 特性图谱总览

### 0.1 14 Feature 分组

| 分组 | UDG特性 | UNC特性 | 小计 |
|------|---------|---------|------|
| 基础感知 | GWFD-110101 SA-Basic | — | 1 |
| PCC框架 | GWFD-020351 PCC基本功能 | WSFD-109101 PCC基本功能 | 2 |
| 离线计费 | GWFD-010171 离线计费 | WSFD-011201 支持离线计费 | 2 |
| 在线计费 | GWFD-020300 在线计费 | — (通过Gy接口实现) | 1 |
| 融合计费 | GWFD-010173 融合计费 | WSFD-011206 支持融合计费 | 2 |
| 内容计费 | GWFD-020301 内容计费基本功能 | WSFD-109002 内容计费基本功能 | 2 |
| 计量方式增强 | GWFD-020302 时长计费 / GWFD-020303 流量计费 / GWFD-020306 事件计费 | — | 3 |
| 热计费 | — | WSFD-011202 支持热计费 | 1 |
| **合计** | **9** | **5** | **14** |

### 0.2 License 总览

| 产品 | License数 | 说明 |
|------|----------|------|
| UDG | 7 | SA-Basic / PCC / 内容计费 / 时长 / 流量 / 事件 / 在线计费 |
| UNC | 4 | PCC / 内容计费 / 热计费(SGSN) / 融合计费依赖内容计费License |
| 无需License | 4特性 | GWFD-010171, GWFD-010173, WSFD-011201, WSFD-011206 |

### 0.3 全局字段声明（status）

> **适用范围**：本文件 §1（14个Feature）和 §3（11个License + 4个无需License特性）所有对象。
> **声明**：除非特别标注，本文件所有 Feature（GWFD/WSFD-*）和 License（LKV*）的 `status` 字段值均为 `active`。
> **依据**：Schema §9.4（Feature.status 必备）和 §9.5（License.status 必备）。计费场景所有特性和 License 均处于正式启用状态。
> **修复来源**：U-M-15（Feature/License 缺 status 字段）。采用全局声明替代逐表格添加，避免14个Feature表格的冗余修改；License 表格在 §3 显式补 `status` 列。
> **例外**：无。所有对象当前均为 `active`，无 `deprecated` 或 `planned` 状态。

---

## 1. Feature 实例化（14个）

### 1.1 基础感知

#### GWFD-110101 SA-Basic（业务感知基本功能）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110101` |
| `feature_name` | `SA-Basic` |
| `feature_summary` | 提供3/4/7层报文解析、协议识别和七层URL解析能力，是所有内容计费特性的前置依赖 |
| `feature_group` | `基础感知` |
| `applicable_nf_map` | UPF/PGW-U/SGW-U（用户面执行）；SMF/PGW-C（下发动态规则） |
| `first_release` | `20.0.0` |
| `requires_license` | `LKV3G5SABS01` |
| `key_capabilities` | ① 3/4层五元组解析 ② 协议识别（知名端口+特征字）③ 7层URL/Method解析 ④ CP/UP配置一致性检查（ALM-81054，30分钟扫描）⑤ 前缀URL检测与剥离（100组×10=1000） |
| `source_evidence_ids` | `EV-FK-SA-Basic`, `EV-CFA` |

### 1.2 PCC框架

#### GWFD-020351 PCC基本功能（UDG）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020351` |
| `feature_name` | `PCC基本功能` |
| `feature_summary` | 策略和计费控制基本功能，UDG侧作为用户面策略执行实体，接收PCRF/PCF策略并执行检测/统计/QoS |
| `feature_group` | `PCC框架` |
| `applicable_nf_map` | PGW-U, UPF |
| `first_release` | `20.0.0` |
| `requires_license` | `LKV3G5PCCB01` |
| `key_capabilities` | ① 接收PCRF/PCF策略（经N4）② 用户面策略执行 ③ 13种Event Trigger ④ 动态/预定义/本地规则 ⑤ PDU会话全流程 ⑥ 2/3/4/5G PCC差异兼容 |
| `source_evidence_ids` | `EV-FK-PCC-UDG`, `EV-CFA` |

#### WSFD-109101 PCC基本功能（UNC）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-109101` |
| `feature_name` | `PCC基本功能` |
| `feature_summary` | UNC(SMF/PGW-C)侧策略和计费控制，作为PCEF-C通过Gx或N7/N15与PCRF/PCF交互 |
| `feature_group` | `PCC框架` |
| `applicable_nf_map` | SMF, PGW-C, GGSN-C, AMF |
| `first_release` | `20.0.0`（5G AMF+SMF）；`20.3.0`（2G/3G/4G Gx） |
| `requires_license` | `LKV3W9SPCC11` |
| `key_capabilities` | ① Gx接口Diameter信令（2/3/4G）② N7/N15服务化接口（5G）③ IP-CAN会话管理（CCR-I/U/T）④ PCRF冗余+Failover ⑤ PCF发现与选择 |
| `source_evidence_ids` | `EV-FK-PCC-UNC`, `EV-CFA` |

### 1.3 离线计费

#### GWFD-010171 离线计费（UDG）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-010171` |
| `feature_name` | `离线计费` |
| `feature_summary` | 非实时计费方式，UDG收集计费信息上报UNC，UNC格式化为话单通过Ga接口发送CG |
| `feature_group` | `离线计费` |
| `applicable_nf_map` | SGW-U, PGW-U |
| `first_release` | `20.0.0` |
| `requires_license` | 无需License |
| `key_capabilities` | ① Ga接口（GTP'协议）② URR核心配置（USAGERPTMODE=OFFLINE）③ 8种OFFMETERINGTYPE组合 ④ N4 PFCP使用量上报 ⑤ 内容计费三件套（URR→URRGROUP→PCCPOLICYGRP） |
| `source_evidence_ids` | `EV-FK-Offline-UDG`, `EV-CFA` |

#### WSFD-011201 支持离线计费（UNC）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-011201` |
| `feature_name` | `支持离线计费` |
| `feature_summary` | UNC侧离线计费，将用户面计费信息格式化为话单通过Ga接口发送CG |
| `feature_group` | `离线计费` |
| `applicable_nf_map` | SGSN, GGSN, SGW-C, PGW-C |
| `first_release` | `20.3.0` |
| `requires_license` | 无需License |
| `key_capabilities` | ① CC计费属性（16位，4级优先级：UserProfile>APN>CC>Global）② OFCTemplate离线计费模板 ③ CG组网可靠性（最多32个CG，负荷分担+WAL保护）④ 费率切换（节假日/工作日/时段）⑤ 话单可靠性（缓存/防重复/零流量抑制） |
| `source_evidence_ids` | `EV-FK-Offline-UNC`, `EV-CFA` |

### 1.4 在线计费

#### GWFD-020300 在线计费（UDG）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020300` |
| `feature_name` | `在线计费` |
| `feature_summary` | 实时计费功能，OCS将用户账户金额转换成配额下发给PGW-U，实时跟踪配额使用，耗尽终止业务 |
| `feature_group` | `在线计费` |
| `applicable_nf_map` | PGW-U（UDG）；PGW-C（UNC）；OCS |
| `first_release` | `20.0.0`（`20.15.2`增加Credit Pooling） |
| `requires_license` | `LKV3G5OLCH01` |
| `key_capabilities` | ① Gy接口（Diameter/DCC协议）② 配额管理（Volume/Time Quota）③ 超时阻塞（T3RESPONSE×N3REQUEST+4秒）④ Default Quota默认配额（SET UPDEFAULTQUOTA）⑤ Credit Pooling（20.15.2引入，仅Gy） |
| `source_evidence_ids` | `EV-FK-Online`, `EV-CFA` |

### 1.5 融合计费

#### GWFD-010173 融合计费（UDG）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-010173` |
| `feature_name` | `融合计费` |
| `feature_summary` | 5G统一计费架构，同一N40会话可同时支持在线RG和离线RG，带配额管理与不带配额管理在同一接口完成 |
| `feature_group` | `融合计费` |
| `applicable_nf_map` | UPF, PGW-U（UDG）；SMF, PGW-C（UNC）；CHF; PCF |
| `first_release` | `20.0.0` |
| `requires_license` | 无需License（依赖内容计费License LKV3G5BCBC01） |
| `key_capabilities` | ① Nchf/N40接口（HTTP/2）② RGAPPLIED三种模式（DEFAULT/ONLINERGONLY/OFFLINERGONLY）③ 每业务2个URR（离线+在线）④ 共享在线计费超时阻塞机制 ⑤ SET URRFAILACTION阻塞应急放通 |
| `source_evidence_ids` | `EV-FK-Converged-UDG`, `EV-CFA` |

#### WSFD-011206 支持融合计费（UNC）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-011206` |
| `feature_name` | `支持融合计费` |
| `feature_summary` | UNC侧融合计费，SMF与CHF间通过Nchf(N40)接口进行实时计费和后计费，统一了2/3/4G的Gy和Ga功能 |
| `feature_group` | `融合计费` |
| `applicable_nf_map` | SMF, PGW-C; CHF; PCF |
| `first_release` | `20.0.0` |
| `requires_license` | 依赖内容计费License（LKV3W9BCC12） |
| `key_capabilities` | ① CCT融合计费模板（QHT/VQT/TQT/VT等触发器）② 7级CHF选择优先级 ③ 计费消息缓存与回放 ④ 主备CHF Failover ⑤ PDU/RG级Trigger ⑥ N40 API版本控制 ⑦ MEC计费（多UPF独立配额）⑧ 互操作计费（5GS↔EPS） |
| `source_evidence_ids` | `EV-FK-Converged-UNC`, `EV-CFA` |

### 1.6 内容计费

#### GWFD-020301 内容计费基本功能（UDG）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020301` |
| `feature_name` | `内容计费基本功能` |
| `feature_summary` | 基于业务的计费，通过包过滤和分析识别业务类型，针对不同业务实施不同费率。定义计费三件套URR→URRGROUP→PCCPOLICYGRP |
| `feature_group` | `内容计费` |
| `applicable_nf_map` | SGW-U, PGW-U, UPF |
| `first_release` | `20.0.0` |
| `requires_license` | `LKV3G5BCBC01` |
| `key_capabilities` | ① 计费三件套（URR→URRGROUP→PCCPOLICYGRP）② FILTER/L7FILTER/FLOWFILTER匹配规则 ③ 11+参数SMF/UPF一致性 ④ SET REFRESHSRV硬约束 ⑤ 重定向计费 ⑥ 关联URL计费 ⑦ 防欺诈SPECURRGRPLIST |
| `source_evidence_ids` | `EV-FK-Content-UDG`, `EV-CFA` |

#### WSFD-109002 内容计费基本功能（UNC）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-109002` |
| `feature_name` | `内容计费基本功能` |
| `feature_summary` | UNC侧基于业务粒度的计费控制，从PCRF/PCF获取计费规则下发给UPF |
| `feature_group` | `内容计费` |
| `applicable_nf_map` | GGSN-C, SGW-C, PGW-C, SMF |
| `first_release` | `20.0.0`（SMF）；`20.3.0`（GGSN/PGW-C） |
| `requires_license` | `LKV3W9BCC12` |
| `key_capabilities` | ① 费率标识RG/(RG,SID) ② USRPROFGROUP/UPBINDUPG/APNUSRPROFG绑定 ③ UNC侧不配FILTER（仅UDG配）④ QUOTAEXHAUSTACT配额耗尽动作（BLOCK/REDIRECT/FORWARD）⑤ 5000个规则规格 ⑥ RGSID复合标识 |
| `source_evidence_ids` | `EV-FK-Content-UNC`, `EV-CFA` |

### 1.7 计量方式增强

#### GWFD-020302 基于业务时长的计费

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020302` |
| `feature_name` | `基于业务时长的计费` |
| `feature_summary` | 内容计费增强形式，URR中METERINGTYPE=DURATION，按业务持续时间统计。支持QCT和CTP两种模式 |
| `feature_group` | `计量方式增强` |
| `applicable_nf_map` | SGW-U, PGW-U, UPF; SGW-C, PGW-C, SMF |
| `first_release` | `20.0.0` |
| `requires_license` | `LKV3G5TBCS01` |
| `key_capabilities` | ① OFFMETERINGTYPE/ONLMETERINGTYPE=DURATION ② QCT（配额消耗时间）vs CTP（连续时长）③ QCT优先级（TQM>OCS QCT>本地配置）④ 不支持CTP↔QCT会话中切换 |
| `source_evidence_ids` | `EV-FK-Duration`, `EV-CFA` |

#### GWFD-020303 基于业务流量的计费

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020303` |
| `feature_name` | `基于业务流量的计费` |
| `feature_summary` | 内容计费增强形式，URR中METERINGTYPE=VOLUME，按业务上下行字节数统计 |
| `feature_group` | `计量方式增强` |
| `applicable_nf_map` | SGW-U, PGW-U, UPF; SGW-C, PGW-C, SMF; CG, OCS, CHF |
| `first_release` | `20.0.0` |
| `requires_license` | `LKV3G5VBCS01` |
| `key_capabilities` | ① OFFMETERINGTYPE/ONLMETERINGTYPE=VOLUME ② 上行/下行/总流量独立统计 ③ CC-Total-Octets/CC-Input-Octets/CC-Output-Octets（在线）④ SET SPECTRAFURRGRP全局缺省URR组处理特殊流量 |
| `source_evidence_ids` | `EV-FK-Volume`, `EV-CFA` |

#### GWFD-020306 支持事件计费

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020306` |
| `feature_name` | `支持事件计费` |
| `feature_summary` | 按业务使用次数计费，三个独立计费点（REQUEST/RESPONSE/FINISH），在线模式仅支持SCUR |
| `feature_group` | `计量方式增强` |
| `applicable_nf_map` | PGW-U, UPF |
| `first_release` | `20.5.0`（`20.9.0`增加ECUR，`20.10.0`增加BIT419） |
| `requires_license` | `LKV3G5EBCS01` |
| `key_capabilities` | ① OFFMETERINGTYPE/ONLMETERINGTYPE=EVENT ② 三个计费点（REQUEST直接占用/RESPONSE预占→正式/返还/FINISH）③ serviceSpecificUnits配额单位 ④ 仅SCUR（在线）⑤ 群发彩信ECUR（每被叫一个MSCC，最大75个） |
| `source_evidence_ids` | `EV-FK-Event`, `EV-CFA` |

### 1.8 热计费

#### WSFD-011202 支持热计费（UNC）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-011202` |
| `feature_name` | `支持热计费` |
| `feature_summary` | 特殊的离线计费方式，CG优先处理带热计费标志（CC=0x0100）的话单，产生速度更快 |
| `feature_group` | `离线计费增强` |
| `applicable_nf_map` | GGSN-C, SGW-C, PGW-C; SGSN |
| `first_release` | `20.3.0` |
| `requires_license` | `LKV2HBILL02`（仅SGSN） |
| `key_capabilities` | ① CC=0x0100（hotbilling标志）② GGSN/PGW-C无需License ③ SGSN 30秒内产生话单 ④ GGSN/PGW-C通过更小阈值加快话单产生 ⑤ SGSN支持断链缓存+BS主动欠费停机 |
| `source_evidence_ids` | `EV-FK-HotBilling`, `EV-CFA` |

---

## 2. Feature depends_on 关系边（16条）

### 2.1 UDG侧依赖（10条）

| 源Feature | 关系 | 目标Feature | 依赖类型 | 依赖理由 |
|-----------|------|-------------|----------|----------|
| GWFD-020351 (PCC) | `depends_on` | GWFD-110101 (SA-Basic) | mandatory | PCC前置条件：完成业务感知配置 |
| GWFD-020301 (内容计费) | `depends_on` | GWFD-110101 (SA-Basic) | mandatory | 必须先开启SA特性才能识别业务类型 |
| GWFD-020300 (在线计费) | `depends_on` | GWFD-020301 (内容计费) | optional | 基于业务粒度在线计费时需要内容计费 |
| GWFD-020302 (时长计费) | `depends_on` | GWFD-020301 (内容计费) | mandatory | 时长计费是内容计费增强形式 |
| GWFD-020302 (时长计费) | `depends_on` | GWFD-110101 (SA-Basic) | mandatory | 依赖链：SA-Basic→内容计费→时长计费 |
| GWFD-020303 (流量计费) | `depends_on` | GWFD-020301 (内容计费) | mandatory | 依赖链：SA-Basic→内容计费→流量计费 |
| GWFD-020303 (流量计费) | `depends_on` | GWFD-110101 (SA-Basic) | mandatory | 内容计费前置依赖SA-Basic |
| GWFD-020306 (事件计费) | `depends_on` | GWFD-020301 (内容计费) | mandatory | 事件计费是内容计费增强特性 |
| GWFD-020306 (事件计费) | `depends_on` | GWFD-110101 (SA-Basic) | mandatory | 事件计费依赖SA-Basic识别业务 |
| GWFD-010173 (融合计费) | `depends_on` | GWFD-020301 (内容计费) | mandatory | 需内容计费License（LKV3G5BCBC01）打开 |

### 2.2 UNC侧依赖（6条）

| 源Feature | 关系 | 目标Feature | 依赖类型 | 依赖理由 |
|-----------|------|-------------|----------|----------|
| WSFD-109002 (UNC内容计费) | `depends_on` | WSFD-109101 (UNC PCC) | mandatory | 内容计费需PCC支撑规则下发 |
| WSFD-011202 (热计费) | `depends_on` | WSFD-011201 (UNC离线计费) | mandatory | 热计费是离线计费的增强特性 |
| WSFD-011206 (UNC融合计费) | `depends_on` | WSFD-109002 (UNC内容计费) | optional | 基于业务粒度融合计费时需开启 |
| WSFD-011206 (UNC融合计费) | `depends_on` | WSFD-011201 (UNC离线计费) | optional | 融合计费基础依赖 |
| WSFD-011201 (UNC离线计费) | `depends_on` | WSFD-109002 (UNC内容计费) | optional | 基于业务粒度离线计费时需开启 |
| WSFD-109101 (UNC PCC) | `depends_on` | GWFD-020351 (UDG PCC) | deployment_prerequisite（跨产品） | 前置条件：部署时需UDG侧先完成GWFD-020351配置，非运行时强依赖 |

---

## 3. License 实例化（License实例11条 + 无需License特性4条 = 15行）

| `license_id` | `license_name` | 对应Feature | 产品 | `status` | 说明 |
|---------------|----------------|-------------|------|----------|------|
| `LKV3G5SABS01` | SA-Basic (82209749) | GWFD-110101 | UDG | `active` | 业务感知基础 |
| `LKV3G5PCCB01` | PCC基本功能 (82209825) | GWFD-020351 | UDG | `active` | PCC框架 |
| `LKV3G5BCBC01` | 内容计费基本功能 (82209822) | GWFD-020301 | UDG | `active` | 内容计费核心 |
| `LKV3G5TBCS01` | 基于业务时长的计费 (82209823) | GWFD-020302 | UDG | `active` | 时长计量 |
| `LKV3G5VBCS01` | 基于业务流量的计费 (82209824) | GWFD-020303 | UDG | `active` | 流量计量 |
| `LKV3G5EBCS01` | 支持事件计费 (82200CKE) | GWFD-020306 | UDG | `active` | 事件计量 |
| `LKV3G5OLCH01` | 在线计费 (82209821) | GWFD-020300 | UDG | `active` | 在线计费 |
| `LKV3W9SPCC11` | PCC基本功能 (82207979) | WSFD-109101 | UNC | `active` | UNC PCC框架 |
| `LKV3W9BCC12` | 内容计费基本功能 (82207988) | WSFD-109002 | UNC | `active` | UNC内容计费 |
| `LKV2HBILL02` | 支持热计费功能 (82206574) | WSFD-011202 | UNC（仅SGSN） | `active` | 热计费 |
| 无需License | — | WSFD-011206 | UNC | `active` | 融合计费依赖内容计费License |
| 无需License | — | GWFD-010171 | UDG | `active` | 离线计费 |
| 无需License | — | GWFD-010173 | UDG | `active` | 融合计费依赖内容计费License |
| 无需License | — | WSFD-011201 | UNC | `active` | 离线计费 |

---

## 4. UDG-UNC 特性对应关系（6对）

| UDG特性 | ↔ | UNC特性 | 配对说明 | 共享对象 |
|---------|---|---------|----------|----------|
| GWFD-020351 PCC基本功能 | ↔ | WSFD-109101 PCC基本功能 | **配对使用**：UNC接收PCF/PCRF策略→N4下发→UDG执行 | RULE, PCCPOLICYGRP |
| GWFD-020301 内容计费基本功能 | ↔ | WSFD-109002 内容计费基本功能 | **配对使用**：UDG配置FILTER/三件套；UNC配置USAGERPTMODE/USRPROFGROUP | URR, URRGROUP, PCCPOLICYGRP, USERPROFILE |
| GWFD-010171 离线计费 | ↔ | WSFD-011201 支持离线计费 | **配对使用**：UDG收集→UNC生成话单→Ga→CG | URR, CG配置对象 |
| GWFD-020300 在线计费 | ↔ | （通过Gy接口由UNC实现） | UDG上报使用量→UNC与OCS交互配额 | URR(USAGERPTMODE=ONLINE), DCC/Diameter |
| GWFD-010173 融合计费 | ↔ | WSFD-011206 支持融合计费 | **配对使用**：UNC与CHF交互Nchf/N40→N4下发→UDG执行 | URR(在线+离线), CCT, CHF选择对象 |
| （无独立特性） | ↔ | WSFD-011202 支持热计费 | 仅UNC侧定义，CC=0x0100控制话单优先级 | UNC CC配置对象 |

> **跨产品协同关键**：CS-CH-01~07方案闭包均需UDG+UNC双侧配置，`BR-CH-07`（RG值跨侧一致性）和`BR-CH-04`（CP/UP URR一致性）是双产品部署的硬约束。

---

## 5. FeatureRule（8条）

| `rule_id` | 所属Feature | `rule_name` | `rule_type` | `rule_logic` | `severity` |
|-----------|------------|-------------|-------------|--------------|------------|
| `FR-CH-01` | GWFD-020301（内容计费） | REFRESHSRV必须最后执行 | `restriction_rule` | 不执行SET REFRESHSRV，FILTER的配置变更不会生效。必须在所有Filter配置完成后执行。PROTBINDFLOWF要求修改后等待60秒再执行 | critical |
| `FR-CH-02` | GWFD-010173（融合计费） | RGAPPLIED与URRGROUP冲突约束 | `restriction_rule` | RGAPPLIED=DEFAULT时，URRGROUP下**不能**同时配置离线和在线URR，否则计费冲突；RGAPPLIED=ONLINERGONLY时URRGROUP**只配在线URR**（UPURRNAME2/DOWNURRNAME2）；RGAPPLIED=OFFLINERGONLY时**只配离线URR**（UPURRNAME1/DOWNURRNAME1）。（命令级细化见CR-CH-07） | critical |
| `FR-CH-03` | GWFD-020300（在线计费） | 超时阻塞公式 | `validation_rule` | 超时时间 = T3RESPONSE × N3REQUEST + 4（秒）。超时未收到配额更新，UPF阻塞业务。SET URRFAILACTION:RETRYFAILACT=CONTINUE可应急放通 | warning |
| `FR-CH-04` | GWFD-020301（内容计费） | SMF/UPF配置一致性（11+参数） | `consistency_rule` | URRID/USAGERPTMODE/OFFMETERINGTYPE/ONLMETERINGTYPE/RULENAME/POLICYTYPE/POLICYNAME/USERPROFILENAME/RULEBINDING RULENAME+POLICYTYPE在SMF和UPF必须一致。30分钟扫描，不一致触发ALM-81054 | critical |
| `FR-CH-05` | GWFD-020301（内容计费） | RULE优先级排序规则 | `naming_rule` | 数字越小优先级越高。只绑定三四层filter的RULE优先级应低于绑定七层filter的RULE。any过滤条件的RULE优先级设为最低（如65000） | info |
| `FR-CH-06` | GWFD-020301（内容计费） | URRGROUP必须同时配置在线+离线URR | `restriction_rule` | URRGROUP下必须同时配置在线URR和离线URR。只配置一种计费模式且和用户计费模式不匹配时无法计费。UPURRNAME1/2和DOWNURRNAME1/2只是编号，无优先级语义。[scope: 融合计费场景CS-CH-03/CS-CH-06] | warning |
| `FR-CH-07` | GWFD-020302（时长计费） | QCT优先级规则 | `dependency_rule` | 在线计费QCT确定优先级：TQM优先 > OCS下发的QCT > PGW-C/SMF本地配置的QCT。OCS下发的计费方式优先级高于本地配置。不支持CTP↔QCT会话中切换 | warning |
| `FR-CH-08` | GWFD-020306（事件计费） | 事件计费点配额管理差异 | `validation_rule` | REQUEST：直接占用配额，无需预占用/返还。RESPONSE/FINISH：收到请求时预占用配额；识别到成功响应后正式占用；未识别到响应则返还预占配额。RG使能状态整个PDU会话不可变 | warning |
| `FR-CH-09` | GWFD-020301（内容计费） | 关联URL计费配置约束 | `restriction_rule` | 关联URL计费要求主URL和关联URL的FILTER必须配置在同一RULE内，共享同一RG；关联URL的MATCHMODE必须为PREFIX | warning |

---

## 6. FeatureTaskOrderEdge（核心Feature的Task展开顺序）

> **Schema参考**：Schema §11.4 FeatureTaskOrderEdge。详细Task定义见 `03-task-layer.md`。
> **关系类型**：本场景所有FTOE均为 `sequential`（顺序执行），因计费配置链存在严格前后依赖。
> **说明**：SET URRFAILACTION 等内联命令步骤归入其所属Task（如T-006），不单独建边。

### 6.1 GWFD-010171 离线计费（UDG侧配置链，8条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-CH-001` | `Feature` | `GWFD-010171` | `T-101` | `T-006` | `sequential` | `EV-FK-Offline-UDG, EV-CFA` |
| `FTOE-CH-002` | `Feature` | `GWFD-010171` | `T-006` | `T-007` | `sequential` | `EV-FK-Offline-UDG, EV-CFA` |
| `FTOE-CH-003` | `Feature` | `GWFD-010171` | `T-007` | `T-001` | `sequential` | `EV-FK-Offline-UDG, EV-CFA` |
| `FTOE-CH-004` | `Feature` | `GWFD-010171` | `T-001` | `T-002` | `sequential` | `EV-FK-Offline-UDG, EV-CFA` |
| `FTOE-CH-005` | `Feature` | `GWFD-010171` | `T-002` | `T-003` | `sequential` | `EV-FK-Offline-UDG, EV-CFA` |
| `FTOE-CH-006` | `Feature` | `GWFD-010171` | `T-003` | `T-004` | `sequential` | `EV-FK-Offline-UDG, EV-CFA` |
| `FTOE-CH-007` | `Feature` | `GWFD-010171` | `T-004` | `T-104` | `sequential` | `EV-FK-Offline-UDG, EV-CFA` |
| `FTOE-CH-008` | `Feature` | `GWFD-010171` | `T-104` | `T-008` | `sequential` | `EV-FK-Offline-UDG, EV-CFA` |

### 6.2 GWFD-020300 在线计费（UDG侧配置链，10条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-CH-009` | `Feature` | `GWFD-020300` | `T-101` | `T-006` | `sequential` | `EV-FK-Online, EV-CFA` |
| `FTOE-CH-010` | `Feature` | `GWFD-020300` | `T-006` | `T-007` | `sequential` | `EV-FK-Online, EV-CFA` |
| `FTOE-CH-011` | `Feature` | `GWFD-020300` | `T-007` | `T-001` | `sequential` | `EV-FK-Online, EV-CFA` |
| `FTOE-CH-012` | `Feature` | `GWFD-020300` | `T-001` | `T-002` | `sequential` | `EV-FK-Online, EV-CFA` |
| `FTOE-CH-013` | `Feature` | `GWFD-020300` | `T-002` | `T-003` | `sequential` | `EV-FK-Online, EV-CFA` |
| `FTOE-CH-014` | `Feature` | `GWFD-020300` | `T-003` | `T-004` | `sequential` | `EV-FK-Online, EV-CFA` |
| `FTOE-CH-015` | `Feature` | `GWFD-020300` | `T-004` | `T-203` | `sequential` | `EV-FK-Online, EV-CFA` |
| `FTOE-CH-016` | `Feature` | `GWFD-020300` | `T-203` | `T-202` | `sequential` | `EV-FK-Online, EV-CFA` |
| `FTOE-CH-017` | `Feature` | `GWFD-020300` | `T-202` | `T-204` | `sequential` | `EV-FK-Online, EV-CFA` |
| `FTOE-CH-018` | `Feature` | `GWFD-020300` | `T-204` | `T-008` | `sequential` | `EV-FK-Online, EV-CFA` |

### 6.3 GWFD-010173 融合计费（UDG侧配置链，8条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-CH-019` | `Feature` | `GWFD-010173` | `T-101` | `T-006` | `sequential` | `EV-FK-Converged-UDG, EV-CFA` |
| `FTOE-CH-020` | `Feature` | `GWFD-010173` | `T-006` | `T-007` | `sequential` | `EV-FK-Converged-UDG, EV-CFA` |
| `FTOE-CH-021` | `Feature` | `GWFD-010173` | `T-007` | `T-001` | `sequential` | `EV-FK-Converged-UDG, EV-CFA` |
| `FTOE-CH-022` | `Feature` | `GWFD-010173` | `T-001` | `T-002` | `sequential` | `EV-FK-Converged-UDG, EV-CFA` |
| `FTOE-CH-023` | `Feature` | `GWFD-010173` | `T-002` | `T-003` | `sequential` | `EV-FK-Converged-UDG, EV-CFA` |
| `FTOE-CH-024` | `Feature` | `GWFD-010173` | `T-003` | `T-004` | `sequential` | `EV-FK-Converged-UDG, EV-CFA` |
| `FTOE-CH-025` | `Feature` | `GWFD-010173` | `T-004` | `T-104` | `sequential` | `EV-FK-Converged-UDG, EV-CFA` |
| `FTOE-CH-026` | `Feature` | `GWFD-010173` | `T-104` | `T-008` | `sequential` | `EV-FK-Converged-UDG, EV-CFA` |

### 6.4 GWFD-020301 内容计费（UDG侧配置链，10条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-CH-027` | `Feature` | `GWFD-020301` | `T-101` | `T-102` | `sequential` | `EV-FK-Content-UDG, EV-CFA` |
| `FTOE-CH-028` | `Feature` | `GWFD-020301` | `T-102` | `T-001` | `sequential` | `EV-FK-Content-UDG, EV-CFA` |
| `FTOE-CH-029` | `Feature` | `GWFD-020301` | `T-001` | `T-002` | `sequential` | `EV-FK-Content-UDG, EV-CFA` |
| `FTOE-CH-030` | `Feature` | `GWFD-020301` | `T-002` | `T-103` | `sequential` | `EV-FK-Content-UDG, EV-CFA` |
| `FTOE-CH-031` | `Feature` | `GWFD-020301` | `T-103` | `T-006` | `sequential` | `EV-FK-Content-UDG, EV-CFA` |
| `FTOE-CH-032` | `Feature` | `GWFD-020301` | `T-006` | `T-007` | `sequential` | `EV-FK-Content-UDG, EV-CFA` |
| `FTOE-CH-033` | `Feature` | `GWFD-020301` | `T-007` | `T-003` | `sequential` | `EV-FK-Content-UDG, EV-CFA` |
| `FTOE-CH-034` | `Feature` | `GWFD-020301` | `T-003` | `T-004` | `sequential` | `EV-FK-Content-UDG, EV-CFA` |
| `FTOE-CH-035` | `Feature` | `GWFD-020301` | `T-004` | `T-104` | `sequential` | `EV-FK-Content-UDG, EV-CFA` |
| `FTOE-CH-036` | `Feature` | `GWFD-020301` | `T-104` | `T-008` | `sequential` | `EV-FK-Content-UDG, EV-CFA` |

### 6.5 WSFD-011206 融合计费（UNC侧配置链，16条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-CH-037` | `Feature` | `WSFD-011206` | `T-101` | `T-301` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |
| `FTOE-CH-038` | `Feature` | `WSFD-011206` | `T-301` | `T-302` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |
| `FTOE-CH-039` | `Feature` | `WSFD-011206` | `T-302` | `T-303` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |
| `FTOE-CH-040` | `Feature` | `WSFD-011206` | `T-303` | `T-309` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |
| `FTOE-CH-041` | `Feature` | `WSFD-011206` | `T-309` | `T-304` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |
| `FTOE-CH-042` | `Feature` | `WSFD-011206` | `T-304` | `T-305` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |
| `FTOE-CH-043` | `Feature` | `WSFD-011206` | `T-305` | `T-306` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |
| `FTOE-CH-044` | `Feature` | `WSFD-011206` | `T-306` | `T-307` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |
| `FTOE-CH-045` | `Feature` | `WSFD-011206` | `T-307` | `T-308` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |
| `FTOE-CH-046` | `Feature` | `WSFD-011206` | `T-308` | `T-006` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |
| `FTOE-CH-047` | `Feature` | `WSFD-011206` | `T-006` | `T-007` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |
| `FTOE-CH-048` | `Feature` | `WSFD-011206` | `T-007` | `T-003` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |
| `FTOE-CH-049` | `Feature` | `WSFD-011206` | `T-003` | `T-004` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |
| `FTOE-CH-050` | `Feature` | `WSFD-011206` | `T-004` | `T-005` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |
| `FTOE-CH-051` | `Feature` | `WSFD-011206` | `T-005` | `T-310` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |
| `FTOE-CH-052` | `Feature` | `WSFD-011206` | `T-310` | `T-204` | `sequential` | `EV-FK-Converged-UNC, EV-CFA` |

> **FTOE统计**：5个核心Feature × 52条顺序边。License开启(T-101)为所有链路起点，REFRESHSRV(T-008)或QUOTAEXHAUSTACT(T-204)为终点。

---

## 7. 特性图谱关系边汇总

| 关系类型 | 数量 | 说明 |
|---------|------|------|
| `depends_on` | 16 | UDG侧10 + UNC侧6（含1跨产品） |
| `requires_license` | 11 | UDG 7 + UNC 4 |
| `constrained_by`（FeatureRule） | 9 | FR-CH-01~FR-CH-09 |
| `task_order`（FeatureTaskOrderEdge） | 52 | FTOE-CH-001~052（5个核心Feature） |
| `decomposes_to`（Feature→ConfigTask） | 14 | 见`05-cross-layer-mapping.md` |
| **特性层对象总计** | **14 Feature + 11 License + 9 FeatureRule + 52 FTOE** | — |

---

## 8. 与带宽场景特性图谱的差异

| 维度 | 计费场景 | 带宽控制场景 |
|------|---------|------------|
| Feature数量 | 14（UDG 9 + UNC 5） | 24（UDG 16 + UNC 8） |
| 核心特性族 | 计费三件套（URR/URRGROUP/PCCPOLICYGRP）+ 协议栈（Ga/Gy/N40） | BWM三级控制体系 |
| 独有Feature | GWFD-010171/010173/020300/020302/020303/020306, WSFD-011201/011202/011206/109002 | GWFD-110311/110312/110313/020354/020357/020358等 |
| 共享Feature | GWFD-110101(SA-Basic), GWFD-020351/WSFD-109101(PCC) | 同左 |
| 独有License族 | 在线/离线/融合/事件/时长/流量/热计费License | BWM/Shaping/ADC/QoS License |
| 依赖链核心 | SA-Basic→PCC→内容计费→[在线/离线/融合/计量增强] | SA-Basic→PCC→BWM→[Shaping/FUP/QoS] |

> 两场景共享SA-Basic和PCC框架基础。计费场景在内容计费基础上向"计量方式+计费方式"两个维度扩展；带宽场景在PCC基础上向"控制机制"维度扩展。

---

## 9. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| Feature | 14 | GWFD-110101/020300/020301/020302/020303/020306/020351/010171/010173 + WSFD-011201/011202/011206/109002/109101 |
| License | 11 | LKV3G5*（7）+ LKV3W9*（2）+ LKV2HBILL02 + 无需(4特性) |
| FeatureRule | 9 | FR-CH-01~FR-CH-09 |
| depends_on边 | 16 | UDG 10 + UNC 6 |
| **特性层对象总计** | **49** | — |

---

> 本文件为计费场景三层图谱第2层。第3层任务原子层、第4层命令图谱、第5层跨层映射、第6层证据索引见同目录其他文件。
