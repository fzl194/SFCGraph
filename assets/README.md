# assets/ · 类型化的 LLM Wiki

> **自包含、可剥离**的唯一对外知识资产面。整个目录可单独交付/部署，不依赖外部路径。

本目录是一个 **类型化的 LLM Wiki（Typed LLM Wiki）**：一个对象 = 一个 md，对象间关系用 `[[wiki 链接]]` 承载。每个 md 是某个预定义对象类型的实例，类型由 `schema/三层图谱定义.md` 约束。

## 这是什么
- **不是随意 wiki**：页面类型和关系都按预定义 Schema 类型化（区别于 Karpathy 原版 LLM Wiki 的即兴页面）。
- **不是只读转换视图**：是 **Agent 持续 Compile/维护、人审** 的编译知识层，会因 Ingest/Query/Lint 而演进。
- **继承 LLM Wiki 内核**：编译（非查询时检索）、Ingest/Query/Lint 三操作、index+log 两基建、复利回填。

## 自包含 / 可剥离
- 所有运行时引用的内容都在 assets/ 内：证据原文拷进来、Schema/SOP 拷进来、`[[wiki]]` 在本目录闭环。
- 开发期源（`../output/` 产品文档、`../CommandGraph/data`、`../FeatureGraph/data` 等）是 Compile 的**读入方**，不进 assets 运行时引用。
- 剥离 assets/ 不影响源，源也不影响 assets 运行。

## 三层架构
| 层 | 位置 | 谁动 |
|---|---|---|
| **Raw Sources**（immutable，真相之源） | `../output/`、`../CommandGraph/data`、`../FeatureGraph/data`、任意知识 | 只读 |
| **Wiki**（本目录） | typed md + `[[wiki]]` | Agent 写维护，人审 |
| **Schema**（约束） | `schema/三层图谱定义.md` + `CLAUDE.md` | 人机共演化 |

## ID 规范（文件名 + wiki 链接依据）
- **绑产品对象**（命令/特性/任务/参数/配置对象）→ 四段式 `{nf}@{version}@{ObjectType}@{local_id}`
  - 例：`UDG@20.15.2@MMLCommand@ADD URR` / `UDG@20.15.2@Feature@GWFD-020301` / `UDG@20.15.2@Task@1-00003`
- **跨产品对象**（业务层 BD/NS/CS）→ 两段式 `{ObjectType}@{语义slug}`（不带 nf@version）
  - 例：`BusinessDomain@business-awareness` / `NetworkScenario@charging` / `ConfigurationSolution@charging-converged`
- 旧业务编号（BD-BSA-01/NS-CH-01/CS-CH-03 等）**已废弃**。

## 目录约定
```
assets/
├─ command/{nf}/{version}/<local>.md        # 如 command/UDG/20.15.2/ADD-URR.md
├─ feature/{nf}/{version}/<feature_code>.md
├─ license/{nf}/{version}/<license_code>.md
├─ business/<domain>/<scenario>/<id>.md     # 两段式 id；+ 域根 bd 文件
├─ task/{nf}/{version}/<local>.md
├─ evidence/            # 证据原文拷贝（可剥离要求）
├─ skill/               # 配置生成 SOP（P5 切换时拷入）
├─ schema/              # Schema 自包含拷贝（三层图谱定义.md）
├─ CLAUDE.md            # 维护准则（Agent 必读）
├─ index.md             # 内容目录（每次 Compile 更新）
└─ log.md               # 演进日志（append-only）
```

## 怎么用
- **Agent**：按 `CLAUDE.md` 执行 Compile/Query/Lint，维护 index/log。
- **人（业务专家）**：读 `index.md` 导航 → 审阅 typed md → 纠正/引导 Agent。你是 reviewer，不是 writer。
- **配置生成 SKILL**：通过服务化接口取子场景子集（Query），不直接读源 = 资产不外泄。

## 体系总方案
`../docs/superpowers/specs/2026-07-08-config-generation-e2e-design.md`
