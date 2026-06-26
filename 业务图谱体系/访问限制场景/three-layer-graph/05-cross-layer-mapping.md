# 访问限制场景三层图谱 · 第5层：跨层映射关系总表

> **文件定位**：`three-layer-graph/05-cross-layer-mapping.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §12 跨层映射（§12.1~§12.5）+ §13 禁止关系
> **作用**：汇总 CS↔Feature/Task、Feature↔Task、Task↔Command/Object/DP、DP 影响、BR/TR refined_by 的所有跨层边
> **合规要求**：严格避免 §13 禁止关系（CS→ConfigObject 直接绑定、Feature→MMLCommand 直接绑定、BusinessRule 直接写死参数等）
> **数据来源**：汇总已建好的 4 个文件（01-business / 02-feature / 03-task / 04-command），所有跨层边两端对象均为真实存在的实例

---

## 0. 跨层映射总览

| 跨层边类型 | 数量 | 方向 | 说明 |
|-----------|------|------|------|
| CS `uses_feature` | 30 | 业务层→特性层 | 9 方案 × 平均 3.3 特性（含 ADC 横切依赖 6 条；★ P5 批次 3 补 CS-AC-07 的 4 条 UNC 辅助特性边 U-H-02） |
| CS `uses_task`（方案闭包级） | 9 | 业务层→任务层 | 每方案一个主 Task 集合 |
| Feature `decomposes_to` ConfigTask | 19 | 特性层→任务层 | 19 Feature 的 Task 展开（5 核心特性显式 FTOE，其余通过 may_require_feature 关联；★ P5 批次 3 补 4 条 UNC 辅助特性 Task 映射） |
| ConfigTask `invokes` MMLCommand | ~68 | 任务层→命令层 | 17 Task 调用的 MML 命令集合（UDG 48 + UNC 20，★ P5 修正计数） |
| ConfigTask `targets` SemanticObject/ConfigObject | ~45 | 任务层→业务/命令层 | Task 操作的 SO/对象 |
| DP `selects` CS/Task | 9 | 业务层/任务层内 | 决策点选择方案或 Task |
| DP `sets_value_pattern` | 6 | 业务层→命令层 | 决策点设置参数模式（含 ★DP-AC-03 轨道选择→RULE.POLICYTYPE） |
| BR/TR `refined_by` FR/TR/CR | 8 | 跨层精化 | 高层规则被下层规则具体化 |

---

## §1. CS → Feature 映射（uses_feature，30条）

> 来源：`01-business-graph.md` §2.1~§2.9 + §9.2
> **★ P5 修复（U-M-07/F05）**：补 `source_evidence_ids` 列，每条 uses_feature 边溯源到 CS 的证据 + Feature 的特性证据（EV-FK-AC-NN 按 06 §0.1 序号映射）。
> **★ P5 批次 3 修复（U-H-02 跨文件同步）**：CS-AC-07 的 4 条 UNC 接入控制辅助特性边（WSFD-106003/105003/106005/105006）的 `source_evidence_ids` 从占位 `EV-FK-AC-15` 修正为独立 `EV-FK-AC-16~19`（与 `02` §1.9 实例化 + `06` §2.8 注册一致）。

| CS | uses_feature | Feature 角色 | `source_evidence_ids` |
|----|-------------|------------|----------------------|
| CS-AC-01 PCC 阻塞 | GWFD-020351（PCC UDG） | 核心：UDG 侧 PCC 规则体系（POLICYTYPE=PCC，DISCARD 兜底） | `EV-CA-AC-01`, `EV-FK-AC-02`, `EV-TK-AC-02` |
| CS-AC-01 | WSFD-109101（PCC UNC） | 基础：UNC 侧策略下发承载 | `EV-CA-AC-01`, `EV-FK-AC-03` |
| CS-AC-01 | GWFD-020357（ADC UDG） | 横切：L7 应用识别前置 + 兜底阻塞 | `EV-CA-AC-01`, `EV-FK-AC-04` |
| CS-AC-02 头增强 | GWFD-110261（HTTP 头增强） | 核心：HTTP 扩展字段插入 | `EV-CA-AC-01`, `EV-FK-AC-06` |
| CS-AC-02 | GWFD-110262（RTSP 头增强） | 可选：RTSP 扩展字段插入 | `EV-CA-AC-01`, `EV-FK-AC-07` |
| CS-AC-02 | GWFD-110263（HTTPS 头增强） | 可选：SSL Extension TLV 插入 | `EV-CA-AC-01`, `EV-FK-AC-08` |
| CS-AC-02 | GWFD-110401（HTTP 头防欺诈） | 可选：头增强前置检测（强耦合 110261） | `EV-CA-AC-01`, `EV-FK-AC-09` |
| CS-AC-02 | GWFD-020357（ADC UDG） | 横切：L7 解析前置 | `EV-CA-AC-01`, `EV-FK-AC-04` |
| CS-AC-03 HTTP 重定向 | GWFD-110284（HTTP 智能重定向） | 核心：L7 HTTP 响应改写（302） | `EV-CA-AC-01`, `EV-FK-AC-13` |
| CS-AC-03 | GWFD-020357（ADC UDG） | 横切：L7 解析前置 | `EV-CA-AC-01`, `EV-FK-AC-04` |
| CS-AC-03 | GWFD-110261（HTTP 头增强） | 可选：REDIRAPPENDINFO 携带 MSISDN/IMSI | `EV-CA-AC-01`, `EV-FK-AC-06` |
| CS-AC-04 DNS 重定向 | GWFD-110283（DNS 纠错） | 核心：DNS Overwriting（构造新 DNS 响应） | `EV-CA-AC-01`, `EV-FK-AC-12` |
| CS-AC-04 | GWFD-020357（ADC UDG） | 横切：DNS 解析前置 | `EV-CA-AC-01`, `EV-FK-AC-04` |
| CS-AC-05 Portal/WebProxy | GWFD-110281（用户 Portal） | 核心：Portal captive/non-captive 周期重定向（SMARTREDIRECT 体系） | `EV-CA-AC-01`, `EV-FK-AC-10` |
| CS-AC-05 | GWFD-110282（WebProxy） | 核心：L3 IP NAT 透明代理（WEBPROXY 独立体系，唯一支持 HTTPS/HTTP2.0） | `EV-CA-AC-01`, `EV-FK-AC-11` |
| CS-AC-05 | GWFD-020357（ADC UDG） | 横切：Portal 依赖 L7 解析（WebProxy 在 L3 不依赖） | `EV-CA-AC-01`, `EV-FK-AC-04` |
| CS-AC-06 URL 过滤（轨道 B） | GWFD-110471（URL 过滤） | 核心：ICAP + CFTEMPLATE/CONTCATEGBIND.ACTION 显式 BLOCK/PERMIT/REDIRECT | `EV-CA-AC-01`, `EV-FK-AC-14` |
| CS-AC-06 | GWFD-020357（ADC UDG） | 横切：URL 提取前置（HTTPS 仅 SNI） | `EV-CA-AC-01`, `EV-FK-AC-04` |
| CS-AC-07 接入控制 | WSFD-211001（基于初始接入位置的策略控制） | 核心：UNC 侧位置触发（CGI/ECGI/NCGI） | `EV-CA-AC-01`, `EV-FK-AC-15` |
| CS-AC-07 | WSFD-106003（用户接入控制 AMF，SAR） | 辅助：注册阶段服务区域限制（★ U-H-02 补，EV-FK-AC-16） | `EV-CA-AC-01`, `EV-FK-AC-16` |
| CS-AC-07 | WSFD-105003（区域漫游限制 AMF） | 辅助：漫游区域限制（★ U-H-02 补，EV-FK-AC-17） | `EV-CA-AC-01`, `EV-FK-AC-17` |
| CS-AC-07 | WSFD-106005（支持 ODB AMF） | 辅助：欠费禁用（★ U-H-02 补，EV-FK-AC-18） | `EV-CA-AC-01`, `EV-FK-AC-18` |
| CS-AC-07 | WSFD-105006（会话服务区域限制 SMF） | 辅助：会话阶段服务区域限制（★ U-H-02 补，EV-FK-AC-19） | `EV-CA-AC-01`, `EV-FK-AC-19` |
| CS-AC-08 配额耗尽重定向 | GWFD-020351（PCC UDG） | 核心：轨道 A 承载（RedirectInformation URL） | `EV-CA-AC-01`, `EV-FK-AC-02` |
| CS-AC-08 | WSFD-109101（PCC UNC） | 核心：UNC 侧 PCF 决策承载 | `EV-CA-AC-01`, `EV-FK-AC-03` |
| CS-AC-08 | GWFD-110284（HTTP 智能重定向） | 可选：充值页重定向机制 | `EV-CA-AC-01`, `EV-FK-AC-13` |
| CS-AC-09 区域引导重定向 | WSFD-211001（位置触发） | 核心：PRA/PLMN/服务区域感知 | `EV-CA-AC-01`, `EV-FK-AC-15` |
| CS-AC-09 | GWFD-110284（HTTP 智能重定向） | 核心：套餐订购页重定向机制 | `EV-CA-AC-01`, `EV-FK-AC-13` |
| CS-AC-09 | GWFD-110281（用户 Portal） | 可选：验证页 Portal captive 推送 | `EV-CA-AC-01`, `EV-FK-AC-10` |

> **去重统计**：共 30 条 uses_feature 边（★ P5 批次 3：26+4 UNC 辅助），覆盖 19 个 Feature（含 4 个三场景共享基础设施：GWFD-110101 SA-Basic / GWFD-020351 PCC-UDG / WSFD-109101 PCC-UNC / WSFD-109102 ADC-UNC；含 4 个 UNC 接入控制辅助特性 U-H-02 补：WSFD-106003/105003/106005/105006）。
> **ADC 横切依赖**：CS-AC-01~06 共 6 个方案依赖 GWFD-020357 作为 L7 解析前置；CS-AC-07 接入控制在 UNC 侧不依赖 ADC；CS-AC-08/09 重定向由 PCF 决策 + UPF 执行，ADC 为可选。
> **注**：GWFD-110101 SA-Basic 作为 10 个独有特性的强依赖前置（depends_on），通过 Feature→Feature 依赖链传递到 CS，不在 CS 闭包的 uses_feature 中显式重复声明（遵循"辐射中心"原则，避免边冗余）。

---

## §2. CS → ConfigTask 映射（uses_task，9条）

> 每方案一个主 Task 集合，按方案闭包粒度聚合。
> **注**：uses_task 列表为**声明式集合**（非执行顺序）。Task 的执行先后关系由 `02-feature-graph.md` §6 FeatureTaskOrderEdge 和 `03-task-layer.md` §7 TaskCommandOrderEdge 定义。

| CS | uses_task（主 Task 集合） | 说明 |
|----|-------------------------|------|
| CS-AC-01 PCC 阻塞 | T-007, T-008, T-001, T-002, T-AC-101, T-003(POLICYTYPE=ADC/PCC), T-AC-107, T-004, T-006 | License+SA 特征库+三四层过滤+ADC 检测+PCC 规则（ADC 兜底/PCC 阻塞）+计费属性+用户模板+刷新 |
| CS-AC-02 头增强 | T-007, T-008, T-001, T-002, T-AC-102, T-003(POLICYTYPE=HEADEN), T-004, T-006 | License 双开（含防欺诈）+SA 特征库+三四层/七层过滤+HEADEN 对象+RULE(HEADEN)+用户模板+刷新 |
| CS-AC-03 HTTP 重定向 | T-007, T-008, T-001, T-AC-103, T-002, T-003(POLICYTYPE=SMARTREDIRECT), T-004, T-006 | License+SA+EXTENDEDFILTER+ERRORCODE+SMARTHTTPREDIR+REDIRAPPENDINFO+RULE(SMARTREDIRECT)+刷新 |
| CS-AC-04 DNS 重定向 | T-007, T-008, T-001, T-AC-104, T-002, T-003(POLICYTYPE=SMARTREDIRECT), T-004, T-006 | License+SA+EXTENDEDFILTER(URL 域名)+ERRORCODE(NXDOMAIN)+DNSOVERWRITING+RULE(SMARTREDIRECT)+刷新 |
| CS-AC-05 Portal/WebProxy | Portal：T-007, T-008, T-001, T-002, T-AC-105, T-003(POLICYTYPE=PCC), T-004, T-006；WebProxy：T-007, T-008, T-001, T-002, T-AC-106, T-003(POLICYTYPE=WEBPROXY+PCC 双规则), T-004, T-006 | Portal：IPFarm+captive(USERPROFILE.CAPMODETHRES)+PCC 规则；WebProxy：IPFarm+BLACKLISTRULE+WEBPROXY/PCC 双规则 |
| CS-AC-06 URL 过滤（轨道 B） | T-007, T-008, T-001, T-002, T-AC-108, T-003(POLICYTYPE=PCC 仅触发), T-AC-107, T-004, T-006 | License+SA+ICAP 互通前置+CFTEMPLATE/CONTCATEGBIND.ACTION(BLOCK/PERMIT/REDIRECT)+PCC 触发+刷新 |
| CS-AC-07 接入控制（UNC 侧） | 动态 PCC：T-007(UNC)；本地 PCC：T-007, T-005, T-AC-109, T-003, T-004 | 动态 PCC 场景仅 License+ULI 透传；本地 PCC 场景需配置 USRLOCATION+USRLOCATIONGRP+UPBINDUPG（TR-AC-08） |
| CS-AC-08 配额耗尽重定向 | T-007, T-008, T-002, T-003(POLICYTYPE=PCC, RedirectInformation), T-004, T-006 | License+SA+流过滤+PCC 规则（携带重定向 URL）+用户模板+刷新；PCF 决策通过 N7 下发 |
| CS-AC-09 区域引导重定向 | T-007(UNC), T-AC-109(可选), T-007(UDG), T-003(POLICYTYPE=PCC/SMARTREDIRECT), T-004, T-006 | UNC 侧位置触发+UDG 侧重定向执行（RedirectInformation URL 或 SMARTHTTPREDIR） |

> **关键**：T-003（配置 PCC 规则）是 10 个 UDG 独有特性的共用 generic Task，但 POLICYTYPE 由 DP-AC-01 路由到不同的独有 Task（T-AC-101~108）操作不同的 ConfigObject（见 §6 DecisionPoint 跨层影响）。

---

## §3. Feature → ConfigTask 映射（decomposes_to，19条）

> 来源：`02-feature-graph.md` §6 FeatureTaskOrderEdge + `03-task-layer.md` §9 ConfigTask 适用矩阵
> 5 个核心 Feature 通过 FTOE 显式编排 Task 顺序（见 02 §6）；其余 14 个 Feature 通过 may_require_feature 关联到独有 Task。
> **★ P5 修复（U-M-07/F05）**：补 `source_evidence_ids` 列，溯源到特性证据 + FTOE 编排边证据（附录 D 端到端流程）。
> **★ P5 批次 3 修复（U-H-02 跨文件同步）**：补 4 个 UNC 接入控制辅助特性的 decomposes_to 边（WSFD-106003/105003/106005/105006），Task 映射到 UNC 侧 T-005（APN 绑定）+ T-AC-109（位置条件策略，仅本地 PCC 场景），与 02 §1.9 + §2.3 depends_on 关系一致。

| Feature | decomposes_to | Task 集 | 说明 | `source_evidence_ids` |
|---------|---------------|--------|------|----------------------|
| GWFD-110101 SA-Basic | T-007, T-008, T-001, T-006 | License+SA 特征库+业务分类+刷新（三场景共享基础链） | `EV-FK-AC-01`, `EV-CA-AC-01` |
| GWFD-020351 PCC(UDG) | T-007, T-001, T-002, T-003, T-004, T-006 | License+业务分类+流过滤+PCC 规则+用户模板+刷新（PCC 框架基础链） | `EV-FK-AC-02`, `EV-CA-AC-01` |
| WSFD-109101 PCC(UNC) | T-007, T-005, T-003(UNC), T-004 | License+用户模板组绑定链+UNC 侧规则+模板（三场景共享 UNC 骨架） | `EV-FK-AC-03`, `EV-CA-AC-01` |
| GWFD-020357 ADC(UDG) | T-007, T-008, T-AC-101, T-AC-107, T-002, T-003(POLICYTYPE=ADC), T-004, T-006 | License+SA 特征库+ADCPARA+计费属性+流过滤+ADC 规则+用户模板+刷新（FTOE-AC-001~005） | `EV-FK-AC-04`, `EV-CA-AC-01`, `EV-CA-D1` |
| WSFD-109102 ADC(UNC) | T-007, T-AC-101(UNC 侧), T-003, T-005 | License+ADC 参数+三策略组规则+绑定链（三场景共享 UNC 侧 ADC） | `EV-FK-AC-05`, `EV-CA-AC-01` |
| GWFD-110261 HTTP 头增强 | T-007, T-008, T-001, T-002, T-AC-102, T-003(POLICYTYPE=HEADEN), T-004, T-006 | License+SA+三四层/七层过滤+HEADEN 对象+RULE(HEADEN)+用户模板+刷新（FTOE-AC-006~011） | `EV-FK-AC-06`, `EV-CA-AC-01`, `EV-CA-D2` |
| GWFD-110262 RTSP 头增强 | T-007, T-008, T-001, T-002, T-AC-102, T-003(POLICYTYPE=HEADEN), T-004, T-006 | 同 HTTP 头增强链（共用 T-AC-102，协议参数差异；不支持防欺诈） | `EV-FK-AC-07`, `EV-CA-AC-01`, `EV-CA-D2` |
| GWFD-110263 HTTPS 头增强 | T-007, T-008, T-001, T-002, T-AC-102, T-003(POLICYTYPE=HEADEN), T-004, T-006 | 同 HTTP 头增强链（共用 T-AC-102，SSL Extension TLV 格式；支持防欺诈） | `EV-FK-AC-08`, `EV-CA-AC-01`, `EV-CA-D2` |
| GWFD-110401 HTTP 头防欺诈 | T-007, T-AC-102（内嵌 ANTIFRAUD/GRAYLIST）, T-003(POLICYTYPE=HEADEN), T-004, T-006 | 强耦合 HTTP 头增强（License 双开）；防欺诈检测→纠正/清理→头增强插入（FTOE-AC-010） | `EV-FK-AC-09`, `EV-CA-AC-01`, `EV-CA-D2` |
| GWFD-110281 用户 Portal | T-007, T-008, T-001, T-002, T-AC-105, T-AC-107, T-003(POLICYTYPE=PCC), T-004, T-006 | License+SA+IPFarm 集群+计费属性+PCC 规则+captive(USERPROFILE.CAPMODETHRES)+刷新 | `EV-FK-AC-10`, `EV-CA-AC-01`, `EV-CA-D3` |
| GWFD-110282 WebProxy | T-007, T-008, T-001, T-002, T-AC-106, T-AC-107, T-003(POLICYTYPE=WEBPROXY+PCC 双规则), T-004, T-006 | License+SA+IPFarm+BLACKLISTRULE+计费属性+WEBPROXY/PCC 双规则+刷新（TR-AC-06） | `EV-FK-AC-11`, `EV-CA-AC-01`, `EV-CA-D3` |
| GWFD-110283 DNS 纠错 | T-007, T-008, T-001, T-AC-104, T-002, T-003(POLICYTYPE=SMARTREDIRECT), T-004, T-006 | License+SA+EXTENDEDFILTER(URL)+ERRORCODE(NXDOMAIN)+DNSOVERWRITING+RULE(SMARTREDIRECT)+刷新 | `EV-FK-AC-12`, `EV-CA-AC-01`, `EV-CA-D3` |
| GWFD-110284 HTTP 智能重定向 | T-007, T-008, T-001, T-AC-103, T-002, T-003(POLICYTYPE=SMARTREDIRECT), T-004, T-006 | License+SA+EXTENDEDFILTER+ERRORCODE+SMARTHTTPREDIR+REDIRAPPENDINFO+RULE(SMARTREDIRECT)+刷新（FTOE-AC-012~015） | `EV-FK-AC-13`, `EV-CA-AC-01`, `EV-CA-D3` |
| GWFD-110471 URL 过滤 | T-007, T-008, T-001, T-002, T-AC-108, T-AC-107, T-003(POLICYTYPE=PCC 仅触发), T-004, T-006 | License+SA+ICAP 互通前置+CFTEMPLATE/CONTCATEGBIND.ACTION+计费属性+PCC 触发+刷新（FTOE-AC-016~021，轨道 B 独立） | `EV-FK-AC-14`, `EV-CA-AC-01`, `EV-CA-D1` |
| WSFD-211001 位置触发（UNC） | T-007, T-AC-109(本地 PCC 场景), T-005 | License（强依赖 PCC UNC）+USRLOCATION+USRLOCATIONGRP+UPBINDUPG+APNUSRPROFG；动态 PCC 场景跳过 T-AC-109（FTOE-AC-022~025，TR-AC-08） | `EV-FK-AC-15`, `EV-CA-AC-01`, `EV-CA-D4` |
| WSFD-106003 用户接入控制（AMF，SAR） | T-007(UNC), T-005, T-AC-109(可选) | UNC 侧 AMF 注册阶段：License+用户模板组/APN 绑定（T-005）+ 位置条件策略（T-AC-109，仅本地 PCC 场景，动态 PCC 由 PCF 下发）；与 WSFD-211001 共用 UNC 侧 Task 骨架（★ U-H-02 补） | `EV-FK-AC-16`, `EV-CA-AC-01`, `EV-CA-D4` |
| WSFD-105003 区域漫游限制（AMF） | T-007(UNC), T-005 | UNC 侧 AMF 注册阶段：License+APN 绑定（区域漫游限制通过 UDM 签约 PLMN/号段触发，不额外配置 ConfigObject；位置条件策略可选复用 T-AC-109）；与 WSFD-106003 共用 UDM 数据源（★ U-H-02 补） | `EV-FK-AC-17`, `EV-CA-AC-01`, `EV-CA-D4` |
| WSFD-106005 支持 ODB（AMF） | T-007(UNC), T-005 | UNC 侧 AMF 注册+SMF 会话：License+APN 绑定（ODB 闭锁通过 UDM 签约 ODB 数据触发，无额外 ConfigObject；跨注册/会话两阶段）；与 WSFD-105003 共用 ODB 数据源（★ U-H-02 补） | `EV-FK-AC-18`, `EV-CA-AC-01`, `EV-CA-D4` |
| WSFD-105006 会话服务区域限制（SMF） | T-007(UNC), T-005, T-AC-109(可选) | UNC 侧 SMF 会话阶段：License+APN 绑定+位置条件策略（T-AC-109，基于签约 SAR/Tracking Area，会话级区域限制如释放/限速）；与 AMF 侧 WSFD-106003 互补构成"注册准入+会话保持"链（★ U-H-02 补） | `EV-FK-AC-19`, `EV-CA-AC-01`, `EV-CA-D4` |

> **去重统计**：19 Feature decomposes_to 19 Task 集合（★ P5 批次 3：15+4 UNC 辅助）；其中 5 个核心 Feature（GWFD-020357 / GWFD-110261+110401 / GWFD-110284 / GWFD-110471 / WSFD-211001）通过 25 条 FTOE 显式编排 Task 内部顺序（见 02-feature-graph.md §6）。4 个 UNC 接入控制辅助特性无独立 FTOE，通过 may_require_feature 关联到 UNC 侧 Task 骨架（T-005/T-AC-109），与 WSFD-211001 共用骨架。

---

## §4. ConfigTask → MMLCommand 映射（invokes，~68条核心映射）

> 来源：`03-task-layer.md` §1~§4 + `04-command-graph.md` §1
> 完整命令清单见 04 §1.1~§1.15。下表按 Task 归类汇总。

| ConfigTask | invokes | MMLCommand（CMD-UDG/UNC-NNN） | 说明 |
|-----------|---------|------------------------------|------|
| **通用 Task** | | | |
| T-001 规划业务分类 | invokes | ADD CATEGORYPROP (CMD-UDG-? ), ADD FILTER (005), ADD L7FILTER (008), ADD EXTENDEDFILTER (010), ADD ERRORCODE (011) | 业务分类与过滤条件定义 |
| T-002 配置流过滤器 | invokes | ADD FLOWFILTER (006), ADD FLTBINDFLOWF (007), ADD PROTBINDFLOWF (009) | 流过滤器组装 |
| T-003 配置 PCC 规则 | invokes | ADD RULE (CMD-UDG-043 / CMD-UNC-012) | PCC 规则（POLICYTYPE 由 DP-AC-01 路由，TR-AC-02） |
| T-004 配置用户模板 | invokes | ADD USERPROFILE (CMD-UDG-044 / CMD-UNC-013), ADD RULEBINDING (045/014) | 用户模板+规则绑定 |
| T-005 配置 APN 绑定 | invokes | ADD USRPROFGROUP (UNC-015), ADD/MOD UPBINDUPG (UNC-016/017), ADD APNUSRPROFG (UNC-018), ADD APN (UDG-024) | UNC 标准绑定链（含 LOCGROUPNAME） |
| T-006 策略刷新 | invokes | SET REFRESHSRV (CMD-UDG-002) | 策略刷新生效（must_be_last，TR-AC-01） |
| T-007 License 开启 | invokes | SET LICENSESWITCH (CMD-UDG-001 / CMD-UNC-001) | License 前置门控 |
| T-008 SA 特征库加载 | invokes | LOD SIGNATUREDB (CMD-UDG-003), LOD PARSERDB (004) | SA 特征库加载 |
| **轨道 A 独有 Task** | | | |
| T-AC-101 配置 ADC | invokes | ADD ADCPARA (CMD-UDG-013), ADD RULE (043, POLICYTYPE=ADC) | ADC 检测参数+规则 |
| T-AC-102 配置头增强 | invokes | ADD WELLKNOWNPORT (012), ADD HEADEN (014, 含 ANTIFRAUD/GRAYLIST), SET BASE64 (015), ADD RULE (043, POLICYTYPE=HEADEN) | 头增强对象+规则（跨 4 特性复用） |
| T-AC-103 配置 HTTP 重定向 | invokes | ADD EXTENDEDFILTER (010), ADD ERRORCODE (011), ADD REDIRAPPENDINFO (017), ADD SMARTHTTPREDIR (016), ADD RULE (043, POLICYTYPE=SMARTREDIRECT, POLICYNAME=SMARTHTTPREDIR) | HTTP 智能重定向链 |
| T-AC-104 配置 DNS 纠错 | invokes | ADD EXTENDEDFILTER (010), ADD ERRORCODE (011), ADD DNSOVERWRITING (018), ADD RULE (043, POLICYTYPE=SMARTREDIRECT, POLICYNAME=DNSOVERWRITING) | DNS 纠错链（共用 SMARTREDIRECT） |
| T-AC-105 配置 Portal | invokes | SET IPFARMGLOBAL (019), ADD LOGICINF (022), ADD IPFARM (020), ADD IPFARMSERVER (021), ADD URR (047), ADD URRGROUP (048), ADD PCCPOLICYGRP (046), ADD USERPROFILE (044, 含 CAPMODETHRES), ADD RULE (043, POLICYTYPE=PCC), ADD RULEBINDING (045), ADD APN (024) | Portal captive 完整链 |
| T-AC-106 配置 WebProxy | invokes | SET IPFARMGLOBAL (019), ADD LOGICINF (022), ADD IPFARM (020), ADD IPFARMSERVER (021), ADD BLACKLISTRULE (023), ADD URR (047), ADD URRGROUP (048), ADD PCCPOLICYGRP (046), ADD RULE×2 (043, POLICYTYPE=WEBPROXY + POLICYTYPE=PCC), ADD USERPROFILE (044), ADD RULEBINDING (045), ADD APN (024) | WebProxy 双规则链（TR-AC-06） |
| T-AC-107 配置 PCC 动作组 | invokes | ADD URR (047), ADD URRGROUP (048), ADD PCCPOLICYGRP (046) | 计费属性绑定（ADC/Portal/WebProxy/URL 过滤共用） |
| **轨道 B 独有 Task** | | | |
| T-AC-108 配置 URL 过滤 | invokes | ADD VPNINST (025), ADD LOGICINF (022), ADD ICAPSERVER (026), ADD ICAPLOCALINFO (027), ADD ICAPSVRGRP (028), ADD ICAPSVRBINDISG (029), SET CFSRVMODE (030), ADD APN (024), SET APNCFFUNC (031), ADD CFPROFILE (032), ADD CFTEMPLATE (033, ACTION), SET APNCFTEMPLATE (034), ADD CFPROFBINDCFT (035), ADD CONTCATEGROUP (036), ADD CONTCATEGBIND (037, ACTION), SET CFCACHEPARA (038), SET GLBCFFUNC (039), ADD CFWHITEURLLST (040), ADD CFIPWHITELIST (041), ADD CFPFSPECACTION (042), ADD URR (047), ADD URRGROUP (048), ADD PCCPOLICYGRP (046), ADD RULE (043, POLICYTYPE=PCC 仅触发) | URL 过滤完整链（轨道 B 独立，TE-AC-108-1~16） |
| **UNC 接入控制 Task** | | | |
| T-AC-109 配置位置策略 | invokes | ADD USRLOCATION (UNC-019), ADD USRLOCATIONGRP (UNC-020), MOD UPBINDUPG (UNC-017), ADD APNUSRPROFG (UNC-018) | UNC 侧位置触发链（仅本地 PCC 场景，TR-AC-08） |

> **说明**：T-001 中的 ADD CATEGORYPROP 在 04-command 主清单中归入辅助对象族（OBJ-CATEGORYPROP），未单独编号；SET LICENSESWITCH / SET REFRESHSRV 等 SET 命令在 04 中均有编号。完整 68 条命令清单（UDG 48 + UNC 20，★ P5 修正计数）见 04 §1.1~§1.15。

---

## §5. ConfigTask → SemanticObject/ConfigObject 映射（targets，~45条）

> 来源：`03-task-layer.md` §9 ConfigTask 适用矩阵 + `04-command-graph.md` §2 ConfigObject 实例

| ConfigTask | targets SemanticObject | targets ConfigObject |
|-----------|------------------------|---------------------|
| T-001 规划业务分类 | SO-AC-02（过滤条件） | CATEGORYPROP, FILTER, L7FILTER, EXTENDEDFILTER, ERRORCODE |
| T-002 配置流过滤器 | SO-AC-02（过滤条件） | FLOWFILTER, FLTBINDFLOWF, PROTBINDFLOWF |
| T-003 配置 PCC 规则 | SO-AC-01（动作类型）, SO-AC-06（规则语义）, SO-AC-07（动作轨道） | RULE（OBJ-RULE） |
| T-004 配置用户模板 | — | USERPROFILE, RULEBINDING |
| T-005 配置 APN 绑定 | SO-AC-05（位置条件，UNC 侧） | USRPROFGROUP, UPBINDUPG, APNUSRPROFG, APN |
| T-006 策略刷新 | — | —（元操作，触发下发） |
| T-007 License 开启 | — | —（License 全局） |
| T-008 SA 特征库加载 | SO-AC-02（业务识别基础） | —（SA 特征库数据） |
| T-AC-101 配置 ADC | SO-AC-06（规则语义-POLICYTYPE=ADC） | ADCPARA（OBJ-ADCPARA）, RULE |
| T-AC-102 配置头增强 | SO-AC-01（动作类型-HEADEN）, SO-AC-04（头增强字段） | HEADEN（OBJ-AC-HEADEN，含 ANTIFRAUD/GRAYLIST）, WELLKNOWNPORT, RULE |
| T-AC-103 配置 HTTP 重定向 | SO-AC-01（动作类型-REDIRECT）, SO-AC-03（重定向目标-SMARTHTTPREDIR）, SO-AC-07（动作轨道-SMARTREDIRECT） | SMARTHTTPREDIR（OBJ-AC-SMARTHTTPREDIR）, REDIRAPPENDINFO, EXTENDEDFILTER, ERRORCODE, RULE |
| T-AC-104 配置 DNS 纠错 | SO-AC-01, SO-AC-03（DNSOVERWRITING）, SO-AC-07 | DNSOVERWRITING（OBJ-AC-DNSOVERWRITING）, EXTENDEDFILTER, ERRORCODE, RULE |
| T-AC-105 配置 Portal | SO-AC-01, SO-AC-03（IPFarm）, SO-AC-07（SMARTREDIRECT/PCC） | IPFARMGLOBAL, IPFARM, IPFARMSERVER, LOGICINF, URR, URRGROUP, PCCPOLICYGRP, USERPROFILE（含 CAPMODETHRES）, RULE, RULEBINDING, APN |
| T-AC-106 配置 WebProxy | SO-AC-01, SO-AC-03（IPFarm-Proxy）, SO-AC-07（WEBPROXY 独立体系） | IPFARMGLOBAL, IPFARM, IPFARMSERVER, LOGICINF, BLACKLISTRULE, URR, URRGROUP, PCCPOLICYGRP, RULE×2（WEBPROXY+PCC）, USERPROFILE, RULEBINDING, APN |
| T-AC-107 配置 PCC 动作组 | SO-AC-06（规则语义-POLICYTYPE=PCC 计费属性） | URR, URRGROUP, PCCPOLICYGRP |
| T-AC-108 配置 URL 过滤 | SO-AC-01（BLOCK/PERMIT/REDIRECT）, SO-AC-02（URL 分类）, SO-AC-07（URL 过滤独立轨道 B） | VPNINST, LOGICINF, ICAPSERVER, ICAPLOCALINFO, ICAPSVRGRP, ICAPSVRBINDISG, CFSRVMODE, APNCFFUNC, CFPROFILE, CFTEMPLATE, APNCFTEMPLATE, CFPROFBINDCFT, CONTCATEGROUP, CONTCATEGBIND, CFCACHEPARA, GLBCFFUNC, CFWHITEURLLST, CFIPWHITELIST, CFPFSPECACTION, URR, URRGROUP, PCCPOLICYGRP, RULE |
| T-AC-109 配置位置策略 | SO-AC-05（位置条件-USRLOCATION）, SO-AC-06（规则语义-接入控制） | USRLOCATION（OBJ-AC-USRLOCATION）, USRLOCATIONGRP, UPBINDUPG, APNUSRPROFG |

---

## §6. DecisionPoint 跨层影响（selects / sets_value_pattern）

> 来源：`01-business-graph.md` §9.6 + `03-task-layer.md` §6

| DP | 关系 | 目标 | 说明 |
|----|------|------|------|
| DP-AC-01 动作类型选择（业务层） | `selects` | CS-AC-01（DISCARD）/ CS-AC-02（HEADEN）/ CS-AC-03~05、08、09（REDIRECT）/ CS-AC-06（PERMIT，仅 URL 过滤） | 动作类型决定方案闭包（双轨道+五子轨入口） |
| DP-AC-01（任务层）POLICYTYPE 路由 | `selects` | T-AC-101（ADC）/ T-AC-102（HEADEN）/ T-AC-103（HTTP 重定向）/ T-AC-104（DNS 纠错）/ T-AC-105（Portal）/ T-AC-106（WebProxy）/ T-AC-107（PCC 动作组）/ T-AC-108（URL 过滤） | POLICYTYPE 路由到不同独有 Task（TR-AC-02） |
| **DP-AC-03 动作轨道选择（★双轨道+五子轨核心）** | `sets_value_pattern` | **ADD RULE.POLICYTYPE** | 轨道 A → POLICYTYPE=ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY；轨道 B → CFTEMPLATE/CONTCATEGBIND.ACTION（BLOCK/PERMIT/REDIRECT）。**决定 ConfigObject 体系（RULE vs CFTEMPLATE）、动作指定方式（隐式 vs 显式）、外部依赖（可选 PCRF vs 必需 ICAP）、是否支持 PERMIT** |
| DP-AC-02 规则类型选择 | `sets_value_pattern` | ADD RULE.RULETYPE | 动态/预定义/本地三选一；URL 过滤必选预定义 |
| DP-AC-04 网元范围选择 | `selects` | CS-AC-07（UNC 侧粗粒度接入控制）vs CS-AC-01~06（UDG 侧细粒度业务控制） | 决定规则生效范围 |
| DP-AC-05 匹配层次选择 | `sets_value_pattern` | FILTER（L3/L4）/ L7FILTER（L7）/ EXTENDEDFILTER（多维）/ ERRORCODE（DNS） | 决定 Filter 类型与 SA 依赖 |
| DP-AC-06 重定向目标选择 | `sets_value_pattern` | SMARTHTTPREDIR / DNSOVERWRITING / IPFARM / RedirectInformation | 决定重定向特性选择 |
| DP-AC-07 协议支持选择 | `sets_value_pattern` | 协议范围（HTTP1.x / HTTPS / RTSP / 任意 TCP / DNS） | 决定特性选择；加密协议仅 WebProxy |
| DP-AC-02 头防欺诈使能（任务层） | `selects` | T-AC-102 内部 ANTIFRAUD/GRAYLIST 参数 + T-007 是否开启 HHAS License | ENABLE 需双开 License；DISABLE 单开 |
| DP-AC-03 位置触发接口（任务层） | `selects` | T-AC-109 是否执行 | 动态 PCC（Gx/N7）→ 跳过；本地 PCC → 执行（TR-AC-08） |

> **★ DP-AC-03 是访问限制场景的核心决策点**：它通过 sets_value_pattern RULE.POLICYTYPE 体现"动作轨道（双轨道+五子轨）"机制（轨道 A PCC 体系隐式驱动 vs 轨道 B URL 过滤体系显式 BLOCK/PERMIT/REDIRECT）。这是访问限制场景区别于计费（固定 CHARGING）和带宽控制（动态 BWM/PCC/QOS/ADC）的标志性架构。

---

## §7. 端到端链路验证（4条完整路径，覆盖双轨道+五子轨）

### 7.1 路径 A：PCC 阻塞/接入控制链路（轨道 A，DISCARD 动作）

```
[业务] BD-AC-01 业务感知（= BD-CH-01 = BD-BW-01，三场景共享）
  → NS-AC-01 访问限制场景
    → CS-AC-01 PCC 阻塞方案（或 CS-AC-07 UNC 接入控制）
      → DP-AC-01 选择 DISCARD 动作
      → DP-AC-03 选择轨道 A（PCC 体系）
      → DP-AC-02 选择规则类型（动态/预定义/本地）
      → BR-AC-01 预定义规则三网元一致性
      → BR-AC-03 一条规则绑定一条策略
      → BR-AC-07 RULE.POLICYTYPE 决定动作轨道（双轨道+五子轨）
      → SO-AC-01（DISCARD）, SO-AC-02（过滤条件）, SO-AC-06（规则语义）, SO-AC-07（轨道 A）

