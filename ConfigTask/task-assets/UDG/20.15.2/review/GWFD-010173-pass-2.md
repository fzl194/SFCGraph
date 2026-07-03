# GWFD-010173 融合计费 (2-00004) — A 段 pass-2

> 重建日期:2026-07-03
> 流程依据:`task-build-skill/procedures/compound-extraction.md` A 段 6 步 + spec §4/§8/§5/§9
> atom 层冻结(命令 task + atom 挂 rule/DP 只读)。本特性重建 = 参照现有校准/演进。

---

## 自审发现

### md 全读(5 个)
- `部署UPF_79654301.md`(主配置,操作步骤 + 数据规划表 + 任务示例脚本,完整列举 4 过滤场景)
- `调测融合计费的费率标识_91966529.md`(调测步骤 1-8,步骤 8 提供可选 SET URRFAILACTION)
- `GWFD-010173 融合计费特性概述_70301693.md`(无需 License,SMF/UPF 适用,RGAPPLIED 控制)
- `实现原理_70301694.md`(PFCP Session 流程,SMF 侧 RGAPPLIED=DEFAULT/DISCARD/CHARGING 控制路径)
- `GWFD-010173 融合计费参考信息_33931912.md`(命令清单 + 软参,无 license/告警/测量)

### 命令真相核对
- 主示例脚本(backbone 必选):URR/URRGROUP/PCCPOLICYGRP + FILTER/L7FILTER/FLOWFILTER/
  FLTBINDFLOWF/PROTBINDFLOWF(FILTERIPV6 在 IMS 场景)+ RULE/USERPROFILE/RULEBINDING +
  SPECURRGRPLIST + SET URRGRPBINDING + SET REFRESHSRV = 15 命令(4 场景并集)
- 步骤 8 可选(条件出现):`SET URRFAILACTION`(业务被阻塞时放通,RETRYFAILACT=CONTINUE)= 1 命令
- 参考信息命令清单与主配置脚本一致(SET URRGRPBINDING/SET REFRESHSRV 在主脚本中段,SET URRFAILACTION
  在调测步骤 8 可选)。

### pass-1 → pass-2 修订点
1. **挂上特性级可选 DP**:0-00018(SET URRFAILACTION)由 condition_ref 指向新建 feature 级 DP 0-00156
   (owner=2-00004),与 2-00002 DP 0-00154 / 2-00003 DP 0-00155 同型对偶。spec §4.3 A 段不依赖
   作用域外 DP,收回特性内。
2. **挂点对齐**:0-00018 挂在收尾 backbone 1-00004 之后(与 2-00002/03 对齐,可选 SET 挂在收尾之后)。
3. **source_evidence_ids 补全**:5 个 md 全列入(pass-1 仅列部分)。
4. **4 backbone 全复用 as-is**:Jaccard=1.0(1-00001/03/04)+ 过滤链 1-00002 复用(融合 md 4 场景
   完整列举,DP 0-00002 的 4 option 全覆盖)。

### 融合专属表达判定
- **URRGROUP 在线+离线共存**:由 atom 层命令级规则约束(consistency_rule 0-00001 +
  conditional_rule 0-00002 挂在 1-00001),不进 feature variants 枚举(覆盖校验只校命令集)。
- **SET URRFAILACTION(融合可选)**:md 唯一在调测步骤标注的可选命令 → 新建 feature 级 DP 0-00156
  (opt-on/opt-off 切 1 SET),不新建 compound。
- **计费方式=融合**:由 atom DP 0-00001(opt-converged)锁定,仅参数 impact(USAGERPTMODE=CONVERGED
  描述),不 adds/excludes atom → 不进 variants 枚举,只引用不改建(冻结)。
- **不依赖 B 段**:generalized DP 0-00004(opt-g-converged)决定"是否叠加 2-00004 特性",B 段作用域外,
  A 段不引用。

---

## 改动记录

