# 三层图谱领导汇报 PPT 大纲

## Slide 1: 标题页
- 标题：云核心网三层配置图谱
- 副标题：从文档知识到配置数字孪生
- 副标题补充：以计费场景为例
- 目标：建立汇报主题，明确这是面向配置知识体系建设的专题汇报
- Layout role：cover
- Visual idea：深色技术背景，叠加网络拓扑、知识节点和连接结构，风格稳重、正式、面向管理层

## Slide 2: 为什么现在要做
- 当前核心问题：配置知识来源多元、知识类型混杂、对象边界不清，导致无法形成从业务到命令的稳定映射与复用
- 我们拿到的材料包括产品文档、专家经验、MOP脚本，知识来源并不单一
- 在计费场景下，同一套材料里会同时出现业务语义、特性能力、配置任务和命令规则
- 结果是边界难判断、复用困难、依赖专家经验，也难进一步支撑生成、核查和诊断
- Layout role：context / problem
- Visual idea：左侧展示产品文档、专家经验、MOP脚本，中间用计费场景真实片段展示知识混杂，右侧展示边界模糊、复用困难和自动化困难

## Slide 3: 三层图谱的本体设计思路
- 三层图谱不是文档分类，也不是命令索引，而是把配置知识收敛成稳定本体
- 主链是：业务域 -> 场景 -> 配置方案 -> 特性/子特性 -> 配置任务 -> 命令 -> 参数/配置对象
- 主链与三层结构一一对应：
  - 业务域 / 场景 / 配置方案 -> 业务图谱
  - 特性 / 子特性 / 配置任务 -> 特性图谱
  - 命令 / 参数 / 配置对象 -> 命令图谱
  - 最底部统一由证据层承接
- 核心原则：按本体层级解耦、不按文档来源解耦；稳定对象入本体；关系优先回到边；证据统一独立承接
- Layout role：concept explanation / ontology design
- Visual idea：上半部分展示三条本体设计原则，中间展示主链，下半部分用一一对应的三层结构图承接主链，最底部单独放证据层

## Slide 4: 一个真实诉求如何穿透三层图谱
- 不再做 schema 总览页，而是直接用《三层图谱对象与关系设计》里的“视频业务差异化计费”诉求走一遍
- 现场诉求：视频按流量扣费，配额耗尽后重定向，在线计费模式，UPF 和 SMF 都要配
- 业务层回答“这是什么问题”：业务感知 → 计费场景 → 差异化计费组合方案
- 特性层回答“靠什么能力实现”：SA-Basic、PCC基本功能、内容计费基本功能、在线计费、URL 内容识别计费
- 配置任务层回答“配置分几步做”：配置七层过滤条件 → 配置流过滤器与绑定 → 配置计费动作链 → 配置 Rule → 配置 UserProfile 与 Rule 绑定
- 命令层回答“每一步敲哪些命令”：ADD URR/URRGROUP/PCCPOLICYGRP、ADD FLOWFILTER/FLTBINDFLOWF/PROTBINDFLOWF、ADD RULE、ADD USERPROFILE/RULEBINDING/URRGRPBINDING/REFRESHSRV
- 页面目标是让领导先看懂“这张图怎么用”
- Layout role：story walkthrough / architecture explanation
- Visual idea：自上而下四段穿透图，顶部放现场诉求，底部放证据条

## Slide 5: 走完案例，再看对象和关系
- 不再做“对象分类科普页”，而是把前一页走过的案例收敛成对象组、关系组和边界规则
- 对象组分四类：业务对象组、特性对象组、配置任务对象组、命令对象组
- 关系只保留主链：contains、instantiated_as、uses_feature、has_subfeature、decomposes_to、invokes、operates_on、references
- 单独强调两类编排边：FeatureTaskOrderEdge、TaskCommandOrderEdge
- 右侧保留三条边界判定规则：有正式编号优先是特性；能独立回答现场问题优先是场景；下沉到稳定配置动作链优先是配置任务
- 底部只放三组最容易混淆的对比：计费场景 vs 内容计费基本功能；GWFD-020302/020303/020306 vs URL 内容识别计费；配置计费动作链 vs ADD URR
- 页面目标是让领导从案例回到结构，记住“图里有哪些关键对象、它们怎么连、最容易混哪里”
- Layout role：summary / boundary clarification
- Visual idea：上半区对象与关系总表，右侧边界规则，底部混淆对比条

