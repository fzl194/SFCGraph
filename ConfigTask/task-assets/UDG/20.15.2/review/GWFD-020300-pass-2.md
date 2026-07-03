# GWFD-020300 在线计费 — A 段 pass-2 自审报告

> feature task: UDG@20.15.2@Task@2-00002
> 日期:2026-07-03
> 流程:compound-extraction.md A 段 6 步
> 前置:atom 层冻结(task-0-* + atom 挂 rule/DP 只读)。dp-0-00001(挂 atom 0-00001)只引用不改建。

---

## 1. 自审发现

- 2-00002 在线计费的 md 操作步骤(配置Gy接口在线计费 §操作步骤 8 步)天然分两段:
  - 步骤1-5 = 内容计费 backbone(费率→过滤条件→规则→用户模板绑定),与 2-00001 同构
  - 步骤6-8 = 在线专属可选命令(默认配额/Credit Pooling/上报失败动作),3 条均标"可选"
- 4 backbone 候选 compound(1-00001~04)全部纯复用,Jaccard=1.0 + 相位同义(详见 §3)
- 3 在线专属 atom(0-00016/17/18)是"条件出现"——但条件性在本特性层就表达(特性本身即"在线计费"):
  - 旧版(pass-1, B 段同建)用 `condition_ref: DP 0-00004`(generalized owner 4-00001)门控,
    违反 spec §4.3 A 段不依赖作用域外 DP
  - 本次 A 段重建:**新建 feature 级 DP 0-00154(在线专属SET开关)**,把 3 atom 的 adds/excludes
    收回到本特性作用域内,与上层 DP 0-00004 不冲突(spec §5 同名决策可多层共存不合并)
- md 操作步骤3 仅展示三四层 IPv4 FILTER(无 L7FILTER/FILTERIPV6),与 dp-0-00002 既有 4 option
  (URL/IMS/any/异常,全部假设 FILTER 配 L7 或 IPv6)无一匹配 → **演进 dp-0-00002 补 opt-basic-l34**
- md 主脚本省略 SET URRGRPBINDING,但该命令由 backbone 1-00004 结构提供且功能必需 → md_required
  含 SET URRGRPBINDING(与 2-00001 pass-2 一致)

## 2. 改动记录(逐文件)

| 文件 | 类型 | 说明 |
|---|---|---|
| `tasks/task-2-00002.yaml` | 修改 | source_evidence_ids 补全 4 md(原仅 1);3 个在线 atom 的 condition_ref 由 DP 0-00004(B 段作用域外)改为本特性级 DP 0-00154;notes 详记演进原因 + md 笔误声明 + 与上层 DP 不冲突论证 |
| `decision_points/dp-0-00154.yaml` | 新增 | feature 级 boolean DP,owner=2-00002。opt-off 排除 3 个在线 atom,opt-on 追加 3 个。与 dp-0-00003(防欺诈)同型 |
| `decision_points/dp-0-00002.yaml` | 修改 | 补第 5 option `opt-basic-l34`(IPv4 三四层基础场景,adds FILTER / excludes FILTERIPV6+L7FILTER+PROTBINDFLOWF)。仅扩 option 不改既有,2-00001 连锁覆盖校验仍通过 |
| `review/GWFD-020300-variants.yaml` | 新增 | 2 个 md 证实变体(基础-不含在线SET / 全在线SET追加)+ dp_options(0-00002/0-00003/0-00154)+ md_required_commands |
| `review/compound-review-queue-计费.md` | 追加 | 2 条事件:DP 0-00002 演进(待审·变更,爆炸半径 22 特性)+ DP 0-00154 新建(待审·新建) |
| `review/GWFD-020300-pass-2.md` | 新增 | 本报告 |

**未改动**(核实现状合理):
- `task_rules/rule-0-00011.yaml`(conditional:Credit Pooling 与 DefaultQuota 不能同使能):
  md L88 + 命令真相(SET UPGLBCHGPARA.CREDITPOOLSW)佐证,与本特性 DP 0-00154 opt-on 配合,
  覆盖校验只校命令集,规则合规由 conditional_rule 在配置生成时强制。保持。
- `tasks/task-1-00001~04.yaml`:4 backbone 全复用 as-is,无演进。
- atom 层全部只读未动(task-0-00016/17/18 + 各 atom 挂 rule 0-00116/117/118/119 + DP 0-00050/51)。
- `decision_points/dp-0-00001.yaml`(atom 0-00001 挂,冻结):opt-online 锁定计费方式=在线,仅参数
  impact 不进 variants 枚举。只引用不改建。
- `decision_points/dp-0-00004.yaml`(generalized 4-00001 挂,B 段):opt-g-online 仍负责"是否叠加
  2-00002 特性",与本特性 DP 0-00154 不冲突。只引用不改建。

## 3. 复用判定证据(每候选 Jaccard + 相位)

