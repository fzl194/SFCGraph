# GWFD-010171 离线计费 (2-00003) — A 段 pass-2

> 重建日期:2026-07-03
> 流程依据:`task-build-skill/procedures/compound-extraction.md` A 段 6 步 + spec §4/§8/§5/§9
> atom 层冻结(命令 task + atom 挂 rule/DP 只读)。本特性重建 = 参照现有校准/演进。

---

## 自审发现

### md 全读(4 个)
- `配置Ga接口离线计费_31927856.md`(主配置,操作步骤 + 数据规划表 + 任务脚本)
- `GWFD-010171 离线计费参考信息_97563135.md`(命令清单 + 软参,无 license/告警/测量)
- `GWFD-010171 离线计费特性概述_66342906.md`(无需 License,无与其他特性交互,SGW-U/PGW-U 适用)
- `实现原理_66342907.md`(PFCP Session 流程,无命令)

### 命令真相核对
- 主示例脚本(必选):`ADD URR / ADD URRGROUP / ADD PCCPOLICYGRP / ADD FILTER / ADD FLOWFILTER /
  ADD FLTBINDFLOWF / ADD RULE / ADD USERPROFILE / ADD RULEBINDING / SET REFRESHSRV`(中段含 REFRESHTYPE=USERPROFILE) = 10 命令
- 步骤 6 可选:`SET URRFAILACTION`(条件出现,离线新业务场景生效) = 1 命令
- 参考信息命令清单列 9 命令(URR/URRGROUP/PCCPOLICYGRP/FILTER/FLOWFILTER/FLTBINDFLOWF/RULE/
  USERPROFILE/RULEBINDING),未含 SET URRFAILACTION/SET REFRESHSRV——参考信息只列 ADD 命令族,
  与主配置脚本一致(SET 在步骤 6 可选 / 主脚本中段)。

### pass-1 → pass-2 修订点
1. **越界 DP 收回**:0-00018 的 condition_ref 由 DP 0-00004(generalized 4-00001 owner,B 段作用域外)
   改为本特性级 DP 0-00155(新建,feature 2-00003 owner)。spec §4.3 A 段不依赖作用域外 DP。
2. **task_relations 编排顺序**:0-00018 由"挂在 1-00003 之后"改为"挂在 1-00004 之后",与 2-00002
   对齐(可选 atom 挂在收尾 backbone 之后)。
3. **source_evidence_ids 补全**:4 个 md 全列入(pass-1 只列主配置 1 个)。
4. **挂上 1-00004 收尾 backbone**:pass-1 已挂(关系 0-00021~0-00023),pass-2 确认保留并修正注释。

---

## 改动记录

| 文件 | 类型 | 改动 |
|---|---|---|
| `tasks/task-2-00003.yaml` | MODIFY | source_evidence_ids 补 4 md;0-00018 condition_ref 改 DP 0-00001→DP 0-00155;0-00018 挂点 1-00003→1-00004;notes 重写 |
| `decision_points/dp-0-00155.yaml` | NEW | feature 级 boolean DP,owner=2-00003,opt-on/opt-off 切 atom 0-00018 |
| `review/GWFD-010171-variants.yaml` | NEW | 2 变体(基础/opt-on 追加),dp_options 含 0-00002=opt-basic-l34 + 0-00003=opt-off + 0-00155 |
| `review/compound-review-queue-计费.md` | MODIFY | 追加【待审·新建】DP 0-00155 事件 |
| `review/GWFD-010171-pass-2.md` | NEW | 本报告 |

未改动:atom 层(task-0-*,atom 挂 rule 0-00119,atom 挂 DP 0-00051)只读保留;backbone compounds
1-00001~04 不动;DP 0-00001/0-00002/0-00003/0-00004(冻结或非本特性 owner)只引用不改建。

---

## 复用判定证据(步骤②双闸)

