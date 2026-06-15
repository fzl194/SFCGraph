# 业务图谱探索器设计文档

> 日期: 2026-06-15
> 状态: 已确认，待实现

## 背景与问题

当前业务图谱前端（BusinessScenario.vue）直接平铺展示 MD 的章节结构，存在两个问题：
1. 六层流图视图只是把 MD 的 ##/### 结构按层堆叠，没有体现对象之间的实际关系
2. 用户看不到 BD → NS → CS → Feature → Task → Command 这条核心关系链

用户需要的是一个**从顶到底层层递进**的探索界面：从业务域开始，逐层展开到场景、方案、特性、任务、命令，能看到完整的关系链，点击任意对象能查看其 schema 属性。

## 数据结构基础

### 核心关系链

```
BusinessDomain (BD) 业务域
  └─contains→ NetworkScenario (NS) 现网场景
       └─instantiated_as→ ConfigurationSolution (CS) 配置方案
            └─uses_feature→ Feature / SubFeature 特性
                 └─decomposes_to→ ConfigTask 配置任务
                      └─invokes→ MMLCommand MML命令
                           └─operates_on→ ConfigObject 配置对象
```

### 横向关系（非主链，在详情面板展示）

| 关系 | 说明 |
|------|------|
| has_decision | 指向 DecisionPoint（业务/特性/任务层） |
| constrained_by | 指向 Rule（BR/FR/TR/CR） |
| uses_semantic_object | 指向 SemanticObject |
| requires_license | Feature → License |
| selects / sets_value_pattern | DecisionPoint → 下层对象 |
| supported_by | 任意对象 → EvidenceSource |

### 数据源

7 个 MD 文件 per scenario（`business-graph/{scenario}/three-layer-graph/`）：
- `01-business-graph.md`：BD、NS、CS、DP、BR、SO 对象 + 层内边
- `02-feature-graph.md`：Feature、SubFeature、License、FeatureRule
- `03-task-layer.md`：ConfigTask、TaskRule、TaskCommandOrderEdge
- `04-command-graph.md`：MMLCommand、ConfigObject、CommandParameter、CommandRule
- `05-cross-layer-mapping.md`：CS→Feature、CS→Task、Feature→Task、Task→Command 的显式边表
- `00-overview.md` / `06-evidence-index.md`：辅助信息

### 约束

- **不修改** `business-graph/` 目录下任何文件（设计态资产）
- MD 可能动态更新，后端需要轻量级解析（按需重解析）
- 当前只做一个业务域（业务感知），后续扩展时结构不变

## 设计方案

### 整体布局：纵向级联卡片 + 右侧详情面板

```
┌──────────────────────────────────────┬──────────────────────────┐
│  左栏：级联卡片树（60-65% 宽）         │  右栏：对象详情（35-40%）  │
│                                      │                          │
│  [BD 业务感知]                       │  对象头                   │
│      │ contains                      │  Schema 属性表            │
│      ├──[NS 计费场景] ●              │  关联关系分组              │
│      │      │ instantiated_as        │                          │
│      │      ├──[CS-01]──[CS-02]...   │                          │
│      │      │ uses_feature           │                          │
│      │      └──[GWFD-0171]──[GWFD]  │                          │
│      │                               │                          │
│      └──[NS 带宽控制场景]             │                          │
└──────────────────────────────────────┴──────────────────────────┘
```

### 左栏：级联卡片树

**组件：** CascadeTree.vue → CascadeNode.vue（递归）+ EdgeConnector.vue

**卡片结构（统一布局，内容因类型不同）：**
```
┌─────────────────────────────────────────┐
│ [类型徽章] ID 名称              ⟲共享    │
│ 一句话摘要                               │
│ N特性 · N任务 · N规则                   │
└─────────────────────────────────────────┘
```

**各类型卡片内容：**

| 类型 | 徽章 | 显示信息 |
|------|------|---------|
| BD | [业务域] | domain_name · domain_summary · N个场景 |
| NS | [场景] | scenario_name · scenario_summary · N个方案 |
| CS | [方案] | solution_name · solution_summary · N特性/N任务/N规则 |
| Feature | [特性] | feature_id · feature_name · feature_summary · N任务 |
| Task | [任务] | task_id · task_name · task_summary · N命令 |

**展开行为：**
- 页面初始：BD → 自动展开到 NS → 自动展开到 CS（3 层）
- 点击卡片主体：选中（右栏切换详情）+ 展开下一层子卡片
- 点击右侧箭头：仅展开/折叠，不切换右栏
- 同层兄弟卡片横向排列；超过 4 个换行
- Feature/Task 层按需展开，不默认展开

**连接线设计：**
- 父子卡片之间用竖线 + 关系标签连接（如 `│ uses_feature`）
- 同层兄弟卡片用横线串联
- 选中路径高亮，未选中分支淡化

**共享对象标记：**
- 被 >1 个父对象引用的对象卡片显示 `⟲共享` 角标
- 右栏详情中显示 `referenced_by (N)` 上游关系列表

### 右栏：对象详情面板

**组件：** ObjectDetail.vue → AttrTable.vue + RelGroup.vue

**3 个区块：**

