# CommandGraph 重构实现计划

> **For agentic workers:** 用 superpowers:subagent-driven-development 实施。步骤用 `- [ ]` 跟踪。

**Goal:** 把命令图谱从"散装流水线+平铺前端+硬编码"重构为"隔离资产目录+一键 pipeline+三级漏斗导航+配置驱动"，新建干净目录 `CommandGraph/`。

**Architecture:** 三层自底向上——Phase1 在 `CommandGraph/` 重建设计态（pipeline.yaml + build_all.py + 模块化抽取器，保留已验证抽取逻辑）；Phase2 platform-next 后端扫描 `CommandGraph/assets` 自动加载、去硬编码、`product`→`nf`、嵌套 stats；Phase3 前端三级漏斗 + 面包屑 + 版本内搜索。

**Tech Stack:** Python 3.12 / FastAPI / Vue 3 + Element Plus / pytest / vitest(可选)

**Spec:** `docs/superpowers/specs/2026-06-25-commandgraph-redesign-design.md`

---

## Chunk 1: Phase 1 — 数据层（CommandGraph/）

### Task 1.1: 骨架与配置

**Files:**
- Create: `CommandGraph/pipeline.yaml`
- Create: `CommandGraph/builder/__init__.py`（空）
- Create: `CommandGraph/builder/constants.py`
- Create: `CommandGraph/builder/core/__init__.py`（空）
- Create: `CommandGraph/builder/extractors/__init__.py`（空）
- Create: `CommandGraph/builder/steps/__init__.py`（空）

- [ ] **Step 1: 建 `pipeline.yaml`**（内容见 spec §3.2；assets_root=data/assets，project_root=..，UDG/UNC 两个网元各 20.15.2）
- [ ] **Step 2: 建 `constants.py`**：`PLACEHOLDER_PARAMETER_NAMES`、`PLACEHOLDER_ID=-2`（从旧 `build_commandparameter.py:21,98` 搬），`ACTIVE_STATUS='active'`，无绝对路径
- [ ] **Step 3: 建包 `__init__.py`**

### Task 1.2: sections.yaml + md_reader（章节字段配置化）

**Files:**
- Create: `CommandGraph/builder/sections.yaml`
- Create: `CommandGraph/builder/core/md_reader.py`
- Port from: `command-graph/builder/md_reader.py`

- [ ] **Step 1: sections.yaml**：把旧 `md_reader._SECTION_TO_FIELD`（19-35 行）搬成 YAML（精确+前缀两段匹配逻辑在代码里保留）
- [ ] **Step 2: md_reader.py**：移植 `parse_md`/`map_section`/`_clean_link` 与正则；`map_section` 改为加载 `sections.yaml`（启动读一次缓存）；`_FIELDS` 从 YAML 的字段集合推导
- [ ] **Step 3: 测试**：脏数据标题（如"操作用户权限DSP RU"）前缀匹配命中

### Task 1.3: identity + mmlcommand step（基本信息，保留 to_mmlcommand）

**Files:**
- Create: `CommandGraph/builder/core/identity.py`
- Create: `CommandGraph/builder/steps/mmlcommand.py`
- Port from: `command-graph/builder/build_mmlcommand.py`（`to_mmlcommand`、`split_code`、main 的扫描逻辑）

- [ ] **Step 1: identity.py**：`to_mmlcommand(raw, nf, version, md_path)` 原样移植（17 基本字段，含 `nf` 不改名）
- [ ] **Step 2: steps/mmlcommand.py**：`run(ctx) -> int`——扫描 `ctx.source` 下 `*.md`，parse_md→to_mmlcommand，去重写 `assets/{nf}/{version}/mml_commands.jsonl`。参数从 ctx 取（nf/version/source/project_root/output_path），不再用 argparse

### Task 1.4: extractors registry + 10 个派生 extractor

**Files:**
- Create: `CommandGraph/builder/extractors/registry.py`
- Create: `CommandGraph/builder/extractors/{command_category,applicable_nf,max_records,permission_groups,output_ref_command,is_dangerous,effect_mode,spec_threshold,initial_values,output_fields}.py`
- Port from: `command-graph/builder/enrich_mmlcommand.py`（10 个函数 + `_VERB_CATEGORY`）

