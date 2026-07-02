# Review UI 按级别拆分目录 + 主区内嵌子卡片

> **日期**:2026-07-02
> **范围**:仅 `ConfigTask/review-ui/`(3 个文件改写:`index.html` / `app.js` / `serve.py`)
> **不动的资产**:`task-assets/UDG/20.15.2/` 所有 yaml、`review-state.json` 已有记录
> **设计模式**:左侧 3 面板平铺 + 主区内嵌子卡片(3 层嵌套上限)
> **状态**:brainstorming 5 段确认 → 待 spec 评审 → 用户 review → 转 writing-plans

---

## 1. 背景与动机

### 1.1 现状
`review-ui/` 当前以"父子树"为左侧目录主轴(`DATA.tree.dfs_order` 全 302 task 排成一个深度优先序列),用户点开某个 feature 后要逐层下钻才能看到它编排的所有 atom。90 个 feature × 平均 3.7 个编排边 × 24 个 compound × 平均 6.7 个 atom,导致审查流程被迫"频繁跳转",而人工审查的核心诉求是 **看一个 task 时,其 rule + 决策点 + 相关其他 task 全部局内可见**。

### 1.2 痛点
- 左侧父子树让"看 command 的全貌"被埋在 feature 下,先要点开 feature 才能看到 atom,而 atom 是要被高频交叉审查的对象(187 个,按 COMMAND_REVIEW_BASELINE.md 主线)
- 右侧当前已经显示 DP/rule/父/子/兄弟/复用面,但:
  - "兄弟"对审查无价值,占视觉空间
  - "复用面"只显示 chip,不显示 task_logical_name,要点过去才知道是谁在用
  - 看 compound 时看不到其编排下的 atom(只看到 chip,要跳转才能看)
  - 看 feature 时看不到其编排下的 compound(同样要跳转)

### 1.3 目标
让审查者**按级别独立走查**:命令面板走 atom 187 个、步骤面板走 compound 24 个、特性面板走 feature 90 个,跨级别通过右侧主区内嵌子卡片**一屏内**看到其编排下层。

---

## 2. 设计决策(brainstorming 已确认)

| # | 决策项 | 选择 |
|---|---|---|
| 1 | 左侧目录结构 | 3 个面板同时平铺(命令 / 步骤 / 特性),顶部辅以统计栏 |
| 2 | 面板内顺序 | 按 task_id 升序(0-00001 → 0-00187 / 1-00001 → 1-00024 / 2-00001 → 2-00092) |
| 3 | 右侧详情信息 | 保留全部现有 + 去除"兄弟"行(无价值) + 复用面显示 task_logical_name |
| 4 | 核心准则 | task 展示时,其 rule + 决策点 + 相关其他 task **局内展示**(不靠跳转) |
| 5 | 子节点展现 | **内嵌卡片式**(3 层嵌套上限) |
| 6 | verdict 按钮位置 | 主 card 顶部带按钮,内嵌 chip 只读不按钮 |
| 7 | 数据契约 | `review-state.json` 字段不变,`/api/assets` 只加字段不删字段 |

---

## 3. 架构

### 3.1 三层架构

```
Browser:
  index.html  ─ 静态骨架(三面板 + 主区 + 审查区 + toast)
  app.js      ─ 渲染逻辑(纯 module + DOM,无框架)

Server:
  serve.py    ─ HTTP 端点(已存在 3 个,本设计增量字段)
                GET  /api/assets        ← 字段扩展
                GET  /api/review-state  ← 不动
                POST /api/review        ← 不动

资产(只读,serve.py 启动时一次性加载,运行期不变):
  task-assets/UDG/20.15.2/
    tasks/*.yaml            ← Task 对象(主数据)
    decision_points/*.yaml  ← DecisionPoint
    task_rules/*.yaml       ← TaskRule
    review-state.json       ← 审查记录(人工改 + 自动同步,字段不变)
    review/manual-feedback.md ← 镜像(serve.py 自动追加,字段不变)
```

### 3.2 渲染组件清单(8 个,标 new/rewrite/unchanged)