[特性] CS-AC-01 uses_feature
  → GWFD-020351 PCC(UDG)（策略载体）
  → WSFD-109101 PCC(UNC)（策略下发承载）
  → GWFD-020357 ADC(UDG)（L7 横切前置 + 兜底阻塞）

[任务] GWFD-020357 decomposes_to（FTOE-AC-001~005）
  → T-007 License 开启（LKV3G5ADCF01 + LKV3G5PCCB01）
  → T-008 SA 特征库加载（LOD SIGNATUREDB + LOD PARSERDB）
  → T-AC-101 配置 ADC（ADD ADCPARA + ADD RULE:POLICYTYPE=ADC）★ 兜底阻塞
  → T-AC-107 配置 PCC 动作组（ADD URR + URRGROUP + PCCPOLICYGRP）★ 计费属性
  → T-002 配置流过滤器（ADD FLOWFILTER + FLTBINDFLOWF）
  → T-003 配置 PCC 规则（ADD RULE:POLICYTYPE=PCC, POLICYNAME=PCCPOLICYGRP）★ 核心规则
  → T-004 配置用户模板（ADD USERPROFILE + RULEBINDING）
  → T-006 SET REFRESHSRV（must_be_last，60s 生效）

[命令] T-003 invokes → ADD RULE (CMD-UDG-043)
  → operates_on → ConfigObject: RULE（OBJ-RULE）
    → 关键参数: RULENAME, POLICYTYPE=PCC, PRIORITY, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME, POLICYNAME=PCCPOLICYGRP
  → constrained_by → CR-AC-02 POLICYTYPE 决定动作对象链（PCC→POLICYNAME→PCCPOLICYGRP）
  → constrained_by → CR-AC-09 预定义规则名三网元一致
  → impacted_by → DP-AC-03 sets_value_pattern(POLICYTYPE=PCC)

