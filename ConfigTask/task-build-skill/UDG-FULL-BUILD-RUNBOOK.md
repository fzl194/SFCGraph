# UDG 全量 Task 构建交接 Runbook

> 目标：把 UDG 所有可配置特性的 Task 层资产构建完整。长周期、跨多会话。
> 本文件是**交接机制**——任何新会话照此续跑，不丢上下文、不漏特性。
> 依赖：`SKILL.md`（构建准则）、`scripts/build_index.py`（索引）、`review-ui/`（审查）、根目录 `改进后三层图谱定义.md`（schema）。

---

## 0. 一句话机制
**每个特性 = 一次独立 pass**：查 `index.json` 找已有 → 按 `SKILL.md` 建全底部 atom → 凝练 compound → feature task（复用/合并/演进已有）→ 自审 + 正向实例化 → 更新 `progress.json` + 重建 `index.json` + 写 review 记录。一个特性可在一个会话内完成；会话结束写回进度，下个会话续。

---

## 1. 快速查找机制（已落地 ✅，回答"是否看已有 task"）

**是的，每次构建前必查已有 task。** 机制：`task-assets/{nf}/{version}/index.json`（每次 pass 末尾由 `scripts/build_index.py` 重建）。

| 查什么 | 索引键 | 用途 |
|---|---|---|
| 命令 C 是否已有 atom | `by_command["ADD URR"]` → `0-00001` | 复用/演进（不重建） |
| 特性 F 已有哪些 task | `by_feature["GWFD-020300"]` → feature task + compounds + atoms | 续建/查漏 |
| atom A 被谁用 | `atom_usage["...0-00001"]` → 4 个 feature | 演进影响面（连锁复审） |
| 语义名是否已存在 | `by_logical_name["配置URR"]` | 合并判据（§7.1） |
| 某 task 挂了哪些 rule/dp | `rules_by_owner` / `dps_by_owner` | co-build 检查 |

构建前必做：`查 index.json` → 对当前特性的每条命令 `by_command` 查 atom → 命中则**复用+评估演进**，未命中才新建。这就是"新 task 结合旧 task"的执行点。

> 人类可读的 `task-index.md` 保留作概览；`index.json` 是机器/Agent/UI 共用的快速查找。

---

## 2. 构建范围（不遗漏的基准）

**封闭清单**：从 `FeatureGraph/data/legacy/UDG_feature_files.csv` 派生"可建特性"（一次性，存 `progress.json`）：
- 按 feature_id 聚合文件；**文件名（basename）** 含 `部署|激活|配置` 的才算有配置步骤（路径前缀 `特性部署` 不算）。
- 每个可建特性最终状态必为 `done` 或 `skipped(带原因)`。**不允许"未处理"残留** → 这就是完整性保证。

派生命令（首次或刷新用）：
```
python task-build-skill/scripts/seed_progress.py UDG 20.15.2
```
（读 CSV → 写 `task-assets/UDG/20.15.2/progress.json`，详见 §6）

---

## 3. 分批策略（长任务切片）

- 按 `UDG_features.csv` 的 `section`（业务域）分批：同域特性共享 atom 概率高，复用密集。
- 每批 **10~15 个特性**，1 个会话做 1~2 批（视复杂度）。
- 批内顺序：先建共享底座特性（如 SA-Basic、PCC、基本接入），再建依赖它们的特性（复用最大化）。
- 批状态在 `progress.json` 的 `batch_status` 里（in_progress/done）。

> 已完成参考：计费域（4 特性：GWFD-020301/020300/010171/010173）已闭，可作样板。

---

## 4. progress.json —— 跨会话状态（交接核心）

结构（`task-assets/UDG/20.15.2/progress.json`）：
```json
{
  "nf_version": "UDG@20.15.2",
  "buildable_total": 86,            // 可建特性总数（seed 时定）
  "done": ["GWFD-020301","GWFD-020300","GWFD-010171","GWFD-010173"],
  "in_progress": [],                // 半成品（含断点说明）
  "not_started": ["GWFD-020351", "..."],
  "skipped": [{"feature_id":"GWFD-110101","reason":"协议底座，无配置步骤"}],
  "batches": [{"id":"B01","section":"计费","features":[...],"status":"done"}, ...],
  "last_session": {"date":"2026-06-30","by":"Agent","did":"计费域 4 特性 + generalized","next":"业务感知/PCC 域"}
}
```
**每个会话起手读它，收尾写它。** 它是唯一的进度真相。

---

## 5. 单特性 pass 流程（在 SKILL §5 基础上明确"查找/合并/演进"）