| 组件 | 状态 | 职责 | 输入 | 输出 |
|---|---|---|---|---|
| `renderStats()` | unchanged | 顶部统计栏 | DATA, REV | 计数 + 进度条 |
| `renderLeftPanel()` | **rewrite** | 三面板左侧目录 + 简化筛选框 | DATA, CUR, FOCUS | 三栏 UL 列表 |
| `renderMain(sid)` | **rewrite** | 主区:主 card + 内嵌 + 审查区 | DATA, REV | 主区 html |
| `renderTaskCard(task, max_depth)` | **new** | 内嵌 L2 卡片(只读变体,可折叠) | task + 嵌套深度 | 简化卡片 html |
| `renderChildren(sids, depth)` | **new** | 内嵌子卡片列表(L2/L3) | sid 数组 + 嵌套深度 | 嵌套 html |
| `renderDP(dp)` | unchanged | DP 卡片 | dp | dp html |
| `renderRule(rule)` | unchanged | 规则卡片 | rule | rule html |
| `renderReview(sid)` | unchanged | 审查区 | sid, status | verdict 按钮 + note + 历史 |

### 3.3 数据流

**加载流程**:
```
init() {
  GET /api/assets
  GET /api/review-state
  → DATA, REV
  → renderStats()
  → renderLeftPanel()        // 3 面板立即可见
  → go(initialSid)            // 进入默认 task
}
```

**go(sid) 流程**:
```
go(sid) {
  CUR = sid
  renderLeftPanel()            // 高亮 CUR + 滚动到可视
  renderMain(sid)              // 替换主区
}
```

**postReview(verdict) 流程**:
```
postReview(v) {
  POST /api/review { object_id: CUR, verdict, note }
  → 后端追加 review-state.json
  → 后端镜像 manual-feedback.md
  → 返回 records
  → REV.records[CUR] = records
  → renderStats()
  → renderLeftPanel()          // 左侧统计更新
  → renderMain(CUR)            // 主区 status 更新
  → toast('已记录:' + verdict)
}
```

### 3.4 嵌套规则(3 层上限)

L1 主 card 显示完整信息:intent / ref / status / category / 参数绑定表 / 编排边 / DP / rule / 复用面 / 审查

L2 内嵌卡片:编排下层 task 卡片(只读变体,无 verdict 按钮),显示 id / name / status / ref / 参数数 / 编排边数。**L2 卡片自身可再内嵌其编排下层**——但只到 L3。

L3 内嵌卡片:编排下下层 task chip(纯跳转,不嵌卡片),只显示 id + name + status。

具体嵌套深度由 `max_depth` 参数控制:
- L1 主 card 永远 max_depth=0(自身内容)
- 主 card 的编排边渲染时,以 max_depth=2 调 `renderChildren(sids, 2)`
- L2 子卡片在自己的渲染中,以 max_depth=1 调 `renderChildren(sids, 1)`
- L3 调用时 depth=0,只生成 chip,不再嵌卡片

```
主 card  (max_depth=2  → 渲染自己的编排下层为 L2 卡片)
  └─ L2 子卡片  (max_depth=1  → 渲染自己的编排下层为 L3 chip, 默认折叠)
       └─ L3 chip  (depth=0  → 不再渲染)
```

**视觉硬约束(防止嵌套爆炸)**:
- L2 卡片**默认折叠**其编排下层(L3 chip 列),点 L2 卡片标题区展开。
- L2 卡片折叠态展示摘要:`▸ 1-00001 计费三件套 (5 atom · 3 通过, 2 待审)`。
- L2 卡片展开后,L3 chip 总数 > 15 时只展示前 5 + "展开更多" 按钮,点开后才显示全部(阈值在 index.html `<script>` 顶部常量,默认 15)。
- "编排下层"指**该 task 的 `task_relations[]` 中 from/to_task_ref 指向的所有其他 task(去重,排除自身,按 id 升序)**——不区分 relation_type、不区分 requiredness,因为审查视角是"该 task 涉及的全部下层",而不是"必走的边"。
- 主 card 的"复用面"(该 atom 被哪些 feature 引用)同样适用 > 20 chip 折叠策略(阈值与 L3 折叠一致,均为 15)。

### 3.5 关键交互

