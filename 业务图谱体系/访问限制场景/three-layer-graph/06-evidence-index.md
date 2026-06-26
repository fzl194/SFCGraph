# 访问限制场景三层图谱 · 第6层：证据层索引

> **文件定位**：`three-layer-graph/06-evidence-index.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §8.11 EvidenceSource（字段：evidence_id, evidence_type, title, path, source_system, status）
> **作用**：为本场景三层图谱所有对象的 `source_evidence_ids` 字段提供可追溯的证据源注册表。每个图谱对象引用本表中的 `evidence_id`，即可通过本表回溯到原始知识文档。

---

## §0 命名约定（★权威，先读此节）

### 0.1 Evidence ID 主编号方案

访问限制场景三层图谱采用 **双层 Evidence ID 体系**，以 `EV-FK-AC-NN`（NN=01~19）为**权威主 ID**，与 `02-feature-graph.md` §0.4 声明完全一致：

| 主 ID（权威） | 别名（04-command-graph.md 使用） | 特性 ID | 特性名 | 知识文档 |
|--------------|-------------------------------|---------|--------|---------|
| `EV-FK-AC-01` | `EV-FK-AC-110101` | GWFD-110101 | SA-Basic（三场景共享） | 复用计费/带宽场景 |
| `EV-FK-AC-02` | `EV-FK-AC-020351` | GWFD-020351 | PCC基本功能（UDG，三场景共享） | 复用计费/带宽场景 |
| `EV-FK-AC-03` | `EV-FK-AC-109101` | WSFD-109101 | PCC基本功能（UNC，三场景共享） | 复用计费/带宽场景 |
| `EV-FK-AC-04` | `EV-FK-AC-020357` | GWFD-020357 | 增强的ADC基本功能（UDG） | `feature-knowledge/GWFD-020357-增强的ADC基本功能.md` |
| `EV-FK-AC-05` | —（04 未直接引用） | WSFD-109102 | ADC基本功能（UNC，三场景共享） | 复用计费/带宽场景 |
| `EV-FK-AC-06` | `EV-FK-AC-110261` | GWFD-110261 | HTTP头增强 | `feature-knowledge/GWFD-110261-HTTP头增强.md` |
| `EV-FK-AC-07` | `EV-FK-AC-110262` | GWFD-110262 | RTSP头增强 | `feature-knowledge/GWFD-110262-RTSP头增强.md` |
| `EV-FK-AC-08` | `EV-FK-AC-110263` | GWFD-110263 | HTTPS头增强 | `feature-knowledge/GWFD-110263-HTTPS头增强.md` |
| `EV-FK-AC-09` | `EV-FK-AC-110401` | GWFD-110401 | HTTP头防欺诈 | `feature-knowledge/GWFD-110401-HTTP头防欺诈.md` |
| `EV-FK-AC-10` | `EV-FK-AC-110281` | GWFD-110281 | 用户Portal | `feature-knowledge/GWFD-110281-用户Portal.md` |
| `EV-FK-AC-11` | `EV-FK-AC-110282` | GWFD-110282 | WebProxy | `feature-knowledge/GWFD-110282-WebProxy.md` |
| `EV-FK-AC-12` | `EV-FK-AC-110283` | GWFD-110283 | DNS纠错 | `feature-knowledge/GWFD-110283-DNS纠错.md` |
| `EV-FK-AC-13` | `EV-FK-AC-110284` | GWFD-110284 | HTTP智能重定向 | `feature-knowledge/GWFD-110284-HTTP智能重定向.md` |
| `EV-FK-AC-14` | `EV-FK-AC-110471` | GWFD-110471 | URL过滤基本功能 | `feature-knowledge/GWFD-110471-URL过滤基本功能.md` |
| `EV-FK-AC-15` | `EV-FK-AC-211001` | WSFD-211001 | 基于初始接入位置的策略控制（UNC） | `feature-knowledge/WSFD-211001-基于初始接入位置的策略控制.md` |
| `EV-FK-AC-16` | —（★ P5 批次 3 新增） | WSFD-106003 | 用户接入控制（AMF，SAR 服务区限制） | `cross-topic-analysis.md` §6.3 CS-AC-07（暂未独立建档） |
| `EV-FK-AC-17` | —（★ P5 批次 3 新增） | WSFD-105003 | 区域漫游限制（AMF） | `cross-topic-analysis.md` §6.3（暂未独立建档） |
| `EV-FK-AC-18` | —（★ P5 批次 3 新增） | WSFD-106005 | 支持 ODB（AMF） | `cross-topic-analysis.md` §6.3（暂未独立建档） |
| `EV-FK-AC-19` | —（★ P5 批次 3 新增） | WSFD-105006 | 会话服务区域限制（SMF） | `cross-topic-analysis.md` §6.3（暂未独立建档） |

### 0.2 跨场景共享编号（复用特性第二别名）

4 个复用特性同时沿用带宽控制场景的跨场景共享编号（与 `02-feature-graph.md` §0.4 一致）：

| 访问限制主 ID | 跨场景共享编号 | 说明 |
|--------------|--------------|------|
| `EV-FK-AC-01` | `EV-FK-01` | SA-Basic（GWFD-110101） |
| `EV-FK-AC-02` | `EV-FK-03` | PCC-UDG（GWFD-020351） |
| `EV-FK-AC-03` | `EV-FK-17` | PCC-UNC（WSFD-109101） |
| `EV-FK-AC-05` | `EV-FK-21` | ADC-UNC（WSFD-109102） |

### 0.3 横向分析证据别名

| 主 ID | 别名 | 说明 |
|------|------|------|
| `EV-CA-AC-01` | `EV-FK-AC-CFA`、`EV-CA-01` | `04-command-graph.md` 使用 `EV-FK-AC-CFA`；`02/03` 使用 `EV-CA-01` 作为简写。三者指向同一份 `cross-feature-analysis.md` |
| `EV-CA-AC-02` | — | `cross-topic-analysis.md`（无别名） |

> **引用一致性原则**：本索引同时注册主 ID 与全部别名，图谱对象无论使用哪种形式，都能在本表中命中。后续图谱演进建议统一到 `EV-FK-AC-NN` / `EV-CA-AC-NN` 主形式。

---

## §1 EvidenceSource 总览

访问限制场景三层图谱的证据源共分五类，合计 **35份知识资产**（按主 ID 计；别名不重复计数；EV-CA-D1~D4 为附录 D 子证据，独立计数；★ P5 批次 3 新增 EV-FK-AC-16~19 共 4 份 UNC 接入控制辅助特性证据）：

| 证据类型 | ID前缀 | 数量 | `evidence_type` | `status` | 路径根目录 |
|---------|--------|------|-----------------|----------|-----------|
| 特性知识文档 | `EV-FK-AC-*` | 19 | markdown | active | `feature-knowledge/`（11 独有）+ 复用（4 共享）+ UNC 接入控制辅助（4，★ P5 批次 3，暂锚定 cross-topic-analysis.md §6.3） |
| 主题知识批次 | `EV-TK-AC-*` | 8 | markdown | active | `topic-knowledge/` |
| 跨特性/跨主题分析 | `EV-CA-AC-*` | 2 | markdown | active | `feature-knowledge/cross-feature-analysis.md`、`cross-topic-analysis.md` |
| 附录 D 端到端流程子证据 | `EV-CA-D*` | 4 | markdown | active | `feature-knowledge/cross-feature-analysis.md#附录D`（EV-CA-AC-01 的子证据） |
| 场景级原始材料 | `EV-BS-AC-*` | 2 | markdown | active | `访问限制场景doc-list.md`、`访问限制场景feature-doc-list.md` |
| **合计** | — | **35** | — | — | — |

