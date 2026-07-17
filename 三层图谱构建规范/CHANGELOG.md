# CHANGELOG

本目录所有变更留痕。**append-only**，最新在上。

---

## 条目格式

每条变更必须包含：

| 字段 | 说明 |
|---|---|
| 版本号 | `MAJOR.MINOR.PATCH`（规则见 [演进机制](演进机制.md)） |
| 日期 | YYYY-MM-DD |
| 变更类型 | 新增 / 修改 / 废弃 / 修复 |
| 变了什么 | 具体改动 |
| 为什么 | 动机 |
| 影响哪些文件 | 文件路径清单 |
| 对已建资产的影响 | 无 / 需重建 / 可兼容 |

## 版本号规则（简述）

- **MAJOR**：不兼容变更，已建资产需重建
- **MINOR**：向后兼容的新增（加字段、加可选规则）
- **PATCH**：措辞澄清、笔误，无行为变化

> 完整规则见 [演进机制](演进机制.md)。

---

## [0.10.0] - 2026-07-16

### 变更（采纳 CR-20260716-001）
- **Feature 模型：文件夹模型 → feature_code 聚合模型**。`build_features.py` 改为遍历 feature-dir 下**全部 md**，按其路径里**最深的 feature_code** 归组（最深=最具体的特性，跳过上级分类码）。同 code 的所有 md 进一个特性文件夹。
  - 解决 v0.9.0 三大缺口：① 嵌套子目录 md 漏收（`glob("*.md")` 非递归）② 特性 md 作为文件落在分类目录里扫不到 ③ 同 code 多文件夹互相覆盖。
- **ID 机制：doc_type 降为 YAML 字段，改用源文件名 slug 作 ID 区分位**。
  - 子文档 ID = `{nf}@Feature@{code}-{slug}`（slug=源文件名去 `_{数字id}.md` 后缀）；概述仍 = `{nf}@Feature@{code}`。
  - 原因：doc_type 是多对一分类（一特性下 N 个「原理」文件），拿它当 ID 后缀会撞名覆盖（如 IPFD-014001 的 28 个原理文件争抢 `-原理`）。同特性 slug 撞名 → 前补父目录消歧。
- `_common.py`：加 `slugify_doc()`、`derive_doc_type()`（文件名关键词优先、否则按所在子目录）；doc_type 关键词补 `调测/部署/术语`；删无用 `sanitize_doc_type`。
- **修复双 H1**：`build_features.py` 之前 prepend `# {doc_name}`，但原文自带 H1 → 全部双 H1。改为**对齐命令层**：body 不 prepend、保留原文 H1（单 H1）；`name` 改从原文首个 H1 取（修掉无文件夹特性 name 回退纯 code 的问题）。
- **修复 License 漏建**：`LICENSE_HEAD_RE` 之前要求段头 control_id 为纯数字 `(\d+)`，但实际 control_id 有**两种格式**（纯数字 `81203214` + 字母数字 `82200CKP`）→ 漏建 89 个 license。放宽为 `([A-Z0-9]+)`，code 锚定 LKV 格式。License 98 → **187**。
  - 教训：v0.9.0 核查 License"98/98 干净"是假象——核查用了和构建**同一条正则**，盲区一致查不出漏建。`check.md` 增"核查独立性"项。
- **修复所需License 边误报**：之前扫概述**全文**取 LKV code，把互斥/交互表里**别的特性的 license** 误挂成本特性所需（如 GWFD-010108 错挂 GWFD-110910 的 LKV3G5RBMS01）。改为**只扫「可获得性」章节**；依赖特性边的 `or md_text` 兜底同步收紧为空。所需License 边 225→168，**真误报 82→0、真漏 0**（对可比特性集与旧版 feature_requires_license.jsonl 完全对齐）。
- 文档同步：`SKILL.md`（聚合模型+文件名ID）、`字段定义.md`（Feature 7 字段、doc_type 不进 ID、control_id 两格式）、`check.md`（ID 唯一/聚合/概述存在/单H1/核查独立性 检查项）、`需求与路线.md`（决策状态）。

