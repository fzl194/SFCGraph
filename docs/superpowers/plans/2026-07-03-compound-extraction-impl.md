# compound/feature 层抽取管线 — 实施计划

> **For agentic workers:** 用 superpowers:executing-plans 实施。Steps 用 checkbox 跟踪。
> 依据 spec:`docs/superpowers/specs/2026-07-02-compound-feature-extraction-design.md`

**Goal:** 落地 spec §12 的构建流程更新(覆盖校验脚本 + canonical 登记表派生 + SKILL/procedure 增订),然后用更新后的 SKILL 串行重建 feature 2-00001~2-00010,atom 层冻结。

**Architecture:** 覆盖校验作自动硬闸(pytest TDD,key off `target_type∈{task,command}` + md 收口);canonical 登记表由 build_index.py 派生;SKILL/procedure 增订 A 段 6 步 + 复用双闸 + 攒批人审;feature 重建串行 Agent(每特性读全 md → 参考/更新现有 compound → 建 feature+rule+DP → 覆盖校验过 → 更新 registry)。

**Tech Stack:** Python(pytest + pyyaml),YAML 资产。前端不动。

**硬边界:** atom 层(命令 task + atom 挂 rule/DP)冻结,只补不改。compound/feature/feature挂 rule·DP / compound挂 rule·DP 可建可改。

---

## Phase 1:构建流程更新

### Task 1:build_index.py 加 compounds 段 + canonical-compounds.md 派生(TDD)
**Files:** MODIFY `task-build-skill/scripts/build_index.py`;NEW `task-build-skill/tests/test_build_index_compounds.py`;NEW(派生)`task-assets/UDG/20.15.2/canonical-compounds.md`

- [ ] 写测试:`compounds` 段存在;每条含 {compound_id, logical_name, phase(=logical_name), intent, command_set(命令名集), features_using};24 个 compound 全覆盖;1-00001 command_set ⊇ {ADD URR,ADD URRGROUP,ADD PCCPOLICYGRP}
- [ ] 跑测试 FAIL
- [ ] 实现:build_index.py 加 `compounds` 段(从 compound task 的 task_relations 解析 atom→command;features_using 反查 atom_usage)+ 生成 canonical-compounds.md(人工可读)
- [ ] 跑测试 PASS
- [ ] 重建 index.json + canonical-compounds.md,人工抽查

### Task 2:check_feature_coverage.py 覆盖校验(TDD)
**Files:** NEW `task-build-skill/scripts/check_feature_coverage.py`;NEW `task-build-skill/tests/test_check_coverage.py` + `tests/fixtures/`

- [ ] 写测试(fixture 造 3 feature:pass / 缺命令 / 多命令 / 含环 / md 无示例 option 不枚举):
  - active_atoms(F,V) 按 target_type∈{task,command} 算(不看 effect_type 名)
  - 环检测报错
  - md_required 取自 `review/{fid}-variants.yaml`(Agent 产物)
  - per-variant 集合相等,不等报 diff(缺/多)
- [ ] 跑 FAIL
- [ ] 实现 check_feature_coverage.py
- [ ] 跑 PASS
- [ ] CLI:`python check_feature_coverage.py <feature_task_id 如 2-00001>`,exit 0=过 / 1=失败带 diff

### Task 3:procedures/compound-extraction.md + SKILL.md 增订
**Files:** NEW `task-build-skill/procedures/compound-extraction.md`;MODIFY `task-build-skill/SKILL.md`

- [ ] NEW procedure:A 段 6 步流程细则(① md 分段 ② 复用双闸 ③ DP 放置 ④ 编排 ⑤ 覆盖校验 ⑥ 事件分流)+ 复用闸阈值表 + 覆盖校验调用方式 + variants.yaml 格式
- [ ] MODIFY SKILL §5 step2:compound 凝练指向新 procedure
- [ ] MODIFY SKILL §7.1:Jaccard 判据改为"引用 procedure §8.2 双闸(0.75/0.4 + 相位)",保留 atom 豁免
- [ ] MODIFY SKILL §8.1:加"per-DP-分支覆盖校验(procedure §5)为硬闸"
- [ ] MODIFY SKILL §8:加"事件驱动攒批人审(procedure §10)"
- [ ] 版本号 v2 → v3,顶部记变更

### Task 4:Phase 1 验收 smoke
- [ ] `pytest task-build-skill/tests/` 全过
- [ ] `python build_index.py` 重建,index compounds 段 24 条
- [ ] `python check_feature_coverage.py 2-00001`(用现有结构 + 手写一份 variants.yaml)能跑出结果

---

## Phase 2:串行重建 feature 2-00001~2-00010

### Task 5:梳理 10 特性上下文(产出 per-feature 上下文清单)
- [ ] 每特性:全部 md 路径(主配置/参考信息/数据规划/实现原理/部署)+ 现有 compounds/atoms/feat-rules/feat-dps + 涉及命令的 mml 真相路径
- [ ] 产出 `review/build2-ctx.md`(10 节,供 Agent 读取)

### Task 6~15:每特性一个 Agent(串行,不并行)
每特性统一流程(遵循 procedure):
- 读该特性**全部** md + 涉及命令的 mml_commands 真相 + 现有该特性的 task/rule/dp + canonical 登记表
- A 段 6 步:① md 分段抽候选 compound(单/双命令降级直挂)② 复用双闸比对 canonical(命中 backbone→复用+演进;独有≥3命令→新建入待审)③ 变体(计费方式等)挂 DP(最底层;feature及以下)④ 编排 feature task_relations ⑤ 写 variants.yaml + 跑 check_feature_coverage.py 过 ⑥ 事件入 review 队列
- co-build:feature 级 rule/DP,compound 级 rule(若新建/演进)
- atom 层**只读**(不改 atom task/atom挂rule/atom挂dp)
- 收尾:更新该特性 review/{fid}-pass-2.md(自审+改动+证据)

**串行关键**:每特性 Agent 完成后,主控重建 index.json + canonical-compounds.md(让下一特性看到新/演进的 compound),再发下一特性。顺序按 2-00001→2-00010。

### Task 16:Phase 2 收尾
- [ ] 重建 index.json + canonical-compounds.md
- [ ] 域级 4-00001 generalized 复校(计费方式 DP 0-00004 传播链 → feature/atom DP 对齐)
- [ ] 10 特性 coverage 全过;progress.json 记 last_session
- [ ] 写 `review/build2-summary.md`(改动汇总 + 新建/演进 compound 清单 + 演进债)

---

## 边界与约束
- atom 层冻结(命令 task / atom 挂 rule / atom 挂 DP 只读)
- feature 重建=参照现有按新方法校准/演进,不是推翻
- 串行 Agent(不并行),因下一特性可能复用上一特性产出
- 每特性必须读其全部 md
- 12 个缺 task_layer 的 atom 是孤立末梢,本期不碰(不影响),记为遗留
