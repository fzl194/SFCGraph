# 知识流转与三层图谱构建 SOP

> 本文档基于计费场景（套餐1）和带宽控制场景（套餐2）两次完整实践，沉淀从原始产品文档到三层图谱的全链路经验。
> 目标：供不同业务域、不同子场景的图谱构建复用。
> **审查要点**：请对比你的SOP，标注一致/差异/遗漏。

---

## ★ 前置参考：三层图谱定义文件（本目录内）

> 本SOP所在的 `业务图谱体系/` 目录已收录三层图谱的全部权威定义文件，也是所有场景图谱产物的根目录。构建任何业务域/子场景的图谱前，**必须先读取以下文件**，理解对象字段、分类原则和关系边定义。

| 文件 | 定位 | 用途 | 阅读时机 |
|------|------|------|---------|
| `三层图谱Schema-最终版-v0.1.md` | **字段级Schema（权威）** | 定义全部对象类型字段、关系边、禁止关系（§8-§13） | Stage 4 前必读全量 |
| `三层图谱本体标准定义.md` | **分类原则（方法论）** | 定义对象本体、为什么这样分层、落位标准 | Stage 1 前必读 |
| `三层图谱对象与关系设计.md` | **设计讲解（案例驱动）** | 用计费案例穿讲图谱怎么用、对象间关系 | 首次构建必读 |
| `知识流转与图谱构建SOP.md` | **本文件** | 全链路5阶段操作手册 | 全流程参考 |

### 版本与去重说明

| 根目录原始文件 | 版本 | 状态 |
|---------------|------|------|
| `三层图谱Schema-最终版-v0.1.md` | v0.1（6月9日） | **★当前最新**，已收录 |
| `三层图谱收敛Schema.md` | v0.8草案（6月8日） | **已废弃**，被v0.1取代，未收录 |
| `三层图谱本体标准定义.md` | 最终版（6月9日） | **★当前最新**，已收录 |
| `三层图谱对象与关系设计.md` | 最终版（6月9日） | **★当前最新**，已收录 |

> 场景实例文件（`业务感知-计费场景图谱实例.md`、`计费案例核心概念标准定义.md`）为计费场景参考，非通用定义，保留在SFCGraph根目录，按需查阅。

### Schema快速导航（`三层图谱Schema-最终版-v0.1.md`）

| Schema章节 | 内容 | 图谱构建关键引用 |
|-----------|------|----------------|
| §8 | 对象类型总览 | 确认7层对象类型 |
| §8.11 | EvidenceSource字段 | evidence_type/status枚举 |
| §9 | 业务图谱层（BD/NS/CS/DP/BR/SO） | 第1层实例化 |
| §9.3 | Feature字段（含variant_dimensions） | 第2层实例化★ |
| §9.6 | Feature constrained_by FeatureRule | 命名规范★ |
| §10 | 特性图谱层 + 任务原子层 | 第2-3层实例化 |
| §10.6 | ConfigTask constrained_by TaskRule | 命名规范 |
| §11 | 命令图谱层（MMLCommand/ConfigObject/CommandRule） | 第4层实例化 |
| §11.6 | CommandRule governs MMLCommand | 命名规范★ |
| §11.7 | ConfigObject间关系边 | 第4层对象关系 |
| §12 | 跨层映射边 | 第5层实例化 |
| §13 | **禁止关系** | 合规检查★ |

---

## 0. 两种实践模式对比

经过两个场景的实践，形成了两种可复用模式：

| 维度 | 模式A：统一知识库模式（计费场景） | 模式B：双轨知识模式（带宽控制场景） |
|------|-------------------------------|-----------------------------------|
| 知识组织 | 文档→批次草稿→**统一知识库**(K编号)→图谱 | 文档→**特性知识+主题知识双轨**→横向分析→图谱 |
| 适合场景 | 单一知识维度（如计费方式），知识量中等(~300篇) | 多维知识（特性+业务专题），知识量大(~500篇) |
| 中间产物 | knowledge-drafts/ → 统一知识库.md | feature-knowledge/ + topic-knowledge/ + cross-analysis |
| 横向归纳 | 内嵌在统一知识库章节中 | 独立的cross-feature + cross-topic分析文件 |
| 图谱构建输入 | 统一知识库 + feature-knowledge | cross-feature-analysis(主) + cross-topic-analysis(辅) + 特性/主题知识(证据) |
| **推荐模式** | — | **★优先推荐**（结构更清晰，更适合三层图谱） |

