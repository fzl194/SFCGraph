# 计费功能（跨特性）— 统一 Task 架构样板 v2

> 日期：2026-06-29
> 数据来源（全部真实）：
> - GWFD-020301 内容计费基本功能/部署UPF_28493406.md
> - GWFD-020300 在线计费/配置Gy接口在线计费_83167737.md（SET URRFAILACTION 第8步可选）
> - GWFD-010171 离线计费/配置Ga接口离线计费_31927856.md（SET URRFAILACTION 第6步可选）
> - GWFD-010173 融合计费/部署UPF_79654301.md
> 目的：用"计费功能"业务域（4 个计费特性）讲清 **父子 DecisionPoint 分开建 + 决策传播**

---

## 0. 为什么用计费功能（不只是内容计费）

单看内容计费基本功能，"计费方式（在线/离线）"只改 ADD URR 参数（参数级），看不出父子 DP。

把在线/离线/融合计费特性一并纳入后，出现一个**跨特性的大 task（计费功能业务域）**：它的"计费方式"决策是 **task 级**——决定纳入哪个计费特性的子 task（在线计费特性带 SET URRFAILACTION，离线计费特性也带，融合计费特性带融合相关）。

于是同一个"计费方式"决策在两层都有投影：
- **domain 层（大 task）**：task 级 —— adds 哪个计费特性的子 task
- **atom 层（ADD URR）**：参数级 —— USAGERPTMODE 取值

**两个 DP 分开建，靠决策传播联动。** 这就是本样板要讲清的。

---

## 1. 4 层 task 结构

task_layer 枚举扩展为 4 层（最大原子无上限）：

```
domain task    计费功能（跨4特性）
   ├─ feature task    内容计费基本功能 / 在线计费 / 离线计费 / 融合计费
   │     ├─ compound task    计费三件套 / 过滤链 / 规则绑定 / 收尾
   │     │     ├─ atom task    ADD URR / ADD URRGROUP / ... （1条命令）
```

### 1.1 atom task（命令级，4特性共享的积木库）

| task_id | logical_name | command_ref | 说明 |
|---|---|---|---|
| Task@00001 | 配置URR | ADD URR | **挂 DP-B 计费方式（参数级）** |
| Task@00002 | 配置URR组 | ADD URRGROUP | |
| Task@00003 | 配置PCC策略组 | ADD PCCPOLICYGRP | |
| Task@00004~00009 | 过滤器/流过滤器/绑定 | ADD FILTER/FILTERIPV6/L7FILTER/FLOWFILTER/FLTBINDFLOWF/PROTBINDFLOWF | |
| Task@00010 | 配置规则 | ADD RULE | |
| Task@00011/00012 | 用户模板/绑定 | ADD USERPROFILE/RULEBINDING | |
| Task@00013 | 配置缺省费率 | SET URRGRPBINDING | |
| Task@00014 | 防欺诈URR列表 | ADD SPECURRGRPLIST | 可选 |
| Task@00015 | 刷新生效 | SET REFRESHSRV | must_be_last |
| Task@00021 | 设置默认配额开关 | SET UPDEFAULTQUOTA | **在线计费可选** |
| Task@00022 | 设置Credit Pooling | SET UPGLBCHGPARA | **在线计费可选** |
| Task@00023 | 设置URR上报失败动作 | SET URRFAILACTION | **在线/离线计费可选** |

> Task@00021/22/23 是计费方式相关的可选命令——它们属于"积木库"，但**默认不进入任何特性的主路径**，由 domain 层 DP 的 option 决定是否 adds。

### 1.2 compound task（特性内步骤组合，4特性共享）

| task_id | logical_name | 编排 |
|---|---|---|
| Task@00101 | 计费三件套 | 00001→00002→00003 |
| Task@00102 | 过滤链 | 00004~00009 |
| Task@00103 | 规则与用户模板绑定 | 00010→00011→00012 |
| Task@00104 | 缺省费率与刷新 | 00013→00014(可选)→00015 |

### 1.3 feature task（单个计费特性）

| task_id | logical_name | feature_ref | 主路径 |
|---|---|---|---|
| Task@00201 | 内容计费基本功能 | Feature@GWFD-020301 | 00101→00102→00103→00104 |
| Task@00202 | 在线计费 | Feature@GWFD-020300 | 00101→00102→00103→00104（+可选00021/22/23） |
| Task@00203 | 离线计费 | Feature@GWFD-010171 | 00101→00102→00103→00104（+可选00023） |
| Task@00204 | 融合计费 | Feature@GWFD-010173 | 00101→00102→00103→00104 |

### 1.4 domain task（业务域，跨特性）—— 新增层

