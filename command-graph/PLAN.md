# Command Graph 构建计划 — UDG 20.15.2

## 目标

从 UDG 产品文档的 ~4,580 个 MML 命令 Markdown 文件中，构建完整的**命令图谱**。
命令图谱是三层图谱的底层基础，向上连接特性图谱的 ConfigObject。

## 语料范围

```
input: output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令/
  ├── 用户面服务管理/     (最大分类)
  ├── 平台服务管理/
  ├── 集中配置命令说明/
  ├── NAT服务管理/
  ├── SAPO服务管理/
  ├── SFIP管理/
  ├── TCP优化服务管理/
  ├── 业务报表管理/
  ├── 智能板管理/
  ├── CoreMind操作维护命令/
  └── MML命令申明_79861195.md
```

每个 md 文件高度结构化，包含：命令功能、注意事项、操作权限、参数说明(表格)、使用实例、输出说明。

## LLM 配置

```
BASE_URL: https://api.deepseek.com/chat/completions
MODEL: deepseek-chat
API_KEY: 从项目根目录 .env 读取
```

---

## 构建管道

### Step 1: 目录扫描 → 命令清单
**脚本**: `step1_scan_commands.py`
**产出**: `data/udg_command_inventory.csv`

扫描所有 md 文件，从目录路径和文件名提取：
- 文件路径、文件名
- 分类层级路径（service_category → service_domain → config_object_area → operation）
- 中文标题、命令名、文档ID

**迭代**: 3-5轮，每轮抽查 20 个文件核对路径解析和命令名提取准确性

### Step 2: 命令文档结构化解析
**脚本**: `step2_parse_commands.py`
**产出**: `data/udg_command_metadata.csv`

解析每个 md 文件的固定 section，提取：
- 命令名、操作类型(动词)、中文标题
- 适用NF
- 命令功能描述
- 注意事项原文
- 操作权限
- 使用实例
- 输出说明
- 各 section 实际存在情况

**迭代**: 3-5轮，每轮抽样 20 个命令，对比原文与解析结果，修复边界case

### Step 3: 参数解析
**脚本**: `step3_extract_parameters.py`
**产出**:
- `data/udg_parameters.csv`
- `data/udg_param_enum_values.csv`

从参数说明表格解析：
- 参数标识、中文名
- 必选/可选/条件必选/条件可选
- 参数含义、数据来源
- 取值范围（原始文本 + 解析后的枚举值）
- 默认值
- 配置原则
- 条件依赖原文

**迭代**: 3-5轮，重点验证表格解析成功率、枚举提取准确性、条件依赖提取覆盖度

### Step 4: 配置对象发现
**脚本**: `step4_discover_config_objects.py`
**产出**:
- `data/udg_config_objects.csv`
- `data/udg_command_groups.csv`

通过代码分析发现：
- 从命令名归纳配置对象（去掉操作动词后同名的命令属同一对象）
- 从目录路径归纳配置对象
- 命令组（ADD/MOD/RMV/DSP/LST 同对象 CRUD 族）

**迭代**: 3-5轮，验证配置对象发现的完整性、命令组匹配合理性

### Step 5: LLM 语义关系抽取（第一轮）
**脚本**: `step5_llm_extract_relationships.py`
**产出**: `data/udg_semantic_relationships_raw.json`

用 DeepSeek LLM 从原始文档中抽取语义关系：
- 参数→参数条件依赖（结构化）
- 命令→命令前置依赖
- 命令→命令引用关系
- 参数→参数互斥关系
- 风险等级、生效时机
- 配置对象层级关系

每条关系包含 evidence_text（原文引用）。

**迭代**: 3-5轮，每轮抽取一批，验证 evidence 准确性，优化 prompt

### Step 6: LLM 语义关系反思审查
**脚本**: `step6_llm_review_relationships.py`
**产出**: `data/udg_semantic_relationships_reviewed.json`

用 LLM 做第二轮反思：
- 验证 evidence_text 是否支持抽取出的关系
- 修正关系类型
- 标注置信度
- 发现遗漏的关系

**迭代**: 3-5轮

### Step 7: 最终合并 + Schema归纳
**脚本**: `step7_merge_and_schema.py`
**产出**:
- `data/udg_command_graph_final/` — 所有最终 CSV
- `COMMAND_GRAPH_SCHEMA.md` — 从实际发现归纳的 Schema 文档

---

## 自我迭代机制

每个 Step 执行流程：

```
1. 编写/优化脚本
2. 运行抽取
3. 质量审查（读取输出CSV + 抽样原始md对比）
4. 发现问题 → 修改代码/prompt → 重新运行
5. 重复 3-4 直到质量达标（至少3轮，最多5轮）
6. 调用 Codex 进行最终审核
7. 进入下一个 Step
```

### 质量审查方法
- **数量校验**: 产出记录数与源文件数是否匹配
- **抽样对比**: 随机抽 20 条，人工对比原文与解析结果
- **字段完整性**: 关键字段非空率统计
- **边界case**: 找到解析失败的文件，分析原因，修复代码

---

## 产出物

```
command-graph/
├── PLAN.md                           # 本文档
├── GUIDELINES.md                     # 工作准则
├── COMMAND_GRAPH_SCHEMA.md           # 最终归纳的 Schema（Step 7 产出）
├── step1_scan_commands.py
├── step2_parse_commands.py
├── step3_extract_parameters.py
├── step4_discover_config_objects.py
├── step5_llm_extract_relationships.py
├── step6_llm_review_relationships.py
├── step7_merge_and_schema.py
├── llm_client.py                     # DeepSeek API 封装
├── data/
│   ├── udg_command_inventory.csv
│   ├── udg_command_metadata.csv
│   ├── udg_parameters.csv
│   ├── udg_param_enum_values.csv
│   ├── udg_config_objects.csv
│   ├── udg_command_groups.csv
│   ├── udg_semantic_relationships_raw.json
│   ├── udg_semantic_relationships_reviewed.json
│   ├── audit/                        # 各步骤审计报告
│   │   ├── step1_audit.md
│   │   ├── step2_audit.md
│   │   └── ...
│   └── final/                        # 最终合并数据
│       ├── commands.csv
│       ├── parameters.csv
│       ├── config_objects.csv
│       ├── relationships.csv
│       └── command_groups.csv
```
