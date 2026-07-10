# 业务层 Wiki 构建 Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.
>
> **项目性质**：这是**知识 wiki 项目**（markdown 对象，非代码）。TDD 步骤适配为「读源 → 写 md → grep 验证 → 提交」；"测试"= 链接/模板/双向回填的 grep 校验 + R1 审视。无单元测试。

**Goal:** 在 `assets/` 内构建业务层 typed wiki——业务域(BD)→场景(NS)→方案(CS) 三类对象 + 配套构建 SOP + 审视流程，并以计费场景（融合计费 CS 为范本）落地 9 个对象。

**Architecture:** 业务层 = 纯树（BD→NS→CS），CS 向下引用已有 `task/{nf}/{ver}/` 的 feature/compound/atom task。不建 `3-` solution task 对象，CS 本身承载"是什么"+"怎么配"。叙述式模板（镜像 feature task），三层结构差异化（配置流程只在 CS，决策点/约束任意层可选）。硬前置门：CS 涉及 feature task 须先建完（计费场景已通过：UDG 9/9 + UNC 5/5）。

**Tech Stack:** Markdown typed wiki + YAML front matter + grep 验证 + git。镜像 `assets/task/特性步骤级构建SOP.md` 的范式。

**Spec:** `docs/superpowers/specs/2026-07-10-business-layer-sop-design.md`（已基线 `f665ed098`）

**硬约束（全程遵守）**：
- 可写仅 `assets/`；只读 `output/`、`ConfigTask/`、`FeatureGraph/`、`业务图谱体系/`。
- 直提 master，不开分支；commit message **无** Co-Authored-By（归属全局禁用）。
- 最多 2 个并行 Agent；并行 Agent **绝不碰共享文件**（`assets/business/index.md`、`assets/task/*/index.md`、已有 task 的"被引用于"段）——只建自己的对象 md + 拷证据，主流程串行回填。
- activation/方案主源 = 原始产品文档章节（业务专题/方案），非凝练版图谱 md（后者仅参考）。

---

## File Structure

### 新建（工具层）
- `assets/task/业务层级构建SOP.md` — 业务层构建 SOP（镜像特性 SOP §0-§8，内容来自 spec §0-§8）
- `assets/task/业务层级wiki审视流程.md` — 业务层审视流程（来自 spec §10）

### 新建（业务层对象，9 个）
- `assets/business/index.md` — 业务层全景 index
- `assets/business/business-awareness/BusinessDomain@business-awareness.md` — BD 业务感知
- `assets/business/business-awareness/charging/NetworkScenario@charging.md` — NS 计费
- `assets/business/business-awareness/charging/ConfigurationSolution@charging-converged.md` — CS-3 融合（★范本，先建）
- `assets/business/business-awareness/charging/ConfigurationSolution@charging-online.md` — CS-2 在线
- `assets/business/business-awareness/charging/ConfigurationSolution@charging-offline.md` — CS-1 离线
- `assets/business/business-awareness/charging/ConfigurationSolution@charging-content.md` — CS-4 内容基础
- `assets/business/business-awareness/charging/ConfigurationSolution@charging-metering.md` — CS-5 计量增强
- `assets/business/business-awareness/charging/ConfigurationSolution@charging-quota-exhaust.md` — CS-6 配额降速
- `assets/business/business-awareness/charging/ConfigurationSolution@charging-fallback.md` — CS-7 兜底

### 新建（证据）
- `assets/evidence/business/charging/*.md` — 计费方案/业务专题原始 md 拷贝（自包含）

### 修改（回填/约定）
- `assets/task/UDG/20.15.2/{被引用的task}.md` + `assets/task/UNC/20.15.2/{被引用的task}.md` — 各 task md 的 `## 关联` → `- 被引用于:` 行追加本 CS 引用。**回填目标是 per-task-md，不是 index.md**（index.md 的 compound 复用库"用于:"是 feature 级摘要，可选同步但不强制）。由主流程做，非并行 Agent。
- `assets/business/index.md` — 标 CS done（去占位）
- `assets/CLAUDE.md` — §5.5/§9 补业务层目录约定（`assets/business/`，两段式 ID）
- `assets/log.md` — append ingest 记录

---

## 构建模式（镜像特性层）

