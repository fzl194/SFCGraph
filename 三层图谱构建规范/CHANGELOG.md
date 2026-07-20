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

## [0.13.0] - 2026-07-18

### 变更（文档引用统一为 `[[逻辑ID]]` + 三层落地 + 前端查名渲染）
- **引用格式：相对路径 → 裸逻辑引用 `[[ID]]`**。特性/命令/ConfigObject 三层正文里的命令引用、特性引用统一成 `[[{nf}@MMLCommand@{cmd}]]` / `[[{nf}@Feature@{code}]]`，与 `## 边` 段同源；前端一套正则识别 + 跳转。**接续并取代 v0.12.0 的相对路径引用**（v0.12.0 的特性引用是 `[文字](../../../../Command/…)`，本版起全改 `[[ID]]`）。
- **特性引用精确到具体子文档**（非笼统指特性文件夹）：特性层构建前预算「源文件名→目标文档ID」映射，特性引用按源文件名精确命中——概述引用→`[[{nf}@Feature@{code}]]`，子文档引用→`[[{nf}@Feature@{code}-{slug}]]`。修了一个关键 bug：子文档文件名**不含特性码**（码在文件夹路径里），旧逻辑靠叶子名匹配特性码会漏掉全部子文档引用（曾误剥为纯文字）。
- **命令层 / ConfigObject 首次具备图片+引用处理**（v0.12.0 只做了特性层）：移植 `rewrite_images`/`rewrite_doc_refs` 到 `command/scripts/_common.py`；`build_commands.py` 接线（命令索引用第一趟内存 `command_names`，图片拷到 `Command/{nf}/{ver}/assets/`）；`build_configobjects.py` 对继承自命令的 `desc` 补图片重解析（`[[ID]]` 透传）。
- **前端 `[[ID]]` 查名渲染**：后端新增 `GET /api/v1/names`（{id:name} 字典）；前端 `MdPreview.vue` 拉 `/names` 建 id→name 映射，正文 `[[ID]]` 显示目标 name（无则显 ID）、`title` 存 ID；点击跳转复用既有 `inlineLinksIntoHtml→emit('navigate')→syncTo` 链路（零改）。
- 文档同步：`conventions/资产图片与引用处理.md`（引用规则改 `[[ID]]`+子文档精度+三层落地）、`feature/SKILL.md`+`check.md`（引用闭环改 `[[ID]]`）、`command/SKILL.md`+`check.md`（sop_version 0.13.0、新增图片闭环/引用闭环两项）。

### 修复
- **`build_features.py:assign_slugs` 死循环**：撞名消歧的 `while True` 在「两个文档 slug 相同且父目录相同/为空」时无限前补父目录（字符串一直变长、`resolved` 永真）→ UNC 某特性触发后构建挂死。改为「一轮父目录消歧后撞名数未减则加序号收尾」。此 bug 先于 v0.13.0 存在，UNC 数据首次触发；UDG 未受影响（无此碰撞）。

### 为什么
- v0.12.0 的相对路径引用能点但脆（目录树一搬就断），且与 `## 边` 的 `[[ID]]` 两套格式；用户要求统一成 `[[ID]]` 供前端自动识别跳转，并精确到特性的具体子文档（特性是多文档文件夹）。

### 自测
- **特性 UDG**：258 特性/865 文档；图片 830；引用解析 8258 / 剥死链 968。其中命令引用 7227、特性概述引用 1424、**特性子文档引用 1170**（修 bug 前为 0，全被误剥）；0 残留相对路径。
- **命令 UDG**：4577 命令；图片 493；引用解析 1267 / 剥死链 35。**ConfigObject UDG**：1175 个 / 图片 219。
- **命令 UNC**：图片 635 / 引用解析 4951；**ConfigObject UNC**：2325 / 图片 279。
- **特性 UNC**：470 特性；图片 2155；引用解析 20862 / 剥死链 4637（含子文档精确引用，如 `[[UNC@Feature@IPFD-010001-控制接口震荡特性]]`）。
- 抽样：`[[UDG@MMLCommand@SET UPGTPPATH]]`、`[[UDG@Feature@GWFD-010102-配置GTP_PFCP路径管理参数]]`（子文档精确命中）、`[[UNC@MMLCommand@DSP PORT]]`。

### 对已建资产的影响
- **三层资产均需重建**（已按 v0.13.0 重建：特性/命令/ConfigObject × UDG+UNC）。引用格式从相对路径切到 `[[ID]]`，旧相对路径引用全部失效需重建。