> 所有证据路径相对本场景目录（`业务图谱体系/访问限制场景/`）。

---

## §2 特性知识证据（EV-FK-AC-*，19份）

来源：19 个特性（11 独有 + 4 复用共享 + 4 UNC 接入控制辅助）。11 个独有特性各产出一份 APN 标杆水平知识文档；4 个复用特性沿用计费/带宽场景的知识文档，本场景未重复产出；4 个 UNC 接入控制辅助特性（★ P5 批次 3 新增 EV-FK-AC-16~19，U-H-02 关联）暂未独立建档，锚定到 `cross-topic-analysis.md` §6.3 CS-AC-07 章节。

### 2.1 业务感知层与 PCC 骨架层（复用共享，4份）

| Evidence ID | 别名 | evidence_type | title | path | source_system | status | 复用说明 |
|------------|------|---------------|-------|------|--------------|--------|---------|
| `EV-FK-AC-01` | `EV-FK-AC-110101`、`EV-FK-01` | markdown | GWFD-110101 SA-Basic（业务感知基本功能） | 复用计费/带宽场景 `feature-knowledge/`（三场景共享） | feature-knowledge/ | active | 三场景共享，知识文档复用计费场景 EV-FK-01 |
| `EV-FK-AC-02` | `EV-FK-AC-020351`、`EV-FK-03` | markdown | GWFD-020351 PCC基本功能（UDG） | 复用计费/带宽场景 `feature-knowledge/`（三场景共享） | feature-knowledge/ | active | 三场景共享，知识文档复用计费场景 EV-FK-03 |
| `EV-FK-AC-03` | `EV-FK-AC-109101`、`EV-FK-17` | markdown | WSFD-109101 PCC基本功能（UNC） | 复用计费/带宽场景 `feature-knowledge/`（三场景共享） | feature-knowledge/ | active | 三场景共享，知识文档复用计费场景 EV-FK-17 |
| `EV-FK-AC-05` | `EV-FK-21` | markdown | WSFD-109102 ADC基本功能（UNC） | 复用计费/带宽场景 `feature-knowledge/`（三场景共享） | feature-knowledge/ | active | 三场景共享，知识文档复用计费场景 EV-FK-21 |