```yaml
task_id: UDG@20.15.2@Task@00301
task_logical_name: 计费功能配置
task_layer: domain
task_summary: 计费业务域配置（内容计费基础 + 按计费方式叠加在线/离线/融合能力）
task_relations:
  # 内容计费基本功能是基础，必做
  - {from_task_ref: Task@00201, to_task_ref: Task@00205, relation_type: precedes, requiredness: required}
status: active
# Task@00205 = "计费方式能力叠加"占位，由 DP-A 决定实际是 00202/00203/00204 中的哪个（或都不选=纯离线基础）
```

> domain task 编排 feature task。它的核心不是固定拓扑，而是 **DP-A 计费方式**——这个决策决定叠加哪个计费特性。

---

## 2. 两个 DecisionPoint 分开建（核心）

### DP-A 计费方式（挂 domain task Task@00301 —— task 级）

**作用域**：决定叠加哪个计费特性的子 task（task 级影响）。

```yaml
decision_id: UDG@20.15.2@DecisionPoint@00010
owner_ref: UDG@20.15.2@Task@00301          # ← 挂 domain task
decision_name: 计费方式选择
decision_question: 该业务采用哪种计费方式（决定叠加哪个计费特性的能力）？
trigger_condition: 完成内容计费基础配置后
options:
  - option_name: 纯离线基础
    impacts:
      - {target_type: task, target_ref: Task@00203, effect_type: excludes, effect_detail: "不叠加离线计费特性的额外命令；仅基础内容计费"}
      - {target_type: decision_point, target_ref: DecisionPoint@00001, effect_type: selects_option, effect_detail: "离线"}   # ← 决策传播
  - option_name: 在线
    impacts:
      - {target_type: task, target_ref: Task@00202, effect_type: adds, effect_detail: "叠加在线计费特性（含可选 SET UPDEFAULTQUOTA/UPGLBCHGPARA/URRFAILACTION）"}
      - {target_type: decision_point, target_ref: DecisionPoint@00001, effect_type: selects_option, effect_detail: "在线"}   # ← 决策传播
  - option_name: 离线
    impacts:
      - {target_type: task, target_ref: Task@00203, effect_type: adds, effect_detail: "叠加离线计费特性（含可选 SET URRFAILACTION）"}
      - {target_type: decision_point, target_ref: DecisionPoint@00001, effect_type: selects_option, effect_detail: "离线"}   # ← 决策传播
  - option_name: 融合
    impacts:
      - {target_type: task, target_ref: Task@00204, effect_type: adds, effect_detail: "叠加融合计费特性（SMF侧 RGAPPLIED 控制）"}
      - {target_type: decision_point, target_ref: DecisionPoint@00001, effect_type: selects_option, effect_detail: "融合"}   # ← 决策传播
status: active
```

> **关键①**：DP-A 每个 option 都有 `target_type=task` 影响（adds/excludes 计费特性子task）——这是 **task 级**影响。
> **关键②**：DP-A 每个 option 都有 `target_type=decision_point, effect=selects_option` ——这是**决策传播**，把选择下达给子层 DP-B。

### DP-B 计费方式（挂 atom task Task@00001 ADD URR —— 参数级）

**作用域**：决定 ADD URR 的参数取值（参数级影响）。这个 DP **独立建在 atom task 上**，描述"单条命令的计费方式参数怎么取"。

```yaml
decision_id: UDG@20.15.2@DecisionPoint@00001
owner_ref: UDG@20.15.2@Task@00001          # ← 挂 atom task（ADD URR），与 DP-A 分开
decision_name: 计费方式选择
decision_question: 该 URR 采用哪种计费方式（决定上报模式与统计类型参数）？
trigger_condition: 配置 ADD URR 时
options:
  - option_name: 离线
    impacts:
      - {target_type: parameter, target_ref: ...ADD URR:USAGERPTMODE, effect_type: sets_value_pattern, effect_detail: "=OFFLINE"}
      - {target_type: parameter, target_ref: ...ADD URR:OFFMETERINGTYPE, effect_type: adds, effect_detail: "条件出现"}
  - option_name: 在线
    impacts:
      - {target_type: parameter, target_ref: ...ADD URR:USAGERPTMODE, effect_type: sets_value_pattern, effect_detail: "=ONLINE"}
      - {target_type: parameter, target_ref: ...ADD URR:ONLMETERINGTYPE, effect_type: adds, effect_detail: "条件出现"}
  - option_name: 融合
    impacts:
      - {target_type: parameter, target_ref: ...ADD URR:USAGERPTMODE, effect_type: sets_value_pattern, effect_detail: "同URRGROUP内在线+离线URR共存"}
status: active
```

