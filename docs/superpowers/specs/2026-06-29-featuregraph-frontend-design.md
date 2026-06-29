# 特性图谱前端展示设计（platform-next）

> 状态：设计稿（brainstorming 产出，待 review + 用户确认 → writing-plans）
> 日期：2026-06-29
> 参考：命令图谱（platform-next/command_graph + frontend/src/command_graph）

## 1. 背景与目标

platform-next 下特性图谱前端展示，参考命令图谱已有的三级结构（首页统计 → 网元版本列表 → 详情左右侧）复刻。数据源用新 FeatureGraph JSONL 流水线产物。

特性图谱相比命令图谱的差异点：
- 特性详情页右侧要展示**多个 md**（命令图谱是单 md）
- 特性关系是**特性间**关系图（命令图谱是参数关系图），复用命令图谱统一图结构

## 2. 边界（设计态 vs 展示态）

| 层 | 目录 | 处理 |
|---|---|---|
| **设计态（保留）** | `FeatureGraph/`（builder/build_all.py/pipeline.yaml/data/） | 数据生产流水线，不动 |
| **展示态-后端（删除重建）** | `platform-next/feature_graph/`（service/router/review_service/column_config） | 旧 CSV 体系，全删重建 |
| **展示态-前端（删除重建）** | `platform-next/frontend/src/feature_graph/`（5 个旧 Vue） | 字段过期，全删重建 |
| **数据桥** | `FeatureGraph/data/{nf}/{version}/*.jsonl` | 新后端 service 读取 |

**不在范围**（本次不做）：
- 关系审查功能（旧 review_service 的接受/拒绝弱关系）—— 用户明确不要
- decomposes_to（特性 → ConfigTask 任务层接入）—— 第一版未建
- SubFeature 独立对象类型 —— 已用 feature_code `-N` 后缀表达，前端按普通 Feature 渲染

## 2A. 前置依赖（设计态 source_evidence_ids 恢复为全部 md）

多 md 展示需要该特性的全部 md 路径。当前 `features.jsonl` 的 `source_evidence_ids` 被收紧为仅概述 path（如 GWFD-020301 只 1 条，实际有 5 个 md：概述/其他/参考/原理/部署），**不足以支撑多 md**。

**设计态改动（FeatureGraph/builder）**：`source_evidence_ids` 恢复为该特性的**全部 md 路径**（概述/激活/原理/参考/调测/...），不收紧。

- 文档都是 md，**不需要 doc_type 分类，不需要 doc_assets 字段**——文件名已含类型信息（"特性概述"/"激活XXX"/"实现原理"/"参考信息"）
- 来源：`FeatureGraph/builder/steps/feature.py` 的 `find_overview_md` 返回的 doc_assets 列表含全部 md，把所有 path 写入 source_evidence_ids（不只概述）
- 前端用 source_evidence_ids（path 列表）做 md 切换，文件名做标签
- service 的 `get_feature_docs` 读 source_evidence_ids + 从文件名/H1 解析 title，纯字段读取不扫 FS

**此为前端展示的前置条件**——先恢复 source_evidence_ids 全部 md，再做前端。

## 3. 整体架构

```text
FeatureGraph/data/{nf}/{version}/*.jsonl   （设计态产物，数据源）
        ↓ 启动扫描
platform-next/feature_graph/service.py     （新后端，复刻 command_graph/service.py）
        ↓ 内存 _adjacency + REST 端点
platform-next/feature_graph/router.py
        ↓ HTTP
frontend/src/feature_graph/*.vue           （新前端，复刻 command_graph/*.vue）
        ├─ FeatureOverview.vue   首页统计 + 网元版本入口
        ├─ FeatureListPage.vue   网元版本页（两 tab：特性 / license）
        ├─ FeatureDetail.vue     特性详情（左右侧）
        └─ LicenseDetail.vue     license 详情（左右侧）
```

## 4. 路由设计（三级，对齐命令图谱）

| 路由 | 页面组件 | 对应命令图谱 | 说明 |
|---|---|---|---|
| `/feature` | FeatureOverview | CommandOverview | 首页：统计量（特性/license/关系数）+ 网元版本卡片网格 |
| `/feature/:nf/:version` | FeatureListPage | CommandList（+tab） | 网元版本页：**两 tab**（特性列表 / license 列表），各自表格+筛选+分页 |
| `/feature/:nf/:version/feature/:code` | FeatureDetail | CommandDetail | 特性详情：左右侧 |
| `/feature/:nf/:version/license/:code` | LicenseDetail | （命令图谱无，新建） | license 详情：左右侧 |

