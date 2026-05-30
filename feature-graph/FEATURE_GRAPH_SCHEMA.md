# 特性图谱 Schema 定义

## 1. 特性图谱是什么

特性图谱是三层知识图谱的**中间层**：

```text
业务图谱 (Business Graph)
    ↕  requires_capability / realized_by_feature
特性图谱 (Feature Graph)        ← 本文档定义
    ↕  uses_command / has_config_object
命令图谱 (Command Graph)        ← 已有
```

特性图谱不是：

- 特性清单表格（xlsx已提供）
- 文档目录索引（Step 2映射已提供）
- 命令手册（命令图谱的职责）

特性图谱是：

```text
把每个产品特性"是什么、怎么配、涉及什么配置对象、有哪些配置场景、依赖谁、怎么验证"
组织成一套结构化对象网络，使Agent能真正基于特性知识执行配置生成、配置核查和故障定位。
```

特性图谱需要能回答以下问题：

1. 这个特性是什么？适用哪些NF？需要什么License？
2. 这个特性怎么配置？有哪些配置场景？每个场景的MML命令序列是什么？
3. 配置对象之间是什么层级关系？（直接桥接命令图谱）
4. 它依赖哪些特性？被谁依赖？
5. 配置时有什么约束和验证点？
6. 它的知识文档在哪里？

---

## 2. 数据模型：点与边

### 2.1 总览

```text
7 张节点表（点） + 2 张边表（关系）
```

| 类型 | 表名 | 中文名 | 说明 |
|------|------|--------|------|
| 节点 | Feature | 特性 | 主节点，xlsx每行一个 |
| 节点 | SubFeature | 子特性 | 按代际拆分（可选） |
| 节点 | ProcedureVariant | 配置场景 | 同一特性的不同配置路径 |
| 节点 | ConfigStep | 配置步骤 | 有序步骤，含MML命令 |
| 节点 | ConfigObject | 配置对象 | MML配置对象（URR、RULE等） |
| 节点 | ValidationRule | 验证规则 | 配置约束和一致性检查 |
| 节点 | DocAsset | 知识文档 | 特性关联的md文件 |
| 边 | FeatureDependency | 特性依赖关系 | 特性间依赖/互斥/协同（边有额外属性，需单独表） |
| 边 | FeatureLicense | 特性License映射 | 特性与License的一对多映射 |

### 2.2 边的承载方式

**方式A：内嵌在节点表的外键字段中**（不需要单独的表）

| 边 | 起点→终点 | 承载字段 | 说明 |
|----|-----------|---------|------|
| 父子层级 | Feature → Feature | Feature.`parent_feature_id` | 目录特性与叶子特性 |
| 所属特性 | SubFeature → Feature | SubFeature.`feature_id` | 子特性属于哪个特性 |
| 所属特性 | ProcedureVariant → Feature | ProcedureVariant.`feature_id` | 场景属于哪个特性 |
| 所属场景 | ConfigStep → ProcedureVariant | ConfigStep.`procedure_variant_id` | 步骤属于哪个场景 |
| 操作对象 | ConfigStep → ConfigObject | ConfigStep.`config_object` | 该步骤操作哪个配置对象 |
| 父子层级 | ConfigObject → ConfigObject | ConfigObject.`parent_object` | 配置对象的包含关系 |
| 所属特性 | ValidationRule → Feature | ValidationRule.`feature_id` | 规则属于哪个特性 |
| 所属特性 | DocAsset → Feature | DocAsset.`feature_id` | 文档属于哪个特性 |

**方式B：单独的关系表**（边本身有额外属性）

| 边 | 起点→终点 | 承载表 | 额外属性 |
|----|-----------|--------|---------|
| 依赖/互斥 | Feature → Feature | FeatureDependency | dependency_type, description, license_control_item, source_type |
| License映射 | Feature → License信息 | FeatureLicense | license_code, license_name, license_number, applicable_nf |

### 2.3 内化到Feature字段的（不单独建表）

