# 命令图谱构建 SOP（迭代累积）

> **本文档是活的 SOP，按阶段迭代追加。**
> 每完成一个阶段（用户引导 → 写代码 → 输入/输出验证），就按"阶段模板"在下方**追加一节**，不重写已有阶段。
> 目标：沉淀成一套可复用到**不同产品文档**（UDG / UNC / 未来其他网元）的标准作业流程。

---

## 阶段索引

| 阶段 | 内容 | 状态 |
|---|---|---|
| 0 | Schema 定稿 | ✅ |
| 1 | MMLCommand 章节级构建（以 UDG 为例） | ✅ |
| 2 | MMLCommand 章节级构建（UNC 验证通用性） | ✅ |
| 3 | MMLCommand 派生字段抽取（10/10 已抽） | ✅ |
| 4 | CommandParameter 构建（内网参数资产映射 + 关系侧输出） | 🟡 |
| 5 | ConfigObject 构建（命令族聚合 + 内网规则表） | ✅ |
| 6 | CommandRule 构建（notes/重复规则/删除保护） | ⏳ |
| 7 | kgdata 校验（kgdata 对照 md 补缺纠错） | ⏳ |

---

## 通用约定（贯穿所有阶段）

1. **md 抽取是正道，kgdata 仅作校验**——很多产品文档无 kgdata（如 UNC），必须从 md 抽。
2. **版本治理 G 模型**——实例键 = `{nf}@{version}@{ObjectType}@{local_name}`（四段带类型，见 schema §1A）；每层是完整实例快照，不跨版本合并。
3. **先章节级、后字段级，逐字段批准**——章节切分确定（rule 自动）；字段抽取常需专家校准（expert），分阶段、逐字段做，不自作主张批量提取。
4. **先分析再运行**——换产品文档前先跑 `_title_stats2.py` 确认章节名/层级，再调 reader。
5. **按文本匹配章节，不按层级**——实测同一命令内 H2/H4 混用，按层级会漏。
6. **每个对象 = 一个 reader + 一个 builder**（统一入口模式）。

---

## 如何使用本 SOP（给后续 agent）

- **接手时**：读"阶段索引"看做到哪了；读对应阶段的"处理/要点"理解现状。
- **做新阶段**：按"阶段模板"在文末**追加一节**（不要改已有阶段），更新"阶段索引"状态。
- **换产品文档**：通用约定直接适用；按各阶段流程跑，但**先跑 `_title_stats2.py` 分析新文档的章节**，确认 `md_reader._SECTION_TO_FIELD` 覆盖后再运行。

### 阶段模板（每阶段按此记录）

```
## 阶段N：<名称>
- **状态**：✅/⏳
- **目标**：
- **输入**：
- **处理**（代码 + 关键逻辑）：
- **输出**：
- **要点 / 坑**：
- **产物**：
```

---

## 阶段0：Schema 定稿 ✅

- **目标**：定义命令图谱 4 对象的 schema（ConfigObject / MMLCommand / CommandParameter / CommandRule）。
- **要点**：版本 G 模型、存储模型（默认属性/表仅一对多）、ConfigObject 轻量化（属性靠图遍历）、`has` 关系（配置块=has 子树，父删子灭）、CommandRule 去重原则。
- **产物**：`command-graph/COMMAND_GRAPH_SCHEMA.md` (v0.5)、memory `command-graph-schema-v0.5.md`。

---

## 阶段1：MMLCommand 章节级构建（以 UDG 为例）✅

- **目标**：从产品文档 md 构建 MMLCommand 章节级节点（schema §3.3 本阶段 14 字段）。
- **输入**：`output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令/*.md`（4580 个）。
- **处理**：
  - 入口 `build_mmlcommand.py`：glob md → `md_reader.parse_md` → `to_mmlcommand` → 去重 → JSONL。
  - `md_reader.parse_md`：
    1. 找 H1（#），正则解析"中文（英文命令码）"→ command_code + command_name_zh；**失败=非命令文件，跳过**。
    2. 扫 H2~H6，**按文本匹配章节**（不按层级）→ 归入字段；跳过 TOC 行（`- [文字](#anchor)`）。
    3. 归并：操作/网管/本地用户权限→`permission_text`；功能描述/适用网元→`command_function`；参考/名词解释/术语解释→`reference_info`。
    4. "参数说明"不收（属 CommandParameter）。
    5. `category_path` = md 相对 input-dir 的目录链。
  - `to_mmlcommand`：command_id=`{nf}@{version}@MMLCommand@{command_name}`；verb/keyword 拆分；章节文本映射；标 `_review_status=auto, _stage=section_level`。
