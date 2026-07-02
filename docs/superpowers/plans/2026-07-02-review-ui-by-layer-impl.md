# Review UI 按级别目录 + 内嵌子卡片 实施 Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 重建 ConfigTask/review-ui 为"左侧 3 面板(命令/步骤/特性)平铺 + 主区内嵌子卡片(3 层嵌套 + 折叠策略)"的审视界面,替换原父子树 UI,数据契约向后兼容(`review-state.json` 字段不变,`/api/assets` 只加不删)。

**Architecture:** 后端 `serve.py` 增量增加 `by_layer` / `relation_targets` 两个派生字段(原 `tree` 等字段全部保留供 nav 与 `_diag.py`);前端 `index.html` 微调 + `app.js` 重写为主,组件 8 个(`renderStats` / `renderLeftPanel` / `renderMain` / `renderTaskCard` / `renderChildren` / `renderDP` / `renderRule` / `renderReview`),FOCUS 数据环与 DOM focus 解耦,L2 卡片默认折叠 + L3 chip 列超阈值折叠 + L1 内嵌区两级折叠(8/15 双档)。

**Tech Stack:** Python 3.11(http.server / yaml / json,无新依赖),原生 HTML + ES module + DOM API(无框架),pytest(`serve.py` 字段派生函数),手工 13 步 smoke(前端无自动化测试)。

**Spec:** `docs/superpowers/specs/2026-07-02-review-ui-by-layer-design.md`(已批准,4 commit 演进:e2cca07)

**用户约束:** 直接 master 提交,不开分支/worktree(全局规则)。Co-Authored-By 已全局禁用。

---

## File Structure

**3 个文件改动**:
- Modify: `ConfigTask/review-ui/serve.py` — `build_assets()` 加 `by_layer` / `relation_targets` 字段;**保留** `build_tree` / `build_reuse` 函数体(`_diag.py` 依赖)
- Modify: `ConfigTask/review-ui/index.html` — 微调(去掉 `.tlegend` 父树图例,加 3 面板容器 + 简化筛选框 input,改 `.tree` 为 `.panels`,加 `.ec` 内嵌卡片样式)
- Modify: `ConfigTask/review-ui/app.js` — 重写(`renderTree` → `renderLeftPanel`;新增 `renderChildren` / `renderTaskCard`;删兄弟渲染;加 FOCUS + Tab 焦点环;加两级折叠逻辑)

**3 个文件不动**:
- `ConfigTask/review-ui/_diag.py` — 跑时用,依赖 `build_tree` / `build_reuse`
- `ConfigTask/review-ui/_render.py` — 命令行预览
- `ConfigTask/review-ui/_serve_nobrowser.py` — 无 GUI 兜底

**新增 1 个测试文件**:
- Create: `ConfigTask/review-ui/tests/test_assets_fields.py` — 验证 `build_assets()` 返回的 `by_layer` / `relation_targets` 字段结构正确

---

## Chunk 1: 后端增量字段 + 前端基础改造(端到端可跑通最小集)

### Task 1: 后端 `by_layer` 字段派生 + 测试

**Files:**
- Modify: `ConfigTask/review-ui/serve.py:133-146`(build_assets 函数体)
- Create: `ConfigTask/review-ui/tests/test_assets_fields.py`

**背景:** `by_layer` 是简单的按 `task_layer` 分组 + `_short` 升序。spec §4 已定义 4 个键(atom/compound/feature/generalized),`solution` 层 v2 体系未使用,不在 `by_layer` 出现。

- [ ] **Step 1: 写失败测试(test_assets_fields.py)**

```python
"""测试 serve.build_assets() 返回的 by_layer / relation_targets 字段结构。"""
import sys; sys.path.insert(0, "ConfigTask/review-ui")
from serve import build_assets


def test_by_layer_has_4_keys():
    """by_layer 必须有 atom/compound/feature/generalized 4 个键,solution 不出现。"""
    a = build_assets()
    assert "by_layer" in a
    assert set(a["by_layer"].keys()) == {"atom", "compound", "feature", "generalized"}


def test_by_layer_each_value_is_sorted_sids():
    """by_layer 每个值是 _short id 列表,按 id 升序。"""
    a = build_assets()
    for layer, sids in a["by_layer"].items():
        assert isinstance(sids, list)
        assert sids == sorted(sids), f"{layer} 未按 id 升序: {sids[:5]}..."
        for sid in sids:
            assert sid.split("-")[0].isdigit()  # 形如 "0-00001"


def test_by_layer_counts_match():
    """by_layer 计数应等于对应 task_layer 的 task 数。"""
    a = build_assets()
    from collections import Counter
    layer_counts = Counter(t["task_layer"] for t in a["tasks"])
    for layer in ("atom", "compound", "feature", "generalized"):
        assert len(a["by_layer"][layer]) == layer_counts.get(layer, 0), (
            f"{layer}: by_layer={len(a['by_layer'][layer])} tasks={layer_counts.get(layer, 0)}"
        )
```

