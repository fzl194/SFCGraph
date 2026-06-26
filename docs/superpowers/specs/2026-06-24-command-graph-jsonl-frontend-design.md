# 命令图谱：数据源切换 JSONL + 数据驱动字段展示

- **日期**: 2026-06-24
- **范围**: `platform-next/command_graph`（后端）+ `platform-next/frontend/src/command_graph`（前端）
- **状态**: 设计待评审

## 1. 背景与动机

`platform-next/command_graph/service.py` 当前从 `command-graph/data/{udg,unc}_commands.csv` 加载数据。这些 CSV 已被删除（迁移到 `command-graph/old/data/`），命令图谱功能**当前不可用**。

与此同时，`command-graph/builder/` 已产出结构化抽取结果（按 md 章节切分的 MMLCommand 字段），存于：

- `command-graph/data/output/mml_commands_udg.jsonl`（4577 条）
- `command-graph/data/output/mml_commands_unc.jsonl`（8498 条）

需要把命令图谱的数据源切换为这两个 JSONL，并让前端**数据驱动地**展示抽取字段——新增/删除/改名字段时，只更新 JSONL，前端无需改代码。

**本次范围**：仅展示 MMLCommand 对象。CommandParameter、ConfigObject 等其它对象暂不展示。

## 2. 目标

1. 后端数据源由 CSV 改为 JSONL，恢复并改进命令图谱功能。
2. 前端保留原有交互：网元 + 版本筛选 + 搜索 → 命令列表 → 详情双 Tab（抽取字段 / 原始 md）。
3. 详情 Tab1「抽取字段」改为**数据驱动**：不写死任何具体内容字段名，record 里的字段自动渲染成 markdown 分区。
4. 抽取字段集合可变，只改 JSONL 即可动态反映。

## 3. 非目标（YAGNI）

- 不构建 CommandParameter / ConfigObject 独立对象或视图（阶段4/5，未来再做）。
- 不做多版本聚合 / 版本治理 G 模型的前端展示（当前仅 20.15.2 一个版本）。
- 不改动 feature_graph、business_graph。
- 列表页列保持固定（均为稳定基本字段）。

## 4. 数据契约

### 4.1 JSONL record 结构（builder 已产出，每行一个 record）

字段**联合**共 25 个 key（已用代码全量核验，13075 条记录的并集）。**字段是稀疏的**：不是每条记录都含全部 key，派生字段仅在可推导时出现。值类型混杂（bool / list / string / object）。设计因此必须数据驱动——硬编码分区会在稀疏字段上失效。

| key | 类型 | 非空率 | 说明 |
|---|---|---|---|
| `command_id` | str | 100% | `UDG@20.15.2:DSP DFSBUCKET` |
| `command_name` | str | 100% | `DSP DFSBUCKET` |
| `command_name_zh` | str | 100% | 中文名 |
| `nf` | str | 100% | 网元（`UDG`/`UNC`），原生字段 |
| `version` | str | 100% | 版本（`20.15.2`），原生字段 |
| `verb` | str | 100% | `DSP` |
| `object_keyword` | str | 99.8% | `DFSBUCKET` |
| `command_function` | str(md) | 100% | 命令功能 |
| `notes` | list[str(md)] | 93.6% | 注意事项，每元素是一段 md |
| `permission_text` | str(md) | 96.4% | 操作权限整段 |
| `parameter_description` | str(md) | 100% | 参数说明 |
| `usage_examples` | list[str(md)] | 100% | 使用实例，每元素含代码块 |
| `output_description` | str(md) | 44.7% | 输出结果说明 |
| `reference_info` | str(md) | 1.7% | 参考信息 |
| `category_path` | list[str] | 100% | `["CoreMind...","DFS..."]` |
| `status` | str | 100% | `active` |
| `source_evidence_ids` | list[str] | 100% | 证据 md 路径（`[0]` 即原始 md 路径，含 `output/` 前缀；后端读原始 md 与前端 DocViewer 均取此） |
| `command_category` | str | 100% | 派生：配置/查询/动作/调测类 |
| `is_dangerous` | bool | 100% | 派生：是否高危（`false` 也展示为"否"） |
| `permission_groups` | list[str] | 96.4% | 派生：`["G_1","G_2","G_3"]` |
| `applicable_nf` | list[str] | 55.5% | 派生：`["UPF"]` |
| `max_records` | num/null | 10.8% | 派生：最大记录数，不可推导时为 `null`（不展示） |
| `output_ref_command` | str | 11.8% | 派生：输出引用命令 |

