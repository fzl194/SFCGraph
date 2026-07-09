# 进展与下一步（Typed LLM Wiki 端到端方案）

> 用途：context 压缩后快速恢复。读本文件 + `assets/CLAUDE.md` 即可接上。
> 更新：2026-07-08

## 总方案
- **定位**：类型化的 LLM Wiki（Typed LLM Wiki）—— md 是载体、Schema 是约束；一对象一 md，关系用链接承载。自包含可剥离，服务化按子场景取子集给 SKILL 配置生成。
- spec：`docs/superpowers/specs/2026-07-08-config-generation-e2e-design.md`（v2）
- 准则：`assets/CLAUDE.md`（§5 ID+引用、§5.6 双向链接、§7 可剥离、§4 三操作 Compile/Query/Lint）
- memory：`~/.claude/projects/D--mywork-KnowledgeBase-SFCGraph/memory/typed-llm-wiki-e2e-plan.md`

## 关键准则（已写进 CLAUDE.md）
- **ID**：绑产品层四段式 `{nf}@{version}@{ObjectType}@{local_id}`（命令 local=命令名、特性=feature_code、任务=层前缀+流水、ConfigObject=对象名）；**业务层两段式 `{ObjectType}@{语义slug}`**（跨产品不带 nf@version）。旧业务编号 `BD-BSA-01`/`NS-CH-01`/`CS-CH-03`/`DP-CH-xx` **废弃**。
- **引用**：已建对象 → 标准 markdown 链接 `[显示名](assets根路径.md)` 带 .md；未建对象 → `[[对象ID]]` 占位（双方括号=待建）。禁文件间相对路径 `../`，统一从 assets/ 根。证据同款（`evidence/...`）。
- **双向链接**（硬约束）：每条关系两端 md 互引（命令↔ConfigObject、Feature↔License、方案↔特性/任务）。Compile/Lint 维护。
- **可剥离**（硬约束）：assets/ 自包含，引用内容拷进来（证据/Schema/SOP），wiki 闭环不断链外部。
- **分工**：Agent 写维护、人 sourcer/reviewer/editor（不是人写 md）。

## 已完成

### P1 基建（commit 0921fec, f6c296e7）
- `assets/` 骨架：command / feature / license / business / task / skill / schema / evidence / configobject
- `assets/CLAUDE.md`（维护准则）、README.md、index.md（顶层导航）、log.md
- `assets/schema/三层图谱定义.md`（Schema 自包含拷贝，1418 行）

### P2 命令层（commit 209f0fde, 419213724, ade4b4df3, 7a4cdce05）
- `assets/scripts/compile_commands.py`：`mml_commands.jsonl` → 命令 typed md（**纯投影**，13075 命令 = UDG 4577 + UNC 8498）。参数内聚（parameter_description 直搬，不单独建）。
- `assets/scripts/compile_configobjects.py`：`config_objects.jsonl` → ConfigObject typed md（5818 = UDG 2210 + UNC 3608）。ConfigObject 是命令聚合枢纽，"操作本对象的命令"双向反查 command_object_edges（把 ADD/MOD/RMV/LST 同对象命令族串起来）。
- 引用体系闭环：已建 `[显示](path.md)` / 未建 `[[ID]]` 占位。
- 证据去重：以**源手册文件名 stem** 命名，命令和 ConfigObject 引同一手册时共用同一 evidence（从 18893 降到 13075）。
- 分级 index：每 `{nf}/{version}/` 一个局部 index（命令按 category_path、ConfigObject 按 object_kind 分组）。顶层 index.md 只导航。

### P2-续 特性层 + License（本批）
- `assets/scripts/compile_features.py`：`features.jsonl` → 特性 typed md（942 = UDG 313 + UNC 629）。13 节正文（`*_raw` 直搬）+ 所需License + 特性关系（双向按 relation_type 分组）+ 目录父子（双向）+ 证据。
- `assets/scripts/compile_licenses.py`：`licenses.jsonl` → License typed md（635 = UDG 187 + UNC 448）。raw 字段 + 控制的能力（反查 requires_license → Feature，与特性层"所需 License"互为双向）+ 证据。
- 双向验证：Feature↔License、Feature↔Feature（depends_on193/conflicts58/interacts18/affects15/supports1）、目录父子 全闭环。
- 占位防护：`link_or_placeholder` —— 关系端点不在本层对象集（audit 标的悬空 target）渲染为 `[[对象ID]]`，绝不产出指向不存在文件的断链。
- 证据去重：与命令层共用 evidence/（按 stem），总数 16231（+3156）。
- 数据备注：jsonl 中文 `open(encoding=utf-8)` 直读干净；终端 `head|json.tool` 乱码是 Windows stdin cp936 再编码，非数据问题。