- **并行 Agent（最多 2）**：每个 Agent 建自己的 CS md + 拷证据，**绝对不碰共享文件**；输出报告（引用的 task + 缺口 + 证据），主流程串行汇总回填 index/被引用于。
- **族内顺序**：先建最复杂的 **CS-3 融合**（跨网元 UDG+UNC、双 URR、CHF 协同最全），把跨网元协同知识 + 复用 compound 场景差异一次沉淀到位；再建简单 CS 复用。
- **每批后自审**：按 `assets/task/业务层级wiki审视流程.md` R1 审视，critical 即修，经验回填 SOP。

---

## Chunk 1: 工具层（SOP + 审视流程 + index 骨架 + CLAUDE.md 约定）

### Task 1.1: 写业务层构建 SOP

**Files:**
- Create: `assets/task/业务层级构建SOP.md`

**内容来源**：spec §0-§8（已基线）。把 spec 的 §0-§8 落地为 SOP 文件，结构镜像 `assets/task/特性步骤级构建SOP.md`（§0 产物层级/§1 编号/§2 单方案流程/§3 复用/§4 模板/§5 DP/§6 硬约束/§7 验收/§8 铺开+自审）。开头痛点参考特性 SOP 顶注（作用/镜像/范本/配套）。

- [ ] **Step 1: 读 spec §0-§8 + 特性 SOP 定结构**

读 `docs/superpowers/specs/2026-07-10-business-layer-sop-design.md` §0-§8 + `assets/task/特性步骤级构建SOP.md`（结构模板）。

- [ ] **Step 2: 写 SOP md**

落地 8 段，标题 `# 业务层 Wiki 构建 SOP（核心准则）`。关键内容（直接取自 spec）：
- §0 产物层级表（BD/NS/CS + 回答的问题 + ref）
- §1 编号（两段式 ID §5.2 + 目录 `assets/business/<domain>/<scenario>/`）
- §2 单方案构建流程（含前置门）
- §3 复用机制（镜像特性 §3，含复用差异双向回填）
- §4 三层差异化模板（BD/NS/CS，配置流程只在 CS，决策点/约束任意层可选）
- §5 决策点规范（DP 任意层，统一 `|选项/场景|影响|`）
- §6 硬约束（前置门/额外步骤进 task/叙述式非填表/证据自包含/双向链接/跨网元全路径）
- §7 验收清单
- §8 铺开范围 + 族内顺序（先建融合）+ 每批自审

- [ ] **Step 3: 验证**

Run: `grep -n "^## " assets/task/业务层级构建SOP.md`
Expected: 8 段标题（§0-§8）齐全。
Run: `grep -c "业务" assets/task/业务层级构建SOP.md`（非空）

- [ ] **Step 4: Commit**

```bash
git add assets/task/业务层级构建SOP.md
git commit -m "docs(task): 业务层构建SOP——BD/NS/CS树+叙述式模板+前置门(镜像特性SOP)"
```

### Task 1.2: 写业务层审视流程

**Files:**
- Create: `assets/task/业务层级wiki审视流程.md`

**内容来源**：spec §10。

- [ ] **Step 1: 写审视流程 md**

标题 `# 业务层 Wiki 审视流程（R1）`。R1 五维度（来自 spec §10）：
- R1.1 task 覆盖度（方案应编排的 task 都引用？额外步骤建 atom/compound 非空写？）
- R1.2 复用合理性（compound 真覆盖？跨网元差异回填？假复用？）
- R1.3 跨网元协同完整性（UDG 用户面 + UNC 控制面协同表达清？）
- R1.4 前置门（涉及 feature task 真建完非占位？）
- R1.5 证据链（命令/参数可追溯；无证据结论穷尽搜索再判 critical）
- R2 辅助 / R3 输出格式 / R4 严重度

- [ ] **Step 2: 验证**

Run: `grep -n "^### R1" assets/task/业务层级wiki审视流程.md`
Expected: R1.1-R1.5 五条。

- [ ] **Step 3: Commit**

```bash
git add assets/task/业务层级wiki审视流程.md
git commit -m "docs(task): 业务层wiki审视流程R1——task覆盖/复用/跨网元协同/前置门/证据链"
```

### Task 1.3: 建 index 骨架 + CLAUDE.md 约定

**Files:**
- Create: `assets/business/index.md`
- Modify: `assets/CLAUDE.md`（§5.5 或 §9 补业务层目录约定）

- [ ] **Step 1: 建 business/index.md 骨架**