关键事实（已用代码核验）：
- `command_id` = `{nf}@{version}:{name}`，可靠解析 product/version。
- `source_evidence_ids[0]` 即原始 md 路径，已含 `output/` 前缀 → 原始 md 解析为 `doc_root / source_evidence_ids[0]`（**不**再加 `output/`）。
- UDG / UNC record 字段结构一致（同一 25-key 联合，稀疏程度不同）。
- 空值（`""`/`null`/`[]`/`{}`）在动态分区中**不渲染**。

### 4.2 字段渲染规则（不隐藏任何字段）

**核心原则：record 里所有非空字段一律渲染成分区，不设排除集合、不隐藏。** 用户明确要求"json 所有字段都展示"，任何字段（含 `parameter_description`、身份字段、构建元数据）只要有值就显示。

| 规则 | 说明 |
|---|---|
| **分区来源** | record 中**所有** key（`Object.keys`），按 JSONL 字段顺序遍历。 |
| **分区标题** | `labelMap[key] ?? key`（已知字段出中文名，未知/新字段用原 key）。`labelMap` 纯装饰，缺失即降级为原 key，**不影响功能**。 |
| **空值处理** | `""`/`null`/`[]`/`{}` → 该分区不显示（不是隐藏策略，只是无内容可展示）。`false`/`0` 视为有值，展示。 |
| **hero/侧栏** | 仅作页面标题/导航 chrome（命令名 + 中文名 + 产品/版本标签 + 分类）。**不**从分区中排除任何字段——身份字段会同时在 hero/侧栏和分区中出现。 |

- **取值归一化**：
  - `string` → 直接 `renderMarkdown(value)`。
  - `list` → **每个元素单独 `renderMarkdown`** 后串联（`notes`/`usage_examples` 的元素是含代码块的多行 md，逐元素渲染才不破坏代码围栏/表格）。元素若为非字符串标量先 `String()`。
  - `object` → `JSON.stringify(value, null, 2)` 包代码块渲染。
  - `bool`/`number` → 转字符串渲染（如 `is_dangerous: false` → "否"）。
- **未来扩展**：build 新增任何字段（含审查/派生标记）→ 无需改前端，自动作为分区出现（标题用原 key，除非 labelMap 有中文名）。`labelMap` 是前端唯一"软"配置，缺失不影响展示。

## 5. 后端设计

### 5.1 `platform-next/command_graph/service.py`（重写）

- 去除 `shared.csv_service` 依赖，改读 JSONL。
- `__init__`：加载两个 JSONL，逐行 `json.loads`；从 `command_id` 解析 `product`/`version` 写回 record；内存存 `list[record]` + `dict[command_id → record]`。
- `get_stats()` → `{ total, by_product, by_version, versions }`。
- `list_commands(product=None, version=None, search=None, page=1, size=50)`：
  - 过滤：product == ；version == ；search（跨 command_name / command_name_zh / command_function / category_path，大小写不敏感）。
  - 排序：(product, command_name)。
  - 返回瘦身列表项：`command_id, command_name, command_name_zh, product, version, category_path, command_function, verb`。
- `get_command(product, command_name, version=None) -> record | None`：完整 record 透传（前端自决渲染）。匹配：nf==product 且 name==command_name，version 给定则进一步过滤，取首条。
- `get_command_md(product, command_name, version=None) -> str`：取 record 的 `source_evidence_ids[0]`，读 `doc_root / 该路径`；不存在返回空串。
- `resolve_doc_path` / `get_doc_content` / `serve_file`：保持现有 `output/` 安全沙箱（图片等服务不变）。

### 5.2 `platform-next/command_graph/router.py`

- `/commands`、`/command`、`/command-md` 新增可选 `version: str | None = Query(None)` 参数并透传。
- `/stats`、`/file`、`/doc-content` 不变。

## 6. 前端设计

### 6.1 `frontend/src/api.ts`

- `commands/command/commandMd` 在已传 `product`+`command_name` 基础上透传可选 `version`。

### 6.2 `frontend/src/shared/markdown.ts`（新增）

- 单例 `markdown-it`（与 `DocViewer` 同款配置）+ `dompurify` 净化；导出 `renderMarkdown(src: string): string`。
- 供 CommandDetail 动态分区与任意 md 文本渲染复用。

### 6.3 `frontend/src/command_graph/CommandList.vue`