`:code` 为 feature_code（如 `GWFD-020301`）或 license_code（如 `LKV3G5BCBC01`）。
子特性（多概述拆分）的 code 形如 `GWFD-010101-1`，按普通 Feature 路由即可。

## 5. 后端 service.py（复刻 command_graph/service.py）

### 5.1 数据加载
启动扫描 `FeatureGraph/data/*/*/*.jsonl`，按文件名分桶（路径 `{nf}/{version}/{file}.jsonl`）：

| 文件 | 加载到 |
|---|---|
| `features.jsonl` | `self._features[(nf,version)]` + `self._feat_by_id` |
| `licenses.jsonl` | `self._licenses[(nf,version)]` + `self._lic_by_id` |
| `feature_relations.jsonl` | `self._relations[(nf,version)]` |
| `feature_requires_license.jsonl` | `self._req_lic[(nf,version)]` |

### 5.2 统一图（复用命令图谱 _adjacency 模型）
`_load_graph()` 聚合：
- 点：Feature（type=feature）、License（type=license）
- 边：feature_relations（实际数据 relation_type：depends_on/conflicts_with/affects/interacts_with/supports；**cooperates_with 当前未挖掘，预留**）、requires_license
- **parent_feature_code 不进关系图**（仅作 Feature 节点字段存储，目录父子树不遍历，避免目录节点污染特性关系图）

`get_feature_graph(nf, version, code, hops=1, edge_types=None)` → `{nodes:[{id,type,label,properties}], edges:[{from,to,type,properties}]}`，BFS 子图（复用 command_graph/service.py:get_subgraph 逻辑）。默认 hops=1 防爆炸，edge_types 白名单过滤（默认 depends_on+conflicts_with）。

### 5.3 接口方法签名

```python
# 首页统计（驱动 L1）
get_stats() -> {total_features, total_licenses, total_relations, ne_versions:[{nf,version,feature_count,license_count,relation_count}], nes:[...]}

# 网元版本页 - 特性列表（L2 tab1）
list_features(nf, version, search=None, feature_category=None, page=1, size=50) -> {total,page,size,items:[slim]}
# slim: {feature_code, name, feature_category, config_relevance, applicable_nf, has_overview}

# 网元版本页 - license 列表（L2 tab2）
list_licenses(nf, version, search=None, page=1, size=50) -> {total,page,size,items:[slim]}
# slim: {license_code, name, control_item_id, applicable_nf, control_item_type}

# 特性详情（L3）
get_feature(nf, version, code) -> full feature record
get_feature_docs(nf, version, code) -> [{doc_path, doc_title}]  # 读 features.jsonl 的 source_evidence_ids（全部md路径），doc_title 从文件名/H1 解析
get_feature_graph(nf, version, code, hops=1, edge_types=None) -> {nodes, edges}  # 统一图，默认1跳防爆炸，edge_types 白名单过滤
get_feature_relations(nf, version, code) -> [edge]  # 该特性参与的边（表格用，悬空 target 回退显示原始 code）
get_feature_licenses(nf, version, code) -> [license_edge]  # 该特性需要的 license

# license 详情（L3）
get_license(nf, version, code) -> full license record
get_license_features(nf, version, code) -> [feature_code]  # 反查哪些特性需要此 license（feature_refs）

# md 内容（L3 右侧 DocViewer）
get_doc_content(rel_path) -> str  # 读 md，路径防穿越
resolve_doc_path(rel_path) -> Path | None  # 图片等静态文件
```

`get_feature_docs` 多 md 来源：**读 `features.jsonl` 的 `source_evidence_ids`**（设计态恢复为全部 md 路径，见 §2A），不扫描文件系统。返回 `[{doc_path, doc_title}]`，doc_title 从文件名或 H1 解析。空 source_evidence_ids（无文档特性）返回 []，前端显示"无文档"空状态。

