# MMLCommand 字段提取策略（审查版 v2）

> 原则修正：
> 1. **MD 抽取是正道，kgdata 仅作校验**（很多产品文档无 kgdata，如 UNC）。
> 2. **本阶段只做章节级拆分**（把 md 按标题切成整段）；**段落内字段抽取是下一阶段**。
> 3. 每个字段提取需批准，不自作主张。

---

## 一、MD 章节标题频次统计

统计源：
- UDG：`output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令/`（4580 md）
- UNC：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/`（8505 md）

**真章节频次**（H1 命令主标题每命令唯一，属噪声，已排除）：

| 章节 | UDG | UNC | 说明 |
|---|---|---|---|
| 命令功能 | 4577 | 8498 | 近全量 |
| 参数说明 | 4577 | 8496 | 近全量（→ 属 CommandParameter，不在 MMLCommand） |
| 使用实例 | 4577 | 8495 | 近全量 |
| 操作用户权限 | 4344 | 6370 | |
| 注意事项 | 3737 | 4446 | |
| 输出结果说明 | 2249 | 3593 | 查询类命令为主 |
| 网管用户权限 | 2 | 1896 | UNC 主用，权限细分 |
| 本地用户权限 | 2 | 1887 | UNC 主用，权限细分 |
| 参考信息 | 88 | 124 | **当前字段表遗漏** |
| 功能描述 | — | 7 | "命令功能"别名 |
| 适用网元 | — | 5 | 命令功能内小节 |
| 参考 | — | 4 | "参考信息"别名 |
| 名词解释 | 2 | — | 零星 |

> reader 须兼容别名：功能描述→命令功能；参考→参考信息。

### 分层级结论（回答三个审查问题）

**1. 出现 1 次的标题**
- H1 全部出现 1 次 = 命令主标题（每命令唯一，预期）
- H4 少量出现 1 次 = 脏数据 + 变体：
  - UDG：`操作用户权限DSP RU` / `集中配置组` / `配置域` / `公共配置`（脏数据/特殊命令）
  - UNC：`术语解释` / `操作场景` / `使用实例ADD GAUSEGRP` / `命令使用实例` / `操作用户权限DSP RU`（变体 + 脏数据，部分为标题拼接错误）
- 处理：脏数据（拼接错误）模糊归并；变体做别名映射（术语解释→参考信息，命令使用实例→使用实例）
- H2 无出现 1 次的标题（H2 只有 5 种标准章节）

**2. 主标题 vs 子标题（已拆分）**
- H1（#）= 命令主标题：UDG 4580 / UNC 8505，每命令唯一
- H2（##）= 章节层 A：仅 5 种（命令功能/参数说明/使用实例/输出结果说明/参考信息）
- H4（####）= 章节层 B：14-18 种（含注意事项/操作用户权限/网管·本地用户权限 + 上述 5 种）
- ⚠️ **章节在 H2 和 H4 两层都出现，且同一命令内可能混用**（实测 RMV PODBLACKLIST：命令功能用 H2、操作用户权限却用 H4）。
  → reader **必须按章节标题文本匹配，不能按固定层级**；同时注意事项偶尔以 `> 说明` 块出现而非独立章节，需容错。

**3. H1 能否可靠提取中英文名**
- UDG 4577/4580（99%）、UNC 8498/8505（99%）可解析为 `中文（英文命令码）`
- 失败的极少数是**非命令文件**（UDG：MML命令申明/MML索引/集中配置概念；UNC：业务系统管理/业务参数管理等目录页）
- 结论：**可靠（99%）**；失败者在 reader 按"H1 无法解析中英文 → 非命令文件"过滤

---

## 二、审查结论

### 必要性（字段是否过度）

原 26 字段表中，以下 **12 个是"章节内细化"**，按"本阶段只做章节级"原则，**移到下一阶段**，本阶段不提取（避免自作主张）：

`command_summary`、`applicable_nf`、`effect_mode`、`effect_delay`、`max_records`、`spec_threshold`、`initial_values`、`is_dangerous`、`danger_warning`、`performance_impact`、`applicability_constraints`、`output_fields`、`output_ref_command`、`command_category`（分类标准待定）

→ 它们都从"命令功能/注意事项/输出结果说明"**段落内部**提取，属下一阶段。

### 完整性（md 信息是否都覆盖）

| 发现 | 处理 |
|---|---|
| **"参考信息"章节**（UDG 88/UNC 124）字段表遗漏 | **新增 `reference_info` 字段**（本阶段，整段） |
| UNC "网管用户权限/本地用户权限"细分 | 本阶段并入 `permission_text` 整段；下阶段解析权限类型 |
| "参数说明"章节 | 属 **CommandParameter** 对象，不在 MMLCommand（正确，非遗漏） |
| 命令功能内"适用NF" | 章节内，下阶段 → `applicable_nf` |

---

## 三、修订字段表（分阶段）

### 本阶段：章节级拆分

字段按来源分三类。**表 A** 讲清每个 md 章节归到哪个字段（含归并），**表 B** 是标题派生，**表 C** 是非章节的元数据。

**表 A — md 章节正文 → 字段（含归并）**

| md 章节标题 | 频次 UDG/UNC | 归入字段 | 归并 / 说明 |
|---|---|---|---|
| 命令功能 | 4577/8498 | `command_function` | 别名"功能描述"并入 |
| 功能描述 | 0/7 | `command_function` | "命令功能"别名 |
| 适用网元 | 0/5 | `command_function` | 命令功能内小节，随整段保留；下阶段 → `applicable_nf` |
| 注意事项 | 3737/4446 | `notes` | |
| 操作用户权限 | 4344/6370 | `permission_text` | 与下面两类**归并** |
| 网管用户权限 | 2/1896 | `permission_text` | 并入权限（UNC 主用） |
| 本地用户权限 | 2/1887 | `permission_text` | 并入权限（UNC 主用） |
| 使用实例 | 4577/8495 | `usage_examples` | |
| 输出结果说明 | 2249/3593 | `output_description` | |
| 参考信息 | 88/124 | `reference_info` | 别名"参考"并入 |
| 参考 | 0/4 | `reference_info` | "参考信息"别名 |
| 名词解释 | 2/0 | `reference_info` | 零星（2 个），归入参考信息 |
| 参数说明 | 4577/8496 | —（属 CommandParameter） | **不在 MMLCommand**，下一对象处理 |

> **三个归并点**：
> - `permission_text` ← 操作用户权限 + 网管用户权限 + 本地用户权限（3 类权限章节归一）；本阶段存整段，下阶段解析出 `permission_groups` + 权限类型。
> - `command_function` ← 命令功能 + 功能描述（别名）+ 适用网元（内嵌小节，随整段保留）。
> - `reference_info` ← 参考信息 + 参考（别名）+ 名词解释（零星）。

**表 B — H1 标题派生**

| 字段 | 来源 | 说明 |
|---|---|---|
| `command_name` | H1 英文名（`ADD URR`） | 标题括号内英文 |
| `command_name_zh` | H1 中文（`增加URR`） | 标题括号前中文 |
| `verb` | command_name split | |
| `object_keyword` | command_name split | |

**表 C — 非章节（元数据 / 派生）**

| 字段 | 来源 | 说明 |
|---|---|---|
| `command_id` | 派生 `nf@version:command_name` | 无章节 |
| `category_path` | md 文件目录路径 | 非正文 |
| `status` | 默认 `active` | 无来源 |
| `source_evidence_ids` | md 文件路径 + 文件名数字 ID | 文件本身 |

> 本阶段全为 `rule`（章节切分 / 派生是确定性的），输出标 `auto`，无 `expert`。

### 下一阶段：章节内字段抽取（10 个派生字段）

> 经审视保留 **10 个派生字段**；删去 `command_summary`/`effect_delay`/`danger_warning`/`performance_impact`/`applicability_constraints`（原始整段 notes/command_function 已承载，下游无需结构化直接用）。含义见 `COMMAND_GRAPH_SCHEMA.md` §3.3。

| 来源原始字段 | 派生字段 | 策略 |
|---|---|---|
| verb | `command_category`（配置/查询/动作/调测） | expert（分类标准待定） |
| command_function | `applicable_nf`（适用 NF） | rule |
| notes | `effect_mode`（生效方式） | expert |
| notes | `max_records`（最大记录数） | rule |
| notes | `spec_threshold`（超阈值告警） | rule（待校准） |
| notes | `initial_values`（系统初始值） | rule |
| notes | `is_dangerous`（高危标记） | expert |
| permission_text | `permission_groups`（G_x） | rule |
| output_description | `output_fields`（输出字段表） | expert |
| output_description | `output_ref_command`（引用命令） | rule |

---

## 四、统一架构

```
build_mmlcommand.py  ← 统一入口（以 md 为主，kgdata 仅校验）
  ├─ 1. reader（按来源）
  │     ├─ md_reader        ← 正道：解析 md 章节标题 → 整段文本（UDG/UNC 通用）
  │     └─ kgdata_reader    ← 校验：对照 kgdata，补缺/纠错
  │     两者产出统一 RawCommand（章节级文本）
  └─ 2. 输出（本阶段）：章节级字段，标 review_status=auto
```

**RawCommand 中间表示**（章节级，reader 归一化目标）：

| 字段 | md 来源 |
|---|---|
| `command_code` | H1 标题（`增加URR（ADD URR）` → `ADD URR`） |
| `command_name_zh` | H1 中文 |
| `function_text` | 命令功能 |
| `notes_text` | 注意事项 |
| `permission_text` | 操作用户权限（含网管/本地） |
| `examples_text` | 使用实例 |
| `output_text` | 输出结果说明 |
| `reference_text` | 参考信息 |
| `category_path` | md 目录 |
| `source_path` | md 文件路径 |

---

## 五、待你决定

1. **本阶段字段表（14 个章节级）** 认可吗？尤其：
   - 新增 `reference_info`（参考信息章节）对不对？
   - `permission_text` 整段存（含网管/本地），下阶段再解析，对吗？
2. **下一阶段字段表**（章节内细化）先不展开，本阶段批准后再逐字段定策略？
3. **架构**：md_reader 为正道、kgdata 仅校验，认可吗？

批了我就按"本阶段 14 字段"重构：写 md_reader（章节切分），kgdata 退为校验角色。