### 2.2 ADC 应用检测层（UDG 独有，1份）

| Evidence ID | 别名 | evidence_type | title | path | source_system | status |
|------------|------|---------------|-------|------|--------------|--------|
| `EV-FK-AC-04` | `EV-FK-AC-020357` | markdown | GWFD-020357 增强的ADC基本功能（UDG） | `feature-knowledge/GWFD-020357-增强的ADC基本功能.md` | feature-knowledge/ | active |

### 2.3 头增强族（UDG 独有，3份）

| Evidence ID | 别名 | evidence_type | title | path | source_system | status |
|------------|------|---------------|-------|------|--------------|--------|
| `EV-FK-AC-06` | `EV-FK-AC-110261` | markdown | GWFD-110261 HTTP头增强 | `feature-knowledge/GWFD-110261-HTTP头增强.md` | feature-knowledge/ | active |
| `EV-FK-AC-07` | `EV-FK-AC-110262` | markdown | GWFD-110262 RTSP头增强 | `feature-knowledge/GWFD-110262-RTSP头增强.md` | feature-knowledge/ | active |
| `EV-FK-AC-08` | `EV-FK-AC-110263` | markdown | GWFD-110263 HTTPS头增强 | `feature-knowledge/GWFD-110263-HTTPS头增强.md` | feature-knowledge/ | active |

### 2.4 防欺诈层（UDG 独有，1份）

| Evidence ID | 别名 | evidence_type | title | path | source_system | status |
|------------|------|---------------|-------|------|--------------|--------|
| `EV-FK-AC-09` | `EV-FK-AC-110401` | markdown | GWFD-110401 HTTP头防欺诈 | `feature-knowledge/GWFD-110401-HTTP头防欺诈.md` | feature-knowledge/ | active |

### 2.5 重定向族（UDG 独有，4份）

| Evidence ID | 别名 | evidence_type | title | path | source_system | status |
|------------|------|---------------|-------|------|--------------|--------|
| `EV-FK-AC-10` | `EV-FK-AC-110281` | markdown | GWFD-110281 用户Portal | `feature-knowledge/GWFD-110281-用户Portal.md` | feature-knowledge/ | active |
| `EV-FK-AC-11` | `EV-FK-AC-110282` | markdown | GWFD-110282 WebProxy | `feature-knowledge/GWFD-110282-WebProxy.md` | feature-knowledge/ | active |
| `EV-FK-AC-12` | `EV-FK-AC-110283` | markdown | GWFD-110283 DNS纠错 | `feature-knowledge/GWFD-110283-DNS纠错.md` | feature-knowledge/ | active |
| `EV-FK-AC-13` | `EV-FK-AC-110284` | markdown | GWFD-110284 HTTP智能重定向 | `feature-knowledge/GWFD-110284-HTTP智能重定向.md` | feature-knowledge/ | active |

### 2.6 URL 内容过滤层（UDG 独有，1份）

| Evidence ID | 别名 | evidence_type | title | path | source_system | status |
|------------|------|---------------|-------|------|--------------|--------|
| `EV-FK-AC-14` | `EV-FK-AC-110471` | markdown | GWFD-110471 URL过滤基本功能 | `feature-knowledge/GWFD-110471-URL过滤基本功能.md` | feature-knowledge/ | active |

### 2.7 接入控制触发层（UNC 独有，1份）

| Evidence ID | 别名 | evidence_type | title | path | source_system | status |
|------------|------|---------------|-------|------|--------------|--------|
| `EV-FK-AC-15` | `EV-FK-AC-211001` | markdown | WSFD-211001 基于初始接入位置的策略控制 | `feature-knowledge/WSFD-211001-基于初始接入位置的策略控制.md` | feature-knowledge/ | active |

### 2.8 UNC 接入控制辅助特性层（UNC 独有，4 份，★ P5 批次 3 新增）

> **注册背景（U-H-02 关联，P5 批次 3 闭环）**：`02-feature-graph.md` §1.9 新增实例化的 4 个 UNC 接入控制辅助特性（WSFD-106003/105003/106005/105006），在 P5 批次 1 时 `source_evidence_ids` 暂用 `EV-CA-AC-02`（cross-topic-analysis.md）占位。批次 3 为其分配独立 `EV-FK-AC-16~19` 并在本表正式注册，锚定到 `cross-topic-analysis.md` §6.3 CS-AC-07 章节（该章节是当前 4 个特性的唯一综合知识源）；后续若为 4 个特性单独建档（feature-knowledge/WSFD-XXXXXX.md），应将 path 字段更新为独立文档路径。

