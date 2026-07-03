# GWFD-020307 TCP重传识别 — A 段 pass-2 自审报告

> feature task: UDG@20.15.2@Task@2-00006
> 日期:2026-07-03
> 流程:compound-extraction.md A 段 6 步
> 前置:atom 层冻结(task-0-* + atom 挂 rule/DP 只读)。atom 0-00013 / 0-00019 / feature 挂 rule 0-00015 只引用不改建。

---

## 1. 自审发现

- 2-00006 是**差量特性**:md 明示"详细配置参考 部署UPF_28493406(=2-00001 内容计费完整 backbone),
  此处仅描述差异"。完整配置 = backbone 全集(1-00001~04)+ License(0-00019) + TCP重传差量
  (atom 0-00013 的 TCP 子集:TCPCHGPROFLAG=CHARGING / TCPURRGRPNAME)。
- md 操作步骤仅 2 步:(1) 打开 License;(2) 参考 部署UPF + 差异(UserProfile 绑 TCP重传 URR 组)。
  backbone 4 候选(1-00001~04)全部纯复用,Jaccard=1.0 + 相位同义(详见 §3)。License 与 0-00013
  是单命令/差量 → 降级 feature→atom 直挂(spec §8.2 例 + procedure §1)。
- md 特性概述 §计费与话单 列 3 种 TCP 重传计费策略(单独费率/关联默认/不计费)。评估后认定这 3 策略
  **不构成命令集分叉**:
  - atom 0-00013 是多用途 atom(DFT 子集用于 backbone 缺省费率 / TCP 子集用于本特性),命令名都是
    SET URRGRPBINDING。3 策略仅是 SET URRGRPBINDING 的参数子集/取值差异(单独费率=
    TCPCHGPROFLAG=CHARGING+TCPURRGRPNAME;关联默认=不配 TCP 子集;不计费=改计费口径)。
  - atom 0-00013 已固定 TCPCHGPROFLAG=CHARGING,锁定 md 唯一证实的"单独费率"配置路径。
  - 按 spec §4.2 仅枚举改命令集的 DP → 本特性无 feature 级改命令集 DP → 退化为单变体
    (spec §4.2 末段:扁平并集校验)。
- 继承的 backbone DP(0-00002 过滤链 / 0-00003 防欺诈):本特性 md 仅"参考部署UPF",未列举任何
  具体过滤场景或防欺诈示例,故不为本特性枚举这些 DP 的子选项(spec §4.2 按 md 收口)。
- atom 0-00013 由 1-00004 结构提供(DFT 子集)+ 本特性 1-00003→0-00013 直挂边(TCP 子集),
  命令名层面同一命令去重后 1 个 SET URRGRPBINDING。

## 2. 改动记录(逐文件)

| 文件 | 类型 | 说明 |
|---|---|---|
| `tasks/task-2-00006.yaml` | 修改 | source_evidence_ids 补全 2 md(原仅 1);notes 重写详记 6 步推理 + 完整性处理 + 3 策略不构成命令集分叉论证 + 0-00013 多用途说明;task_relations 注释补 P2 重建说明 + 0-00013 多用途/3策略论证。**relation 结构不变**(0-00036/01950~3 全保留,原 P1 完整性修正已正确) |
| `review/GWFD-020307-variants.yaml` | 新增 | 1 个 md 证实变体(完整配置)+ dp_options 空(扁平并集,无 feature 级 DP)+ md_required_commands 16 命令(backbone 全集 + License + TCP 差量去重) |
| `review/GWFD-020307-pass-2.md` | 新增 | 本报告 |

**未改动**(核实现状合理):
- `tasks/task-1-00001~04.yaml`:4 backbone 全复用 as-is,无演进。
- `tasks/task-0-00013.yaml`(多用途 atom,DFT+TCP 子集):冻结。atom 层固定 TCPCHGPROFLAG=CHARGING
  锁定 md 唯一证实路径,3 策略参数层选择不进 A 段覆盖枚举。
