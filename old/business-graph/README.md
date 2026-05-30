# 业务图谱工作台

## 定位

本目录只负责：

```text
业务图谱怎么构建
```

当前锚定业务域：

```text
业务感知
```

这里不直接放命令图谱和特性图谱结果。  
命令和特性的正式定义仍以：

- [work/business-awareness-result/](../work/business-awareness-result/00-README.md)

为准。

本目录关注的是：

1. 业务图谱从哪里来
2. 业务图谱该先构建什么
3. 哪些能代码化，哪些必须 Agent 归纳
4. 怎么分模块、分 pipeline 逐步推进

## 当前文件

1. [01-business-graph-build-strategy-v0.1.md](01-business-graph-build-strategy-v0.1.md)
   
   基于当前三层定义和真实产品文档，给出业务感知业务图谱的首版构建策略。

2. [02-fixed-source-registry.md](02-fixed-source-registry.md)
   
   固定业务感知业务图谱默认使用的命令目录、特性目录、业务专题目录，以及小步迭代原则。

3. [03-business-graph-roadmap-v0.1.md](03-business-graph-roadmap-v0.1.md)
   
   说明业务图谱不是只做最小MVP，而是如何从第一条闭包逐步扩展到整个业务感知工作面。

4. [04-business-source-index-schema-v0.1.md](04-business-source-index-schema-v0.1.md)
   
   定义业务图谱原料池 `business_source_index.csv` 的字段和 code/Agent 分工。

5. [05-business-related-coverage-rules-v0.1.md](05-business-related-coverage-rules-v0.1.md)
   
   定义业务感知相关特性、命令、对象链候选集该怎么筛。

6. [06-network-scenario-discovery-rules-v0.1.md](06-network-scenario-discovery-rules-v0.1.md)
   
   定义如何从原料池和候选覆盖面中归纳第一批 `NetworkScenario`。

7. [07-business-awareness-mvp-phase1-charging-v0.1.md](07-business-awareness-mvp-phase1-charging-v0.1.md)
   
   基于直接原始语料形成第一条完整闭包：差异化计费 + 免费业务 + 默认兜底计费。

8. [08-business-awareness-related-feature-set-v0.1.md](08-business-awareness-related-feature-set-v0.1.md)
   
   记录第一批已经直接确认与业务感知主线相关的特性子集。

9. [09-business-awareness-related-command-set-v0.1.md](09-business-awareness-related-command-set-v0.1.md)
   
   记录第一批已经直接确认与业务感知主线相关的命令子集。

10. [10-business-awareness-phase2-quota-redirect-source-notes-v0.1.md](10-business-awareness-phase2-quota-redirect-source-notes-v0.1.md)
   
   固定第二条主线“配额耗尽动作 + 重定向”的直接原始语料、正式 MVP 增量和待核查问题。

11. [11-business-awareness-graph-self-audit-v0.2.md](11-business-awareness-graph-self-audit-v0.2.md)
   
   合并构建 Agent 自查和独立审查报告，给出当前状态判断、明确错误、设计决策点和下一步 P0/P1/P2/P3 演进方案。

12. [12-schema-alignment-audit-v0.1.md](12-schema-alignment-audit-v0.1.md)
   
   对照 `work/business-awareness-result/01-schema-binding.md`，逐项审计当前 `business-graph/data` 是否真的按原 schema 落地，明确哪些已对齐、哪些只是降级实现、哪些还没做。

13. [13-data2-bottom-up-rebuild-plan-v0.1.md](13-data2-bottom-up-rebuild-plan-v0.1.md)
   
   说明为什么从顶向下切到“先命令层、再特性层、最后业务层”的底向上路线，并明确 `data2/` 的阶段目标和工作纪律。

14. [14-agent-handoff-context-v0.1.md](14-agent-handoff-context-v0.1.md)
   
   给中途接手项目的 Agent 的完整上下文，说明当前目标、目录、边界、原始语料和下一步做法。

15. [data/README.md](data/README.md)
    
   放当前业务感知闭包已经实际落出的结构化结果表。`data/` 已按“业务实体 / 业务关系 / 语义桥接 / 特性实体 / 命令实体 / 跨层关系 / 运行验收风险 / 证据 / 视图”分层。

16. [data2/README.md](data2/README.md)
   
   放新的底向上结果目录。当前只承载命令图谱 phase 1 的数据。

17. [templates/README.md](templates/README.md)
   
   放第一批业务图谱结构化产物的表头模板，便于后续直接进入代码和审查。

## 当前建议审查顺序

1. [11-business-awareness-graph-self-audit-v0.2.md](11-business-awareness-graph-self-audit-v0.2.md)
   
   先看业务感知业务图谱当前整体状态、必须修复的问题、设计决策点和下一步执行方案。

2. [12-schema-alignment-audit-v0.1.md](12-schema-alignment-audit-v0.1.md)
   
   再看当前 `business-graph/data` 到底有没有严格按最初 schema 落地，哪些只做到了主骨架，哪些还是 md/字段/视图级承载。

3. [13-data2-bottom-up-rebuild-plan-v0.1.md](13-data2-bottom-up-rebuild-plan-v0.1.md)
   
   之后看为什么路线切换，以及新路线现在只做哪一层。

4. [14-agent-handoff-context-v0.1.md](14-agent-handoff-context-v0.1.md)
   
   如果不是当前 Agent 接手，直接看这份文档即可进入工作。

5. [data2/README.md](data2/README.md)
   
   看新的 `data2/` 目录职责。当前 phase 1 只看命令层。

6. [07-business-awareness-mvp-phase1-charging-v0.1.md](07-business-awareness-mvp-phase1-charging-v0.1.md)
   
   再看第一条闭包是否严格回到 schema 对象与关系。

7. [10-business-awareness-phase2-quota-redirect-source-notes-v0.1.md](10-business-awareness-phase2-quota-redirect-source-notes-v0.1.md)
   
   看第二条闭包是否真的由原始文档支撑，尤其是 CCT、配额耗尽动作、PCC、重定向链是否合理。

8. `data2/01-command-source/`
9. `data2/02-command-entities/`
10. `data2/03-command-relations/`
11. `data2/04-command-evidence/`
12. `data2/90-review/`
13. `data/01-business-entities/`
14. `data/02-business-relations/`
15. `data/03-semantic-entities/`
16. `data/04-semantic-bridges/`
17. `data/05-feature-entities/`
18. `data/06-feature-relations/`
19. `data/07-command-entities/`
20. `data/08-cross-layer-relations/`
21. `data/09-runtime-validation-risk/`
22. `data/10-evidence/`
23. `data/11-source-and-views/`
