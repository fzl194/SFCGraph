# SFCGraph — 云核心网三层配置图谱与 Agent 可用知识体系

## 1. 项目目标

将云核心网（5G Core）领域中复杂、隐性、分散的业务知识，转化为 **Agent 可检索、可理解、可推理、可调用、可生成、可核查、可持续演进** 的运行时知识体系。

三层图谱是该体系的结构化主干，但不是全部。系统还需结合 RAG 证据、配置范式、规则、Action、Skill 和运行反馈。

**一句话总目标**：构建面向 Agent 执行期的领域知识运行层（Agent Runtime Knowledge Layer）。

---

## 2. 核心问题

项目围绕"云核心网配置生成"展开，解决的是从业务语义逐层收敛为可执行配置的链路：

```
用户模糊业务需求 / 动网MOP / 配置指导书
  → 业务意图理解
  → 业务作业场景归一
  → 具体网元特性分解
  → 特性配置范式选择
  → 配置块实例化
  → MML命令生成
  → 语法核查 / 规范核查 / 语义核查
  → 回退方案 / 证据追溯 / 人工修正回流
```

---

## 3. 三层图谱架构

```
业务图谱 (Business Graph)
    ↕  requires_capability / realized_by_feature
特性图谱 (Feature Graph)
    ↕  uses_command / has_config_object
命令图谱 (Command Graph)
```

| 层级 | 定义 | 职责 |
|------|------|------|
| **业务图谱** | 业务意图—作业场景—网元特性分解图 | 将开放意图归一为收敛的业务作业场景 |
| **特性图谱** | 网元特性—配置范式—规则约束沉淀图 | 将具体网元特性沉淀为可复用配置范式 |
| **命令图谱** | 配置对象—对象关系—配置块结构底座图 | 将命令体系抽象为可生成、可核查的配置对象网络 |

### 三项关键技术

| 技术 | 对应层 | 核心能力 |
|------|--------|----------|
| 基于意图语义单元的业务图谱挖掘技术 | 业务层 | 意图归一与场景收敛 |
| 基于配置块的频繁子图挖掘技术 | 特性层 | 配置范式挖掘与沉淀 |
| 面向配置对象的命令本体建模技术 | 命令层 | 配置对象本体建模 |

---

## 4. 知识形态体系

图谱只是知识组织形态之一，复杂领域知识需要区分不同形态：

| 知识形态 | 作用 |
|----------|------|
| 图谱 / 本体 | 表达对象、关系、层级、约束、可推理结构 |
| RAG 证据文本 | 保留产品文档、MOP、指导书中的原文依据 |
| 配置范式 / 模板 | 表达稳定的配置组合和生成路径 |
| 规则 / 核查项 | 表达业务规则、特性规则、命令规则 |
| Action / Tool | 执行查询、生成、核查、回退、比对等动作 |
| Skill | 面向具体业务场景封装图谱、证据、规则、工具和流程 |
| 运行反馈 | 记录人工修正、生成失败、核查失败、新场景发现 |

---

## 5. 项目结构

```
SFCGraph/
├── 云核心网三层配置图谱与Agent可用知识体系构建上下文.md   # 项目全景设计文档
├── product_doc_md_exporter_optimized.py                    # HDX文档→Markdown导出工具
│
├── output/                                                 # 产品文档原始语料（118,000+ md文件）
│   ├── UDG_Product_Documentation_CH_20.15.2/              # UDG 用户面产品文档（71,374 文件）
│   └── UNC 20.15.2 产品文档(裸机容器) 05/                 # UNC 控制面产品文档（46,657 文件）
│
├── FeatureGraph/                                           # 特性图谱（特性层，三层图谱承接者）
│   ├── 特性层对象与关系定义.md                              # 特性层 schema 权威定义
│   ├── pipeline.yaml / build_all.py                        # 抽取 pipeline（半自动，对齐 ConfigTask 模式）
│   ├── builder/{core,steps,agent}/                         # 模块化抽取（step1-4 逻辑已移植于此）
│   └── data/{nf}/{version}/*.jsonl                         # 产物 + legacy/ 历史 CSV 种子
│
├── business-graph/                                          # 业务图谱（上层）
│   ├── 00-design-charter.md                                # 设计章程
│   ├── 01-current-structure-analysis.md                    # 现状分析
│   ├── 02-usage-scenarios.md                               # 使用场景
│   ├── 03-schema-design.md                                 # Schema 设计初版
│   ├── 04-schema-final.md                                  # Schema 定稿
│   ├── 04-schema-final-v2.md                               # Schema 定稿v2
│   ├── 05-second-layer-objects-design-final.md             # 第二层对象设计
│   ├── 06-business-awareness-business-graph-final.md       # 业务感知图谱终稿
│   ├── 06-business-awareness-business-graph-final.xlsx     # 业务感知图谱Excel产出
│   ├── build_business_graph_workbook.py                    # 图谱→Excel构建脚本
│   └── myoutput/                                           # 探索过程产出
│       ├── business-awareness-graph/                       # 业务感知图谱构建过程
│       │   ├── 00~22-*.md                                  # 从工作计划到终稿的完整迭代
│       │   └── notes/                                      # UDG/UNC特性研究笔记
│       └── business-awareness-discovery/                   # 业务感知发现过程
│           └── 00~02-*.md                                  # 候选特性与业务描述
│
└── old/                                                     # 历史迭代（第一版）
    └── business-graph/                                     # 自顶向下构建的早期尝试
        ├── gen_viz_data.py                                 # 可视化数据生成脚本
        ├── 01~14-*.md                                      # 构建策略→自审→重建计划
        ├── data/                                           # 早期CSV数据
        ├── data2/                                          # 自底向上重建数据
        └── templates/                                      # 模板文件
```