- `tasks/task-0-00019.yaml`(License atom):冻结。LICITEM=LKV3G5TCPR01 由 feature 投影(md 脚本明示)。
- `task_rules/rule-0-00015.yaml`(dependency_rule:license LKV3G5TCPR01 + 内容计费 backbone 前置):
  命令级审查已闭环,保持不动。
- atom 层全部只读未动(0-00013/0-00019 + 各自 atom 挂 rule)。

**未新建**:无新 compound / 无新 feature DP / 无新 feature 挂 rule(均现状合理)。

## 3. 复用判定证据(每候选 Jaccard + 相位)

| 候选(本特性 md 步骤段) | 命令集 | 命中 backbone | Jaccard | 相位 | 动作 |
|---|---|---|---|---|---|
| A: 费率→URRGROUP→PCC策略组(部署UPF 步骤,md 参考) | {ADD URR, ADD URRGROUP, ADD PCCPOLICYGRP} | 1-00001 计费三件套 | 3/3 = **1.0** | "费率→策略组绑定" 同义 | 复用 |
| B: 过滤链(部署UPF 步骤,md 参考) | {ADD FILTER, ADD FILTERIPV6, ADD FLOWFILTER, ADD FLTBINDFLOWF, ADD L7FILTER, ADD PROTBINDFLOWF} | 1-00002 过滤链 | 6/6 = **1.0** | "过滤链" 同义 | 复用(本特性 md 未裁剪场景) |
| C: 规则与用户模板绑定(部署UPF 步骤,md 参考) | {ADD RULE, ADD USERPROFILE, ADD RULEBINDING} | 1-00003 规则与用户模板绑定 | 3/3 = **1.0** | "规则绑定" 同义 | 复用 |
| D: 收尾(部署UPF 步骤,md 参考,含 DFT 子集 + 可选防欺诈 + 刷新) | {ADD SPECURRGRPLIST, SET REFRESHSRV, SET URRGRPBINDING} | 1-00004 收尾 | 3/3 = **1.0** | "缺省费率/刷新" 同义 | 复用 |
| E(降级): License(md 步骤1) | {SET LICENSESWITCH} | atom 0-00019 跨 56 特性复用 | 单命令 | 激活前置 | **降级 feature→atom 直挂**(单命令,procedure §1) |
| F(降级): TCP重传差量(md 步骤2) | {SET URRGRPBINDING} | atom 0-00013 多用途 atom(backbone 已结构提供 DFT 子集) | 单命令 | 差量参数子集 | **降级 feature→atom 直挂**(0-00013 TCP 子集,通过 1-00003→0-00013 边表达,propagated_context USERPROFILENAME/TCPURRGRPNAME) |

**结论**:4 backbone 候选全部纯复用,License + TCP 差量 atom 降级 feature→atom 直挂(符合 procedure §1
"单命令/无命中→直挂" + spec §8.2 例)。**不新建任何 compound / DP / rule**,不为建而建(procedure §0)。

## 4. 覆盖校验结果

```
=== 覆盖校验:feature 2-00006 (GWFD-020307) ===
结构命令集(16):['ADD FILTER', 'ADD FILTERIPV6', 'ADD FLOWFILTER', 'ADD FLTBINDFLOWF',
  'ADD L7FILTER', 'ADD PCCPOLICYGRP', 'ADD PROTBINDFLOWF', 'ADD RULE', 'ADD RULEBINDING',
  'ADD SPECURRGRPLIST', 'ADD URR', 'ADD URRGROUP', 'ADD USERPROFILE', 'SET LICENSESWITCH',
  'SET REFRESHSRV', 'SET URRGRPBINDING']
变体校验数:1
结果:✓ 覆盖通过
EXIT=0
```

**变体清单**:完整配置(部署UPF backbone + TCP重传差量)(共 1,单变体扁平并集校验)。
**无连锁复审**:本特性未改任何 compound / DP,不影响引用方。

## 5. 差量 atom(0-00013 / 0-00019)如何表达