| 原对象 | 处理方式 | Feature中的字段 |
|--------|---------|----------------|
| NF | 不单独建表，作为Feature属性 | `nf_support_map`（来自xlsx NF列）、`applicable_nf`（来自概述） |
| Standard | 不单独建表，作为Feature属性 | `standards`（文本列表，如 `3GPP 29.244, 3GPP 23.502`） |

### 2.4 图结构可视化

```text
Feature
  │
  ├──[parent_feature_id]────────→ Feature (目录特性层级)
  │
  ├── SubFeature.feature_id ────→ SubFeature
  │    (按代际拆分, 可选)            └── DocAsset (子特性自己的文档)
  │
  ├── ProcedureVariant.feature_id → ProcedureVariant (配置场景)
  │                                    └── ConfigStep.procedure_variant_id
  │                                          ├── config_object → ConfigObject
  │                                          │                    └── parent_object → ConfigObject
  │                                          └── [mml_command] → 命令图谱.Command
  │
  ├── ValidationRule.feature_id → ValidationRule
  │
  ├── DocAsset.feature_id ──────→ DocAsset
  │
  ├── FeatureDependency表 ─────→ Feature (depends_on / conflicts_with / cooperates_with)
  │    (边表, 有额外属性)
  │
  └── FeatureLicense表 ─────────→ License信息 (一对多)
       (映射表)
```

---

## 3. 节点详细定义

### 3.1 Feature（特性）

```text
作用: 特性图谱的主节点，每个xlsx中的特性条目对应一个Feature实例。
来源: xlsx特性清单 + 概述md的固定section。
承载的边: parent_feature_id(父子)、nf/support/standards(内化属性)
```

| 字段名 | 类型 | 含义 | 来源 | 示例 |
|--------|------|------|------|------|
| `id` | string | 全局唯一标识 | 拼接 | `UDG:GWFD-020301` |
| `feature_id` | string | xlsx中的特性编号 | xlsx | `GWFD-020301` |
| `feature_name` | string | 特性名称 | xlsx | `内容计费基本功能` |
| `product_type` | enum | 产品类型 | xlsx | `UDG` / `UNC` |
| `product_version` | string | 产品版本 | xlsx | `20.15.2` |
| `is_directory` | boolean | 是否为目录特性 | xlsx | `false` |
| `section` | string | 所属分组 | xlsx | `计费功能` |
| **`parent_feature_id`** | string | 父特性ID（**边：父子层级**） | xlsx | `GWFD-020300` |
| `nf_support_map` | map | 各NF的支持状态（**内化：NF**） | xlsx NF列 | `{"UPF(5G)": "E", "S/PGW-U(4G)": "M"}` |
| `applicable_nf` | list | 适用NF列表（更详细，来自概述） | 概述-适用NF | `["SGW-U", "PGW-U", "UPF"]` |
| `feature_type` | enum | 特性类型 | 推断 | `protocol_base` / `config_enable` / `business_policy` |
| `definition` | text | 一句话定义 | 概述-定义 | `基于业务的计费，通过包过滤和分析技术...` |
| `customer_value` | text | 客户价值 | 概述-客户价值 | `运营商：基于用户访问的具体业务进行收费...` |
| `application_scenario` | text | 应用场景 | 概述-应用场景 | `当运营商希望区分用户数据流中的内容所属的业务类型...` |
| `system_impact` | text | 对系统的影响 | 概述-系统影响 | `三四层解析对系统吞吐量影响较小，七层解析影响较大` |
| `restrictions` | text | 应用限制 | 概述-应用限制 | `不包含对加密协议报文的解析功能` |
| `spec` | text | 特性规格 | 概述-特性规格 | `每APN/DNN绑定16个地址池` |
| `standards` | list | 遵循标准（**内化：Standard**） | 概述-遵循标准 | `["3GPP 23.502 Release 15", "3GPP 29.244"]` |
| `first_release_version` | string | 首次发布版本 | 概述-发布历史 | `20.0.0` |
| `config_required` | boolean | 是否需要配置 | 推断 | `true` / `false` |

**feature_type 取值说明：**