### 类型
- MINOR（引用格式变更 + 命令/ConfigObject 新增图片/引用处理；向后兼容新增，但已建资产需重建）

---

## [0.12.0] - 2026-07-17

### 变更（特性层图片纳入 + 文档引用改写/清理）
- **推翻 v0.10.0 的「图片不纳入」决策**：特性层资产现在**保留图片**。每特性文件夹下一个扁平 `assets/`，合并该特性全部源 md 旁的 `{md名}.assets/` 图片（按文件夹 hash 去重，同名异内容按源 slug 前缀消歧），md 里 `![]({旧名}.assets/x.png)` 改写为 `![](assets/x.png)`。
- **文档引用改写/清理**（特性 md 正文里的 `[文字](相对路径)`）：
  - **命令引用**（叶子名/标签含全角括号 `（CMD）` 或标签即命令名）→ 改写为到 `Command/{nf}/{ver}/{nf}@MMLCommand@{CMD}.md` 的相对路径；需命令资产已存在。
  - **特性引用**（叶子名含 `[A-Z]+FD-\d{6}`）→ 改写为到 `Feature/…/{nf}@Feature@{code}/概述.md` 的相对路径（v1 跳概述）。
  - **其余/不可解析**（PDF/外链/未建命令/分类码）→ **剥 URL 留文字**（`[文字](死链)` → `文字`）。
  - 外链 http/锚点/图片语法不动。
- 新增跨层约定 `conventions/资产图片与引用处理.md`（所有层共用；本次仅特性层落地，命令层/ConfigObject 后续照搬）。
- 实现：`feature/scripts/_common.py` 增 `build_command_index / build_feature_codes / extract_cmd_name / rewrite_images / rewrite_doc_refs`（纯标准库，URL 解析用 `_parse_link_url` 正确处理含空格路径）；`build_features.py` 在每特性文件夹建 `assets/`、按文档循环改写；manifest 增 `images_copied / doc_refs_resolved / doc_refs_stripped`。
- 文档同步：`SKILL.md`（图片纳入+输出+构建流程，sop_version 0.12.0）、`字段定义.md`（图片/引用均不进 YAML 注）、`check.md`（增图片闭环/引用闭环两项，原文完整行更新）。

### 为什么
- 源 md 旁有 `.assets/` 图片（全量 UDG 特性指南 431 目录/844 PNG）+ 正文相对路径文档引用，旧构建器只搬 md 文本 → **图片全丢、引用全成死链**。资产不自包含、引用不可跳。

### 自测（全量 UDG）
- 258 特性 / 865 文档（与 v0.10.0 一致，无回归）。
- **图片**：830 处引用对应图片拷入，落盘 797 张（去重后）；0 残留 `{旧名}.assets/` 旧路径；0 个 `.assets` 目录（全改扁平 `assets/`，178 个特性文件夹有图）。抽样 `GWFD-020401`：`![](assets/zh-cn_image_0226536218.png)` 指向实存 png。
- **引用**：解析 7867（命令 7227 + 特性 461 + 余量）/ 剥死链 1359；0 残留指向 output/ 的相对路径。抽样命令引用 `../../../../Command/UDG/20.15.2/UDG@MMLCommand@SET UPGTPPATH.md` 目标实存；PDF 等死链已剥成纯文字。
- 实现期修了一个关键 bug：URL 含空格（`UDG MML命令`、`GWFD-000101 支持…assets`）被 `split()[0]` 截断 → 改 `_parse_link_url` 按 `"` 标题切、保留空格，命令解析 33→7227、图片 437→830。

### 对已建资产的影响
- **Feature 侧需重建**（已按 v0.12.0 重建：图片+引用就位）。License 侧无图片/引用问题，不受影响。

### 类型
- MINOR（新增图片纳入 + 引用改写规则；向后兼容新增，但已建 Feature 资产需重建）

> 注：本版本与并行的 [0.11.0]（task 层 AtomTask 迁移）互不冲突——task 工作明确不动 command/feature 层；二者仅共享 VERSION/CHANGELOG，本条目置于其上。

---

## [0.12.0] - 2026-07-17

### 新增
- **task 层 AtomTask 资产构建（二期：UNC 全量迁移）**。基于 v0.11.0 已验证的迁移脚本:
  - 迁移脚本扩展支持 `--nf UNC` 参数（默认 `--nf UDG` 保持向后兼容）；模块级 `NF/VERSION` 通过 CLI 覆盖
  - UNC atom 资产特点: 280 个 atom（UDG 237 个），无 `nf:` 字段但 ref 同 UDG 格式 (`UNC@20.15.2@MMLCommand@...`)；命令行分布 ADD 154 / SET 73 / MOD 27 / RMV 13 / DSP 9 / 其他 4
  - 共建产出：`三层图谱资产/AtomTask/UNC/20.15.2/UNC@AtomTask@{COMMAND}.md`（**280 个**）