| Evidence ID | 别名 | evidence_type | title | path | source_system | status | 说明 |
|------------|------|---------------|-------|------|--------------|--------|------|
| `EV-FK-AC-16` | — | markdown | WSFD-106003 用户接入控制（AMF，SAR 服务区限制） | `cross-topic-analysis.md#§6.3-CS-AC-07` | （场景根目录） | active | AMF 注册阶段 SAR 准入决策（TAI 允许/禁止列表）、ULI 上报 |
| `EV-FK-AC-17` | — | markdown | WSFD-105003 区域漫游限制（AMF） | `cross-topic-analysis.md#§6.3-CS-AC-07` | （场景根目录） | active | PLMN/号段/ODB 漫游准入（区域套餐、漫游限制、出国引导） |
| `EV-FK-AC-18` | — | markdown | WSFD-106005 支持 ODB（AMF） | `cross-topic-analysis.md#§6.3-CS-AC-07` | （场景根目录） | active | ODB（运营商决定闭锁），欠费禁用、拥塞小区流控，跨注册/会话两阶段 |
| `EV-FK-AC-19` | — | markdown | WSFD-105006 会话服务区域限制（SMF） | `cross-topic-analysis.md#§6.3-CS-AC-07` | （场景根目录） | active | SMF 侧基于签约 SAR/Tracking Area 的会话级区域限制（释放/限速/重定向） |

### 2.9 特性知识证据分组汇总

| 特性分组 | Evidence IDs（主形式） | 数量 |
|---------|----------------------|------|
| 业务感知层（复用） | EV-FK-AC-01 | 1 |
| PCC骨架层（复用） | EV-FK-AC-02, EV-FK-AC-03 | 2 |
| ADC应用检测层 | EV-FK-AC-04（UDG独有）, EV-FK-AC-05（UNC复用） | 2 |
| 头增强族 | EV-FK-AC-06, EV-FK-AC-07, EV-FK-AC-08 | 3 |
| 防欺诈层 | EV-FK-AC-09 | 1 |
| 重定向族 | EV-FK-AC-10, EV-FK-AC-11, EV-FK-AC-12, EV-FK-AC-13 | 4 |
| URL内容过滤层 | EV-FK-AC-14 | 1 |
| 接入控制触发层 | EV-FK-AC-15 | 1 |
| **UNC 接入控制辅助层（★ P5 批次 3 新增）** | **EV-FK-AC-16, EV-FK-AC-17, EV-FK-AC-18, EV-FK-AC-19** | **4** |
| **合计** | — | **19** |

---

## §3 主题知识证据（EV-TK-AC-*，8份）

来源：访问限制场景源文档按 `(产品, 主题)` 切分为 8 批次后产出的综合知识，合计 2303 行。

| Evidence ID | 批次 | 主题 | evidence_type | title | path | source_system | status | 规模 |
|------------|------|------|---------------|-------|------|--------------|--------|------|
| `EV-TK-AC-01` | Batch-01 | 业务感知基础 | markdown | 业务感知基础 | `topic-knowledge/Batch-01-业务感知基础.md` | topic-knowledge/ | active | 221 行 |
| `EV-TK-AC-02` | Batch-02 | PCC基本功能 | markdown | PCC基本功能 | `topic-knowledge/Batch-02-PCC基本功能.md` | topic-knowledge/ | active | 414 行 |
| `EV-TK-AC-03` | Batch-03 | PCC-SM策略下发 | markdown | PCC-SM策略下发 | `topic-knowledge/Batch-03-PCC-SM策略下发.md` | topic-knowledge/ | active | 409 行 |
| `EV-TK-AC-04` | Batch-04 | ADC核心 | markdown | ADC核心 | `topic-knowledge/Batch-04-ADC核心.md` | topic-knowledge/ | active | 192 行 |
| `EV-TK-AC-05` | Batch-05 | 头增强 | markdown | 头增强 | `topic-knowledge/Batch-05-头增强.md` | topic-knowledge/ | active | 231 行 |
| `EV-TK-AC-06` | Batch-06 | 重定向族 | markdown | 重定向族 | `topic-knowledge/Batch-06-重定向族.md` | topic-knowledge/ | active | 263 行 |
| `EV-TK-AC-07` | Batch-07 | URL过滤与接入控制 | markdown | URL过滤与接入控制 | `topic-knowledge/Batch-07-URL过滤与接入控制.md` | topic-knowledge/ | active | 321 行 |
| `EV-TK-AC-08` | Batch-08 | 防欺诈 | markdown | 防欺诈 | `topic-knowledge/Batch-08-防欺诈.md` | topic-knowledge/ | active | 252 行 |

> ★ 核心证据：EV-TK-AC-07（URL过滤与接入控制，321 行）和 EV-TK-AC-06（重定向族，263 行）是构建业务层 ConfigurationSolution 的关键来源，覆盖访问限制场景两大核心动作链。

---

## §4 跨特性/跨主题分析证据（EV-CA-AC-*，2份）

