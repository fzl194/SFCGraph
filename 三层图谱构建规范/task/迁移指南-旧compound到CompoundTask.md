# 迁移指南：旧 compound task → 新版 CompoundTask

> **这是一次性迁移工程文档，不是 SOP。** 把已建好的旧 compound（步骤级，多命令可复用模块）转成新格式。
> 目标读者：执行迁移的 Agent / 脚本维护者。读本文 + 附录 slug 表即可迁移，无需读 SOP、无需读命令层/特性层资产、无需理解业务。
> 配套脚本：`task/scripts/migrate_old_compounds.py`（本文是它的规则源）。

---

## 0. 任务定义

把旧步骤级 task（**compound**，`assets/task/UDG/20.15.2/1-*.md`，共 **34** 个）转换成新版本 CompoundTask md 格式。

- compound = **多命令可复用步骤模块**（`ref` 全 `null`，无单一命令锚）。
- **纯格式转换**：不重新理解业务、不补内容。旧 compound 写了什么就转什么。
- **ID 用英文语义 slug 做锚**（compound 没有命令名，slug 是人造锚，见附录 A）。
- **范围**：只迁 compound（`1-` 前缀）。atom 已迁完；feature_task（`2-`）不在本批。

---

## 1. 输入 / 输出

| | 旧 | 新 |
|---|---|---|
| 路径 | `assets/task/UDG/20.15.2/1-00003.md` | `三层图谱资产/CompoundTask/UDG/20.15.2/UDG@CompoundTask@bwm-usergroup-rule-bind.md` |
| 文件名 | 编号 `1-00003` | 完整 ID `UDG@CompoundTask@bwm-usergroup-rule-bind`（= slug 锚）|
| 总数 | 34 | 34 |

**slug 从哪来**：附录 A（34 条 `编号→slug`）。slug 是定稿的人造锚，不能像 atom 那样从 ref 现场读（compound ref=null）。

> ⚠ 输出目录 `三层图谱资产/` 当前被 `.gitignore` 忽略。迁移产物是否进 git 由用户定（同 atom 迁移）。

---

## 2. 总原则（对齐 atom 迁移，先记这三条）

1. **只改格式，不改内容**：配置方法 / 决策点 / 约束 / 场景差异的业务内容原样保留。只动 ID 体系、引用形式、段落结构、删证据。
2. **编号全废（仅限三套）**：只删 `1-XXXXX`（compound 自身）、`DP 0-XXXXX`、`rule-0-XXXXX`。特性编号（`GWFD-110311` 等）/规格数值/字母后缀占位**不删**。
3. **跨层/未迁引用删链接留文字**：feature_task（`2-`）、business CS（`business/...`）本批未迁，链接删、显示文字留为纯文本。

---

## 3. YAML 字段转换（7 字段，固定顺序）

```
id / type / name / name_zh / nf / version / status
```
（**无 ref** —— compound 无对应单命令；atom 的 ref 字段在 compound 删除）

| 旧字段 | → 新字段 | 规则 |
|---|---|---|
| `id: UDG@20.15.2@Task@1-00003` | `id: UDG@CompoundTask@bwm-usergroup-rule-bind` | 三段式 `{nf}@CompoundTask@{slug}`，去 version、去编号 |
| `type: Task` | `type: CompoundTask` | 改细分类型 |
| `task_layer: compound` | **删** | `type: CompoundTask` 已隐含 |
| `task_logical_name: BWM 用户组、规则与绑定` | `name_zh: BWM 用户组、规则与绑定` | 改字段名，值不变 |
| （旧无） | `name: bwm-usergroup-rule-bind` | **新增**，= slug（= id 的 local 段）|
| `ref: null` | **删** | compound 无对应命令 |
| `nf` / `version` / `status` | 原样 | — |
| `task_intent: ...` | **删** | 内容若正文未覆盖，补一句进引子（见 §4.2）|
| `source_evidence_ids: [...]` | **删** | task 层无证据 |

---

## 4. 正文转换（逐段）

> **迁移只转旧 compound 已有的段，不补缺段**：旧无 `## 决策点` 就不写；无 `## 约束` 就不写。

### 4.1 H1
**原样保留**：`# BWM 用户组、规则与绑定`