### 自测
- UDG 237/237 + UNC 280/280 = **517/517** 全通过 ad-hoc 验证（`hermes-verify-migrate.py`，含 YAML 8 字段 / id 三段式 / ## 边 单行 / 禁词零命中 / 业务内容保留 / 关键转换点）
- 业务正文总量 1,509,997 字符 / 40,372 行（UDG 711k / UNC 799k，平均 2,920 字/篇）
- ad-hoc 验证脚本支持 `--nf UDG|UNC` 自适应（cmdmap 数量、期望命令、关键转换点都按 NF 分流）

### 修复
- **破损 markdown 链接保护**: UNC 0-00164 源文件含破损 markdown `[ADD CHGTARI](task/UNC/20.15**（warning，rule-0-03168）`（粗体闭合符截断），迁移脚本 MD_LINK_RE 收紧为 `[^)\s*][^)\s]*`（拒绝目标含 `*`），不误吃破损链接，原样保留
- **DP 编号语义改写 `（DP 0-NNNNN，xxx）` 形式**: 之前 regex 只匹配纯 `(DP 0-NNNNN)`，遇到带 ",xxx" 的形式残留 `（，xxx）`。扩展为 `(DP 0-NNNNN，xxx)` -> `(决策点，xxx)`
- **code block 保护机制**: 之前 strip 函数可能误吃 ``` 围栏代码块和行内代码里的字符。新增 `_protect_code_blocks` / `_restore_code_blocks`，所有 strip 在 code block 保护上下文跑、最后还原
- **strip_dp_inline_refs 顺序**: 之前 `replace_bare_atom_refs` 在 `strip_dp_inline_refs` 之前跑，把 `DP 0-00019` 提前吃成 `DP [[UDG@AtomTask@SET LICENSESWITCH]]`，导致 9 条 DP 编号语义改写模板全部失效。调成 `strip_dp_inline_refs` **先于** `replace_bare_atom_refs`
- **尖括号 `0-XXXXX` 引用**: 新增 `<0-00215 产出>` 形式识别（IPSECINTFCFG 围栏外 `//` 注释行），strip_paren_atom_num 加 #4 刀

### 为什么
- 用户要求"UNC 也要一并处理下，UNC 的命令级别的 task"。UNC 与 UDG 是同构资产（YAML/H1/## 配置方法/## 决策点/## 约束/## 关联 一致），可直接复用 v0.11.0 迁移脚本，扩展 `--nf` CLI 参数即可支持

### 影响文件
- 改 `task/scripts/migrate_old_atoms.py`（加 argparse、加 _protect_code_blocks、5 类 regex 修复）
- 新增 `三层图谱资产/AtomTask/UNC/20.15.2/UNC@AtomTask@{COMMAND}.md`（**280 个**）

### 对已建资产的影响
- **task 层资产** — UDG 237 个 + UNC 280 个 AtomTask 全建
- **command/feature 层** — 无影响
- 旧的 `assets/task/UNC/20.15.2/0-XXXXX.md` 由迁移指南 §0 明确"只迁格式不删源"，保留为可追溯的旧版本

### 类型
- MINOR（task 层资产新增；向后兼容；v0.11.0 UDG 产物不动）

---

## [0.11.0] - 2026-07-17

### 新增
- **task 层 AtomTask 资产构建（一期：旧 atom 全量迁移）**。按 [task/迁移指南-旧atom到AtomTask.md](task/迁移指南-旧atom到AtomTask.md) 执行：
  - 新增 `task/scripts/migrate_old_atoms.py`（一次性迁移脚本；纯标准库；237 个 atom 一次性批处理）
  - 产出：`三层图谱资产/AtomTask/UDG/20.15.2/UDG@AtomTask@{COMMAND}.md`（**237 个**，与旧 atom 一对一）
  - YAML 8 字段：`id`/`type`/`name`/`name_zh`/`nf`/`version`/`ref`/`status`，id 三段式 `{nf}@AtomTask@{命令}`（无 version/无编号），ref 三段式 `{nf}@MMLCommand@{命令}`
  - 文件名 = 完整 ID；命令名含空格时保留（如 `UDG@AtomTask@LST POOL.md` / `UDG@AtomTask@EXP MML.md`）
  - 业务正文原样保留（只改格式不改内容）；删除证据/配置对象链接/Task↔Task/被引用于；保留并转译命令层 markdown 链接为 `[[{nf}@MMLCommand@{cmd}]]`；旧四段式 wiki 占位剥 `20.15.2@` 段、按 Type 分流
  - ## 边 段统一为 `- 对应命令: [[{nf}@MMLCommand@{命令}]]` 单行