### P5 命令级别 task wiki（atom 187，本批）
- **定位关键转折**：task wiki **不是纯投影**，是 **Agent 读证据包+原始 md 重写**。命令 wiki = 命令静态产品文档；命令级别 task wiki = 配置生成实例化时**该命令怎么配**的动作知识（参数取值来源/决策点联动/约束/配置原则），**不复述命令静态字段**只链接。
- **主输入**：`ConfigTask/task-build-skill/scripts/build_command_evidence.py` 生成的**命令证据包**（`ConfigTask/assert/UDG/20.15.2/command-evidence/{atom}.md`），含③「各特性配置范式」（数据规划表取值样例+脚本+步骤）——"命令真正配置方法"的来源。task/rule/dp yaml 是结论参考不复述。
- 产出：task md 187（atom，平均 50 行/篇），rule/DP 内嵌（不拆三对象，§5.3 锚点）。局部 index 按编号。
- 构建：Agent 驱动，每批 5 atom × 2 并行，19 轮。
- 回填：`assets/scripts/lint_and_backfill.py` 把命令 md 的 `[[Task]]` 占位 + task md 误占位的已建对象 回填为 markdown 链接（401 处/265 文件）。
- 范围：UDG atom 187 + UNC atom 209 均已建。compound(4)/feature(11) 级 task 后续；task↔task 双向预留。
- **UNC 补充**（pre-build 证据包驱动）：UNC atom 资产残缺（只 27），用 `build_command_evidence.py --cmds` 的 pre-build 证据包（209，①段空，只有②命令真相+③各特性配置范式）驱动 Agent 建 209 篇。决策点/rule **现场归纳、不编号**内嵌（UNC 无①atom/rule/dp yaml，DP/Rule 与 task 绑定无独立 ID）。编号：0-00001~0-00027 沿用 UNC atom yaml，0-00028~0-00209 接续（`renumber_unc_tasks.py` 建映射 + 重命名 + 改引用）。
- 沉淀方案：`docs/superpowers/specs/2026-07-08-configtask-layer-compile-design.md`（v2 Agent 构建）

## 跑通的模式（业务层/任务层 LLM 凝练时复用引用与 index 约定）
**纯投影 Compile 器**（jsonl → typed md）+ markdown 链接引用（带 .md）+ 双向链接 + 证据去重（源手册 stem 命名）+ 分级 index + 占位防护（`link_or_placeholder`）。

## 下一步候选（待用户定方向）
1. **服务化接口（P3，推荐）**：platform-next（FastAPI 已有业务图谱接口雏形）扩展"知识包"接口，输入 `{域}/{场景}`，输出子场景裁剪子图全量 md 包。验证"服务化取包 → SKILL 消费"端到端。此时命令/特性/License 三层已就绪，可端到端跑通取包。
2. **业务层 Compile（P4）**：LLM 读产品文档按 Schema 凝练 BD/NS/CS typed md + 人审（现有 business-graph md / BusinessGraph yaml 仅作线索）。核心范式（Agent 写、人审）首次验证，慢、要业务专家卷入。同时定业务层 wiki ID → 文件路径 resolver（两段式 ID 没含 domain/scenario 段，需 slug 索引或链接补 domain）。
3. **compound/feature 级 task wiki**：命令级 atom 已完成（UDG 187 + UNC 209）；步骤级 compound(4)/特性级 feature(11) task wiki 后续建（建时同步 task↔task 双向编排、回填命令级 task 的"参与编排于"节）。
4. **Lint（P8 提前做一版）**：静态体检——查断链（被引无页）、缺反向链接、占位未回填、Schema 不合规。命令+特性层已够多对象，Lint 有素材。

## 已知小缺口（留给 Lint 阶段）
- ConfigObject 中文名缺失（`object_name_zh` 数据本身是英文，如 URR）——数据问题不是 Compile 问题。
- `command_parameters.jsonl` / `command_has_parameter.jsonl` 仅 443 条（严重不全），参数知识全在 `mml_commands.parameter_description`（已内聚进命令 md），不影响。

## 关键文件指针
- Compile 器：`assets/scripts/compile_commands.py`、`assets/scripts/compile_configobjects.py`
- 准则：`assets/CLAUDE.md`
- 产出：`assets/command/{nf}/{ver}/`、`assets/configobject/{nf}/{ver}/`、`assets/evidence/{nf}/{ver}/`
- 数据源（只读）：`CommandGraph/data/assets/{nf}/{ver}/*.jsonl`、`ConfigTask/assert/{nf}/{ver}/*.yaml`、`FeatureGraph/data/{nf}/{ver}/*.jsonl`、`business-graph/`、`output/`

## 演进路线（spec §11）
P1 基建 ✅ → P2 命令层 ✅ → P3 服务化 → P4 业务层 → P5 任务层 → P6 SKILL 切换 → P7 test → P8 Lint+debug。
