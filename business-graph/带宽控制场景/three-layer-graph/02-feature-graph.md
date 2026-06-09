# 带宽控制场景特性图谱（新 Schema，v0.1）

> 范围：仅描述带宽控制场景（业务感知套餐2）在新三层图谱 schema 下的特性图谱部分。
> 约束：对象、关系、属性命名严格服从 `三层图谱Schema-最终版-v0.1.md` §9 特性图谱 Schema。
> 来源：基于 `cross-feature-analysis.md`（24特性横向分析，§1分类/§4依赖/§2.3 License/附录B命令/附录C对象）。
> 说明：24个特性全部为 `Feature`（无 SubFeature），差异通过 `variant_dimensions` 属性和 FeatureRule 表达。

---

## 0. 适用定义与来源

### 0.1 根定义

- `三层图谱本体标准定义.md`
- `三层图谱Schema-最终版-v0.1.md`

### 0.2 直接来源

- `cross-feature-analysis.md`（§1.1功能层次分类、§4.1-4.2依赖图、§2.3 License依赖链、附录A 24特性索引）
- `feature-knowledge/GWFD-*.md`（16个UDG特性详情）
- `feature-knowledge/WSFD-*.md`（8个UNC特性详情）

### 0.3 本文件保留对象

| 对象 | 中文名 | 实例数 |
| --- | --- | --- |
| `Feature` | 特性 | 24 |
| `License` | License | 24 |
| `FeatureRule` | 特性规则 | 5 |
| `FeatureTaskOrderEdge` | 特性到任务编排边 | 见 §6 |
| `DecisionPoint` | 决策点（特性层） | 见 `01-business-graph.md`（跨层共享） |
| `SemanticObject` | 语义对象（跨层共享） | 见 `01-business-graph.md` |

---

## 1. Feature 分组总览

按 `cross-feature-analysis.md` §1.1 功能层次分类，24 个特性分为 10 个 `feature_group`：

| feature_group | 特性ID | 数量 |
| --- | --- | --- |
| `基础感知` | GWFD-110101, GWFD-111600 | 2 |
| `PCC框架` | GWFD-020351, WSFD-109101 | 2 |
| `核心带宽控制` | GWFD-110311, WSFD-211005 | 2 |
| `Shaping整形` | GWFD-020354, GWFD-110313 | 2 |
| `FUP累计流量` | GWFD-020353, WSFD-109104, GWFD-110312, WSFD-211009 | 4 |
| `QoS保证` | GWFD-020358, WSFD-109107, GWFD-110302 | 3 |
| `ADC检测` | GWFD-020357, WSFD-109102 | 2 |
| `无线优化` | GWFD-020359, GWFD-110301, GWFD-110331, GWFD-110332, WSFD-211101 | 5 |
| `位置感知` | WSFD-109108 | 1 |
| `异常检测` | GWFD-020305 | 1 |

---

## 2. Feature 实例

### 2.1 基础感知层

#### GWFD-110101 SA-Basic

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-110101` |
| `feature_name` | `SA-Basic` |
| `feature_summary` | L3/L4/L7 业务识别基础引擎，提供 SVC/APP 识别能力，是整个带宽控制场景的数据基础 |
| `feature_group` | `基础感知` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["识别层级(L3/L4/L7)", "特征库版本"]` |
| `first_release` | `UDG 20.0.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-110101`, `EV-CFA-§2.2`, `EV-TK-17` |

