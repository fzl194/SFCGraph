# ConfigTask 流水线操作手册（Runbook）

> 半自动化：**自动代码步连续跑，Agent 步遇 PAUSE 停**。
> Agent 步不调 LLM——代码把全部 prompt 写到文件，Agent 基于文件跑，输出回填后续跑。
> **数字资产按 网元×版本 隔离**：所有产出在 `data/{nf}/{version}/` 下（Schema §2）。拿到的网元/版本互不覆盖。
> 拿到内网跑别的网元/版本，照本文 §4 走。

---

## 1. 模型：code → Agent → code-verify → code → ...

```
[自动步] 输入文件 → 代码 → 输出文件（幂等；输出已存在则跳过）
   │
[Agent 步]  prep(写全部 prompt 到文件) → check(输出齐?)
   ├─ 未齐 → 打印待处理清单 → 返回 PAUSE → build_all 停
   └─ 齐了 → ingest(解析+追加) → 下一步自动 verify
   │
[自动步] ... 循环
```

**唯一驱动命令**：`python build_all.py <nf> <version>`（全量）或 `python build_all.py <nf> <version> <step>`（单步）。

- 全量跑：自动步输出已存在则**跳过**（快速续跑）；Agent 步**总执行** prep/check。
- 单步跑：不跳过，强制执行该步。
- `--rerun <key>`：强制把匹配 doc/cluster 当 pending 重处理。

---

## 2. 每步明细（输入 → 代码 → 输出 → 校验）

所有文件路径前缀为 `data/{nf}/{version}/`（如 `data/UDG/20.15.2/`）。下表省略该前缀。

| # | 步 | 类型 | 输入文件 | 代码 | 输出文件 | 校验 |
|---|---|---|---|---|---|---|
| 0 | scan | 自动 | corpus_root | `builder/steps/scan.py` | `corpus_manifest.csv` | — |
| 1 | extract_steps | 自动 | corpus_manifest | `builder/steps/extract_steps.py` | `doc_steps.jsonl` | — |
| 2 | **split_tasks** | **Agent** | `doc_steps.jsonl` | `builder/steps/split_tasks.py` | `task_candidates.jsonl` | verify_split |
| 2.5 | verify_split | 自动 | doc_steps + candidates | `builder/steps/verify_split.py` | (控制台) | 完整/连续/非空/对象族 |
| 3 | cluster | 自动 | `task_candidates.jsonl` | `builder/steps/cluster.py` | `task_clusters.jsonl` | 完整性 |
| 3.5 | enrich | 自动 | task_clusters + doc_steps + 原始md | `builder/steps/enrich.py` | `task_clusters_enriched.jsonl` | 0 空 member |
| 4 | **merge_fields** | **Agent** | `task_clusters_enriched.jsonl` | `builder/steps/merge_fields.py` | `config_tasks.jsonl` | verify_merge |
| 4.5 | finalize_fields | 自动 | config_tasks + mml_commands | `builder/steps/finalize_fields.py` | `config_tasks.jsonl`(补字段) | command_ref 全键命中 |
| 5 | verify_merge | 自动 | `config_tasks.jsonl` | `builder/steps/verify_merge.py` | (控制台) | 字段非空/binding 枚举 |
| 6 | extract_rules | **Agent(未实现)** | config_tasks | — | task_rules/decision_points | verify_rules |
| 7 | assemble | 自动(未实现) | config_tasks+rules | — | `assets/` | — |

---

## 3. Agent 步交接契约（纯文件，可移植）

每个 Agent 步（split_tasks / merge_fields / 未来 extract_rules）遵循同一契约。路径均在 `data/{nf}/{version}/` 下：

| 角色 | 路径 | 谁写 |
|---|---|---|
| prompt（入） | `data/{nf}/{version}/agent_prompts/{step}/<key>.txt` | **代码 prep** 生成（一次写全） |
| 输出（出） | `data/{nf}/{version}/agent_outputs/{step}/<key>.json` | **Agent / 人** 写 |

**key 规则**：
- `split_tasks`：`batch_<hash8>`（每批 `agent_batch_size=5` 文档，hash 来自批内 doc 集合）
- `merge_fields`：`<cluster_id>`（如 `cluster-003`）

**done 判定**：从**输出 jsonl** 派生（不依赖易丢的 progress 文件）：
- split_tasks：`doc_path` 在 `task_candidates.jsonl` 里 = done
- merge_fields：`cluster_id` 在 `config_tasks.jsonl` 里 = done