[UNC 侧接入控制（CS-AC-07 补充链路，本地 PCC 场景）]
  → WSFD-211001 decomposes_to（FTOE-AC-022~025）
  → T-007 License 开启（LKV2PCIAL01 + LKV3W9SPCC11 强依赖）
  → T-AC-109 配置位置策略（ADD USRLOCATION[CGI/ECGI/NCGI] + USRLOCATIONGRP + MOD UPBINDUPG[LOCGROUPNAME] + APNUSRPROFG）
  → 用户激活时匹配 ULI → UNC 下发 PCC 策略（N4）→ UDG 执行 USERPROFILE 绑定的阻塞/重定向规则

[证据] CS-AC-01 → [EV-CA-AC-01, EV-FK-AC-02, EV-FK-AC-04, EV-TK-AC-01/02/04]
  ADD RULE → [EV-FK-AC-CFA, EV-CA-D1]
  WSFD-211001 → [EV-FK-AC-15, EV-CA-D4]
```

### 7.2 路径 B：URL 过滤链路（轨道 B，BLOCK/PERMIT/REDIRECT 显式动作）

```
[业务] BD-AC-01 → NS-AC-01
  → CS-AC-06 URL 过滤方案（轨道 B）
    → DP-AC-01 选择 BLOCK/PERMIT/REDIRECT
    → DP-AC-03 选择轨道 B（URL 过滤体系，独立于 PCC）★
    → DP-AC-05 选择 L7 匹配（URL 分类）
    → BR-AC-05 REFRESHSRV 最后执行
    → BR-AC-10 PERMIT 唯一性（URL 过滤独有）
    → SO-AC-01（BLOCK/PERMIT/REDIRECT）, SO-AC-02（URL 分类）, SO-AC-07（轨道 B）

