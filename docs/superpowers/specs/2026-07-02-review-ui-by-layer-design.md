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

### 3.2 渲染组件清单

| 组件 | 职责 | 输入 | 输出 |
|---|---|---|---|
| `renderStats()` | 顶部统计栏 | DATA, REV | 计数 + 进度条(已存在) |
| `renderLeftPanel()` | 三面板左侧目录 | DATA, CUR | 三栏 UL 列表(本设计重写) |
| `renderMain(sid)` | 主区:主 card + 内嵌 + 审查区 | DATA[by_layer], DATA[embedded_children], REV | 主区 html(本设计重写) |
| `renderTaskCard(task)` | 内嵌卡片(只读 chip 变体) | task 对象 | 简化卡片 html(本设计新增) |
| `renderChildren(sids, depth)` | 内嵌子卡片列表 | sid 数组 + 嵌套深度(0/1/2) | 嵌套 html(本设计新增) |
| `renderDP(dp)` | DP 卡片 | dp | dp html(已存在) |
| `renderRule(rule)` | 规则卡片 | rule | rule html(已存在) |
| `renderReview(sid)` | 审查区 | sid, status | verdict 按钮 + note + 历史(已存在) |

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
  └─ L2 子卡片  (max_depth=1  → 渲染自己的编排下层为 L3 chip)
       └─ L3 chip  (depth=0  → 不再渲染)