> **经验总结**：模式B更适合三层图谱构建，因为cross-feature-analysis直接提供了图谱第2-4层（特性分类/依赖/命令/配置对象/端到端流程）的数据，cross-topic-analysis直接提供了第1层（方案/决策点/共性机制）的数据。

---

## 1. 全链路总览

```
原始产品文档(N百~N千篇)
  │
  ▼ Stage 1: 文档筛选
  │  输入: 关键词 + 产品文档路径
  │  产出: doc-list.md（特性仅ID + 业务专题/概念展开文件列表）
  │        + batch-plan（主题知识分批计划）
  │
  ▼ Stage 2: 知识提取（双轨并行）
  │  轨道1 - 特性知识: 逐特性读取产品文档 → feature-knowledge/{feature-id}.md
  │  轨道2 - 主题知识: 逐批次读取业务专题/概念文档 → topic-knowledge/Batch-{NN}.md
  │
  ▼ Stage 3: 横向分析
  │  产出1: cross-feature-analysis.md（跨特性归纳）
  │  产出2: cross-topic-analysis.md（跨主题归纳）
  │
  ▼ Stage 4: 三层图谱实例化
  │  输入: cross-analysis(主) + 特性/主题知识(证据) + Schema定义
  │  产出: three-layer-graph/ (7文件: 00~06)
  │
  ▼ Stage 5: 审查修复
     输入: 三层图谱7文件 + Schema + 权威源
     产出: 审查报告 + 分批修复记录
```

---

## 2. Stage 1: 文档筛选

### 2.1 输入

| 项目 | 说明 | 示例 |
|------|------|------|
| 主题名称 | 子场景名 | 带宽控制场景 |
| 目标目录 | `业务图谱体系/{主题}/` | `业务图谱体系/带宽控制场景/` |
| 所属业务域 | BusinessDomain | 业务感知 (service-awareness) |
| 关键词列表 | 文档筛选核心词 | BWM, bandwidth, CAR, Shaping, FUP, URR, 带宽, 限速 |
| 产品文档路径 | UDG/UNC文档根目录 | 见§2.2 |

### 2.2 产品文档入口路径（固定知识）

**UDG产品文档**：
| 层级 | 说明 |
|------|------|
| 一望5G | 基础概念层：SA专题、计费、PCC、QoS、分流 |
| 特性部署指南 | 特性激活/配置命令参考 |
| 命令参考手册 | MML命令详细参数 |

**UNC产品文档**：
| 层级 | 说明 |
|------|------|
| 一望5G | 与UDG对称（同ID同内容→保留UNC版去重） |
| 业务专题 | 解决方案专题文档（最大量） |
| 协议流程 | 接口信令、会话流程 |
| 初始配置 | 开局配置 |
| 网络运维 | 告警、信令跟踪 |
| 知识问答 | Q&A |
| 术语 | 术语条目 |

### 2.3 文档清单组织

**doc-list.md结构**：

```markdown
# {主题}文档清单
## 总览（分类统计表）
## Section 1: 特性清单（仅ID，不展开文件）
  ### 1.1 核心特性（必读）— 标注★
  ### 1.2 辅助特性（按需阅读）
## Section 2: 业务专题（展开md文件，等权重）
## Section 3: 5G基础知识概念（按目录展开）
```

**关键规则**：
- 特性**仅定位ID**（用户后续单独阅读特性文档），不展开特性内文件
- 业务专题、概念文档**列出所有md文件，等权重**
- 排除：MML命令文档、与本场景无关的业务专题

### 2.4 主题知识分批计划

**batch-plan生成策略**：
```
按(产品, 主题)分组 → 路径排序（同目录聚类）→ 按~10个文件/batch切分 → 合并尾部小批次
```

**产出**：`topic-batch-plan.md`，列出每个Batch的分组主题、产品、文件数。

### 2.5 质量门禁

- [ ] 所有层级路径均已扫描（一望5G、业务专题、协议、配置、运维、问答、术语）
- [ ] 去重规则已执行（UDG/UNC同ID保留UNC版）
- [ ] 核心特性全部标注★
- [ ] 遗漏分析完成，无高价值遗漏
- [ ] 分批计划中每个batch ≤ 15个文件