[特性] CS-AC-06 uses_feature
  → GWFD-110471 URL 过滤基本功能（轨道 B 核心，唯一显式 PERMIT）
  → GWFD-020357 ADC(UDG)（URL 提取前置，HTTPS 仅 SNI）

[任务] GWFD-110471 decomposes_to（FTOE-AC-016~021）
  → T-007 License 开启（LKV3G5UFBF01，82200FCP）
  → T-008 SA 特征库加载
  → T-AC-108 配置 URL 过滤 ★ 完整独立链（TE-AC-108-1~16）
    ├─ ① ICAP 互通前置层：ADD VPNINST → LOGICINF → ICAPSERVER → ICAPLOCALINFO → ICAPSVRGRP → ICAPSVRBINDISG
    ├─ ② APN 开关：ADD APN + SET APNCFFUNC
    ├─ ③ CF 业务层：ADD CFPROFILE → CFTEMPLATE(ACTION=BLOCK/PERMIT/REDIRECT) → SET APNCFTEMPLATE → ADD CFPROFBINDCFT
    ├─ ④ 分类级动作：ADD CONTCATEGROUP → ADD CONTCATEGBIND(ACTION，覆盖模板级缺省)
    ├─ ⑤ 共用 PCC 触发层：ADD URR → URRGROUP → PCCPOLICYGRP → ADD RULE(POLICYTYPE=PCC 仅触发)
    └─ ⑥ 辅助：SET CFCACHEPARA, SET GLBCFFUNC, ADD CFWHITEURLLST, ADD CFIPWHITELIST
  → T-006 SET REFRESHSRV（must_be_last）

