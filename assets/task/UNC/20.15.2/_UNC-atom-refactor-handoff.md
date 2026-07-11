# UNC Atom 重构 Agent 交接文档（两阶段）

> 用途：将 UDG 端 27 条 APN-1 atom 全闭环的实战工作流，平移到 UNC 端。
> 写给接手的 Agent：照本文 + 配套 SOP + 实战脚本，**两阶段** 完成 UNC atom 重构与 APN 域扩展。
> 写于：2026-07-11，由已完成 UDG APN-1（27 条 0-00298~0-00324 全闭环）的 Agent 出品。

---

## 0. 起点状态（接手时基线）

| 项 | 当前值 | 备注 |
|---|---|---|
| UNC `_numbering.json` 总数 | **212** | 0-00001 ~ 0-00212 |
| UNC atom md 数量 | 212 | 与 numbering 对齐 |
| UNC atom 现状模板 | **旧式**（`status: evidence_only` / 无 4 章节结构 / 无 DP/rule 编号化）| 参 `assets/task/UNC/20.15.2/0-00001.md`（证据式 + 表格 + 无 DP/rule 段） |
| UNC command-summary 数量 | **687** | `assets/_intermediates/command-summary/UNC/20.15.2/` + `_no-hit.txt` 6033 条 |
| UNC command wiki | 8499 个 md | `assets/command/UNC/20.15.2/` 全量已建 |
| UNC 1-/2- task | 32 个（compound/feature）| 见 `assets/task/UNC/20.15.2/` 目录 |
| UNC tracker | **未建** | 与 UDG 同名 `_atom-refactor-tracker.md`，**需新建** |

---

## 1. 总体目标（两阶段）

| 阶段 | 范围 | 目标产物 | 触发条件 |
|---|---|---|---|
| **第一阶段** | UNC 现有 212 atom 重构 | 212 个 atom 全部按 SOP 升级为新模板（4 章节 + DP/rule 编号化 + status:draft + source_evidence_ids）| 起点即可启动 |
| **第二阶段** | APN 域 UNC 22 个特性 → UNC 命令筛选 → 构建 atom | 新增 UNC atom + 在 tracker 加新批次行 | 第一阶段收尾后启动（也可并行，但命令命名空间独立不会冲突） |

---

## 2. 必读 SOP（硬约束来源）

1. **`assets/task/命令级atom构建SOP.md`** —— **核心 SOP**（§5 frontmatter 7 字段 / §6 正文 4 章节 / §7 DP+rule 编号机制 / §8 关联段 4 项硬性 / §9 自检清单 / §2.3 evidence 三级分支决策树）
2. **`assets/task/特性步骤级构建SOP.md`** —— 上层（atom 之上的 compound/feature 准则，第二阶段不直接用，但反向链接 grep 会涉及 1-/2-）
3. **`assets/CLAUDE.md`** —— §5 ID/文件名规范、§7 自包含（evidence 拷到 assets/evidence/）、§9 边界（_intermediates/ 中间态不入 wiki 引用）
4. **`assets/task/UDG/20.15.2/_atom-refactor-tracker.md`** —— **模板参考**（批次风格、tracker 段落结构、实战教训沉淀格式）

---

## 3. UNC tracker 初始搭建

新建文件：`assets/task/UNC/20.15.2/_atom-refactor-tracker.md`

首版骨架（最小可用版，后续阶段追加）：

