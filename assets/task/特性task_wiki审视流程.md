# 特性 task wiki 审视流程（R1）

> 目的：对已建 feature task wiki 做**独立批判性审视**，补构建者自检（SOP §7）的盲区。
> 核心关切：**激活案例是否真覆盖**、**复用是否抹平特性差异**、**步骤拆分是否合理**。
> 适用：每完成一族特性（或一批）后执行；构建者自检 ≠ 审视（自检问"建全了吗"，审视问"复用过度吗/覆盖真实吗/拆分对吗"）。
> 配套：`特性步骤级构建SOP.md`（§3复用/§3.5存在前提/§7验收）。

---

## R1 核心审视三维度（必做）

### R1.1 激活案例覆盖度（最高优先）
**防遗漏**——原始文档每一步都要有着落。

对每个 feature：
1. 读原始 activation 文档「操作步骤 / 配置流程 / 数据规划」**全部步骤**（每个"第N步"、每条 ADD/SET 命令、每个数据规划表行）。
2. 读 feature「配置流程」步骤。
3. **逐步骤核对**：原始步骤 i → feature 是否有对应？
   - ✓ 覆盖（直接步骤 或 并入某 compound 且该 compound 命令集真包含所需命令）
   - ✗ 遗漏（原始有、feature 无）
   - ⚠ 语义偏离（有对应步骤但参数/命令/顺序与原始不一致）
4. 复用 compound 时，**必须打开该 compound 确认其命令集真的包含这一步需要的命令**——不能假设"复用了就覆盖了"。

> 典型盲区：原始文档有 13 步，feature 编排了 6 步（复用 backbone），中间的"全局缺省URR组/防欺诈列表/特殊参数"等步骤被默认并入收尾compound，但收尾compound的命令集未必含 → 静默遗漏。

> **activation 空缺/无独立 activation 子规则**：部分特性 activation 主文档空（如 SA-Basic 根索引仅标题）或仅有概述（如 SA特征库更新/会话级 FUP）。此时 feature 命令序列来自参考信息 MML 清单 + 特性知识，审视须：① 核实 feature 脚注声称的命令源（参考信息/特性知识/实现原理）**原文是否在 evidence/ 提供**——未提供 → warning（证据链不完整，待补 evidence）；② 区分"能力型特性"（License 门控 + 复用 backbone，如 SA特征库更新/会话级 FUP，2 步合理）vs "配置型特性"（有完整 activation），勿要求能力型特性配齐命令。

### R1.2 复用合理性
**防一刀切**——复用不能抹平特性差异。

对 feature 复用的每个 compound：
1. compound 命令集是否真覆盖 feature 这步所需**全部命令**？（Jaccard ≥ 0.75 且相位同义，SOP §3.2）
2. feature 的**特性差异**（参数增量 / 专属命令 / 配置变种）是否进了：
   - feature 的 DP 影响表（必全），**且**
   - compound 的「场景差异」小节（若该差异是该步骤的阶段级选择）？
3. 有无**假复用**？命令集重合 < 0.75 或相位不同却强行复用 → 特性专属命令丢失、或被塞进不相关 compound。
4. **假通用判定（critical，必查）**：逐 feature 核对——该 feature 有的核心差异维度（参数变种/专属命令/约束/组装方式），compound「场景差异」是否有对应条目？若 **feature 有差异而 compound 场景差异无** → compound 对该 feature 是**假通用**（命令集覆盖但差异抹平）。**复用时必须把差异双向回填到 compound 场景差异，不能只写进 feature DP**（SOP §3.5 强制）。

> 典型盲区（计费族实战）：7 个计费特性都复用 1-00010 计费三件套，但融合的"双 URR + RGAPPLIED 约束"、离线的"OFFMETERINGTYPE 8 种"、时长/事件/流量的"METERINGTYPE 变种"——这些差异**只写进各 feature DP，1-00010 场景差异只有 3 条泛化项** → 1-00010 对 7 特性是假通用。复用者点开 1-00010 看不到任何特性差异。