[命令] T-AC-108 invokes → ADD CFTEMPLATE (CMD-UDG-033) + ADD CONTCATEGBIND (CMD-UDG-037)
  → operates_on → ConfigObject: CFTEMPLATE（OBJ-AC-CFTEMPLATE）/ CONTCATEGBIND（OBJ-AC-CONTCATEGBIND）
    → 关键参数: CFTEMPLATENAME, ICAPSRVGMNAME, ACTION=BLOCK/PERMIT/REDIRECT（模板级缺省）
    → 关键参数: CFPROFILENAME, CONTCATEGNAME, ACTION（分类级精确，覆盖模板级）
  → constrained_by → CR-AC-05 ICAP Server 必需（前置链路）
  → constrained_by → CR-AC-06 PERMIT 动作唯一性（仅轨道 B 显式支持）
  → constrained_by → CR-AC-14 双轨可并存（轨道 A + 轨道 B）
  → impacted_by → DP-AC-03 sets_value_pattern(轨道 B → CFTEMPLATE.ACTION)

[证据] CS-AC-06 → [EV-CA-AC-01, EV-FK-AC-09, EV-TK-AC-07]
  ADD CFTEMPLATE → [EV-FK-AC-14, EV-CA-D1]
```

### 7.3 路径 C：HTTP 重定向链路（轨道 C，SMARTREDIRECT）

```
[业务] BD-AC-01 → NS-AC-01
  → CS-AC-03 HTTP 重定向方案
    → DP-AC-01 选择 REDIRECT
    → DP-AC-03 选择轨道 A（PCC 体系，POLICYTYPE=SMARTREDIRECT 子轨）
    → DP-AC-06 选择重定向目标（第三方服务器）
    → DP-AC-07 选择协议（仅 HTTP1.x）
    → BR-AC-07 RULE.POLICYTYPE=SMARTREDIRECT
    → BR-AC-09 加密协议仅 WebProxy 可处理（HTTP 重定向不支持 HTTPS）
    → SO-AC-01（REDIRECT）, SO-AC-03（SMARTHTTPREDIR）, SO-AC-07（SMARTREDIRECT）