- **输出**：`data/output/mml_commands_udg.jsonl`（4577 条，跳过 3 非命令文件）。
- **要点 / 坑**：
  - H2/H4 混用 → 必须按文本匹配，不能按层级。
  - 非命令文件（MML命令申明/MML索引/集中配置概念）靠 H1 解析失败过滤。
  - 章节级只切整段，**不**做字段细化（effect_mode 等留阶段3）。
  - notes/usage_examples 存 `[整段]` 单元素，下阶段再切分。
- **产物**：`md_reader.py`、`build_mmlcommand.py`、`_title_stats2.py`（分析工具）、`EXTRACTION_STRATEGY.md`（字段↔章节映射）。

### 运行命令
```bash
python builder/build_mmlcommand.py \
  --input-dir "output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令" \
  --nf UDG --version 20.15.2 \
  --output data/output/mml_commands_udg.jsonl
```

---

## 阶段2：MMLCommand 章节级构建（UNC 验证）✅

- **目标**：用阶段1 的同一程序跑 UNC，验证通用性（UNC 无 kgdata，纯 md 抽取）。
- **输入**：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/*.md`（8505 个）。
- **处理**：代码不改，只换 `--input-dir --nf UNC --version 20.15.2`。
- **输出**：`data/output/mml_commands_unc.jsonl`（8498 条，跳过 7 非命令文件）。
- **验证**：
  - 基本结构（command_id/nf/category_path/source_evidence_ids）✓
  - 输出结果说明（查询类命令的输出字段表格整段）✓
  - `permission_text` 非空 8265/8498（97%）；网管/本地用户权限按 `map_section` 归并到同一 `permission_text`（代码逻辑正确，建议后续抽查原始 md 逐条确认）。
- **要点 / 坑**（曾发现 bug，已修复）：
  - ⚠️ **bug**：UNC 用 `<div class="mmlnote">` 注意事项章节，转换脚本 `_has_class_name(node,"note",...)` 子串匹配误判（`"note" in "mmlnote"`），把注意事项当 advisory 提示框处理 → 丢 `<h2>注意事项</h2>` 标题、内容变 `>说明` 块混入命令功能，UNC `notes` 大量缺失。UDG 用 `div.section` 不含 note 子串，不受影响。
  - **修复**（2026-06-24，`product_doc_md_exporter_optimized.py` `_render_node`）：advisory 判断加 `mml*` 前缀排除，`mmlnote` 走普通 div → 输出 `## [注意事项]` + 内容。
  - **重转 UNC + 重跑 build**：`notes` 非空率从缺失回升到 **99%**（8497/8498）。
  - 跳过的 7 个非命令文件是分类目录页（业务系统管理/业务参数管理等），与 H1 解析失败过滤一致。
- **质量审查**（`audit_quality.py`，2026-06-24）：独立解析原始 md 章节 vs 产出字段。抽样 16 命令（UDG 8 + UNC 8）**0 漏切/错切**。全量字段非空率：UDG notes 81% / permission 94% / output 49%；UNC notes 99% / permission 97% / output 42%。
- **产物**：`data/output/mml_commands_unc.jsonl`（代码同阶段1，无新增脚本）。

### 运行命令
```bash
python builder/build_mmlcommand.py \
  --input-dir "output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令" \
  --nf UNC --version 20.15.2 \
  --output data/output/mml_commands_unc.jsonl
```

---

## 阶段3：MMLCommand 派生字段抽取（10/10 完成）✅

- **目标**：从原始字段抽 10 个派生字段（见 `COMMAND_GRAPH_SCHEMA.md` §3.3）。
- **机制（已定）**：**文件名不变**，派生字段增量合并进同一 jsonl。`enrich_mmlcommand.py` 读 jsonl → 逐行 `enrich(cmd)` → 写回同文件名。幂等（派生可重算覆盖）。前端始终读 `mml_commands_{nf}.jsonl`。
- **已全部抽取（10 个派生字段）**：
  - 规则类（6）：`command_category`（verb→类）/ `applicable_nf`（正则）/ `max_records`（正则）/ `permission_groups`（正则 G_x）/ `output_ref_command`（正则"参见"）/ `is_dangerous`（关键词"高危"）
  - 复杂类（4）：`effect_mode`（notes 语义归类，优先级 对新用户>对新流>延迟>立即）/ `spec_threshold`（notes 解析 alarm_id+ratio+recover+modify_command）/ `initial_values`（notes 初始值表解析）/ `output_fields`（output_description 表格解析）
- **覆盖率（UDG / UNC）**：command_category 100%；applicable_nf 35%/66%；max_records 15%/8%；permission_groups 94%/97%；output_ref_command 17%/8%；is_dangerous=True 368/194；effect_mode 49%/59%；spec_threshold 40/46；initial_values 226/~；output_fields 33%/32%。
- **案例验证**：ADD URR（立即生效/ALM-135602215 告警 90%）、SET SAAITRAINPARA（对新用户生效/初始值表）、DSP NATSESSION（输出字段表）均正确。
- **要点 / 坑**：
  - `applicable_nf` 的"适用NF"被 md 加粗（`**`），抽取后须清 `*` 标记。
  - `command_category` 动作类经扩充（含 STR/CLR/STP/LOD/SYN/RTR 等）；RTR=恢复/重置，归动作类。
  - `output_ref_command` 正则须剥 markdown 链接（`参见 [**XXX**](路径)`）+ 兼容"参见的/参见命令"。
  - `effect_mode` 是单值 enum，混合生效取最显著（如 SET SAAITRAINPARA 部分立即部分新用户→取"对新用户生效"）。
  - `initial_values` 226/311（85 个表格格式变体未匹配，边际）。
- **产物**：`enrich_mmlcommand.py`；`mml_commands_udg.jsonl` / `mml_commands_unc.jsonl`（同文件名，27 字段 = 原始 17 + 派生 10）。

### 运行命令
```bash
python builder/enrich_mmlcommand.py --input data/output/mml_commands_udg.jsonl
python builder/enrich_mmlcommand.py --input data/output/mml_commands_unc.jsonl
```

---

## 阶段4：CommandParameter 构建（内网参数资产映射）🟡

- **目标**：把内网参数资产（当前先支持 `csv` / `xlsx` 第一张 sheet）转换成 `CommandParameter` 节点，并输出参数归属关系与命令内条件依赖。
- **输入**：内网参数表，当前已用 `command-graph/test.csv` 子集验证。
- **处理**：
  - 入口 `build_commandparameter.py`：
    1. 读取 `csv` 或 `xlsx` 第一张 sheet；
    2. 将表头映射到 schema §3.4 的参数字段；
    3. 从 `说明` 中补抽 `data_source / semantic_summary / config_principle / default_value / value_range`；
    4. 跳过 `参数ID=-2` / `参数标识=zhanwei` 的占位行；
    5. 生成 `command_ref = {nf}@{version}@MMLCommand@{command_name}`，建立参数归属；
    6. 解析 `条件`（如 `{"3=IPV4": "必选"}`）为命令内 `depends_on` 边。
  - 关系侧当前拆成两个 sidecar：
    - `has_parameter`：`MMLCommand -> CommandParameter`
    - `depends_on`：`CommandParameter -> CommandParameter`
  - 支持可选 `--command-jsonl`：对照 `MMLCommand` 产物校验 `command_ref` 是否存在，但不强依赖。
- **输出**：
  - 参数节点 JSONL
  - `has_parameter` 关系 JSONL
  - `depends_on` 关系 JSONL
- **当前验证结果**（`test.csv`）：
  - 456 行输入
  - 443 个参数节点
  - 443 条 `has_parameter`
  - 112 条 `depends_on`
  - 13 行占位参数被过滤
  - 命令内条件依赖无未解析残留
- **要点 / 坑**：
  - `关联命令 / 关联参数` 在当前子集中无样例，**跨命令参数依赖语义待样例确认后再落地**。
  - `is_identifier` 不能仅靠当前参数表确定，后续要与 MOD/RMV/重复规则联动回填。
  - 当前参数构建来源是内网结构化资产，不是 md 的 `parameter_description`；后续要补“md 抽取 vs 内网资产校验”的合流方案。
- **产物**：
  - `builder/build_commandparameter.py`
  - `tests/test_build_commandparameter.py`

---

## 阶段5：ConfigObject 构建（命令族聚合 + 内网规则表）✅

- **目标**：按 object_keyword 聚合命令族 → ConfigObject 节点 + 命令→对象关系边（schema §3.2 终版）。
- **输入**：
  - `mml_commands.jsonl`（命令层全量；提供 object_keyword/verb/command_name_zh/applicable_nf/command_function/output_fields/source_evidence_ids）
  - `command_parameters.jsonl`（参数层；attribute_names 取 ADD/MOD/SET 参数名）
  - 内网规则独立表：`MOD规则.csv` / `RMV规则.csv` / `重复规则.csv`（identifier/uniqueness；7 表合一的源文件用 `split_rules.py` 拆）
- **处理**：
  - 入口 `builder/steps/configobject.py`（step 模式 run(ctx)）；聚合 `builder/core/config_object.py`。
  - 聚合逻辑：
    1. 按 (nf, object_keyword) 聚合命令族，一族一对象——**全建**（含查询/动作，用 object_kind 区分，不筛除）。
    2. object_kind 5 类判定（entity/global_setting/query_target/action/binding），优先级 + 数据驱动判据见 schema §3.2.1（**不按对象名后缀猜**，旧版 group/profile/filter 取消）。
    3. identifier ← MOD规则"索引参数"（MOD 缺失用 RMV规则）；uniqueness ← 重复规则"重复检查"。**必须从专门表读，非参数 required_mode 推断**。
    4. attribute_names ← ADD∪MOD∪SET 命令参数名（可配置属性），**去重**；不含 LST/DSP output_fields（查询输出结构，留命令层）。
    5. object_name_zh ← command_name_zh 去动词前缀（标 _auto 待校准）；description ← ADD command_function 优先。
    6. 命令→对象边：verb→relation_type（creates/modifies/deletes/sets/queries/operates_on）。
- **输出**：`config_objects.jsonl` + `command_object_edges.jsonl`。
- **当前验证结果**（UDG 20.15.2，test.csv 参数 + old/data 子集规则表）：
  - ConfigObject 2210 个，edges 4566；kind 分布 entity 597 / global_setting 541 / query_target 838 / action 197 / binding 37。
  - identifier 命中 MOD规则 7/7；uniqueness 6；attribute **15/2210** 有值（去掉 output_fields 后只靠参数表，test.csv 仅覆盖 SET 命令 → 几乎全空，全量参数表上线后填）；unit 测试 12 passed。
  - UNC 3608 对象（无 UNC 规则表 + 无 UNC 参数表 → identifier/uniqueness/attribute 全暂空）。
- **要点 / 坑**：
  - **全建边界**：所有 object_keyword 都建对象（含纯查询/动作），用 kind 区分。
  - **object_kind 数据驱动**：按 verb 画像 + 命名判定；group/profile/filter 取消（用对象间关系表达）。
  - **identifier/uniqueness 必须从内网规则专门表读**（MOD规则/重复规则），不是参数 required_mode。
  - **子集数据**：test.csv 参数少 + old/data 规则表是子集 → 多数对象 identifier/attribute 暂空（如 URR），全量内网规则上线后填。
  - **版本错配**：当前规则表 20.13.2 vs 命令层 20.15.2，按 object_name 跨版本关联；全量对版后自然解决。
  - **删除了 max_records**：对象规格上限不在 ConfigObject 存（命令层 mml_commands 已有）。
- **产物**：`builder/core/config_object.py`、`builder/steps/configobject.py`、`split_rules.py`、`data/rules/*.csv`、`tests/test_build_configobject.py`。

---

## builder/ 文件清单（参考）

| 文件 | 职责 |
|---|---|
| `build_mmlcommand.py` | MMLCommand 统一入口（原始字段） |
| `enrich_mmlcommand.py` | 派生字段抽取（增量合并，文件名不变） |
| `md_reader.py` | md 读取器（正道） |
| `audit_quality.py` | 抽取质量审查（独立解析 md vs 产出字段） |
| `_title_stats2.py` | 标题分析工具（先分析再运行） |
| `EXTRACTION_STRATEGY.md` | 字段策略 + 章节↔字段映射 |
| `README.md` | 本文档（SOP） |