| 类型 | 含义 | 典型特征 | 示例 |
|------|------|---------|------|
| `protocol_base` | 协议基础型 | 无需配置，协议层面运行时行为 | GWFD-010101 会话管理 |
| `config_enable` | 配置使能型 | 有明确MML配置步骤，配置对象链清晰 | GWFD-010105 用户地址分配 |
| `business_policy` | 业务策略型 | 配置步骤复杂，涉及多配置对象链和策略组合 | GWFD-020301 内容计费 |

---

### 3.2 SubFeature（子特性）

```text
作用: 当一个特性跨多个代际（2G/3G、4G、5G）时，按代际拆分为子特性。
      不是所有特性都有子特性（如GWFD-010105就没有）。
来源: 文档目录结构（如 GWFD-010101 下的 2_3G会话管理/、4G会话管理/、5G会话管理/）。
承载的边: feature_id(所属特性)
```

| 字段名 | 类型 | 含义 | 来源 | 示例 |
|--------|------|------|------|------|
| `id` | string | 全局唯一标识 | 拼接 | `GWFD-010101:5G` |
| **`feature_id`** | string | 父特性ID（**边：所属特性**） | 关联 | `GWFD-010101` |
| `generation` | enum | 代际 | 目录名推断 | `2_3G` / `4G` / `5G` |
| `sub_feature_name` | string | 子特性名称 | 概述标题 | `会话管理（5G）` |
| `applicable_nf` | list | 适用NF列表 | 概述-适用NF | `["UPF"]` |
| `definition` | text | 代际特有定义 | 概述-定义 | `PDU会话的建立、修改、释放...` |
| `minimum_product_version` | string | 最低产品版本 | 概述-可获得性 | `20.0.0` |
| `minimum_unc_version` | string | 最低UNC版本 | 概述-可获得性 | `20.0.0` |

---

### 3.3 ProcedureVariant（配置场景）

```text
作用: 同一特性下有多种配置路径时，每种路径是一个ProcedureVariant。
      例如用户地址分配有4种方式，内容计费有4种典型场景。
来源: 激活/部署文档的子页面或操作场景分类。
承载的边: feature_id(所属特性)
```

| 字段名 | 类型 | 含义 | 来源 | 示例 |
|--------|------|------|------|------|
| `id` | string | 唯一标识 | 拼接 | `GWFD-010105:APN_DNN` |
| **`feature_id`** | string | 所属特性（**边：所属特性**） | 关联 | `GWFD-010105` |
| `variant_name` | string | 场景名称 | 激活文档 | `基于APN_DNN分配地址` |
| `variant_type` | enum | 场景类型 | 推断 | `primary` / `alternative` / `fallback` |
| `description` | text | 场景描述 | 激活文档 | `最基础的地址分配场景` |
| `doc_path` | string | 对应的激活文档路径 | Step 2 | `output/.../基于APN_DNN分配地址_72547232.md` |
| `prerequisite` | text | 前置条件 | 激活文档 | `已完成VPN实例和APN创建` |

---

### 3.4 ConfigStep（配置步骤）

```text
作用: ProcedureVariant中的有序配置步骤，每步对应一条MML命令。
      这是特性图谱桥接到命令图谱的核心连接点。
来源: 激活/部署文档中的操作步骤和数据规划表。
承载的边: procedure_variant_id(所属场景)、config_object(操作对象)
```

| 字段名 | 类型 | 含义 | 来源 | 示例 |
|--------|------|------|------|------|
| `id` | string | 唯一标识 | 拼接 | `GWFD-020301:url_charging:01` |
| **`procedure_variant_id`** | string | 所属配置场景（**边：所属场景**） | 关联 | `GWFD-020301:url_charging` |
| `step_order` | integer | 步骤序号 | 激活文档 | `1` |
| `step_name` | string | 步骤名称 | 激活文档 | `配置URR` |
| `mml_command` | string | MML命令名 | 激活文档 | `ADD URR` |
| **`config_object`** | string | 操作的配置对象（**边：操作对象**） | 激活文档 | `URR` |
| `key_parameters` | list | 关键参数及示例值 | 数据规划表 | `[{"name": "URRID", "value": "1", "desc": "URR编号"}]` |
| `purpose` | text | 本步骤目的 | 激活文档 | `定义使用量上报规则，指定计费模式和统计类型` |
| `is_activation_step` | boolean | 是否为激活/提交类命令 | 推断 | `true`（如SET REFRESHSRV） |