[特性] CS-AC-03 uses_feature
  → GWFD-110284 HTTP 智能重定向（L7 HTTP 响应改写）
  → GWFD-020357 ADC(UDG)（L7 解析前置）
  → GWFD-110261 HTTP 头增强（可选，REDIRAPPENDINFO 携带 MSISDN/IMSI）

[任务] GWFD-110284 decomposes_to（FTOE-AC-012~015）
  → T-007 License 开启（LKV3G5SHPR01，82209783）
  → T-008 SA 特征库加载
  → T-001 规划业务分类（EXTENDEDFILTER + ERRORCODE，多条件 AND）
  → T-AC-103 配置 HTTP 智能重定向 ★
    ├─ ADD EXTENDEDFILTER（URL/UserAgent/ContentType/URLPostfix 多维）
    ├─ ADD ERRORCODE（HTTP 错误码 GT 400）
    ├─ ADD REDIRAPPENDINFO（携带 MSISDN/IMSI/IMEI，可选）
    ├─ ADD SMARTHTTPREDIR（绑定 EXTFLT + ERRORCODE + APPENDINFO）
    └─ ADD RULE:POLICYTYPE=SMARTREDIRECT, POLICYNAME=SMARTHTTPREDIR
  → T-002 配置流过滤器（ADD FLOWFILTER + FLTBINDFLOWF）
  → T-004 配置用户模板（ADD USERPROFILE + RULEBINDING）
  → T-006 SET REFRESHSRV

[命令] T-AC-103 invokes → ADD SMARTHTTPREDIR (CMD-UDG-016) + ADD RULE (043)
  → operates_on → ConfigObject: SMARTHTTPREDIR（OBJ-AC-SMARTHTTPREDIR）
    → 关键参数: SMTHTTPREDINAME, SERVERURL, EXTFLTTYPE1/2(AND), EXTFLTNAME1/2, APPENDINFONAME, BINDErrCODENAME
  → constrained_by → CR-AC-02 POLICYTYPE=SMARTREDIRECT → POLICYNAME 指向 SMARTHTTPREDIR
  → constrained_by → CR-AC-03 SMARTREDIRECT 两子类型共用 POLICYTYPE（区分点在 POLICYNAME 指向 SMARTHTTPREDIR vs DNSOVERWRITING）
  → constrained_by → CR-AC-10 HTTPS/HTTP2.0 加密盲区（HTTP 重定向不支持）
  → impacted_by → DP-AC-06 sets_value_pattern(重定向目标=SMARTHTTPREDIR)

[证据] CS-AC-03 → [EV-CA-AC-01, EV-FK-AC-05, EV-TK-AC-06]
  ADD SMARTHTTPREDIR → [EV-FK-AC-13, EV-CA-D3]
```

### 7.4 路径 D：头增强链路（轨道 D，HEADEN）

```
[业务] BD-AC-01 → NS-AC-01
  → CS-AC-02 头增强方案
    → DP-AC-01 选择 HEADEN
    → DP-AC-03 选择轨道 A（PCC 体系，POLICYTYPE=HEADEN 子轨）
    → DP-AC-05 选择 L7 匹配（URL/SNI/Method）
    → DP-AC-07 选择协议（HTTP1.x / HTTPS / RTSP 三选一）
    → DP-AC-02（任务层）头防欺诈使能决策（ENABLE 需双开 License）
    → BR-AC-04 License 前置门控（头防欺诈 82209786 + 头增强 82209777 双开）
    → BR-AC-06 头防欺诈依赖头增强
    → BR-AC-08 字段加密与编码约束
    → SO-AC-01（HEADEN）, SO-AC-04（头增强字段）, SO-AC-06（规则语义）

[特性] CS-AC-02 uses_feature
  → GWFD-110261 HTTP 头增强（HTTP1.x，支持防欺诈）
  → GWFD-110262 RTSP 头增强（RTSP，不支持防欺诈）
  → GWFD-110263 HTTPS 头增强（SSL Extension TLV，支持防欺诈）
  → GWFD-110401 HTTP 头防欺诈（强耦合 110261）
  → GWFD-020357 ADC(UDG)（L7 解析前置）

[任务] GWFD-110261 + GWFD-110401 decomposes_to（FTOE-AC-006~011，含防欺诈强耦合）
  → T-007 License 双开（LKV3G5HTHE01 头增强 + LKV3G5HHAS01 头防欺诈）
  → T-008 SA 特征库 + 协议解析库加载
  → T-001 规划业务分类（FILTER + L7FILTER + WELLKNOWNPORT）
  → T-002 配置三四层+七层过滤（ADD FILTER/FLOWFILTER/FLTBINDFLOWF + L7FILTER/PROTBINDFLOWF）
  → T-AC-102 配置头增强对象（ADD HEADEN:ANTIFRAUD=ENABLE/GRAYLIST=ENABLE）★ 核心
    ├─ ADD WELLKNOWNPORT（识别 HTTP 端口 80/8080）
    ├─ ADD HEADEN（DATATYPE=IMSI1/MSISDN1, ENCRYALGORI=AES128/SHA256, ANTIFRAUD=ENABLE）
    └─ 防欺诈子模式：检测→字段纠正/冗余清理→头增强插入（BIT1030 控制顺序）
  → T-003 配置 PCC 规则（ADD RULE:POLICYTYPE=HEADEN, POLICYNAME=HEADEN 对象名）
  → T-004 配置用户模板（ADD USERPROFILE + RULEBINDING）
  → T-006 SET REFRESHSRV

