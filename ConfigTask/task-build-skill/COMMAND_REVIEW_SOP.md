# 命令级审查标准 SOP（COMMAND_REVIEW_SOP）

> 版本：v1（2026-07-02 定稿，基于 UDG@20.15.2 全量 187 命令实战审查闭环验证）
> 对象：任意 NF@version 的命令层 atom（`task-0-*.yaml`）+ 每个 atom 挂的 TaskRule / DecisionPoint
> 性质：**校准/重构**（把已有 atom + 其 rule + DP 改对），不是新建
> 权威依据：`改进后三层图谱定义.md` §4-§8 + `SKILL.md` + 本目录 `COMMAND_REVIEW_BASELINE.md`

---

## 0. 前置条件

| 条件 | 说明 |
|---|---|
| **atom 已全量存在** | 每条配置类命令（ADD/SET/MOD/DEL）已有对应 atom yaml；查询类（DSP/LST）不建 atom |
| **mml_commands.jsonl 可用** | `CommandGraph/data/assets/{nf}/{version}/mml_commands.jsonl` 含每命令的 `parameter_description`+`notes`+`source_evidence_ids` |
| **特性激活 md 可达** | `output/{产品文档}/特性部署/特性指南/{nf}特性指南/` 下各特性的激活/配置 md |
| **feature-graph CSV 可达** | `FeatureGraph/data/legacy/{nf}_feature_files.csv` 含 feature_id → md 路径映射 |
| **index.json 已生成** | `task-assets/{nf}/{version}/index.json` 含 `atom_usage`（命令→特性反查）|

---

## 1. 全流程总览（5 阶段）

```
阶段 A 预处理：运行 2 个脚本，产出审查索引 + 结构化证据包
    ↓
阶段 B 批次规划：按命令功能域分批，确定每批命令清单 + Agent 分组 + ID 段
    ↓
阶段 C 并行审查：每 Agent 读证据包 → 按 §4 清单审 → 改 atom/rule/DP yaml
    ↓
阶段 D 主控复验：全量 dangling/dup 检查 + 重建 index + 缺口收敛
    ↓
阶段 E 收尾：审查日志追加 + 重建证据包（反映改动）+ 遗漏扫描
```

---

## 2. 阶段 A：预处理（产出证据包）

### 2.1 工具 1：审查索引

**脚本**：`task-build-skill/scripts/build_command_review_index.py`
**用法**：`python build_command_review_index.py [nf] [version]`（默认 UDG 20.15.2）
**产物**：`task-assets/{nf}/{version}/command-review-index.json`

每 atom 一张"审查卡"（JSON key = atom 短 id）：
- `command_name` / `command_name_zh` / `original_md`（原始 md 路径，来自 mml_commands.jsonl 的 `source_evidence_ids`）
- `command_notes`（命令规格 notes → 应投影 atom rule）
- `atom_owned_rules` / `atom_owned_dps`（当前 atom 挂的 rule/DP）
- `bound_params`（atom 已绑参数列表）
- `truth_params`（从 mml_commands.jsonl `parameter_description` 精确正则解析：`data_source` / `requiredness` / `value_range` / `default`）
- `missing_params_in_atom`（命令真相有、atom 未绑的参数 = 缺口）
- `feature_evidence`（用该命令的特性清单 + 其激活 md 路径）

> **用途**：批次规划（按 `command_name` 功能域聚合、按 `missing_params_in_atom` 长度排优先级）、统计（缺口收敛追踪）。

### 2.2 工具 2：结构化证据包 ★

**脚本**：`task-build-skill/scripts/build_command_evidence.py`
**用法**：`python build_command_evidence.py [nf] [version] [--only {atom短id}]`
**产物**：`task-assets/{nf}/{version}/command-evidence/{atom短id}.md`（每命令一个 MD 文件）

**证据包 = 一个命令的全部审查资料，含两部分**：

#### Part A：代码组织的上下文（Agent 直接审）
- **① atom + atom-挂 rule/DP**：完整 yaml 原文（agent 无需另开文件）
- **② 命令真相**：功能 / notes（规格上限/唯一性 → 应投影 rule）/ 参数真相表（精确解析：数据来源/必选/取值范围/默认值）
- **③ 各特性的配置范式**（代码从激活 md 抽取，精确词边界匹配命令名，不误带子串如 ADD URR 误匹配 ADD URRGROUP）：
  - 数据规划表中**该命令的参数行**（参数名 / 取值样例 / 获取方法 / 说明）
  - 任务示例脚本中**该命令的代码行**（`ADD URR:URRNAME=..., URRID=...`）
  - 操作步骤中**该命令的 ±2 行上下文**（原始 md 摘录）