#### GWFD-111600 SA特征库更新管控

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-111600` |
| `feature_name` | `SA特征库更新管控` |
| `feature_summary` | SA 特征库版本 License 管理，维护 SA-Basic 使用的特征库数据 |
| `feature_group` | `基础感知` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["特征库版本"]` |
| `first_release` | `UDG 20.12.2` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-111600`, `EV-CFA-§2.2` |

### 2.2 PCC 框架层

#### GWFD-020351 PCC基本功能（UDG）

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-020351` |
| `feature_name` | `PCC基本功能` |
| `feature_summary` | UDG 侧 PCC 基础，接收 N4 规则（PDR/FAR/QER/URR/BAR），执行 MBR限速/GBR保障/Gate门控 |
| `feature_group` | `PCC框架` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["规则来源(动态/预定义/本地)", "有无PCRF"]` |
| `first_release` | `UDG 20.0.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-020351`, `EV-CFA-§2.1` |

#### WSFD-109101 PCC基本功能（UNC）

| 字段 | 值 |
| --- | --- |
| `feature_id` | `WSFD-109101` |
| `feature_name` | `PCC基本功能` |
| `feature_summary` | UNC 侧 PCC 基础，接收 PCRF/PCF 的 QCI/5QI/MBR/GBR/ARP 策略，管理 PCC 规则生命周期，通过 N4 下发 |
| `feature_group` | `PCC框架` |
| `applicable_nf_map` | `{"UNC": ["SMF", "PGW-C", "AMF", "GGSN"]}` |
| `variant_dimensions` | `["接口(Gx/N7)", "PCRF冗余模式"]` |
| `first_release` | `UNC 20.0.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-109101`, `EV-CFA-§2.1` |

### 2.3 核心带宽控制层

#### GWFD-110311 基于业务感知的带宽控制（UDG）

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-110311` |
| `feature_name` | `基于业务感知的带宽控制` |
| `feature_summary` | UDG 侧核心带宽控制，定义独有的三级 BWM 控制体系（用户级/组级/全局级），通过 SA 识别执行 CAR/Shaping |
| `feature_group` | `核心带宽控制` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["控制层级(用户/组/全局)", "CTRLTYPE(CAR/SHAPING)", "BWMRULETYPE"]` |
| `first_release` | `UDG 20.9.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-110311`, `EV-CFA-§3.2`, `EV-TK-19` |

#### WSFD-211005 基于业务感知的带宽控制（UNC）

| 字段 | 值 |
| --- | --- |
| `feature_id` | `WSFD-211005` |
| `feature_name` | `基于业务感知的带宽控制` |
| `feature_summary` | UNC 侧 BWM 规则管理，通过 `ADD RULE(POLICYTYPE=BWM)` 定义策略，N4 下发至 UDG 执行 |
| `feature_group` | `核心带宽控制` |
| `applicable_nf_map` | `{"UNC": ["GGSN", "PGW-C", "SMF"]}` |
| `variant_dimensions` | `["接口(Gx/N7)"]` |
| `first_release` | `UNC 20.5.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-211005`, `EV-CFA-§5.6` |

### 2.4 Shaping 整形层

#### GWFD-020354 基于业务的Shaping

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-020354` |
| `feature_name` | `基于业务的Shaping` |
| `feature_summary` | 用户级令牌桶整形，缓冲超额报文到 GTS 队列延迟转发，TCP 友好（适合视频等抖动敏感业务） |
| `feature_group` | `Shaping整形` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["RATE", "QUEDEPTH"]` |
| `first_release` | `UDG 20.1.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-020354`, `EV-CFA-§3.2`, `EV-CFA-附录F` |

#### GWFD-110313 智能Shaping组级带宽控制

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-110313` |
| `feature_name` | `智能Shaping组级带宽控制` |
| `feature_summary` | 组级智能整形，在普通 Shaping 基础上增加 AUTO 模式自动调优，按 ServiceLevel 差异化分配带宽 |
| `feature_group` | `Shaping整形` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["WORKMODE(AUTO/MANUAL)", "ASSUREMODE(EXPFIRST/RATEFIRST)"]` |
| `first_release` | `UDG 20.7.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-110313`, `EV-CFA-§3.2`, `EV-CFA-附录F.4` |

### 2.5 FUP 累计流量层

#### GWFD-020353 基于累计流量的策略控制（会话级FUP，UDG）

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-020353` |
| `feature_name` | `基于累计流量的策略控制` |
| `feature_summary` | UDG 侧会话级 FUP，URR 流量阈值监控，per Session 累计所有流量，不依赖 SA |
| `feature_group` | `FUP累计流量` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["USAGERPTMODE(ONLINE/MONITORINGKEY)", "接口(Gx/N7)"]` |
| `first_release` | `UDG 20.2.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-020353`, `EV-CFA-§3.4`, `EV-TK-01` |

#### WSFD-109104 基于累计流量的策略控制（会话级FUP，UNC）

| 字段 | 值 |
| --- | --- |
| `feature_id` | `WSFD-109104` |
| `feature_name` | `基于累计流量的策略控制` |
| `feature_summary` | UNC 侧会话级 FUP，接收 PCRF 阈值，N4 URR 下发；Gx 场景需额外配置 PCCFUNC/PCRF/PCCPOLICYGRP |
| `feature_group` | `FUP累计流量` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `variant_dimensions` | `["接口(Gx/N7)", "UMCH拥塞处理"]` |
| `first_release` | `UNC 20.3.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-109104`, `EV-CFA-§3.4`, `EV-TK-22` |

#### GWFD-110312 基于业务累计流量的策略控制（业务级FUP，UDG）

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-110312` |
| `feature_name` | `基于业务累计流量的策略控制` |
| `feature_summary` | UDG 侧业务级 FUP，per SVC/per APP 独立累计，依赖 SA 识别 + BWM 规则匹配 |
| `feature_group` | `FUP累计流量` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["累计粒度(per SVC/per APP)", "Monitoring-Key"]` |
| `first_release` | `UDG 20.5.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-110312`, `EV-CFA-§3.4` |

#### WSFD-211009 基于业务累计流量的策略控制（业务级FUP，UNC）

| 字段 | 值 |
| --- | --- |
| `feature_id` | `WSFD-211009` |
| `feature_name` | `基于业务累计流量的策略控制` |
| `feature_summary` | UNC 侧业务级 FUP，URR 绑定指定业务流的 PDRs，依赖 BWM(UNC) |
| `feature_group` | `FUP累计流量` |
| `applicable_nf_map` | `{"UNC": ["GGSN", "PGW-C", "SMF"]}` |
| `variant_dimensions` | `["接口(Gx/N7)"]` |
| `first_release` | `UNC 20.3.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-211009`, `EV-CFA-§3.4` |

### 2.6 QoS 保证层

#### GWFD-020358 业务触发的QoS保证（UDG）

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-020358` |
| `feature_name` | `业务触发的QoS保证` |
| `feature_summary` | UDG 侧 GBR 保证，SA 识别高价值业务 → URR(QOS模式)上报 → 触发专有承载/QoS Flow，保证带宽下限 |
| `feature_group` | `QoS保证` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["USAGERPTMODE(QOS)", "QOSTYPE(QOS_FLOW_PARA/QOS_BEARER_PARA)"]` |
| `first_release` | `UDG 20.2.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-020358`, `EV-CFA-§3.5` |

#### WSFD-109107 业务触发的QoS保证（UNC）

| 字段 | 值 |
| --- | --- |
| `feature_id` | `WSFD-109107` |
| `feature_name` | `业务触发的QoS保证` |
| `feature_summary` | UNC 侧 GBR 保证，接收 QoS 事件，发起专有承载(2/3/4G)/专有 QoS Flow(5G) 建立 |
| `feature_group` | `QoS保证` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `variant_dimensions` | `["接口(Gx/N7)", "QOSTYPE"]` |
| `first_release` | `UNC 20.5.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-109107`, `EV-CFA-§3.5` |

#### GWFD-110302 基于上下行解耦的视频承载信令控制

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-110302` |
| `feature_name` | `基于上下行解耦的视频承载信令控制` |
| `feature_summary` | 视频业务上下行解耦，只为下行建专载，上行走缺省，复用 QoS 保证的 QOSPROP 增加 DECOUPLINGSW 参数 |
| `feature_group` | `QoS保证` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["DECOUPLINGSW(ENABLE/DISABLE)"]` |
| `first_release` | `UDG 20.9.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-110302`, `EV-CFA-附录G`, `EV-CFA-§H.1` |

### 2.7 ADC 检测层

#### GWFD-020357 增强的ADC基本功能（UDG）

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-020357` |
| `feature_name` | `增强的ADC基本功能` |
| `feature_summary` | UDG 侧 ADC，基于 SA 的 L7 DPI 引擎检测应用，上报 APPLICATION_START/STOP（Gx）/APP_STA/STO（N7）触发 PCRF 动态策略 |
| `feature_group` | `ADC检测` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["接口(Gx/N7)", "Event Triggers"]` |
| `first_release` | `UDG 20.1.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-020357`, `EV-CTA-§7.5`, `EV-TK-27` |

#### WSFD-109102 ADC基本功能（UNC）

| 字段 | 值 |
| --- | --- |
| `feature_id` | `WSFD-109102` |
| `feature_name` | `ADC基本功能` |
| `feature_summary` | UNC 侧 ADC，转发 PCRF/PCF 应用检测事件，承载管理，三策略组（Normal/Start/Stop） |
| `feature_group` | `ADC检测` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `variant_dimensions` | `["接口(Gx/N7)"]` |
| `first_release` | `UNC 20.5.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-109102`, `EV-TK-28` |

### 2.8 无线资源优化层

#### GWFD-020359 IM类业务无线资源管控

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-020359` |
| `feature_name` | `IM类业务无线资源管控` |
| `feature_summary` | SA 识别 IM 业务（QQ/MSN/Fetion），映射 DSCP 值影响 BSC/RNC 无线调度，优化心跳保活 |
| `feature_group` | `无线优化` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["DSCP映射(QQ=12/MSN=14/Fetion=18)"]` |
| `first_release` | `UDG 20.7.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-020359`, `EV-CFA-附录G` |

#### GWFD-110301 基于终端系统的码率差异化控制

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-110301` |
| `feature_name` | `基于终端系统的码率差异化控制` |
| `feature_summary` | SA 识别终端 OS（Android/iOS/Windows），通过 BWM 框架增加 OSTYPE 维度实现码率差异化 |
| `feature_group` | `无线优化` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["OSTYPE"]` |
| `first_release` | `UDG 20.9.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-110301`, `EV-CFA-附录G` |

#### GWFD-110331 基于业务流标识的无线资源优化

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-110331` |
| `feature_name` | `基于业务流标识的无线资源优化` |
| `feature_summary` | SA 识别业务流 → 匹配 FPI 规则 → 标记 FPI/DSCP/GTP-U扩展头 → 基站按队列调度 |
| `feature_group` | `无线优化` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["FPI值范围(0-255)", "队列映射(0-6)"]` |
| `first_release` | `UDG 20.7.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-110331`, `EV-CFA-附录G` |

> **规划风险**: FPI值8~15映射的队列1调度权重仅为1（其他队列为10），配置时需避免将高价值业务映射到此范围。

#### GWFD-110332 基于小区负荷上报的无线资源优化（UDG）

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-110332` |
| `feature_name` | `基于小区负荷上报的无线资源优化` |
| `feature_summary` | UDG 侧小区负荷感知，RAN 上报负荷等级（Level 0-3）→ UDG 转发 → UNC 上报 PCRF → 动态调整 BWM |
| `feature_group` | `无线优化` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["负荷等级(Invalid/Normal/Congestion/Overload)"]` |
| `first_release` | `UDG 20.8.2` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-110332`, `EV-CFA-附录G` |