- [ ] **Step 2: 跑测试,确认 FAIL**

Run: `cd ConfigTask/review-ui && python -m pytest tests/test_assets_fields.py -v`
Expected: FAIL —— `assert "by_layer" in a` 不通过(当前 `build_assets()` 没返回该字段)

- [ ] **Step 3: 在 `serve.py:build_assets()` 加 `by_layer` 派生**

在 `serve.py` 的 `build_assets()` 内,`tree = build_tree(tasks)` 之后,加:

```python
    # spec §4 by_layer: 按 task_layer 分组,_short 升序
    by_layer = {"atom": [], "compound": [], "feature": [], "generalized": []}
    for t in tasks:
        layer = t.get("task_layer", "")
        if layer in by_layer:
            by_layer[layer].append(t["_short"])
    for layer in by_layer:
        by_layer[layer].sort()
```

然后把 `return {...}` 的 dict 里加 `"by_layer": by_layer`。

- [ ] **Step 4: 跑测试,确认 PASS**

Run: `cd ConfigTask/review-ui && python -m pytest tests/test_assets_fields.py -v`
Expected: PASS —— 3 个测试全过

- [ ] **Step 5: Commit**

```bash
git add ConfigTask/review-ui/serve.py ConfigTask/review-ui/tests/test_assets_fields.py
git commit -m "feat(review-ui): 后端 build_assets 加 by_layer 字段(按 task_layer 分组)"
```

---

### Task 2: 后端 `relation_targets` 字段派生 + 测试

**Files:**
- Modify: `ConfigTask/review-ui/serve.py`(build_assets 函数体,接 Task 1)
- Modify: `ConfigTask/review-ui/tests/test_assets_fields.py`(追加测试)

**背景:** `relation_targets` 是去重 + 排除自身的编排下层 task 集合,与 `tree.children`(单一 parent)互补。spec §4 line 175-195 定义。

- [ ] **Step 1: 追加失败测试**

在 `test_assets_fields.py` 末尾加:

```python
def test_relation_targets_present():
    """relation_targets 是 dict,sid → [引用到的其他 task _short 列表]"""
    a = build_assets()
    assert "relation_targets" in a
    assert isinstance(a["relation_targets"], dict)


def test_relation_targets_excludes_self():
    """任何 task 的 relation_targets 列表都不包含自身 sid"""
    a = build_assets()
    tb = {t["_short"]: t for t in a["tasks"]}
    for sid, targets in a["relation_targets"].items():
        assert sid not in targets, f"{sid} 出现在自己的 relation_targets 中"


def test_relation_targets_sorted_and_unique():
    """每个 task 的 relation_targets 列表去重 + 按 id 升序"""
    a = build_assets()
    for sid, targets in a["relation_targets"].items():
        assert targets == sorted(targets), f"{sid} 未按 id 升序: {targets}"
        assert len(targets) == len(set(targets)), f"{sid} 含重复"


def test_relation_targets_atoms_have_no_dangling():
    """relation_targets 引用的 sid 必须真实存在于 tasks"""
    a = build_assets()
    tb = {t["_short"]: t for t in a["tasks"]}
    for sid, targets in a["relation_targets"].items():
        for t in targets:
            assert t in tb, f"{sid}.relation_targets 含不存在的 {t}"


def test_relation_targets_known_feature_has_compound_or_atom_children():
    """sanity: feature 2-00001 应至少引用 1 个 compound 或 atom(其编排下层)"""
    a = build_assets()
    targets = a["relation_targets"].get("2-00001", [])
    assert len(targets) >= 1
    assert any(t.startswith("1-") or t.startswith("0-") for t in targets), (
        f"2-00001 应编排至少 1 个 compound/atom, 实得 {targets}"
    )
```

- [ ] **Step 2: 跑测试,确认 FAIL**

Run: `cd ConfigTask/review-ui && python -m pytest tests/test_assets_fields.py -v`
Expected: FAIL —— `assert "relation_targets" in a` 不通过

- [ ] **Step 3: 在 `serve.py:build_assets()` 加 `relation_targets` 派生**

紧跟 Task 1 的 `by_layer` 代码后,加:

```python
    # spec §4 relation_targets: 去重 + 排除自身 + 按 id 升序
    relation_targets = {t["_short"]: set() for t in tasks}
    for t in tasks:
        ps = t["_short"]
        for r in (t.get("task_relations") or []):
            for ref in (r.get("from_task_ref"), r.get("to_task_ref")):
                if not ref:
                    continue
                s = ref.split("@")[-1]
                if s != ps and s in relation_targets:
                    relation_targets[ps].add(s)
    relation_targets = {k: sorted(v) for k, v in relation_targets.items()}
```

然后 `return {...}` dict 里加 `"relation_targets": relation_targets`。

- [ ] **Step 4: 跑测试,确认 PASS**

Run: `cd ConfigTask/review-ui && python -m pytest tests/test_assets_fields.py -v`
Expected: PASS —— 8 个测试全过(3 + 5)

- [ ] **Step 5: 验证 `_diag.py` 仍能跑(回归)**

Run: `cd ConfigTask/review-ui && python _diag.py 2>&1 | tail -20`
Expected: 输出悬挂/自环等检查正常,无 KeyError(确认 `tree` / `tree_parent` 字段未被破坏)

- [ ] **Step 6: Commit**

```bash
git add ConfigTask/review-ui/serve.py ConfigTask/review-ui/tests/test_assets_fields.py
git commit -m "feat(review-ui): 后端 build_assets 加 relation_targets 字段(编排下层)"
```

---

### Task 3: 前端 `index.html` 骨架改造

**Files:**
- Modify: `ConfigTask/review-ui/index.html`(全文 ~131 行,部分 CSS + body 结构改)

**背景:** 当前 index.html 是"左 tree + 右 main"两栏布局。要改为"左 3 面板 + 右 main",CSS 加内嵌卡片样式(`.ec`),加阈值常量声明。

- [ ] **Step 1: 改 CSS 区**

`.tree` 容器改为 `.panels`(允许多面板并存)。新增 `.panel`(单个面板)、`.ec`(内嵌卡片)、筛选框样式、`hidden` class。

具体改动参考 spec §10 风险对策行:input min-width: 60%,text-overflow ellipsis 截断。

- [ ] **Step 2: 改 body 结构**

`<aside class="tree">` → `<aside class="panels" id="panels">`(内含 4 个 panel 子元素:atom / compound / feature / generalized)。

- [ ] **Step 3: 加 `<script>` 顶部常量**

```html
<script>
  const CHIP_COLLAPSE_AT = 15;
  const CHIP_COLLAPSE_AT_LIGHT = 8;
  const PANEL_WIDTH = 110;
</script>
<script type="module" src="app.js"></script>
```

- [ ] **Step 4: 浏览器打开检查无 JS 报错**

Run: `cd ConfigTask/review-ui && python serve.py 8765`,浏览器开 `http://localhost:8765`,DevTools Console 应无报错(此时 app.js 还没改,左面板会空白但应不报错)。

- [ ] **Step 5: Commit**

```bash
git add ConfigTask/review-ui/index.html
git commit -m "feat(review-ui): index.html 改造——三面板容器+内嵌卡片样式+阈值常量"
```

---

### Task 4: 前端 `app.js` 重写核心逻辑

**Files:**
- Modify: `ConfigTask/review-ui/app.js`(全文 ~288 行,重写)

**背景:** 这是最大一块。分 4 个 sub-step 渐进 commit。

- [ ] **Sub-step 4.1: 状态对象 + 数据装载 + 索引构建**

替换 app.js 顶部状态声明 + init() 函数:

```js
let DATA = null, REV = null, CUR = null, FOCUS = 'main';
const TBY = {}, DPS_BY = {}, RULES_BY = {};
const CHIP_COLLAPSE_AT = window.CHIP_COLLAPSE_AT || 15;
const CHIP_COLLAPSE_AT_LIGHT = window.CHIP_COLLAPSE_AT_LIGHT || 8;

async function init() {
  const [a, r] = await Promise.all([
    fetch("/api/assets").then(x => x.json()),
    fetch("/api/review-state").then(x => x.json())
  ]);
  DATA = a; REV = r;
  $("nfver").textContent = DATA.nf_version;
  for (const t of DATA.tasks) TBY[t._short] = t;
  for (const r of DATA.rules) {
    const o = short(r.owner_task_ref || "");
    (RULES_BY[o] = RULES_BY[o] || []).push(r);
  }
  for (const d of DATA.dps) {
    const o = short(d.owner_task_ref || "");
    (DPS_BY[o] = DPS_BY[o] || []).push(d);
  }
  renderStats();
  renderPanels();
  go(DATA.by_layer.feature[0] || DATA.by_layer.atom[0], true);
}
```

- [ ] **Sub-step 4.2: renderStats() + renderPanels()**