---

### 3.5 ConfigObject（配置对象）

```text
作用: 特性涉及的MML配置对象，以及它们之间的层级关系。
      直接桥接命令图谱——命令图谱中的ConfigObject是同一个实体。
来源: 激活/部署文档中的MML命令和数据规划，以及参考信息中的命令清单。
承载的边: parent_object(父子层级)
```

| 字段名 | 类型 | 含义 | 来源 | 示例 |
|--------|------|------|------|------|
| `id` | string | 配置对象名 | MML命令名推导 | `URR` |
| `object_name` | string | 对象中文名 | 激活文档 | `使用量上报规则` |
| **`parent_object`** | string | 父级配置对象（**边：父子层级**） | 层级关系 | `URRGROUP` |
| `mml_commands` | list | 操作该对象的MML命令 | 参考信息 | `["ADD URR", "LST URR", "RMV URR"]` |
| `description` | text | 对象在特性中的作用 | 激活文档 | `定义计费模式(在线/离线)和统计类型(流量/时长)` |
| `feature_scope` | list | 该对象在哪些特性中出现 | 汇总 | `["GWFD-020301", "GWFD-020300"]` |

---

### 3.6 ValidationRule（验证规则）

```text
作用: 配置时的约束条件和一致性检查点，支持配置核查和故障定位。
来源: 部署文档中的约束说明、调测文档中的排障步骤。
承载的边: feature_id(所属特性)
```

| 字段名 | 类型 | 含义 | 来源 | 示例 |
|--------|------|------|------|------|
| `id` | string | 唯一标识 | 拼接 | `GWFD-020301:cp_up_consistency` |
| **`feature_id`** | string | 所属特性（**边：所属特性**） | 关联 | `GWFD-020301` |
| `rule_type` | enum | 规则类型 | 推断 | `cross_nf_consistency` / `parameter_range` / `activation_order` / `naming_convention` |
| `description` | text | 规则描述 | 部署文档 | `URRID/USAGERPTMODE需在SMF和UPF间保持一致` |
| `check_method` | text | 检查方法 | 调测文档 | `DSP SESSIONINFO查看URRID是否与SMF配置一致` |
| `severity` | enum | 严重级别 | 推断 | `critical` / `warning` |

---

### 3.7 DocAsset（知识文档）

```text
作用: 特性关联的md文件，含文档类型分类。
来源: Step 2的文件映射 + 目录结构推断文档类型。
承载的边: feature_id(所属特性)、sub_feature_id(所属子特性, 可选)
```

| 字段名 | 类型 | 含义 | 来源 | 示例 |
|--------|------|------|------|------|
| `id` | string | 唯一标识 | 文件路径hash | `GWFD-020301:doc:66863837` |
| **`feature_id`** | string | 所属特性（**边：所属特性**） | Step 2 | `GWFD-020301` |
| `file_path` | string | md文件相对路径 | Step 2 | `output/.../GWFD-020301...概述_66863837.md` |
| `doc_type` | enum | 文档类型 | 目录名/文件名推断 | `overview` / `principle` / `activation` / `debug` / `reference` / `index` / `flow` |
| `doc_title` | string | 文档标题 | md文件H1标题 | `GWFD-020301 内容计费基本功能特性概述` |
| `sub_feature_id` | string | 所属子特性（可选） | 推断 | `GWFD-010101:5G` |

**doc_type 取值说明：**