```markdown
# UNC atom 重构批次跟踪

> 范围：UNC 已有 atom 212 条，按编号 0-XXXXX 顺序分批（10 条/批）
> 状态：✅ 已重构 / ⏳ 待重构
> 已完成：[首阶段填入]

| 批次 | 范围 | 状态 | 完成日期 | 命令 |
|---|---|---|---|---|
| 批次1 | 0-00001 ~ 0-00010 | ⏳ 待重构 |  | （每行 10 条命令名） |
| ... | | | | |

## 重构简版模板
1. frontmatter 7 字段（id/type/task_layer/task_logical_name/ref/task_intent/status:draft）
2. 配置方法段：**配置方法字典**（按维度组织，每维度 1 表：取值+作用+配套参数），**不**逐特性罗列
3. 决策点段：`## 决策点：{名}（DP 0-XXXXX）`
4. 约束段：bullet `- **{名}**（{severity}，{rule_id}）：{约束} — {后果}`
5. 关联段：命令 wiki + 配置对象 + 配套组 atom + 被引用于

## 简化原则
- **不**做证据拷贝（引路径到 source_evidence_ids）
- **不**做精细自检（主 Agent 验证）
- **不**改 _numbering.json 已建编号
- 遇分歧以原始命令 md 为准
- 每条 50-100 行

## 进度
- （每阶段完成时追加）
```

---

## 4. 第一阶段：UNC 212 atom 重构（21 批 × 10 条）

### 4.1 批次划分

UNC 已有 212 atom 编号 0-00001~0-00212，分 21 批（每批 10 条 + 末批 12 条）。
- 批次1~21：每批 10 条
- 末批（批次22 或 批次21.2）：2 条

建议沿用 UDG APN-1 经验，**每批 4 个并行子 Agent**（每 Agent 2-3 条），主 Agent 独立验证。

### 4.2 子 Agent 提示词模板（**直接复用 UDG APN-1 子 Agent 提示词**，把路径/编号段位换 UNC 即可）

将 UDG APN-1 子 Agent 提示词中所有 `UDG` → `UNC`、`UDG@20.15.2` → `UNC@20.15.2`、`UDG 20.15.2` → `UNC 20.15.2`、`UDG特性指南` → `UNC特性指南`、路径 `assets/task/UDG/20.15.2/` → `assets/task/UNC/20.15.2/`、`assets/command/UDG/20.15.2/` → `assets/command/UNC/20.15.2/`、`assets/_intermediates/command-summary/UDG/20.15.2/` → `assets/_intermediates/command-summary/UNC/20.15.2/`。

UNC 原始产品文档根目录是 `output/UNC {ver} 产品文档(裸机容器) 05/`（带空格 + 括号 + 05 后缀），UNC 特性激活树是 `网络部署/特性部署/UNC特性指南/`（多一层 `网络部署/`，与 UDG 的 `特性部署/特性指南/UDG特性指南/` 不同），**子 Agent 写 command wiki 路径时务必用 UNC 的实际路径**。

### 4.3 关键差异（UNC vs UDG，**不能直接复制粘贴提示词**）

| 项 | UDG | UNC |
|---|---|---|
| 原始产品文档根 | `output/UDG_Product_Documentation_CH_{ver}/` | `output/UNC {ver} 产品文档(裸机容器) 05/` |
| 特性激活树 | `特性部署/特性指南/UDG特性指南/` | `网络部署/特性部署/UNC特性指南/` |
| 命令 wiki 路径前缀 | `assets/command/UDG/20.15.2/` | `assets/command/UNC/20.15.2/` |
| 汇总 md 路径前缀 | `assets/_intermediates/command-summary/UDG/20.15.2/` | `assets/_intermediates/command-summary/UNC/20.15.2/` |
| 现有 atom 数量 | 211 | **212** |
| **现有 atom 旧式模板** | 已全部升级为新 SOP 模板 | **仍是旧式**（evidence_only / 无 4 章节 / 无 DP/rule 编号）—— 第一阶段任务是**全部升级** |

> ⚠️ 第一阶段要做的是**改写（不是新建）**：212 个已有 atom 全部按 SOP §5/§6/§7/§8 重写。子 Agent 提示词应明确："读取现有 atom md → 按新 SOP 模板重写（不是新建）"。

### 4.4 UNC 212 atom 编号速查

```
批次  范围         命令数
1     0-00001~10  10
2     0-00011~20  10
3     0-00021~30  10
4     0-00031~40  10
5     0-00041~50  10
6     0-00051~60  10
7     0-00061~70  10
8     0-00071~80  10
9     0-00081~90  10
10    0-00091~100 10
11    0-00101~110 10
12    0-00111~120 10
13    0-00121~130 10
14    0-00131~140 10
15    0-00141~150 10
16    0-00151~160 10
17    0-00161~170 10
18    0-00171~180 10
19    0-00181~190 10
20    0-00191~200 10
21    0-00201~210 10
22    0-00211~212 2
合计              212
```

**具体每个编号对应的命令名**：读 `assets/task/UNC/20.15.2/_numbering.json`（已存在，键值对是命令名→编号）。

### 4.5 子 Agent 提示词范例（UNC 批次1 子批1，复用 UDG APN-1 子 Agent 1 的结构）

```markdown
你是 SFCGraph UNC atom 重构 Agent。**严格按命令级 SOP** (`D:\mywork\KnowledgeBase\SFCGraph\assets\task\命令级atom构建SOP.md`) **改写**以下 3 个 UNC atom task wiki（不是新建）。