### 4.2 引子（H1 下 blockquote）
- 命令层链接转双方括号：`[ADD APN](command/...)` → `[[UDG@MMLCommand@ADD APN]]`
- task 链接按 §5 转。
- 若旧 `task_intent` 含正文未覆盖的概述，补一句进引子；否则丢弃。

### 4.3 `## 配置方法`（步骤表）
**业务内容原样保留**（步骤表「步骤/命令/关键参数」、典型脚本代码块）。只转其中的链接（§5）。代码块（` ``` `）**不动**。
- 纯文本括号编号 `ADD BWMRULE(0-00037)` 按括号去编号规则删（同 atom §4.3）。

### 4.4 `## 决策点`
- 去 DP 编号：`## 决策点：xxx（DP 0-XXXXX）` → `## 决策点：xxx`；正文 `DP 0-XXXXX` 引用删编号留语义。
- 选项表原样。

### 4.5 `## 约束`
- 去 rule 编号 + 来源标记，只留 severity：`（critical，rule-0-00317）` → `（critical）`。

### 4.6 `## 场景差异`（compound 特有，部分有）
**保留整段**。其中的 feature 引用按 §5 转：
- `[GWFD-020301](feature/...)` → `[[UDG@Feature@GWFD-020301]]`
- feature_task `[2-00001](task/...)` → 删链接留文字（未迁）

### 4.7 `## 关联` → `## 边`（**compound 特有，关键差异**）
见 §6。compound 关联段**不是整段删**，而是逐行解析、提取多条边。

---

## 5. 正文引用转换总表

| 旧形式 | 新形式 | 说明 |
|---|---|---|
| `[ADD APN](command/UDG/20.15.2/ADD-APN.md)` | `[[UDG@MMLCommand@ADD APN]]` | 命令层，连字符→空格 |
| `[0-00020](task/.../0-00020.md)` | `[[UDG@AtomTask@ADD APN]]` | atom 链接，查 atom 编号→命令表（现场读 0-*.md ref）|
| `[1-00002](task/.../1-00002.md)` | `[[UDG@CompoundTask@bwm-service-controller]]` | compound 链接，**查附录 A slug 表** |
| `[2-00001](task/.../2-00001.md)` | **删链接留文字** | feature_task 未迁 |
| `[GWFD-020301](feature/...)` | `[[UDG@Feature@GWFD-020301]]` | 特性层 |
| `[BWM-CS](business/...)` | **删链接留文字** | business CS 跨层 |
| `[FLOWFILTER](configobject/...)` | **删整条** | 配置对象 |
| `[...](evidence/...)` | **删整条** | 证据 |

**裸编号**（非链接）：正文纯文本里的 `1-XXXXX` → 查 slug 表转 `[[UDG@CompoundTask@{slug}]]`；`0-XXXXX` → 查 atom 命令表转 `[[UDG@AtomTask@{cmd}]]`。

**旧四段式 wiki 占位** `[[UDG@20.15.2@{Type}@{local}]]`：去 `20.15.2@` 段；`Task@1-` → `CompoundTask@{slug}`；`Task@0-` → `AtomTask@{cmd}`；`Feature` 保留；`DecisionPoint`/`ConfigObject` 删占位（同 atom §5.1）。

---

## 6. 关联段 → `## 边`（compound 关键差异）

compound 旧 `## 关联` 段**逐行解析**，按行首标签分流：可解析的 Task↔Task 关系提取成边，跨层/未迁/证据删。

| 旧关联行标签 | 处置 |
|---|---|
| `含 atom：[0-00019]、[0-00020]` | → `## 边` 多条 `- 含 atom: [[UDG@AtomTask@{cmd}]]`（每个 atom 一条）|
| `上游：[1-00002]` | → `- 上游: [[UDG@CompoundTask@{slug}]]` |
| `下游：[1-00002]` | → `- 下游: [[UDG@CompoundTask@{slug}]]` |
| `平行：[0-00072] / [1-...]` | → `- 平行: [[...]]`（0-→AtomTask，1-→CompoundTask）|
| `前置` / `前置任务：[1-...]` | → `- 上游: [[UDG@CompoundTask@{slug}]]` |
| `被引用于：[2-00001] · [BWM-CS](business/...)` | **删**（feature_task 未迁 / CS 跨层）|
| `证据：[...](evidence/...)` | **删** |
| `配置对象` / `命令 wiki` / `配套组` | **删** |