| Evidence ID | 别名 | evidence_type | title | path | source_system | status | 规模 | 关键章节 |
|------------|------|---------------|-------|------|--------------|--------|------|---------|
| `EV-CA-AC-01` | `EV-FK-AC-CFA`、`EV-CA-01` | markdown | 访问限制场景跨特性分析 | `feature-knowledge/cross-feature-analysis.md` | feature-knowledge/ | active | 1602 行 | §1 分类；§3 配置差异；§4 依赖；§5 关键发现；附录 A 15特性索引；附录 B MML命令；附录 C 配置对象；附录 D 端到端流程 |
| `EV-CA-AC-02` | — | markdown | 访问限制场景跨主题分析 | `cross-topic-analysis.md` | （场景根目录） | active | 1558 行 | §1 场景定位；§4 核心链路；§6 维度归纳；§7 策略体系；§8 场景归并；附录 冲突矩阵 |

### 4.1 跨层分析与图谱层的映射

| 图谱层 | 主要引用证据 |
|-------|------------|
| 第1层 业务图谱（CS/DP/BR） | EV-CA-AC-02（§4/§6/§8）+ EV-TK-AC-06/07 |
| 第2层 特性图谱（Feature依赖/License） | EV-CA-AC-01（§4 依赖图/附录A）+ EV-FK-AC-* |
| 第3层 任务原子层（Task/OrderEdge） | EV-CA-D1~D4（附录D 四类端到端流程）+ EV-FK-AC-* |
| 第4层 命令图谱（Command/Object/Rule） | EV-CA-AC-01（附录B/C）+ EV-FK-AC-*（特性命令详表） |
| 第5层 跨层映射 | EV-CA-AC-01 + EV-CA-AC-02 + EV-CA-D1~D4（综合引用） |

### 4.2 附录 D 端到端流程子证据（EV-CA-D1~D4，4份，★ P5 新增注册）

> **注册背景**：`03-task-layer.md` §7/§8 的 TaskCommandOrderEdge（合计 59 条）和 `05-cross-layer-mapping.md` §7 端到端链路示例大量引用 `EV-CA-D1~D4`（合计 67 处），此前仅在 F03 §0.4 以说明文字描述，未按 Schema §8.11 注册为独立 EvidenceSource。P5 修复（U-H-03）补齐注册，作为 `EV-CA-AC-01` 的附录 D 子证据，path 锚定到具体子节。

| Evidence ID | parent_evidence_id | evidence_type | title | path | source_system | status | 覆盖场景 | 被引用情况 |
|------------|-------------------|---------------|-------|------|--------------|--------|---------|-----------|
| `EV-CA-D1` | `EV-CA-AC-01` | markdown | 附录 D.1 DISCARD 兜底阻塞端到端流程 | `feature-knowledge/cross-feature-analysis.md#附录D.1` | feature-knowledge/ | active | ADC 兜底阻塞 / PCC 显式阻塞 / URL 过滤 BLOCK（轨道 A 阻塞 + 轨道 B ICAP 互通前置） | 03 §7.1/§7.7/§8.1（22 处）+ 05 §7.1/§7.2 |
| `EV-CA-D2` | `EV-CA-AC-01` | markdown | 附录 D.2 HEADEN 头增强端到端流程 | `feature-knowledge/cross-feature-analysis.md#附录D.2` | feature-knowledge/ | active | HTTP/HTTPS/RTSP 头增强 + 头防欺诈强耦合子模式（License 双开 + 执行顺序） | 03 §7.2/§8.2（8 处）+ 05 §7.4 |
| `EV-CA-D3` | `EV-CA-AC-01` | markdown | 附录 D.3 REDIRECT 重定向族端到端流程 | `feature-knowledge/cross-feature-analysis.md#附录D.3` | feature-knowledge/ | active | HTTP 智能重定向 / DNS 纠错 / 用户 Portal captive / WebProxy 双规则 | 03 §7.3~§7.6/§8.3（31 处）+ 05 §7.3/§7.5 |
| `EV-CA-D4` | `EV-CA-AC-01` | markdown | 附录 D.4 接入控制触发端到端流程 | `feature-knowledge/cross-feature-analysis.md#附录D.4` | feature-knowledge/ | active | UNC 侧位置条件策略（USRLOCATION + USRLOCATIONGRP + UPBINDUPG） | 03 §7.8/§8.4（6 处）+ 05 §7.1 UNC 侧补充链 |

> **字段说明**：`parent_evidence_id=EV-CA-AC-01` 表明这 4 个子证据是 `cross-feature-analysis.md` 附录 D 的四个子节，与父证据同源同文件，仅为提升溯源粒度而独立注册。Schema §8.11 EvidenceSource 核心字段（evidence_id, evidence_type, title, path, source_system, status）全部具备；`parent_evidence_id` 为扩展字段，标注父子层级。
> **引用计数**：67 处（22 + 8 + 31 + 6），分布在 03 §7/§8 与 05 §7。注册后 F03/F05 的 `source_evidence_ids` 中所有 `EV-CA-D1~D4` 均可命中本表，追溯断链消除。

---

## §5 场景级原始材料证据（EV-BS-AC-*，2份）

访问限制场景的业务图谱直接以三层图谱形式产出（无独立 md），EV-BS-AC-* 登记本场景的原始材料清单与特性文档清单，作为图谱构建的源头治理依据。