| 类型 | 含义 | 识别模式 |
|------|------|---------|
| `overview` | 特性概述 | 文件名含"特性概述"或"功能概述" |
| `principle` | 实现原理 | 目录名为"实现原理" |
| `activation` | 激活/部署 | 文件名含"激活"或"部署"或"配置" |
| `debug` | 调测 | 文件名含"调测" |
| `reference` | 参考信息 | 文件名含"参考信息" |
| `index` | 索引页 | 仅含标题无实质内容的入口文件 |
| `flow` | 信令流程 | 文件名含"流程"（如PDU会话建立） |

---

## 4. 边表详细定义

### 4.1 FeatureDependency（特性间依赖关系）

```text
作用: 表达特性间的依赖、互斥和协同关系。边本身有额外属性（类型、说明、控制项），因此需要单独表。
来源: 概述文档的"与其他特性的交互"section。
      注意：原理文档中可能引用更多关联特性，需合并。
```

| 字段名 | 类型 | 含义 | 来源 | 示例 |
|--------|------|------|------|------|
| `id` | string | 唯一标识 | 拼接 | `GWFD-020301:depends_on:GWFD-110101` |
| `source_feature_id` | string | 源特性（**边起点**） | 概述 | `GWFD-020301` |
| `target_feature_id` | string | 目标特性（**边终点**） | 概述 | `GWFD-110101` |
| `dependency_type` | enum | 依赖类型 | 概述 | `depends_on` / `conflicts_with` / `cooperates_with` |
| `description` | text | 依赖说明 | 概述 | `内容计费需先识别业务类型，必须先开启SA` |
| `license_control_item` | string | 关联License控制项 | 概述 | `82209749 SA-Basic` |
| `source_type` | enum | 信息来源 | 推断 | `overview_explicit` / `principle_implicit` |

**dependency_type 取值说明：**

| 类型 | 含义 | 示例 |
|------|------|------|
| `depends_on` | 必须先开启目标特性 | 内容计费 depends_on SA-Basic |
| `conflicts_with` | 与目标特性互斥 | (待从文档中挖掘) |
| `cooperates_with` | 协同工作但非强制依赖 | 地址分配 cooperates_with N4接口 |

---

### 4.2 FeatureLicense（特性→License映射）

```text
作用: 一个特性可能有0~N个License（如WSFD-220002有2个，分属SMF和AMF），因此单独建映射表。
来源: 概述的"可获得性"section中的License支持。
```

| 字段名 | 类型 | 含义 | 来源 | 示例 |
|--------|------|------|------|------|
| `id` | string | 唯一标识 | 拼接 | `GWFD-020301:license:82209822` |
| `feature_id` | string | 所属特性（**边起点**） | 关联 | `GWFD-020301` |
| `license_number` | string | License编号 | 概述 | `82209822` |
| `license_code` | string | License编码 | 概述 | `LKV3G5BCBC01` |
| `license_name` | string | License名称 | 概述 | `内容计费基本功能` |
| `applicable_nf` | string | 适用NF（部分License按NF区分） | 概述 | `SMF` |

---

## 5. 三种特性类型的实例对照

### 5.1 协议基础型：GWFD-010101 会话管理

```text
Feature: GWFD-010101 会话管理
  feature_type: protocol_base
  config_required: false
  applicable_nf: ["PGW-U", "SGW-U", "UPF"]
  standards: ["3GPP 29.244", "3GPP 23.502"]
  parent_feature_id: "GWFD-010100"

  SubFeature (3个):
    - GWFD-010101:2_3G → PGW-U, 概述+4个PDP流程文档
    - GWFD-010101:4G   → SGW-U+PGW-U, 概述
    - GWFD-010101:5G   → UPF, 概述+8个PDU会话流程文档

  ProcedureVariant: (空，无需配置)
  ConfigObject: (空，协议运行时行为)
  FeatureDependency: (概述声称无，但原理引用了WSFD-107015等)
  FeatureLicense: (无)
  DocAsset: 16个md (overview×3 + flow×13)
```

### 5.2 配置使能型：GWFD-010105 用户面地址分配