### 自测
- 全量 UDG：**258 特性 / 865 Feature 文档 + 187 License**（v0.9.0 仅 127/417 + 98）。铁证 IPFD-014001 支持OSPF：源 29 个 md 全收齐，每个 ID 唯一；铁证 LKV3G5RBMS01（control_id `82200CKP`）从漏建→已建。
- 全局 0 重复 ID / 0 同文件夹重名 / 865 文档单 H1；无概述特性 1 个（NPFD-010005）、多概述候选 4 个（取首个并记录）。
- 边闭环 1929 条，闭环 1885（**97%**）；剩 44 断裂全是真·无资产引用（2 跨产品 license + 41 指向分类码/无概述特性 + 1 NPFD-010005），非构建 bug。
- **所需License 边精度**：对可比特性集与旧版 `feature_requires_license.jsonl` 完全对齐（真误报 0、真漏 0）；168 条边里 25 条是旧版未收录特性的合法边。
- 用老版本（FeatureGraph legacy，**仅 check 不作输入**）对比：老 303(含 83 幽灵)/831 doc；本次 258/865 覆盖 216/220 真特性（漏的 4 个是分类目录码，不建才对）+ 多收老漏的 25 个真特性。

### 对已建资产的影响
- **Feature + License 侧均需重建**（v0.9.0 资产作废，已删重建）。

### 类型
- MINOR（Feature 收集模型 + ID 机制变更；向后兼容的新规则集合，但已建 Feature 资产需重建）

---

## [0.9.0] - 2026-07-16

### 新增
- **特性层能力包**（`feature/`）：与命令层同构
  - **Feature 文件夹模型**：每特性一个文件夹，里面每个 md（概述/激活/参考信息…）都是 `YAML+原文+边` 统一资产，按 ID 引用（概述=`{nf}@Feature@{code}`，子文档=`…-{doc_type}`）
  - **License 段落模型**：控制项 md 按 `#### [{control_id} {code} {名}]` 切段，每 license 一资产
  - `SKILL.md` / `字段定义.md`（Feature 6字段 + License 7字段）/ `check.md` / `template/`
  - `scripts/`：`build_features`（文件夹+doc类型识别+边推导）/ `build_licenses`（段切分）/ `build_all`（编排）/ `_common`（共享）
  - 边全从源文档推导（Feature↔License 所需License↔对应特性、Feature→Feature 依赖、概述↔子文档），**不依赖 FeatureGraph jsonl**

### 自测
- IPv6功能子集：**6 特性 / 22 文档 + 98 license**。验证：文件夹结构、doc类型识别（概述/激活/参考信息/原理…）、概述边（所需License+依赖特性）、license 段切分+对应特性边

### 类型
- MINOR（新增特性层能力包）

---

## [0.8.4] - 2026-07-16

### 变更
- **删除 `source` 字段**（命令 + 配置对象）：命令正文即原始产品文档内容（复用原文），source 指向 output/ 属冗余；配置对象合成、source 无意义
- **原始产品文档不进资产**：`build_all` 的 `--product-doc` 改为导出到**临时目录**（不写 `{storage}/output/`）；资产只有 `Command/` + `ConfigObject/`
- 字段数：命令 12→11、配置对象 10→9；文档（字段定义 / SKILL / check）同步去 source
- 验证：三层图谱资产/ 仅 Command+ConfigObject、无 source 字段、无 output/

### 类型
- MINOR（字段删减 + 存储模型简化；命令正文内容不变，pre-1.0 资产重建无迁移负担）

---

## [0.8.3] - 2026-07-16

### 修复（文档同步 + 规则定稿）
- **配置对象产生规则定稿**：只有配置类命令(ADD/MOD/DEL/RMV/SET)产生配置对象；查询(LST/DSP)/动作(ACT)不产生（但可关联已存在的）。全量 UDG 配置对象 2107→1175（剔除查询/动作专属对象）
- 文档同步到当前实现：
  - 重写 `check.md`（旧规则全替换：三段式逻辑ID、逻辑ID文件名、关系统一进"边"章节、`source` 字段、配置类产生规则、参数不单独建）
  - `字段定义.md` 配置对象改 10 字段（+`object_kind`）、正文仅 `## 说明`
  - `SKILL.md` 补"配置类才产生配置对象"规则、边表更新、sop_version 0.8.3
- 清空样例资产目录 `三层图谱资产/`（交付干净状态）

### 类型
- PATCH（文档同步 + 规则收窄；命令层构建行为对齐最终规则）

---

## [0.8.2] - 2026-07-16

### 修复（测试反馈 5 问题）
1. **非命令混入**：`集中配置概念` 等无"中文（英文码）"标题的页面被误收 → `parse_title` 强制命令标题模式，跳过（4580→4577，过滤 3）
2. **边假阳**：`参见:[[...ADD A]]` 正文片段误匹配 → 边校验（只引真实存在的命令，2 趟收名集）+ regex 收紧（object token ≥2 字符）
3. **冗余**：TOC 链接行 + 标题 anchor `(#xxx)` 导出残留 → `clean_md` 清洗
4. **命令↔命令边**：校验后保留真实边（1326 命令有"参见"边，如 `ADD URR → MOD CFGTHRESHOLD`）
5. **配置对象无描述**：补 ADD 命令"命令功能"作描述（对应原 jsonl `description`）