### Agent 怎么调（两种环境都一样）

**外网（当下，Claude/subagent）**：
```
subagent 指令 = 「读 data/agent_prompts/merge_fields/cluster-003.txt，按其指令做，把 JSON 写到 data/agent_outputs/merge_fields/cluster-003.json」
```
（subagent 有 Write 工具，直接写输出文件）

**内网（换 LLM）**：把 `<key>.txt` 喂给你的 LLM，把返回 JSON 存到对应 `<key>.json`。契约不变。

### PAUSE 时 build_all 的输出样例
```
[PAUSE] @merge_fields：Agent 待处理（交接清单见上）
   1. 调 Agent，把输出写到 data/agent_outputs/merge_fields/<key>.json
   2. 重跑续: python build_all.py UDG 20.15.2
```

---

## 4. 新网元/版本怎么跑（例：UNC 20.15.2）

1. **改配置**：`pipeline.yaml` 的 `ne.UNC.20.15.2` 指向 UNC 的 corpus_root + command_graph_dir（已配）。
2. **自动段**：`python build_all.py UNC 20.15.2`
   - 自动跑 scan → extract_steps，**到 split_tasks PAUSE**（prompt 写到 `data/agent_prompts/split_tasks/`）。
3. **Agent 段（split）**：对每个 `batch_*.txt` 调 Agent，输出写 `data/agent_outputs/split_tasks/batch_*.json`。（受并行上限约束，分波调）
4. **续跑**：再 `python build_all.py UNC 20.15.2`
   - split_tasks ingest → verify_split → cluster → enrich，**到 merge_fields PAUSE**。
5. **Agent 段（merge）**：对每个 `cluster-*.txt` 调 Agent，输出写 `data/agent_outputs/merge_fields/cluster-*.json`。
6. **续跑**：merge_fields ingest → finalize_fields → verify_merge。完成。
7. （未来）extract_rules / assemble 同模式。

**关键**：每次 `build_all` 跑到下一个 Agent 步就停（PAUSE），填完输出再续。自动步幂等可重跑，输出已存在则跳过。

---

## 5. 停点清单（什么时候停、停在哪）

| 停点 | 触发 | 你要做的 |
|---|---|---|
| PAUSE @ split_tasks | split prompt 已写，输出未齐 | 调 Agent 写 split 输出 → 重跑 |
| PAUSE @ merge_fields | merge prompt 已写，输出未齐 | 调 Agent 写 merge 输出 → 重跑 |
| 全完成 | config_tasks.jsonl 全簇齐 + verify_merge 过 | 进入 extract_rules（未实现）|

**重抽单个**：删对应 `data/agent_outputs/{step}/<key>.json`，必要时从输出 jsonl 删该条，重跑 build_all。

---

## 6. 字段后处理边界（外网 vs 内网）

| 字段 | 哪补 | 说明 |
|---|---|---|
| `command_ref` 全键 | **finalize_fields（外网，mml_commands 全）** | 裸名 → `UDG@20.15.2@MMLCommand@<name>` |
| `source_evidence_ids` | finalize_fields（外网） | 聚合 cluster member.doc_path |
| `_decision_points`/`_split_notes` | finalize_fields（外网） | 中间态加 `_` 前缀，喂下一阶段 |
| `parameter_ref` 全键 | **内网程序**（command_parameters 全集在内网） | 当前裸名，待补 |
| `source_ref` | **内网程序**（parameter_references + DecisionPoint 对象） | 当前缺，待补 |

外网 `finalize_fields` 只补不删，基本信息零丢失；未知命令保留裸名不臆造。

---

## 7. 目录约定

```
ConfigTask/
├── build_all.py                 # 唯一驱动入口
├── pipeline.yaml                # 配置（换网元/版本改这里）
├── builder/steps/*.py           # 各步实现
├── builder/core/                # md_reader / enrich 解析器 / commands
├── builder/agent/prompts.py     # SPLIT_TASKS_PROMPT（merge/extract 各步自带 build_prompt）
├── tests/                       # pytest（每步 prep/ingest/verify 都有测）
└── data/{nf}/{version}/         # ★ 网元×版本隔离（UDG/UNC 互不覆盖）
    ├── corpus_manifest.csv ... config_tasks.jsonl   # 权威产出（6+1 文件）
    ├── agent_prompts/{step}/<key>.txt               # 代码 prep 生成
    ├── agent_outputs/{step}/<key>.json              # Agent 输出（人/LLM 写）
    └── assets/                                      # assemble 产出（未来）
```