- **④ 自动比对**：已绑参数 vs 命令真相 vs 缺口 + 跨特性"获取方法"分布（若多值 → 提示升 decision_driven）

#### Part B：原始 md 片段
- ③ 的步骤上下文/脚本原文 = 原始 md 摘录（Agent 可直接读）
- ② 的参数表 = 命令原始 md 的结构化产物（来自 mml_commands.jsonl）
- 顶部记录原始命令 md 全路径（需深查时直接读 `output/.../OM参考/命令/.../<命令>.md`）

> **关键价值**：证据包把"代码读 md + 抽上下文 + 结构化比对"一次性做完。审查 Agent 读一个 MD 文件即可完成审查，**无需逐个翻特性激活 md**。

### 2.3 运行顺序
```bash
cd ConfigTask/task-build-skill/scripts
python build_command_review_index.py UDG 20.15.2    # 先建索引（快）
python build_command_evidence.py UDG 20.15.2         # 再建证据包（慢，需读所有激活 md）
```

---

## 3. 阶段 B：批次规划

### 3.1 分批原则
- 按**命令功能域**分批（语义连贯，便于同族参数跨命令对齐）
- 每批 ~15-25 命令，3 并行 Agent（用户上限），每 Agent ~5-8 命令
- 大域（如路由 41 命令）拆成子批（C3a 核心 + C3b 进阶）

### 3.2 ID 段分配协议（防冲突 ★）
**每次派 Agent 前**：主控 grep 当前 max rule_id / dp_id，给每个 Agent 分配**不重叠的 ID 安全段**：
```bash
# 查 max
python -c "import glob,yaml; rs=[int(yaml.safe_load(open(f,encoding='utf-8')).get('rule_id','0-0').split('-')[-1]) for f in glob.glob('task_rules/*.yaml')]; ds=[int(yaml.safe_load(open(f,encoding='utf-8')).get('decision_id','0-0').split('-')[-1]) for f in glob.glob('decision_points/*.yaml')]; print(f'max rule=0-{max(rs):05d} max dp=0-{max(ds):05d}')"
```
分配示例（假设当前 max rule=0-00318, max dp=0-00121）：
- Agent 1：rule 0-00325~0-00344, DP 0-00122~0-00135
- Agent 2：rule 0-00345~0-00364, DP 0-00136~0-00149
- Agent 3：rule 0-00365~0-00384, DP 0-00150~0-00163

> **实战教训**：Agent 段不隔离会导致重复 ID / 覆盖冲突。C3b 曾因 DP 0-00094/095 与既有 UNC rule ID 冲突。

### 3.3 Agent Brief 模板
每个 Agent 的指令含：
1. **硬约束**（可写边界 / 只动分配的 atom / 不新建 atom·compound / atom ref·parameter_ref ID 不改 / 仅本 NF）
2. **命令清单**（atom 短 ID + 命令名 + 缺口数 + 所属域提示）
3. **输入说明**（读证据包 + 实际 yaml + 原始 md 按需）
4. **审查清单**（§4 四条，逐条过）
5. **修改动作**（改 atom bindings + 改/补 rule·DP + 独占 ID 段 + status→inferred + notes 追加日期标记）
6. **自验要求**（bindings 与②③一致 / rule·DP 投影完整 / 0 dangling / ID 段唯一 / 一命令一 atom）
7. **汇报格式**（逐命令：补绑依据/修 binding/补 rule·DP/分叉处理 + rule/dp ID 段）

---

## 4. 阶段 C：单命令审查清单（核心）

### 4.1 参数完整度
- [ ] 证据包④的 `missing_params_in_atom` 逐个判：
  - 命令真相标 **必选** → 绑
  - 在某特性数据规划表(③)里**出现**（实际用到）→ 绑
  - 命令真相标可选 + 无特性用到（冷门）→ **不绑**（避免臃肿）
- **门槛（已锁定）**：只绑"通用配置"参数（用到或必选），不追全量

### 4.2 参数准确性
- [ ] `variable_source`：对齐命令真相②的 `data_source`（全网→global_planned / 本端→local_planned / 对端→peer_planned / 已配置→reference）。证据包③各特性的"获取方法"列如有**多值分叉** → 升 `decision_driven`
- [ ] `requiredness`：对齐命令真相②的 `requiredness`（required / optional / conditional）
- [ ] `binding_type` + `value`：固定值 fixed+value；余 variable；受决策 decision_driven+decision_ref
- [ ] `decision_driven` binding：`decision_ref` 指向的 DP **存在**，且其 options 覆盖该参数取值