```markdown
# index · business（业务层）

## 业务域（BD）
- [业务感知](business/business-awareness/BusinessDomain@business-awareness.md) — 对用户报文解析区分业务，实现策略/计费控制

## 场景（NS）
### 业务感知
- [计费](business/business-awareness/charging/NetworkScenario@charging.md) — 按业务差异化计费（离线/在线/融合）

## 方案（CS）
### 计费
- [融合计费](business/business-awareness/charging/ConfigurationSolution@charging-converged.md) — Nchf统一接口，双URR(offline+online)+RGAPPLIED
（其余 CS 待建占位 [[charging-online]] 等）
```

- [ ] **Step 2: CLAUDE.md 补业务层约定**

在 §5.5（文件名与引用路径）或 §9（边界）补一条：业务层对象（BD/NS/CS）住 `assets/business/<domain>/<scenario>/`，两段式 ID（§5.2，不带 nf@version），一个 md 一个对象；CS 引用下层 task 用 assets 根路径跨网元全路径。

- [ ] **Step 3: 验证**

Run: `ls assets/business/index.md`（存在）

- [ ] **Step 4: Commit**

```bash
git add assets/business/index.md assets/CLAUDE.md
git commit -m "docs(assets): 业务层index骨架+CLAUDE.md业务层目录约定"
```

---

## Chunk 2: 范本（BD + NS + CS-3 融合）—— ★ SOP 验证门

> 本 Chunk 建出第一个完整 CS（融合），验证 SOP 是否可产出合格对象。范本通过后才能并行铺其余 CS。

### Task 2.1: 建 BD（业务感知）

**Files:**
- Create: `assets/business/business-awareness/BusinessDomain@business-awareness.md`

**源**（参考，非拷）：
- `业务图谱体系/计费场景/three-layer-graph/01-business-graph.md` §1.1（BD-CH-01 业务感知定义）
- `业务图谱体系/三层图谱本体标准定义.md`（业务感知域定义）

- [ ] **Step 1: 读源**（BD 定义/价值/含哪些场景）

- [ ] **Step 2: 写 BD md**（BD 模板：概览/范围与边界/关联）

front matter: `id: BusinessDomain@business-awareness` / `type: BusinessDomain` / `name: 业务感知` / `status: draft` / `source_evidence_ids`。
正文：业务感知域定义 + 含场景（计费/带宽控制/访问限制，链接 NS）+ 不属于本域。

- [ ] **Step 3: 验证**

Run: `grep -n "^## " assets/business/business-awareness/BusinessDomain@business-awareness.md`
Expected: 概览 / 范围与边界 / 关联（决策点/约束可选，BD 罕见可略）。

- [ ] **Step 4: Commit**

```bash
git add assets/business/business-awareness/BusinessDomain@business-awareness.md
git commit -m "feat(business): BD业务感知——业务层首个对象(定义/范围/关联)"
```

### Task 2.2: 建 NS（计费）

**Files:**
- Create: `assets/business/business-awareness/charging/NetworkScenario@charging.md`

**源**：
- `业务图谱体系/计费场景/three-layer-graph/01-business-graph.md` §1.2（NS-CH-01 计费场景 + 边界）
- `业务图谱体系/计费场景/charging-doc-list/batch-03-计费专题.md`（计费专题主源定位）

- [ ] **Step 1: 读源**（场景定义/判断依据/典型产出/边界/方案选择）

- [ ] **Step 2: 写 NS md**（NS 模板：概览/边界/决策点/关联）

决策点段记场景级方案路由（计费方式→离线/在线/融合→对应 CS）。关联段含上游 BD + 下游 7 CS 链接（未建 `[[占位]]`）。

- [ ] **Step 3: 验证**

Run: `grep -n "^## " assets/business/business-awareness/charging/NetworkScenario@charging.md`
Expected: 概览 / 边界 / 决策点 / 关联。

- [ ] **Step 4: Commit**

```bash
git add assets/business/business-awareness/charging/NetworkScenario@charging.md
git commit -m "feat(business): NS计费场景——定义/边界/方案选择决策点"
```

### Task 2.3: 拷证据

**Files:**
- Create: `assets/evidence/business/charging/*.md`

- [ ] **Step 1: 定位 + 拷融合计费相关原始 md**

定位规则：`业务图谱体系/计费场景/charging-doc-list/batch-03-计费专题.md` 列出计费专题 md，文件头有 `路径前缀: UNC/网络部署/业务专题/5G Core 计费解决方案/` + 各条相对文件名。on-disk 解析：`output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core 计费解决方案/{相对文件名}`（路径前缀开头的 `UNC/` 是产品标签，output 根目录已表 UNC，实际子路径从 `网络部署/` 起；用 `ls` 验证存在）。
查 batch-03 找融合计费方案/计费原理相关 md，拷贝到 `assets/evidence/business/charging/`，命名 `{描述名}_{原始ID}.md`。UDG 侧融合计费 feature 的 activation 证据已在 `assets/evidence/UDG/20.15.2/`（无需重拷，CS 引用即可）。