| 操作 | 行为 |
|---|---|
| 点击左面板任意项 | `go(sid)`(CUR 切到该 task,FOCUS 跟随切到对应面板,左侧高亮,主区重渲染) |
| 点击主 card(空白处) | 无操作(只是当前焦点) |
| 点击内嵌 chip | `go(sid)`(跳转) |
| 点击 L2 卡片标题区 | 切换其编排下层 L3 chip 列的展开/折叠 |
| 点击主 card verdict 按钮 | `postReview(v)` |
| 输入 note | 留在 textarea,提交时随 verdict 上送 |
| 键盘 ← / → | 在 **FOCUS 对应面板**的 `by_layer` 列表内 prev/next;FOCUS='main' 时不响应 |
| 键盘 1 / 2 / 3 | 主 card verdict(通过 / 驳回 / 待补),与 FOCUS 无关,始终作用于 CUR |
| 键盘 Tab | 在三面板 + 主区焦点环循环切换(FOCUS 顺序:atom → compound → feature → main → atom) |
| 浏览器 Ctrl+F | 仍可用(节点文本含 task_logical_name);左面板定位靠面板内简化版筛选框(见 §9.1) |

---

## 4. 后端增量字段

`serve.py` 的 `build_assets()` 增加 2 个字段,**原有字段全部保留**(特别是 `tree` 全保留供 nav 与 `_diag.py` 使用):

```python
{
  ...原有字段(nf_version, tasks, dps, rules, reuse, tree),
  "by_layer": {
    "atom": [短 id 列表, 按 id 升序],
    "compound": [...],
    "feature": [...],
    "generalized": [...]      # UDG@20.15.2 当前仅 1 项;`solution` 层 v2 体系未使用
  },
  "relation_targets": {
    "0-00001": ["0-00002", "0-00003"],   # 该 task 的 task_relations 引用到的所有其他 task 短 id(去重 + 排除自身 + 按 id 升序)
    "1-00001": ["0-00001", "0-00002", ...],
    ...
  }
}
```

**字段命名说明**:原草稿用 `embedded_children`,与 `tree.children` 命名相近易混淆,正式命名为 `relation_targets`——语义更直白"该 task 经 task_relations 引用到的所有 task 集合"。

**计算逻辑**:
- `by_layer`:遍历 `tasks`,按 `task_layer` 字段分组,各组内按 `_short`(task_id 末段)升序排序
- `relation_targets`:遍历每个 task 的 `task_relations[]`,取 `from_task_ref / to_task_ref` 短 id,去重,排除自身,按 id 升序排序

**与 `tree.children` 的关系(明确分工)**:
- `tree.children[sid]` = 父子树视角下的**单一**直接父-子(每个 child 恰一个 parent,按 `build_tree` 的"最近上层优先"规则)。**保留**——供前端 `navPrev`/`navNext`(基于 `tree.dfs_order`)与 `_diag.py`(基于 `tree.tree_parent` 做悬挂/自环检查)使用。
- `tree.containers[sid]` = 父子树视角下的**全部**上层引用方(可多个)。**保留**——供前端做"父/引用方 chips"展示。
- `relation_targets[sid]` = 编排视角下的**全部**下层(可多层跨层引用,如 feature→atom 直接 precedes;不区分 relation_type、不区分 requiredness)。**新增**——供前端 `renderChildren` 做内嵌渲染。
- 三者并存不重复:`tree.*` 单一视角 + 多引用方视角,`relation_targets` 全下层视角,互为补充。

**`build_tree` / `build_reuse` 函数保留**:`serve.py` 中这两个函数不被删除,因为 `_diag.py` 仍依赖 `tree.tree_parent` / `tree.children` 做悬挂与自环检查(详见 §7.2)。

---

## 5. 前端实现要点

### 5.1 状态对象

```js
let DATA = null;        // GET /api/assets
let REV = null;         // GET /api/review-state
let CUR = null;         // 当前主 card task 的 _short
let FOCUS = 'main';     // 焦点环:main / atom / compound / feature / generalized, Tab 切换
const TBY = {};         // _short → task 索引
const DPS_BY = {};      // _short → DP[] 索引(已存在)
const RULES_BY = {};    // _short → rule[] 索引(已存在)
const CHIP_COLLAPSE_AT = 15;   // chip 列阈值常量(放 index.html <script> 顶部)
```