---

## 3. Stage 2: 知识提取（双轨并行）

### 3.1 轨道1 — 特性知识提取

**目标**：为每个特性产出一份结构化知识文档。

**输入**：特性的产品文档（特性部署指南中的特性章节）。

**特性知识文档结构**（6大板块）：

```markdown
# {特性ID} {特性名} 知识文档

## 概述
### 特性定义        — 一段话说明特性做什么
### 适用NF          — NF角色表（网元名/角色/说明）
### 版本信息        — 特性版本/发布版本/发布说明
### License         — License控制项
### 前置条件与依赖  — 依赖特性表

## 激活             — License开启命令
## 原理             — 工作机制、流程图、关键概念
## 配置             — 配置对象、MML命令、参数、典型配置实例
## 调测             — 验证命令、故障排查
## 参考信息         — 参数取值表、约束条件、版本差异
```

**关键要求**：
- 每条知识标注来源文件路径（SourcePath/OriginalPath）
- 配置实例保留原始MML命令（不转述）
- 参数取值必须与命令参考手册一致

### 3.2 轨道2 — 主题知识提取

**目标**：逐批次阅读业务专题/概念文档，提取结构化知识条目。

**主题知识文档结构**：

```markdown
# Batch-{NN}: {分组主题}

> 批次 | 主题 | 来源 | 文件数 | 核心度(★)

## 1. 概述           — 本批次文档覆盖的板块
## 2. 核心知识点
### KP-01: {标题}   — 知识条目（表格/列表/配置实例）
### KP-02: {标题}
...
## 3. 关键发现       — 跨文档归纳的隐性规则/约束
```

**关键要求**：
- 每个KP标注来源文件
- 核心度标注（★★★★★ = 直接关联目标场景）
- 配置实例保留原始MML命令

### 3.3 质量门禁

- [ ] 每个特性知识文档覆盖6大板块
- [ ] 每个主题知识批次完成
- [ ] 每条知识标注来源
- [ ] 无大量重复条目（相似知识需合并）
- [ ] 核心度标注完成

---

## 4. Stage 3: 横向分析

### 4.1 跨特性分析（cross-feature-analysis.md）

**目标**：横向归纳N个特性的共性、差异、依赖、命令、配置对象。

**结构**：

| 章节 | 内容 | 图谱用途 |
|------|------|---------|
| §1 特性分类总览 | feature_group分组 | 第2层 Feature.feature_group |
| §2 共性分析 | 通用机制归纳 | 第2层 FeatureRule |
| §3 配置差异分析 | 参数差异对比 | 第4层 CommandParameter |
| §4 依赖关系分析 | depends_on图 | 第2层 depends_on边 |
| §5 关键发现 | 隐藏关系/约束 | 第1层 BusinessRule |
| 附录A | 特性索引表 | 第6层 EV-FK映射 |
| 附录B | MML命令交叉参考 | 第4层 MMLCommand + invokes边 |
| 附录C | 配置对象复用矩阵 | 第4层 ConfigObject + operates_on边 |
| 附录D | 典型端到端配置流程 | 第3层 TaskCommandOrderEdge |
| 附录E~H | 版本演进/令牌桶/无线/隐藏关系 | 补充约束 |

### 4.2 跨主题分析（cross-topic-analysis.md）

**目标**：横向归纳主题知识的共性机制、方案、决策点。

**结构**：

| 章节 | 内容 | 图谱用途 |
|------|------|---------|
| §2 主题分类与知识地图 | 主题维度归纳 | — |
| §3 共性机制分析 | 跨主题共用机制 | 第1层 SemanticObject |
| §4 配置差异对比 | 主题间差异 | 第4层 CommandParameter |
| §5 依赖关系与协同 | 主题间依赖 | 第1层 BusinessRule |
| §6 与{场景}核心关联 | 方案/决策点归纳 | **★第1层 CS/DP/BR/SO的直接来源** |
| §7 关键发现 | 隐藏关系 | 第1层 BusinessRule |
| §8 附录 | 场景归并、冲突矩阵 | 第4层 CommandRule |

### 4.3 质量门禁

- [ ] 跨特性分析覆盖全部特性
- [ ] 附录B/C/D（命令/对象/流程）完整
- [ ] 跨主题分析的§6直接产出方案闭包(CS)和决策点(DP)