- [ ] **Step 1: registry.py**：`@register(name)` 装饰器 + `_REGISTRY` 列表 + `apply_all(cmd) -> dict`（遍历调用，immutable 合并到新 dict）。`_VERB_CATEGORY` 放 `command_category.py` 或配置
- [ ] **Step 2: 10 个 extractor 文件**：每个移植一个函数，签名统一为 `(cmd: dict) -> value`（从 cmd 取原始字段，而非多参数），用 `@register('field_name')` 注册
- [ ] **Step 3: 测试**：注册一个 extractor → `apply_all` 返回含该字段；返回的 dict 与输入非同一对象（immutable）

### Task 1.5: enrich + parameter step

**Files:**
- Create: `CommandGraph/builder/steps/enrich.py`
- Create: `CommandGraph/builder/steps/parameter.py`
- Port from: `command-graph/builder/build_commandparameter.py`

- [ ] **Step 1: steps/enrich.py**：`run(ctx)`——读 `mml_commands.jsonl`，逐行 `extractors.registry.apply_all`，写回同文件；打印各字段非空率（沿用旧 enrich 的统计打印）
- [ ] **Step 2: steps/parameter.py**：`run(ctx)`——CSV→CommandParameter JSONL + `command_has_parameter` + `parameter_depends_on` 两个关系 sidecar。移植旧 `build_commandparameter.py` 全部逻辑（CSV 列名、占位符过滤、关系解析），CSV 路径从 `ctx.parameter_csv` 取

### Task 1.6: build_all.py 编排器 + step registry

**Files:**
- Create: `CommandGraph/builder/steps/registry.py`（name→step.run 映射）
- Create: `CommandGraph/build_all.py`

- [ ] **Step 1: steps/registry.py**：`STEPS = {'mmlcommand': mmlcommand.run, 'enrich': enrich.run, 'parameter': parameter.run}`；缺前置校验（enrich/parameter 依赖 mmlcommand 产物）
- [ ] **Step 2: build_all.py**：
  ```python
  # 读 pipeline.yaml → 选性过滤 [nf] [version] → 依序跑 steps → 写 assets/
  # 每个 (nf,version,step) 失败 try/except，打印三元组错误，继续其他
  # ctx = SimpleNamespace(nf=, version=, source=, project_root=, assets_root=, output_path=, parameter_csv=)
  ```
- [ ] **Step 3: 跑全量**：`python CommandGraph/build_all.py` → 生成 `CommandGraph/data/assets/{UDG,UNC}/20.15.2/*.jsonl`
- [ ] **Step 4: 对比验证**（关键 gate）：新 `mml_commands.jsonl` 行数 == 旧 `command-graph/data/output/mml_commands_{udg,unc}.jsonl` 行数；各派生字段非空率一致。不一致则定位修复

### Task 1.7: 测试

**Files:**
- Create: `CommandGraph/tests/test_build_all.py`（选性执行、步骤顺序、单步失败隔离）
- Create: `CommandGraph/tests/test_extractors_registry.py`（注册即调用、immutable）
- Port: `command-graph/tests/test_build_commandparameter.py` → `CommandGraph/tests/`

- [ ] **Step 1: 移植 + 新增测试，pytest 全绿**

---

## Chunk 2: Phase 2 — 后端（platform-next/command_graph/）

### Task 2.1: service.py 重写（扫描 assets + 嵌套 stats + nf 统一）

**Files:**
- Modify: `platform-next/command_graph/service.py`（整体重写加载/统计部分）
- Modify: `platform-next/config.yaml`（加 assets_root）

- [ ] **Step 1: config.yaml 加** `command_graph.assets_root: "../CommandGraph/data/assets"`
- [ ] **Step 2: service.py 用 `shared.config.get_config()` 读 assets_root**（替代 16-18 行硬编码）
- [ ] **Step 3: `_load` 改为扫描** `assets_root/{nf}/{version}/*.jsonl`：glob 发现所有 nf/version/object；按 (nf,version,object_type) 索引；MMLCommand 进主索引，CommandParameter 计入 parameter_count
- [ ] **Step 4: `get_stats` 返回嵌套结构**：`{total, total_parameters, nes:[{name, command_count, parameter_count, versions:[{version, command_count, parameter_count}]}]}`（同时保留 `by_nf`/`versions` 供过渡）
- [ ] **Step 5: 内部 `product`→`nf`**，删 `_slim` 的 nf→product 映射（68 行）；`list_commands`/`get_command` 参数 `product`→`nf`
- [ ] **Step 6: 跑后端冒烟**：启动 → `/stats` 返回嵌套结构，UDG/UNC 计数正确