> **关键**：DP-B 是**独立对象**，自己完整描述了 ADD URR 的参数决策。它**不知道** DP-A 的存在（信息归属：atom 只管自己层级的参数决策）。
> 联动关系存在 **DP-A 的 option impact** 里（selects_option），不存在 DP-B 里——单向引用，干净。

---

## 3. 决策传播机制（实例化时怎么联动）

**建模阶段**（抽取时）：
- DP-A 建在 domain task，DP-B 建在 atom task —— **分开建，各自独立**
- DP-A 的每个 option 里写一条 `selects_option` 指向 DP-B 的对应 option —— **传播关系存在 DP-A 侧**

**实例化阶段**（配置下发时）：
```
1. 进入 domain task Task@00301
2. 遇 DP-A → 用户/上下文选"在线"
3. 引擎读"在线"option 的 impacts：
   a. target_type=task, adds Task@00202（在线计费特性）→ 子task集合加入在线计费特性
   b. target_type=decision_point, selects DecisionPoint@00001.在线 → 锁定 DP-B="在线"
4. 递归进入各子task。当进入 atom task Task@00001（ADD URR）时：
   - DP-B 已被锁定为"在线"（不用再问用户）→ 直接套用"在线"option 的参数impact
   - ADD URR.USAGERPTMODE=ONLINE, ONLMETERINGTYPE 出现
5. 进入在线计费特性 Task@00202 → 含 SET URRFAILACTION（Task@00023）等可选命令
```

> **核心**：用户只在**顶层 DP-A 选一次**"在线"，引擎通过 `selects_option` 自动把 DP-B 锁定到"在线"，子层参数自动正确。**不会出现"父选在线、子选离线"的矛盾**。

---

## 4. 实例化演示：选"在线" → 命令序列

| 步骤 | 来源 | 命令 |
|---|---|---|
| 基础内容计费（必做） | Task@00201 主路径 | ADD URR/URRGROUP/PCCPOLICYGRP/FILTER/.../RULE/USERPROFILE/RULEBINDING/SET URRGRPBINDING/SET REFRESHSRV |
| ADD URR 参数 | DP-B 被 DP-A 锁定"在线" | USAGERPTMODE=ONLINE, ONLMETERINGTYPE=VOLUME |
| 在线能力叠加 | DP-A"在线"adds Task@00202 | SET UPDEFAULTQUOTA（可选）/ SET UPGLBCHGPARA（可选）/ **SET URRFAILACTION**（可选，在线申请配额场景）|

**对比**：若 DP-A 选"离线" → DP-B 锁定"离线"（USAGERPTMODE=OFFLINE），叠加 Task@00203（含 SET URRFAILACTION 但无 UPDEFAULTQUOTA/UPGLBCHGPARA）。
若 DP-A 选"纯离线基础" → 不叠加任何特性 task，DP-B 锁定"离线"，命令集最小。

---

## 5. 这版样板验证的设计点

1. ✅ **task_layer 开放（4 层）**：atom→compound→feature→domain，最大无上限
2. ✅ **父子 DP 分开建**：DP-A（domain，task级）和 DP-B（atom，参数级）是**两个独立 DP 对象**，描述相似但作用域不同，不合并
3. ✅ **决策传播用显式 impact**：DP-A option 的 `target_type=decision_point, effect=selects_option` 表达传播；复用 impact 机制，不引入新关系类型
4. ✅ **单向引用**：传播关系只存父侧（DP-A），子侧（DP-B）不知道父——信息归属干净
5. ✅ **SET URRFAILACTION 正当归属**：它是 atom 积木库里的 Task@00023，由 DP-A 的 task 级 option（adds 在线/离线计费特性）决定是否启用，**不臆造、不乱挂**
6. ✅ **共享积木 + 差异在 DP**：4 特性共享同一套核心 atom/compound task，差异完全由 DP-A 的 option（adds 不同特性 task）表达——组合爆炸被消化

---

## 6. 对 schema 的两点确认

基于这版样板，UNIFIED_TASK_SCHEMA 该确认：

1. **task_layer 枚举加 `domain`**（atom/compound/feature/domain），体现"最大原子无上限"
2. **DecisionPoint impacts 的 target_type 加 `decision_point`**，effect_type 加 `selects_option`——决策传播的统一出口
3. **挂载点原则**（已在上版样板确立）：参数级决策挂 atom，task 级决策挂 compound/feature/domain；父子同义决策各建各的，靠父侧 selects_option 联动

要我把这 3 点补进 UNIFIED_TASK_SCHEMA.md 吗？还是样板本身还有要调整的？