---

## 6. 特性图谱详细进度

### 6.1 数据模型

**7 张节点表 + 2 张边表：**

| 类型 | 表名 | 说明 |
|------|------|------|
| 节点 | Feature | 特性主节点（xlsx每行一个） |
| 节点 | SubFeature | 子特性（按代际拆分：2_3G/4G/5G） |
| 节点 | ProcedureVariant | 配置场景（同一特性的不同配置路径） |
| 节点 | ConfigStep | 配置步骤（有序，含MML命令） |
| 节点 | ConfigObject | 配置对象（桥接命令图谱） |
| 节点 | ValidationRule | 验证规则 |
| 节点 | DocAsset | 知识文档 |
| 边 | FeatureDependency | 特性间依赖/互斥/协同 |
| 边 | FeatureLicense | 特性与License映射 |

### 6.2 抽取进度

| 层级 | 抽取内容 | 方法 | 状态 | 规模 |
|------|---------|------|------|------|
| **L1** | Feature基础属性 | 代码自动化 | ✅ 已完成 | 898特性(UDG 303 + UNC 595) |
| **L2** | DocAsset分类 | 代码自动化 | ✅ 已完成 | 3,194条 |
| **L3** | FeatureDependency | 代码自动化 | ✅ 已完成 | 673条 |
| **L4** | FeatureLicense | 代码自动化 | ✅ 已完成 | 412条 |
| **L5** | SubFeature | 代码自动化 | ❌ 未开始 | — |
| **L6** | ConfigObject + 层级 | 代码初抽 + LLM精抽 | ❌ 未开始 | — |
| **L7** | ProcedureVariant + ConfigStep | LLM | ❌ 未开始 | — |
| **L8** | ValidationRule | LLM | ❌ 未开始 | — |

### 6.3 处理管道

> **已迁移至 `FeatureGraph/builder/`**：特性抽取改由 `pipeline.yaml` + `build_all.py` 编排（半自动：自动步连续跑、Agent 步遇 PAUSE 停），产物落 `data/{nf}/{version}/*.jsonl` + 四段式实例键。历史 step1-4（xlsx→特性CSV、文档映射、L1-L4 抽取）的逻辑已移植进 `builder/core/`，旧脚本随 `feature-graph/` 目录移除；历史 CSV 作为种子保留在 `FeatureGraph/data/legacy/`。

### 6.4 已知质量问题

| 严重度 | 问题 | 根因 |
|--------|------|------|
| CRITICAL | `applicable_nf` 对"适用 N F"等变体格式解析失败 | 正则匹配不兼容空格 |
| HIGH | 部分特性License信息缺失 | 纯文本格式未被解析 |
| MEDIUM | License存在脏数据行（名称带"|"后缀） | 表格解析多提取了一行 |
| LOW | Definition仅取首段 | 设计取舍 |

### 6.5 Schema待补字段

| 表 | 缺失字段 | 修复方式 |
|----|---------|---------|
| DocAsset | `id`, `doc_title` | 代码生成 |
| DocAsset | `sub_feature_id` | 等L5完成后回填 |
| FeatureDependency | `id`, `source_type` | 代码拼接/默认值 |
| FeatureLicense | `id` | 代码拼接 |

---

## 7. 业务图谱详细进度

### 7.1 Schema演进

业务图谱经历了多轮迭代：

| 版本 | 内容 | 文档 |
|------|------|------|
| v1 | 初始17对象类型，基于业务感知单域 | `myoutput/.../05-*-v1.md` |
| v2 | 合并优化，32能力87流程218功能 | `myoutput/.../19-*-final_v2.md` |
| final | 结构设计讨论，面向多域通用骨架 | `00-design-charter.md` ~ `06-*-final.md` |

### 7.2 当前状态

- **已完成**: 业务感知（Business Awareness）域的单案例完整图谱
  - 差异化计费 / 免费服务 / 默认计费 三个业务主线
  - 配额耗尽 / 欠费重定向 场景
  - Schema + 实例 + Excel产出物
- **进行中**: Schema泛化讨论（从业务感知专属模板→通用骨架）
- **未开始**: 其他业务域（故障管理、切片管理、安全防护等）

### 7.3 历史教训（old/目录）