1. **对象头**：类型徽章 + ID + 名称 + 一句话摘要
2. **Schema 属性表**：KV 表展示完整属性（从 MD 的 `字段|值` 表提取）
3. **关联关系分组**：按关系类型分组，每组可折叠

关系分组类型：
- **下游** `uses_feature` / `decomposes_to` / `invokes` / `operates_on`
- **上游** `referenced_by`（谁引用了我）
- **约束** `constrained_by`（规则）
- **决策** `has_decision` / `selects`
- **语义** `uses_semantic_object`
- **许可证** `requires_license`

每条关系项可点击 → 左栏树展开定位到该对象 + 右栏切换。

## 后端设计

### 数据模型

**统一对象格式：**
```json
{
  "object_id": "CS-CH-01",
  "type": "ConfigurationSolution",
  "name": "离线计费方案",
  "summary": "通过RG标识业务...",
  "layer": "business",
  "attributes": {
    "solution_id": "CS-CH-01",
    "solution_name": "离线计费方案",
    "design_intent": "...",
    "core_mechanism_combo": "...",
    "status": "active"
  }
}
```

**统一边格式：**
```json
{
  "from": "CS-CH-01",
  "relation": "uses_feature",
  "to": "GWFD-010171",
  "meta": {"role": "核心"}
}
```

### API

```
GET /api/v1/business-graph/scenarios/{scenario_id}/graph
```

返回完整图数据（单次加载，对象总量数百级，payload 可控）：
```json
{
  "objects": { "CS-CH-01": {...}, ... },
  "edges": [ {"from": "...", "relation": "...", "to": "..."}, ... ],
  "root_id": "BD-CH-01"
}
```

### 解析策略

在现有 `service.py` 基础上新增深度解析器 `graph_parser.py`：

**对象提取：**
- KV 表对象（BD/NS/CS/Feature/Task）：从 `### x.x ID 名称` 标题 + 紧跟的 `字段|值` 表提取
- 宽表对象（DP/BR/SO/License/Rule/Command/ConfigObject）：每行一个对象，列名为属性名

**边提取（两个来源合并去重）：**
1. 各层文件内联标记：`**uses_feature**: GWFD-010171、GWFD-020301`
2. `05-cross-layer-mapping.md` 显式边表（§1-§4）

**主链边类型（驱动树展开）：**
- `contains`（BD → NS）
- `instantiated_as`（NS → CS）
- `uses_feature`（CS → Feature）
- `decomposes_to`（Feature → Task）
- `invokes`（Task → Command）
- `operates_on`（Command → ConfigObject）

### 缓存

解析结果在内存中缓存（singleton service），MD 文件修改后需重启后端或手动刷新。不做文件监听（YAGNI）。

## 前端设计

### 组件结构

```
business_graph/
├── BusinessGraphIndex.vue      （已有，域级卡片入口）
├── BusinessScenario.vue        （改造：替换为 Explorer 布局）
├── CascadeTree.vue             （新建：左栏容器）
├── CascadeNode.vue             （新建：递归卡片节点）
├── ObjectDetail.vue            （新建：右栏详情面板）
├── AttrTable.vue               （新建：属性 KV 表）
└── RelGroup.vue                （新建：关系分组列表）
```

### 数据流

1. `BusinessScenario.vue` onMounted → 调用 `GET /graph` 获取完整图
2. 构建 adjacency map：`{parentId → [{child, relation, meta}]}`
3. 从 root_id 开始递归渲染 CascadeNode
4. CascadeNode 点击时：
   - emit select → 右栏 ObjectDetail 显示该对象
   - emit expand → 子节点列表 toggle 显示
5. ObjectDetail 关系项点击 → emit navigate → CascadeTree 展开到目标对象

### 样式要点

- 卡片：圆角、浅边框、hover 阴影、选中态左侧 accent 色条
- 连接线：1px 灰色竖线 + 关系标签（小号灰色文字）
- 共享角标：`⟲` 图标 + accent 色
- 层级缩进：每层缩进 24px-32px，不超过 5 层
- 右栏：粘性定位（sticky），可折叠

## 实现步骤

### Phase 1: 后端图解析器
1. 新建 `platform-next/business_graph/graph_parser.py`
2. 实现 KV 表对象提取（BD/NS/CS/Feature/Task）
3. 实现宽表对象提取（DP/BR/SO/License/Command/ConfigObject）
4. 实现边提取（内联标记 + 跨层映射边表）
5. 添加 `GET /scenarios/{id}/graph` API endpoint
6. 测试：验证计费场景 + 带宽控制场景的对象数和边数

### Phase 2: 前端级联卡片树
1. 新建 CascadeTree.vue + CascadeNode.vue
2. 加载 graph 数据，构建 adjacency map
3. 渲染 BD → NS → CS 三层卡片 + 连接线
4. 实现展开/折叠 + 选中状态

### Phase 3: 右侧详情面板
1. 新建 ObjectDetail.vue + AttrTable.vue + RelGroup.vue
2. 显示选中对象的 schema 属性 + 关系分组
3. 关系项点击跳转

### Phase 4: 深层展开 + 交互优化
1. Feature/Task 层展开
2. 共享对象标记
3. 连接线视觉优化
4. 路径高亮