---

## 5. Stage 4: 三层图谱实例化

### 5.1 前置准备（★关键教训）

**必须先完成**（文件均在本目录内）：
1. 读取Schema定义文件（`./三层图谱Schema-最终版-v0.1.md`），确认所有对象字段 — 重点看§8-§13
2. 读取本体标准定义（`./三层图谱本体标准定义.md`），确认分类原则与落位标准
3. 读取对象与关系设计（`./三层图谱对象与关系设计.md`），理解对象间关系（首次构建必读）
4. **确定EV ID命名规范**（★这是最容易出错的地方）

**EV ID命名规范**（★教训：必须Stage4前统一确定）：

```
特性知识:    EV-FK-{NN}          编号格式（如EV-FK-01~24），不用语义别名
主题知识:    EV-TK-{NN}          编号格式（如EV-TK-01~32）
跨特性分析:  EV-CA-01
跨主题分析:  EV-CA-02
业务图谱:    EV-BS-01
```

> **教训**：带宽控制场景首次构建时，Agent自由发挥用了EV-FK-BWM/EV-FK-SA-Basic等语义别名，导致158处引用与06-evidence-index的编号格式不一致，需大量修正。

### 5.2 7文件结构与构建顺序

```
three-layer-graph/
├── 00-overview.md            # 总览（最后建，依赖01-06计数）
├── 01-business-graph.md      # 第1层：BD/NS/CS/DP/BR/SO
├── 02-feature-graph.md       # 第2层：Feature/License/FR/depends_on
├── 03-task-layer.md          # 第3层：ConfigTask/TaskRule/TCOE
├── 04-command-graph.md       # 第4层：MMLCommand/ConfigObject/CommandRule
├── 05-cross-layer-mapping.md # 第5层：跨层映射边
├── 06-evidence-index.md      # 第6层：EvidenceSource注册表
```

**构建顺序**（可并行的Wave）：

| Wave | 文件 | 数据源 | 可并行 |
|------|------|--------|--------|
| 1a | 01-business-graph | cross-topic §6(方案/DP) + cross-feature §5(规则) | 与1b并行 |
| 1b | 02-feature-graph | cross-feature §1/§4(分类/依赖) + 附录A | 与1a并行 |
| 1c | 06-evidence-index | feature-knowledge/ + topic-knowledge/清单 | 与1a/1b并行 |
| 2a | 03-task-layer | cross-feature 附录D(流程) + 特性知识§配置 | 与2b并行 |
| 2b | 04-command-graph | cross-feature 附录B/C(命令/对象) + 特性知识§配置 | 与2a并行 |
| 3 | 05-cross-layer-mapping | 01-04的跨层边汇总 | 依赖Wave 1-2 |
| 4 | 00-overview | 01-06计数统计 + 端到端链路 | 依赖Wave 1-3 |

### 5.3 各层数据源映射

| 图谱层 | 对象 | 主要数据源 |
|--------|------|-----------|
| 第1层 | CS(方案闭包) | cross-topic §6(场景归并) + cross-feature §5 |
| | DP(决策点) | cross-topic §6(五维度/决策树) |
| | BR(业务规则) | cross-feature §5 + cross-topic §7 |
| | SO(语义对象) | cross-topic §3(共性机制) |
| 第2层 | Feature | cross-feature §1(分类) + 附录A(索引) |
| | depends_on | cross-feature §4(依赖图) |
| | License | cross-feature §2.3(License链) |
| 第3层 | ConfigTask | cross-feature 附录D(端到端流程) |
| | TaskCommandOrderEdge | cross-feature 附录D + 特性知识§配置 |
| 第4层 | MMLCommand | cross-feature 附录B(命令交叉参考) |
| | ConfigObject | cross-feature 附录C(配置对象矩阵) |
| | CommandRule | cross-feature §H.4(冲突矩阵) |
| 第6层 | EvidenceSource | feature-knowledge/ + topic-knowledge/ + cross-analysis |

### 5.4 Schema合规要点（★教训汇总）