**提取规则（行首标签白名单，关键）**：只从 `含 atom / 上游 / 下游 / 平行 / 前置` 这 5 类标签行提取边；**白名单外的所有标签**（含但不限于 `配套 / 配套组 / 父特性 / 被依赖特性 / C-U 对应 / 命令 wiki / 被引用于 / 证据 / 配置对象`）**整行删、不扫号提取**（否则会把"被引用于/配套"里的编号误建成边、或产生自指向）。
- 同行的 `0-XXXXX` → `[[UDG@AtomTask@{cmd}]]`、`1-XXXXX` → `[[UDG@CompoundTask@{slug}]]`，**边类型由行标签定**（不固定 `0-`→含 atom：如"上游"行里的 atom 是**上游 atom**，不是含 atom）。
- `含 atom` 行只扫 `0-`（不扫 `1-`）。

新文件末尾 `## 边`（多条，去重；含 atom 在前，其次上游/下游/平行）：
```
## 边
- 含 atom: [[UDG@AtomTask@ADD BWMUSERGROUP]]
- 含 atom: [[UDG@AtomTask@ADD BWMRULE]]
- 含 atom: [[UDG@AtomTask@ADD APNBINDBWMUSRG]]
- 上游: [[UDG@CompoundTask@bwm-service-controller]]
```

> 若某 compound 关联段没有任何可解析边（如只有被引用于+证据），则 `## 边` 段为空（只写 `## 边` 标题，无条目）——属正常，该 compound 在本批无 Task↔Task 关系。

---

## 7. 校验清单（每个 compound 迁移完自检）

- [ ] 输出路径 = `三层图谱资产/CompoundTask/UDG/20.15.2/UDG@CompoundTask@{slug}.md`
- [ ] YAML 7 字段齐全且顺序：id/type/name/name_zh/nf/version/status（**无 ref**）
- [ ] `id` = `UDG@CompoundTask@{slug}`，三段式，无 version 无编号
- [ ] `name` = slug；`name_zh` = 旧 `task_logical_name`
- [ ] 正文段保留：H1 / 引子 / `## 配置方法` / `## 决策点`（若有）/ `## 约束`（若有）/ `## 场景差异`（若有）
- [ ] **全文无 `1-XXXXX` 编号残留**（id、链接都已转 slug）
- [ ] **无 `DP 0-`、`rule-0-`、`source_evidence`、`configobject/`、`evidence/`、`@20.15.2@`、`task_layer`、`task_intent`、`ref:` 残留**
- [ ] `## 边` 只含 `含 atom / 上游 / 下游 / 平行`，**无被引用于/证据/配置对象残留**
- [ ] 所有引用是 `[[...]]` 双方括号，无 markdown 相对路径 `[..](..md)` 残留（feature_task/CS 例外：删链接留文字）

> 最快核验：产出文件搜 `1-\d{5}(?![a-zA-Z0-9])`、`DP 0-`、`rule-0-`、`evidence`、`configobject`、`source_evidence`、`@20.15.2@`、`task_layer`、`task_intent`、`ref:`、`## 关联`、`(evidence/`、`(configobject/`，应全零命中。

---

## 8. 完整范例（before → after）

**样本：`1-00003` BWM 用户组、规则与绑定** → slug `bwm-usergroup-rule-bind`。

### 8.1 旧（节选）
```yaml
id: UDG@20.15.2@Task@1-00003
type: Task
task_layer: compound
task_logical_name: BWM 用户组、规则与绑定
ref: null
task_intent: 配置 BWM 用户组与规则...绑定到接入域并刷新生效
status: draft
---
# BWM 用户组、规则与绑定
> ...承接 [1-00002](task/UDG/20.15.2/1-00002.md) 的控制器/业务...归属特性 [2-00001](task/UDG/20.15.2/2-00001.md)。
## 配置方法
...（步骤表，含 [1-00005](task/.../1-00005.md)、[0-00289](task/.../0-00289.md)）...
## 决策点
...（联动 [1-00002] / [2-00001]）...
## 约束
- ...（critical，rule-0-00XXX）...
## 关联
- 上游：[1-00002](task/.../1-00002.md)（业务与控制器）
- 含 atom：[0-00033](...)、[0-00037](...)、[0-00035](...)、[0-00106](...)、[0-00015](...)
- 被引用于：[2-00001](...) · [BWM-CS](business/...) · ...
- 证据：[...](evidence/...)
```