| 候选(本特性 md 步骤段) | 命令集 | 命中 backbone | Jaccard | 相位 | 动作 |
|---|---|---|---|---|---|
| A: 费率→URRGROUP→PCC策略组(步骤1-2) | {ADD URR, ADD URRGROUP, ADD PCCPOLICYGRP} | 1-00001 计费三件套 | 3/3 = **1.0** | "费率→策略组绑定" 同义 | 复用 |
| B: 过滤条件(步骤3,三四层基础) | {ADD FILTER, ADD FLOWFILTER, ADD FLTBINDFLOWF} | 1-00002 过滤链 | 3/6 = 0.5(并集 6 含 L7/IPv6/PROTBIND) | "过滤链" 同义 | **复用 1-00002** + DP 0-00002 opt-basic-l34 裁剪(本特性 md 只用 IPv4 三四层) |
| C: 规则与用户模板绑定(步骤4-5) | {ADD RULE, ADD USERPROFILE, ADD RULEBINDING} | 1-00003 规则与用户模板绑定 | 3/3 = **1.0** | "规则绑定" 同义 | 复用 |
| D: 收尾(脚本含 SET REFRESHSRV,md 简化省 SET URRGRPBINDING) | {ADD SPECURRGRPLIST, SET REFRESHSRV, SET URRGRPBINDING} | 1-00004 收尾 | 3/3 = **1.0** | "缺省费率/刷新" 同义 | 复用(SPECURRGRPLIST 由 DP 0-00003 opt-off 裁剪) |
| E(降级): 在线专属可选(步骤6-8) | {SET UPDEFAULTQUOTA, SET UPGLBCHGPARA, SET URRFAILACTION} | 单命令 ≤2 命令规则不适用(3 命令);dp-0-00002 / 1-0000[1-4] 均无在线 SET 相位 | — | 无 backbone 匹配 | **降级 feature→atom 直挂**(3 atom 各挂 task_relations 边,由 feature DP 0-00154 门控 adds/excludes),不新建 compound |

**结论**:4 backbone 候选全部纯复用,3 在线 atom 降级 feature→atom 直挂(符合 procedure §1
"单命令/无命中→直挂"和 spec §8.2 例"URRFAILACTION 作在线专属挂条件")。**不新建任何 compound**,
不为建而建(procedure §0)。

## 4. 覆盖校验结果

```
=== 覆盖校验:feature 2-00002 (GWFD-020300) ===
结构命令集(18):['ADD FILTER', 'ADD FILTERIPV6', 'ADD FLOWFILTER', 'ADD FLTBINDFLOWF',
  'ADD L7FILTER', 'ADD PCCPOLICYGRP', 'ADD PROTBINDFLOWF', 'ADD RULE', 'ADD RULEBINDING',
  'ADD SPECURRGRPLIST', 'ADD URR', 'ADD URRGROUP', 'ADD USERPROFILE', 'SET REFRESHSRV',
  'SET UPDEFAULTQUOTA', 'SET UPGLBCHGPARA', 'SET URRFAILACTION', 'SET URRGRPBINDING']
变体校验数:2
结果:✓ 覆盖通过
EXIT=0
```

**变体清单**:基础-不含在线专属SET / 全在线专属SET追加(共 2,md 步骤6-8 可选 on/off)。
**连锁复审**:2-00001 覆盖校验仍 ✓ 通过(dp-0-00002 仅扩 option 不改既有 option)。

## 5. 在线专属 atom(0-00016/17/18)如何表达

- **DP adds/excludes 模式**:本特性新建 DP 0-00154(feature 层 boolean)
  - opt-off → excludes atom 0-00016/17/18(对应 md 主示例脚本:不含 3 SET)
  - opt-on → adds atom 0-00016/17/18(对应 md 步骤6-8 文字可选项)
- **feature→atom 直挂边**:task_relations 含 3 条 1-00004→0-00016/17/18 边,requiredness=optional,
  condition_ref=DP 0-00154
- **不新建 compound**:3 atom 跨"默认配额 / Credit Pooling / 上报失败"3 个不同语义,无共享相位,
  单命令各自独立,符合 procedure §1 "单命令步骤不成为候选 → feature→atom 直挂"
- **规则 0-00011 配合**:atom 0-00016(UPDEFAULTQUOTA)与 0-00017(UPGLBCHGPARA)的配置值由
  conditional_rule 0-00011 强制互斥,DP 0-00154 只管命令集出现,不强制配置值

## 6. 缺口或演进债

- **DP 0-00002 演进**(compound 1-00002 挂,爆炸半径 22 特性):补 opt-basic-l34 option,
  已入 compound-review-queue-计费.md 【待审·变更】。本次仅扩 option 不改既有 option,
  已连锁重跑 2-00001 覆盖校验 ✓ 仍通过。后续引用 1-00002 的 2-00003/04/30/31 等若 md 也是
  "三四层基础"配法,可直接选 opt-basic-l34(不必每个都演进)。
- **DP 0-00154 新建**(feature 2-00002 挂):已入 compound-review-queue-计费.md 【待审·新建】。
- **md 笔误**(GWFD-020300 配置md L87):prose 称"Credit Pooling 由 SET UPDEFAULTQUOTA 的
  CREDITPOOLSW 控制",实属 SET UPGLBCHGPARA(命令真相 + L85 上下文佐证,见 pass-2 0203 报告)。
  task 层 rule 0-00011 按命令真实归属引用,未受笔误影响。md 只读不改。
- **md 简化展示缺口**:md 主脚本省略 SET URRGRPBINDING,本特性 md_required 含该命令(与 2-00001
  一致,反映 backbone 结构现实)。该决策可重审:若人审认为应严格按 md 字面不含,则需在
  compound 1-00004 加 DP 排除 SET URRGRPBINDING(爆炸半径 9 特性,目前不推荐)。
- 无 atom 层改动需求。

## 7. 下个特性可复用产物

- DP 0-00002 opt-basic-l34:2-00003(离线)/2-00004(融合)等"复用 backbone 仅承担计费方式差量"
  的特性 md 同样仅展示三四层基础 FILTER,可直接选此 option,无需再演进。
- DP 0-00154 模式:2-00003(离线)若也有离线专属可选命令(如 SET URRFAILACTION 复用),可建
  类似 feature 级 DP(不与 2-00002 共享,因 owner 不同),但 SET URRFAILACTION atom 0-00018
  跨在线/离线复用——2-00003 引用同一 atom 即可,无需重复建 atom。
- DP 0-00002 5 option 现覆盖 URL/IMS/any/异常/基础 5 形态,2-00001 演进版 + 本次扩 option 已稳。