5. **★ 命令集 union 致误带（新型假通用，配置生成风险，2026-07-10 QoS 族实战）**：族通用 compound 的命令集是族内多特性**并集**（如 1-00017 QoS专有承载链 = QOSPROP + SADEDICBEARER），但个别 feature **只用子集**（如 2-00030 视频承载仅 QOSPROP，无 SADEDICBEARER）。Jaccard 可能 < 0.75。**风险**：配置生成若按 compound 典型脚本盲目套用该 feature，会**误产出 feature 不用的命令**（如给 2-00030 误带 ADD SADEDICBEARER）。这与"差异抹平"型假通用（1-00010）相反——是"命令多带"型。
   - **判定**：feature 复用 compound 时，若 feature **不执行 compound 的某段命令**，compound「场景差异」是否显式分列该 feature 的命令子集（"本特性不执行 X 段"）+ 复用警示？若 compound 场景差异对该 feature 全空/仅"待核实" → 假通用未解除（critical）。
   - **防法**：compound 场景差异表**逐 feature 列命令子集**（哪些命令执行/哪些省略 + 参数变种）+ ★复用警示「勿按典型脚本盲目套用 X 场景，X 场景不执行 Y 段」。feature 配置流程复用 compound 时，对省略的段加脚注「本特性不执行 compound 的 Y 段」。

### R1.3 步骤拆分合理性
**防错位**——compound 该建才建。

1. **单命令步骤是否错建了 compound？**（应直接 atom，SOP §3.5）。检查每个 compound 是否真为"多命令可复用模块"，有无仅含 1 命令的伪 compound。
2. **多命令可复用模块是否漏建 compound？** 多特性重复"散编 atom"却无 compound 承载 → 该建未建。
3. compound **边界是否高内聚**？有无把不相关命令混进一个 compound（如 BWM 范本初期把过滤链+规则绑定混进 PCC链）。

### R1.4 activation 模板复用识别（critical，防零证据差异）
产品文档常对相似特性**复用同一份 activation 部署模板**（实战：时长/流量/事件计费的 activation md5 完全相同，都演示 VOLUME）。
1. 比对待审特性 activation 文档是否与其他特性雷同（md5 / 内容抽样比对）。
2. 若雷同（模板复用）：feature 声称的**差异化参数**（如 DURATION/EVENT/计费点）在该特性 activation 中是否有演示？若无 → **零证据差异**。
3. 零证据差异必须：①标真实来源（特性概述/实现原理/命令 wiki 的 evidence）②feature 配置流程/DP 脚注注明"本参数 activation 未演示，取值来自 XXX"。
4. **配置生成按 feature 配置流程产出脚本——零证据参数 = 编造 = critical 阻塞**。
5. **R1.4 子规则·组合参数跨 activation 来源（warning→critical）**：feature 某 compound 场景差异/配置流程声称的**参数集**若来自**多份 activation 分别演示**（非单一脚本合并演示），须脚注"参数 A 来自 activation X，参数 B 来自 activation Y，配置生成合并产出时须核实命令支持同条带多参数"。典型：融合计费 `SET USRPROFCHARGE/SET APNCHARGECTRL` 的 `CCTEMPLATE`（配置融合计费模板_93400212）与 `CONVERGEDSW/RGAPPLIED`（使能融合计费功能_77691175）分属两份 activation，从未合并演示 → 合并产出前须核实命令 wiki 参数表同时含三者。**未核实即合并 = 隐含编造同条支持 = critical 阻塞**。