| 要点 | 说明 | 教训来源 |
|------|------|---------|
| `variant_dimensions` | Feature必须有此字段（Schema §9.3） | 带宽场景首次缺失，需补回 |
| `applicable_nf_map` | JSON格式 `{"UDG": ["SGW-U"]}`，不用文本格式 | 带宽场景首次用文本格式 |
| `constrained_by` | Feature `constrained_by` FeatureRule（非`has_rule`） | 计费场景审查U-M-17 |
| `governed_by` | MMLCommand `governed_by` CommandRule（反向：CommandRule `governs`） | 计费场景审查U-M-17 |
| `evidence_type/status` | EvidenceSource必须有此两列（Schema §8.11） | 计费场景审查U-M-20 |
| EV ID格式 | 全库统一编号格式，不用语义别名 | 带宽场景158处修正 |

### 5.5 质量门禁

- [ ] 所有对象类型严格匹配Schema §8-§12定义
- [ ] 无Schema §13禁止关系（CS→ConfigObject直接绑定、Feature→MMLCommand直接绑定等）
- [ ] 所有对象包含`source_evidence_ids`字段
- [ ] EV ID格式全库统一
- [ ] Feature包含`variant_dimensions`字段
- [ ] `applicable_nf_map`为JSON格式
- [ ] 至少3条端到端链路验证（BD→NS→CS→Feature→Task→Command→Object）

---

## 6. Stage 5: 审查修复

### 6.1 审查流程

```
Step 1: Schema合规审查 → 产出审查报告（按HIGH/MEDIUM/LOW分级）
Step 2: 分批修复 → 快捷(P2) → 中等(P2) → 大工作量(P2) → 高价值(P3)
Step 3: 每次修改前追溯到知识库/产品文档验证权威性
Step 4: 修复记录文档化 → audit/批次N-修复记录.md
```

### 6.2 审查检查清单

| 类别 | 检查项 |
|------|--------|
| Schema合规 | 对象类型/字段/关系边/禁止关系 |
| 命名一致性 | EV ID格式/关系边命名(has_rule vs constrained_by) |
| 证据可追溯 | 每个对象source_evidence_ids指向真实文档 |
| 跨层一致 | CS的uses_feature→Feature存在；Task的invokes→Command存在 |
| 内容准确性 | 参数取值/单位/取值范围与权威源一致 |
| 计数一致 | 总览计数与各文件实际数量一致 |

### 6.3 质量门禁

- [ ] P2级审查项全部清零
- [ ] 修复记录文档化
- [ ] 整体合规率 ≥ 90%

---

## 7. 目录结构标准

> 所有业务图谱产物统一存放在 `业务图谱体系/{场景名}/` 下，与SOP和三层图谱定义文件同级。

### 7.1 体系根目录

```
业务图谱体系/                            # ★全部业务图谱的根目录
├── README.md                          # 导航
├── 知识流转与图谱构建SOP.md            # 本文件（全链路操作手册）
├── 三层图谱Schema-最终版-v0.1.md       # 字段级Schema（权威）
├── 三层图谱本体标准定义.md             # 分类原则
├── 三层图谱对象与关系设计.md           # 设计讲解
│
├── 计费场景/                          # 场景实例（已构建）
├── 带宽控制场景/                      # 场景实例（已构建）
└── {新场景名}/                        # 新场景直接在此构建
```

### 7.2 场景目录结构（★标准）

```
{场景名}/
│
│  ═══ Stage 1: 文档筛选 ═══
├── {场景}doc-list.md              # ★文档清单
├── {场景}feature-doc-list.md      # ★特性文档清单
├── topic-batch-plan.md            # ★主题分批计划（模式B必需）
│
│  ═══ Stage 2 轨道1 + Stage 3: 特性知识 + 跨特性分析 ═══
├── feature-knowledge/
│   ├── GWFD-{ID}-{name}.md       #   UDG特性知识（N个）
│   ├── WSFD-{ID}-{name}.md       #   UNC特性知识（M个）
│   └── cross-feature-analysis.md #   ★跨特性分析（归入此目录）
│
│  ═══ Stage 2 轨道2: 主题知识 ═══
├── topic-knowledge/
│   └── Batch-{NN}-{topic}.md     #   主题批次（K个）
│
│  ═══ Stage 3: 跨主题分析 ═══
├── cross-topic-analysis.md        # ★跨主题分析（独立文件）
│
│  ═══ Stage 4-5: 三层图谱 + 审查 ═══
├── three-layer-graph/
│   ├── 00-overview.md
│   ├── 01-business-graph.md
│   ├── 02-feature-graph.md
│   ├── 03-task-layer.md
│   ├── 04-command-graph.md
│   ├── 05-cross-layer-mapping.md
│   ├── 06-evidence-index.md
│   └── audit/                     #   Stage 5: 审查记录
│       ├── 00-审查报告汇总.md
│       └── 批次N-修复记录.md
│
│  ═══ 可选区域（按需，不强制）═══
├── scripts/                       #   辅助脚本与验证报告（gen_*.py, verify_*）
├── SKILL/                         #   图谱效果测试整体（含kb/、ref-phase*等）
├── knowledge-drafts/              #   模式A中间产物（草稿→统一知识库）
│   └── draft-batch-*.md
├── unified-knowledge/              #   模式A知识产物（统一知识库+融合知识）
│   ├── {场景}统一知识库.md          #     EV-KB-001 证据源
│   └── knowledge-fused-part*.md    #     EV-KB-002~004 证据源
└── (场景级散件md)                    #   原始业务图谱 / 设计文档（如有）
    ├── 01{场景}业务图谱.md          #     EV-BS-001 证据源
    └── design-*.md                 #     设计文档
```