#### WSFD-211101 基于小区负荷上报的无线资源优化（UNC）

| 字段 | 值 |
| --- | --- |
| `feature_id` | `WSFD-211101` |
| `feature_name` | `基于小区负荷上报的无线资源优化` |
| `feature_summary` | UNC 侧负荷信息转发，接收 UDG 上报，转发 PCRF，CELL_CONGESTION_CHANGE Event Trigger |
| `feature_group` | `无线优化` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C"]}` |
| `variant_dimensions` | `["接口(Gx)"]` |
| `first_release` | `UNC 20.7.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-211101`, `EV-CFA-§4.3链路` |

### 2.9 位置感知层

#### WSFD-109108 基于接入点策略控制

| 字段 | 值 |
| --- | --- |
| `feature_id` | `WSFD-109108` |
| `feature_name` | `基于接入点策略控制` |
| `feature_summary` | WiFi 用户位置变化感知（UE_LOCAL_IP_ADDRESS_CHANGE, Trigger=43），激活预定义差异化带宽规则 |
| `feature_group` | `位置感知` |
| `applicable_nf_map` | `{"UNC": ["PGW-C"]}` |
| `variant_dimensions` | `["位置条件(PLMN/接入点)"]` |
| `first_release` | `UNC 20.5.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-109108`, `EV-TK-28`, `EV-TK-29` |