## 输入材料（必读）
1. **SOP**：`assets/task/命令级atom构建SOP.md`（§5/§6/§7/§8 模板硬约束）
2. **tracker 模板参考**：`assets/task/UDG/20.15.2/0-00059.md`（4 章节 + status:draft 完整范本）
3. **UNC tracker**：`assets/task/UNC/20.15.2/_atom-refactor-tracker.md`（UNC 批次1 在最末）
4. **CLAUDE.md**：`assets/CLAUDE.md`
5. **现有 3 个 UNC atom**（**待改写**，非新建）：
   - `assets/task/UNC/20.15.2/0-00001.md`（ADD URR）
   - `assets/task/UNC/20.15.2/0-00002.md`（ADD ADCPARA）
   - `assets/task/UNC/20.15.2/0-00003.md`（ADD AMUEPLCYCTRL）
6. **命令 wiki（权威源）**：
   - `assets/command/UNC/20.15.2/ADD-URR.md`
   - `assets/command/UNC/20.15.2/ADD-ADCPARA.md`
   - `assets/command/UNC/20.15.2/ADD-AMUEPLCYCTRL.md`
7. **汇总 md（SOP 主线证据）**：
   - `assets/_intermediates/command-summary/UNC/20.15.2/ADD-URR.md`
   - `assets/_intermediates/command-summary/UNC/20.15.2/ADD-ADCPARA.md`
   - `assets/_intermediates/command-summary/UNC/20.15.2/ADD-AMUEPLCYCTRL.md`

## 改写 3 个 atom（编号固定，不动 _numbering.json）

| 编号 | 命令 | summary? |
|---|---|---|
| 0-00001 | ADD URR | 有 |
| 0-00002 | ADD ADCPARA | （查 _no-hit.txt 或确认） |
| 0-00003 | ADD AMUEPLCYCTRL | （同上） |

## 必须遵守的硬约束
（同 UDG APN-1 子 Agent 提示词，全文照抄——frontmatter 7 字段 + status:draft + task_intent 单引号 + 4 章节 + rule_id 防撞号 + 关联段 4 项硬性 + source_evidence_ids 不指 _intermediates/）

## 与 UDG 重构的关键差异
1. UNC **原始命令 md** 路径用 `output/UNC 20.15.2 产品文档(裸机容器) 05/...`（UDG 是 `output/UDG_Product_Documentation_CH_20.15.2/...`）
2. UNC **特性激活 md** 树是 `网络部署/特性部署/UNC特性指南/`（UDG 是 `特性部署/特性指南/UDG特性指南/`）
3. **改写而非新建**：现有 212 atom 是旧式 `status: evidence_only` 模板，需整篇重写为新模板