| 候选段 | 命令集 | top-1 backbone | Jaccard | 相位 | 动作 |
|---|---|---|---|---|---|
| 步骤1-2 费率→策略组 {URR, URRGROUP, PCCPOLICYGRP} | 3 | 1-00001(3) | 3/3 = 1.0 ≥0.75 | 计费三件套同义 | **复用 1-00001** |
| 步骤3 过滤链 {FILTER, FLOWFILTER, FLTBINDFLOWF} | 3 | 1-00002(6) | 3/6 = 0.5 + 相位过滤链同义 + opt-basic-l34 收敛 | 过滤链同义 | **复用 1-00002**(经 opt-basic-l34 excludes 收敛,2-00002 pass-2 已演进) |
| 步骤4-5 规则与用户模板绑定 {RULE, USERPROFILE, RULEBINDING} | 3 | 1-00003(3) | 3/3 = 1.0 ≥0.75 | 规则与用户模板绑定同义 | **复用 1-00003** |
| 收尾 {REFRESHSRV} | 1 | 1-00004(3) | 1/3 = 0.33 < 0.4 | 收尾同义 | **复用 1-00004**(结构提供,不新建;URRGRPBINDING/SPECURRGRPLIST 简化展示缺口与 2-00001/2-00002 同处理) |
| 步骤6 SET URRFAILACTION(可选) | 1 | 候选≤2 命令 | — | 离线专属条件 atom | **降级 feature→atom 直挂**(挂 0-00018 + DP 0-00155 门控) |

无新建 compound(全部命中 backbone 复用);新建 1 个 feature 级 DP(0-00155);无 compound 演进。

---

## 离线专属 atom 0-00018 表达方式

- **feature 级 DP 0-00155(新建)** 表达,owner=2-00003,boolean,opt-on/opt-off 切 atom 0-00018 出现/缺失
- impact:`opt-on` → `adds task 0-00018`;`opt-off` → `excludes task 0-00018`
- 对偶 2-00002 的 DP 0-00154(在线):0-00154 opt-on 切 3 SET,0-00155 opt-on 只切 1 SET(URRFAILACTION
  是 md 唯一标注"离线"字样的可选命令)
- 不依赖 B 段 generalized DP 0-00004(opt-g-offline 决定"是否叠加 2-00003 特性",本 DP 在特性叠加后
  内部决定是否追加可选命令,spec §5 同名决策多层共存不合并)
- atom 0-00018 自挂的 rule 0-00119 + DP 0-00051 命令级约束闭环,本 feature DP 只管命令集出现/缺失

---

## 覆盖校验结果

```
=== 覆盖校验:feature 2-00003 (GWFD-010171) ===
结构命令集(16):['ADD FILTER', 'ADD FILTERIPV6', 'ADD FLOWFILTER', 'ADD FLTBINDFLOWF',
'ADD L7FILTER', 'ADD PCCPOLICYGRP', 'ADD PROTBINDFLOWF', 'ADD RULE', 'ADD RULEBINDING',
'ADD SPECURRGRPLIST', 'ADD URR', 'ADD URRGROUP', 'ADD USERPROFILE', 'SET REFRESHSRV',
'SET URRFAILACTION', 'SET URRGRPBINDING']
变体校验数:2
结果:✓ 覆盖通过
EXIT=0
```

变体数:2(基础-不含离线专属SET / 离线专属SET追加);结构命令集大小:16(含 backbone 全并集,
DP 0-00002 opt-basic-l34 + 0-00003 opt-off 在变体校验时动态 excludes 收敛到 md_required 12/13 命令)。

---

## 缺口 / 遗留问题

1. **SET URRGRPBINDING 简化展示缺口**:md 主配置脚本未显式列,但由 backbone 1-00004 结构提供。
   与 2-00001/2-00002 同处理(参 2-00002 variants.yaml 注释),md_required 含此命令。**不视为缺口**。
2. **无 feature 挂 rule**:本特性无需 License(概述明示)、无配置值互斥(atom 0-00018 命令级已闭环)、
   无防欺诈(由 2-00001 承载)。**无遗留**。
3. **B 段 generalized 4-00001**:本域特性齐了再建,本期 A 段不碰。DP 0-00004 opt-g-offline 仍负责
   "是否叠加 2-00003 特性",与本 DP 0-00155 不冲突。**待 B 段**。
4. **与 2-00002 互斥变体的表达**:在线 vs 离线是特性级互斥(B 段用 DP 0-00004 选 feature 表达);
   A 段 feature 内不表达跨特性互斥(spec §4.3 A/B 段隔离)。**符合 spec**。