### Task 2.2: router.py（nf 主参数 + product 兼容别名）

**Files:**
- Modify: `platform-next/command_graph/router.py`

- [ ] **Step 1: 所有端点 `product`→`nf`**；为兼容旧前端，`list_commands`/`get_command`/`get_command_md` 同时接受 `product: str | None = Query(None, alias=...)` 或在 service 层 `nf = nf or product` 兼容
- [ ] **Step 2: `/stats` 直接返回嵌套**；其余契约不变

---

## Chunk 3: Phase 3 — 前端（platform-next/frontend/src/command_graph/）

### Task 3.1: 路由漏斗 + api.ts

**Files:**
- Modify: `platform-next/frontend/src/router.ts`
- Modify: `platform-next/frontend/src/api.ts`

- [ ] **Step 1: router.ts 改 `/command-graph` 子路由**：
  ```
  children:
    '' → CommandOverview (name: command-overview)
    ':nf' → CommandVersions (name: command-versions)
    ':nf/:version' → CommandList (name: command-list)
  /command-graph/:nf/:version/:commandName(.*) → CommandDetail (name: command-detail)
  ```
- [ ] **Step 2: api.ts**：`command(product,...)`→`command(nf, commandName, version)`，参数键 `nf`；`commandMd` 同理

### Task 3.2: CommandOverview.vue（L1 新建）

**Files:**
- Create: `platform-next/frontend/src/command_graph/CommandOverview.vue`

- [ ] **Step 1: 调 `/stats`**：渲染统计数字（总命令/网元数/版本数/参数数）+ 网元卡片网格（每卡：网元名/版本数/命令数），点卡 → `router.push({name:'command-versions', params:{nf}})`

### Task 3.3: CommandVersions.vue（L2 新建）

**Files:**
- Create: `platform-next/frontend/src/command_graph/CommandVersions.vue`

- [ ] **Step 1: 从 `/stats` 的 `nes[].versions` 取选中 nf 的版本卡片**（版本号/命令数/参数数），点卡 → `router.push({name:'command-list', params:{nf, version}})`

### Task 3.4: CommandList.vue（L3 改造）

**Files:**
- Modify: `platform-next/frontend/src/command_graph/CommandList.vue`

- [ ] **Step 1: 删 product/version 筛选器**；从路由 param 取 `nf`/`version` 固定范围
- [ ] **Step 2: 保留搜索框**（版本内）；调 `/commands?nf=&version=&search=`；`filters.product`→`filters.nf`
- [ ] **Step 3: 点行 → 详情**：`router.push({name:'command-detail', params:{nf, version, commandName}})`

### Task 3.5: CommandDetail.vue + CommandIndex.vue（小改）

**Files:**
- Modify: `platform-next/frontend/src/command_graph/CommandDetail.vue`
- Modify: `platform-next/frontend/src/command_graph/CommandIndex.vue`

- [ ] **Step 1: CommandDetail route param `product`→`nf`**，补 `version`；双栏动态 sections 不动
- [ ] **Step 2: CommandIndex 加面包屑**（统计 > {nf} > {version}，从 route param 推导，可点击回退）

### Task 3.6: 前端构建验证

- [ ] **Step 1: `cd platform-next/frontend && npm run build`** 通过，无 TS 报错

---

## Chunk 4: 端到端验证与收尾

- [ ] **Step 1: 启动后端** `cd platform-next && python main.py`，浏览器/ curl 验证 `/stats` 嵌套、`/commands?nf=UDG&version=20.15.2`、漏斗三级可点通、详情双栏 + 原始文档
- [ ] **Step 2: 删 `product` 兼容别名**（Phase 2.2 引入），前端已全切 nf
- [ ] **Step 3: 旧 `command-graph/` 暂保留**（验证后用户决定是否删）