### R1.5 配置流程参数证据链（critical，防编造参数）
feature「配置流程」是配置生成的**可执行蓝图**（非知识叙述）。写进配置流程的**每个命令+参数**必须可追溯到 evidence：
1. 每个命令：有对应 atom（查 `_numbering.json`）或有原始文档脚本出处。
2. 每个参数：activation 脚本 / 命令 wiki / 数据规划表有该参数取值证据。
3. **无证据的参数必须移除或改为"UDG 侧不配 / 由上层决定"**，否则配置生成编造参数。
4. **R1.5 子规则·可选命令证据链（warning→critical）**：feature 配置流程/DP 表中**可选步骤的命令**若 activation 未直接演示，**不能默认有证据**——必须明确标 evidence 出处（命令 wiki / 特性 wiki / 场景推断），并在步骤脚注注"activation 未直接演示，证据来自 XXX"。典型：PCC 基本功能 步骤 10 `ADD PCCPBINDUPG`（4 份 activation 均未演示）→ 须标命令 wiki 为证据 + 注"本地 PCC 多 UserProfile 场景，activation 未直接演示，按全网规划产出"。命令 wiki 也不存在 → critical 阻塞（命令本身无证据）。**配置生成对"可选 + 无 activation + 无命令 wiki"的步骤默认不产出，待补证据**。
5. **R1.5 子规则·DP/配置流程分列不同命令（warning）**：同一配置层次（如 CC 层）涉及**多个不同命令**且职责不同时（如"使能开关"vs"模板绑定"），DP 表/配置流程**必须分列**，不能合并"走法=命令A+命令B"造成混淆。典型：融合计费 CC 粒度 = ① `ADD CHARGEMETHOD`（使能开关 CONVERGED/RGAPPLIED，步骤 1）② `ADD SELECTCCTBYCC`（CCT 模板绑定 CCVALUE→CCTMPLTNAME，步骤 6）—— 两命令参数集正交（命令 wiki 佐证），合并写"走法=ADD CHARGEMETHOD+ADD SELECTCCTBYCC"会让配置生成误判为一条命令或同步骤执行。分列标准：命令 wiki 参数表是否正交（正交→分列；同参数集→可合并为 compound）。
> 实战教训：事件计费 feature 配置流程写了"PCCPOLICYGRP 可配计费点 REQUEST/RESPONSE/FINISH"，但 activation 与 PCCPOLICYGRP 命令 wiki 均无此参数 → 配置生成会编造。约束/DP 里的叙述性知识（"仅 SCUR/不支持 Default Quota"）可不进配置流程，但须标 evidence 出处。

> **★ 审视者警示：无证据结论须穷尽搜索后再判 critical**。审视发现"疑似编造参数/假约束"时，须先 grep 原始文档 / 特性 wiki / **官方差异表** / **软件参数文档（BIT/BYTE/BYTE837 等）** / 命令 wiki 全文，确认真无证据再判 critical。实战 2 次反转（均因搜索不充分误判 critical，后修复时核实发现有证据）：①计费事件计费点 REQUEST/RESPONSE/FINISH（命令 wiki 确有 `EVENTCHARGEFLAG`/`EVENTCHGPOINT`）②头增强 Byte837 十六进制编码（软件参数文档 `BYTE837_08922610` 确有）+ RTSP 不支持防欺诈（官方差异表 `头增强功能之间的差异_10706790` 确有）。**判 critical 前穷尽搜索；修复移除前也先核实**。反转不否定审视价值——每次都逼出了 evidence 链接，产出更严谨。

---

## R2 辅助维度（顺带查）

- **R2.1 命令完整性**：feature 涉及命令是否都有 atom（查 `_numbering.json`）？缺失是否标注待补？
- **R2.2 DP 影响表**：每 option 影响全记？特性核心差异维度进 DP？有无"走法"列（多命令compound vs 单命令atom）？
- **R2.3 双向链接**：atom ↔ compound ↔ feature 闭环；无 `[[占位]]` 残留（除明确待建）；无断链。

---

## R3 输出格式

### 每 feature
```
## {feature_id} {名称}（2-XXXXX）
### R1.1 覆盖度：原始 N 步 → 逐条 ✓/✗/⚠
  - 步1 ✓ | 步2 ✓ | 步3 ✗(遗漏:xxx) | 步4 ⚠(偏离:xxx)
### R1.2 复用：✓合理 / ⚠差异未记全(列哪条) / ✗假复用(列哪个compound)
### R1.3 拆分：✓ / ⚠问题(列)
### 问题清单：[critical|warning|info] 具体问题 + 修复建议
```

### 族级总结
- **共性问题**（多特性重复出现的）
- **复用模式是否合理**（backbone 是否被正确复用/有无假通用）
- **SOP/拆分方法改进建议**（沉淀回 SOP 或本流程）

---

## R4 严重度
- **critical**：激活步骤遗漏 / 假复用致命令丢失 / 计费冲突级约束未记 → 必须修
- **warning**：差异未进场景差异 / DP影响不全 / 拆分错位 → 应修
- **info**：措辞/链接/格式 → 可选
