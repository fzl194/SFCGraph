# GWFD-020308 7层流量统计 — A 段 pass-2 自审报告

> feature task: UDG@20.15.2@Task@2-00007
> 日期:2026-07-03
> 流程:compound-extraction.md A 段 6 步
> 前置:atom 层冻结(task-0-* + atom 挂 rule/DP 只读)。atom 0-00020 / feature 挂 rule 0-00017 只引用不改建。

---

## 1. 自审发现

- 2-00007 是 **SINGLE 形态**:仅 1 个 atom(0-00020 ADD APN),md 操作步骤仅 1 步("配置仅统计7层
  应用层流量功能"),数据规划表唯一命令即 ADD APN。
- md 全读(3 个:参考信息/特性概述/激活)交叉确认:
  - 参考信息 §命令:本特性相关 MML 命令仅 `ADD APN`(无其他命令)。
  - 特性概述 §原理 / §计费与话单:UDG 通过 ADD APN 的 APPLAYERVOLUME 参数控制统计口径
    (ENABLE=仅 L7;DISABLE=L7+L3/L4)。
  - 激活 md §操作步骤:唯一步骤即 ADD APN,脚本 `ADD APN: APN="apn-test", APPLAYERVOLUME=ENABLE;`。
- **形态判定:确认 SINGLE 直挂,不建 compound**(procedure §1:候选 ≤2 命令且无命中 → 降级
  feature→atom 直挂;spec §8.2:单命令步骤不成为候选)。不为 SINGLE 硬造 compound。
- 现有 relation 0-00038(2-00007 contains 0-00020)即该 feature→atom 直挂边,P1 已正确建立,P2 保留。
- 变体分析(步骤③):APPLAYERVOLUME ENABLE/DISABLE 是 atom 0-00020 的参数级选择(variable_source
  local_planned,requiredness conditional,atom 层冻结)。DISABLE = 命令默认值 = 本特性"未开启"
  (= backbone 2-00001 内容计费默认口径),ENABLE = 本特性 task_intent。该开关不改命令出现/缺失
  → 不构成命令集分叉 → 按 spec §4.2 不挂 feature DP → 退化为单变体(扁平并集校验)。
- 前置合规(内容计费 2-00001 backbone + SA-Basic):由 feature 挂 rule 0-00017(dependency_rule)
  在配置生成时强制,不进命令集覆盖枚举。

## 2. 改动记录(逐文件)

| 文件 | 类型 | 说明 |
|---|---|---|
| `tasks/task-2-00007.yaml` | 修改 | source_evidence_ids 补全 3 md(原仅激活 1);task_relations 注释补 P2 SINGLE 形态确认;notes 扩写 6 步推理(形态判定 + canonical 复用查无 + 变体退化论证 + 覆盖校验结果)。**relation 结构不变**(0-00038 保留,P1 直挂边已正确) |
| `review/GWFD-020308-variants.yaml` | 新增 | 1 个 md 证实变体(基础:APPLAYERVOLUME=ENABLE)+ dp_options 空(扁平并集,无 feature 级 DP)+ md_required_commands 1 命令(ADD APN) |
| `review/GWFD-020308-pass-2.md` | 新增 | 本报告 |

**未改动**(核实现状合理):
- `tasks/task-0-00020.yaml`(ADD APN atom,跨特性共享基础对象):冻结。APPLAYERVOLUME 参数绑定
  已在 atom 层闭环(local_planned/conditional)。
- `task_rules/rule-0-00017.yaml`(dependency_rule:内容计费 backbone 前置 + APPLAYERVOLUME 统计
  口径影响):命令级审查已闭环,保持不动。
- atom 层全部只读未动。

**未新建**:无新 compound / 无新 feature DP / 无新 feature 挂 rule(均现状合理)。

## 3. 复用判定证据(候选 Jaccard + 相位)

本特性仅 1 atom,无多命令候选 compound。仍按 procedure §2 在 canonical-compounds.md 检索 ADD APN
相关 compound:

| 候选(本特性 md 步骤段) | 命令集 | 命中 canonical | Jaccard | 相位 | 动作 |
|---|---|---|---|---|---|
| A(单命令): 配置 APN 仅统计7层(md 操作步骤唯一) | {ADD APN} | 1-00012 地址池族(含 ADD APN + 5 地址池命令) | 1/7 ≈ **0.14** | 1-00012 相位=地址分配池链,本特性相位=流量统计口径开关,**不同义** | **降级 feature→atom 直挂**(单命令 + 不同义,procedure §1 + spec §8.2) |

**结论**:无 canonical compound 可复用(唯一含 ADD APN 的 1-00012 相位不同义,Jaccard<0.4)。
单命令 → 降级 feature→atom 直挂(符合 procedure §1 + spec §8.2)。**不新建任何 compound / DP / rule**,
不为建而建(procedure §0)。

## 4. 覆盖校验结果

```
=== 覆盖校验:feature 2-00007 (GWFD-020308) ===
结构命令集(1):['ADD APN']
变体校验数:1
结果:✓ 覆盖通过
EXIT=0
```

**变体清单**:基础(配置仅统计7层应用层流量,APPLAYERVOLUME=ENABLE)(共 1,单变体扁平并集校验)。
**无连锁复审**:本特性未改任何 compound / DP,不影响引用方。

## 5. 事件分流(步骤⑥)

- **不入队**:SINGLE 形态降级直挂,无 compound 新建/演进,无 feature DP 新建。
  按 procedure §6 "纯复用/直挂不入队" + spec §10.1 "纯复用 as-is 自动放行,不入队"。
- `review/compound-review-queue-计费.md` 无新增事件。

## 6. 形态判定与 atom 直挂表达(供下个特性参考)

- **SINGLE 形态判定**:feature 含 1 atom + md 操作步骤 ≤2 命令 + canonical 无同义命中 →
  feature→atom 直挂,不建 compound(procedure §1 + spec §8.2)。
- **relation 表达**:feature task_relations 含 `{from: feature, to: atom, type: contains}` 直挂边
  (本特性即 0-00038: 2-00007→0-00020)。覆盖校验沿该边收集 atom 命令集 → struct_commands。
- **参数级开关不升 feature DP**:APPLAYERVOLUME ENABLE/DISABLE 是 atom 参数级选择(不改命令集
  出现/缺失)→ 不挂 feature DP → 退化为单变体(spec §4.2)。统计口径影响由 feature 挂
  dependency_rule(0-00017)在配置生成时强制,不进覆盖枚举。
- **license 无需单独 atom**:md 概述 §可获得性 明示"本特性无需 License 许可"→ feature 不挂
  License atom(与 2-00006 TCP重传识别需 SET LICENSESWITCH 形成对比)。

## 7. 缺口或演进债

- 无 compound 新建/演进事件 → 不入 compound-review-queue-计费.md。
- 无 feature DP 新建 → 不入 review 队列。
- atom 0-00020 演进(跨特性共享基础对象,参数持续补全中)在 atom 层审查闭环,本特性仅引用不改。
- APPLAYERVOLUME ENABLE/DISABLE 的参数级选择不进 A 段命令集覆盖枚举。若人审认为应在配置生成时
  显式建模(如 feature 级 parameter-only DP),可在 B 段或后续反哺 SKILL 时讨论;当前按 spec §4.2
  仅枚举改命令集的 DP,本特性退化为单变体。

## 8. 下个特性可复用产物

- **SINGLE 形态范式**:1 atom + 单命令步骤 + canonical 无同义 → feature→atom 直挂 + 单变体扁平并集
  校验 + 不入队。可作为后续 SINGLE 特性(如 2-00008 终端异常下行流量检测的双 atom 形态需另判)的参考。
- **参数级开关不升 DP 判据**:ENABLE/DISABLE 类二元参数开关若不改命令出现/缺失 → 不挂 feature DP,
  退化为单变体。统计口径/计费影响由 feature 挂 dependency_rule 表达,不进覆盖枚举。
