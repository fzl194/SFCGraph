# 业务感知原料池 Schema v0.1

## 1. 目标

本页定义：

```text
business_source_index.csv
```

它不是业务图谱结果本身，而是业务图谱的原料池。

作用：

- 固定业务感知相关原始文档块
- 让后续 `NetworkScenario` 归纳有稳定输入
- 让 Agent 不需要每轮重新从全库盲搜

## 2. 设计原则

### 2.1 原料池先宽后窄

第一轮宁可多收一些候选，也不要过早裁掉。

### 2.2 以“文档块”为最小单位

不是整本目录，也不是单句原文，而是：

```text
一个可独立理解的页面或章节块
```

### 2.3 保留来源类型

因为业务图谱要区分：

- 业务专题样板
- 特性知识
- 命令对象链
- 基础知识/流程知识

## 3. 表结构

建议字段如下：

| 字段名 | 含义 | 类型 | 生成方式 |
| --- | --- | --- | --- |
| `source_id` | 原料唯一ID | string | code |
| `vendor` | `UDG` / `UNC` | string | code |
| `source_kind` | `business_topic` / `feature_page` / `command_doc` / `basic_knowledge` | string | code |
| `source_group` | 来源分组，如 `业务感知专题`、`业务感知功能`、`智能PCC解决方案` | string | code |
| `feature_code` | 若来源属于某特性，记录特性编号 | string/null | code |
| `command_name` | 若来源属于命令文档，记录命令名 | string/null | code |
| `title` | 页面标题 | string | code |
| `source_path` | 原始 md 路径 | string | code |
| `page_type_candidate` | `overview` / `activation` / `configuration` / `reference` / `topic` / `command` / `knowledge` | string | code |
| `business_awareness_relevance` | `high` / `medium` / `low` | string | hybrid |
| `candidate_scene_tags_json` | 候选场景标签 | json | hybrid |
| `candidate_semantic_tags_json` | 候选语义标签 | json | hybrid |
| `object_chain_hints_json` | 候选对象链提示 | json | hybrid |
| `summary_hint` | 原料摘要提示 | string | hybrid |
| `evidence_id` | 对应证据节点 | string | code |
| `status` | `draft` / `reviewed` / `accepted` | string | code |

## 4. 字段解释

### 4.1 `source_kind`

建议固定为：

- `business_topic`
- `feature_page`
- `command_doc`
- `basic_knowledge`

### 4.2 `page_type_candidate`

建议固定为：

- `topic`
- `overview`
- `activation`
- `configuration`
- `deployment`
- `reference`
- `debug`
- `command`
- `knowledge`

### 4.3 `business_awareness_relevance`

这是业务图谱原料池里很关键的字段。

含义：

- `high`
  - 明显属于业务感知主线
- `medium`
  - 与业务感知有关，但更偏外围支撑
- `low`
  - 只作为补充知识保留

这个字段不建议纯代码拍板，应该：

```text
代码给候选
Agent 定稿
```

## 5. 哪些字段可以代码直接生成

### 5.1 纯代码字段

- `source_id`
- `vendor`
- `source_kind`
- `source_group`
- `feature_code`
- `command_name`
- `title`
- `source_path`
- `page_type_candidate`
- `evidence_id`
- `status`

### 5.2 代码可给候选、Agent 再修正

- `business_awareness_relevance`
- `candidate_scene_tags_json`
- `candidate_semantic_tags_json`
- `object_chain_hints_json`
- `summary_hint`

## 6. `source_id` 生成规则

建议格式：

```text
BSRC:<vendor>:<kind>:<doc_or_feature_key>:<local_id>
```

示例：

- `BSRC:UDG:business_topic:business_awareness:001`
- `BSRC:UDG:feature_page:GWFD-020301:deploy_upf`
- `BSRC:UNC:feature_page:WSFD-011206:overview`
- `BSRC:UNC:command_doc:ADD_URR:09897158`

## 7. 第一批默认纳入哪些来源

### 7.1 UDG

- `特性部署\业务专题\UDG业务感知专题`
- `特性部署\特性指南\UDG特性指南\业务感知功能`
- `OM参考\命令\UDG MML命令` 中业务感知相关命令

### 7.2 UNC

- `网络部署\特性部署` 中 PCC / 内容计费 / 融合计费 / 热计费 / 离线计费 / 5G LAN / 智能PCC 相关特性页
- `OM参考\命令\UNC MML命令` 中计费与策略相关命令
- `网络部署\业务专题` 中计费方案、PCC 方案相关页面
- `一望5G` / `5G基本知识` 中与会话策略、计费、配额、业务控制相关页面

## 8. 第一轮代码策略

代码第一轮不需要做复杂 NLP，只需要：

1. 扫固定目录
2. 识别来源类型
3. 识别特性编号、命令名、页面类型
4. 建 Evidence
5. 产出 `business_source_index.csv` 初稿

## 9. 第一轮 Agent 策略

Agent 第一轮只做 4 件事：

1. 判 `business_awareness_relevance`
2. 打第一批 `candidate_scene_tags_json`
3. 打第一批 `candidate_semantic_tags_json`
4. 为强相关原料补 `summary_hint`

## 10. 与后续 pipeline 的关系

这张表后续直接喂给：

- `Scenario Discovery Pipeline`
- `Solution Closure Pipeline`
- `Validation & Diagnosis Pipeline`

所以它是业务图谱当前最先要落的结构化输入。
