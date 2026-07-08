# assets/ · 类型化的 LLM Wiki

> 唯一对外暴露的知识资产面。源在各 builder 目录（不动）。

本目录是一个 **类型化的 LLM Wiki（Typed LLM Wiki）**：一个对象 = 一个 md，对象间关系用 `[[wiki 链接]]` 承载。每个 md 是某个预定义对象类型的实例，类型由 `../改进后三层图谱定义.md` 约束。

## 这是什么
- **不是随意 wiki**：页面类型和关系都按预定义 Schema 类型化（区别于 Karpathy 原版 LLM Wiki 的即兴页面）。
- **不是只读转换视图**：是 **Agent 持续 Compile/维护、人审** 的编译知识层，会因 Ingest/Query/Lint 而演进。
- **继承 LLM Wiki 内核**：编译（非查询时检索）、Ingest/Query/Lint 三操作、index+log 两基建、复利回填。

## 三层架构
| 层 | 位置 | 谁动 |
|---|---|---|
| **Raw Sources**（immutable，真相之源） | `../output/`（产品文档）、`../CommandGraph/data`、`../FeatureGraph/data`、任意知识 | 只读，不改 |
| **Wiki**（本目录） | typed md + `[[wiki]]` | Agent 写维护，人审 |
| **Schema**（约束） | `../改进后三层图谱定义.md` + `./CLAUDE.md` | 人机共演化 |

## 目录约定
```
assets/
├─ command/{nf}/{version}/<command>.md      # 如 command/UDG/20.15.2/ADD-URR.md
├─ feature/{nf}/{version}/<feature_code>.md
├─ license/{nf}/{version}/<license>.md
├─ business/{domain}/{scenario}/<id>.md     # + 域根 bd-<domain>.md
├─ task/{nf}/{version}/<task-id>.md
├─ skill/        # 配置生成 SOP（Phase 0-7）
├─ schema/       # 各对象类型 typed 模板（Compile 该层时落地）
├─ CLAUDE.md     # 维护准则（Agent 必读）
├─ index.md      # 内容目录（每次 Compile 更新）
└─ log.md        # 演进日志（append-only）
```

## 怎么用
- **Agent**：按 `CLAUDE.md` 执行 Compile/Query/Lint，维护 index/log。
- **人（业务专家）**：读 `index.md` 导航 → 审阅 typed md → 纠正/引导 Agent。你是 reviewer，不是 writer。
- **配置生成 SKILL**：通过服务化接口取子场景子集（Query），不直接读源 = 资产不外泄。

## 体系总方案
`../docs/superpowers/specs/2026-07-08-config-generation-e2e-design.md`
