# GWFD-020301 内容计费基本功能 — A 段 pass-2 自审报告

> feature task: UDG@20.15.2@Task@2-00001
> 日期:2026-07-02
> 流程:compound-extraction.md A 段 6 步
> 前置:atom 层冻结(0-00001~0-00015 + atom 挂 rule/DP 只读)

---

## 1. 自审发现

- 2-00001 是内容计费基础特性,md 操作步骤(部署UPF §操作步骤 11 步)天然分为 4 段,
  与 backbone 1-00001~04 一一对齐,无单命令降级段。
- 4 候选 compound 全部命中 backbone,Jaccard=1.0 + 相位同义,**纯复用,不新建**。
- md 揭示的 feature 级分叉已由现有 DP 表达完毕:
  - 0-00003 防欺诈(feature 层,opt-on/off)✓ 已存在
  - 0-00001 计费方式(atom 0-00001 层,冻结)✓ 仅参数 impact 不进枚举
  - 0-00002 业务匹配场景(compound 1-00002 层)✓ 已存在,但**需演进补 excludes**(见下)
- 无需新挂 feature 级 DP。

## 2. 改动记录(逐文件)

| 文件 | 类型 | 说明 |
|---|---|---|
| `decision_points/dp-0-00002.yaml` | 修改 | 为 4 个 option 补 `excludes` 子句(原版只 adds 不 excludes,导致 per-variant 命令集不收敛)。owner=compound 1-00002,**非 atom 层**,允许演进。入 compound-review-queue-计费.md 待审。 |
| `review/GWFD-020301-variants.yaml` | 新增 | 5 个 md 证实变体(URL防欺诈关/开、IMS、any、异常) + dp_options + md_required_commands |
| `review/compound-review-queue-计费.md` | 新增 | 计费域攒批人审队列,本次 1 条【待审·变更】(DP 0-00002 演进) |
| `review/GWFD-020301-pass-2.md` | 新增 | 本报告 |

**未改动**(核实现状合理):
- `tasks/task-2-00001.yaml`:task_relations 序 1-00001→02→03→04 对齐 md 操作步骤,notes
  正确引用 DP 0-00001/0-00002。保持原状。
- `tasks/task-1-00001~04.yaml`:4 个 backbone 全复用 as-is,无演进。
- `task_rules/rule-0-00008.yaml`(conditional:防欺诈开启时 URL RULE 必同绑三四层 filter):与
  DP 0-00002 opt-url 配合,表达 md L7FILTER 表 URLTYPE 字段说明。保持。
- `task_rules/rule-0-00009.yaml`(dependency:依赖 SA-Basic + License):对齐 md 特性概述
  "与其他特性的交互"。保持。
- `task_rules/rule-0-00010.yaml`(dependency:CommandParameter 待 CommandGraph 抽取):元规则,
  标记 15 命令的静态层缺口。保持。
- `decision_points/dp-0-00003.yaml`(防欺诈,feature 层):对齐 md 表1 L7FILTER URLTYPE 说明 +
  场景1 防欺诈示例(ADD SPECURRGRPLIST)。保持。

**atom 层全部只读未动** (task-0-*.yaml + dp-0-00001.yaml + 各 atom 挂 rule)。

## 3. 复用判定证据(每候选 Jaccard + 相位)

| 候选(本特性 md 步骤段) | 命令集 | 命中 backbone | Jaccard | 相位 | 动作 |
|---|---|---|---|---|---|
| A: 配置费率→URRGROUP→PCC策略组(步骤1-2) | {ADD URR, ADD URRGROUP, ADD PCCPOLICYGRP} | 1-00001 计费三件套 | 3/3 = **1.0** | "费率→策略组绑定" 同义 | 复用 |
| B: 配置过滤链(步骤3-5) | {ADD FILTER, ADD FILTERIPV6, ADD FLOWFILTER, ADD FLTBINDFLOWF, ADD L7FILTER, ADD PROTBINDFLOWF} | 1-00002 过滤链 | 6/6 = **1.0** | "过滤链/业务匹配" 同义 | 复用 |
| C: 规则与用户模板绑定(步骤6-8) | {ADD RULE, ADD RULEBINDING, ADD USERPROFILE} | 1-00003 规则与用户模板绑定 | 3/3 = **1.0** | "规则绑定" 同义 | 复用 |
| D: 收尾(步骤9-11) | {ADD SPECURRGRPLIST, SET REFRESHSRV, SET URRGRPBINDING} | 1-00004 收尾 | 3/3 = **1.0** | "缺省费率/刷新" 同义 | 复用 |

**结论**:4 候选全部纯复用,**不新建任何 compound**,不为建而建(procedure §0)。

## 4. 覆盖校验结果

```
=== 覆盖校验:feature 2-00001 (GWFD-020301) ===
结构命令集(15):[ADD FILTER, ADD FILTERIPV6, ADD FLOWFILTER, ADD FLTBINDFLOWF,
  ADD L7FILTER, ADD PCCPOLICYGRP, ADD PROTBINDFLOWF, ADD RULE, ADD RULEBINDING,
  ADD SPECURRGRPLIST, ADD URR, ADD URRGROUP, ADD USERPROFILE, SET REFRESHSRV,
  SET URRGRPBINDING]
变体校验数:5
结果:✓ 覆盖通过
EXIT=0
```

**变体清单**:场景1-URL-防欺诈关 / 场景1-URL-防欺诈开 / 场景2-IMS / 场景3-any基础 /
场景4-异常信令费率(共 5,md 表1-表4 + 防欺诈 on/off)。

## 5. 缺口或演进债

- **DP 0-00002 演进**(compound 1-00002 挂,爆炸半径 22 特性):补 excludes 子句,已入
  compound-review-queue-计费.md 【待审·变更】。人审通过后需连锁重跑 2-00002/3/4/6/9/10/
  11/12/14/15/16/17/18/30/31/32/33/50/89/91 等引用 1-00002 特性的覆盖校验(SKILL §7.2)。
  本次精确化 excludes 只收敛不新增,语义更准,不应改变任一特性的有效变体集,但仍走人审。
- **rule 0-00010 元规则**:本特性 15 命令的 CommandParameter 结构化对象仍待 CommandGraph 抽取
  (元规则,非本次 A 段职责)。
- 无 atom 层改动需求。

## 6. 下个特性可复用产物

- backbone 1-00001~04:本次确认 as-is 复用稳定,后续 2-00002(在线)/2-00003(离线)/
  2-00004(融合)应同样全复用,差异仅在线/离线/融合专属可选命令(URRFAILACTION 等)。
- DP 0-00002 演进版:URL/IMS/any/异常 4 option 现精确表达 per-variant 命令集,后续特性
  引用同 DP 不必再改。
