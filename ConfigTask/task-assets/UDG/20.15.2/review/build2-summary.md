# Phase 2 构建汇总 — feature 2-00001 ~ 2-00010 重建

> 日期:2026-07-03
> 方法:`task-build-skill/procedures/compound-extraction.md`(A 段 6 步)+ spec `docs/superpowers/specs/2026-07-02-compound-feature-extraction-design.md`
> 前置:Phase 1 构建流程更新(commit: feat(configtask) compound/feature 层抽取管线)

## 总览

| 指标 | 值 |
|---|---|
| 重建 feature 数 | **10/10**(2-00001~2-00010,计费 + PCC 族) |
| 覆盖校验 | **10/10 通过**(共 20 变体,exit 0) |
| atom 层冻结 | **0 违规**(14 个今日改动 yaml 全为 feature task 或 feature/compound 挂 rule·DP) |
| 新建 compound | **0**(全部复用 backbone 1-00001~04,符合"不为建而建") |
| 演进 compound-owned DP | 1(`dp-0-00002` 过滤链:补 excludes + `opt-basic-l34` option,爆炸半径 22 特性) |
| 新建 feature DP | 3(`dp-0-00154` 在线 / `dp-0-00155` 离线 / `dp-0-00156` 融合——条件 SET atom 门控) |
| 新建 feature rule | 1(`rule-0-00409` 2-00008 SIGDEFERREDTIME≥60s consistency) |
| variants.yaml 产出 | 10(每特性一份,覆盖校验输入) |

## 逐特性结果

| task | feature | 形态 | 变体数 | 复用判定 | 关键产出 |
|---|---|---|---|---|---|
| 2-00001 | GWFD-020301 内容计费基本 | STEP-OK | 5 | backbone 1-00001~04 Jaccard 1.0 | 演进 dp-0-00002(补 excludes)|
| 2-00002 | GWFD-020300 在线计费 | STEP-OK | 2 | backbone 全复用 | 新建 dp-0-00154(在线 3 SET atom);修 condition_ref 越界 generalized 违规 |
| 2-00003 | GWFD-010171 离线计费 | STEP-OK | 2 | backbone 全复用 | 新建 dp-0-00155(离线 URRFAILACTION)|
| 2-00004 | GWFD-010173 融合计费 | STEP-OK | 5 | backbone 全复用 | 新建 dp-0-00156(融合 URRFAILACTION)|
| 2-00005 | GWFD-020351 PCC基本功能 | STEP-OK | 1 | 1-00002/03 复用 + 3 直挂 | 纯复用,无新建 |
| 2-00006 | GWFD-020307 TCP重传识别 | 差量 | 1 | backbone 全复用(完整性:md"参考部署UPF")| 差量 atom 直挂;3 TCP 策略判定为参数级不挂 DP |
| 2-00007 | GWFD-020308 7层流量统计 | SINGLE | 1 | 无同义 compound,直挂 | 确认 SINGLE,不硬造 compound |
| 2-00008 | GWFD-020305 终端异常下行流量检测 | ATOM-CHAIN | 1 | ≤2 atom 直挂 | 新建 rule-0-00409 |
| 2-00009 | GWFD-020302 业务时长计费 | STEP-OK | 1 | backbone 全复用 | metering=TIME 判定为 atom 参数级/SMF 侧 |
| 2-00010 | GWFD-020303 业务流量计费 | STEP-OK | 1 | backbone 全复用 | VOLUME 默认,与 2-00009 同构 |

## 关键设计验证(方法学的硬闸都生效)

1. **per-DP-分支覆盖硬闸**:每个特性的每个 md 证实变体,active 命令集 == md_required。20 变体全过。退化为单变体的(2-00005~10)也跑扁平并集校验。
2. **复用双闸**:每候选 compound 都过了 Jaccard≥0.75 + 相位同义。10 特性 0 新建 compound——backbone 1-00001~04 全复用,印证充电/PCC 族的高质量存量。
3. **A/B 段隔离**:2-00002 抓出并修正了原 task 把 `condition_ref` 指向 generalized DP 0-00004(B 段作用域外)的违规,收回 feature 内 DP。
4. **atom 层冻结**:0 违规。计费方式差异(在线/离线/融合)正确挂在 atom DP 0-00001(冻结,只引用)+ 新建 feature DP 表达条件 SET atom,没碰 atom 层。
5. **形态判据**:2-00007(SINGLE)/ 2-00008(≤2 atom)正确不建 compound,直挂。

## 攒批人审队列(review/compound-review-queue-计费.md)

**待审 5 条**:
- 【待审·变更】dp-0-00002(1-00002 挂)补 excludes + opt-basic-l34 option — 影响 22 特性(2-00001/02 触发)
- 【待审·新建】dp-0-00154(2-00002 挂)在线 3 SET atom 门控
- 【待审·新建】dp-0-00155(2-00003 挂)离线 URRFAILACTION 门控
- 【待审·新建】dp-0-00156(2-00004 挂)融合 URRFAILACTION 门控
- 【待审·新建】rule-0-00409(2-00008 挂)SIGDEFERREDTIME consistency

**透明记录(自动放行)**:2-00005/09/10 纯复用。

## 遗留(非本次错误,记入 CONSOLIDATION-BACKLOG)

1. **12 个孤立 atom 缺 `task_layer`**(0-00109/110/149/150/153/154/155/156/174/175/177/199):命令级审查期遗留,孤立末梢(0 引用),不影响覆盖。本期按"atom 冻结"未碰,待专门 hygiene pass。
2. **SET SPECTRAFURRGRP 无 atom**:部署 md 步骤 10 出现,mml_commands 有但 tasks 无 atom。2-00001/03/04/09/10 同族一致不列。A 段不新建(atom 冻结),记 CONSOLIDATION-BACKLOG。
3. **时长计费 md 用 VOLUME**(2-00009 文档缺口):部署 md 任务示例未展示 TIME,task_intent 仅靠特性名语义区分。建议文档 owner 补。
4. **B 段 generalized 4-00001 未做**:按 spec,本域特性齐了才做 B 段(跨特性 DP 0-00004 传播链 + 域级覆盖校验)。本期 A 段先行,B 段脚本待建。

## 下一步建议

1. **人审攒批**:开 review-ui 过 5 条待审(dp-0-00002 演进 + 3 新 feature DP + rule-0-00409)→ active
2. **B 段**:建 generalized 4-00001 的跨特性关系 + DP 0-00004 向下传播链 + 域级覆盖校验脚本
3. **推广**:同法处理其余 48 个 ATOM-CHAIN feature(B2~B6 域)
