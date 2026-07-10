# log · assets/ 演进日志

> **append-only，不删改历史。** 给 wiki 演进时间线，帮 Agent 理解近期变更。
> 每条前缀 `## [YYYY-MM-DD] <ingest|query|lint> | <对象/操作>`，便于 `grep "^## \[" log.md | tail -N`。
> 规则见 `CLAUDE.md` §6。

---

## [2026-07-08] ingest | assets/骨架
- 来源：P1 纯基建（`docs/superpowers/specs/2026-07-08-config-generation-e2e-design.md` v2）
- 动作：建立 assets/ 目录骨架 + README.md + CLAUDE.md（维护准则）+ index.md + log.md
- 状态：容器就位，未 Compile 任何对象内容（下一步 P2：命令层 Compile 器）

## [2026-07-08] ingest | 命令层 + ConfigObject
- 来源：P2，`CommandGraph/data/assets/{nf}/{ver}/*.jsonl` 纯投影
- 产出：命令 md 13075（UDG 4577 + UNC 8498）、ConfigObject md 5818（UDG 2210 + UNC 3608）
- 模式：纯投影 + markdown 链接引用（带 .md）+ 双向（命令↔ConfigObject 经 command_object_edges）+ 证据按源手册 stem 去重 + 分级 index
- 准则落地：CLAUDE.md §5.5（已建 `[..](.md)` / 未建 `[[ID]]` 占位）已写进

## [2026-07-08] ingest | 特性层 + License
- 来源：P2-续，`FeatureGraph/data/{nf}/{ver}/*.jsonl` 纯投影（features/licenses/feature_requires_license/feature_relations）
- 产出：特性 md 942（UDG 313 + UNC 629）、License md 635（UDG 187 + UNC 448）
- 双向：Feature↔License（requires_license 出/入向）、Feature↔Feature（depends_on/conflicts_with/interacts_with/affects/supports，双向按类型分组）、目录父子（parent_feature_code 双向）
- 占位：悬空 target（audit 标 depends_on 3/conflicts 1/requires_license 1）渲染为 `[[对象ID]]`，无断链（compile_features/compile_licenses 加 link_or_placeholder 防护）
- 证据：与命令层共用 evidence/，按 stem 去重，总数 16231（命令 13075 + 特性/License 新增 3156）
- 数据说明：jsonl 中文文本经 `open(encoding=utf-8)` 直读完全干净；早期终端 `head|json.tool` 乱码是 Windows stdin 管道 cp936 再编码所致，非数据问题



## [2026-07-09] ingest | 命令级别 task wiki（atom 187）
- 来源：P5，ConfigTask/assert/UDG/20.15.2 命令证据包（build_command_evidence.py 生成）+ atom/rule/dp yaml + 命令 wiki
- 产出：task md 187（atom，平均 50 行/篇），覆盖计费三件套+过滤链+带宽+QoS+接入+IPsec+L2TP+路由+URL过滤+IPSQM+TWAMP 等场景
- 定位：命令级别 task wiki = 配置生成实例化时该命令**怎么配**的动作知识（参数取值来源/决策点联动/约束/配置原则），从证据包③「各特性配置范式」归纳，**不复述命令静态字段**（链接命令 wiki）
- 构建：Agent 驱动（每批 5 atom × 2 并行，19 轮），证据包③为主输入；rule/DP 内嵌（不拆三对象）
- 回填：lint_and_backfill.py 把命令 md 的 [[Task]] 占位回填为 markdown 链接（401 处/265 文件）
- 范围：仅 UDG atom（compound/feature 级 + UNC 后续）；task↔task 双向预留


## [2026-07-09] ingest | 命令级别 task wiki · UNC（atom 209）
- 来源：P5-续，ConfigTask/assert/UNC/20.15.2 pre-build 命令证据包（209，build_command_evidence.py --cmds 生成，①段空，只有②命令真相+③各特性配置范式）+ 命令 wiki
- 产出：task md 209（atom，平均 60 行/篇），覆盖 APN/计费/CG/PCC/PCRF/CHF/Diameter/N40/话单/策略 等 UNC 控制面场景
- 定位同 UDG：命令级别 task wiki = 实例化怎么配，不复述命令静态字段
- 构建：Agent 驱动（每批 5 × 2 并行，21 轮），pre-build 证据包②③为主输入（①段空）
- 决策点/rule：现场从②③归纳，**不编号**内嵌语义标题（UNC 无①atom/rule/dp yaml，DP/Rule 与 task 绑定无独立 ID）
- 编号：0-00001~0-00027 沿用 UNC atom yaml；0-00028~0-00209 按命令名排序接续。renumber_unc_tasks.py 建映射+重命名+改引用（先建命令名后改编号）
- 回填：lint_and_backfill.py 回填 UNC task 互引 + 命令 wiki 关联任务占位（136 处/90 文件）
- 范围：仅 UNC atom。compound/feature 级 + UDG 的 compound/feature 后续

## [2026-07-10] lint | UNC 计费族首批 5 warning R3 修复 + SOP 沉淀
- **范围**：assets/task/UNC/20.15.2/ 计费族 2-00002/2-00003/2-00004/2-00005 + compound 1-00002/1-00003 + 特性task_wiki审视流程.md
- **5 warning 修复（只改不删，编辑标注/分列/补证据）**：
  1. 2-00002 热计费 ROAMOFFLINE：activation 脚本仅演示 HOMEOFFLINE/VISITOFFLINE=ENABLE，ROAMOFFLINE 仅数据规划表列示 → 标注"脚本未演示，按全网规划，不可默认 ENABLE"
  2. 1-00002/1-00003 融合计费组合参数：CCTEMPLATE（配置融合计费模板_93400212）与 CONVERGEDSW/RGAPPLIED（使能融合计费功能_77691175）分属两份 activation 未合并演示 → 加脚注，合并产出前须核实命令 wiki 支持同条带三参数
  3. 2-00003 CC 粒度分列：ADD CHARGEMETHOD（使能开关 step1）vs ADD SELECTCCTBYCC（CCT 模板绑定 step6）两命令参数集正交 → DP 表/配置流程分列，不可混写"走法=命令A+命令B"
  4. 2-00004 ONLMETERINGTYPE=EVENT_VOLUME_TIME：核实 ADD URR 命令 wiki（line 67 确有此取值，与 OFFMETERINGTYPE 对称）→ 命令层证据成立；activation 仅演示 FREE/VOLUME → 标 evidence=命令 wiki 非 activation，实际取值全网规划
  5. 2-00005 步10 ADD PCCPBINDUPG：4 份 activation 均未演示 → 标 evidence=命令 wiki（PGW-C/SMF，立即生效，用途本地 PCC 多 UserProfile 策略源），注可选+全网规划产出
- **SOP 沉淀（特性task_wiki审视流程.md）**：
  - R1.4 第5点 组合参数跨 activation 来源子规则（warning→critical）
  - R1.5 第4点 可选命令证据链子规则（warning→critical）
  - R1.5 第5点 DP/配置流程分列不同命令子规则（warning）
- **证据核实结论**：EVENT_VOLUME_TIME 命令 wiki 有（ADD-URR.md line 67）；ADD PCCPBINDUPG 命令 wiki 存在（PGW-C/SMF）