| Evidence ID | evidence_type | title | path | source_system | status | 规模 | 说明 |
|------------|---------------|-------|------|--------------|--------|------|------|
| `EV-BS-AC-01` | markdown | 访问限制场景文档清单 | `访问限制场景doc-list.md` | （场景根目录） | active | 7482 字节 | 场景全部源文档清单，P0 修订后权威版 |
| `EV-BS-AC-02` | markdown | 访问限制场景特性文档清单 | `访问限制场景feature-doc-list.md` | （场景根目录） | active | 6581 字节 | 15 特性（11独有+4复用）的源文档映射清单（注：U-H-02 新补 4 个 UNC 接入控制辅助特性由 cross-topic-analysis §6.3 承载，未单独列入此清单） |

> 访问限制场景未像计费场景那样产出独立的 `01业务图谱.md` 散件，业务层直接以三层图谱第1层（`three-layer-graph/01-business-graph.md`）形式产出，故不单独注册业务图谱散件证据。

---

## §6 引用一致性核查（★核心质量门禁）

### 6.1 被引用的 EV ID 集合（扫描 01~05 图谱文件）

扫描 `01-business-graph.md`、`02-feature-graph.md`、`03-task-layer.md`、`04-command-graph.md`、`05-cross-layer-mapping.md` 的所有 `source_evidence_ids` 字段，提取被引用的 EV ID 集合（已去重，排除 `EV-FK-AC-*`、`EV-FK-AC-NN` 占位符形式）：

| 引用形式 | 出处 | 本表注册状态 |
|---------|------|------------|
| `EV-FK-AC-01` ~ `EV-FK-AC-15` | 01/02/03/04 主用 | 已注册（§2 主 ID） |
| **`EV-FK-AC-16` ~ `EV-FK-AC-19`** | **02 §1.9（4 个 UNC 辅助特性实例化）+ 05 §1/§3（跨层映射）** | **★ P5 批次 3 新增注册（§2.8，U-H-02 跨文件闭环）** |
| `EV-FK-AC-110101`、`EV-FK-AC-020351`、`EV-FK-AC-109101`、`EV-FK-AC-020357`、`EV-FK-AC-110261`、`EV-FK-AC-110262`、`EV-FK-AC-110263`、`EV-FK-AC-110281`、`EV-FK-AC-110282`、`EV-FK-AC-110283`、`EV-FK-AC-110284`、`EV-FK-AC-110401`、`EV-FK-AC-110471`、`EV-FK-AC-211001` | 04（P5 后已统一为序号主形式） | 已注册为别名（§0.1 + §2） |
| `EV-FK-AC-CFA` | 04（20处，P5 后已统一为 EV-CA-AC-01） | 已注册为 EV-CA-AC-01 的别名（§0.3） |
| `EV-CA-01` | 02/03 简写 | 已注册为 EV-CA-AC-01 的别名（§0.3） |
| `EV-CA-AC-01` | 01/04/05 | 已注册（§4 主 ID） |
| `EV-CA-AC-02` | 01（02 §1.9 的 4 个 UNC 辅助特性 P5 批次 1 曾作占位引用，批次 3 已替换为 EV-FK-AC-16~19） | 已注册（§4 主 ID） |
| **`EV-CA-D1` ~ `EV-CA-D4`** | **03 §7/§8（59 边）+ 05 §7（8 处），合计 67 处** | **★ P5 批次 2 新增注册（§4.2）** |
| `EV-TK-AC-01` ~ `EV-TK-AC-08` | 01 主用 | 已注册（§3 主 ID） |

### 6.2 核查结论

| 核查项 | 结果 |
|-------|------|
| 被引用 EV ID 数（去重，主形式） | 19 EV-FK-AC（含 16~19，★ P5 批次 3）+ 8 EV-TK-AC + 2 EV-CA-AC + 4 EV-CA-D = **33** |
| 本表注册 EV ID 数（主形式） | 19 EV-FK-AC + 8 EV-TK-AC + 2 EV-CA-AC + 4 EV-CA-D + 2 EV-BS-AC = **35** |
| 被引用 ⊆ 已注册 | **通过**（★ P5 批次 2 后含 EV-CA-D1~D4 的 67 处引用全部命中；批次 3 后含 EV-FK-AC-16~19 的 4 个 UNC 辅助特性引用全部命中，追溯断链消除） |
| 已注册但未被引用 | `EV-BS-AC-01`、`EV-BS-AC-02`（场景级原始材料，作为源头治理依据注册，图谱对象未直接引用，属预期） |
| 别名覆盖 | **通过**（04 使用的 14 个特性编号别名 + `EV-FK-AC-CFA` + `EV-CA-01` 简写均已覆盖；4 个 UNC 辅助特性无别名） |
| 占位符清理 | 01-03 中出现的 `EV-FK-AC-NN`、`EV-TK-AC-NN` 为说明性占位（非实际引用），已在各自文件 §0 说明，本表无需注册；02 §1.9 原 `EV-CA-AC-02` 占位（4 个 UNC 辅助特性）已于 P5 批次 3 替换为 `EV-FK-AC-16~19` |

