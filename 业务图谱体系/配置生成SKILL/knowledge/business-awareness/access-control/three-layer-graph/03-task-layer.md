# 访问限制场景三层图谱 · 第3层：任务原子层

> **文件定位**：`three-layer-graph/03-task-layer.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §10 任务原子层（§10.3 ConfigTask / §10.4 TaskRule / §10.5 TaskCommandOrderEdge / §10.6 关系）
> **作用**：实例化 17 个 ConfigTask（8 generic 复用 + 9 独有） + 8 条 TaskRule + TaskCommandOrderEdge
> **数据来源**：`feature-knowledge/cross-feature-analysis.md`（附录 D 典型端到端配置流程、附录 B 命令交叉参考、附录 C 配置对象复用矩阵、附录 E 双轨动作机制、附录 F POLICYTYPE 全景表）、`feature-knowledge/*.md`（11 个独有特性的 §4 配置流程 / §5 配置案例）
> **质量标杆**：`带宽控制场景/three-layer-graph/03-task-layer.md`（751 行，generic 复用 + 编号段隔离 + 动作轨道规则）

---

## §0 任务层总览

### 0.1 ConfigTask 分类

| 类型 | 数量 | 编号范围 | 说明 |
|------|------|---------|------|
| generic（通用，三场景复用） | 8 | `T-001~T-008` | 业务分类 / 流过滤 / PCC 规则 / 用户模板 / APN 绑定 / 策略刷新 / License / SA 特征库 |
| feature_specific（访问限制独有，轨道A） | 7 | `T-AC-101~T-AC-107` | 头增强 / HTTP 智能重定向 / DNS 纠错 / Portal / WebProxy / ADC 参数 / 头防欺诈子模式 |
| feature_specific（URL过滤独有，轨道B） | 1 | `T-AC-108` | URL 过滤（ICAP 互通 + CF 模板/分类） |
| feature_specific（接入控制触发，UNC侧） | 1 | `T-AC-109` | 位置条件策略（USRLOCATION / USRLOCATIONGRP） |
| **合计** | **17** | — | — |

> **Task 编号段说明**：
> - `T-001~T-008`：通用 Task（generic），三场景共享基础配置步骤（直接复用计费 / 带宽控制场景的 generic 定义，**编号相同、语义相同、跨场景可合并**）
> - `T-AC-101~T-AC-107`：访问限制**轨道 A（PCC 体系）**独有 Task，对应头增强族 / 重定向族 / ADC / 防欺诈
> - `T-AC-108`：访问限制**轨道 B（URL 过滤体系）**独有 Task，承载 ICAP 互通 + CF 模板/分类整套独立配置链
> - `T-AC-109`：UNC 侧接入控制触发（位置条件），与 UDG 侧动作执行解耦

### 0.2 任务原子化原则

1. **每 Task 一个明确 goal**：一个可复用的配置步骤独立成 Task（如"配置头增强"不等同于"配置 PCC 规则"，前者操作 HEADEN 对象，后者操作 RULE 对象）
2. **generic 优先**：跨 3+ 特性复用的步骤提升为 generic（三四层过滤链、PCC 规则、用户模板、APN 绑定、刷新、License、SA 特征库——访问限制全部复用带宽场景已建 generic）
3. **双轨道分离**：轨道 A 动作（RULE.POLICYTYPE 隐式驱动，轨道 A 内含五子轨：ADC / PCC / HEADEN / SMARTREDIRECT / WEBPROXY）与轨道 B 动作（CFTEMPLATE / CONTCATEGBIND.ACTION 显式驱动，独立于 RULE 体系）拆为独立 Task，避免 ConfigObject 体系混淆
4. **POLICYTYPE 路由由 TaskRule 表达**：同一 generic Task `T-003 配置PCC规则` 通过 TaskRule `TR-AC-02` 区分轨道 A 的 5 种 POLICYTYPE（即五子轨），调用不同 Task / 操作不同 ConfigObject
5. **命令顺序通过 TaskCommandOrderEdge 表达**：Task 内部命令依赖通过本文件 §9 的编排边表达；Task 间顺序通过 `05-cross-layer-mapping.md` 的 FeatureTaskOrderEdge 表达

### 0.3 与计费 / 带宽控制场景的编号段隔离

> 访问限制场景独有 Task 使用 `T-AC-101~T-AC-109` 编号段（AC = Access Control）：
> - 与计费场景 `T-101~T-311`（计费三件套 / 在线计费 / 融合计费 / CG 接口）**不重叠**
> - 与带宽控制场景 `T-101~T-603`（BWM / FUP / QoS / ADC / UNC 控制面 / 无线优化）**不重叠**
>
> 通用 Task `T-001~T-008` 三场景编号相同、语义相同。合并三场景时：
> - generic Task 需加场景前缀（如 `T-CH-001` / `T-BW-001` / `T-AC-001`）避免节点重复，但语义可直接合并为同一 generic 节点
> - 独有 Task 因编号段天然隔离，可无缝合并

### 0.4 Evidence ID 命名约定（与 02-feature 对齐）

> - `EV-FK-AC-NN`（NN = 01~15）：访问限制场景 15 特性索引表序号（与 02-feature-graph.md 一致）
> - 复用特性沿用跨场景编号：`EV-FK-01`（SA-Basic）/ `EV-FK-03`（PCC-UDG）/ `EV-FK-17`（PCC-UNC）/ `EV-FK-21`（ADC-UNC）
> - `EV-CA-01`：访问限制场景跨特性横向分析报告（含附录 D/E/F）
> - `EV-CA-D1`~`EV-CA-D4`：附录 D 的 4 类端到端配置流程（DISCARD / HEADEN / REDIRECT / 接入控制）——任务编排边的直接来源

---

## §1 通用 Task（generic，8 个，三场景共享）

> **复用声明**：以下 8 个 generic Task 与计费场景 `03-task-layer.md` §1、带宽控制场景 `03-task-layer.md` §1 定义完全一致。访问限制场景仅补充 `reused_by` 列表为本场景的特性清单。**三场景合并时，generic Task 直接合并为同一节点**（task_id 相同、字段相同），独有 Task 通过编号段隔离合并。

### T-001 规划业务分类与识别条件

| 字段 | 值 |
|------|---|
| `task_id` | `T-001` |
| `task_name` | `规划业务分类与识别条件` |
| `task_summary` | 建立 SVC 业务大类与 APP 具体应用的识别规则，为 ADC / 头增强族 / 重定向族 / URL 过滤 / 防欺诈提供 SA 分类基础 |
| `task_scope_type` | `generic` |
| `task_goal` | 定义三四层 + 七层识别条件，输出 CATEGORYPROP / FILTER / L7FILTER / EXTENDEDFILTER 实例集 |
| `input_contract` | 业务需求清单、目标业务类型列表、URL 域名 / 错误码 / UserAgent 匹配规则 |
| `output_contract` | 业务分类表、FILTER / L7FILTER / EXTENDEDFILTER 实例集 |
| `scopes` | UDG 用户面 |
| `command_refs` | `ADD CATEGORYPROP`, `ADD FILTER`, `ADD L7FILTER`, `ADD EXTENDEDFILTER`, `ADD ERRORCODE` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-01`, `EV-FK-AC-01`, `EV-CA-01` |
| `reused_by` | ADC / 头增强族（HTTP / HTTPS / RTSP）/ 重定向族（HTTP 智能重定向 / DNS 纠错 / Portal）/ URL 过滤 / 头防欺诈 |

### T-002 配置流过滤器与绑定

| 字段 | 值 |
|------|---|
| `task_id` | `T-002` |
| `task_name` | `配置流过滤器与绑定` |
| `task_summary` | 建立可复用的流匹配条件，承接 ADC / 头增强族 / 重定向族 / URL 过滤 / 防欺诈规则匹配入口 |
| `task_scope_type` | `generic` |
| `task_goal` | 配置 FLOWFILTER + FLTBINDFLOWF + PROTBINDFLOWF，定义业务流匹配条件 |
| `input_contract` | T-001 输出的业务分类表（FILTER / L7FILTER 实例） |
| `output_contract` | FLOWFILTER + 绑定关系实例集 |
| `scopes` | UDG 用户面 |
| `command_refs` | `ADD FLOWFILTER`, `ADD FLTBINDFLOWF`, `ADD PROTBINDFLOWF` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-01`, `EV-FK-AC-02`, `EV-CA-01` |
| `reused_by` | 全部 11 个独有特性（轨道 A 全部 + 轨道 B URL 过滤触发层共用三四层匹配链） |

### T-003 配置 PCC 规则

| 字段 | 值 |
|------|---|
| `task_id` | `T-003` |
| `task_name` | `配置PCC规则` |
| `task_summary` | 通过 ADD RULE 定义 PCC 策略规则，**POLICYTYPE 由决策点 DP-AC-01 定**（ADC / PCC / HEADEN / SMARTREDIRECT / WEBPROXY），是访问限制轨道 A 动作类型的核心区分 |
| `task_scope_type` | `generic` |
| `task_goal` | 建立策略规则实例，承接 FLOWFILTER 与策略动作，POLICYTYPE 标识动作类型分支并决定 POLICYNAME 指向对象 |
| `input_contract` | T-002 输出的 FLOWFILTER + 决策点 DP-AC-01（POLICYTYPE 取值） |
| `output_contract` | RULE 实例（POLICYTYPE = ADC / PCC / HEADEN / SMARTREDIRECT / WEBPROXY） |
| `scopes` | UDG 用户面（动态 PCC 场景需 PCRF / PCF 下发；本地 PCC 场景本地定义） |
| `command_refs` | `ADD RULE` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-AC-02`, `EV-FK-AC-04`, `EV-CA-01` |
| `reused_by` | 全部 10 个 UDG 独有特性（ADC / 头增强族 / 重定向族 / 头防欺诈 / URL 过滤） |
| `note` | POLICYTYPE 是访问限制轨道 A 的动作路由器（发现一 / 附录 F）：ADC=应用检测、PCC=标准 PCC（Portal 计费 / URL 过滤触发）、HEADEN=头增强、SMARTREDIRECT=HTTP 智能重定向 + DNS 纠错共用、WEBPROXY=Web Proxy。**URL 过滤的 RULE 用 POLICYTYPE=PCC，但实际 BLOCK / PERMIT / REDIRECT 动作不走 PCCPOLICYGRP，而走 CFTEMPLATE / CONTCATEGBIND（轨道 B）** |

### T-004 配置用户模板与规则绑定

| 字段 | 值 |
|------|---|
| `task_id` | `T-004` |
| `task_name` | `配置用户模板与规则绑定` |
| `task_summary` | 配置 USERPROFILE（含 Portal captive 的 CAPMODETHRES 定时器）并通过 RULEBINDING 绑定 RULE |
| `task_scope_type` | `generic` |
| `task_goal` | 将规则组织为用户模板，承载多类型规则组合与 Portal captive 周期 |
| `input_contract` | T-003 输出的 RULE 实例集 |
| `output_contract` | USERPROFILE + RULEBINDING 实例集 |
| `scopes` | UDG 用户面 / UNC 控制面 |
| `command_refs` | `ADD USERPROFILE`, `ADD RULEBINDING` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-AC-02`, `EV-CA-01` |
| `reused_by` | 全部 10 个 UDG 独有特性 |
| `note` | Portal 特性（GWFD-110281）的 captive 周期配置在 USERPROFILE.CAPMODETHRES（如 `CAPMODETHRES=6` 表示 6 分钟），而非 RULE——这是 Portal 与其他重定向族的关键差异 |

### T-005 配置用户模板组与 APN 绑定

| 字段 | 值 |
|------|---|
| `task_id` | `T-005` |
| `task_name` | `配置用户模板组与APN绑定` |
| `task_summary` | 完成 APN / DNN 级策略生效的标准绑定链（USRPROFGROUP → UPBINDUPG → APNUSRPROFG），UNC 侧 UPBINDUPG 含 LOCGROUPNAME 位置组绑定 |
| `task_scope_type` | `generic` |
| `task_goal` | 使策略按 APN / DNN 生效，UNC 侧同时承载位置组绑定 |
| `input_contract` | T-004 输出的 USERPROFILE 实例（UNC 侧还需 USRLOCATIONGRP 实例） |
| `output_contract` | USRPROFGROUP + UPBINDUPG + APNUSRPROFG 实例集 |
| `scopes` | UNC 控制面（UDG 侧仅 Portal / WebProxy / URL 过滤需 ADD APN） |
| `command_refs` | `ADD USRPROFGROUP`, `ADD UPBINDUPG`, `MOD UPBINDUPG`, `ADD APNUSRPROFG`, `ADD APN` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-01`, `EV-FK-AC-15` |
| `reused_by` | UNC 侧 WSFD-211001 位置触发（绑定链完整）；UDG 侧 Portal / WebProxy / URL 过滤（仅 ADD APN） |

### T-006 策略刷新生效

| 字段 | 值 |
|------|---|
| `task_id` | `T-006` |
| `task_name` | `策略刷新生效` |
| `task_summary` | 执行 SET REFRESHSRV 刷新策略，约 60 秒后完全下发（PROTBINDFLOWF 定时器） |
| `task_scope_type` | `generic` |
| `task_goal` | 使 UDG 侧 FILTER / FLOWFILTER / L7FILTER / 策略配置变更生效 |
| `input_contract` | 所有 FILTER / FLOWFILTER / L7FILTER / 策略配置完成 |
| `output_contract` | 配置生效 |
| `scopes` | UDG 用户面 |
| `command_refs` | `SET REFRESHSRV` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-01`, `EV-FK-AC-01`, `EV-FK-AC-02`, `EV-CA-01` |
| `reused_by` | 全部 10 个 UDG 独有特性（FILTER / L7FILTER 变更后均需刷新） |
| `must_be_last` | `true` |
| `note` | TR-AC-01 硬约束：必须在所有 FILTER / FLOWFILTER / L7FILTER / RULE 配置之后执行；REFRESHTYPE = ALL（全量）/ USERPROFILE（用户模板级）；执行后约 60 秒（PROTBINDFLOWF 定时器）策略完全下发 |

### T-007 License 开启

| 字段 | 值 |
|------|---|
| `task_id` | `T-007` |
| `task_name` | `License开启` |
| `task_summary` | 通过 SET LICENSESWITCH 开启对应特性的 License，是全部特性的前置门控；防欺诈 License 强依赖头增强 License（双开） |
| `task_scope_type` | `generic` |
| `task_goal` | 满足 License 前置门控，使特性功能可用 |
| `input_contract` | 特性清单、对应 License 项（UDG 独有 `LKV3G5` 前缀；UNC 独有 `LKV2` 前缀） |
| `output_contract` | License 使能 |
| `scopes` | UDG 用户面 / UNC 控制面 |
| `command_refs` | `SET LICENSESWITCH` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-01` |
| `reused_by` | 全部 11 个独有特性（10 UDG + 1 UNC）；复用特性（SA-Basic / PCC / ADC UNC）也通过此 Task 开启 |
| `note` | UDG 与 UNC 的 License 编号体系完全独立（`LKV3G5` vs `LKV2` / `LKV3W9`），需分别获取；头防欺诈 License（`LKV3G5HHAS01`）与 HTTP 头增强 License（`LKV3G5HTHE01`）需双开（强耦合，TR-AC-04） |

### T-008 SA 特征库加载

| 字段 | 值 |
|------|---|
| `task_id` | `T-008` |
| `task_name` | `SA特征库加载` |
| `task_summary` | 加载 SA 特征库与解析库，为 SA-Basic 引擎提供 L3 / L4 / L7 业务识别数据基础 |
| `task_scope_type` | `generic` |
| `task_goal` | 使 SA 引擎具备协议解析能力（HTTP / HTTPS / RTSP / DNS / URL 提取） |
| `input_contract` | SA 特征库文件（signature_db.dat）、解析库文件（parser_db.dat） |
| `output_contract` | SA 引擎就绪 |
| `scopes` | UDG 用户面 |
| `command_refs` | `LOD SIGNATUREDB`, `LOD PARSERDB` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-01`, `EV-FK-AC-01` |
| `reused_by` | SA-Basic（GWFD-110101）+ ADC / 头增强族 / 重定向族 / URL 过滤 / 头防欺诈（10 个独有特性直接依赖 SA 解析能力） |
| `note` | SA-Basic 辐射范围最大：访问限制场景 10 个独有特性全部直接依赖 SA 的协议解析能力（附录 G SA 协议解析依赖矩阵） |

---

## §2 访问限制轨道 A 独有 Task（feature_specific，7 个）

> 轨道 A = PCC 体系（RULE.POLICYTYPE 驱动，隐式动作）。涵盖 ADC / 头增强族 / 重定向族 / 头防欺诈。

### T-AC-101 配置 ADC 检测参数与规则

| 字段 | 值 |
|------|---|
| `task_id` | `T-AC-101` |
| `task_name` | `配置ADC检测参数与规则` |
| `task_summary` | 配置 ADC 流信息上报与迟滞定时器（ADCPARA），并通过 RULE.POLICYTYPE=ADC 建立应用检测规则，触发 APPLICATION_START / STOP 事件上报 PCRF / PCF |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 使能 ADC 应用检测与事件上报，为动态 PCC 策略提供"应用感知层"输入；不匹配规则时兜底阻塞 |
| `input_contract` | T-002 FLOWFILTER 实例、检测目标应用列表 |
| `output_contract` | ADCPARA 实例 + RULE（POLICYTYPE=ADC）实例 |
| `scopes` | UDG 用户面 |
| `command_refs` | `ADD ADCPARA`, `ADD RULE` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-AC-04`, `EV-FK-21`, `EV-CA-01`, `EV-CA-D1` |
| `feature_ref` | GWFD-020357, WSFD-109102 |
| `note` | ADC 是 L7 动态访问限制的"应用感知层"横切依赖（发现八）；兜底阻塞机制——业务流匹配不上所有 PCC rule 时，UDG 阻塞业务流 |

### T-AC-102 配置头增强对象（含防欺诈子模式）

| 字段 | 值 |
|------|---|
| `task_id` | `T-AC-102` |
| `task_name` | `配置头增强对象` |
| `task_summary` | 通过 ADD HEADEN 定义跨协议（HTTP / HTTPS / RTSP）复用的头增强对象，含 ANTIFRAUD / GRAYLIST 子模式；RULE.POLICYTYPE=HEADEN，POLICYNAME 指向 HEADEN 对象名 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立头增强对象，插入 MSISDN / IMSI / IMEI 等用户信息字段；启用防欺诈时执行"检测 → 纠正 / 清理 → 插入"前置流程 |
| `input_contract` | 字段类型（DATATYPE=IMSI1/MSISDN1 等）、加密算法（AES128 / SHA256）、前缀名（如 `X-imsi`）、防欺诈使能决策（DP-AC-02） |
| `output_contract` | HEADEN 对象实例（含 ANTIFRAUD / GRAYLIST 参数）+ RULE（POLICYTYPE=HEADEN）实例 |
| `scopes` | UDG 用户面 |
| `command_refs` | `ADD HEADEN`, `ADD WELLKNOWNPORT`, `SET BASE64`, `ADD RULE` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-AC-06`, `EV-FK-AC-07`, `EV-FK-AC-08`, `EV-FK-AC-13`, `EV-CA-01`, `EV-CA-D2` |
| `feature_ref` | GWFD-110261, GWFD-110262, GWFD-110263, GWFD-110401 |
| `note` | TR-AC-04 头防欺诈强耦合：启用 ANTIFRAUD=ENABLE 必须先开启 HTTP 头增强 License（双开）；执行顺序：防欺诈检测 → 字段纠正 / 冗余清理 → 头增强插入（灰名单模式跳过插入）；RTSP 头增强不支持防欺诈（族内唯一例外）。HEADEN 跨 4 特性复用（HTTP / HTTPS / RTSP + 防欺诈），是协议无关的统一头增强对象（发现五） |

### T-AC-103 配置 HTTP 智能重定向

| 字段 | 值 |
|------|---|
| `task_id` | `T-AC-103` |
| `task_name` | `配置HTTP智能重定向` |
| `task_summary` | 通过 ADD SMARTHTTPREDIR + ADD REDIRAPPENDINFO 定义 HTTP 响应改写动作；RULE.POLICYTYPE=SMARTREDIRECT，POLICYNAME 指向 SMARTHTTPREDIR 对象 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 在 L7 HTTP 响应层（301 / 302 / 303）将用户业务流引导到指定服务器，可携带 MSISDN / IMSI / IMEI |
| `input_contract` | T-001 的 EXTENDEDFILTER + ERRORCODE 实例（多维度匹配）、目标服务器 URL、携带信息配置 |
| `output_contract` | SMARTHTTPREDIR + REDIRAPPENDINFO 实例 + RULE（POLICYTYPE=SMARTREDIRECT）实例 |
| `scopes` | UDG 用户面 |
| `command_refs` | `ADD EXTENDEDFILTER`, `ADD ERRORCODE`, `ADD REDIRAPPENDINFO`, `ADD SMARTHTTPREDIR`, `ADD RULE` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-AC-12`, `EV-CA-01`, `EV-CA-D3` |
| `feature_ref` | GWFD-110284 |
| `note` | TR-AC-02：HTTP 智能重定向与 DNS 纠错**共用 POLICYTYPE=SMARTREDIRECT**，区分点在 POLICYNAME 指向（SMARTHTTPREDIR vs DNSOVERWRITING）；不支持 HTTPS / HTTP2.0（加密无法获取 HTTP 响应特征，发现二） |

### T-AC-104 配置 DNS 纠错

| 字段 | 值 |
|------|---|
| `task_id` | `T-AC-104` |
| `task_name` | `配置DNS纠错` |
| `task_summary` | 通过 ADD DNSOVERWRITING 定义 DNS 响应重写动作（绑定第三方 Platform IP）；RULE.POLICYTYPE=SMARTREDIRECT（与 HTTP 智能重定向共用），POLICYNAME 指向 DNSOVERWRITING 对象 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 在 DNS 解析层（最早介入，未建 TCP）将错误域名引导到搜索引擎 / Platform |
| `input_contract` | T-001 的 EXTENDEDFILTER（URL 域名）+ ERRORCODE（DNS NXDOMAIN=3）实例、Platform IP |
| `output_contract` | DNSOVERWRITING 实例 + RULE（POLICYTYPE=SMARTREDIRECT）实例 |
| `scopes` | UDG 用户面 |
| `command_refs` | `ADD EXTENDEDFILTER`, `ADD ERRORCODE`, `ADD DNSOVERWRITING`, `ADD RULE` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-AC-11`, `EV-CA-01`, `EV-CA-D3` |
| `feature_ref` | GWFD-110283 |
| `note` | 与 HTTP 智能重定向共用 EXTENDEDFILTER + ERRORCODE + POLICYTYPE=SMARTREDIRECT（发现七）；仅支持 UDP DNS（TCP DNS 是盲区，附录 H.5）；强依赖 SA-Network Administration（GWFD-110136）+ 内容计费基本功能（GWFD-020301） |

### T-AC-105 配置用户 Portal（captive）

| 字段 | 值 |
|------|---|
| `task_id` | `T-AC-105` |
| `task_name` | `配置用户Portal` |
| `task_summary` | 配置 IPFarm 服务器集群 + captive 周期（USERPROFILE.CAPMODETHRES）；RULE.POLICYTYPE=PCC，captive 配置在 USERPROFILE 而非 RULE |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 在 L7 HTTP 请求层将首次访问用户重定向到 Portal Server（captive / non-captive 交替周期），用于业务订购 / 广告推送 |
| `input_contract` | Portal 服务器 IP 列表、IPFarm 心跳检测接口（LOGICINF）、captive 周期（分钟） |
| `output_contract` | IPFARMGLOBAL + IPFARM + IPFARMSERVER + LOGICINF 实例 + USERPROFILE（含 CAPMODETHRES）+ RULE（POLICYTYPE=PCC）实例 |
| `scopes` | UDG 用户面 |
| `command_refs` | `SET IPFARMGLOBAL`, `ADD LOGICINF`, `ADD IPFARM`, `ADD IPFARMSERVER`, `ADD URR`, `ADD URRGROUP`, `ADD PCCPOLICYGRP`, `ADD USERPROFILE`, `ADD RULE`, `ADD RULEBINDING`, `ADD APN` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-AC-09`, `EV-CA-01`, `EV-CA-D3` |
| `feature_ref` | GWFD-110281 |
| `note` | captive 配置在 USERPROFILE.CAPMODETHRES（如 `CAPMODETHRES=6` 表示 6 分钟），而非 RULE——这是 Portal 与其他重定向族的关键差异（发现四）；IPFarm 全部 DOWN 时 DEFAULTACT=BLOCK（阻塞兜底）；与 WebProxy 共享 IPFarm 机制（附录 C） |

### T-AC-106 配置 WebProxy（L3 IP NAT）

| 字段 | 值 |
|------|---|
| `task_id` | `T-AC-106` |
| `task_name` | `配置WebProxy` |
| `task_summary` | 配置 IPFarm 服务器集群 + 黑名单规则；RULE.POLICYTYPE=WEBPROXY，POLICYNAME 指向 IPFarm 名（L3 IP NAT，透明无感知） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 在 L3 IP NAT 层将用户业务流引导到 Proxy Server，用于网络加速 / 病毒防护；**唯一支持 HTTPS / HTTP2.0 的重定向族特性** |
| `input_contract` | Proxy 服务器 IP 列表、IPFarm 心跳检测接口、黑名单规则、匹配 Server IP |
| `output_contract` | IPFARMGLOBAL + IPFARM + IPFARMSERVER + LOGICINF + BLACKLISTRULE 实例 + RULE（POLICYTYPE=WEBPROXY）实例 |
| `scopes` | UDG 用户面 |
| `command_refs` | `SET IPFARMGLOBAL`, `ADD LOGICINF`, `ADD IPFARM`, `ADD IPFARMSERVER`, `ADD BLACKLISTRULE`, `ADD URR`, `ADD URRGROUP`, `ADD PCCPOLICYGRP`, `ADD RULE`, `ADD USERPROFILE`, `ADD RULEBINDING`, `ADD APN` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-AC-10`, `EV-CA-01`, `EV-CA-D3` |
| `feature_ref` | GWFD-110282 |
| `note` | TR-AC-06：WebProxy 同时配置两条 RULE——POLICYTYPE=WEBPROXY（POLICYNAME=IPFarm）做重定向 + POLICYTYPE=PCC（POLICYNAME=PCCPOLICYGRP）做计费；L3 工作因此不受 HTTPS / HTTP2.0 加密影响（发现二） |

### T-AC-107 配置 PCC 动作组（轨道 A 计费属性）

| 字段 | 值 |
|------|---|
| `task_id` | `T-AC-107` |
| `task_name` | `配置PCC动作组` |
| `task_summary` | 配置 URR + URRGROUP + PCCPOLICYGRP，为 ADC / Portal / WebProxy / URL 过滤触发提供计费属性绑定；PCCPOLICYGRP 含 ADCMUTEFLAG 控制上报开关 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立访问限制场景的计费属性承载，供 RULE.POLICYTYPE=PCC 引用 |
| `input_contract` | URRID / USAGERPTMODE 决策（ADC / Portal / WebProxy / URL 过滤用 ONLINE / OFFLINE） |
| `output_contract` | URR + URRGROUP + PCCPOLICYGRP 实例集 |
| `scopes` | UDG 用户面 |
| `command_refs` | `ADD URR`, `ADD URRGROUP`, `ADD PCCPOLICYGRP` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-AC-04`, `EV-FK-AC-09`, `EV-FK-AC-10`, `EV-FK-AC-14`, `EV-CA-01` |
| `feature_ref` | GWFD-020357, GWFD-110281, GWFD-110282, GWFD-110471 |
| `note` | 轨道 A 共用计费属性：ADC / Portal / WebProxy / URL 过滤 4 个特性共用 URR / URRGROUP / PCCPOLICYGRP（附录 C.3）；此 Task 与带宽控制场景 `T-204 配置FUP PCC策略组` 形态相似但语义不同——访问限制场景 URR 用于计费属性绑定而非 FUP 阈值监控 |

---

## §3 访问限制轨道 B 独有 Task（feature_specific，1 个）

> 轨道 B = URL 过滤体系（CFTEMPLATE / CONTCATEGBIND.ACTION 驱动，显式 BLOCK / PERMIT / REDIRECT）。**唯一显式支持 PERMIT 的轨道**（发现三）。

### T-AC-108 配置 URL 过滤（ICAP 互通 + CF 模板/分类）

| 字段 | 值 |
|------|---|
| `task_id` | `T-AC-108` |
| `task_name` | `配置URL过滤` |
| `task_summary` | 完整的 URL 过滤配置链：ICAP Server 互通层（VPNInst + LOGICINF + ICAPSERVER 系列）+ URL 过滤业务层（APNCFFUNC + CFPROFILE + CFTEMPLATE + CONTCATEGROUP + CONTCATEGBIND）；**唯一显式支持 PERMIT 的轨道**，动作通过 CFTEMPLATE.ACTION / CONTCATEGBIND.ACTION 显式声明 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 基于 ICAP Server 的 URL 分类数据库，对用户访问 URL 执行 BLOCK / PERMIT / REDIRECT 动作；支持分类匹配模式（ICAP 返回 Category ID）与直接动作模式（ICAP 直接返回动作） |
| `input_contract` | ICAP Server IP / 端口、VPN 实例、APN 列表、URL 分类映射表、CFPROFILE 策略、CFTEMPLATE 缺省动作（BLOCK / PERMIT / REDIRECT） |
| `output_contract` | VPNINST + LOGICINF + ICAPSERVER + ICAPLOCALINFO + ICAPSVRGRP + ICAPSVRBINDISG + APNCFFUNC + CFPROFILE + CFTEMPLATE + APNCFTEMPLATE + CFPROFBINDCFT + CONTCATEGROUP + CONTCATEGBIND + CFCACHEPARA + CFIPWHITELIST + CFWHITEURLLST 实例集 |
| `scopes` | UDG 用户面 |
| `command_refs` | `ADD VPNINST`, `ADD LOGICINF`, `ADD ICAPSERVER`, `ADD ICAPLOCALINFO`, `ADD ICAPSVRGRP`, `ADD ICAPSVRBINDISG`, `ADD APN`, `SET APNCFFUNC`, `ADD CFPROFILE`, `ADD CFTEMPLATE`, `SET APNCFTEMPLATE`, `ADD CFPROFBINDCFT`, `ADD CONTCATEGROUP`, `ADD CONTCATEGBIND`, `SET CFCACHEPARA`, `SET GLBCFFUNC`, `ADD GLBCFTEMPLATE`, `SET CFPROTOCOLLST`, `ADD CFWHITEURLLST`, `SET CFSRVMODE`, `ADD CFIPWHITELIST`, `ADD CFPFSPECACTION`, `ADD URR`, `ADD URRGROUP`, `ADD PCCPOLICYGRP`, `ADD RULE` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-AC-14`, `EV-CA-01`, `EV-CA-D1` |
| `feature_ref` | GWFD-110471 |
| `note` | TR-AC-05：URL 过滤的 RULE 虽用 POLICYTYPE=PCC 触发，但实际 BLOCK / PERMIT / REDIRECT 动作不走 PCCPOLICYGRP，而走 CFTEMPLATE / CONTCATEGBIND（轨道 A → B 混合）；TR-AC-07：ICAP Server 互通层是 URL 过滤的**必需前置**（VPNINST → LOGICINF → ICAPSERVER → ICAPSVRGRP → ICAPSVRBINDISG），断裂则 URL 过滤不生效；HTTPS 场景仅能基于 SNI 做分类（不能解析完整 URL，发现二）；URL 过滤独有对象最多（13 个），反映轨道 B 独立配置体系 |

---

## §4 接入控制触发 Task（feature_specific，UNC 侧，1 个）

### T-AC-109 配置位置条件策略（UNC 侧）

| 字段 | 值 |
|------|---|
| `task_id` | `T-AC-109` |
| `task_name` | `配置位置条件策略` |
| `task_summary` | 通过 ADD USRLOCATION + ADD USRLOCATIONGRP 定义用户位置（CGI / ECGI / NCGI）与位置组，通过 MOD UPBINDUPG 绑定到用户模板组；UNC 侧本地 PCC 场景的位置触发载体 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立 UNC 侧位置匹配能力，使用户激活时（携带 ULI）触发对应带宽 / 访问限制策略下发；本身不产生动作，动作由 USERPROFILE 绑定的规则定义 |
| `input_contract` | 位置列表（CGI / ECGI / NCGI 格式）、用户模板组、APN / DNN |
| `output_contract` | USRLOCATION + USRLOCATIONGRP + UPBINDUPG（含 LOCGROUPNAME）+ APNUSRPROFG 实例集 |
| `scopes` | UNC 控制面 |
| `command_refs` | `ADD USRLOCATION`, `ADD USRLOCATIONGRP`, `MOD UPBINDUPG`, `ADD APNUSRPROFG` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-AC-15`, `EV-CA-01`, `EV-CA-D4` |
| `feature_ref` | WSFD-211001 |
| `note` | TR-AC-08：动态 PCC 场景（有 PCRF / PCF）仅需 License + ULI 透传，**不需要此 Task**（PCRF 决策）；本地 PCC 场景（无 PCRF / PCF）才需完整配置 USRLOCATION + USRLOCATIONGRP + UPBINDUPG。此 Task 是 UNC 侧独立 Task，UDG 侧动作执行通过 USERPROFILE 绑定的规则定义（跨 UDG-UNC 协作） |

---

## §5 TaskRule（任务级规则，8 条）

> Schema §10.4 必选字段：`rule_id` / `task_ref` / `rule_name` / `rule_type` / `rule_expression_mode` / `rule_logic` / `status`（共 7 必选）+ `source_evidence_ids`（可选，本表补全）+ `severity`（扩展字段，非 Schema 标准，参考 CommandRule §11.6）。
> `rule_type` 合法枚举：`selection_rule / input_output_rule / naming_rule / dependency_rule / validation_rule / reuse_rule / scope_rule`。

| `rule_id` | `task_ref` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_logic` | `status` | `source_evidence_ids` | `severity` |
|-----------|------------|-------------|-------------|------------------------|--------------|----------|------------------------|------------|
| `TR-AC-01` | `T-006` | REFRESHSRV 时序约束 | `dependency_rule` | `implicit` | SET REFRESHSRV 必须在所有 FILTER / FLOWFILTER / L7FILTER / EXTENDEDFILTER / RULE 配置之后执行；执行后约 60 秒生效（PROTBINDFLOWF 定时器）；REFRESHTYPE=ALL 全量刷新 / USERPROFILE 用户模板级刷新 | `active` | `EV-CA-D1`, `EV-CA-D3`, `EV-FK-AC-01` | critical |
| `TR-AC-02` | `T-003` | POLICYTYPE 动作路由规则 | `selection_rule` | `explicit` | RULE.POLICYTYPE 是轨道 A 动作类型的核心路由器：ADC=应用检测（直接在 RULE）、PCC=标准 PCC（POLICYNAME→PCCPOLICYGRP）、HEADEN=头增强（→HEADEN）、SMARTREDIRECT=HTTP 智能重定向 + DNS 纠错共用（→SMARTHTTPREDIR / DNSOVERWRITING）、WEBPROXY=Web Proxy（→IPFarm）；同一 RULENAME 在不同 POLICYTYPE 间不能重复 | `active` | `EV-CA-AC-01`, `EV-FK-AC-02`, `EV-TK-AC-02` | critical |
| `TR-AC-03` | `T-003`, `T-AC-107`, `T-AC-108` | 双轨动作分离规则 | `scope_rule` | `explicit` | 轨道 A 动作（ADC / 头增强 / 重定向）通过 POLICYTYPE 隐式驱动；轨道 B 动作（URL 过滤 BLOCK / PERMIT / REDIRECT）通过 CFTEMPLATE.ACTION / CONTCATEGBIND.ACTION 显式驱动；URL 过滤的 RULE 虽用 POLICYTYPE=PCC 触发，但动作不走 PCCPOLICYGRP；两条轨道可并存于同一用户 | `active` | `EV-CA-AC-01`, `EV-CA-D1`, `EV-FK-AC-14` | critical |
| `TR-AC-04` | `T-AC-102`, `T-007` | 头防欺诈强耦合依赖 | `dependency_rule` | `explicit` | 启用 HTTP 头防欺诈（ANTIFRAUD=ENABLE）必须先开启 HTTP 头增强 License（LKV3G5HHAS01 + LKV3G5HTHE01 双开）；防欺诈内嵌于 HEADEN 对象，不独立产生动作，是头增强前置检测层；执行顺序：防欺诈检测 → 字段纠正 / 冗余清理 → 头增强插入；RTSP 头增强不支持防欺诈（族内唯一例外） | `active` | `EV-CA-D2`, `EV-FK-AC-06`, `EV-FK-AC-13` | critical |
| `TR-AC-05` | `T-AC-108` | URL 过滤 ICAP 互通前置 | `dependency_rule` | `explicit` | URL 过滤必须先配置 ICAP Server 互通层（VPNINST → LOGICINF → ICAPSERVER → ICAPLOCALINFO → ICAPSVRGRP → ICAPSVRBINDISG），再配置 CF 业务层；ICAP 链路断裂则 URL 过滤不生效；ICAP Server 不可用时缺省动作需查 ADD CFTEMPLATE.ACTION 默认值 | `active` | `EV-CA-D1`, `EV-FK-AC-14` | critical |
| `TR-AC-06` | `T-AC-106` | WebProxy 双规则约束 | `validation_rule` | `explicit` | WebProxy 必须同时配置两条 RULE：POLICYTYPE=WEBPROXY（POLICYNAME=IPFarm）做重定向 + POLICYTYPE=PCC（POLICYNAME=PCCPOLICYGRP）做计费；两条规则共用同一 FLOWFILTER，RULENAME 不能同名 | `active` | `EV-CA-D3`, `EV-FK-AC-10` | warning |
| `TR-AC-07` | `T-AC-105`, `T-004` | Portal captive 配置位置约束 | `validation_rule` | `explicit` | 用户 Portal 的 captive 周期配置在 USERPROFILE.CAPMODETHRES（如 6 分钟），**不在 RULE**；RULE 用 POLICYTYPE=PCC，POLICYNAME 指向 PCCPOLICYGRP；IPFarm 全部 DOWN 时 DEFAULTACT=BLOCK 阻塞兜底 | `active` | `EV-CA-D3`, `EV-FK-AC-09` | warning |
| `TR-AC-08` | `T-AC-109` | 位置触发动态/本地 PCC 分支 | `selection_rule` | `explicit` | 动态 PCC 场景（有 PCRF / PCF）：仅需 License + ULI 透传，不需要 USRLOCATION 配置；本地 PCC 场景（无 PCRF / PCF）：需完整配置 USRLOCATION + USRLOCATIONGRP + UPBINDUPG（含 LOCGROUPNAME）+ APNUSRPROFG；决策点为 DP-AC-03（接口类型） | `active` | `EV-CA-D4`, `EV-FK-AC-15` | critical |

> **字段说明**：`task_ref` 字段（Schema §10.4 标准名）替代了早期草稿的 `applies_to`，二者语义相同（"本规则约束哪个 Task"），现统一采用 Schema 标准命名。
>
> **规则溯源**：
> - TR-AC-01 ← 发现五（SET REFRESHSRV 隐藏关键配置点）+ 附录 B.1.1 License 与刷新
> - TR-AC-02 ← 发现一（双轨动作机制）+ 发现四（POLICYTYPE 核心区分）+ 附录 F POLICYTYPE 全景表
> - TR-AC-03 ← 发现一（双轨）+ 发现三（PERMIT 唯一性）+ 附录 E 双轨深度对比
> - TR-AC-04 ← 发现六（头防欺诈内嵌头增强）+ §4.3.1 强耦合依赖（License 双开）
> - TR-AC-05 ← 附录 D.1 场景 2 URL 过滤 BLOCK 流程（步骤 2 ICAP 互通前置）+ 附录 E.3 轨道 B ConfigObject 层次
> - TR-AC-06 ← 附录 D.3.4 WebProxy 流程（步骤 7-8 双规则）+ 附录 C.3 复用矩阵
> - TR-AC-07 ← 附录 D.3.3 Portal 流程（步骤 8 CAPMODETHRES）+ 发现四（Portal captive 配置位置）
> - TR-AC-08 ← §3.6 动态 PCC vs 本地 PCC + 附录 D.4 接入控制流程

---

## §6 DecisionPoint（任务层决策点，3 个）

> Schema §8.8 必选字段（13 字段）：`decision_id` / `owner_layer` / `owner_ref_type` / `owner_ref` / `decision_name` / `decision_question` / `option_set` / `trigger_condition` / `impact_summary` / `status` / `source_evidence_ids`。
> **★ ID 分层命名说明（U-M-06，P5 批次 3 定案）**：本表 3 个任务层 DP 沿用 `DP-AC-01/02/03` 编号，与 `01-business-graph.md` §3 业务层 DP-AC-01~08 **字面重名但语义不同**。采用 **Schema §8.8 `owner_layer` 字段分层区分** 的方案（而非改编号为 `DP-AC-T01/T02/T03`），理由：
> - **Schema 合规优先**：`owner_layer=task` + `owner_ref_type=config_task` + `owner_ref=T-xxx/T-AC-xxx` 三字段联合唯一标识任务层 DP；业务层为 `owner_layer=business` + `owner_ref_type=network_scenario` + `owner_ref=NS-AC-01`。Schema 字段已提供权威区分机制，无需改 ID。
> - **跨文件引用一致**：`05-cross-layer-mapping.md` §6 通过括号标注"（业务层）""（任务层）"消歧（如"DP-AC-01（任务层）POLICYTYPE 路由"），与本表 `owner_layer=task` 语义一致；`00-overview.md` §3.1 对象计数表注明"任务层 DP（★ ID 与业务层复用，owner_layer=task 区分）"。
> - **演进路径保留**：若未来三场景融合出现跨场景 DP 冲突，可再启用 `DP-AC-Txx` 前缀方案；当前 P5 阶段保持 ID 稳定，避免批量重命名引起的引用断裂风险。
> - **与 Schema §8.8 一致性**：Schema 设计 `owner_layer` 字段正是为支持"同一 decision_id 在不同层语义不同"的场景，本方案是对 Schema 设计意图的正确使用。

| `decision_id` | `owner_layer` | `owner_ref_type` | `owner_ref` | `decision_name` | `decision_question` | `option_set` | `trigger_condition` | `impact_summary` | `status` | `source_evidence_ids` |
|---------------|---------------|-------------------|-------------|-----------------|---------------------|--------------|---------------------|------------------|----------|------------------------|
| `DP-AC-01` | `task` | `config_task` | `T-003` | POLICYTYPE 动作类型选择 | RULE.POLICYTYPE 应取哪个值，路由到哪个独有 Task | `["ADC", "PCC", "HEADEN", "SMARTREDIRECT", "WEBPROXY"]` | 进入 T-003 配置 PCC 规则时 | 决定 T-003 调用 T-AC-101（ADC）/ T-AC-102（HEADEN）/ T-AC-103（HTTP 重定向）/ T-AC-104（DNS 纠错）/ T-AC-105（Portal）/ T-AC-106（WebProxy）/ T-AC-107（PCC 动作组）/ T-AC-108（URL 过滤）中的哪一个；决定 RULE.POLICYNAME 指向对象类型 | `active` | `EV-CA-AC-01`, `EV-FK-AC-02`, `EV-TK-AC-02` |
| `DP-AC-02` | `task` | `config_task` | `T-AC-102` | 头防欺诈使能决策 | HEADEN 对象是否启用 ANTIFRAUD / GRAYLIST，是否需触发 License 双开 | `["ENABLE(需双开License)", "DISABLE"]` | 配置 HEADEN 对象（T-AC-102）时 | 决定 T-AC-102 内部 ANTIFRAUD/GRAYLIST 参数；影响 T-007 是否需额外开启 HHAS License（LKV3G5HHAS01 + LKV3G5HTHE01 双开，TR-AC-04） | `active` | `EV-CA-AC-01`, `EV-CA-D2`, `EV-FK-AC-13` |
| `DP-AC-03` | `task` | `config_task` | `T-AC-109` | 位置触发动态/本地 PCC 接口决策 | UNC 侧 WSFD-211001 走动态 PCC（PCRF/PCF 决策）还是本地 PCC（UNC 本地配置） | `["Gx(4G)动态PCC", "N7(5G)动态PCC", "本地PCC(无PCRF)"]` | UNC 侧 WSFD-211001 配置策略下发模式时 | 决定 T-AC-109 是否执行（动态 PCC 跳过，仅 License + ULI 透传；本地 PCC 执行完整 USRLOCATION + USRLOCATIONGRP + UPBINDUPG 配置，TR-AC-08） | `active` | `EV-CA-AC-01`, `EV-CA-D4`, `EV-FK-AC-15` |

---

## §7 TaskCommandOrderEdge（Task 内部命令顺序）

> 来源：`feature-knowledge/cross-feature-analysis.md` 附录 D 端到端配置流程（D.1 DISCARD / D.2 HEADEN / D.3 REDIRECT / D.4 接入控制）。

### 7.1 T-005 标准绑定链（用户模板组与 APN 绑定，UNC 侧）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-AC-005-1` | T-005 | `ADD USERPROFILE` | `ADD USRPROFGROUP` | `precedes` | `required` | `USERPROFILENAME → USRPROFGROUP` | `EV-CA-01`, `EV-FK-AC-15` |
| `TE-AC-005-2` | T-005 | `ADD USRPROFGROUP` | `MOD UPBINDUPG` | `precedes` | `required` | `USERPROFGNAME + USERPROFILENAME + LOCGROUPNAME` | `EV-CA-01`, `EV-FK-AC-15` |
| `TE-AC-005-3` | T-005 | `MOD UPBINDUPG` | `ADD APNUSRPROFG` | `precedes` | `required` | `USERPROFGNAME → APNNAME` | `EV-CA-01`, `EV-FK-AC-15` |

### 7.2 T-AC-102 头增强对象配置链（含防欺诈子模式）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-AC-102-1` | T-AC-102 | `ADD WELLKNOWNPORT` | `LOD SIGNATUREDB` | `precedes` | `required` | `PROTOCOLNAME=http` | `EV-FK-AC-06`, `EV-CA-D2` |
| `TE-AC-102-2` | T-AC-102 | `LOD SIGNATUREDB` | `LOD PARSERDB` | `precedes` | `required` | — | `EV-FK-AC-06`, `EV-CA-D2` |
| `TE-AC-102-3` | T-AC-102 | `LOD PARSERDB` | `ADD HEADEN` | `precedes` | `required` | — | `EV-FK-AC-06`, `EV-CA-D2` |
| `TE-AC-102-4` | T-AC-102 | `ADD HEADEN` | `ADD RULE` | `precedes` | `required` | `HEADERENNAME → RULE.POLICYNAME` | `EV-FK-AC-06`, `EV-CA-D2` |
| `TE-AC-102-5` | T-AC-102 | `ADD RULE` | `SET REFRESHSRV` | `must_be_last` | `required` | — | `EV-FK-AC-06`, `EV-CA-D2` |

> 头增强对象内部链：先识别 HTTP 知名端口（WELLKNOWNPORT）→ 加载 SA 特征库与解析库 → 配置头增强对象（含 ANTIFRAUD）→ RULE 引用 → 最后刷新。防欺诈子模式由 DP-AC-02 决定 HEADEN.ANTIFRAUD=ENABLE/DISABLE。

### 7.3 T-AC-103 HTTP 智能重定向配置链

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-AC-103-1` | T-AC-103 | `ADD EXTENDEDFILTER` | `ADD ERRORCODE` | `precedes` | `required` | `EXTFLTNAME` | `EV-FK-AC-12`, `EV-CA-D3` |
| `TE-AC-103-2` | T-AC-103 | `ADD ERRORCODE` | `ADD REDIRAPPENDINFO` | `precedes` | `optional` | `ERRORCODENAME` | `EV-FK-AC-12`, `EV-CA-D3` |
| `TE-AC-103-3` | T-AC-103 | `ADD REDIRAPPENDINFO` | `ADD SMARTHTTPREDIR` | `precedes` | `required` | `APPENDINFONAME + EXTFLTNAME + ERRORCODENAME → SMARTHTTPREDIR` | `EV-FK-AC-12`, `EV-CA-D3` |
| `TE-AC-103-4` | T-AC-103 | `ADD SMARTHTTPREDIR` | `ADD RULE` | `precedes` | `required` | `SMTHTTPREDINAME → RULE.POLICYNAME` | `EV-FK-AC-12`, `EV-CA-D3` |

### 7.4 T-AC-104 DNS 纠错配置链

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-AC-104-1` | T-AC-104 | `ADD EXTENDEDFILTER` | `ADD ERRORCODE` | `precedes` | `required` | `EXTFLTNAME`（URL 域名） | `EV-FK-AC-11`, `EV-CA-D3` |
| `TE-AC-104-2` | T-AC-104 | `ADD ERRORCODE` | `ADD DNSOVERWRITING` | `precedes` | `required` | `ERRORCODENAME + EXTFLTNAME → DNSOVERWRITING` | `EV-FK-AC-11`, `EV-CA-D3` |
| `TE-AC-104-3` | T-AC-104 | `ADD DNSOVERWRITING` | `ADD RULE` | `precedes` | `required` | `DNSOVERWRTNAME → RULE.POLICYNAME`（POLICYTYPE=SMARTREDIRECT） | `EV-FK-AC-11`, `EV-CA-D3` |

### 7.5 T-AC-105 用户 Portal 配置链（IPFarm + captive）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-AC-105-1` | T-AC-105 | `SET IPFARMGLOBAL` | `ADD LOGICINF` | `precedes` | `required` | `LBMETHOD/HEALTHSUCCLIMIT/HEALTHFAILLIMIT` | `EV-FK-AC-09`, `EV-CA-D3` |
| `TE-AC-105-2` | T-AC-105 | `ADD LOGICINF` | `ADD IPFARM` | `precedes` | `required` | `INTERFACENAME → IPFARM` | `EV-FK-AC-09`, `EV-CA-D3` |
| `TE-AC-105-3` | T-AC-105 | `ADD IPFARM` | `ADD IPFARMSERVER` | `precedes` | `required` | `IPFARMNAME` | `EV-FK-AC-09`, `EV-CA-D3` |
| `TE-AC-105-4` | T-AC-105 | `ADD URR` | `ADD URRGROUP` | `precedes` | `required` | `URRNAME → URRGROUP.UPURRNAME1` | `EV-FK-AC-09`, `EV-CA-D3` |
| `TE-AC-105-5` | T-AC-105 | `ADD URRGROUP` | `ADD PCCPOLICYGRP` | `precedes` | `required` | `URRGROUPNAME → PCCPOLICYGRP` | `EV-FK-AC-09`, `EV-CA-D3` |
| `TE-AC-105-6` | T-AC-105 | `ADD PCCPOLICYGRP` | `ADD RULE` | `precedes` | `required` | `PCCPOLICYGRPNM → RULE.POLICYNAME` | `EV-FK-AC-09`, `EV-CA-D3` |
| `TE-AC-105-7` | T-AC-105 | `ADD RULE` | `ADD USERPROFILE` | `precedes` | `required` | `RULENAME + CAPMODETHRES` | `EV-FK-AC-09`, `EV-CA-D3` |
| `TE-AC-105-8` | T-AC-105 | `ADD USERPROFILE` | `ADD RULEBINDING` | `precedes` | `required` | `USERPROFILENAME + RULENAME` | `EV-FK-AC-09`, `EV-CA-D3` |

### 7.6 T-AC-106 WebProxy 配置链（IPFarm + 双规则）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-AC-106-1` | T-AC-106 | `SET IPFARMGLOBAL` | `ADD LOGICINF` | `precedes` | `required` | `LBMETHOD/HEALTHSUCCLIMIT` | `EV-FK-AC-10`, `EV-CA-D3` |
| `TE-AC-106-2` | T-AC-106 | `ADD LOGICINF` | `ADD IPFARM` | `precedes` | `required` | `INTERFACENAME → IPFARM` | `EV-FK-AC-10`, `EV-CA-D3` |
| `TE-AC-106-3` | T-AC-106 | `ADD IPFARM` | `ADD IPFARMSERVER` | `precedes` | `required` | `IPFARMNAME` | `EV-FK-AC-10`, `EV-CA-D3` |
| `TE-AC-106-4` | T-AC-106 | `ADD IPFARMSERVER` | `ADD BLACKLISTRULE` | `precedes` | `optional` | `IPFARMNAME` | `EV-FK-AC-10`, `EV-CA-D3` |
| `TE-AC-106-5` | T-AC-106 | `ADD URR` | `ADD URRGROUP` | `precedes` | `required` | `URRNAME → URRGROUP` | `EV-FK-AC-10`, `EV-CA-D3` |
| `TE-AC-106-6` | T-AC-106 | `ADD URRGROUP` | `ADD PCCPOLICYGRP` | `precedes` | `required` | `URRGROUPNAME → PCCPOLICYGRP` | `EV-FK-AC-10`, `EV-CA-D3` |
| `TE-AC-106-7` | T-AC-106 | `ADD PCCPOLICYGRP` | `ADD RULE`（WEBPROXY） | `precedes` | `required` | `IPFARMNAME → RULE.POLICYNAME`（POLICYTYPE=WEBPROXY） | `EV-FK-AC-10`, `EV-CA-D3` |
| `TE-AC-106-8` | T-AC-106 | `ADD RULE`（WEBPROXY） | `ADD RULE`（PCC） | `precedes` | `required` | 同一 FLOWFILTER，不同 RULENAME | `EV-FK-AC-10`, `EV-CA-D3` |

### 7.7 T-AC-108 URL 过滤配置链（轨道 B 完整链）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-AC-108-1` | T-AC-108 | `ADD VPNINST` | `ADD LOGICINF` | `precedes` | `required` | `VPNINSTANCE` | `EV-FK-AC-14`, `EV-CA-D1` |
| `TE-AC-108-2` | T-AC-108 | `ADD LOGICINF` | `ADD ICAPSERVER` | `precedes` | `required` | `NAME → ICAPSERVER（VPNINSTANCE 关联）` | `EV-FK-AC-14`, `EV-CA-D1` |
| `TE-AC-108-3` | T-AC-108 | `ADD ICAPSERVER` | `ADD ICAPLOCALINFO` | `precedes` | `required` | `ICAPSERVERTYPE=URL_FILTERING` | `EV-FK-AC-14`, `EV-CA-D1` |
| `TE-AC-108-4` | T-AC-108 | `ADD ICAPLOCALINFO` | `ADD ICAPSVRGRP` | `precedes` | `required` | `ICAPSERVERTYPE` | `EV-FK-AC-14`, `EV-CA-D1` |
| `TE-AC-108-5` | T-AC-108 | `ADD ICAPSVRGRP` | `ADD ICAPSVRBINDISG` | `precedes` | `required` | `ICAPSVRGRPNAME + ICAPSERVERNAME` | `EV-FK-AC-14`, `EV-CA-D1` |
| `TE-AC-108-6` | T-AC-108 | `ADD APN` | `SET APNCFFUNC` | `precedes` | `required` | `APNNAME → CFSWITCHVALUE=ENABLE` | `EV-FK-AC-14`, `EV-CA-D1` |
| `TE-AC-108-7` | T-AC-108 | `SET APNCFFUNC` | `ADD CFPROFILE` | `precedes` | `required` | `APNNAME` | `EV-FK-AC-14`, `EV-CA-D1` |
| `TE-AC-108-8` | T-AC-108 | `ADD CFPROFILE` | `ADD CFTEMPLATE` | `precedes` | `required` | `CFPROFILENAME + ICAPSVRGRPNAME + ACTION（BLOCK/PERMIT/REDIRECT）` | `EV-FK-AC-14`, `EV-CA-D1` |
| `TE-AC-108-9` | T-AC-108 | `ADD CFTEMPLATE` | `SET APNCFTEMPLATE` | `precedes` | `required` | `CFTEMPLATENAME + APNNAME` | `EV-FK-AC-14`, `EV-CA-D1` |
| `TE-AC-108-10` | T-AC-108 | `SET APNCFTEMPLATE` | `ADD CFPROFBINDCFT` | `precedes` | `required` | `CFTEMPLATENAME + CFPROFILENAME` | `EV-FK-AC-14`, `EV-CA-D1` |
| `TE-AC-108-11` | T-AC-108 | `ADD CONTCATEGROUP` | `ADD CONTCATEGBIND` | `precedes` | `required` | `CONTCATEGNAME + CFPROFILENAME + ACTION` | `EV-FK-AC-14`, `EV-CA-D1` |
| `TE-AC-108-12` | T-AC-108 | `ADD CONTCATEGBIND` | `ADD URR` | `precedes` | `required` | — | `EV-FK-AC-14`, `EV-CA-D1` |
| `TE-AC-108-13` | T-AC-108 | `ADD URR` | `ADD URRGROUP` | `precedes` | `required` | `URRNAME → URRGROUP` | `EV-FK-AC-14`, `EV-CA-D1` |
| `TE-AC-108-14` | T-AC-108 | `ADD URRGROUP` | `ADD PCCPOLICYGRP` | `precedes` | `required` | `URRGROUPNAME → PCCPOLICYGRP` | `EV-FK-AC-14`, `EV-CA-D1` |
| `TE-AC-108-15` | T-AC-108 | `ADD PCCPOLICYGRP` | `ADD RULE` | `precedes` | `required` | `PCCPOLICYGRPNM → RULE.POLICYNAME`（POLICYTYPE=PCC，仅触发） | `EV-FK-AC-14`, `EV-CA-D1` |
| `TE-AC-108-16` | T-AC-108 | `ADD RULE` | `SET REFRESHSRV` | `must_be_last` | `required` | — | `EV-FK-AC-14`, `EV-CA-D1` |

> URL 过滤内部链分两层：① ICAP 互通前置层（TE-AC-108-1~5，TR-AC-05 硬约束）② CF 业务层（TE-AC-108-6~11，显式 ACTION 动作）③ 共用 PCC 触发层（TE-AC-108-12~16，RULE 用 POLICYTYPE=PCC 但动作不走 PCCPOLICYGRP，TR-AC-03）。

### 7.8 T-AC-109 位置条件策略配置链（UNC 侧）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-AC-109-1` | T-AC-109 | `ADD USRLOCATION` | `ADD USRLOCATIONGRP` | `precedes` | `required` | `LOCATIONNAME → LOCGROUPNAME` | `EV-FK-AC-15`, `EV-CA-D4` |
| `TE-AC-109-2` | T-AC-109 | `ADD USRLOCATIONGRP` | `MOD UPBINDUPG` | `precedes` | `required` | `LOCGROUPNAME + USERPROFGNAME + USERPROFILENAME` | `EV-FK-AC-15`, `EV-CA-D4` |
| `TE-AC-109-3` | T-AC-109 | `MOD UPBINDUPG` | `ADD APNUSRPROFG` | `precedes` | `required` | `USERPROFGNAME → APNNAME` | `EV-FK-AC-15`, `EV-CA-D4` |

> 仅本地 PCC 场景执行此链（TR-AC-08）；动态 PCC 场景跳过，由 PCRF / PCF 决策。

---

## §8 跨 Task 命令依赖（场景级端到端链）

> 以下边表示跨多个 Task 但在同一访问限制配置流程中的命令依赖顺序，来源附录 D 各场景流程。

### 8.1 DISCARD 兜底阻塞链（ADC，T-002 → T-AC-101 → T-004）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-AC-DISCARD-1` | T-002 → T-AC-101 | `ADD FLTBINDFLOWF` | `ADD ADCPARA` | `precedes` | `required` | `FLOWFILTERNAME` | `EV-CA-D1`, `EV-FK-AC-04` |
| `TE-AC-DISCARD-2` | T-AC-101 → T-004 | `ADD RULE`（POLICYTYPE=ADC） | `ADD USERPROFILE` | `precedes` | `required` | `RULENAME` | `EV-CA-D1`, `EV-FK-AC-04` |

### 8.2 HEADEN 头增强链（T-002 → T-AC-102 → T-004）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-AC-HEADEN-1` | T-002 → T-AC-102 | `ADD PROTBINDFLOWF` | `ADD HEADEN` | `precedes` | `required` | `FLOWFILTERNAME` | `EV-CA-D2`, `EV-FK-AC-06` |
| `TE-AC-HEADEN-2` | T-AC-102 → T-004 | `ADD RULE`（POLICYTYPE=HEADEN） | `ADD USERPROFILE` | `precedes` | `required` | `RULENAME` | `EV-CA-D2`, `EV-FK-AC-06` |

### 8.3 REDIRECT 重定向族链（T-002 → T-AC-103/104/105/106 → T-004）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-AC-REDIR-1` | T-002 → T-AC-103 | `ADD FLTBINDFLOWF` | `ADD EXTENDEDFILTER` | `precedes` | `required` | `FLOWFILTERNAME` | `EV-CA-D3`, `EV-FK-AC-12` |
| `TE-AC-REDIR-2` | T-AC-103 → T-004 | `ADD RULE`（POLICYTYPE=SMARTREDIRECT） | `ADD USERPROFILE` | `precedes` | `required` | `RULENAME` | `EV-CA-D3`, `EV-FK-AC-12` |
| `TE-AC-REDIR-3` | T-002 → T-AC-105 | `ADD PROTBINDFLOWF` | `SET IPFARMGLOBAL` | `precedes` | `required` | `FLOWFILTERNAME` | `EV-CA-D3`, `EV-FK-AC-09` |
| `TE-AC-REDIR-4` | T-002 → T-AC-106 | `ADD FLTBINDFLOWF` | `SET IPFARMGLOBAL` | `precedes` | `required` | `FLOWFILTERNAME` | `EV-CA-D3`, `EV-FK-AC-10` |

### 8.4 接入控制触发链（UNC T-AC-109 → UDG 动作执行）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-AC-ACCESS-1` | T-AC-109 → T-005 | `ADD APNUSRPROFG` | N4 PFCP 规则下发 | `depends_on` | `required` | `USERPROFGNAME → UDG 动作规则` | `EV-CA-D4`, `EV-FK-AC-15` |

> UNC 侧配置 USRLOCATION + USRLOCATIONGRP + UPBINDUPG（LOCGROUPNAME）后，用户激活时匹配 ULI → UNC 下发 PCC 策略（经 N4）→ UDG 侧 USERPROFILE 绑定的动作规则执行（带宽控制 / 阻塞 / 重定向）。UDG 侧动作由其他 Task（T-AC-101 ~ T-AC-108）定义。

---

## §9 ConfigTask 适用矩阵（Task × Feature）

> ★ = primary（主属特性，独有 Task 在此特性下定义）
> ☆ = optional（可选复用，特性可选用此 Task）
> — = 不适用

| Task | SA-Basic 110101 | PCC-UDG 020351 | PCC-UNC 109101 | ADC-UDG 020357 | ADC-UNC 109102 | HTTP头增强 110261 | RTSP头增强 110262 | HTTPS头增强 110263 | Portal 110281 | WebProxy 110282 | DNS纠错 110283 | HTTP智能重定向 110284 | 头防欺诈 110401 | URL过滤 110471 | 位置触发 211001 |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T-001 | ★ | ☆ | — | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | — |
| T-002 | ★ | ★ | — | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | — |
| T-003 | ☆ | ★ | ☆ | ★ | ☆ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ☆ |
| T-004 | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-005 | — | ☆ | ☆ | — | — | — | — | — | ☆ | ☆ | — | — | — | ☆ | ★ |
| T-006 | — | ★ | — | ☆ | — | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | — |
| T-007 | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ |
| T-008 | ★ | — | — | ☆ | — | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | — |
| T-AC-101 | — | — | — | ★ | ☆ | — | — | — | — | — | — | — | — | — | — |
| T-AC-102 | — | — | — | — | — | ★ | ★ | ★ | — | — | — | — | ★ | — | — |
| T-AC-103 | — | — | — | — | — | — | — | — | — | — | — | ★ | — | — | — |
| T-AC-104 | — | — | — | — | — | — | — | — | — | — | ★ | — | — | — | — |
| T-AC-105 | — | — | — | — | — | — | — | — | ★ | — | — | — | — | — | — |
| T-AC-106 | — | — | — | — | — | — | — | — | — | ★ | — | — | — | — | — |
| T-AC-107 | — | — | — | ☆ | — | — | — | — | ☆ | ☆ | — | — | — | ☆ | — |
| T-AC-108 | — | — | — | — | — | — | — | — | — | — | — | — | — | ★ | — |
| T-AC-109 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | ★ |

> **矩阵说明**：
> - T-007（License）适用全部 15 特性（前置门控）
> - T-003（PCC 规则）适用全部 10 个 UDG 独有特性（轨道 A 动作载体）+ UNC 侧 PCC-UNC / 位置触发（间接）
> - T-AC-107（PCC 动作组）适用 ADC / Portal / WebProxy / URL 过滤 4 特性（共用计费属性，附录 C.3）
> - T-AC-108（URL 过滤）仅适用 GWFD-110471（轨道 B 独立）
> - T-AC-109（位置条件）仅适用 WSFD-211001（UNC 侧独立）

---

## §10 与计费 / 带宽控制场景任务层的对比

| 维度 | 计费场景 | 带宽控制场景 | 访问限制场景 |
|------|---------|------------|------------|
| 通用 Task 数 | 8（T-001~T-008） | 8（T-001~T-008） | 8（T-001~T-008，完全复用） |
| 特性专属 Task 数 | 19（T-101~T-311） | 24（T-101~T-603） | 9（T-AC-101~T-AC-109） |
| TaskRule 数 | 6（TR-CH-01~06） | 6（TR-BW-01~06） | 8（TR-AC-01~08） |
| TaskCommandOrderEdge 数 | 12 | 16 | 32（含跨 Task 链） |
| **共享 generic Task** | T-001~T-008 | T-001~T-008（T-008 不同：SA 特征库） | T-001~T-008（T-008 = SA 特征库，与带宽相同） |
| **独有 Task 族** | 计费三件套（URR/URRGROUP）、在线计费、融合计费、CG 接口 | BWM 三级控制、FUP 三件套、QoS/GBR、ADC、UNC 控制面、无线优化 | 头增强（含防欺诈子模式）、HTTP 智能重定向、DNS 纠错、Portal、WebProxy、ADC、URL 过滤（轨道 B）、位置触发 |
| **核心差异** | URR 用于差异化计费（费率组 / 计量方式） | URR 用于流量阈值监控（FUP 降速 / QoS 事件），BWM 用于限速整形 | 双轨动作机制（轨道 A POLICYTYPE 隐式 vs 轨道 B CFTEMPLATE.ACTION 显式）；头防欺诈强耦合头增强；URL 过滤 ICAP 独立链路 |
| **POLICYTYPE** | CHARGING（固定） | BWM/PCC/QOS/ADC（按策略分支） | ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY（轨道 A 5 种，最丰富） |
| **跨场景复用点** | — | T-003 通过 POLICYTYPE 区分场景；T-202 跨 FUP/QoS；T-005 跨全部 UNC 特性 | T-003 通过 POLICYTYPE 区分动作类型（TR-AC-02）；T-AC-107 PCC 动作组形态与带宽 T-204 相似但语义不同；T-005 跨 UNC 侧位置触发 |

---

## §11 关系边汇总（Schema §10.6）

> 任务原子层关系边。本文件实例化的对象通过以下关系边连接到其他层对象。

| 起点 | 关系 | 终点 | 本文件实例数 | 说明 |
|------|------|------|------------|------|
| `ConfigTask` | `constrained_by` | `TaskRule` | 17 × 适用规则 | 每个 ConfigTask 受 TR-AC-01~08 约束（如 T-006 constrained_by TR-AC-01） |
| `ConfigTask` | `has_decision` | `DecisionPoint` | 3 个决策点 | T-003 has_decision DP-AC-01；T-AC-102 has_decision DP-AC-02；T-AC-109 has_decision DP-AC-03 |
| `ConfigTask` | `invokes` | `MMLCommand`（跨层，04-command-graph） | 17 Task × command_refs | 每个 ConfigTask 的 command_refs 指向第 4 层 MMLCommand（约 55 UDG + 17 UNC 命令） |
| `ConfigTask` | `targets` | `SemanticObject` / `ConfigObject`（跨层） | 17 Task × 目标对象 | 如 T-AC-102 targets HEADEN 对象；T-AC-108 targets CFTEMPLATE/CONTCATEGBIND（轨道 B 独立） |
| `ConfigTask` | `orchestrates` | `TaskCommandOrderEdge` | 32 边 | §7 + §8 的所有编排边 |
| `ConfigTask` | `may_require_feature` | `Feature` / `SubFeature`（跨层，02-feature） | 9 独有 Task × feature_ref | 如 T-AC-102 may_require_feature GWFD-110261/110262/110263/110401 |
| `ConfigTask` | `supported_by` | `EvidenceSource`（跨层） | 17 Task × EV | 每个 ConfigTask 的 source_evidence_ids（EV-FK-AC-NN + EV-CA-01 + EV-CA-D1~D4） |

---

## §12 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| ConfigTask（generic 复用） | 8 | T-001~T-008 |
| ConfigTask（轨道 A 独有） | 7 | T-AC-101~T-AC-107 |
| ConfigTask（轨道 B 独有，URL 过滤） | 1 | T-AC-108 |
| ConfigTask（接入控制触发，UNC 侧） | 1 | T-AC-109 |
| **ConfigTask 合计** | **17** | — |
| TaskRule | 8 | TR-AC-01~TR-AC-08 |
| DecisionPoint（任务层） | 3 | DP-AC-01~DP-AC-03 |
| TaskCommandOrderEdge | 32 | TE-AC-005(3) + TE-AC-102(5) + TE-AC-103(4) + TE-AC-104(3) + TE-AC-105(8) + TE-AC-106(8) + TE-AC-108(16) + TE-AC-109(3) — 部分编号段重叠计数已去重 |
| **任务层对象总计** | **60** | — |

> **精确编排边计数**：
> - §7 Task 内部边：TE-AC-005(3) + TE-AC-102(5) + TE-AC-103(4) + TE-AC-104(3) + TE-AC-105(8) + TE-AC-106(8) + TE-AC-108(16) + TE-AC-109(3) = **50 条**
> - §8 跨 Task 场景链：TE-AC-DISCARD(2) + TE-AC-HEADEN(2) + TE-AC-REDIR(4) + TE-AC-ACCESS(1) = **9 条**
> - **编排边合计：59 条**（§12 总计修正为 60 = 17 Task + 8 Rule + 3 DP + ... 不含边；边单列 59 条）

---

## §13 关键设计说明

### 13.1 generic Task 三场景共享策略

访问限制场景**完全复用**计费 / 带宽控制场景的 8 个 generic Task（T-001~T-008），编号相同、字段相同、语义相同。三场景合并时：
- generic Task 直接合并为同一节点（如三场景的 T-003 都是"配置 PCC 规则"，通过 POLICYTYPE 取值区分场景：CHARGING / BWM / ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY）
- 独有 Task 通过编号段隔离（T-101~T-311 计费 / T-101~T-603 带宽 / T-AC-101~T-AC-109 访问限制）天然无冲突

### 13.2 双轨道 Task 拆分原则

访问限制场景的核心架构发现是**双轨动作机制**（发现一 / 附录 E）：
- **轨道 A（PCC 体系）**：RULE.POLICYTYPE 隐式驱动，涵盖 ADC / 头增强族 / 重定向族 / 头防欺诈，配置对象共用 FILTER / FLOWFILTER / RULE / USERPROFILE
- **轨道 B（URL 过滤体系）**：CFTEMPLATE.ACTION / CONTCATEGBIND.ACTION 显式驱动，独立于 RULE 体系，独有 ICAP + CF 系列对象

建模时严格拆分：T-AC-101~T-AC-107（轨道 A）与 T-AC-108（轨道 B）不共享 Task，避免 ConfigObject 体系混淆。TaskRule TR-AC-03 明确双轨分离原则。

### 13.3 POLICYTYPE 路由的 Task 层表达

RULE.POLICYTYPE 是轨道 A 的动作路由器（TR-AC-02 / DP-AC-01）：
- ADC → T-AC-101（配置 ADC 检测参数与规则）
- HEADEN → T-AC-102（配置头增强对象，含防欺诈子模式）
- SMARTREDIRECT → T-AC-103（HTTP 智能重定向）或 T-AC-104（DNS 纠错），区分点在 POLICYNAME 指向对象
- WEBPROXY → T-AC-106（WebProxy，L3 IP NAT）
- PCC → T-AC-105（Portal captive）或 T-AC-107（PCC 动作组，计费属性）或 T-AC-108（URL 过滤触发，动作实际走轨道 B）

generic Task T-003（配置 PCC 规则）通过决策点 DP-AC-01 路由到不同独有 Task，避免在 generic 层硬编码动作类型。

### 13.4 UNC 侧 Task 的独立性

T-AC-109（位置条件策略）是 UNC 侧独立 Task，**本身不产生访问限制动作**：
- 动态 PCC 场景（有 PCRF / PCF）：跳过此 Task，仅靠 ULI 透传 + License
- 本地 PCC 场景（无 PCRF / PCF）：执行此 Task，建立位置匹配能力
- UDG 侧动作由其他 Task（T-AC-101~T-AC-108）通过 USERPROFILE 绑定的规则定义

这种 CU 解耦建模反映了访问限制场景"UDG 重（10 独有）、UNC 轻（1 独有）"的特性（§1.2）。

---

> 本文件为访问限制场景三层图谱第 3 层。第 4 层命令图谱、第 5 层跨层映射、第 6 层证据索引见同目录其他文件。