- [ ] **Step 2: 验证**

Run: `ls assets/evidence/business/charging/`（非空）

- [ ] **Step 3: Commit**

```bash
git add assets/evidence/business/charging/
git commit -m "feat(evidence): 计费方案原始文档拷贝(自包含)"
```

### Task 2.4: 建 CS-3 融合计费（★范本）

**Files:**
- Create: `assets/business/business-awareness/charging/ConfigurationSolution@charging-converged.md`

**源**（主源 = 原始产品文档；参考 = 业务图谱体系）：
- 主源：`output/` 下融合计费方案/业务专题 md（Task 2.3 已拷贝到 evidence）
- 参考：`业务图谱体系/计费场景/three-layer-graph/01-business-graph.md` §2.3（CS-CH-03 融合）+ §10.3（融合端到端流程）
- 参考：`业务图谱体系/计费场景/feature-knowledge/GWFD-010173-融合计费.md` + `WSFD-011206-融合计费.md`
- 下层 task（必读，确认命令集 + 场景差异）：
  - UDG: `assets/task/UDG/20.15.2/2-00006.md`（融合计费 feature task）+ `1-00010.md`（计费三件套）+ `1-00009.md`（过滤链）+ `1-00011.md`（规则绑定）+ `1-00012.md`（计费收尾）
  - UNC: `assets/task/UNC/20.15.2/2-00003.md`（融合计费）+ `1-00005.md`（CCT 模板）+ `1-00007.md`（CHF 选择）+ `1-00008.md`（SMF-CHF Trigger）+ `1-00009.md`（费率标识链）

- [ ] **Step 1: 前置门核验**

Run: 确认 UDG 2-00006 + UNC 2-00003 存在且无 `[[占位]]`。
```bash
ls assets/task/UDG/20.15.2/2-00006.md assets/task/UNC/20.15.2/2-00003.md
grep -c "\[\[" assets/task/UDG/20.15.2/2-00006.md assets/task/UNC/20.15.2/2-00003.md
```
Expected: 两文件存在；`[[` 计数为 0（或仅明确待建）。

- [ ] **Step 2: 读源 + 下层 task**（理解融合方案：跨网元协同 UDG 用户面 URR 双URR + UNC 控制面 Nchf/CCT/CHF；RGAPPLIED 约束；端到端流程）

- [ ] **Step 3: 设计 CS 编排**

方案编排哪些 feature task + compound + atom + 方案特有额外步骤。融合方案特有额外步骤（跨网元协同的、不属于任何特性的命令）→ 单命令建 atom、多命令建 compound（进 `task/`，CS 引用）。先查 `assets/task/UDG|UNC/20.15.2/index.md` compound 复用库，能复用不新建。

- [ ] **Step 4: 写 CS md**（CS 模板：概览/配置与协同/决策点/约束/关联）

front matter: `id: ConfigurationSolution@charging-converged` / `type: ConfigurationSolution` / `domain: business-awareness` / `scenario: charging` / `status: draft` / `source_evidence_ids: [EV-BIZ-charging-01]`。
- 概览：融合方案是什么 + 跨网元协同骨架（UDG 用户面双URR / UNC 控制面 Nchf+CCT+CHF）
- 配置与协同：每步"干啥 + 引用哪个 task"（UDG 侧 2-00006/1-00010/1-00011/1-00012 + UNC 侧 2-00003/1-00005/1-00007/1-00008 + 跨网元顺序）
- 决策点：配置级 DP（如 RGAPPLIED 约束、双 URR 在线/离线分配、CCT 模板选择）
- 约束：跨网元 URRID 一致性、RGAPPLIED 强约束、License 前置、REFRESHSRV 时序（severity 标注）
- 关联：上游 NS + 下游 task（带命令提示）+ 证据

- [ ] **Step 5: 验证**

Run: `grep -n "^## " assets/business/business-awareness/charging/ConfigurationSolution@charging-converged.md`
Expected: 概览 / 配置与协同 / 决策点 / 约束 / 关联。
Run: `grep -c "\[\[" assets/business/business-awareness/charging/ConfigurationSolution@charging-converged.md`
Expected: 0（feature task 全建完，无占位；evidence 已拷贝）。
Run: `grep -c "task/UDG/20.15.2/\|task/UNC/20.15.2/" assets/business/business-awareness/charging/ConfigurationSolution@charging-converged.md`
Expected: ≥6（融合 CS 应引 9 个 task：UDG 5 + UNC 5，去重后 ≥6；低于此说明漏引一侧）。