### 影响
- 重写 `build_commands.py`（过滤 + 清洗 + 2 趟校验）；改 `build_configobjects.py`（补描述）
- 重跑全量 UDG 验证：4577 命令 + 2210 配置对象，5 问题全解

### 类型
- PATCH（构建质量修复；输出微调：原文清洗 + 配置对象补描述）

---

## [0.8.1] - 2026-07-16

### 清理 / 交付
- `command/` 清理为干净任务包：删 obsolete `调研-输入输出与存储格式.md`（旧全量抽取路线，已被 `需求与路线.md` 取代）+ `scripts/__pycache__`
- 修 `agent.md` / `check.md` 旧"三类对象"表述 → 命令+配置对象两类（参数在命令 md 内）；修 agent.md 已删调研文档的断链
- 构建样例资产目录 `三层图谱资产/`（全量 UDG：**4580 命令 + 2210 配置对象**，自包含 `output/`，source 路径资产根相对、边闭环验证通过）

### 类型
- PATCH（文档清理 + 样例产物；无构建行为变更）

---

## [0.8.0] - 2026-07-16

### 变更
- 命令层对象收窄为 **命令 + 配置对象** 两类：**参数不单独建 md**（参数说明表在命令 md 原文内）
- 删 `build_parameters.py`；新增 `build_configobjects.py`（按 object_keyword 聚合命令族 → 配置对象 md，**反向边闭环**）
- 新增 `_common.py`（共享解析/YAML/边工具）
- 新增 `build_all.py` **端到端编排器**：原始产品文档(自动导出到 {storage}/output/) 或 已解压目录 → 命令 → 配置对象

### 自测
- 计费控制子集：**40 命令 + 17 配置对象**端到端通过。配置对象 URR 验证：聚合 ADD/LST/MOD/RMV URR 命令族，边 `被操作` 与命令的 `操作配置对象` **双向闭环**

### 为什么
- 用户明确：参数在命令 md 内不单独建；命令层=命令+配置对象；要端到端（原始文档→资产）

### 影响文件
- 新增 `command/scripts/{_common,build_configobjects,build_all}.py`
- 删 `command/scripts/build_parameters.py`
- 重写 `command/{SKILL,字段定义}.md`（2 类对象）；更新 需求与路线 / README

### 类型
- MINOR

---

## [0.7.0] - 2026-07-16

### 新增
- **命令层能力包核心**（`command/`）：
  - `SKILL.md` 构建流程（输入 5 项 → 输出；模块化边）
  - `字段定义.md`（12 YAML 字段，来源/规则）
  - `template/command.md.tpl`（骨架）
  - `scripts/build_commands.py`（构建器，纯标准库；模块化边：`edge_configobject` 代码推导 / `edge_cmdref_body` 正文扫描 / `edge_cmdref_intranet` 内网图谱可选）

### 自测
- 计费控制子集 **40 命令构建通过**（0 跳过）。ADD URR 验证：YAML 12 字段全对（id 网元在前、`applicable_nf=[PGW-U,UPF]`、`effect_mode=立即生效` 正确抽取）、原始 md 原样保留、边正确（`[[UDG@ConfigObject@URR]]` 推导 + `[[UDG@MMLCommand@MOD CFGTHRESHOLD]]` 正文扫出）

### 为什么
- 命令层需求全锁定（`需求与路线.md`），落地**可测试**的能力包：另一个 Agent 直接跑脚本即可验证

### 影响文件
- 新增 `command/SKILL.md` / `字段定义.md` / `template/command.md.tpl` / `scripts/build_commands.py`
- `VERSION` → 0.7.0

### 类型
- MINOR

---

## [0.6.0] - 2026-07-15

### 新增
- 顶层 `层包标准.md`：每层文件夹统一结构标准（加新层照此，确保四层同构）
- `feature/agent.md` / `task/agent.md` / `business/agent.md`：**恢复**上轮重构误删的其它层构建师人设（已按层下沉、对齐 per-layer 模型）
- `command/需求与路线.md`：忠实记录命令层新需求与路线转变（复用原始md + YAML frontmatter，非全量抽取；evidence 不拷贝直接引用 output；引用以资产根相对路径）

### 为什么
- 统一目录管理需罗列清楚，确保其它层照标准构建；上轮重构误删其它层 agent.md 需恢复；命令层路线重大调整必须记录以免遗忘