```
输入：feature_id F + FeatureGraph/data/legacy/UDG_feature_files.csv 过滤 F 的全部 md
0. 读 index.json：
   - by_feature[F]：F 是否已有 feature task / 用过哪些 atom/compound（续建？重建？）
   - 对 F 涉及的每条命令 C：by_command[C] 命中？→ 复用 atom；评估是否需演进（新配法/新证据/跨特性分叉）
1. 建全底部 atom（一命令一 atom）：
   - 命中 by_command：复用已有 atom；看 F 是否带来新配法（加 DP option）/新证据（加 source_evidence_ids）
       /variable_source 跨特性分叉（→ decision_driven，§4.5）。改动 atom 的 status 回 inferred，用 atom_usage 找影响面连锁复审（§7.2）。
   - 未命中：新建 atom（参数从 md 获取方法 + command jsonl 抽，§4.4/§4.5）。
2. 凝练 compound（按业务阶段）：每个候选先 by_logical_name + 命令集 Jaccard 判 合并/引用/新建（§7.1）。
   backbone 类 compound（计费三件套式）跨特性共享，直接复用。
3. 建 feature task（强制）：ref→Feature@F，task_relations 编排本特性 compound/atom + 特性专属可选 atom。
4. 跨特性凝练 generalized/solution（当 F 与已有特性可组合时）：按 §7.1 演化合并。
5. co-build：每层 task 连带建其 TaskRule + DecisionPoint（§6.2）。
6. 自审（review subagent，§8.1）+ 正向实例化（复现 F 的任务示例脚本）。
7. 收尾三件：
   - 写 review/{F}-pass-{N}.md
   - python task-build-skill/scripts/build_index.py   # 重建 index.json
   - 更新 progress.json：F 从 not_started → done（或 in_progress 若未竟）
```

---

## 6. 脚本（只读工具，非构建 pipeline）
- `task-build-skill/scripts/build_index.py [nf] [version]`：读 yaml → 写 `index.json`（每次 pass 末尾跑）。
- `task-build-skill/scripts/seed_progress.py [nf] [version]`：读 `UDG_feature_files.csv` → 派生可建特性清单 → 写/合并 `progress.json`（保留已 done 项）。**待创建**（见下）。
- `review-ui/serve.py`：审查 UI（读 index.json 渲染 + 收反馈）。

> 这些是**只读索引/派生/展示**工具，不替 Agent 抽取（抽取仍由 Agent 按 SKILL 做）。

---

## 7. 跨会话交接协议（新会话怎么续）

**会话起手**（Agent 读这 4 个文件恢复上下文）：
1. `task-build-skill/SKILL.md`（当前准则版本）
2. `task-assets/UDG/20.15.2/progress.json`（进度 + 下一个）
3. `task-assets/UDG/20.15.2/index.json`（已有 task 全景）
4. 根目录 `改进后三层图谱定义.md`（schema，按需查）

**取活**：从 `progress.json` 取一个 `in_progress`（续半成品）或首个 `not_started` 特性 → 按 §5 跑一个 pass。

**会话收尾**（写回交接）：
1. 重建 `index.json`（`build_index.py`）。
2. 更新 `progress.json`（done/in_progress/not_started + last_session 记"本次做了什么、下一个是谁"）。
3. 若 SKILL 有改动 → 版本号 +1（v2→v3…），在 SKILL.md 顶部记变更。
4. review 记录已落 `review/`。

> **健壮性**：progress.json 是唯一真相；index.json 可随时从 yaml 重建。即使某会话中途断了，下个会话读 progress.json 即知断点（in_progress 项 + last_session.next）。

---

## 8. 完整性保证（不漏特性）
- 可建清单**封闭**（seed 时定，CSV 全量派生）。
- 每特性终态必为 done 或 skipped(带 reason)。`seed_progress.py` 会报"无终态残留"。
- done 判据（硬）：① feature task 存在 ② 该特性 md 出现的配置类命令全有 atom（by_command 覆盖） ③ 正向实例化复现示例脚本 ④ review 记录已写。
- skipped 判据：记录原因（协议底座/纯查询/无配置文档/被并入他特性）。
- 每批收尾跑一次 `seed_progress.py --check`：列未终态项，强制归零。

---

## 9. UI 细粒度升级（展示 task 内部）
当前卡片是摘要。升级方向（`review-ui/index.html`）：
- **点击 task 卡片展开内部**：atom 展开 parameter_bindings 表（参数/binding_type/variable_source/requiredness/value/decision_ref）；compound/feature 展开内嵌 task_relations（from→to/relation_type/requiredness/propagated_context/condition_ref）。
- **规则卡片展开**：condition / constraint.expression / target_refs / violation_effect。
- **检索栏**：按命令名、feature_id、logical_name、status 过滤（直接用 index.json 的 by_command/by_feature）。
- **复用/演进高亮**：atom 卡片显示 atom_usage（被哪些特性用）+ 标记 decision_driven 的"演进过的"参数。
- **进度面板**：读 progress.json，显示 done/in_progress/not_started/skipped 计数 + 批次状态。

---

## 10. 每会话起手/收尾 Checklist
起手：[ ] 读 SKILL.md [ ] 读 progress.json [ ] 读 index.json [ ] 确认工作目录=ConfigTask、其余只读
收尾：[ ] 重建 index.json [ ] 更新 progress.json [ ] review 记录 [ ] SKILL 改动记版本 [ ] 提示人工可开 UI 审查