### 2.10 异常检测层

#### GWFD-020305 终端异常下行流量检测

| 字段 | 值 |
| --- | --- |
| `feature_id` | `GWFD-020305` |
| `feature_name` | `终端异常下行流量检测` |
| `feature_summary` | 异常流量检测，SA 辅助识别异常模式，阈值计数触发阻断恶意终端 |
| `feature_group` | `异常检测` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `variant_dimensions` | `["检测阈值", "阻断动作"]` |
| `first_release` | `UDG 20.5.0` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-020305`, `EV-CFA-§4.2` |

---

## 3. License

24 个特性均有独立 License 控制项，来源：`cross-feature-analysis.md` §2.3。UDG 16个 + UNC 8个。

### 3.1 UDG 侧 License（16个）

| `license_id` | `license_name` | `license_summary` | 关联Feature | `status` |
| --- | --- | --- | --- | --- |
| `LIC-UDG-SABS` | `LKV3G5SABS01` (82209749) | SA-Basic 基础License | GWFD-110101 | `active` |
| `LIC-UDG-PCCB` | `LKV3G5PCCB01` (82209825) | PCC基本功能License | GWFD-020351 | `active` |
| `LIC-UDG-TCSA` | `LKV3G5TCSA01` (82209832) | BWM License | GWFD-110311 | `active` |
| `LIC-UDG-FPBS` | `LKV3G5FPBS01` (82209776) | 业务级FUP License | GWFD-110312 | `active` |
| `LIC-UDG-FSHP` | `LKV3G5FSHP01` (82200FNS) | 智能Shaping License | GWFD-110313 | `active` |
| `LIC-UDG-PCBT` | `LKV3G5PCBT01` (82200AFM) | 会话级FUP License | GWFD-020353 | `active` |
| `LIC-UDG-SBTS` | `LKV3G5SBTS01` (82200AFN) | Shaping License | GWFD-020354 | `active` |
| `LIC-UDG-ADTD` | `LKV3G5ADTD01` (82200BAJ) | 异常检测 License | GWFD-020305 | `active` |
| `LIC-UDG-ADCF` | `LKV3G5ADCF01` (82200AFK) | ADC License | GWFD-020357 | `active` |
| `LIC-UDG-STQE` | `LKV3G5STQE01` (82200AFP) | QoS保证 License | GWFD-020358 | `active` |
| `LIC-UDG-ITSR` | `LKV3G5ITSR01` (82200BLD) | IM管控 License | GWFD-020359 | `active` |
| `LIC-UDG-RDSC` | `LKV3G5RDSC01` (82209784) | 码率差异化 License | GWFD-110301 | `active` |
| `LIC-UDG-SCUD` | `LKV3G5SCUD01` (82200EBQ) | 上下行解耦 License | GWFD-110302 | `active` |
| `LIC-UDG-WOFR` | `LKV3G5WOFR01` (82200DHE) | FPI标记 License | GWFD-110331 | `active` |
| `LIC-UDG-WOCR` | `LKV3G5WOCR01` (82200DHW) | 小区负荷 License | GWFD-110332 | `active` |
| `LIC-UDG-SSDUC` | `LKV3G5SSDUC1` (81203996) | SA特征库管控 License | GWFD-111600 | `active` |

### 3.2 UNC 侧 License（8个）

| `license_id` | `license_name` | `license_summary` | 关联Feature | `status` |
| --- | --- | --- | --- | --- |
| `LIC-UNC-SPCC` | `LKV3W9SPCC11` (82207979) | PCC基本功能 SMF/PGW-C | WSFD-109101 | `active` |
| `LIC-UNC-ADCF` | `LKV2BADCF01` (82200BNK) | ADC License | WSFD-109102 | `active` |
| `LIC-UNC-PCBT` | `LKV3W9PCBT12` (82207980) | 会话级FUP License | WSFD-109104 | `active` |
| `LIC-UNC-STQE` | `LKV3W9STQE11` (82208819) | QoS保证 License | WSFD-109107 | `active` |
| `LIC-UNC-PWULI` | `LKV3WPWULI11` (82209475) | 接入点策略 License | WSFD-109108 | `active` |
| `LIC-UNC-CBSA` | `LKV3TCBSA01` (82200CQU) | BWM(UNC) License | WSFD-211005 | `active` |
| `LIC-UNC-FUPSAT` | `LKV2FUPSAT01` (82200BNU) | 业务级FUP(UNC) License | WSFD-211009 | `active` |
| `LIC-UNC-WOCR` | `LKV3W9WOCR11` (82209457) | 小区负荷(UNC) License | WSFD-211101 | `active` |

### 3.3 License 依赖链（来源：§2.3）

```
基础License（必须先开启）
├── UDG: LIC-UDG-PCCB (PCC) + LIC-UDG-SABS (SA-Basic)
└── UNC: LIC-UNC-SPCC (PCC)
        │
        ▼
