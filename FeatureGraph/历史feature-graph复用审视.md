# 历史 feature-graph 复用审视

> 结论：旧 `feature-graph/` 不再作为特性层 schema 来源，但其中的代码和抽取资产可以作为新 `FeatureGraph` 的种子数据、证据数据和 pipeline 改造基础。

---

## 1. 背景定位

历史 `feature-graph/` 的核心工作是从产品特性清单和特性文档中抽取 L1-L4 数据：

- L1：Feature 属性
- L2：DocAsset 文档资产
- L3：FeatureDependency 特性依赖
- L4：FeatureLicense 特性 License

新的三层图谱已经重新划分边界：

- 命令层由 `CommandGraph/` 承接
- 任务层由 `ConfigTask/` 承接
- 特性层由 `FeatureGraph/` 承接

因此历史目录里的 schema、跨层直连设计和部分对象定义不再继承；历史抽取结果、解析逻辑和审计经验可以复用。

---

## 2. 可直接复用的内容

### 2.1 Feature 种子数据

可复用资产：

- `feature-graph/data/UDG_features.csv`
- `feature-graph/data/UNC_features.csv`
- 历史 xlsx 特性清单

用途：

- 作为正式 `Feature` 节点的初始种子
- 保留产品侧正式特性编号、名称、产品域、版本和目录信息
- 后续统一转换为 JSONL

注意：

- 产品清单中的正式编号优先建 `Feature`
- 不应因为语义上像某个能力的子项而降级为 `SubFeature`

### 2.2 文档资产映射

可复用资产：

- `feature-graph/data/UDG_feature_files.csv`
- `feature-graph/data/UNC_feature_files.csv`
- `feature-graph/data/l1_udg_doc_assets.csv`
- `feature-graph/data/l1_unc_doc_assets.csv`

用途：

- 作为 `EvidenceSource` 或 `DocAsset` 的种子
- 支撑 `Feature / FeatureRule / License` 的证据追溯
- 为后续 Agent 深抽提供文档入口

注意：

- 历史 `doc_type` 分类可以保留为初始标签
- 不应把文档类型直接等同于特性层对象类型

### 2.3 License 抽取结果

可复用资产：

- `feature-graph/data/l1_udg_feature_license.csv`
- `feature-graph/data/l1_unc_feature_license.csv`
- `step4_extract_l1.py` 中的 License 表解析逻辑

用途：

- 生成 `License` 节点
- 生成 `Feature requires_license License` 关系
- 保留 `license_number / license_code / license_name / applicable_nf`

注意：

- License 开通命令不属于特性层
- License 配置动作应下沉到 `ConfigTask` 和 `CommandGraph`

### 2.4 依赖和互斥关系

可复用资产：

- `feature-graph/data/l1_udg_feature_dependency.csv`
- `feature-graph/data/l1_unc_feature_dependency.csv`
- 历史审计报告中的 dependency_type 和 conflict_pair_id 处理经验

可直接进入核心图谱的关系：

- `depends_on`
- `conflicts_with`

用途：

- 生成 `Feature depends_on Feature`
- 生成 `Feature conflicts_with Feature`
- 使用 `conflict_pair_id` 对互斥关系做对称去重和证据聚合

注意：

- 互斥是逻辑对称关系，历史双向证据可以保留，但展示和推理时需要按 pair 去重
- `affects / interacts_with / supports / other` 暂不直接进入核心图谱

### 2.5 抽取代码经验

可复用资产：

- `feature-graph/step4_extract_l1.py`
- `feature-graph/step1_extract_features.py`
- `feature-graph/step2_map_docs.py`
- `feature-graph/step3_audit_report.py`
- `feature-graph/audit_deps.py`

可复用能力：

- 从 xlsx 特性清单抽取 Feature seed
- 将 Feature 映射到文档资产
- 识别概述文档
- 解析固定章节
- 解析 License 表
- 解析特性依赖表
- 审计依赖和 License 抽取质量

注意：

- 这些脚本应改造成可配置 pipeline
- 输出应统一改为 JSONL
- 旧字段命名和旧 schema 不应原样固化

---

## 3. 需要改造后复用的内容

### 3.1 Feature 属性抽取

可复用资产：

- `feature-graph/data/l1_udg_feature_attributes.csv`
- `feature-graph/data/l1_unc_feature_attributes.csv`

历史字段包括：

- `definition`
- `customer_value`
- `application_scenario`
- `system_impact`
- `restrictions`
- `spec`
- `standards`
- `first_release_version`
- `nf_support_map`
- `applicable_nf`

改造原则：

- 不把所有历史字段都变成第一版 `Feature` 核心属性
- 长文本字段优先作为证据摘要或原文事实保留
- 核心 Feature 属性保持克制，优先服务对象识别、关系抽取和跨层链接