[命令] T-AC-102 invokes → ADD HEADEN (CMD-UDG-014) + ADD RULE (043)
  → operates_on → ConfigObject: HEADEN（OBJ-AC-HEADEN）
    → 关键参数: HEADERENNAME, DATATYPE, PREFIXNAME, ENCRYALGORI, PSWDKEY, ANTIFRAUD(ENABLE/DISABLE), GRAYLIST(ENABLE/DISABLE)
  → constrained_by → CR-AC-02 POLICYTYPE=HEADEN → POLICYNAME 指向 HEADEN 对象
  → constrained_by → CR-AC-04 头防欺诈强依赖头增强（License 双开）
  → constrained_by → CR-AC-11 RTSP 不支持头防欺诈（族内唯一例外）
  → impacted_by → DP-AC-02（任务层）sets ANTIFRAUD=ENABLE/DISABLE

[证据] CS-AC-02 → [EV-CA-AC-01, EV-CA-AC-02, EV-FK-AC-03/04, EV-TK-AC-05/08]
  ADD HEADEN → [EV-FK-AC-06/07/08/13, EV-CA-D2]
```

### 7.5 补充链路：WebProxy 重定向（轨道 B-1，唯一支持 HTTPS/HTTP2.0）

```
[业务] BD-AC-01 → NS-AC-01
  → CS-AC-05 Portal/WebProxy 重定向方案（WebProxy 子链）
    → DP-AC-06 选择重定向目标=Proxy 服务器
    → DP-AC-07 选择协议=任意 TCP（含 HTTPS/HTTP2.0）★ 唯一
    → BR-AC-09 加密协议仅 WebProxy 可处理
    → SO-AC-01（REDIRECT）, SO-AC-03（IPFarm-Proxy）, SO-AC-07（WEBPROXY 独立体系）

[特性] CS-AC-05 uses_feature
  → GWFD-110282 WebProxy（L3 IP NAT，支持加密协议）
  → GWFD-110281 用户 Portal（同一方案的另一子链，SMARTREDIRECT 体系）

[任务] GWFD-110282 decomposes_to
  → T-007 License 开启（LKV3G5WEBP01，82209781）
  → T-008 SA 特征库加载（可选，L3 不强依赖）
  → T-001/T-002 配置三四层过滤（TCP SYN 匹配，L3）
  → T-AC-106 配置 WebProxy ★ 双规则链
    ├─ ADD LOGICINF + IPFARM + IPFARMSERVER + BLACKLISTRULE（Proxy 服务器集群）
    ├─ ADD URR + URRGROUP + PCCPOLICYGRP（计费属性）
    ├─ ADD RULE:POLICYTYPE=WEBPROXY, POLICYNAME=IPFARM ★ 重定向规则
    └─ ADD RULE:POLICYTYPE=PCC, POLICYNAME=PCCPOLICYGRP ★ 计费规则（同一 FLOWFILTER，不同 RULENAME）
  → T-004/T-006 用户模板+刷新

[命令] T-AC-106 invokes → ADD RULE×2 (CMD-UDG-043)
  → constrained_by → CR-AC-02 POLICYTYPE=WEBPROXY → POLICYNAME 指向 IPFARM
  → constrained_by → TR-AC-06 WebProxy 双规则约束（WEBPROXY+PCC）
  → constrained_by → CR-AC-14 双轨可并存

[证据] CS-AC-05 → [EV-CA-AC-01, EV-FK-AC-07/08, EV-TK-AC-06]
  ADD IPFARM → [EV-FK-AC-10/11, EV-CA-D3]