## 工序
1. 读现有 3 个 atom md + 命令 wiki + 汇总 md
2. **整篇改写**（保留前文主线，套新模板 4 章节）
3. 检查 `_numbering.json` 编号（**不动**，原编号保留）
4. rule_id 防撞号（先 grep 全 UNC task 目录现有 rule_id 段位）
5. 写 `assets/task/UNC/20.15.2/0-00001.md` 等 3 个文件（覆盖旧文件）
6. 更新 `index.md`（如有）

## 自检 / 报告
（同 UDG APN-1 子 Agent 提示词末尾）
```

> ⚠️ 关键改动：**输入材料第 5 项是"现有 atom md 待改写"** 而不是"待新建"；工序第 2 步是"整篇改写" 而不是"起草"；工序第 5 步是"覆盖旧文件" 而不是"新建"。其余完全复用 UDG 子 Agent 提示词。

### 4.6 第一阶段实战教训（必须吸取）

UDG APN-1 暴露的 4 个反复出现的问题，UNC 第一阶段务必预判：

1. **rule_id 撞号**：UNCG 已用 rule_id 段位必须**前置 grep**（`grep -h "rule-0-" assets/task/UNC/20.15.2/*.md | sort -u`）。UDG 子 Agent 3 自主发现 `0-00304` 撞号并改 `0-01304` 段位避让——这是好习惯，子 Agent 应主动复用。
2. **task_intent 含 `:` 触发 YAML 解析**：所有含 `(LOADMODE: LATEST/SPECIFIC)` `(SRCTYPE no_type/ip_address/if_name)` `(DP 0-XXXXX)` 的 task_intent 必须**单引号包整字段**。
3. **source_evidence_ids 不能指 `_intermediates/`**（CLAUDE.md §9 边界硬约束）：子 Agent 须把命令 wiki 的命令真相 + 特性激活 md 拷到 `assets/evidence/UNC/20.15.2/` 下，或指向 OM 原始路径（UNC 用 `output/UNC 20.15.2 产品文档(裸机容器) 05/...`）。
4. **旧模板有 `status: evidence_only`** —— 第一阶段必须改为 `status: draft`（SOP §5 硬约束）；UNC tracker 21 批记录应明确标"旧 evidence_only 模板升级为 draft"。

### 4.7 主 Agent 独立验证脚本（**每批 4 子 Agent 完成后必跑**）

```python
import yaml, json, os, re
from collections import Counter

# === 参数：当前批次文件列表（10 个）===
files = ['0-00001', '0-00002', '0-00003', ..., '0-00010']  # 按当前批改
base = 'assets/task/UNC/20.15.2'

print(f'{"ID":<8} {"YAML":<5} {"4ch":<4} {"draft":<5} {"ref":<4} {"bad_evi"}')
print('-'*60)
all_rules = []
for f in files:
    path = f'{base}/{f}.md'
    if not os.path.exists(path):
        print(f'{f}  MISSING'); continue
    with open(path, encoding='utf-8') as fh: content = fh.read()
    parts = content.split('---', 2)
    try:
        fm = yaml.safe_load(parts[1])
    except Exception as e:
        print(f'{f}  YAML FAIL: {e}'); continue
    sections = content.count('\n## ')
    ref_ok = 'MMLCommand@' in (fm.get('ref') or '')
    draft_ok = fm.get('status') == 'draft'
    # evidence 审计
    ev_match = re.search(r'source_evidence_ids:\s*\n((?:\s*-\s*.+\n?)+)', parts[1])
    bad_ev = 0
    if ev_match:
        evs = [l.strip().lstrip('-').strip() for l in ev_match.group(1).splitlines() if l.strip().startswith('-')]
        bad_ev = sum(1 for e in evs if '_intermediates' in e)
    print(f'{f}  Y     {sections}     {"Y" if draft_ok else "N"}    {"Y" if ref_ok else "N"}    {bad_ev}')
    rules = re.findall(r'rule-(0-\d+)', content)
    for r in rules: all_rules.append((f, r))

# rule_id 唯一性检查
c = Counter(r for _, r in all_rules)
dups = {r: n for r, n in c.items() if n > 1}
print(f'\nRules total={len(all_rules)}, unique={len(c)}, dups={dups if dups else "none"}')
```

跑完无 dups + bad_evi=0 + 4ch=4 + draft=Y 即该批通过。**任何一项不通过 → 该批打回子 Agent 重做**。

---

## 5. 第二阶段：APN 域 UNC 22 个特性 → 命令筛选 → atom 构建

### 5.1 流程（**完全复用 UDG APN-1 经验**）

#### Step 1: 筛选 UNC APN 22 个特性的所有命令

```python
import json, os
import re

with open('assets/task/UNC/20.15.2/_numbering.json') as f:
    num = json.load(f)

# 读 22 个 UNC APN feature knowledge md
apn_unc_dir = '业务图谱体系/APN业务域/feature-knowledge'
apn_unc_features = [f for f in os.listdir(apn_unc_dir) if f.startswith('WSFD-')]

# 提取命令名（粗粒度：粗体 VERB NAME 模式）
config_ops = ['ADD', 'MOD', 'SET', 'STR', 'STP', 'EXP', 'ACT', 'RMV']
all_cmds = set()
for f in apn_unc_features:
    p = os.path.join(apn_unc_dir, f)
    with open(p, encoding='utf-8') as fh:
        content = fh.read()
    cmds = set()
    # 模式 1: **CMD NAME** 粗体
    for m in re.finditer(r'\*\*([A-Z]{2,5} [A-Z][A-Z0-9]+)\*\*', content):
        cmds.add(m.group(1))
    # 模式 2: `CMD: ...;` 任务示例
    for m in re.finditer(r'`([A-Z]{2,5} [A-Z][A-Z0-9]+):', content):
        cmds.add(m.group(1))
    all_cmds |= cmds

# 过滤：只保留配置类 + UNC 命令真实存在
apn_cfg = sorted([c for c in all_cmds if c.split()[0] in config_ops])

# 校验 UNC 命令是否真实存在
real_cmds = []
fake_cmds = []
for cmd in apn_cfg:
    fn = f'assets/command/UNC/20.15.2/{cmd.replace(" ", "-")}.md'
    if os.path.exists(fn):
        real_cmds.append(cmd)
    else:
        fake_cmds.append(cmd)

print(f'APN UNC 真实命令 {len(real_cmds)} 条（剔除字面提及 {len(fake_cmds)} 条）：')
for c in real_cmds: print(f'  {c}')
print('\n剔除（字面提及/非UNC）：')
for c in fake_cmds: print(f'  {c}')
```

#### Step 2: 拆已建/未建

```python
built = [(cmd, num[cmd]) for cmd in real_cmds if cmd in num]
not_built = [cmd for cmd in real_cmds if cmd not in num]

print(f'已建: {len(built)} 条')
for cmd, no in built:
    md = 'Y' if os.path.exists(f'assets/task/UNC/20.15.2/{no}.md') else 'N'
    print(f'  {no} [{md}] {cmd}')

print(f'\n未建: {len(not_built)} 条')
for c in not_built: print(f'  {c}')
```

#### Step 3: 过滤 ADD/SET（UDG 经验：优先 ADD/SET，MOD/RMV/EXP/STR/STP 放下一批）

```python
add_set = [c for c in not_built if c.startswith('ADD ') or c.startswith('SET ')]
print(f'新增 ADD+SET: {len(add_set)} 条')
```

#### Step 4: 预分配编号 + 批次划分（10 条/批）

```python
nums = sorted(int(v.split('-')[1]) for v in num.values() if v.startswith('0-'))
mx = nums[-1]
print(f'当前 max: 0-{mx:05d}, next: 0-{mx+1:05d}')

start = mx + 1
batches = [add_set[i:i+10] for i in range(0, len(add_set), 10)]
for bi, b in enumerate(batches, 1):
    print(f'APN-1.{bi} ({len(b)} 条) 编号 0-{start:05d}~0-{start+len(b)-1:05d}:')
    for c in b:
        print(f'  0-{start:05d} {c}')
        start += 1
```

#### Step 5: 在 UNC tracker 追加新批次行（**完全复用 UDG tracker 风格**）

```markdown
| **批次APN-1.1** | **0-XXXXX ~ 0-YYYYY（10 条）** | ⏳ 待重构 | 2026-07-XX | **APN域·UNC 第 1 批 10 条 ADD/SET**（命令名 1、命令名 2、...） |
| ... | | | | |
```

#### Step 6: 并行子 Agent 构建（**完全复用 UDG APN-1 子 Agent 提示词**，把路径改 UNC 即可）

- 每批 4 个子 Agent，每 Agent 2-3 条
- 主 Agent 用 §4.7 独立验证脚本验证

### 5.2 UNC APN 第二阶段的预期命令范围（参考）

UNC APN 22 个特性可能涉及 80-150 条命令（UDG APN 14 特性涉及 165 条，UNC 22 特性按比例更多），其中：
- **已建（_numbering.json 有登记）**：估计 70-100 条（UNC 在计费/PCC/SA 等业务域已建过）
- **未建（新增）**：估计 30-60 条（主要 APN 域特有：DHCP/Radius/UPF选择/多PDN-PDU 等）

按 UDG 经验，**优先 ADD/SET**，MOD/RMV/EXP/STR/STP 放第三阶段。

---

## 6. 与 UDG APN-1 的差异汇总（执行者必读）

| 维度 | UDG APN-1（已完成） | UNC 第一阶段 | UNC 第二阶段 |
|---|---|---|---|
| 操作类型 | **新建** 27 条 atom | **改写** 212 条旧式 atom → 新 SOP 模板 | **新建** ~30-60 条 atom |
| 旧式 atom 现状 | 已全部升级 | 仍是 `status: evidence_only` 旧式 | （前阶段升级完成后）已是新式 |
| 路径前缀 | `assets/task/UDG/20.15.2/` 等 | `assets/task/UNC/20.15.2/` 等 | 同左 |
| 原始产品文档根 | `output/UDG_Product_Documentation_CH_20.15.2/` | `output/UNC 20.15.2 产品文档(裸机容器) 05/` | 同左 |
| 特性激活树 | `特性部署/特性指南/UDG特性指南/` | `网络部署/特性部署/UNC特性指南/` | 同左 |
| tracker 文件 | 已存在（55 行）| **需新建** | 已有 |
| 编号空间 | 0-00298~0-00324 | 0-00001~0-00212 不动 | 接续 0-00213~（若第一阶段后 _numbering 没新增）或后续批次 |
| 子 Agent 数 / 批 | 4（每 2-3 条）| 4（每 2-3 条）| 4（每 2-3 条） |
| 子 Agent 提示词结构 | 完整 SOP 引用 + 路径 + 工序 + 自检 | **改写**而非新建；其余同左 | **新建**（同 UDG APN-1 子 Agent 提示词结构） |
| 主 Agent 验证脚本 | §4.7 同一脚本 | 同脚本 + 加"4 章节齐 + draft=Y" + 旧 `evidence_only` 改 `draft` 检查 | 同 UDG APN-1 验证脚本 |

---

## 7. 实战工作流（按时间顺序）

```
Day 1
├── 上午：建 UNC tracker 首版（§3）
├── 上午：UNC 批次1~5（0-00001~0-00050，5 批 50 条）首批子 Agent 启动
├── 下午：UNC 批次1~5 独立验证 + 修正
└── 下午：UNC 批次6~10（0-00051~0-00100，5 批 50 条）

Day 2
├── 上午：UNC 批次11~15（0-00101~0-00150，5 批 50 条）
├── 下午：UNC 批次16~21（0-00151~0-00210，6 批 60 条）
└── 下午：UNC 批次22（0-00211~0-00212，2 条收尾）

Day 3
├── 上午：第一阶段完结报告（212/212 全闭环）
└── 下午：第二阶段启动——UNC APN 22 特性命令筛选（§5.1 step 1-4）

Day 4+
├── UNC APN 新增 atom 批次构建（每批 4 子 Agent）
└── 每批独立验证 + tracker 进度更新
```

---

## 8. 关键产出（最终交接给用户）

1. **UNC tracker** `assets/task/UNC/20.15.2/_atom-refactor-tracker.md`：含 22 个批次行（第一阶段）+ N 个 APN 批次行（第二阶段）
2. **212 个改写后 atom md**（第一阶段）+ **~30-60 个新建 atom md**（第二阶段）
3. **进度总结**：每批报告 + 最终总报告（212 + APN 新增数）

---

## 9. 接手 Agent 启动检查清单

接手时务必**先跑完以下 4 步**，确认环境就绪：

- [ ] Step 1: 读 `assets/command/UNC/20.15.2/` 至少 3 个命令 wiki（例 ADD URR / ADD ADCPARA / ADD APN），确认 UNC 命令 wiki 格式与 UDG 一致
- [ ] Step 2: 读 `assets/_intermediates/command-summary/UNC/20.15.2/ADD-URR.md` 至少 1 个，确认汇总 md 格式（4 段：命令真相 + 各特性配置范式 + 配置方法差异汇总 + 数据源）
- [ ] Step 3: 读 `assets/task/UNC/20.15.2/0-00001.md` 现有 atom，确认旧式模板（status:evidence_only + 无 4 章节）
- [ ] Step 4: 跑 §4.7 验证脚本 1 次（先用文件列表占位 `[0-00001]`），确认 Python 环境正常

完成 4 步后，正式启动第一阶段批次 1。

---

## 10. 实战教训沉淀（写进 UNC tracker 的"进度"段）

接手的 Agent 务必把以下 UDG APN-1 的实战教训**复制进 UNC tracker 的"进度"段**：

1. **rule_id 撞号必须前置 grep**：`grep -h "rule-0-" assets/task/UNC/20.15.2/*.md | sort -u` 拿到所有已用段位；新 rule_id 用 0-XXXXX 直接续位，撞号时**主动避让**到 0-01XXX 段位（UDG 实战：0-00304/305/306/314 → 0-01304/01305/01306/01314）
2. **task_intent 单引号**：含 `:` 的整字段必须单引号包（最常见：枚举值的 `:`，如 `LOADMODE: LATEST/SPECIFIC`、`SRCTYPE no_type/ip_address/if_name`）
3. **source_evidence_ids 不指 `_intermediates/`**：必须拷到 `assets/evidence/UNC/20.15.2/` 或指向 UNC 原始 OM 路径（`output/UNC 20.15.2 产品文档(裸机容器) 05/...`）
4. **status: draft 不可降级**：旧式 `evidence_only` 是 UNC 第一阶段必须**改写**的对象；**绝不允许**新 atom 沿用 evidence_only
5. **4 子 Agent 并行是甜区**：每 Agent 2-3 条 atom 是 UDG 实战最稳的并行度（4 个 Agent 并发，2-3 条各，wall-clock 与 1 个 Agent 单跑 10 条相近，但主 Agent 验证负担按 Agent 数翻倍——4 是验证负担与并行收益的平衡点）
6. **主 Agent 验证不可省**：UDG 实战多次发现子 Agent 报"OK"但实际少写章节（如漏关联段 4 项硬性）；§4.7 脚本每批必跑

---

**祝顺利。接手遇到歧义，以 SOP + UDG APN-1 实际产物为锚。**