第一版采用自顶向下构建方式，发现以下问题：

1. **语义桥接层断裂** — 业务层到技术层的中间对象未正确落地
2. **构建顺序问题** — 自顶向下导致中间层断层
3. **证据粒度不足** — 停留在页面摘要级，未到字段级断言

**关键转折**: 从自顶向下改为自底向上（`13-data2-bottom-up-rebuild-plan-v0.1.md`），即：

```
命令图谱（基础）→ 特性图谱（中间）→ 业务图谱（上层）
```

---

## 8. 产品文档语料

| 产品 | 类型 | 文件数 | 说明 |
|------|------|--------|------|
| UDG 20.15.2 | 用户面（UPF/PGW-U等） | ~71,374 | 特性部署、OM命令、5G基础知识等 |
| UNC 20.15.2 | 控制面（AMF/SMF等） | ~46,657 | 特性部署、OM命令、网络运维等 |

文档通过 `product_doc_md_exporter_optimized.py` 从 HDX 归档导出为 Markdown，保留主题层级和原始内容。

### 原始产品文档入口目录

构建三层图谱所使用的原始语料入口：

**UDG（用户面）：**

| 入口路径 | 内容 |
|----------|------|
| `output/UDG_Product_Documentation_CH_20.15.2/` | UDG 产品文档根目录 |
| `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/` | UDG 特性文档（特性概述、激活、原理、调测、参考信息） |
| `output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令/` | UDG MML 命令手册 |

**UNC（控制面）：**

| 入口路径 | 内容 |
|----------|------|
| `output/UNC 20.15.2 产品文档(裸机容器) 05/` | UNC 产品文档根目录 |
| `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/` | UNC 特性文档 |
| `output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/` | UNC MML 命令手册 |

**其他重要目录：**

- `5G基础知识/一望5G/` — 5G核心网概念、架构、解决方案总览
- `网络部署/` / `网络运维/` — 部署与运维指导

---

## 9. 工具说明

### product_doc_md_exporter_optimized.py

从 HDX（HTML归档）格式批量导出产品文档为结构化 Markdown 文件。

- **输入**: `.hdx` 归档文件（ZIP格式，含HTML文档和navi.xml导航结构）
- **输出**: 按主题层级组织的 Markdown 文件 + 主题映射文件
- **核心组件**: `TopicRecord`（主题数据类）、`HtmlToMarkdownConverter`（HTML→MD转换）、`ProductDocMarkdownExporter`（主流程）
- **入口**: `main()` 处理HDX文件，`main2()` 处理已解压目录

### build_business_graph_workbook.py

将业务图谱数据构建为 Excel 工作簿，包含多个 Sheet 对应不同实体类型和关系。

### gen_viz_data.py（old/）

早期可视化脚本，从 CSV 生成 vis-network 图数据，用于交互式图谱浏览。

---

## 10. 阶段规划

### 2026年：三层图谱最小闭环

- 特性图谱：完成 L1-L8 全量抽取
- 业务图谱：业务感知域完整闭环，启动其他高频域
- 命令图谱：配置对象建模与配置块样板
- 支撑 APN + DPI/BWM 典型场景穿刺

### 2027年：规模化扩展

- 多业务域扩展
- 语义核查闭环
- 特性规则结构化表达
- 运行反馈回流机制
- 跨场景复用与版本差异管理

---

## 11. 快速上手

### 环境要求

- Python 3.10+
- 依赖: `openpyxl`, `beautifulsoup4`（文档导出工具）

### 特性图谱构建

```bash
# 特性层抽取 pipeline（半自动：自动步连续跑，Agent 步遇 PAUSE 停）
python FeatureGraph/build_all.py UDG 20.15.2          # 全量（自动步 skip-if-exists）
python FeatureGraph/build_all.py UDG 20.15.2 feature   # 只跑某步（显式单步不 skip）
```

### 查看结果

```python
import csv
with open('FeatureGraph/data/legacy/l1_udg_feature_attributes.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['feature_id'], row['feature_name'], row['feature_type'])
        break
```

---

## 12. 关键文档索引

| 文档 | 路径 | 说明 |
|------|------|------|
| 项目全景设计 | `云核心网三层配置图谱与Agent可用知识体系构建上下文.md` | 项目目标、三层架构、技术路线、阶段规划 |
| 特性层 schema | `FeatureGraph/特性层对象与关系定义.md` | 特性层对象/关系权威定义（Feature/SubFeature/License/FeatureRule/DecisionPoint） |
| 业务图谱设计章程 | `business-graph/00-design-charter.md` | Schema讨论范围与目标 |
| 业务感知终稿 | `business-graph/06-business-awareness-business-graph-final.md` | 业务感知完整图谱定义与实例 |
| 业务感知v2终稿 | `business-graph/myoutput/.../19-*-final_v2.md` | v2版本（7域32能力87流程218功能） |
| 构建策略 | `old/business-graph/01-*-build-strategy-*.md` | 方法论与经验教训 |