`renderStats()` 保留但简化(去 `tree.dfs_order` 引用,改用 `tasks.length`)。
`renderPanels()` 新建,渲染 4 个面板(只对前 3 个 + generalized 单项)。每个面板顶部 input 筛选框。

- [ ] **Sub-step 4.3: go(sid) + FOCUS 自动跟随 + navPrev/navNext 改面板内**

`go(sid)` 末尾加 `FOCUS = TBY[sid]?.task_layer || 'main'`。
`navPrev` / `navNext` 改为读 `FOCUS` + `DATA.by_layer[FOCUS]` 列表,找不到则 toast '无可切换 task'。

- [ ] **Sub-step 4.4: renderMain(sid) 重写——主 card + 内嵌子卡片 3 层嵌套 + 折叠**

按 spec §3.4 / §3.7 实现 `renderChildren(sids, depth)` + `renderTaskCard(task, depth)` + L2 默认折叠 + L3 chip 折叠 + L1 内嵌区两级折叠。

- [ ] **Sub-step 4.5: 键盘 handler 改造**

`keydown` handler 改:
- `1/2/3`:仅当 `e.target.tagName !== 'TEXTAREA'` 时才 postReview
- `Tab`:`FOCUS = {atom: 'compound', compound: 'feature', feature: 'main', main: 'atom'}[FOCUS] || 'atom'`
- `Ctrl+F` / `Ctrl+P`:不监听(浏览器原生)

- [ ] **Sub-step 4.6: 事件 delegation**

更新 `click` delegation,加 `data-act="toggle-l2"` 处理 L2 卡片折叠切换。

- [ ] **Step 5: Commit**

```bash
git add ConfigTask/review-ui/app.js
git commit -m "feat(review-ui): app.js 重写——三面板 + 主区内嵌子卡片 3 层 + FOCUS/折叠"
```

---

### Task 5: 端到端 smoke 验证(spec §7.1 13 步)

**Files:** 无文件改动,纯手工验证

- [ ] **Step 1: 启动 serve**

Run: `cd ConfigTask/review-ui && python serve.py 8765`,浏览器开 `http://localhost:8765`

- [ ] **Step 2-14: 按 spec §7.1 13 步逐条验证**

具体步骤见 spec §7.1 line 271-285。每步 pass 在该 step 前的 checkbox 标 [x]。

- [ ] **Step 15: Commit 验收报告(如有问题)**

若 smoke 全过,本任务结束。
若有 bug,在 `ConfigTask/review-ui/tests/test_smoke_results.md` 写实测结果,后续修。

---

## 总 Commit 列表(预期)

1. `feat(review-ui): 后端 build_assets 加 by_layer 字段(按 task_layer 分组)` (Task 1)
2. `feat(review-ui): 后端 build_assets 加 relation_targets 字段(编排下层)` (Task 2)
3. `feat(review-ui): index.html 改造——三面板容器+内嵌卡片样式+阈值常量` (Task 3)
4. `feat(review-ui): app.js 重写——三面板 + 主区内嵌子卡片 3 层 + FOCUS/折叠` (Task 4)

---

## 验证矩阵(spec §7 对齐)

| spec 验证项 | 本 plan 对应 | 状态 |
|---|---|---|
| §7.1 13 步 smoke | Task 5 | 待执行 |
| §7.2 `review-state.json` 字段不变 | Task 2 (无修改) | 自动保证 |
| §7.2 `tree` 字段保留供 nav/diag | Task 2 (build_tree 不动) | Step 5 验证 |
| §7.3 不引入 pytest 套件 | 仅 1 个测试文件(字段派生) | 符合 |
| §7.3 `_diag.py` 保留 | Task 2 Step 5 跑通 | 验证 |

---

## 风险与对策

| 风险 | 对策 |
|---|---|
| app.js 重写引入 JS 报错 | Task 4 拆 6 个 sub-step,每步浏览器开 Console 验;先做骨架,再补功能 |
| L1 内嵌区两级折叠实现时算错总高 | spec §3.7 已给阈值(8/15),按字面实现;Task 5 smoke 验证 |
| 前端无 pytest 覆盖 | Task 1+2 后端测试 8 项覆盖字段派生;前端 13 步手工 smoke(spec §7.1) |
| FOCUS 数据环与 DOM focus 失同步 | spec §3.6 已规定解耦;Tab 只更数据环,DOM focus 由用户点击触发 |
| `relation_targets` 与 `tree.children` 命名混淆 | spec §4 line 183 已显式说明;Task 2 测试 case `test_relation_targets_known_feature_has_compound_or_atom_children` 防御 |