```text
Feature: GWFD-010105 用户面地址分配
  feature_type: config_enable
  config_required: true
  applicable_nf: ["PGW-U", "UPF"]
  standards: ["3GPP 29.244", "3GPP 23.501", "3GPP 23.502"]
  parent_feature_id: "GWFD-010100"

  SubFeature: (无)

  ProcedureVariant (4个):
    - 基于APN_DNN分配地址 (primary)
      ConfigStep: ADD L3VPNINST → ADD VPNINSTAF → ADD VPNINST →
                  ADD APN → SET APNADDRESSATTR → ADD POOL → ADD SECTION →
                  ADD POOLGROUP → ADD POOLBINDGROUP → ADD POOLGRPMAP →
                  SET IPALLOCRULE → ADD OSPF → ... (共约20步)
    - 基于SMF分配地址 (alternative)
    - 基于SMF+APN_DNN组合 (alternative)
    - 基于RADIUS下发地址池名称 (alternative)

  ConfigObject层级:
    VPNINST → APN → POOL → SECTION
                     → POOLGROUP → POOLBINDGROUP → POOLGRPMAP

  FeatureDependency:
    - depends_on: GWFD-010224(N4接口)
    - depends_on: GWFD-010233(Sxb接口)

  FeatureLicense: (无，免费特性)

  ValidationRule:
    - 地址池IP段不能重叠 (warning)
    - PFCP私有扩展要求对接华为设备 (warning)

  DocAsset: 10个md (overview×1 + reference×1 + debug×1 + principle×3 + activation×4)
```

### 5.3 业务策略型：GWFD-020301 内容计费基本功能

```text
Feature: GWFD-020301 内容计费基本功能
  feature_type: business_policy
  config_required: true
  applicable_nf: ["SGW-U", "PGW-U", "UPF"]
  standards: ["3GPP 23.502 Release 15", "3GPP 29.244"]
  parent_feature_id: "GWFD-020300"

  SubFeature: (无)

  ProcedureVariant (4个):
    - URL内容计费 (primary, 优先级100)
    - IMS语音计费 (alternative, 优先级110)
    - 兜底any计费 (fallback, 优先级65000)
    - 异常流量(免费) (fallback, 通过缺省信令URR)

  ConfigObject层级 (双链路):
    链路1-费率层: URR → URRGROUP → PCCPOLICYGRP
    链路2-过滤层: FILTER/FILTERIPV6 + L7FILTER → FLOWFILTER
    汇聚-规则层: RULE = FLOWFILTER + PCCPOLICYGRP
    顶层: USERPROFILE → RULEBINDING → RULE
                          → URRGRPBINDING(缺省费率)

  ConfigStep: ADD URR → ADD URRGROUP → ADD PCCPOLICYGRP →
              ADD FILTER → ADD L7FILTER → ADD FLOWFILTER →
              ADD FLTBINDFLOWF → ADD PROTBINDFLOWF →
              ADD RULE → ADD USERPROFILE → ADD RULEBINDING →
              SET URRGRPBINDING → ADD SPECURRGRPLIST → SET REFRESHSRV (共14步)

  FeatureDependency:
    - depends_on: GWFD-110101(SA-Basic, 强制), license: 82209749 SA-Basic
    - depends_on: GWFD-020300(在线计费, 可选)
    - depends_on: GWFD-010171(离线计费, 可选)

  FeatureLicense:
    - 82209822 LKV3G5BCBC01 内容计费基本功能

  ValidationRule:
    - cross_nf_consistency: URRID/USAGERPTMODE需SMF和UPF保持一致 (critical)
    - naming_convention: USERPROFILE名称需PCF/SMF/UPF统一规划 (warning)

  DocAsset: 5个md (overview×1 + reference×1 + principle×1 + activation×1 + index×1)
```

---

## 6. 抽取策略（进度追踪）

> 更新时间: 2026-05-26
> 实现代码: `step4_extract_l1.py`

### 6.1 总览