- 筛选栏在「产品」`el-select` 旁新增「版本」`el-select`（options 来自 `stats.versions`，按字母序）。
- 任一筛选变更：`page=1` 后重新加载。
- `category_path` 现为数组 → `formatCategoryPath` 直接 `(arr||[]).join(' > ')`，移除 `JSON.parse`。
- 表格列：命令 / 中文名 / 产品 / 版本（新增列）/ 分类路径 / 功能（command_function 预览，缺失显示 `-`）。
- 行点击 → `router.push({ name: 'command-detail', params: { product, commandName } })`（路由形态不变）。

### 6.4 `frontend/src/command_graph/CommandDetail.vue`

- **Tab1「抽取字段」= 数据驱动**：
  - hero：command_name（大）、command_name_zh、product tag、version tag。
  - 计算分区：遍历 `Object.keys(record)` **所有** key（不排除任何字段，仅跳过空值），按原顺序映射为 `{ key, label, html }`。
  - 每分区：标题 `labelMap[key] ?? key`；取值归一化（§4.2 规则）；`v-html="renderMarkdown(...)"`。
  - 空值分区不显示。
  - **彻底移除**当前 `CommandDetail.vue` 中所有硬编码内容分区：现有的「命令功能」「注意事项」「操作用户权限」「使用实例」四个 `summary-section` 块 + 底部「全部字段」键值表，**全部删除**，统一由上述数据驱动循环生成。hero 区块保留。
- **Tab2「原始文档」**：机制不变，`DocViewer` 读 `command-md` 返回内容。
- 侧栏：product / version / category_path 标签（仅作导航 chrome；这些字段也会出现在 Tab1 分区中，不冲突）。
- 路由保持 `/:product/:commandName`（当前同命令单版本，product+name 唯一；内部按 command_id 精确查找）。

### 6.5 路由 `frontend/src/router.ts`

- 不变（`/command-graph/:product/:commandName(.*)`）。

## 7. 单元边界与接口

| 单元 | 职责 | 接口 | 依赖 |
|---|---|---|---|
| `CommandGraphService` | 加载 JSONL、过滤、查找、读 md | `get_stats/list_commands/get_command/get_command_md` | JSONL 文件、doc_root |
| `router` | HTTP 路由 | `/stats /commands /command /command-md /file /doc-content` | service |
| `markdown.ts` | md → 安全 HTML | `renderMarkdown(src)` | markdown-it, dompurify |
| `CommandList.vue` | 列表 + 筛选 + 搜索 | props 无；emit 路由跳转 | api |
| `CommandDetail.vue` | 数据驱动字段分区 + 双 Tab | route params | api, markdown.ts, DocViewer |

每个单元可独立理解与测试：service 可单测（mock JSONL），markdown 可单测（输入→输出 HTML），组件可按 record fixture 测试分区渲染。

## 8. 错误处理 / 边界

- JSONL 文件缺失/行解析失败：跳过坏行，日志计数；service 不抛（返回空集合）。
- `get_command` 找不到：返回 None，router 返回 `{error: ...}`，前端显示「命令未找到」。
- `source_evidence_ids[0]` 指向文件不存在：`get_command_md` 返回空串，Tab2 显示「无关联文档」。
- 非法字段值（非 str/list/object）：归一化为字符串，不崩。
- 大分区内容（长 md）：分区自然换行；列表分页仍由后端控制。

## 9. 验收标准

1. `/stats` 返回 total=13075、by_product={UDG:4577, UNC:8498}、by_version={20.15.2:13075}、versions=["20.15.2"]。
2. `/commands?product=UDG&search=URR` 能返回含 `ADD URR` 等的列表，分页正确。
3. `/commands?product=UDG&version=20.15.2` 与不传 version 结果一致。
4. `/command?product=UDG&command_name=ADD URR` 返回完整 record（含 notes/usage_examples 等 list 字段）。
5. `/command-md?product=UDG&command_name=ADD URR` 返回原始 md（非空）。
6. 前端列表：产品+版本下拉、搜索、分页正常；行点击进详情。
7. 详情 Tab1：record 所有非空字段（含 `parameter_description`/`nf`/`command_category`/`is_dangerous` 等）均出现为 markdown 分区；标题中文/原 key 正确。
8. 详情 Tab2：渲染原始 md，图片/锚点正常。
9. 在 JSONL 里新增一个测试字段后，前端无需改代码即出现新分区。

## 10. 风险

- **R1**：`labelMap` 是装饰性硬编码，字段改名后降级为原 key（可接受，非功能阻断）。
- **R2**：路由用 product+commandName 而非 command_id，未来多版本同名命令需演进（当前单版本，已知限制）。
- **R3**（已澄清）：用户确认"json 所有字段都展示"，不设任何隐藏列表；`parameter_description` 与全部字段均展示。