```

### 3.5 关键交互

| 操作 | 行为 |
|---|---|
| 点击左面板任意项 | `go(sid)`(CUR 切到该 task,左侧高亮,主区重渲染) |
| 点击主 card(空白处) | 无操作(只是当前焦点) |
| 点击内嵌 chip | `go(sid)`(跳转) |
| 点击主 card verdict 按钮 | `postReview(v)` |
| 输入 note | 留在 textarea,提交时随 verdict 上送 |
| 键盘 ← / → | 在**当前所在面板**内 task_id 序列切换 |
| 键盘 1 / 2 / 3 | 主 card verdict(通过 / 驳回 / 待补) |
| 键盘 Tab | 在三面板 + 主区焦点环切换 |
| 浏览器 Ctrl+F | 仍可用(节点文本含 task_logical_name) |

---

## 4. 后端增量字段

`serve.py` 的 `build_assets()` 增加 2 个字段,**原有字段全部保留**:

```python
{
  ...原有字段(nf_version, tasks, dps, rules, reuse, tree),
  "by_layer": {
    "atom": [短 id 列表, 按 id 升序],
    "compound": [...],
    "feature": [...],
    "generalized": [...]
  },
  "embedded_children": {
    "0-00001": ["0-00002", "0-00003"],   # 该 task 编排的下层 task 短 id 列表, 去重 + 排序
    "1-00001": ["0-00001", "0-00002", ...],
    ...
  }
}
```

**计算逻辑**:
- `by_layer`:遍历 `tasks`,按 `task_layer` 字段分组,各组内按 `_short`(task_id 末段)排序
- `embedded_children`:遍历每个 task 的 `task_relations[]`,取 `from_task_ref / to_task_ref` 短 id,去重,排除自身,按 id 排序

**与 `tree.children` 的关系**:
- `tree.children[sid]` = 父子树视角下的直接子(一个 parent)
- `embedded_children[sid]` = 编排视角下的所有下层(可能含多层跨层引用,如 feature→atom 直接 precedes)
- 两者**不冲突**:前者用于树渲染(本设计已弃用),后者用于内嵌渲染(本设计新增)

---

## 5. 前端实现要点

### 5.1 状态对象

```js
let DATA = null;     // GET /api/assets
let REV = null;      // GET /api/review-state
let CUR = null;      // 当前主 card task 的 _short
let FOCUS = 'main';  // 焦点环:main / atom / compound / feature, Tab 切换
const TBY = {};      // _short → task 索引
const DPS_BY = {};   // _short → DP[] 索引(已存在)
const RULES_BY = {}; // _short → rule[] 索引(已存在)
```

### 5.2 渲染函数签名

```js
function renderLeftPanel() -> void
function renderMain(sid: string) -> void
function renderTaskCard(task, max_depth: int) -> string  // 返回 html 字符串
function renderChildren(sids: string[], depth: int) -> string  // 返回 html 字符串
```

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
| `GET /api/assets` 失败 | toast '加载失败,请重试' + 主区显示 empty '资产加载失败,检查 serve.py 是否运行' |
| `GET /api/review-state` 失败 | REV = 空对象,所有 status 默认 '待审查',功能可用但不持久化 |
| `POST /api/review` 失败(网络/400) | toast '提交失败:' + msg,note 文本保留在 textarea |
| 单 yaml 解析失败 | serve.py 已有(`_error` 字段),前端过滤不渲染,正常渲染其他 |
| 点 chip 找不到 task | toast 'task 不存在:' + sid,不渲染主区 |
| CUR 非法 hash(刷新时) | `go()` 兜底 `if (!sid || !TBY[sid]) sid = DATA.by_layer.feature[0]` |

---

## 7. 验证

### 7.1 手工 smoke(10 步)

```
1. 启动 python review-ui/serve.py 8765
2. 浏览器开 http://localhost:8765
3. 验证三面板全部可见,计数正确(187 / 24 / 90)
4. 点 atom 0-00001 → 主区显示完整信息 + 复用面(含 logical_name)
5. 点 feature 2-00001 → 主区显示编排 + 内嵌 compound 卡片
6. 2-00001 内嵌的 1-00001 卡片 → 含其编排下的 atom chip 列表
7. 点 chip 0-00001 → 跳转到 atom 主 card
8. 点主 card [✕ 驳回] + note → review-state.json 追加一行 + manual-feedback.md 追加
9. 刷新 → status 保留
10. 键盘 ← / → → 在当前面板内切换 task
```

### 7.2 回归兼容

- `review-state.json` 字段不变 → 升级安全
- `/api/assets` 字段只加不删 → 前端可平滑升级
- `_diag.py` 仍能跑(serve.py 内部函数 `build_tree` / `build_reuse` 保留)

### 7.3 自动化测试

- 不引入 pytest 套件(单文件改动 < 500 行,手工 smoke 已覆盖)
- `_diag.py` 保留为最小回归工具(检查悬挂/自环/多 atom,不变)

---

## 8. 关键文件改动清单

| 文件 | 改动类型 | 影响行数预估 |
|---|---|---|
| `review-ui/index.html` | 微调(去掉 .tlegend 父树图例,加 3 面板容器) | ~30 行 |
| `review-ui/app.js` | 重写(renderTree → renderLeftPanel;新增 renderChildren/renderTaskCard) | ~500 行 |
| `review-ui/serve.py` | 增量(`build_assets()` 加 by_layer / embedded_children 字段) | ~30 行 |
| `review-ui/_diag.py` | 不动 | 0 |
| `review-ui/_render.py` | 不动 | 0 |
| `review-ui/_serve_nobrowser.py` | 不动 | 0 |

---

## 9. 不在本设计范围

- UNC 网元(本设计仅 UDG@20.15.2,与现状一致)
- search 栏(原 UI 有 tfilter,本设计移除,改用 Ctrl+F 浏览器原生)
- 审查 UI 的外部 API(只读 index.json,不动 Task 资产)
- 数据契约破坏性变更(`review-state.json` 字段不动)
- 后端持久化方案升级(仍用 review-state.json + manual-feedback.md)
- 自动化测试套件(手工 smoke 覆盖)

---

## 10. 风险与对策

| 风险 | 对策 |
|---|---|
| 嵌入卡片层级过深导致主区滚动过长 | 3 层硬上限,L3 强制 chip 不再嵌 |
| 复用面 chip 数量爆炸(atom 0-00019 被 60 个 feature 用) | chip 列超 20 时折叠为"前 20 + 展开更多" |
| verdict 误点(主 card 一旦点驳回影响范围大) | verdict 仅作用于当前 task 短 id;UI 上确认 verdict 后才显示 |
| review-state.json 字段变更破坏升级 | 本设计字段只加不删,review-state 完全不动 |
| 三面板宽度挤压主区 | 左侧 3 面板总宽 ≤ 320px(每栏 ~100px,带竖滚动) |

---

## 11. 设计准则引用

- 静态三层不可变(Task / DP / rule 资产 yaml 不动)— SKILL §0 边界规则
- `review-state.json` 是审查唯一真相源(RUNBOOK §7)
- 审查 verdict 由人给,Agent 自审仅辅助(SKILL §8 闭环)
- verdict 通过镜像 manual-feedback.md 反哺 SKILL(SKILL §8.2 / §9)