| 层级 | 抽取内容 | 目标表 | 数据来源 | 抽取方法 | 状态 | 备注 |
|------|---------|--------|---------|---------|------|------|
| **L1** | Feature基础属性 | Feature | xlsx + 概述md固定section | 代码 | ✅ 已完成 | 已审查，Schema字段全覆盖 |
| **L2** | DocAsset分类 | DocAsset | Step 2映射 + H1/目录名模式匹配 | 代码 | ✅ 已完成 | 缺3个Schema字段，见下方 |
| **L3** | FeatureDependency | FeatureDependency | 概述"与其他特性的交互"table | 代码 | ✅ 已完成 | 已去重，缺2个Schema字段 |
| **L4** | FeatureLicense | FeatureLicense | 概述"可获得性"License section | 代码 | ✅ 已完成 | 支持3种License格式，缺1个Schema字段 |
| **L5** | SubFeature | SubFeature | 文档目录结构（代际子目录） | 代码 | ❌ 未开始 | — |
| **L6** | ConfigObject + 层级 | ConfigObject | 激活/部署md + 参考信息命令清单 | 代码初抽 + LLM精抽 | ❌ 未开始 | — |
| **L7** | ProcedureVariant + ConfigStep | ProcedureVariant + ConfigStep | 激活/部署md的操作步骤和数据规划 | LLM | ❌ 未开始 | — |
| **L8** | ValidationRule | ValidationRule | 部署文档约束 + 调测文档 | LLM | ❌ 未开始 | — |

**L1-L4** 已完成代码自动化抽取。
**L5** 可用代码自动化（结构化：目录名→代际推断）。
**L6-L8** 需要LLM理解非结构化文本，结果需人工审核。

### 6.2 L1 Feature — 已完成

**输出文件**: `data/l1_{udg,unc}_feature_attributes.csv`

| 统计项 | UDG | UNC |
|--------|-----|-----|
| 总特性数 | 303 | 595 |
| 有概述成功抽取 | 217 | 431 |
| 无文档(no_docs) | 83 | 162 |
| 概述为空(empty) | 2 | 1 |
| 有文档但无概述(no_overview) | 1 | 1 |
| 目录特性(is_directory=true) | 63 | 104 |

**字段来源分组**:
- xlsx直接搬运(8个): `feature_id, feature_name, product_type, product_version, is_directory, section, parent_feature_id, nf_support_map`
- 概述md截取(9个): `applicable_nf, definition, customer_value, application_scenario, system_impact, restrictions, spec, standards, first_release_version`
- 规则推断(2个): `feature_type`(启发式关键词匹配), `config_required`(枚举映射)
- 辅助字段(2个): `id`(拼接), `has_overview`(状态标记)

**推断规则详情**:

`feature_type`:
1. [可获得性]含"无需配置" 且 无activation文档 → `protocol_base`
2. 有activation文档 且 activation数>=2 且 definition含策略关键词(策略/规则/过滤/计费/QoS/带宽/流量控制/访问控制/策略控制) → `business_policy`
3. 默认 → `config_enable`

`config_required`: feature_type=="protocol_base" → false, 否则 → true

**Schema额外字段**: `has_overview`(不在Schema中，但实用，保留)

### 6.3 L2 DocAsset — 已完成，需补字段

**输出文件**: `data/l1_{udg,unc}_doc_assets.csv` (UDG 831条, UNC 2363条)

**当前字段**: `feature_id, product_type, file_path, doc_type`

**与Schema对比**:

| Schema字段 | 当前状态 | 说明 |
|------------|---------|------|
| `id` | ❌ 缺失 | 需生成，格式 `{feature_id}:doc:{hash}` |
| `feature_id` | ✅ | — |
| `file_path` | ✅ | — |
| `doc_type` | ✅ | overview/activation/debug/reference/principle/flow/index/other |
| `doc_title` | ❌ 缺失 | 需从md文件H1标题提取 |
| `sub_feature_id` | ❌ 缺失 | 依赖L5 SubFeature抽取完成后回填 |
| — | `product_type` 额外 | Schema未定义，但实用，保留 |

**待补**: `id`, `doc_title` 可立即补；`sub_feature_id` 需等L5完成后回填。

