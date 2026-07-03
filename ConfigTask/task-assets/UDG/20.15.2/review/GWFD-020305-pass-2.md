# GWFD-020305 终端异常下行流量检测 — A 段 pass-2 重建

> feature 2-00008 | 串行第 8 个 | ATOM-CHAIN 形态(2 atom)
> 日期:2026-07-03 | procedure:`task-build-skill/procedures/compound-extraction.md` | spec §4/§8/§5/§9

## 形态判定

**ATOM-CHAIN ≤2 atom → feature→atom 直挂,不建 compound。**

- 直接 atom:0-00019(SET LICENSESWITCH,跨特性 License 开关)、0-00021(ADD ABNTRAFFICDT,本特性专属)
- atom 数 = 2,命中 spec §8.2 / procedure §1「≤2 atom 直挂」判据
- 现有无 compounds(保留为空),本次不新建 — 核实不硬造

## 自审发现

| # | 发现 | 处理 |
|---|---|---|
| 1 | md「原理概述」描述两种检测方案(简单 / 基于流特征),由 ADD ABNTRAFFICDT 的 TRAFFICBEHAVIORSWITCH 区分 | md「操作步骤」+「数据规划表」+「任务示例」仅给出基于流特征一条操作路径(SWITCH=ENABLE,TRAFFICBEHAVIORSWITCH=ENABLE);「简单检测」仅原理概述概念说明,无独立步骤 → 不构成 md_required 命令分支 → 变体数 = 1(基础) |
| 2 | TRAFFICBEHAVIORSWITCH 语义分叉(简单 DISABLE / 流特征 ENABLE) | atom 0-00021 已绑 local_planned/required(默认 ENABLE,见命令级审查笔记),分叉在 atom 层吸收;特性级不重复升 DP(atom 层冻结,且本特性无需特性级 DP) |
| 3 | md「应用限制」:SET SRVCOMMONPARA.SIGDEFERREDTIME ≥ 60s | 该命令是全局业务公共参数,非本特性激活步骤 → 不进结构基线/不进 md_required;但约束需留档 → 新建 feature 挂 consistency_rule 0-00409(target_type 非 command 故不影响覆盖校验命令集) |
| 4 | md「参考信息」命令清单含 SET ABNTRADTTHR(阈值)、SET SRVCOMMONPARA、LST LICENSESWITCH、LST ABNTRAFFICDT、EXP MML | SET ABNTRADTTHR 经参考信息单列引用、非激活步骤(阈值另配);LST/EXP 为查询/导出,非配置;均不计入 md_required |
| 5 | md「与其他特性的交互」明示依赖 GWFD-020301 内容计费基本功能 | 已由 feature 挂 rule 0-00016 表达(requires 内容计费 + APN 前置),无需新建 |

## 改动记录

| 文件 | 动作 | 说明 |
|---|---|---|
| `tasks/task-2-00008.yaml` | 改 | notes 增补 A 段重建说明(形态/覆盖校验/新 rule/无 DP);task_relations 保留现有 0-00019→0-00021 precedes 边(license 先于 ABNTRAFFICDT) |
| `task_rules/rule-0-00409.yaml` | 新建 | feature 挂 consistency_rule:SET SRVCOMMONPARA.SIGDEFERREDTIME ≥ 60s(md 应用限制);status=inferred |
| `review/GWFD-020305-variants.yaml` | 新建 | 单变体·基于流特征检测,md_required={SET LICENSESWITCH, ADD ABNTRAFFICDT} |

未改:atom task(0-00019/0-00021)、atom 挂 rule/DP、现有 feature 挂 rule 0-00016(license 与 APN 前置依赖,已准确)。

## 复用判定证据

无 compound 候选(≤2 atom 直挂,跳过步骤②双闸)。canonical-compounds.md 无同义 compound 可复用(本特性的 ADD ABNTRAFFICDT 为专属命令,无 backbone 命中)。

## 覆盖校验

```
python ConfigTask/task-build-skill/scripts/check_feature_coverage.py 2-00008
=== 覆盖校验:feature 2-00008 (GWFD-020305) ===
结构命令集(2):['ADD ABNTRAFFICDT', 'SET LICENSESWITCH']
变体校验数:1
结果:✓ 覆盖通过
EXIT=0
```

- 结构命令集大小:2
- 变体数:1
- 结构集 == md_required(操作步骤命令集),无缺无多

## 事件分流(人审攒批)

- 纯复用/直挂:本特性无 compound,不入队
- 新建 rule 0-00409(consistency_rule,feature 挂):单特性,无爆炸半径,随批审

## 缺口/遗留

无。本特性为 ATOM-CHAIN 末端,不指向 B 段 generalized DP(无跨特性 DP 传播需求)。