### 7.3 目录设计原则

| 原则 | 说明 |
|------|------|
| **按pipeline阶段组织** | 每个目录对应pipeline的一个或多个阶段 |
| **正式产物在标准位置** | doc-list/feature-doc-list/batch-plan在根目录，cross-analysis在对应knowledge目录内 |
| **辅助文件归入scripts/** | 生成脚本、验证脚本、验证报告统一放scripts/，不污染根目录 |
| **模式A/B差异用可选区域** | drafts/、散件md标注为可选，模式B场景不需要 |
| **SKILL作为整体保留** | SKILL/目录不拆分，是测试图谱效果的独立整体 |

### 7.4 两个已有场景的对照

| 目录/文件 | 计费场景（模式A） | 带宽控制场景（模式B） |
|----------|-----------------|---------------------|
| doc-list.md | `charging-doc-list.md` + `charging-doc-list/`(batch明细) | `bandwidth-doc-list.md` |
| feature-doc-list | `charging-feature-doc-list.md` | `bandwidth-feature-doc-list.md` |
| batch-plan | （模式A无） | `topic-batch-plan.md` |
| feature-knowledge/ | 15文件（14特性+CFA） | 25文件（24特性+CFA） |
| topic-knowledge/ | （模式A无） | 32个Batch |
| cross-topic-analysis | （模式A无） | ✓ |
| three-layer-graph/ | 7文件+audit/(10文件) | 7文件 |
| scripts/ | verify脚本+报告 | gen脚本+verify脚本 |
| SKILL/ | ✓（测试整体） | （无） |
| knowledge-drafts/ | 12个草稿 | （无） |
| unified-knowledge/ | 统一知识库+融合知识(4文件) | （无） |
| 场景级散件md | 01业务图谱+设计文档(2个) | （无） |

> **注**：计费场景和带宽控制场景已从 `business-graph/` 拷贝迁入本体系（源文件保留）。新场景直接在 `业务图谱体系/{场景名}/` 下构建。

---

## 8. 并行执行约束

- **最多2个并行Agent**（用户明确约束）
- 独立层可并行（如01业务图谱 + 02特性图谱）
- 有依赖的层串行（如05跨层映射依赖01-04）

---

## 9. 经验教训汇总

| # | 教训 | 影响 | 防范措施 |
|---|------|------|---------|
| 1 | EV ID命名规范必须在Stage 4前统一确定 | 带宽场景158处修正 | Stage 1确定编号格式，写入SOP |
| 2 | Schema字段必须完整理解再实例化 | variant_dimensions缺失 | Stage 4前置：读Schema全量字段清单 |
| 3 | Agent覆盖重写会丢失已有内容 | 带宽场景覆盖了用户高质量骨架 | Agent指令须含"保留已有内容，增量补充" |
| 4 | cross-analysis是三层图谱的关键输入 | — | Stage 3不可跳过 |
| 5 | 特性知识6大板块缺一不可 | 配置/调测缺失影响图谱完整度 | 质量门禁检查6板块覆盖 |
| 6 | 审查修复必须追溯到权威源 | 参数取值错误 | 每次修改前验证原始产品文档 |
| 7 | applicable_nf_map必须JSON格式 | Schema不合规 | 在feature-knowledge模板中固化 |
