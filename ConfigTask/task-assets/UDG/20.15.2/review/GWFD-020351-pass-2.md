# GWFD-020351 PCC基本功能 — A 段 pass-2(2026-07-03)

> feature task `2-00005` | 串行第 5 个 | 按 `procedures/compound-extraction.md` A 段 6 步
> atom 层冻结(只读)。本特性只动 feature / feature 挂 rule·DP / 复用 compound。

## 自审发现

### md 全读(9 个,全读毕)
- 激活(2):配置动态PCC功能_74096530.md / 配置本地PCC功能_74096529.md — **操作步骤+脚本逐字相同**
- 调测(1):调测PCC基本功能_42369277.md(LST 查询+消息跟踪,非配置生成命令)
- 参考/概述(2):参考信息_79592737.md(命令清单含 ADD QOSPROP 跨特性引用)/ 特性概述_47011385.md
- 原理(4):相关概念_72244993.md(策略/触发器/规则/条件/动作/SDF)/ 业务流程_47013470.md / Event Trigger_47013472.md / 2_3_4_5G PCC功能差异_47013471.md

### 关键判定
1. **动态PCC = 本地PCC 命令集**(md 明示+逐字对齐):9 命令,DP 0-00007 纯参数分叉(changes_scope),不产生独立覆盖变体。
2. **过滤场景 = any-to-any 三四层**(md 任务示例明示"3/4层any to any的filter,未配置7层规则")→ DP 0-00002 opt-basic-l34。
3. **ADD QOSPROP 不入 md_required**:参考信息 md 命令清单含,但激活步骤不含,属 GWFD-010201 QoS 特性。
4. **不复用 1-00001 计费三件套**:PCC 是策略控制,无独立 URR 链;URRGROUPNAME 仅 PCCPOLICYGRP 参数级可选(rule 0-00014)。
5. **不复用 1-00004 收尾**:计费专属,本特性直挂 REFRESHSRV。
6. **业务排除/重复排除/规则优先级**:原理 md 概念(动态>预定义>本地;安装+删除同 rule 取安装),不引入 UPF 侧新命令,无新 DP。

## 改动记录
| 文件 | 动作 | 说明 |
|---|---|---|
| `tasks/task-2-00005.yaml` | MODIFY notes | 校准 md_required 9 命令 + DP 0-00002 opt-basic-l34 收敛口径;task_relations 保持(已对) |
| `review/GWFD-020351-variants.yaml` | NEW | 1 变体(扁平,DP 0-00007 不枚举因其纯参数) |
| `review/GWFD-020351-pass-2.md` | NEW | 本报告 |
| `review/compound-review-queue-计费.md` | APPEND | 透明笔:本特性纯复用,无新事件 |

## 复用判定证据(top-3)

### 候选 A:过滤链 {FILTER, FLOWFILTER, FLTBINDFLOWF} → 复用 1-00002
| 现有 compound | Jaccard | phase 比对 | 推荐 |
|---|---|---|---|
| **1-00002 过滤链** {FILTER, FILTERIPV6, FLOWFILTER, FLTBINDFLOWF, L7FILTER, PROTBINDFLOWF} | 3/6=0.5(候选是 1-00002 真子集) | 同义(过滤链) | **复用 + DP 0-00002=opt-basic-l34** |
| 1-00003 规则绑定 | 0/3=0 | 不同义 | — |
| 1-00001 计费三件套 | 0/3=0 | 不同义 | — |

判定:Jaccard 0.5 落 reference 区,但候选是 1-00002 真子集且 backbone 已有 opt-basic-l34 option 精确匹配 md any-to-any 子集 → 复用 + DP(与 2-00002/03/04 同型 precedent)。不新建。

### 候选 B:规则与用户模板绑定 {RULE, USERPROFILE, RULEBINDING} → 复用 1-00003
| 现有 compound | Jaccard | phase 比对 | 推荐 |
|---|---|---|---|
| **1-00003 规则与用户模板绑定** {RULE, RULEBINDING, USERPROFILE} | 3/3=1.0 | 同义 | **复用 as-is** |
| 1-00002 过滤链 | 0/3=0 | 不同义 | — |
| 1-00004 收尾 | 0/3=0 | 不同义 | — |

### 单命令步骤 → feature→atom 直挂(降级)
- SET LICENSESWITCH(步骤1)→ 直挂 atom 0-00019(不可复用,L2TP 1-00021 含此但相位不同义+Jaccard 1/3)
- ADD PCCPOLICYGRP(步骤2)→ 直挂 atom 0-00003(PCC 专属,backbone 无独立 compound)
- SET REFRESHSRV(步骤7)→ 直挂 atom 0-00015(must_be_last,在 1-00004 内但本特性不复用整个收尾)

## PCC 变体如何表达
| 变体维度 | DP | option | 表达 |
|---|---|---|---|
| PCC模式(动态/本地) | 0-00007(feature owner) | opt-pcc-dynamic / opt-pcc-local | 纯参数 changes_scope(RULENAME 动态 vs USERPROFILENAME 本地),命令集不变,不进覆盖枚举 |
| 过滤场景 | 0-00002(1-00002 owner) | opt-basic-l34 | excludes FILTERIPV6/L7FILTER/PROTBINDFLOWF,结构 12→9 |
| URRGROUPNAME 可选 | rule 0-00014(dependency) | — | 参数级,PCCPOLICYGRP 仍在,URR/URRGROUP 不入命令集 |
| 业务排除/重复排除 | — | — | 原理概念(规则优先级/安装删除仲裁),无 UPF 命令,无 DP |

## 缺口
- 无。覆盖校验 exit 0,结构 12 / 变体 1 / 通过。
- DP 0-00007 已存在(原版建),两 option 纯参数 impact,不需演进。
- feature 挂 rule 0-00012(License LKV3G5PCCB01 + 业务感知前置)/ 0-00013(LICENSESWITCH CommandParameter 缺口)已对齐 md,不动。

## 事件分流
- 1-00002 复用 + opt-basic-l34:option 已在 2-00002 pass-2 入队待审 → 本特性纯复用 as-is,**不入队**。
- 1-00003 复用 as-is:**不入队**。
- DP 0-00007:已存在,无演进,**不入队**。
- feature 挂 rule/DP:已对齐,**不动**。
- **本特性不新建/不演进任何 compound/DP**。compound-review-queue 追加透明笔。