- **降级 feature→atom 直挂**(procedure §1 单命令/无命中 → 直挂):
  - 0-00019(License):task_relations 含 0-00019→1-00001 边(required,md 步骤1 明示 License 在计费
    backbone 前)。LICITEM=LKV3G5TCPR01 由 feature 投影(md 脚本明示),atom 0-00019 跨 56 特性复用,
    每特性固定一个 LICITEM,不在 atom 升 DP(已在 atom 0-00019 notes 记录)。
  - 0-00013(TCP重传差量):task_relations 含 1-00003→0-00013 边(required,propagated_context
    USERPROFILENAME 由 0-00011 传播 / TCPURRGRPNAME 引用 0-00002 URRGROUP),表达 md 步骤2 的
    "UserProfile 绑 TCP重传 URR 组"。atom 0-00013 的 TCP 子集(TCPCHGPROFLAG=CHARGING 固定 +
    TCPURRGRPNAME reference)即本特性差量。
- **不新建 compound**:License 与 TCP 差量均为单命令,无共享相位,符合 procedure §1
  "单命令步骤不成为候选 → feature→atom 直挂"。atom 0-00013 是多用途 atom(backbone DFT 子集 +
  本特性 TCP 子集),无需为 TCP 子集新建专用 compound。
- **不挂 feature DP**:3 种 TCP 重传计费策略仅是 SET URRGRPBINDING 参数子集/取值差异,不改变命令
  出现/缺失,atom 0-00013 已固定 TCPCHGPROFLAG=CHARGING 锁定 md 唯一证实路径 → 不构成命令集分叉
  → 不挂 feature DP(spec §4.2)。
- **feature 挂 rule 0-00015 配合**:dependency_rule(license LKV3G5TCPR01 + 内容计费 backbone 前置)
  是命令级审查已闭环的约束,覆盖校验只校命令集出现/缺失,前置合规由 rule 在配置生成时强制。

## 6. 完整性处理(差量特性的 backbone 纳入)

- md 明示"详细配置参考 部署UPF_28493406(=2-00001 内容计费完整 backbone)"→ 本特性完整配置 = backbone
  全集(1-00001~04 复用)+ 差量。
- 候选 compound → 命中 backbone 1-00001~04 → **复用**(Jaccard 1.0 + 相位同义,§3)。
- 差量 atom 0-00013(TCP重传专属 SET URRGRPBINDING 子集):本特性独有差量,直挂 feature(1-00003→0-00013)。
- License atom 0-00019(激活类):跨特性复用,直挂 feature(0-00019→1-00001)。
- P1 完整性修正(2026-07-02)已正确把 backbone compounds 纳入(0-00036/01950~2 边)。本次 P2 保留,
  覆盖校验验证 16 命令扁平并集 == md_required。

## 7. 缺口或演进债

- 无 compound 新建/演进事件 → 不入 compound-review-queue-计费.md(spec §10.1 纯复用自动放行)。
- 无 feature DP 新建 → 不入 review 队列。
- atom 0-00013 多用途演进(DFT+TCP 子集)在 atom 层审查已闭环(pass-3,2026-07-02 已记录 notes),
  本特性仅引用不改。
- 3 种 TCP 重传计费策略的参数层选择(单独费率/关联默认/不计费)不进 A 段命令集覆盖枚举。若人审认为
  应在配置生成时显式建模(如 feature 级 parameter-only DP),可在 B 段或后续反哺 SKILL 时讨论;
  当前按 spec §4.2 仅枚举改命令集的 DP,本特性退化为单变体。

## 8. 下个特性可复用产物

- 差量特性模式(md "详细配置参考 XXX"):2-00009(基于业务时长的计费)/2-00010(基于业务流量的计费)
  md 同款"参考部署UPF"差量特性,可复用本次"backbone 全复用 + 差量 atom 降级直挂 + 单变体扁平并集"
  范式(若其 md 也无改命令集的 feature 级 DP)。
- atom 0-00013 多用途(DFT+TCP 子集)模式:可作为后续 atom 演进的参考(单一命令承载多场景参数子集,
  各子集 requiredness conditional 适配)。