## 6. 后端 router.py（REST 端点，对齐命令图谱风格）

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/api/v1/feature-graph/stats` | 首页统计 |
| GET | `/api/v1/feature-graph/features?nf=&version=&search=&category=&page=&size=` | 特性列表 |
| GET | `/api/v1/feature-graph/licenses?nf=&version=&search=&page=&size=` | license 列表 |
| GET | `/api/v1/feature-graph/feature?nf=&version=&code=` | 特性详情 |
| GET | `/api/v1/feature-graph/feature-docs?nf=&version=&code=` | 特性多 md 列表 |
| GET | `/api/v1/feature-graph/feature-graph?nf=&version=&code=&hops=` | 特性关系图（统一 {nodes,edges}） |
| GET | `/api/v1/feature-graph/license?nf=&version=&code=` | license 详情 |
| GET | `/api/v1/feature-graph/doc-content?path=` | md 内容 |
| GET | `/api/v1/feature-graph/file?path=` | 图片等静态文件 |

## 7. 前端页面组件

### 7.1 FeatureOverview.vue（← CommandOverview.vue）
- 统计量卡片：总特性数 / 总 license 数 / 总关系数
- 网元版本卡片网格：每卡片 `nf@version` + 特性数/license数/关系数徽章，点击跳 `/feature/:nf/:version`

### 7.2 FeatureListPage.vue（← CommandList.vue + tab）
- 顶部两 tab：**特性** / **license**
- 特性 tab：表格（feature_code/name/feature_category/config_relevance/applicable_nf），筛选（搜索/category），分页，点行跳特性详情
- license tab：表格（license_code/name/control_item_id/applicable_nf），筛选，分页，点行跳 license 详情

### 7.3 FeatureDetail.vue（← CommandDetail.vue）
左右侧布局（可拖拽分隔条，复用命令图谱 cmd-divider）：
- **左侧**（多 tab）：
  - `特性` tab：特性属性字段（feature_code/name/catalog_section/feature_category/config_relevance/applicable_nf/nf_support_map/first_release_version/standards/category_reason 等），数据驱动渲染
  - `特性关系` tab：上部 vis-network 关系图（统一 {nodes,edges}，复用命令图谱图组件）+ 下部关系表格（related_feature/relation_type/interaction_note）
  - `license` tab：该特性需要的 license 列表（点跳 license 详情）
- **右侧**：DocViewer + **顶部 md 切换**（文件名/doc_title，来自 get_feature_docs 的 source_evidence_ids），选中渲染对应 md

### 7.4 LicenseDetail.vue（新建）
左右侧布局：
- **左侧**：
  - `license` tab：license 属性（license_code/control_item_id/name/license_domain/control_item_type/applicable_nf/value_range/default_value/description/feature_refs）
  - `关联特性` tab：feature_refs 列表（点跳特性详情）
- **右侧**：DocViewer（license 控制项 md，来自 license.source_path，单一）

### 7.5 复用组件
- `shared/DocViewer.vue`：md 渲染（markdown-it + DOMPurify + 图片路径重写），不变
- `shared/markdown.ts`：markdown 配置，不变
- vis-network 图渲染：复用命令图谱 CommandGraph.vue 的 vis-network 配置 + 数据格式（吃统一 {nodes,edges}）

## 8. 多 md 展示机制

特性详情右侧顶部 md 切换：
1. 进入详情 → 调 `get_feature_docs(nf,version,code)` 返回 `[{doc_path,doc_title}]`（数据来自 source_evidence_ids，见 §2A）
2. 顶部渲染 md 切换（按 doc_title/文件名），默认选第一个（或含"概述"的）
3. 选中 → 调 `get_doc_content(doc_path)` → DocViewer 渲染
4. md 内图片/交叉引用走 `/api/v1/feature-graph/file` + `/doc-content`（复用命令图谱 DocViewer 的路径重写）
5. **空状态**：source_evidence_ids 为空（无文档特性）→ 右侧显示"该特性无产品文档"占位，不调 DocViewer

命令图谱单 md（source_evidence_ids[0]）→ 特性图谱多 md（doc_type tab 切换），DocViewer 本身复用（已支持 feature-graph/command-graph 双 base path，无需改）。

## 9. 特性关系图（统一结构复用 + 独立渲染组件）

后端 `get_feature_graph(code, hops=1, edge_types=None)` 复用命令图谱 `get_subgraph` 模型：
- `{nodes:[{id,type,label,properties}], edges:[{from,to,type,properties}]}`
- BFS 从中心特性（code）N 跳，默认 **hops=1**（防高连接特性图爆炸），前端提供"展开"控件调 hops=2
- `edge_types` 白名单（默认 depends_on+conflicts_with，可加 cooperates_with/affects 等）
- 节点 type=feature，边 type=关系类型（实际数据：depends_on/conflicts_with/affects/interacts_with/supports；cooperates_with 当前未挖掘，预留）

**前端图组件不直接复用 CommandGraph.vue**（其 buildVisNodes/buildVisEdges 硬编码命令图谱 type→group/颜色 + edge→样式，特性节点/边无样式规则）。

方案：新建 `shared/RelationGraphBase.vue`（吃统一 `{nodes,edges}` + `nodeTypeConfig`/`edgeTypeConfig` 配置映射），命令图谱 CommandGraph.vue 和特性 `FeatureRelationGraph.vue` 都基于它扩展。特性图配置：
- 节点：type=feature → 蓝色方块（中心特性高亮）
- 边：depends_on 实线灰、conflicts_with 红色、affects/interacts_with/supports 虚线灰，边 label=relation_type
- 点节点跳对应特性详情

（若不想抽 base，可简化为新建 `FeatureRelationGraph.vue` 独立配置 vis-network，不复用 CommandGraph.vue。两者皆可，实现时定。）

## 10. 配置（重写 config.yaml feature_graph 块）

现有 `platform-next/config.yaml` 的 `feature_graph` 块用旧键（`data_dir` + `columns:` 用过期字段 feature_id/feature_name/product_type）。**本次完全重写该块**（删 data_dir/columns，加 assets_root/doc_root），对齐 command_graph 模式：
```yaml
feature_graph:
  assets_root: ../FeatureGraph/data   # 设计态产物（相对 platform-next/ 根，同 command_graph 的 ../CommandGraph/data/assets）
  doc_root: ..                         # 仓库根（读 md，output/... 路径，同 command_graph）