**FOCUS 转移规则**(补 §3.5 缺口):
- `go(sid)` 时:根据 `TBY[sid].task_layer` 自动设 `FOCUS = layer`(如 `go('0-00001')` → `FOCUS='atom'`)
- 键盘 Tab:循环切 `atom → compound → feature → main → atom`(generalized 项只有 1 个,不进焦点环)
- 键盘 ←/→:仅当 `FOCUS ∈ {atom, compound, feature}` 时响应,在对应 `DATA.by_layer[FOCUS]` 列表内 prev/next

### 5.2 渲染函数签名

```js
function renderLeftPanel() -> void
function renderMain(sid: string) -> void
function renderTaskCard(task, max_depth: int) -> string  // 返回 html 字符串
function renderChildren(sids: string[], depth: int) -> string  // 返回 html 字符串(编排下层渲染,从 DATA.relation_targets 取)
```

**L2 卡片折叠状态**:折叠态用 DOM `hidden` 属性或 class 切换,初始 `hidden=true`(默认折叠),点 L2 卡片标题区切。

### 5.3 复用面渲染改进

原 chip 列表只显示 id,改为显示 `id + task_logical_name + status 图标`:
```
▸ 2-00002 在线计费 [✓]    而不是   2-00002 在线计费
▸ 2-00003 离线计费 [·]
```

### 5.4 内嵌卡片样式

复用现有 `.dp` 卡片样式,但加 `.ec` 类(embedded card):
- 默认显示:task_id + name + status icon + ref + 参数数 + 编排边数
- hover 时高亮 + tooltip 提示"点击主 card 跳转"
- cursor:default(L2 卡片不可整体点击)
- 内部 L3 chip 仍用 `.chip` 类,可点击

### 5.5 不再渲染的元素

- "兄弟"行(对审查无价值) — 直接删除
- `renderTree()` 中父子树渲染 — 三面板替换
- `_diag.py` 使用的 `tree.tree_parent` 仍保留(供调试)

---

## 6. 错误处理

| 错误 | 处理 |
|---|---|
| `GET /api/assets` 失败 | 主区显示 empty '审查服务未响应(请在 review-ui 目录运行 python serve.py)' |
| `GET /api/review-state` 失败 | REV = 空对象,所有 status 默认 '待审查',功能可用但不持久化 |
| `POST /api/review` 失败(网络/400) | toast '提交失败:' + msg,note 文本保留在 textarea |
| 单 yaml 解析失败 | serve.py 已有(`_error` 字段),前端过滤不渲染,正常渲染其他 |
| 点 chip 找不到 task | toast 'task 不存在:' + sid,不渲染主区 |
| CUR 非法 hash(刷新时) | `go()` 兜底 `if (!sid || !TBY[sid]) sid = DATA.by_layer.feature[0]` |

---

## 7. 验证

### 7.1 手工 smoke(13 步)

```
1. 启动 python review-ui/serve.py 8765
2. 浏览器开 http://localhost:8765
3. 验证三面板全部可见,计数正确(187 / 24 / 90 / 1 generalized)
4. 点 atom 0-00001 → 主区显示完整信息 + 复用面(含 logical_name)
5. 点 feature 2-00001 → 主区显示编排 + 内嵌 compound 卡片(默认折叠)
6. 点 2-00001 内嵌的 1-00001 卡片标题区 → 展开 L3 chip 列
7. 点 chip 0-00001 → 跳转到 atom 主 card(FOCUS 跟随切到 atom)
8. 点主 card [✕ 驳回] + note → review-state.json 追加一行 + manual-feedback.md 追加
9. 刷新 → status 保留
10. 键盘 ← / → → 在当前 FOCUS 面板内切换 task
11. 键盘 1 / 2 / 3 → 主 card verdict(确认 key handler 未被 textarea 吞掉)
12. 终端跑 python review-ui/_diag.py → 无报错(确认 build_tree / build_reuse 仍存在)
13. 点面板内筛选框,输入"计费" → 该面板仅显示命中项
```

### 7.2 回归兼容