### 自测
- 237 个 atom 全部通过 §6 校验清单：YAML 8 字段齐全且顺序正确 / id 三段式无 version 无编号 / ref 三段式 / name=name_zh / 文件名=ID / ## 边 只有对应命令一行 / 全部禁词零命中（`0-XXXXX`/`rule-0-`/`DP 0-`/`configobject/`/`evidence/`/`(command/`/`(task/`/`@20.15.2@`/YAML 旧字段 `task_layer`/`task_intent`/`task_logical_name`/`source_evidence`/`****`/空括号）
- 业务正文总量 667,466 字符 / 16,091 行（平均 2,816 字/篇）；命令行分布 ADD 147 / SET 72 / LST 5 / MOD 5 / DSP 3 / LOD 3 / EXP 1 / STR 1
- 命令名从每个旧 `0-XXXXX.md` YAML 的 `ref` 字段末段现场读取（不依赖附录 A 静态表，单源可信）

### 边界 case 处理（指南未明文，遇到后沉淀到脚本）
- 全角/半角括号 + 全角/半角逗号都要吃 `rule-0-XXXXX`
- `（warning，rule-0-00110 同族）` / `（critical，rule-0-00443，命令 notes）` 等多级来源标记一并删
- `**rule-0-00178-impl**` 单独成粗体标题时删（仅 0-00214 出现 1 次）
- 正文裸 `0-XXXXX` 不在 markdown 链接/wiki 占位/括号里 → 转 `[[UDG@AtomTask@{cmd}]]`（如 `License 0-00019` / `须 0-00144 先生效` / `引用 0-00215 产出`）
- 括号里 `0-XXXXX.XXX` / `0-XXXXX:XXX`（编号+点/冒号+参数引用形式）→ 删编号段
- `§0-XXXXX` / `feature-rule 0-XXXXX` / `selection_rule 0-XXXXX` 引用 → 删
- 旧 wiki4 占位单层方括号变体 `[UDG@20.15.2@DecisionPoint@0-XXXXX]`（CONTCATE 系列）→ 按 Type 分流
- `0-00XXX.md` 链接（未建对象的占位符）→ 用显示文字做命令名
- `command-evidence/0-XXXXX` 自引用（仅 NTPSVR）→ 整段删
- DP 编号 `DP 0-XXXXX` 正文出现按语义改写：`另存演进` → `另存一个演进决策`；`仅在 ... 标注` → `仅在决策点标注`；`决策点驱动` / `由决策点编排` / `见决策点` 等
- 占位删除后残留的双重粗体 `****` 兜底清理

### 为什么
- 旧 atom (237 个 `0-XXXXX.md`) 用了旧 ID 体系（`UDG@20.15.2@Task@0-XXXXX`），不符合 task 层新 SOP（id 用命令名做锚，三段式）；同时引用形式 / 关联段结构 / 证据字段等都需按新规范重构。本次只迁 atom (1:1)，compound (1-) / feature_task (2-) 留待后续批次

### 影响文件
- 新增 `task/scripts/migrate_old_atoms.py`（一次性脚本，~400 行）
- 新增 `task/迁移指南-旧atom到AtomTask.md`（迁移 SOP 文档）
- 新增 `三层图谱资产/AtomTask/UDG/20.15.2/UDG@AtomTask@{COMMAND}.md`（**237 个**）

### 对已建资产的影响
- **task 层资产** — 全新产出，旧 atom 不动（保留在 `assets/task/UDG/20.15.2/0-XXXXX.md` 作历史档案）；atom 阶段闭环完成
- **command/feature 层** — 无影响
- 旧的 `assets/task/UDG/20.15.2/0-XXXXX.md` 由迁移指南 §0 明确"只迁格式不删源"，保留为可追溯的旧版本

### 待用户确认（不影响本批）
- `三层图谱资产/AtomTask/UDG/20.15.2/` 当前 git 仍 ignore（沿用 `三层图谱资产/` 的全局 ignore）。是否要为 `AtomTask/` 单独放行？详见迁移指南 §9

### 类型
- MINOR（task 层资产新增；向后兼容；旧 atom 资产保留）

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