### 影响文件
- 新增 `层包标准.md` / `feature/agent.md` / `task/agent.md` / `business/agent.md` / `command/需求与路线.md`
- 更新 `README.md`（引用层包标准 + 各层状态）、`VERSION` → 0.6.0

### 对已建资产的影响
- 无

### 类型
- MINOR（向后兼容新增）

---

## [0.5.0] - 2026-07-15

### 重构
- 结构改为"**全局顶层 + 每层独立能力包**"（整体=大能力包，每层=独立能力包）
- 顶层 `agents/` 解散（构建师 / 核查下沉到各层）
- 顶层 `change-requests/` 下沉到各层（→ `command/change-requests/`）
- `command/` 成为完整独立包：`agent.md` + `check.md` + `change-requests/` + 调研

### 为什么
- 每层构建要独立可测。全局放顶层，每层下沉；层与层互不依赖

### 影响文件
- 移动 `agents/命令构建师.md` → `command/agent.md`（角色引用同步改为本层 check / 本层 change-requests）
- 移动 `change-requests/` → `command/change-requests/`
- 删除顶层 `agents/`（特性/Task/业务构建师 + 核查师 + SOP维护师——随各层开建时在层内重建）
- 新增 `command/check.md`（命令层核查：角色纪律 + 审查项类别）
- 重写 `README.md`（结构原则 + 统一层包模板 + 每层协作闭环）

### 对已建资产的影响
- 无（尚无资产；纯规范结构重组）

### 类型
- MINOR（结构重组，向后兼容；无绑定 spec 变更）

---

## [0.4.0] - 2026-07-15

### 新增
- `conventions/命名规范-建议.md`：基于现有 `assets/` 的命名观察 + 统一建议（advisory）

### 为什么
- 现有资产命名存在 NF 隔离/非隔离两类、大小写不统一、命令语义段空格等问题。先给统一建议，各层细化时定夺后再升格为绑定规则

### 影响文件
- 新增 `conventions/命名规范-建议.md`
- 更新 `README.md`（结构 + 状态）、`VERSION` → 0.4.0

### 对已建资产的影响
- 无（advisory，非绑定；现有 `assets/` 不据此改动）

### 类型
- MINOR（向后兼容的新增）

---

## [0.3.0] - 2026-07-15

### 新增
- `agents/` 人设组件：6 个特化 Agent 角色
  - 4 个构建师（命令/特性/Task/业务，按层特化）
  - 1 核查师（独立审查，与构建方分离）
  - 1 SOP 维护师（处理 change-request，修规范）

### 为什么
- 构建工作由不同人设完成，避免单一 Agent"自建自审"。核心是职责分离：**构建 ≠ 核查 ≠ 维护**

### 影响文件
- 新增 `agents/README.md` + 6 个人设规格文档（命令构建师/特性构建师/Task构建师/业务构建师/核查师/SOP维护师）
- 更新 `README.md`（结构 + 状态 + 阅读顺序）、`VERSION` → 0.3.0

### 对已建资产的影响
- 无（尚无资产；人设规格只定角色边界，具体构建方法在各层 SOP）

### 类型
- MINOR（向后兼容的新增）

---

## [0.2.0] - 2026-07-15

### 新增
- `scripts/` 组件：构建管线（产品文档 → 资产）
- 纳入阶段0 脚本 `product_doc_md_exporter_optimized.py`（复制自仓库根目录，原文件保留）

### 为什么
- 本规范的输入起点是**原始产品文档**，不是已导出的 md。必须把"产品文档→md"这第一环纳入，否则 Agent 有 SOP 却没入口工具

### 影响文件
- 新增 `scripts/README.md`
- 复制 `product_doc_md_exporter_optimized.py` 到 `scripts/`（根目录原文件保留）
- 更新 `README.md`（结构 + 状态 + 阅读顺序）、`VERSION` → 0.2.0
- 仓库根 `README.md`：标注同名副本亦在规范包
- 规范文档（README / 演进机制 / change-requests）去除部署术语（内网/外网），统一为角色表述（SOP 维护方 / Agent）

### 对已建资产的影响
- 无（尚无资产基于本规范构建；脚本复制一份，原文件保留，行为不变）

### 类型
- MINOR（向后兼容的新增）

---

## [0.1.0] - 2026-07-15

### 新增
- 初始架构骨架

### 为什么
- 建立规范的元框架（Agent 入口 + 演进机制 + 变更回路），为逐类对象 SOP 打基础

### 影响文件
- `README.md`
- `VERSION`
- `CHANGELOG.md`
- `演进机制.md`
- `change-requests/README.md`

### 对已建资产的影响
- 无（尚无资产基于本规范构建）