```
实现时确认旧 `columns` 列表不残留（避免新 service 继承过期字段）。

## 11. 废弃清单（删除 platform-next 前后端，保留 FeatureGraph/ 设计态）

**删除（展示态-后端）**：
- `platform-next/feature_graph/service.py`（旧 CSV）
- `platform-next/feature_graph/router.py`（旧）
- `platform-next/feature_graph/review_service.py`（审查功能，不要）
- `platform-next/feature_graph/column_config.py`（旧字段配置）
- `platform-next/feature_graph/__init__.py`（重建）

**删除（展示态-前端）**：
- `platform-next/frontend/src/feature_graph/FeatureIndex.vue`
- `platform-next/frontend/src/feature_graph/FeatureList.vue`
- `platform-next/frontend/src/feature_graph/FeatureRelations.vue`
- `platform-next/frontend/src/feature_graph/FeatureLicenses.vue`
- `platform-next/frontend/src/feature_graph/FeatureDetail.vue`

**保留（设计态）**：`FeatureGraph/`（抽取流水线 + data/）。本次还要在 `FeatureGraph/builder` 恢复 source_evidence_ids 为全部 md（见 §2A）。

## 12. 验收标准

- 首页展示特性/license/关系统计 + 网元版本卡片（UDG/UNC）
- 网元版本页两 tab（特性/license）可切换、筛选、分页
- 特性详情左右侧：左侧三 tab（特性属性/特性关系图/license关联），右侧多 md（doc_type tab 切换）
- 特性关系图复用命令图谱 vis-network 统一结构，点节点跳转
- license 详情左右侧：license 字段 + 关联特性 + md
- 数据全部来自新 JSONL（不依赖旧 CSV）
- 旧 feature_graph 前后端删除干净，FeatureGraph/ 设计态不动

## 13. 关键复用对照（实现时参考）

| 特性图谱新建 | 命令图谱参考 | 复用程度 |
|---|---|---|
| feature_graph/service.py | command_graph/service.py（_load/get_stats/list/get_xxx/get_subgraph） | 结构复刻，字段换特性域 |
| feature_graph/router.py | command_graph/router.py | 端点风格复刻 |
| FeatureOverview.vue | command_graph/CommandOverview.vue | 结构复刻 |
| FeatureListPage.vue | command_graph/CommandList.vue（+tab） | 复刻 + 加两 tab |
| FeatureDetail.vue | command_graph/CommandDetail.vue | 复刻（左侧 tab 内容换特性域） |
| LicenseDetail.vue | command_graph/CommandDetail.vue（简化） | 参考结构 |
| 特性关系图渲染 | command_graph/CommandGraph.vue | **不直接复用**（type/edge 样式硬编码命令域）；建 shared/RelationGraphBase.vue 或独立 FeatureRelationGraph.vue（见 §9） |
| md 渲染 | shared/DocViewer.vue | **复用不变**（已支持 feature-graph/command-graph 双 base path） |