### 8.2 新
```yaml
---
id: "UDG@CompoundTask@bwm-usergroup-rule-bind"
type: "CompoundTask"
name: "bwm-usergroup-rule-bind"
name_zh: "BWM 用户组、规则与绑定"
nf: "UDG"
version: "20.15.2"
status: "draft"
---

# BWM 用户组、规则与绑定

> ...承接 [[UDG@CompoundTask@bwm-service-controller]] 的控制器/业务...归属特性 2-00001。

## 配置方法
...（步骤表原样；[1-00005]→[[UDG@CompoundTask@slice-bind]]；[0-00289]→[[UDG@AtomTask@ADD BWMRULEGLOBAL]]）...

## 决策点
...（联动 [[UDG@CompoundTask@bwm-service-controller]] / 2-00001[留文字]）...

## 约束
- ...（critical）...

## 边
- 含 atom: [[UDG@AtomTask@ADD BWMUSERGROUP]]
- 含 atom: [[UDG@AtomTask@ADD BWMRULE]]
- 含 atom: [[UDG@AtomTask@ADD APNBINDBWMUSRG]]
- 含 atom: [[UDG@AtomTask@SET BANDWIDTHMNG]]
- 含 atom: [[UDG@AtomTask@SET REFRESHSRV]]
- 上游: [[UDG@CompoundTask@bwm-service-controller]]
```

**要点**：关联段"含 atom"5 条 → 5 条边；"上游"1 条 → 1 条边；"被引用于/证据"删；feature_task `2-00001` 删链接留文字。

---

## 9. 批量执行

脚本 `task/scripts/migrate_old_compounds.py`（仿 `migrate_old_atoms.py`），内置 SLUG_MAP（附录 A）。命令：
```
python migrate_old_compounds.py                 # 全量 UDG
python migrate_old_compounds.py 1-00003.md      # 单个 dry-run
```

---

## 附录 A：compound 编号 → slug 映射表（34 条，定稿）

```
1-00001 -> license-access-prep
1-00002 -> bwm-service-controller
1-00003 -> bwm-usergroup-rule-bind
1-00004 -> pcc-predefined-rule-chain
1-00005 -> slice-bind
1-00006 -> timerange-control
1-00007 -> icap-server-interconnect
1-00008 -> cf-content-filter
1-00009 -> filter-chain
1-00010 -> charging-core-trio
1-00011 -> rule-userprofile-bind
1-00012 -> charging-tail
1-00013 -> header-enrich
1-00014 -> ipfarm-redirect-chain
1-00015 -> smart-redirect-action-chain
1-00016 -> sa-protocol-identify-chain
1-00017 -> qos-dedicated-bearer-chain
1-00018 -> session-addr-alloc
1-00019 -> session-pcc-policy
1-00020 -> session-n4-interface
1-00021 -> addr-alloc-rule
1-00022 -> addr-pool-hierarchy
1-00023 -> smf-addr-alloc-mode
1-00024 -> downlink-route-export
1-00025 -> dualstack-apn-poolgroup
1-00026 -> ipv6-bearer-ospfv3-wlr
1-00027 -> ipv6-bearer-infra
1-00028 -> ipv6pd-prefix-flag
1-00029 -> apn-access-infra
1-00030 -> mpls-vpn-infra
1-00031 -> gre-redundancy-master-standby
1-00032 -> gre-tunnel-setup
1-00033 -> ipsec-tunnel-setup
1-00034 -> l2tp-lns-setup
```

> atom 编号→命令名映射（关联段"含 atom"、正文 `0-` 引用反查用）：由 `assets/task/UDG/20.15.2/0-*.md` 各文件 ref 字段现场读出（同 atom 迁移）。