### 3.2 feature_type 和 config_required

历史字段：

- `feature_type`
- `config_required`

改造判断：

- 历史 `feature_type=config_enable` 粒度偏粗
- `config_required` 不能只靠特性概述判断
- 后续应结合 `ConfigTask` 覆盖情况重新计算

建议新口径：

- `feature_category`：基础能力、增强能力、集成能力、运维能力、协议能力等
- `config_relevance`：需要配置、间接配置、无需配置、仅运维触发等

### 3.3 parent_feature_id

历史字段：

- `parent_feature_id`

改造判断：

- 它更接近产品目录层级或清单结构
- 不等同于能力依赖
- 不应映射为 `depends_on`

建议用途：

- 保留为产品目录关系或 `catalog_parent`
- 用于导航、聚合和展示
- 不参与能力依赖推理

### 3.4 弱语义依赖

历史 dependency_type 中存在：

- `affects`
- `interacts_with`
- `supports`
- `other`

改造判断：

- 这些类型语义不够稳定
- 不应直接进入核心 `depends_on`
- 可作为候选关系进入 staging

建议用途：

- 统一转为 `FeatureRelationCandidate`
- 人工或 Agent 审核后再决定是否映射为 `cooperates_with`、`constrained_by` 或丢弃

---

## 4. 明确废弃的内容

### 4.1 旧特性层 schema

历史 `FEATURE_GRAPH_SCHEMA.md` 已过期，不再作为定义来源。

废弃原因：

- 与当前三层图谱边界不一致
- 存在 Feature 直接下沉到命令或配置对象的倾向
- 和当前 `CommandGraph`、`ConfigTask` 的对象归口重复

### 4.2 Feature 直连命令或配置对象

废弃模式：

```text
Feature -> MMLCommand
Feature -> CommandParameter
Feature -> ConfigObject
Feature -> ConfigStep -> Command
```

新模式：

```text
Feature
  -> ConfigTask
  -> MMLCommand / CommandParameter / ConfigObject
```

### 4.3 旧 L5-L8 中的跨层对象

不再继承的旧对象方向：

- 特性层 `ConfigStep`
- 特性层 `ConfigObject`
- 特性层 `ProcedureVariant`
- 特性层 `ValidationRule`

归口调整：

- 配置步骤和命令序列归 `ConfigTask`
- 配置对象归 `CommandGraph`
- task 内规则归 `TaskRule`
- 命令级校验归 `CommandRule`
- 能力级规则才归 `FeatureRule`

---

## 5. 后续 JSONL 与 pipeline 改造方向

### 5.1 目标

逐步补齐特性层对象和关系定义，并将历史可用代码和资产统一转换为：

- JSONL 数据资产
- 可配置抽取 pipeline
- 可审计的中间产物
- 可回放的抽取链路

### 5.2 建议 pipeline 分层

```text
raw assets
  -> seed extraction
  -> staging jsonl
  -> relation normalization
  -> candidate review
  -> final FeatureGraph jsonl
```

### 5.3 建议阶段

阶段一：Feature seed

- 输入：xlsx、`UDG_features.csv`、`UNC_features.csv`
- 输出：`feature_nodes.staging.jsonl`
- 目标：建立正式 Feature 池

阶段二：Evidence seed

- 输入：feature_files、doc_assets
- 输出：`evidence_sources.staging.jsonl`
- 目标：建立 Feature 到文档证据的链接

阶段三：License seed

- 输入：feature_license CSV
- 输出：`licenses.staging.jsonl`、`feature_requires_license.staging.jsonl`
- 目标：建立 License 节点和 License 门控关系

阶段四：Dependency seed

- 输入：feature_dependency CSV
- 输出：`feature_relations.staging.jsonl`
- 目标：沉淀强关系和候选弱关系

阶段五：Task mapping

- 输入：`ConfigTask` 聚类与深抽结果
- 输出：`feature_decomposes_to_task.jsonl`、`feature_task_order_edges.jsonl`
- 目标：建立 Feature 到任务层的唯一跨层通道

阶段六：Audit

- 检查 Feature 是否直连命令、参数、配置对象
- 检查正式特性编号是否被误建为 SubFeature
- 检查弱关系是否未经审核进入核心关系
- 检查 License、Dependency、Evidence 是否有来源

---

## 6. 当前结论

历史 `feature-graph/` 的定位应调整为：

```text
历史 schema：废弃
历史 CSV：作为 seed / staging 资产复用
历史脚本：改造成可配置 JSONL pipeline
历史审计报告：作为抽取规则和质量门禁依据
```

新 `FeatureGraph` 的建设顺序应是：

```text
先稳对象和关系
再接历史种子数据
再统一 JSONL 格式
最后沉淀可配置 pipeline
```