- `review-state.json` 字段不变 → 升级安全
- `/api/assets` 字段只加不删(`by_layer` / `relation_targets` 新增;`tree` 等旧字段保留) → 前端可平滑升级
- `_diag.py` 仍能跑(`serve.py` 中 `build_tree` / `build_reuse` 函数体保留,因为 `_diag.py` 依赖 `tree.tree_parent` / `tree.children` 做悬挂与自环检查)
- `_serve_nobrowser.py` / `_render.py` 不动(serve.py 内部接口不变)

### 7.3 自动化测试

- 不引入 pytest 套件(单文件改动 < 500 行,手工 smoke 已覆盖)
- `_diag.py` 保留为最小回归工具(检查悬挂/自环/多 atom,不变)

---

## 8. 关键文件改动清单

| 文件 | 改动类型 | 影响行数预估 |
|---|---|---|
| `review-ui/index.html` | 微调(去掉 .tlegend 父树图例,加 3 面板容器 + 简化筛选框 input) | ~40 行 |
| `review-ui/app.js` | 重写(`renderTree` → `renderLeftPanel`;新增 `renderChildren` / `renderTaskCard`;删兄弟渲染;加 FOCUS + Tab 焦点环) | ~500 行 |
| `review-ui/serve.py` | 增量(`build_assets()` 加 `by_layer` / `relation_targets` 字段;`build_tree` / `build_reuse` 函数体保留不动) | ~40 行 |
| `review-ui/_diag.py` | 不动 | 0 |
| `review-ui/_render.py` | 不动 | 0 |
| `review-ui/_serve_nobrowser.py` | 不动 | 0 |

---

## 9. 不在本设计范围

- UNC 网元(本设计仅 UDG@20.15.2,与现状一致)
- 自动化测试套件(手工 smoke 覆盖)
- 后端持久化方案升级(仍用 review-state.json + manual-feedback.md)
- 审查 UI 的外部 API(只读 index.json,不动 Task 资产)
- 数据契约破坏性变更(`review-state.json` 字段不动)
- `review-state.json` 的 `reviewer` 字段:仍写 `"人工"`(与现状一致,本设计不动)
- `manual-feedback.md` 模板:仍用 SKILL §8.2 模板("反哺Skill条款: (待 Agent 下一 pass 归类)"),本设计不动
- `_serve_nobrowser.py` / `_render.py`:保留(serve.py 自动调 webbrowser 时无 GUI 的兜底;_render.py 是命令行预览工具),本设计不动

### 9.1 保留的左面板简化筛选框
原 UI 的 `tfilter` 输入框(在父树根部的 id/名 筛选)——**保留简化版**,不放树而直接对 `by_layer` 列表做模糊匹配:
- 每面板顶部一个 input,只过滤该面板内的 task(`id + logical_name` 子串匹配,大小写不敏感)
- 实现成本 ~20 行 JS,回报:审查者定位"在线计费"无需滚动 90 项 feature
- 与 Ctrl+F 浏览器原生搜索互补(原生搜全页主区;面板框只搜该面板列表)

---

## 10. 风险与对策

| 风险 | 对策 |
|---|---|
| 嵌入卡片层级过深导致主区滚动过长 | 3 层硬上限 + L2 卡片**默认折叠**其编排下层(§3.4) |
| 复用面 / L3 chip 数量爆炸(atom 0-00019 被 60 feature 用) | 阈值常量 `CHIP_COLLAPSE_AT = 15`(§5.1),超阈值折叠为"前 5 + 展开更多";主区复用面与编排下层共用同一阈值,视觉一致 |
| verdict 误点(主 card 一旦点驳回影响范围大) | verdict 仅作用于当前 task 短 id;UI 上 toast 确认已记录 |
| review-state.json 字段变更破坏升级 | 本设计字段只加不删,review-state 完全不动 |
| 三面板宽度挤压主区 | 左侧 3 面板总宽 ≤ 360px(每栏 ~110px,带竖滚动);主区 ≥ 600px(响应式自适应) |

---

## 11. 设计准则引用

- 静态三层不可变(Task / DP / rule 资产 yaml 不动)— SKILL §0 边界规则
- `review-state.json` 是审查唯一真相源(RUNBOOK §7)
- 审查 verdict 由人给,Agent 自审仅辅助(SKILL §8 闭环)
- verdict 通过镜像 manual-feedback.md 反哺 SKILL(SKILL §8.2 / §9)