### 6.3 命名异类说明

> **命名异类已修复**：P5 修复前 `04-command-graph.md` 使用 `EV-FK-AC-XXXXXX`（特性编号）形式，与 02 声明的 `EV-FK-AC-NN`（序号）权威形式不一致；P5 已全局统一 04 到序号主形式（按 §0.1 映射表，约 80 处替换），本索引别名表保留仅为向后兼容说明。三场景合并时建议统一为 `EV-FK-{场景}-NN`（如 `EV-FK-AC-NN`），访问限制的 XXXXXX 别名形式已弃用。

---

## §7 证据使用规范

### 7.1 图谱对象引用证据的方式

每个图谱对象的 `source_evidence_ids` 字段填写本表中的 `evidence_id`，遵循以下规范：

```yaml
# 业务层对象示例（ConfigurationSolution）
- id: CS-AC-01
  type: ConfigurationSolution
  source_evidence_ids:
    - EV-CA-AC-01        # 跨特性分析附录D端到端流程
    - EV-CA-AC-02        # 跨主题分析§4核心链路
    - EV-FK-AC-14        # GWFD-110471 URL过滤特性
    - EV-TK-AC-07        # Batch-07 URL过滤与接入控制

# 特性层对象示例（Feature）
- id: GWFD-110471
  type: Feature
  source_evidence_ids:
    - EV-FK-AC-14        # 特性专属证据（必填，主形式）
    - EV-CA-AC-01        # 跨特性分析§4依赖图

# 命令层对象示例（MMLCommand）—— 04 可沿用特性编号别名
- id: CMD-UDG-043
  type: MMLCommand
  source_evidence_ids:
    - EV-FK-AC-020357    # ADC UDG（等价于主形式 EV-FK-AC-04）
    - EV-FK-AC-110261    # HTTP头增强（等价于主形式 EV-FK-AC-06）
    - EV-FK-AC-110284    # HTTP智能重定向（等价于主形式 EV-FK-AC-13）
    - EV-FK-AC-CFA       # 跨特性分析（等价于主形式 EV-CA-AC-01）
```

### 7.2 证据强度等级（参考 Schema §8.11）

| 等级 | 判定 | 典型证据 |
|------|------|---------|
| `direct` | 结论与原文明确对应 | 特性文档中的命令定义、参数取值 |
| `supporting` | 原文支持但非直接陈述 | 跨特性分析归纳的依赖关系 |
| `inferred` | 由多条证据推理得出 | 跨主题分析归纳的方案闭包 |
| `weak` | 单一弱证据，需进一步验证 | 配置实例中的隐含规则 |

> 本图谱所有正式对象的 `source_evidence_ids` 至少达到 `supporting` 强度；特性/命令层对象的证据默认 `direct`。

### 7.3 证据可追溯链路验证

图谱任意对象 → `source_evidence_ids` → 本索引 → 知识文档 → 原始产品文档（通过知识文档中的 SourcePath/OriginalPath 字段回溯到原始 md）。

完整链路示例：
```
CS-AC-XX (URL过滤方案)
  → source_evidence_ids: [EV-CA-AC-01, EV-CA-AC-02, EV-FK-AC-14, EV-TK-AC-07]
    → cross-feature-analysis.md 附录D 端到端流程
    → cross-topic-analysis.md §4 核心链路
    → GWFD-110471-URL过滤基本功能.md
    → Batch-07-URL过滤与接入控制.md
      → SourcePath: 原始产品文档 UDG/UNC 特性指南（权威事实源）
```

---

## §8 证据完整性检查清单