- [ ] **Step 6: Commit**

```bash
git add assets/business/business-awareness/charging/ConfigurationSolution@charging-converged.md
git commit -m "feat(business): CS融合计费范本——跨网元协同(UDG双URR+UNC Nchf/CCT/CHF)+RGAPPLIED约束"
```

### Task 2.5: 双向回填 + index 更新

**Files:**
- Modify: 被融合 CS 引用的各 task md 的 `## 关联` → `- 被引用于:` 行（**per-task-md，非 index.md**）：
  - UDG: `2-00006.md`、`1-00010.md`、`1-00009.md`、`1-00011.md`、`1-00012.md`
  - UNC: `2-00003.md`、`1-00005.md`、`1-00007.md`、`1-00008.md`、`1-00009.md`
- Modify: `assets/business/index.md`（融合 CS 去占位标 done）

- [ ] **Step 1: 回填 per-task-md "被引用于"**（主流程做，非并行 Agent）

在上述每个 task md 的 `- 被引用于:` 行末追加 `、[融合计费](business/business-awareness/charging/ConfigurationSolution@charging-converged.md)`。现有"被引用于"列的是 feature task（2-），CS 是业务层消费者，追加即可（混列 OK，语义=谁引用我）。

- [ ] **Step 2: 更新 business/index.md**（融合 CS 标 done，去 `[[占位]]`）

- [ ] **Step 3: 验证双向链接**

Run: `grep -rl "charging-converged" assets/task/UDG/20.15.2/ assets/task/UNC/20.15.2/`
Expected: ≥5 个 task md 命中（被引用的 task 侧有回链）。

- [ ] **Step 4: Commit**

```bash
git add assets/task/UDG/20.15.2/2-00006.md assets/task/UDG/20.15.2/1-00010.md assets/task/UDG/20.15.2/1-00009.md assets/task/UDG/20.15.2/1-00011.md assets/task/UDG/20.15.2/1-00012.md assets/task/UNC/20.15.2/2-00003.md assets/task/UNC/20.15.2/1-00005.md assets/task/UNC/20.15.2/1-00007.md assets/task/UNC/20.15.2/1-00008.md assets/task/UNC/20.15.2/1-00009.md assets/business/index.md
git commit -m "feat(business): 融合CS双向回填——per-task-md被引用于+business/index更新"
```

### Task 2.6: 范本自审（R1）—— ★ SOP 验证门

- [ ] **Step 1: 按 `assets/task/业务层级wiki审视流程.md` R1 审视融合 CS**

逐维度：R1.1 task 覆盖 / R1.2 复用合理性 / R1.3 跨网元协同完整性 / R1.4 前置门 / R1.5 证据链。无证据结论先穷尽搜索再判 critical。

- [ ] **Step 2: 修 critical/warning**

- [ ] **Step 3: 沉淀经验**

若 SOP 有缺陷 → 修 `assets/task/业务层级构建SOP.md` + 版本号 +1。

- [ ] **Step 4: Commit（如有修订）**

```bash
git add -A
git commit -m "fix(business): 融合CS范本R1审视修复+SOP经验回填"
```

> **门**：范本通过 R1（无未修 critical）→ 进入 Chunk 3 并行铺其余 CS。否则迭代修到通过。

---

## Chunk 3: 其余 6 CS + 族级审视 + 收尾

> 范本通过后，6 CS 可并行（最多 2 Agent）。每个 Agent 建自己的 CS md + 拷证据，**不碰共享文件**，主流程串行回填。

### Task 3.1: 建 CS-1 离线 / CS-2 在线 / CS-4 内容基础 / CS-5 计量 / CS-6 配额降速 / CS-7 兜底

**Files:**
- Create: 6 个 `ConfigurationSolution@charging-{offline,online,content,metering,quota-exhaust,fallback}.md`

每个 CS 的下层 task 引用（来自 spec §9.2 表）：
- CS-1 离线: UDG 2-00005+2-00003, UNC 2-00001
- CS-2 在线: UDG 2-00004+2-00003+2-00009
- CS-4 内容基础: UDG 2-00019(SA)+2-00003+2-00018(PCC), UNC 2-00005+2-00004
- CS-5 计量增强: UDG 2-00003+2-00007+2-00008+2-00009
- CS-6 配额降速: UDG 2-00004+2-00006, UNC 2-00003
- CS-7 兜底: UDG 2-00003+2-00018