### 4.3 rule/DP 投影
- [ ] 命令 `notes`②的规格/上限/唯一性 → 是否投影成 atom-挂 rule（`cardinality_rule` / `uniqueness_rule`）？漏的补
- [ ] 命令 conditional_required（"前提条件X时必选"）→ 是否投影成 atom-挂 DP？漏的补
- [ ] 现有 atom-挂 rule/DP 内容对齐命令真相（无臆造/过期）

### 4.4 证据与一致性
- [ ] atom `source_evidence_ids` 覆盖该命令主要用法（非只有建 atom 时的那一个特性 md）
- [ ] 跨特性配法分叉已用 DP/decision_driven 表达，未硬编码单一取值
- [ ] 证据包④的"获取方法分布"若提示多值 → 核实是否该升 decision_driven

---

## 5. 阶段 D：主控复验（每批末）

### 5.1 全量 dangling/dup 检查
```python
# 检查所有 rule/dp owner_task_ref、atom decision_ref、source_ref 无 dangling + ID 唯一
python -c "
import glob,yaml,collections
atoms={}; rules={}; dps={}; all_ids=set()
for f in glob.glob('tasks/task-*.yaml'):
    d=yaml.safe_load(open(f,encoding='utf-8'))
    if d and d.get('task_id'): all_ids.add(d['task_id'])
    if d and d.get('task_layer')=='atom': atoms[d['task_id']]=d
def ld(pat,key):
    m={}; dc=collections.Counter()
    for f in glob.glob(pat):
        d=yaml.safe_load(open(f,encoding='utf-8'))
        if d and d.get(key): m[d[key]]=d; dc[d[key]]+=1
    return m,[k for k,v in dc.items() if v>1]
rules,dup_r=ld('task_rules/*.yaml','rule_id')
dps,dup_d=ld('decision_points/*.yaml','decision_id')
dp_ids=set(dps)
do=sum(1 for r in rules.values() if r.get('owner_task_ref','') not in all_ids)
do+=sum(1 for d in dps.values() if d.get('owner_task_ref','') not in all_ids)
dd=sum(1 for a in atoms.values() for b in (a.get('parameter_bindings') or []) if b.get('decision_ref','') and b['decision_ref'] not in dp_ids)
print(f'rule={len(rules)} dp={len(dps)} dup_r={len(dup_r)} dup_d={len(dup_d)} dangling={do+dd}')
"
```
**验收**：`dup_r=0 dup_d=0 dangling=0`

### 5.2 重建索引 + 缺口收敛
```bash
python build_command_review_index.py UDG 20.15.2
# 查看该批命令的 missing_params 收敛情况
```

### 5.3 遗漏扫描（收尾必做 ★）
```python
# 扫描所有 atom：mtime 在今天之前 且 status!=inferred 的 = 未审遗漏
import glob,os,yaml,datetime as dt
today_0=dt.datetime.today().replace(hour=0,minute=0,second=0).timestamp()
for f in sorted(glob.glob('tasks/task-0-*.yaml')):
    mt=os.path.getmtime(f)
    d=yaml.safe_load(open(f,encoding='utf-8'))
    if mt<today_0 and d.get('status')!='inferred':
        print(f'⚠️ 遗漏: {d.get(\"task_id\",\"\").split(\"@\")[-1]} status={d.get(\"status\")} mtime={dt.datetime.fromtimestamp(mt).strftime(\"%Y-%m-%d\")}')
```
> **实战教训**：UDG C6 批次中 9 个 atom 被分配给 Agent 但因范围混淆遗漏跳过——只有遗漏扫描才发现。

---

## 6. 阶段 E：收尾

- [ ] 审查日志追加：`review/command-review-log.md`（每批一节：命令数/新建 rule·DP 数/核心演进债/累计进度）
- [ ] 重建证据包（`build_command_evidence.py`）反映改动后的 atom 状态（供下一轮/UNC 参考）
- [ ] 重建 `index.json`（`build_index.py`）
- [ ] 遗漏扫描通过（§5.3）

---

## 7. 审查单元定义

**一个命令 = 一个审查单元**，同步审视三件事（不割裂）：
1. **atom task**（`tasks/task-0-NNNNN.yaml`，含 `parameter_bindings`）
2. **atom 挂的 TaskRule**（`owner_task_ref = 该 atom`）
3. **atom 挂的 DecisionPoint**（`owner_task_ref = 该 atom`）

> **范围（已锁定）**：rule/DP 只看 `owner_task_ref = 该 atom`（不含 feature 挂的 dependency_rule）

---

## 8. 三输入对照表