- [x] 19 份特性知识全部登记并分配主 Evidence ID（EV-FK-AC-01 ~ EV-FK-AC-19，★ P5 批次 3 补 16~19）
- [x] 4 份复用共享特性注明"三场景共享，复用计费/带宽场景"（EV-FK-AC-01/02/03/05）
- [x] 11 份独有特性知识文档路径真实存在（feature-knowledge/*.md）
- [x] **★ 4 份 UNC 接入控制辅助特性登记（EV-FK-AC-16~19，P5 批次 3 新增 U-H-02 关联），暂锚定 cross-topic-analysis.md §6.3**
- [x] 8 份主题知识全部登记并分配 Evidence ID（EV-TK-AC-01 ~ EV-TK-AC-08）
- [x] 2 份跨特性/跨主题分析全部登记（EV-CA-AC-01, EV-CA-AC-02）
- [x] **★ 4 份附录 D 端到端流程子证据登记（EV-CA-D1~D4，P5 批次 2 新增，U-H-03）**
- [x] 2 份场景级原始材料登记（EV-BS-AC-01 doc-list, EV-BS-AC-02 feature-doc-list）
- [x] 所有路径相对本场景目录（`业务图谱体系/访问限制场景/`）准确
- [x] 所有 Feature 对象引用对应 EV-FK-AC-*（19 特性全覆盖）
- [x] 所有核心 Command 对象引用对应 EV-FK-AC-* + EV-CA-AC-01（别名 EV-FK-AC-CFA）
- [x] 证据可追溯链路验证（图谱对象 → 本索引 → 知识文档 → 原始 md）
- [x] 所有证据 status = active，evidence_type = markdown
- [x] **引用一致性核查通过**（被引用 33 个 ID ⊆ 已注册 35 个 ID，别名全覆盖，含 EV-CA-D1~D4 + EV-FK-AC-16~19）
- [x] **★ 命名异类已修复**（P5 批次 2 统一 04 到序号主形式 EV-FK-AC-01~15；批次 3 消除 02 §1.9 的 EV-CA-AC-02 占位，4 个 UNC 辅助特性获得独立 EV-FK-AC-16~19）

---

## §9 与计费/带宽控制场景证据层的对比

| 维度 | 计费场景 | 带宽控制场景 | 访问限制场景 |
|------|---------|------------|------------|
| 证据总数 | 32 | 59 | **35**（P5 批次 2/3 修正：27 + EV-CA-D1~D4 4 + EV-FK-AC-16~19 4） |
| 特性知识 | 14 EV-FK | 24 EV-FK | **19 EV-FK-AC**（11 独有 + 4 复用 + 4 UNC 辅助，★ P5 批次 3） |
| 主题知识 | — | 32 EV-TK（317源文档） | **8 EV-TK-AC**（2303 行） |
| 跨特性分析 | 1 EV-CFA（580行） | 1 EV-CA-01（1119行） | **EV-CA-AC-01（1602行）** |
| 跨主题分析 | — | 1 EV-CA-02（862行） | **EV-CA-AC-02（1558行）** |
| 附录 D 端到端流程子证据 | — | — | **★ 4 EV-CA-D1~D4**（P5 批次 2，DISCARD/HEADEN/REDIRECT/接入控制） |
| 场景级原始材料 | — | — | **2 EV-BS-AC**（doc-list + feature-doc-list） |
| 业务图谱 | 2 EV-BS | 1 EV-BS（三层形式） | 直接三层形式（不单独注册） |
| 命名方案 | 单一 EV-FK-NN | 单一 EV-FK-NN | **★ P5 统一为单一 EV-FK-AC-NN 主形式**（XXXXXX 别名已弃用；批次 3 补 EV-FK-AC-16~19） |

### 关键差异说明

1. **访问限制场景证据规模居中**：19 特性（★ P5 批次 3 补 4 UNC 辅助）+ 8 主题批次 + 4 附录 D 子证据 = 31 份知识文档（不含原始材料 EV-BS），介于计费（14）与带宽（56）之间。主题批次数（8）远少于带宽（32），因访问限制源文档规模较小，按业务功能族归并更紧凑。

2. **★ 附录 D 子证据独立注册（P5 新增）**：访问限制独有 EV-CA-D1~D4，将跨特性分析附录 D 的四类端到端流程（DISCARD / HEADEN / REDIRECT / 接入控制）独立注册为子证据，覆盖 03 任务层 59 条编排边 + 05 跨层链路 8 处引用（共 67 处），追溯粒度比计费/带宽更细。这是访问限制场景图谱对端到端流程溯源的特殊强化。

3. **命名异类已修复**：P5 前 `04-command-graph.md` 使用特性编号后缀（`EV-FK-AC-110471` 等），与 02 声明的序号主形式（`EV-FK-AC-14`）不一致，本索引曾通过 §0 别名映射表桥接。P5 已全局统一 04 到序号主形式（约 80 处替换），本索引别名表保留为向后兼容说明。计费/带宽场景本就是单一命名方案。

4. **复用比例较高**：19 特性中 4 个（21%）复用计费/带宽场景知识文档（SA-Basic、PCC-UDG、PCC-UNC、ADC-UNC），三场景共享同一份知识资产，体现业务感知层与 PCC 骨架层的通用性；另 4 个 UNC 接入控制辅助特性（★ P5 批次 3 新增）暂锚定 cross-topic-analysis.md §6.3，待后续独立建档。

5. **跨特性分析最深**：1602 行，为三场景之最（计费 580、带宽 1119）。原因是访问限制涉及 7 大功能族（ADC/头增强×3/防欺诈/重定向×4/URL过滤/接入控制），依赖与配置对象共享关系最复杂，附录 A-F 覆盖最全。

6. **场景级原始材料单独注册**：访问限制独有 EV-BS-AC-01/02（doc-list + feature-doc-list），作为 P0 文档治理的产物留档。计费/带宽场景未单独注册此类清单证据。

---

> 本索引为访问限制场景三层图谱的"证据层"，确保图谱任何结论都能反查到权威事实源，满足 Schema §8.11 EvidenceSource 字段规范和质量门禁的"可信度门禁"要求。通过 §0 别名映射表与 §6 引用一致性核查，保证 01-05 各层图谱引用的 EV ID 均可命中本表，消除命名异类导致的追溯断链。
