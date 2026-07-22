# 测试用例管理平台设计（数据飞轮·数据层）

**日期**：2026-07-22
**状态**：已对齐，实现中
**定位**：挂在现有 graph-asset-platform 上的**独立子系统**，作为数据飞轮的"数据层"。

## 1. 背景与目标

图谱已建好。要让它在实际使用中越转越准（数据飞轮），需要：
1. 面向业务域构建 input/output 测试集；
2. Agent 跑测试 → 产出存平台；
3. 人工（现在）/ Agent（未来预留）审查 → 意见存平台；
4. 另一个 Agent 基于审查意见定位图谱问题 → 反向改图谱（= **修正 SOP**，独立入口，不在本 spec）。

本 spec 只管**第 1~3 步的管理与展示**。第 4 步消费本 spec 产出的 Review md。

## 2. 隔离边界（硬约束）

用户唯一硬要求：**隔离，已有图谱资产（前端+后端）零改动**。

**后端**：新增 `app/tests/` 包 + `app/routers/tests.py`，**完全不 import 图谱 app 代码**（md 解析器复制一份进 `tests/parser.py`，不共享）。只读写 `platform-data/tests/`，绝不碰 `platform-data/assets/`。独立索引、独立锁、独立 Service 单例。增量接线：`main.py` 注册路由 + lifespan 构建 TestService；`config.py` 加一行 `TESTS_DIR`。

**前端**：新增 `src/tests-module/`（独立 views/components/composable），路由 `/tests/*` 独立，顶部第 4 菜单「测试」。只复用通用原语（Element Plus、md 渲染器），不复用图谱专属组件。

**跨子系统"图谱对象名渲染"**：由前端直接调图谱现有 `GET /names`——后端两侧零耦合。

## 3. 数据模型

### 3.1 目录结构（`platform-data/tests/`，不入 git）

```
platform-data/tests/
├── cases/{domain}/{scenario}/TestCase@{slug}.md     # 用例（SA 手写）
├── runs/{TestCaseID}/{RunID}/                        # 一次运行 = 一个文件夹
│   ├── {RunID}.md
│   ├── config.txt   # SKILL 生成的 MML
│   ├── 方案.md
│   └── LLD.md
└── reviews/{RunID}/Review@{slug}.md                   # 审查（人工 UI / 未来 Agent）
```

### 3.2 ID 规范

| 类型 | 格式 | 例 |
|---|---|---|
| TestCase | `TestCase@{slug}` | `TestCase@charging-offline-basic` |
| Run | `Run@{case-slug}-{YYYYMMDDHHMM}-{rand4}` | `Run@charging-offline-basic-202607221030-a1b2` |
| Review | `Review@{run-slug}-{seq}` | `Review@...-a1b2-01` |

### 3.3 字段必需性（**降级原则·核心**）

> **路径 + 文件名 = 骨架（强约束，系统靠它识别/分组）；YAML + 正文 = "有就用、没有就降级"，全部不硬要求。**

| 字段 | 必需性 | 缺了怎么办 |
|---|---|---|
| id | 强 ← 文件名 | 规则保证 |
| type | 强 ← 所在目录(cases/runs/reviews) | 目录推断 |
| domain/scenario（TestCase）| 路径推断 ← `cases/{domain}/{scenario}/` | 段缺失→"未分类" |
| case（Run）| 路径推断 ← `runs/{TestCaseID}/{RunID}/` 上级 | 上级目录即 case |
| run（Review）| 路径推断 ← `reviews/{RunID}/` 上级 | 上级目录即 run |
| name | 可选 | 取正文首 H1 → 取 id |
| Run artifacts | 不看 YAML，扫目录内实际文件 | 有就列 |
| verdict/problem_count | 可选 | 缺→"未判定"；count 按 `### 问题` 兜底 |
| 其余（runner/reviewed_at/author/status/solution）| 可选 | 缺→不显示 |

正文是 payload，原样展示；Review 的结构化字段（归因/涉及对象）best-effort 抽取，抽不到不算错。UI 表单产出的 Review md 是规范的；手写/Agent 写的可能自由文本——两种都收。

## 4. 多写者数据流

两个写者都落同一棵 `platform-data/tests/` 树：
- **Agent（本地）**：跑 SKILL，直接写 Run 文件夹；写完调一次 `POST /api/v1/tests/reindex`（一条 curl）。
- **人工（UI）**：填审查表单 → `POST /api/v1/tests/reviews` → 平台写 md + 立即 rebuild（加锁原子）。
- 人工浏览 stale：页面"刷新"按钮（调 reindex）。文件监听 v1 不做。

## 5. 后端 API（`/api/v1/tests/*`，独立路由）

**读**：`GET /tests/cases`（列用例，含运行数+最新结论）、`/tests/cases/{id}`、`/tests/runs?case=`、`/tests/runs/{id}`、`/tests/runs/{id}/artifact/{name}`（取产出原文）、`/tests/reviews?run=`、`/tests/reviews/{id}`、`/tests/stats`。

**写（v1 只有审查）**：`POST /tests/reviews`（body `{run, reviewer?, verdict, conclusion?, problems:[{desc, attribution, object?}]}` → 盖 id/reviewed_at、写结构化 md、rebuild）、`PATCH /tests/reviews/{id}`。

**索引**：`POST /tests/reindex`。

**v1 写边界**：TestCase 由 SA 手写 md；Run 由 Agent 写——这俩 v1 不做创建 API，只有 Review 走 UI 写。

## 6. 前端 UI（第 4 菜单，路由式下钻）

```
/tests                 用例列表（按域/场景筛 + 搜索）
/tests/cases/:id       用例详情（输入正文 + 运行列表）
/tests/runs/:id        运行详情（产出 config/方案/LLD + 审查列表 + [添加审查]）
```

「添加审查」表单：结论(通过/不通过/部分通过) + 总结 + 问题清单（每条 {描述, 归因下拉, 涉及对象 autocomplete 调图谱 /names}）→ 产出结构化 Review md。

## 7. 错误处理

- md 异常：跳过 + 收集 warnings（不阻断）。
- 并发写：模块级锁串行化 write+rebuild（独立于图谱 import_lock）。
- 断链（涉及对象指向不存在图谱对象）：显示裸 ID，不阻断。
- 产出文件缺失：显示"缺失"。

## 8. 测试

后端 pytest：样例 tests md 夹具，覆盖 parse/index/list/get/write-review/reindex。前端组件测试 + ReviewForm 写流程。

## 9. 与修正 SOP 的衔接

Review md 里每条 `归因=图谱知识` 的问题 + `涉及对象`，是修正 SOP 那个 Agent 的输入。定位 Agent 读 Review 时兼容结构化与自由文本两种。本平台只产 Review md，不参与定位/改图谱。

## 10. v1 范围

最小飞轮：TestCase + Run + Review 三类 md + 列用例/看产出/看写审查 UI；Agent 自动审查只预留结构；定位+改图谱归修正 SOP。