| 输入 | 内容 | 来源 | 证据包对应段 |
|---|---|---|---|
| ① 已抽 yaml | atom + atom-挂 rule/DP | `tasks/task-0-*.yaml` + `task_rules/` + `decision_points/` | 证据包 §① |
| ② 命令证据 md | 各特性激活 md 里该命令的配置范式 | `output/.../激活*.md`（feature_evidence 给清单） | 证据包 §③ |
| ③ 命令原始 md + 参数真相 | 功能/参数表/notes/原始 md 路径 | `mml_commands.jsonl`（= 命令原始 md 的结构化产物） | 证据包 §② |

---

## 9. 批次划分参考（UDG 实战）

| 批 | 功能域 | 命令示例 | atom 数 |
|---|---|---|---|
| C1 | 计费/PCC | ADD URR, ADD RULE, ADD FILTER, SET REFRESHSRV | 18 |
| C2 | 接入/地址池/APN | ADD APN, ADD POOL, ADD SECTION, ADD VPNINST | 14 |
| C3a | 路由/接口核心 | ADD INTERFACE, ADD GRETUNNEL, ADD OSPF, SET BFD | 16 |
| C3b | 路由进阶 | ADD OSPFV3, SET BGP, ADD AUTOSCALINGSERVICE, ADD ROUTEPOLICY | 17 |
| C4 | QoS/ACL/BWM | ADD BWMCONTROLLER, ADD ACLRULEADV4, ADD QOSPROP | 25 |
| C5 | 业务感知/HTTP/过滤 | ADD REDIRAPPENDINFO, ADD CFTEMPLATE, LOD SIGNATUREDB | 11 |
| C6a-d | 网管/IPSec/eDRX/其他 | ADD IKEPEER, ADD TWAMPSENDER, SET IOTCAPABILITY, L2TP 族 | ~79 |

> 精确清单由 `command-review-index.json` 按 `command_name` 聚合 + `missing_params_in_atom` 优先排序。

---

## 10. 边界（硬约束）

- **可写**：仅 `ConfigTask/`
- **只读**：`改进后三层图谱定义.md`、`FeatureGraph/data/legacy/`、`CommandGraph/data/assets/`、`output/…产品文档…/`
- 不新建 atom（命令已全量存在）；不新建 compound/feature
- atom `ref` / `parameter_ref` 指向 CommandGraph 静态对象，**不改这些 ID**
- 命令真相以 `mml_commands.jsonl` + 命令原始 md 为准；特性用法以激活 md 为准
- 每命令审查独立可并行（atom 间无写冲突）；rule/DP 按 owner 归属，不跨 atom 改
- 新建 rule/DP 必须 `owner_task_ref = 该 atom`（不建 feature-level rule/DP）

---

## 11. 实战经验（UDG 全量审查总结）

### 11.1 核心演进债落地
- **跨特性分叉升 decision_driven**：30+ 处（RULE.POLICYTYPE / REFRESHSRV.REFRESHTYPE / INTERFACE.IFNAME / GRETUNNEL.REDUNDANCYEN / POOL.POOLTYPE / SECTION.IPVERSION / IPFARMGLOBAL.SERVERTYPE / BWMCONTROLLER 控制类型 / 等）
- **参数补绑**：USERPROFILE.CAPMODETHRES/DDOSCHECK/ALIASMARKFLAG、FILTER SVRIP/MSIP 组、ADD APN 双栈参数 HASVPNIPV6/VPNINSTANCEIPV6 等
- **rule 投影**：174+ 条 cardinality_rule/uniqueness_rule/dependency_rule（规格上限/唯一性/前置约束/安全高危）

### 11.2 常见陷阱
1. **ID 段不隔离** → 重复 ID/覆盖（C3b DP 0-00094/095 教训）→ 每批前 grep max + 分配不重叠段
2. **Agent 范围混淆** → 命令遗漏（C6 9 个 atom 被跳过）→ 收尾必做遗漏扫描
3. **API 错误中断** → Agent 零写入 → 重派即可（无半成品残留）
4. **聚合 atom**（多命令合一，如 SET BGP+ADD BGPVRF+ADD IMPORTROUTE）→ 本审查不拆，只审 binding + 标记债
5. **词边界匹配**：证据包抽取用 `\b` 正则精确匹配命令名（ADD URR 不误匹配 ADD URRGROUP）

### 11.3 统计（UDG@20.15.2 全量结果）
- atom 187 命令（175 个独立 yaml，含 12 个聚合债多命令合一）
- rule 98→281（+183）
- dp 39→80（+41）
- 0 dangling / 0 重复 ID（全量闭环验证）
- 10 批次（C1-C6 含 C3b/C6 拆子批），含 1 次重派（API 错误）+ 1 次补审（9 遗漏命令）