## Slide 6: 顺序关系怎么承载
- 顺序不混在对象里，而是按层级承载
- TaskCommandOrderEdge 表达 task 内部命令的稳定顺序
- FeatureTaskOrderEdge 表达特性下 task 的稳定编排顺序
- 方案级完整顺序当前不进入主 schema，因为更依赖场景分支、决策点和实例上下文
- Layout role：process / architecture detail
- Visual idea：左右双栏，左边展示 task 内命令链，右边展示特性下 task 链

## Slide 7: 为什么要引入配置任务
- 口径统一为“配置任务”，不再用“Task”“任务原子”作为页内主文案
- 特性太粗，命令太细，中间缺少可复用、可编排的配置粒度
- 用计费场景真实例子说明三类配置任务：
- 配置计费动作链：T-EXEC-005，对应命令 ADD URR → ADD URRGROUP → ADD PCCPOLICYGRP
- 配置 Rule：T-EXEC-008，对应命令 ADD RULE
- 配置 UserProfile 与 Rule 绑定：T-EXEC-010，对应命令 ADD USERPROFILE → SET URRGRPBINDING → ADD RULEBINDING → SET REFRESHSRV
- 用真实特性替换占位符“特性A/B/C”：GWFD-020301 内容计费基本功能、GWFD-020300 在线计费、GWFD-010173 融合计费、WSFD-109002 内容计费基本功能（SMF侧）
- 明确显示“哪些特性共享哪个配置任务”，突出配置任务的复用价值
- Layout role：concept explanation / bridge layer
- Visual idea：特性在上、配置任务在中、命令在下，中间层最强视觉；用多对多连线体现复用

## Slide 8: 当前进展：从三层图谱走向服务化支撑
- 当前完成的不是单点图谱，而是一个初步闭环
- 已定义三层图谱对象 schema，并基于业务感知完成首轮打样
- 已构建业务图谱这一层的定义
- 已完成业务感知场景下两类业务图谱样板：
  - 计费场景业务图谱
  - 带宽控制场景业务图谱
- 三层图谱已开始支撑配置生成、配置核查能力
- 页面需要明确体系层级：Agent → SKILL → 服务层 → 三层图谱 → 数据层
- 下一步不是按月份排期，而是沿项目内容继续演进：
  - 扩展高频变更场景
  - 进入割接类场景、对接类场景
  - 引入 MOP 脚本
  - 构建服务层接口，为 SKILL 提供统一调用入口
  - 支撑 Agent 调用不同 SKILL 完成配置生成、配置核查、方案生成
- Layout role：progress / evolution / service-layer positioning
- Visual idea：左侧放五层体系结构，右侧放“当前完成”和“下一阶段”的树形进展，底部放一句总结

## Slide 9: 三层图谱最终带来什么
- 配置知识统一沉淀
- 配置方案可复用
- 支撑智能问答与推荐
- 支撑配置生成、核查、诊断
- 为 Agent 可用知识体系提供结构化底座
- Layout role：value / outcome
- Visual idea：中心为三层图谱，向外发散能力场景和业务价值

## Slide 10: 下一步规划
- 第一阶段：本体收敛，统一对象边界和关系主链
- 第二阶段：以计费场景为标准化样板完成完整映射
- 第三阶段：扩展到带宽控制、访问限制、本地分流等场景
- 第四阶段：支撑推荐、生成、核查、诊断等智能能力
- 结论：三层图谱建设不是做一套图，而是在构建云核心网配置知识的长期工程底座
- Layout role：roadmap / closing
- Visual idea：三阶段或四阶段路线图，风格稳重，强调长期能力建设