功能License（在基础License之上叠加）
├── UDG: LIC-UDG-TCSA (BWM) 等14个
└── UNC: LIC-UNC-CBSA (BWM) 等7个
```

---

## 4. Feature 依赖关系（depends_on）

来源：`cross-feature-analysis.md` §4.1-4.2。

### 4.1 核心依赖边

| 起点 | 关系 | 终点 | 依赖类型 | 说明 |
| --- | --- | --- | --- | --- |
| `GWFD-111600` | `maintains`→`depends_on` | `GWFD-110101` | data_maintenance | SA特征库数据维护 |
| `GWFD-110311` | `depends_on` | `GWFD-110101` | direct | BWM依赖SA识别业务 |
| `GWFD-110311` | `depends_on` | `GWFD-020351` | direct | BWM依赖PCC规则体系 |
| `GWFD-110312` | `depends_on` | `GWFD-110101` | direct | 业务FUP依赖SA识别按业务累计 |
| `GWFD-110312` | `depends_on` | `GWFD-110311` | direct | 业务FUP依赖BWM规则匹配 |
| `GWFD-020354` | `depends_on` | `GWFD-110101` | direct | Shaping依赖SA识别业务 |
| `GWFD-110313` | `depends_on` | `GWFD-110311` | direct | 智能Shaping依赖BWM |
| `GWFD-110313` | `depends_on` | `GWFD-020354` | direct | 智能Shaping依赖Shaping |
| `GWFD-020357` | `depends_on` | `GWFD-110101` | direct | ADC使用SA的L7 DPI引擎 |
| `GWFD-020358` | `depends_on` | `GWFD-110101` | direct | QoS保证依赖SA识别触发 |
| `GWFD-020358` | `depends_on` | `GWFD-020351` | direct | QoS保证依赖PCC专载信令 |
| `GWFD-020305` | `depends_on` | `GWFD-110101` | indirect | 异常检测SA辅助识别 |
| `GWFD-020359` | `depends_on` | `GWFD-110101` | direct | IM管控依赖SA识别IM业务 |
| `GWFD-110301` | `depends_on` | `GWFD-110101` | direct | 码率差异化依赖SA识别终端OS |
| `GWFD-110301` | `depends_on` | `GWFD-110311` | indirect | 码率差异化复用BWM框架 |
| `GWFD-110302` | `depends_on` | `GWFD-020358` | direct | 视频解耦是QoS保证增强版 |
| `GWFD-110331` | `depends_on` | `GWFD-110101` | direct | FPI标记依赖SA识别业务流 |
| `GWFD-110332` | `depends_on` | `GWFD-110311` | indirect | 小区负荷需BWM配合执行 |
| `WSFD-211005` | `depends_on` | `WSFD-109101` | direct | BWM(UNC)依赖PCC(UNC) |
| `WSFD-211009` | `depends_on` | `WSFD-109101` | direct | 业务FUP(UNC)依赖PCC(UNC) |
| `WSFD-211009` | `depends_on` | `WSFD-211005` | direct | 业务FUP(UNC)依赖BWM(UNC) |
| `WSFD-109104` | `depends_on` | `WSFD-109101` | direct | 会话FUP(UNC)依赖PCC(UNC) |
| `WSFD-109107` | `depends_on` | `WSFD-109101` | direct | QoS保证(UNC)依赖PCC(UNC) |
| `WSFD-211101` | `depends_on` | `WSFD-109101` | direct | 小区负荷(UNC)依赖PCC(UNC) |

### 4.2 辐射范围

**SA-Basic (GWFD-110101)** 辐射范围最大，12个特性直接或间接依赖它：
GWFD-110311, GWFD-110312, GWFD-020354, GWFD-110313, GWFD-020357, GWFD-020358, GWFD-020305, GWFD-020359, GWFD-110301, GWFD-110302, GWFD-110331, GWFD-110332。

**PCC基本功能 (GWFD-020351)** 辐射：11个UDG特性。
**PCC基本功能 (WSFD-109101)** 辐射：7个UNC特性。

### 4.3 UDG-UNC 配对协作（8对）

| UDG侧 | UNC侧 | 协作模式 |
| --- | --- | --- |
| GWFD-020351 | WSFD-109101 | UNC接收PCRF/PCF策略 → N4下发 → UDG执行 |
| GWFD-110311 | WSFD-211005 | UNC配置BWM规则(POLICYTYPE=BWM) → N4 → UDG SA+BWM执行 |
| GWFD-020353 | WSFD-109104 | UNC接收PCRF阈值 → N4 URR → UDG流量检测 → 上报 → 降速 |
| GWFD-110312 | WSFD-211009 | 同上但粒度为业务级 |
| GWFD-020358 | WSFD-109107 | UDG识别 → 上报QoS事件 → UNC专载建立 |
| GWFD-020357 | WSFD-109102 | UDG检测应用 → UNC转发PCRF → 策略决策 |
| GWFD-110332 | WSFD-211101 | UDG检测负荷 → UNC转发PCRF → BWM调整 |
| GWFD-110101 | WSFD-211005 | SA特征库仅驻留UDG，UNC通过N4间接依赖 |

---

## 5. FeatureRule

5 个关键特性级规则。

| `rule_id` | `owner_ref_type` | `owner_ref` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `rule_logic` | `violation_effect` | `status` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `FR-BW-01` | `feature` | `GWFD-110311` | BWM三级控制层级不叠加 | `restriction_rule` | `explicit` | `restriction` | 用户级/组级/全局级 BWM 控制不可在同一对象上叠加；同一业务流只能匹配一个层级的 BWMRULE | 多层级规则冲突，匹配混乱 | `active` | `EV-FK-110311`, `EV-CFA-§3.2` |
| `FR-BW-02` | `feature` | `GWFD-110313` | 智能Shaping依赖链 | `dependency_rule` | `explicit` | `principle` | 智能Shaping 需 BWM(LIC-UDG-TCSA) + Shaping(LIC-UDG-SBTS) 双 License 同时开启 | 功能不可用 | `active` | `EV-FK-110313`, `EV-CFA-§4.1` |
| `FR-BW-03` | `feature` | `WSFD-211005` | POLICYTYPE=BWM仅UNC侧 | `naming_rule` | `explicit` | `design` | `ADD RULE(POLICYTYPE=BWM)` 是 UNC 侧独有；UDG 侧用 BWM 专有命令体系(BWMSERVICE/BWMCONTROLLER等) | 侧别配置错误，规则无法生效 | `active` | `EV-FK-211005`, `EV-CFA-§5.6` |
| `FR-BW-04` | `feature` | `GWFD-110312` | 业务FUP依赖SA | `dependency_rule` | `explicit` | `principle` | 业务级FUP需 SA 识别才能 per SVC/per APP 独立累计；会话级FUP(GWFD-020353)不依赖SA | 业务级FUP不生效 | `active` | `EV-FK-110312`, `EV-CFA-§3.4` |
| `FR-BW-05` | `feature` | `GWFD-020358` | QoS保证URR模式 | `validation_rule` | `explicit` | `config` | QoS保证的 URR.USAGERPTMODE 必须为 QOS（区别于FUP的ONLINE/MONITORINGKEY） | QoS事件无法上报，专载不建立 | `active` | `EV-FK-020358`, `EV-CFA-§5.2` |

---

## 6. FeatureTaskOrderEdge（核心特性 task 展开顺序）

> 完整 task 定义见 `03-task-layer.md`。此处定义核心特性的 task 编排顺序。

### 6.1 GWFD-110311 BWM task 顺序

| `edge_id` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `requiredness` | `priority_hint` | `propagated_context` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `FE-BW-01-1` | `GWFD-110311` | `T-007` | `T-008` | `precedes` | `required` | `1` | `License开关` | `EV-FK-110311` |
| `FE-BW-01-2` | `GWFD-110311` | `T-008` | `T-101` | `precedes` | `required` | `2` | `SA特征库` | `EV-FK-110311` |
| `FE-BW-01-3` | `GWFD-110311` | `T-101` | `T-102` | `precedes` | `required` | `3` | `BWM策略规划` | `EV-FK-110311` |
| `FE-BW-01-4` | `GWFD-110311` | `T-102` | `T-103` | `precedes` | `required` | `4` | `BWMSERVICE` | `EV-FK-110311` |
| `FE-BW-01-5` | `GWFD-110311` | `T-103` | `T-104` | `precedes` | `required` | `5` | `BWMCONTROLLER` | `EV-FK-110311` |
| `FE-BW-01-6` | `GWFD-110311` | `T-104` | `T-105` | `precedes` | `required` | `6` | `BWMUSERGROUP` | `EV-FK-110311` |
| `FE-BW-01-7` | `GWFD-110311` | `T-105` | `T-106` | `precedes` | `required` | `7` | `BWMRULE` | `EV-FK-110311` |
| `FE-BW-01-8` | `GWFD-110311` | `T-106` | `T-006` | `must_be_last` | `required` | `8` | `APN绑定→REFRESHSRV` | `EV-FK-110311`, `EV-CFA-§5.5` |

### 6.2 GWFD-020353 会话级FUP task 顺序

| `edge_id` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `requiredness` | `propagated_context` |
| --- | --- | --- | --- | --- | --- | --- |
| `FE-BW-02-1` | `GWFD-020353` | `T-007` | `T-201` | `precedes` | `required` | `License` |
| `FE-BW-02-2` | `GWFD-020353` | `T-201` | `T-202` | `precedes` | `required` | `FUP策略规划` |
| `FE-BW-02-3` | `GWFD-020353` | `T-202` | `T-203` | `precedes` | `required` | `URRID` |
| `FE-BW-02-4` | `GWFD-020353` | `T-203` | `T-204` | `precedes` | `required` | `URRGROUPNAME` |
| `FE-BW-02-5` | `GWFD-020353` | `T-204` | `T-006` | `must_be_last` | `required` | `PCCPOLICYGRP→REFRESHSRV` |

### 6.3 WSFD-211005 BWM(UNC) task 顺序

| `edge_id` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `requiredness` | `propagated_context` |
| --- | --- | --- | --- | --- | --- | --- |
| `FE-BW-03-1` | `WSFD-211005` | `T-007` | `T-501` | `precedes` | `required` | `License` |
| `FE-BW-03-2` | `WSFD-211005` | `T-501` | `T-003` | `precedes` | `required` | `PCRF组` |
| `FE-BW-03-3` | `WSFD-211005` | `T-003` | `T-004` | `precedes` | `required` | `RULENAME(POLICYTYPE=BWM)` |
| `FE-BW-03-4` | `WSFD-211005` | `T-004` | `T-005` | `precedes` | `required` | `USERPROFILE` |

### 6.4 GWFD-110313 智能Shaping task 顺序（依赖BWM+Shaping）

| `edge_id` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `requiredness` | `propagated_context` |
| --- | --- | --- | --- | --- | --- | --- |
| `FE-BW-04-1` | `GWFD-110313` | `T-007` | `T-103` | `depends_on` | `required` | `双License` |
| `FE-BW-04-2` | `GWFD-110313` | `T-103` | `T-107` | `precedes` | `required` | `BWMCONTROLLER(CTRLTYPE=SHAPING)` |
| `FE-BW-04-3` | `GWFD-110313` | `T-107` | `T-006` | `must_be_last` | `required` | `BCSRVLEVELPLY→REFRESHSRV` |

---

## 7. 特性图谱关系边汇总

| 起点 | 关系 | 终点 | 数量 |
| --- | --- | --- | --- |
| `Feature` | `depends_on` | `Feature` | 24条（见§4.1） |
| `Feature` | `requires_license` | `License` | 24条（1:1） |
| `Feature` | `constrained_by` | `FeatureRule` | 5条（见§5） |
| `Feature` | `orchestrates` | `FeatureTaskOrderEdge` | 见§6（核心特性） |
| `Feature` | `decomposes_to` | `ConfigTask` | 见`05-cross-layer-mapping.md` |
| `Feature` | `uses_semantic_object` | `SemanticObject` | 见`05-cross-layer-mapping.md` |
| `Feature` | `supported_by` | `EvidenceSource` | 见`06-evidence-index.md` |