```

> **双轨道+五子轨覆盖核查**：
> - 轨道 A（PCC 体系）：路径 A（PCC 阻塞）+ 路径 D（HEADEN）✅
> - 轨道 B-1（WEBPROXY/Portal）：补充链路（WebProxy）✅
> - 轨道 B-2（URL 过滤）：路径 B（URL 过滤，独立 CFTEMPLATE/CONTCATEGBIND.ACTION）✅
> - 轨道 C（SMARTREDIRECT）：路径 C（HTTP 重定向）+ 路径 A 中 DNS 纠错子链（共用 SMARTREDIRECT，POLICYNAME 区分）✅
> - 端到端 6-7 层穿透：BD → NS → CS → DP/BR/SO → Feature → Task → Command → Object，每条路径完整可溯源。

---

## §8. 跨层 refined_by 关系（8条）

> **Schema参考**：Schema §12.1~§12.4 定义了 `refined_by` 跨层精化关系：上层规则被下层规则具体化。
> **含义**：BusinessRule 的高层约束在 FeatureRule 和 TaskRule 中被精化为可执行的配置规则，TaskRule 进一步在 CommandRule 中体现为具体命令约束。

| 序号 | 上层规则 | 关系 | 下层规则 | 精化语义 |
|------|---------|------|---------|---------|
| 1 | `BR-AC-01`（预定义规则三网元一致性） | `refined_by` | `FR-AC-01`（跨 NF FlowFilter/RULENAME 一致性） | BR"三网元参数一致"→FR"RULENAME/appid/FlowFilterName 在 UDG+UNC+PCRF/PCF 三处一致；URL 过滤还需 Category ID 与 ICAP Server 一致；位置触发需 ULI 三处一致" |
| 2 | `BR-AC-07`（RULE.POLICYTYPE 决定动作轨道（双轨道+五子轨）） | `refined_by` | `FR-AC-02`（POLICYTYPE 决定动作轨道★双轨道+五子轨机制） | BR"POLICYTYPE 决定动作"→FR"ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY 五值路由 + 轨道 B URL 过滤独立 ACTION" |
| 3 | `BR-AC-07`（RULE.POLICYTYPE 决定动作轨道） | `refined_by` | `TR-AC-02`（POLICYTYPE 动作路由规则） | BR"POLICYTYPE 决定"→TR"T-003 通过 DP-AC-01 路由到 T-AC-101~108 独有 Task，操作不同 ConfigObject" |
| 4 | `BR-AC-06`（头防欺诈依赖头增强） | `refined_by` | `FR-AC-03`（头防欺诈强耦合依赖头增强） | BR"依赖"→FR"License 82209786+82209777 双开 + 共用 HEADEN 对象 + 执行顺序 + RTSP 例外" |
| 5 | `BR-AC-06`（头防欺诈依赖头增强） | `refined_by` | `CR-AC-04`（头防欺诈强依赖头增强 License 强耦合） | BR"依赖"→CR"ADD HEADEN.ANTIFRAUD=ENABLE 必须 License 双开；RTSP 场景无效" |
| 6 | `BR-AC-05`（REFRESHSRV 必须最后执行） | `refined_by` | `TR-AC-01`（REFRESHSRV 时序约束） | BR"最后执行"→TR"T-006 必须在所有 FILTER/FLOWFILTER/L7FILTER/EXTENDEDFILTER/RULE 之后执行，约 60 秒生效" |
| 7 | `BR-AC-05`（REFRESHSRV 必须最后执行） | `refined_by` | `CR-AC-12`（配置变更后必须 SET REFRESHSRV）+ `CR-AC-13`（REFRESHSRV 后 60 秒禁改 Filter） | BR"最后执行"→CR"FILTER/L7FILTER/RULE 变更后必须 SET REFRESHSRV；60 秒窗口期禁改 Filter" |
| 8 | `BR-AC-10`（PERMIT 唯一性，URL 过滤独有） | `refined_by` | `CR-AC-06`（URL 过滤 PERMIT 动作唯一性） | BR"PERMIT 唯一"→CR"仅 CFTEMPLATE.ACTION=PERMIT 或 CONTCATEGBIND.ACTION=PERMIT 显式支持；轨道 A 的'放行'是隐式（不匹配=放行）" |

> **覆盖范围**：以上 8 条覆盖了 BR→FR（3 条）、BR→TR（2 条）、BR→CR（3 条）三层 refined_by 关系。其余 BR（如 BR-AC-02 规则匹配类型独立、BR-AC-03 一条规则绑定一条策略、BR-AC-04 License 前置门控、BR-AC-08 字段加密约束、BR-AC-09 加密协议仅 WebProxy）作为独立高层约束存在，或通过 FR-AC-04/05/06/07/08 和 TR-AC-03/04/05/06/07/08 在下层有部分精化（详见 02 §5 和 03 §5）。

---

## §9. 禁止关系检查（§13 合规）

| 禁止关系（Schema §13） | 是否存在 | 说明 |
|---------|---------|------|
| `ConfigurationSolution -> ConfigObject` 直接绑定 | **无** | CS 通过 uses_feature → Feature → decomposes_to → Task → invokes → Command → operates_on 间接到达 ConfigObject |
| `ConfigurationSolution -> MMLCommand` 直接拥有 | **无** | CS 通过 uses_task → ConfigTask → invokes 间接调用 MMLCommand |
| `BusinessRule -> CommandParameter` 直接写死参数值 | **无** | BR 通过 DP.sets_value_pattern 间接影响参数（如 DP-AC-03 sets RULE.POLICYTYPE）；BR 的高层约束通过 refined_by 落到 FR/TR/CR |
| `Feature -> MMLCommand` 直接强绑定 | **无** | Feature 通过 decomposes_to → ConfigTask → invokes 间接调用命令 |
| `Feature -> ConfigObject` 携带参数差异 | **无** | Feature 的协议/字段差异通过 SemanticObject（SO-AC-01/04）或 FeatureRule（FR-AC-02/05/06/07）表达，非直接绑定 ConfigObject |
| 业务图谱内建 `ConfigObject` 实体 | **无** | ConfigObject 由任务层（targets）和命令层（operates_on）承接，业务层仅持有 SemanticObject |
| `ConfigurationSolution -> ConfigTask` 的完整顺序链 | **无** | 仅保留 `uses_task`（声明式集合），顺序由 FTOE（02 §6）和 TaskCommandOrderEdge（03 §7）承接 |

> **合规结论**：本图谱严格遵循 Schema §13 禁止关系约束，所有跨层连接通过标准关系边（uses_feature / uses_task / decomposes_to / invokes / operates_on / targets / selects / sets_value_pattern / refined_by）完成，无任何禁止关系违规。

---

## §10. 跨层边统计

| 跨层边 | 数量 |
|-------|------|
| CS `uses_feature` | 30（★ P5 批次 3：26+4 UNC 辅助） |
| CS `uses_task`（闭包级） | 9 |
| Feature `decomposes_to` ConfigTask | 19（★ P5 批次 3：15+4 UNC 辅助） |
| ConfigTask `invokes` MMLCommand | ~68（17 Task × 平均 4 命令，UDG 48 + UNC 20，★ P5 修正） |
| ConfigTask `targets` SO/ConfigObject | ~45 |
| DP `selects` CS/Task | 9 |
| DP `sets_value_pattern` | 6 |
| BR/TR `refined_by` FR/TR/CR | 8 |
| **跨层边总计** | **~194**（★ P5 批次 3：uses_feature +4、decomposes_to +4、invokes 62→68） |

---

## §11. 与计费/带宽控制场景跨层映射的对比

| 维度 | 计费场景 | 带宽控制场景 | 访问限制场景 |
|------|---------|------------|------------|
| CS uses_feature 边数 | 20 | 25 | **30**（★ P5 批次 3：26+4 UNC 辅助） |
| CS uses_task 边数 | 7 | 7 | **9** |
| Feature decomposes_to 边数 | 14 | 24 | **19**（★ P5 批次 3：15+4 UNC 辅助） |
| ConfigTask invokes 边数 | ~50 | ~50 | **~68**（P5 修正） |
| ConfigTask targets 边数 | ~28 | ~30 | **~45** |
| DP selects 边数 | 3 | 4 | **9** |
| DP sets_value_pattern 边数 | 3 | 3 | **6** |
| refined_by 边数 | 5 | 6 | **8** |
| 跨层边总计 | ~130 | ~149 | **~194**（P5 批次 3：uses_feature +4、decomposes_to +4、invokes 62→68） |
| 核心路径数 | 6 | 3 | **4（覆盖双轨道+五子轨）+1 补充（WebProxy）** |
| 共享机制 | URR 三件套（计费→差异化费率） | URR 三件套（FUP→流量阈值监控） | **RULE.POLICYTYPE 双轨道+五子轨路由（ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY）+ 轨道 B CFTEMPLATE.ACTION** |
| 独有跨层链 | 在线 DCC 链(T-201~T-204), 融合 18 步链(T-301~T-310) | BWM 三级控制(101~106), ADC 三策略组(401~402), QoS 专载(301~303) | **头增强+防欺诈强耦合(T-AC-102)**, **SMARTREDIRECT 双子类型共用(T-AC-103/104)**, **IPFarm 集群 Portal/WebProxy 共用(T-AC-105/106)**, **URL 过滤 ICAP+CF 独立链(T-AC-108)**, **UNC 侧位置触发(T-AC-109)** |
| POLICYTYPE | 固定 CHARGING | 动态 BWM/PCC/QOS/ADC（由 DP-BW-01 决策） | **动态 ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY 五值（由 DP-AC-01/03 路由，双轨道+五子轨核心）** |
| 端到端差异 | 路径覆盖离线/在线/融合/内容计费/配额降速/兜底 | 路径覆盖 BWM 限速/FUP 降速/ADC 应用感知 | **路径覆盖 PCC 阻塞/URL 过滤/HTTP 重定向/头增强 + WebProxy 补充（五子轨+1）** |

> 三场景共享部分通用 Task 链（T-001~T-008、T-003 PCC 规则、T-005 绑定链），但 POLICYTYPE 分支不同：计费用 CHARGING，带宽用 BWM/PCC/QOS/ADC，**访问限制用 ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY 五值（最丰富）**。
> RULE 跨场景复用但 POLICYTYPE 取值语义完全不同：计费用于费率区分，带宽用于控制机制区分，**访问限制用于动作类型区分（双轨道+五子轨核心架构）**。
> URR 跨场景复用：计费用于计费属性，带宽用于 FUP 阈值监控，**访问限制用于 ADC/Portal/WebProxy/URL 过滤的计费属性绑定（非主用途）**。

---

## §12. 跨层一致性检查清单

- [x] 所有 CS 的 uses_feature 指向真实存在的 Feature（19 个：UDG 11 + UNC 8 含 4 个 UNC 接入控制辅助特性，★ P5 批次 3 U-H-02 跨文件同步完成）
- [x] 所有 Feature 的 decomposes_to 指向真实存在的 ConfigTask（17 个：8 generic + 9 独有）
- [x] 所有 ConfigTask 的 invokes 指向真实存在的 MMLCommand（68 个：UDG 48 + UNC 20，★ P5 修正计数）
- [x] 所有 MMLCommand 的 operates_on 指向真实存在的 ConfigObject（41 个：共享 18 + 独有 23）
- [x] 所有 ConfigTask 的 targets 指向真实存在的 SemanticObject（7 个）或 ConfigObject
- [x] 所有 DP 的 selects 指向真实存在的 CS（9 个）或 Task（17 个）
- [x] 所有 DP 的 sets_value_pattern 指向真实存在的 CommandParameter 或对象（RULE.POLICYTYPE / CFTEMPLATE.ACTION 等）
- [x] 路径 A~D 端到端完整：BD → NS → CS → Feature → Task → Command → Object，每条路径带 EV 溯源
- [x] ★ DP-AC-03 动作轨道选择的 sets_value_pattern 体现 RULE.POLICYTYPE 双轨道+五子轨机制
- [x] ★ 端到端链路覆盖双轨道+五子轨（轨道 A 五子轨：PCC/HEADEN/SMARTREDIRECT/WEBPROXY/ADC + 轨道 B：URL 过滤独立）
- [x] 无 §13 禁止关系（CS→ConfigObject / Feature→MMLCommand / BR→CommandParameter 等全部通过中间层间接到达）
- [x] **★ P5 新增（U-M-07/F05）**：§1 CS→Feature、§3 Feature→Task 映射表补 `source_evidence_ids` 列，每条跨层边溯源到 EV-CA-AC-01 + 特性 EV-FK-AC-NN + 附录 D 子证据 EV-CA-D1~D4
- [x] **★ P5 新增（EV ID 统一）**：§7 端到端链路的 EV ID 全部采用序号主形式（EV-FK-AC-01~19 + EV-CA-AC-01 + EV-CA-D1~D4），原特性编号别名弃用
- [x] **★ P5 批次 3 新增（U-H-02 跨文件闭环）**：§1 CS-AC-07 的 4 条 UNC 辅助特性边 EV ID 修正为 EV-FK-AC-16~19；§3 补 4 条 decomposes_to 边；CS-AC-07 → 4 个 UNC 辅助特性 → UNC 侧 Task 骨架（T-005/T-AC-109）链路闭环

---

> 本文件为访问限制场景三层图谱第 5 层。第 6 层证据索引见同目录其他文件。
> **核心架构发现**：访问限制场景的跨层映射体现了"**双轨道动作机制（轨道A 五子轨 POLICYTYPE 路由 + 轨道B CFTEMPLATE.ACTION）**"——轨道 A（PCC 体系）通过 RULE.POLICYTYPE 隐式驱动 ADC/PCC/HEADEN/SMARTREDIRECT/WEBPROXY 五种动作类型，轨道 B（URL 过滤体系）通过 CFTEMPLATE/CONTCATEGBIND.ACTION 显式驱动 BLOCK/PERMIT/REDIRECT（唯一显式 PERMIT）。DP-AC-03 的 sets_value_pattern RULE.POLICYTYPE 是这一架构的决策入口。