| 文件 | 类型 | 改动 |
|---|---|---|
| `tasks/task-2-00004.yaml` | MODIFY | source_evidence_ids 补 5 md;0-00018 condition_ref → 新建 DP 0-00156;挂点 1-00004;notes 重写 |
| `decision_points/dp-0-00156.yaml` | NEW | feature 级 boolean DP,owner=2-00004,opt-on/opt-off 切 atom 0-00018 |
| `review/GWFD-010173-variants.yaml` | NEW | 5 变体(4 场景 opt-off + 1 场景 opt-on 追加),dp_options 含 0-00002/0-00003/0-00156 |
| `review/compound-review-queue-计费.md` | MODIFY | 追加【待审·新建】DP 0-00156 事件 |
| `review/GWFD-010173-pass-2.md` | NEW | 本报告 |

未改动:atom 层(task-0-*,atom 挂 rule 0-00119,atom 挂 DP 0-00051)只读保留;backbone compounds
1-00001~04 不动;DP 0-00001/0-00002/0-00003/0-00004(冻结或非本特性 owner)只引用不改建。

---

## 复用判定证据(步骤②双闸)

| 候选段 | 命令集 | top-1 backbone | Jaccard | 相位 | 动作 |
|---|---|---|---|---|---|
| 步骤1-2 费率→策略组 {URR, URRGROUP, PCCPOLICYGRP} | 3 | 1-00001(3) | 3/3 = 1.0 ≥0.75 | 计费三件套同义 | **复用 1-00001** |
| 步骤3 过滤链(4 场景并集){FILTER, FILTERIPV6, L7FILTER, FLOWFILTER, FLTBINDFLOWF, PROTBINDFLOWF} | 6 | 1-00002(6) | 6/6 = 1.0 ≥0.75 | 过滤链同义 | **复用 1-00002**(4 option 全证实,opt-url/ims/any/abnormal) |
| 步骤4-5 规则与用户模板绑定 {RULE, USERPROFILE, RULEBINDING} | 3 | 1-00003(3) | 3/3 = 1.0 ≥0.75 | 规则与用户模板绑定同义 | **复用 1-00003** |
| 收尾 {SPECURRGRPLIST, URRGRPBINDING, REFRESHSRV} | 3 | 1-00004(3) | 3/3 = 1.0 ≥0.75 | 收尾同义 | **复用 1-00004**(融合 md 显式列 SET URRGRPBINDING,无简化展示缺口) |
| 步骤8 SET URRFAILACTION(可选) | 1 | 候选≤2 命令 | — | 融合专属条件 atom | **降级 feature→atom 直挂**(挂 0-00018 + DP 0-00156 门控) |

无新建 compound(全部命中 backbone 复用,Jaccard 均 ≥0.75);新建 1 个 feature 级 DP(0-00156);无 compound 演进。

---

## 覆盖校验(步骤⑤硬闸)

```
=== 覆盖校验:feature 2-00004 (GWFD-010173) ===
结构命令集(16):['ADD FILTER', 'ADD FILTERIPV6', 'ADD FLOWFILTER', 'ADD FLTBINDFLOWF',
  'ADD L7FILTER', 'ADD PCCPOLICYGRP', 'ADD PROTBINDFLOWF', 'ADD RULE', 'ADD RULEBINDING',
  'ADD SPECURRGRPLIST', 'ADD URR', 'ADD URRGROUP', 'ADD USERPROFILE', 'SET REFRESHSRV',
  'SET URRFAILACTION', 'SET URRGRPBINDING']
变体校验数:5
结果:✓ 覆盖通过
EXIT=0
```

5 变体 = 4 场景 opt-off(URL/IMS/any/异常,DP 0-00002 四 option × 0-00003=opt-on × 0-00156=opt-off)
+ 1 场景 opt-on(URL+防欺诈+URRFAILACTION 追加)。结构命令集 16 = backbone 15(4 场景并集)+
 可选 SET URRFAILACTION。

---

## 缺口/遗留

- 无 atom 层缺口(SET URRFAILACTION = atom 0-00018 已存在,3 特性复用)。
- 无 compound 新建/演进(全复用 as-is)。
- DP 0-00156 待人审(A 段 inferred,人审通过 → active)。
- 不依赖 B 段 generalized DP 0-00004(opt-g-converged 决定"是否叠加 2-00004 特性",B 段作用域外)。