### 6.4 L3 FeatureDependency — 已完成，需补字段

**输出文件**: `data/l1_{udg,unc}_feature_dependency.csv` (UDG 267条, UNC 406条)

**当前字段**: `source_feature_id, target_feature_id, dependency_type, description, license_control_item`

**与Schema对比**:

| Schema字段 | 当前状态 | 说明 |
|------------|---------|------|
| `id` | ❌ 缺失 | 需生成，格式 `{source}:dep:{target}` |
| `source_feature_id` | ✅ | — |
| `target_feature_id` | ✅ | — |
| `dependency_type` | ✅ | depends_on/conflicts_with/cooperates_with |
| `description` | ✅ | — |
| `license_control_item` | ✅ | — |
| `source_type` | ❌ 缺失 | 当前全部来自概述，应填 `overview_explicit` |

**待补**: `id`(可立即补), `source_type`(当前全部为overview_explicit，L6阶段补充principle_implicit)

### 6.5 L4 FeatureLicense — 已完成，需补字段

**输出文件**: `data/l1_{udg,unc}_feature_license.csv` (UDG 137条, UNC 275条)

**当前字段**: `feature_id, license_number, license_code, license_name, applicable_nf`

**与Schema对比**:

| Schema字段 | 当前状态 | 说明 |
|------------|---------|------|
| `id` | ❌ 缺失 | 需生成，格式 `{feature_id}:license:{license_number}` |
| `feature_id` | ✅ | — |
| `license_number` | ✅ | 支持纯数字和字母数字混合编号 |
| `license_code` | ✅ | — |
| `license_name` | ✅ | — |
| `applicable_nf` | ✅ | 部分License按NF区分 |

**待补**: `id` 可立即补。

### 6.6 待补字段汇总（可在step4中一次性修复）

| 表 | 缺失字段 | 修复方式 | 前置依赖 |
|----|---------|---------|---------|
| DocAsset | `id` | 代码生成 hash | 无 |
| DocAsset | `doc_title` | 读取md文件H1标题 | 无 |
| DocAsset | `sub_feature_id` | L5完成后回填 | **L5** |
| FeatureDependency | `id` | 代码拼接 | 无 |
| FeatureDependency | `source_type` | 默认填 `overview_explicit` | 无 |
| FeatureLicense | `id` | 代码拼接 | 无 |

**立即可做**: 补 DocAsset.id, DocAsset.doc_title, FeatureDependency.id, FeatureDependency.source_type, FeatureLicense.id
**需等L5**: DocAsset.sub_feature_id

### 6.7 后续层级规划

#### L5 SubFeature（代码可完成）

数据来源: 文档目录结构中的代际子目录（如 `2_3G会话管理/`, `4G会话管理/`, `5G会话管理/`）

推断逻辑:
1. 扫描每个feature目录下的子目录
2. 子目录名匹配代际模式: `2_3G`, `4G`, `5G`, `NSA`, `SA` 等
3. 子目录下的md文件即为该代际的概述文档
4. 从子目录概述md中提取 applicable_nf, definition, minimum_product_version

预估规模: 仅部分特性有子特性（主要是大型特性如会话管理、接口等）

#### L6 ConfigObject（代码初抽 + LLM精抽）

数据来源:
1. 参考信息md中的命令清单（结构化表格，代码可抽）
2. 激活/部署md中的配置步骤（需LLM理解上下文）
3. 命令图谱已有的ConfigObject数据（可复用）

关键挑战: 配置对象层级关系的确定（如 URR → URRGROUP → PCCPOLICYGRP）

#### L7 ProcedureVariant + ConfigStep（LLM为主）

数据来源: 激活/部署md的操作步骤和数据规划表

关键挑战: 同一特性多种配置场景的识别和拆分；步骤间的顺序关系；配置对象链的提取

#### L8 ValidationRule（LLM为主）

数据来源:
1. 部署文档中的约束说明（如"需保持一致"）
2. 调测文档中的排障步骤
3. 应用限制section中的约束条件（L1已提取为文本，需LLM结构化）