**源**（每个 CS）：
- 主源：`output/` 下对应方案/业务专题 md（拷到 `assets/evidence/business/charging/`）
- 参考：`业务图谱体系/计费场景/three-layer-graph/01-business-graph.md` §2 对应 CS + §10 端到端流程
- 参考：`业务图谱体系/计费场景/feature-knowledge/cross-feature-analysis.md`（跨特性归纳）
- 下层 task：上表对应 feature task + compound（读确认命令集 + 场景差异）

每个 CS 重复 Task 2.4 的 Step 1-6（前置门 → 读源 → 设计编排 → 写 md → grep 验证 → commit）。

- [ ] **Step 1: 6 CS 逐个建（并行 ≤2，分批 3 轮）**

每批 2 个 CS 并行 Agent；Agent 输出报告（引用 task + 缺口 + 证据），不碰 index/被引用于。

- [ ] **Step 2: 主流程串行回填**（每批后，**非并行 Agent**）

回填该批 CS 引用的各 task md 的 `## 关联` → `- 被引用于:` 行（追加 CS 引用，格式同 Task 2.5；**目标是 per-task-md，不是 index.md**）+ `assets/business/index.md` 标 done。

- [ ] **Step 3: 每批 Commit**

```bash
git add assets/business/business-awareness/charging/ConfigurationSolution@charging-{x}.md assets/evidence/business/charging/
git commit -m "feat(business): CS{离线/在线/...}——编排+跨网元协同+证据"
```

### Task 3.2: 族级审视（R1）

- [ ] **Step 1: 对 7 CS 整体做 R1 族级审视**

重点：复用合理性（7 CS 复用 1-00010 计费三件套等，差异是否回填防假通用——镜像特性层计费族教训）、跨网元协同完整性、前置门、证据链。共性问题沉淀。

- [ ] **Step 2: 修 critical/warning + 经验回填 SOP**

- [ ] **Step 3: Commit**

```bash
git add -A
git commit -m "fix(business): 计费族7CS族级R1审视修复+SOP经验回填"
```

### Task 3.3: 全量 lint + log 收尾

**Files:**
- Modify: `assets/log.md`

- [ ] **Step 1: 全量 lint**

```bash
# 无 [[占位]] 残留（全部 CS 建完后应为 0）
grep -rn "\[\[" assets/business/
# 双向链接闭环：每个被引用的 task 在 assets/task/ 有"被引用于"回链
grep -rl "ConfigurationSolution@charging" assets/task/
# 模板段齐全：每个 CS 必含 配置与协同/决策点/约束
grep -L "## 配置与协同" assets/business/business-awareness/charging/ConfigurationSolution@*.md
grep -L "## 决策点" assets/business/business-awareness/charging/ConfigurationSolution@*.md
grep -L "## 约束" assets/business/business-awareness/charging/ConfigurationSolution@*.md
```
Expected: `[[` 计数 0（全部 CS 建完）；task 侧回链 ≥ 每个 CS 引用的 task 数；三个 `grep -L` 无输出（所有 CS 都含这三段）。注：Chunk 3 进行中 `[[` 会非零（未建 CS 占位），仅最终为 0。

- [ ] **Step 2: log.md append**

```markdown
## [2026-07-10] ingest | 业务层计费场景
- BD 业务感知 / NS 计费 / 7 CS（融合范本+离线/在线/内容/计量/配额降速/兜底）
- 证据拷入 assets/evidence/business/charging/
- 双向回填 UDG/UNC task 侧"被引用于"
```

- [ ] **Step 3: 最终 Commit**

```bash
git add assets/log.md
git commit -m "chore(assets): 业务层计费场景全量lint+log收尾(9对象)"
```

---

## 执行交接

Plan complete and saved to `docs/superpowers/plans/2026-07-10-business-layer-sop-build.md`.

**执行路径**（本 harness 有 subagents）：
- REQUIRED: 用 superpowers:subagent-driven-development 执行本计划
- Chunk 1（工具层）串行快速过；Chunk 2（范本）串行 + R1 验证门；Chunk 3（6 CS）并行 ≤2 Agent + 串行回填
- 每个 task 产出 self-contained 变更 + commit

**范本门**：Chunk 2 的 Task 2.6（融合 CS R1 自审）是 SOP 验证门——通过后再并行铺 Chunk 3。未通过则迭代修 SOP/范本到通过。
