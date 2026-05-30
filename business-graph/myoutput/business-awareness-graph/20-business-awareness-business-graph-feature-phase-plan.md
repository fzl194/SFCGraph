# 业务感知业务图谱 — 特性指南阶段迭代计划 (20-plan)

> 本文件由 `gen_20plan.py` 代码生成。特性列表和文件路径均通过代码验证。
> 如需重新生成，运行：`python gen_20plan.py`

## 1. 目标

本文件是 `20-plan`，业务图谱迭代的**第二阶段执行计划**。

第一阶段（v2-plan，T01–T11）已完成**业务描述层**语料的阅读与图谱更新（当前最新版 v10）。
本阶段从**特性指南层**切入，对 UDG 和 UNC 两侧的业务感知核心/强相关特性进行系统性精读。

语料来源：`myoutput/business-awareness-discovery/01-feature-candidates.md` 中标记为
`核心直接相关`、`强相关支撑`、`强相关旁支`、`保留为MEC/漫游旁支` 的全部特性。

## 2. 覆盖范围（代码验证）

- 特性总数：**43**
- md 文件总数：**345**
- 覆盖分区：6 个（2.1~2.3 UDG 侧，3.1~3.3 UNC 侧）
- 所有特性目录均通过代码扫描确认存在且 md 文件非空

特性清单：

| 分区 | 特性编号 | 名称 | 相关性 | 文件数 |
| --- | --- | --- | --- | --- |
| 2.1 UDG/业务感知功能 | GWFD-110101 | SA-Basic | 核心直接相关 | 6 |
| 2.1 UDG/业务感知功能 | GWFD-110201 | HTTP2.0 Host识别 | 强相关支撑 | 5 |
| 2.1 UDG/业务感知功能 | GWFD-110202 | HTTP2.0协议回落 | 强相关支撑 | 4 |
| 2.1 UDG/业务感知功能 | GWFD-110203 | HTTPS业务地址识别 | 强相关支撑 | 5 |
| 2.1 UDG/业务感知功能 | GWFD-110251 | HTTP3.0 Host识别 | 强相关支撑 | 5 |
| 2.1 UDG/业务感知功能 | GWFD-110252 | HTTP3.0 Host分析 | 强相关支撑 | 5 |
| 2.1 UDG/业务感知功能 | GWFD-110321 | 支持内置百万级业务规则库 | 强相关支撑 | 4 |
| 2.1 UDG/业务感知功能 | GWFD-110471 | URL过滤基本功能 | 强相关支撑 | 5 |
| 2.1 UDG/业务感知功能 | GWFD-111600 | SA特征库更新管控 | 强相关支撑 | 1 |
| 2.2 UDG/智能策略控制功能 | GWFD-020351 | PCC基本功能 | 核心直接相关 | 9 |
| 2.2 UDG/智能策略控制功能 | GWFD-020353 | 基于累计流量的策略控制 | 核心直接相关 | 2 |
| 2.2 UDG/智能策略控制功能 | GWFD-020354 | 基于业务的Shaping | 强相关支撑 | 6 |
| 2.2 UDG/智能策略控制功能 | GWFD-020357 | 增强的ADC基本功能 | 强相关支撑 | 5 |
| 2.2 UDG/智能策略控制功能 | GWFD-020358 | 业务触发的QoS保证 | 强相关支撑 | 13 |
| 2.2 UDG/智能策略控制功能 | GWFD-110281 | 用户Portal | 强相关支撑 | 12 |
| 2.2 UDG/智能策略控制功能 | GWFD-110284 | HTTP智能重定向 | 核心直接相关 | 5 |
| 2.2 UDG/智能策略控制功能 | GWFD-110311 | 基于业务感知的带宽控制 | 核心直接相关 | 23 |
| 2.2 UDG/智能策略控制功能 | GWFD-110312 | 基于业务累计流量的策略控制 | 核心直接相关 | 3 |
| 2.3 UDG/计费功能 | GWFD-010173 | 融合计费 | 核心直接相关 | 5 |
| 2.3 UDG/计费功能 | GWFD-020300 | 在线计费 | 核心直接相关 | 5 |
| 2.3 UDG/计费功能 | GWFD-020301 | 内容计费基本功能 | 核心直接相关 | 4 |
| 2.3 UDG/计费功能 | GWFD-020302 | 基于业务时长的计费 | 强相关支撑 | 10 |
| 2.3 UDG/计费功能 | GWFD-020303 | 基于业务流量的计费 | 强相关支撑 | 3 |
| 2.3 UDG/计费功能 | GWFD-020304 | 关联URL核减 | 强相关支撑 | 5 |
| 2.3 UDG/计费功能 | GWFD-020308 | 7层流量统计 | 强相关支撑 | 3 |
| 3.1 UNC/智能PCC解决方案 | WSFD-109101 | PCC基本功能 | 核心直接相关 | 25 |
| 3.1 UNC/智能PCC解决方案 | WSFD-109102 | ADC基本功能 | 核心直接相关 | 6 |
| 3.1 UNC/智能PCC解决方案 | WSFD-109103 | IPv6 SA | 强相关支撑 | 4 |
| 3.1 UNC/智能PCC解决方案 | WSFD-109104 | 基于累计流量的策略控制 | 核心直接相关 | 6 |
| 3.1 UNC/智能PCC解决方案 | WSFD-109107 | 业务触发的QoS保证 | 强相关支撑 | 6 |
| 3.1 UNC/智能PCC解决方案 | WSFD-211005 | 基于业务感知的带宽控制 | 核心直接相关 | 4 |
| 3.1 UNC/智能PCC解决方案 | WSFD-211009 | 基于业务累计流量的策略控制 | 核心直接相关 | 6 |
| 3.2 UNC/计费管理功能 | WSFD-011201 | 支持离线计费 | 强相关支撑 | 34 |
| 3.2 UNC/计费管理功能 | WSFD-011206 | 支持融合计费 | 核心直接相关 | 27 |
| 3.2 UNC/计费管理功能 | WSFD-109001 | Gy_Diameter在线计费 | 核心直接相关 | 30 |
| 3.2 UNC/计费管理功能 | WSFD-109002 | 内容计费基本功能 | 核心直接相关 | 2 |
| 3.2 UNC/计费管理功能 | WSFD-109003 | 基于业务时长的计费 | 强相关支撑 | 6 |
| 3.2 UNC/计费管理功能 | WSFD-109004 | 基于业务流量的计费 | 强相关支撑 | 3 |
| 3.3 UNC/MEC解决方案 | WSFD-108002 | 基于预定义规则的分流策略控制 | 强相关旁支 | 6 |
| 3.3 UNC/MEC解决方案 | WSFD-223001 | 基于位置信息的分流策略控制 | 强相关旁支 | 7 |
| 3.3 UNC/MEC解决方案 | WSFD-223003 | 基于漫游地动态签约的分流策略控制 | 强相关旁支 | 12 |
| 3.3 UNC/MEC解决方案 | WSFD-223004 | 基于动态规则的分流策略控制 | 强相关旁支 | 6 |
| 3.3 UNC/MEC解决方案 | WSFD-228003 | 公网私网业务独立计费 | 保留为MEC/漫游旁支 | 2 |

## 3. 与 v2-plan 的关系

| 维度 | v2-plan | 20-plan |
| --- | --- | --- |
| 语料层 | 业务描述层（专题、一望5G、解决方案概述） | 特性指南层（每个特性的概述、原理、流程、配置、调测） |
| 起始版本 | v1 → v2 | v10 → v11 |
| 迭代机制 | 相同 | 相同 |
| 每 task 文档上限 | ≤10 | ≤10 |
| task 组织维度 | 按主题跨特性 | 按特性维度 |

## 4. 输出文件约定

沿用 v2-plan 的逐版拷贝机制：

1. 当前最新版本为 `14-business-awareness-business-graph-v10.md`。
2. 20-plan 第一个 task（T20-01）开始时，先拷贝 v10 生成 v11：
   `15-business-awareness-business-graph-v11.md`
3. 后续每完成一个 task，拷贝上一版生成新版本，在新版本上修改。
4. 版本号推进：v10 → v11 → v12 → ...

## 5. 迭代机制

完全沿用 v2-plan 的机制：

1. 按 task 顺序执行，不跳跃。
2. 每个 task 固定 5 步：读取 → 记录结论 → 拷贝上一版 → 更新图谱 → 整体融合。
3. 整体融合从 4 个角度回看：定义准确度、抽象重叠、主链清晰度、主图完整性。
4. 中断恢复：从第一个 `pending` task 继续。

### 5.1 本阶段融合侧重点

特性指南层比业务描述层更深，融合时应额外关注：

1. **特性间的对象链交叉验证**：不同特性是否引用相同的配置对象（如 IPLIST / FILTER / RULE / USERPROFILE）？对象在特性间的语义是否一致？
2. **UDG vs UNC 对称性**：同名能力（如 PCC基本功能、带宽控制、内容计费）在两侧的分工差异是否需要在图谱中体现？
3. **RuntimeFlow / ValidationPlan / DiagnosisRule 补全**：特性指南中的流程图和调测步骤是这两类 schema 实例的最佳来源。
4. **RiskConstraint 扩展**：特性指南中的约束条件、前置依赖、互斥关系应补充到风险约束中。

## 6. task 拆分原则

1. **按特性维度组织**：每个 task 对应一个特性（或同一分区下的多个小特性合并）。
2. 文件数 > 10 的大特性按顺序拆分为多个 sub-task（标注 (1) (2) (3)）。
3. 文件数 ≤ 3 的小特性尝试与同分区的相邻小特性合并。
4. 单个 task 文档数严格 ≤ 10。
5. 先 UDG 侧（2.1→2.2→2.3）、后 UNC 侧（3.1→3.2→3.3）。

## 7. task 总表

本轮共拆分为 **57** 个 task。

| Task | 状态 | 文档数 | 相关性 | 主题 |
| --- | --- | --- | --- | --- |
| `T20-01` | `pending` | `6` | 核心直接相关 | 2.1 UDG/业务感知功能 / GWFD-110101 SA-Basic |
| `T20-02` | `pending` | `5` | 强相关支撑 | 2.1 UDG/业务感知功能 / GWFD-110201 HTTP2.0 Host识别 |
| `T20-03` | `pending` | `4` | 强相关支撑 | 2.1 UDG/业务感知功能 / GWFD-110202 HTTP2.0协议回落 |
| `T20-04` | `pending` | `5` | 强相关支撑 | 2.1 UDG/业务感知功能 / GWFD-110203 HTTPS业务地址识别 |
| `T20-05` | `pending` | `5` | 强相关支撑 | 2.1 UDG/业务感知功能 / GWFD-110251 HTTP3.0 Host识别 |
| `T20-06` | `pending` | `5` | 强相关支撑 | 2.1 UDG/业务感知功能 / GWFD-110252 HTTP3.0 Host分析 |
| `T20-07` | `pending` | `4` | 强相关支撑 | 2.1 UDG/业务感知功能 / GWFD-110321 支持内置百万级业务规则库 |
| `T20-08` | `pending` | `5` | 强相关支撑 | 2.1 UDG/业务感知功能 / GWFD-110471 URL过滤基本功能 |
| `T20-09` | `pending` | `1` | 强相关支撑 | 2.1 UDG/业务感知功能 / GWFD-111600 SA特征库更新管控 |
| `T20-10` | `pending` | `9` | 核心直接相关 | 2.2 UDG/智能策略控制功能 / GWFD-020351 PCC基本功能 |
| `T20-11` | `pending` | `2` | 核心直接相关 | 2.2 UDG/智能策略控制功能 / GWFD-020353 基于累计流量的策略控制 |
| `T20-12` | `pending` | `6` | 强相关支撑 | 2.2 UDG/智能策略控制功能 / GWFD-020354 基于业务的Shaping |
| `T20-13` | `pending` | `5` | 强相关支撑 | 2.2 UDG/智能策略控制功能 / GWFD-020357 增强的ADC基本功能 |
| `T20-14` | `pending` | `10` | 强相关支撑 | 2.2 UDG/智能策略控制功能 / GWFD-020358 业务触发的QoS保证 (1) |
| `T20-15` | `pending` | `3` | 强相关支撑 | 2.2 UDG/智能策略控制功能 / GWFD-020358 业务触发的QoS保证 (2) |
| `T20-16` | `pending` | `10` | 强相关支撑 | 2.2 UDG/智能策略控制功能 / GWFD-110281 用户Portal (1) |
| `T20-17` | `pending` | `2` | 强相关支撑 | 2.2 UDG/智能策略控制功能 / GWFD-110281 用户Portal (2) |
| `T20-18` | `pending` | `5` | 核心直接相关 | 2.2 UDG/智能策略控制功能 / GWFD-110284 HTTP智能重定向 |
| `T20-19` | `pending` | `10` | 核心直接相关 | 2.2 UDG/智能策略控制功能 / GWFD-110311 基于业务感知的带宽控制 (1) |
| `T20-20` | `pending` | `10` | 核心直接相关 | 2.2 UDG/智能策略控制功能 / GWFD-110311 基于业务感知的带宽控制 (2) |
| `T20-21` | `pending` | `3` | 核心直接相关 | 2.2 UDG/智能策略控制功能 / GWFD-110311 基于业务感知的带宽控制 (3) |
| `T20-22` | `pending` | `3` | 核心直接相关 | 2.2 UDG/智能策略控制功能 / GWFD-110312 基于业务累计流量的策略控制 |
| `T20-23` | `pending` | `5` | 核心直接相关 | 2.3 UDG/计费功能 / GWFD-010173 融合计费 |
| `T20-24` | `pending` | `5` | 核心直接相关 | 2.3 UDG/计费功能 / GWFD-020300 在线计费 |
| `T20-25` | `pending` | `4` | 核心直接相关 | 2.3 UDG/计费功能 / GWFD-020301 内容计费基本功能 |
| `T20-26` | `pending` | `10` | 强相关支撑 | 2.3 UDG/计费功能 / GWFD-020302 基于业务时长的计费 |
| `T20-27` | `pending` | `3` | 强相关支撑 | 2.3 UDG/计费功能 / GWFD-020303 基于业务流量的计费 |
| `T20-28` | `pending` | `5` | 强相关支撑 | 2.3 UDG/计费功能 / GWFD-020304 关联URL核减 |
| `T20-29` | `pending` | `3` | 强相关支撑 | 2.3 UDG/计费功能 / GWFD-020308 7层流量统计 |
| `T20-30` | `pending` | `10` | 核心直接相关 | 3.1 UNC/智能PCC解决方案 / WSFD-109101 PCC基本功能 (1) |
| `T20-31` | `pending` | `10` | 核心直接相关 | 3.1 UNC/智能PCC解决方案 / WSFD-109101 PCC基本功能 (2) |
| `T20-32` | `pending` | `5` | 核心直接相关 | 3.1 UNC/智能PCC解决方案 / WSFD-109101 PCC基本功能 (3) |
| `T20-33` | `pending` | `6` | 核心直接相关 | 3.1 UNC/智能PCC解决方案 / WSFD-109102 ADC基本功能 |
| `T20-34` | `pending` | `4` | 强相关支撑 | 3.1 UNC/智能PCC解决方案 / WSFD-109103 IPv6 SA |
| `T20-35` | `pending` | `6` | 核心直接相关 | 3.1 UNC/智能PCC解决方案 / WSFD-109104 基于累计流量的策略控制 |
| `T20-36` | `pending` | `6` | 强相关支撑 | 3.1 UNC/智能PCC解决方案 / WSFD-109107 业务触发的QoS保证 |
| `T20-37` | `pending` | `4` | 核心直接相关 | 3.1 UNC/智能PCC解决方案 / WSFD-211005 基于业务感知的带宽控制 |
| `T20-38` | `pending` | `6` | 核心直接相关 | 3.1 UNC/智能PCC解决方案 / WSFD-211009 基于业务累计流量的策略控制 |
| `T20-39` | `pending` | `10` | 强相关支撑 | 3.2 UNC/计费管理功能 / WSFD-011201 支持离线计费 (1) |
| `T20-40` | `pending` | `10` | 强相关支撑 | 3.2 UNC/计费管理功能 / WSFD-011201 支持离线计费 (2) |
| `T20-41` | `pending` | `10` | 强相关支撑 | 3.2 UNC/计费管理功能 / WSFD-011201 支持离线计费 (3) |
| `T20-42` | `pending` | `4` | 强相关支撑 | 3.2 UNC/计费管理功能 / WSFD-011201 支持离线计费 (4) |
| `T20-43` | `pending` | `10` | 核心直接相关 | 3.2 UNC/计费管理功能 / WSFD-011206 支持融合计费 (1) |
| `T20-44` | `pending` | `10` | 核心直接相关 | 3.2 UNC/计费管理功能 / WSFD-011206 支持融合计费 (2) |
| `T20-45` | `pending` | `7` | 核心直接相关 | 3.2 UNC/计费管理功能 / WSFD-011206 支持融合计费 (3) |
| `T20-46` | `pending` | `10` | 核心直接相关 | 3.2 UNC/计费管理功能 / WSFD-109001 Gy_Diameter在线计费 (1) |
| `T20-47` | `pending` | `10` | 核心直接相关 | 3.2 UNC/计费管理功能 / WSFD-109001 Gy_Diameter在线计费 (2) |
| `T20-48` | `pending` | `10` | 核心直接相关 | 3.2 UNC/计费管理功能 / WSFD-109001 Gy_Diameter在线计费 (3) |
| `T20-49` | `pending` | `2` | 核心直接相关 | 3.2 UNC/计费管理功能 / WSFD-109002 内容计费基本功能 |
| `T20-50` | `pending` | `6` | 强相关支撑 | 3.2 UNC/计费管理功能 / WSFD-109003 基于业务时长的计费 |
| `T20-51` | `pending` | `3` | 强相关支撑 | 3.2 UNC/计费管理功能 / WSFD-109004 基于业务流量的计费 |
| `T20-52` | `pending` | `6` | 强相关旁支 | 3.3 UNC/MEC解决方案 / WSFD-108002 基于预定义规则的分流策略控制 |
| `T20-53` | `pending` | `7` | 强相关旁支 | 3.3 UNC/MEC解决方案 / WSFD-223001 基于位置信息的分流策略控制 |
| `T20-54` | `pending` | `10` | 强相关旁支 | 3.3 UNC/MEC解决方案 / WSFD-223003 基于漫游地动态签约的分流策略控制 (1) |
| `T20-55` | `pending` | `2` | 强相关旁支 | 3.3 UNC/MEC解决方案 / WSFD-223003 基于漫游地动态签约的分流策略控制 (2) |
| `T20-56` | `pending` | `6` | 强相关旁支 | 3.3 UNC/MEC解决方案 / WSFD-223004 基于动态规则的分流策略控制 |
| `T20-57` | `pending` | `2` | 保留为MEC/漫游旁支 | 3.3 UNC/MEC解决方案 / WSFD-228003 公网私网业务独立计费 |

## 8. task 明细

### T20-01

- 状态：`pending`
- 文档数：`6`
- 主题：`2.1 UDG/业务感知功能 / GWFD-110101 SA-Basic`
- 特性编号：GWFD-110101

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101 SA-Basic/GWFD-110101 SA-Basic参考信息_90197552.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101 SA-Basic/GWFD-110101 SA-Basic特性概述_73565837.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101 SA-Basic/实现原理/UNC和UDG配置映射_92963580.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101 SA-Basic/实现原理/规则匹配原理_73618107.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101 SA-Basic/实现原理/解析与识别_73594052.md`
6. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101 SA-Basic/实现原理/配置架构_92957237.md`

### T20-02

- 状态：`pending`
- 文档数：`5`
- 主题：`2.1 UDG/业务感知功能 / GWFD-110201 HTTP2.0 Host识别`
- 特性编号：GWFD-110201

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110201 HTTP2.0 Host识别/GWFD-110201 HTTP2.0 Host识别参考信息_79595493.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110201 HTTP2.0 Host识别/GWFD-110201 HTTP2.0 Host识别特性概述_24082586.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110201 HTTP2.0 Host识别/实现原理_86448316.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110201 HTTP2.0 Host识别/激活HTTP2.0 Host识别_24082592.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110201 HTTP2.0 Host识别/调测HTTP2.0 Host识别_24082593.md`

### T20-03

- 状态：`pending`
- 文档数：`4`
- 主题：`2.1 UDG/业务感知功能 / GWFD-110202 HTTP2.0协议回落`
- 特性编号：GWFD-110202

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110202 HTTP2.0协议回落/GWFD-110202 HTTP2.0协议回落参考信息_79595494.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110202 HTTP2.0协议回落/GWFD-110202 HTTP2.0协议回落特性概述_65157761.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110202 HTTP2.0协议回落/激活HTTP2.0协议回落_65157762.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110202 HTTP2.0协议回落/调测HTTP2.0协议回落_65157763.md`

### T20-04

- 状态：`pending`
- 文档数：`5`
- 主题：`2.1 UDG/业务感知功能 / GWFD-110203 HTTPS业务地址识别`
- 特性编号：GWFD-110203

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110203 HTTPS业务地址识别/GWFD-110203 HTTPS业务地址识别参考信息_79595495.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110203 HTTPS业务地址识别/GWFD-110203 HTTPS业务地址识别特性概述_24082595.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110203 HTTPS业务地址识别/实现原理_54492825.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110203 HTTPS业务地址识别/调测HTTPS业务地址识别_24082602.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110203 HTTPS业务地址识别/配置HTTPS业务地址识别_24082599.md`

### T20-05

- 状态：`pending`
- 文档数：`5`
- 主题：`2.1 UDG/业务感知功能 / GWFD-110251 HTTP3.0 Host识别`
- 特性编号：GWFD-110251

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110251 HTTP3.0 Host识别/GWFD-110251 HTTP3.0 Host识别参考信息_56986853.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110251 HTTP3.0 Host识别/实现原理_06506894.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110251 HTTP3.0 Host识别/激活HTTP3.0 Host识别_56786521.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110251 HTTP3.0 Host识别/特性概述_06826690.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110251 HTTP3.0 Host识别/调测HTTP3.0 Host识别_06346954.md`

### T20-06

- 状态：`pending`
- 文档数：`5`
- 主题：`2.1 UDG/业务感知功能 / GWFD-110252 HTTP3.0 Host分析`
- 特性编号：GWFD-110252

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110252 HTTP3.0 Host分析/GWFD-110252 HTTP3.0 Host分析参考信息_08178442.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110252 HTTP3.0 Host分析/实现原理_08018450.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110252 HTTP3.0 Host分析/激活HTTP3.0 Host分析_07698710.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110252 HTTP3.0 Host分析/特性概述_58218397.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110252 HTTP3.0 Host分析/调测HTTP3.0 Host分析_58138565.md`

### T20-07

- 状态：`pending`
- 文档数：`4`
- 主题：`2.1 UDG/业务感知功能 / GWFD-110321 支持内置百万级业务规则库`
- 特性编号：GWFD-110321

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110321 支持内置百万级业务规则库/GWFD-110321 支持内置百万级业务规则库参考信息_05455407.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110321 支持内置百万级业务规则库/GWFD-110321 支持内置百万级业务规则库特性概述_05455408.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110321 支持内置百万级业务规则库/激活支持OTT业务规则库功能_05455409.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110321 支持内置百万级业务规则库/调测支持OTT业务规则库功能_05695393.md`

### T20-08

- 状态：`pending`
- 文档数：`5`
- 主题：`2.1 UDG/业务感知功能 / GWFD-110471 URL过滤基本功能`
- 特性编号：GWFD-110471

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110471 URL过滤基本功能/GWFD-110471 URL过滤基本功能参考信息_56449901.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110471 URL过滤基本功能/GWFD-110471 URL过滤基本功能特性概述_56369529.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110471 URL过滤基本功能/激活URL过滤基本功能/配置URL过滤_47348205.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110471 URL过滤基本功能/激活URL过滤基本功能/配置到ICAP Server的互通数据_75400117.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110471 URL过滤基本功能/调测URL过滤基本功能_56249725.md`

### T20-09

- 状态：`pending`
- 文档数：`1`
- 主题：`2.1 UDG/业务感知功能 / GWFD-111600 SA特征库更新管控`
- 特性编号：GWFD-111600

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-111600 SA特征库更新管控/GWFD-111600 SA特征库更新管控特性概述_73163205.md`

### T20-10

- 状态：`pending`
- 文档数：`9`
- 主题：`2.2 UDG/智能策略控制功能 / GWFD-020351 PCC基本功能`
- 特性编号：GWFD-020351

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/GWFD-020351 PCC基本功能参考信息_79592737.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/GWFD-020351 PCC基本功能特性概述_47011385.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/2_3_4_5G PCC功能差异_47013471.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/Event Trigger_47013472.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/业务流程_47013470.md`
6. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/相关概念_72244993.md`
7. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/激活PCC基本功能/配置动态PCC功能_74096530.md`
8. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/激活PCC基本功能/配置本地PCC功能_74096529.md`
9. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/调测PCC基本功能_42369277.md`

### T20-11

- 状态：`pending`
- 文档数：`2`
- 主题：`2.2 UDG/智能策略控制功能 / GWFD-020353 基于累计流量的策略控制`
- 特性编号：GWFD-020353

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020353 基于累计流量的策略控制/GWFD-020353 基于累计流量的策略控制特性概述_83974937.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020353 基于累计流量的策略控制/实现原理_83974938.md`

### T20-12

- 状态：`pending`
- 文档数：`6`
- 主题：`2.2 UDG/智能策略控制功能 / GWFD-020354 基于业务的Shaping`
- 特性编号：GWFD-020354

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/GWFD-020354 基于业务的Shaping参考信息_83195649.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/GWFD-020354 基于业务的Shaping特性概述_83823121.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/实现原理_83823122.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/激活基于业务的Shaping/针对TOS基于用户的流量整形_83195647.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/激活基于业务的Shaping/针对URL应用基于用户的流量整形配置_83195646.md`
6. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/调测基于业务的Shaping_83195648.md`

### T20-13

- 状态：`pending`
- 文档数：`5`
- 主题：`2.2 UDG/智能策略控制功能 / GWFD-020357 增强的ADC基本功能`
- 特性编号：GWFD-020357

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/GWFD-020357 增强的ADC基本功能参考信息_84866922.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/GWFD-020357 增强的ADC基本功能特性概述_84866818.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/实现原理_84866819.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/激活增强的ADC基本功能_84866820.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/调测增强的ADC基本功能_84866921.md`

### T20-14

- 状态：`pending`
- 文档数：`10`
- 主题：`2.2 UDG/智能策略控制功能 / GWFD-020358 业务触发的QoS保证 (1)`
- 特性编号：GWFD-020358

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/GWFD-020358 业务触发的QoS保证特性概述_80966039.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/参考信息_92206303.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/实现原理/专有QoS Flow相关流程（适用于5G）_10779227.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/实现原理/专有承载相关流程（适用于2_3_4G）_81656835.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/实现原理_81656834.md`
6. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/激活业务触发的QoS保证/配置七层业务触发的QOS保证（PGW-U、UPF）_80361858.md`
7. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/激活业务触发的QoS保证/配置三四层业务触发的QoS保证（PGW-U、UPF）_80318438.md`
8. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/相关术语/QoS Flow_11153135.md`
9. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/相关术语/专有承载_84864577.md`
10. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/相关术语/缺省承载_84864576.md`

### T20-15

- 状态：`pending`
- 文档数：`3`
- 主题：`2.2 UDG/智能策略控制功能 / GWFD-020358 业务触发的QoS保证 (2)`
- 特性编号：GWFD-020358

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/调测业务触发的QoS保证/调测七层业务触发的QoS保证_10883660.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/调测业务触发的QoS保证/调测三四层业务触发的QoS保证_10507253.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/调测业务触发的QoS保证/调测基于协议或协议组的专有承载创建功能_10883659.md`

### T20-16

- 状态：`pending`
- 文档数：`10`
- 主题：`2.2 UDG/智能策略控制功能 / GWFD-110281 用户Portal (1)`
- 特性编号：GWFD-110281

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110281 用户Portal/GWFD-110281 用户Portal参考信息_77079045.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110281 用户Portal/GWFD-110281 用户Portal特性概述_66655000.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110281 用户Portal/实现原理_74004638.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110281 用户Portal/调整用户Portal参数/修改Captive模式时间的间隔_66620143.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110281 用户Portal/调整用户Portal参数/修改HTTP重定向响应码_66620118.md`
6. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110281 用户Portal/调整用户Portal参数/修改IPFarm的ServerIP_66620120.md`
7. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110281 用户Portal/调整用户Portal参数/修改IPFarm的VIRTUALIP_66620119.md`
8. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110281 用户Portal/调整用户Portal参数/修改IPFarm的心跳检测参数_66620142.md`
9. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110281 用户Portal/调整用户Portal参数/修改被IPFarm绑定的心跳检测接口_66620141.md`
10. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110281 用户Portal/调整用户Portal参数/修改重定向Server的负荷分担方式_66620117.md`

### T20-17

- 状态：`pending`
- 文档数：`2`
- 主题：`2.2 UDG/智能策略控制功能 / GWFD-110281 用户Portal (2)`
- 特性编号：GWFD-110281

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110281 用户Portal/调测用户Portal_66620115.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110281 用户Portal/配置用户Portal_66620114.md`

### T20-18

- 状态：`pending`
- 文档数：`5`
- 主题：`2.2 UDG/智能策略控制功能 / GWFD-110284 HTTP智能重定向`
- 特性编号：GWFD-110284

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110284 HTTP智能重定向/GWFD-110284 HTTP智能重定向参考信息_93168884.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110284 HTTP智能重定向/GWFD-110284 HTTP智能重定向特性概述_67329006.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110284 HTTP智能重定向/实现原理_73611724.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110284 HTTP智能重定向/激活HTTP智能重定向_67075035.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110284 HTTP智能重定向/调测HTTP智能重定向_67075036.md`

### T20-19

- 状态：`pending`
- 文档数：`10`
- 主题：`2.2 UDG/智能策略控制功能 / GWFD-110311 基于业务感知的带宽控制 (1)`
- 特性编号：GWFD-110311

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/GWFD-110311 基于业务感知的带宽控制参考信息_06417276.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/GWFD-110311 基于业务感知的带宽控制特性概述_77219469.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/实现原理_77219470.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于APN_DNN的用户组级带宽控制_49155915.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于PCC预定义规则的带宽控制_06381676.md`
6. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于切片的带宽控制_44919837.md`
7. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于时间段的带宽控制_84034122.md`
8. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于用户_用户组_整机三级的带宽控制_84034124.md`
9. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于用户TOS的带宽控制_84034080.md`
10. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于用户组TOS的带宽控制_84034121.md`

### T20-20

- 状态：`pending`
- 文档数：`10`
- 主题：`2.2 UDG/智能策略控制功能 / GWFD-110311 基于业务感知的带宽控制 (2)`
- 特性编号：GWFD-110311

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于用户组的分级带宽管理控制_95938110.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/针对HTTP应用基于用户的带宽控制_84034123.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/相关术语_78496471.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于APN_DNN的用户组级带宽控制_49155922.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于PCC预定义规则的带宽控制_08247339.md`
6. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于切片的带宽控制_98479796.md`
7. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于时间段的带宽控制_97098914.md`
8. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于用户_用户组_整机三级控制中的整机的带宽控制_84034130.md`
9. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于用户_用户组_整机三级控制中的用户组的带宽控制_84034128.md`
10. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于用户TOS的带宽控制_84034127.md`

### T20-21

- 状态：`pending`
- 文档数：`3`
- 主题：`2.2 UDG/智能策略控制功能 / GWFD-110311 基于业务感知的带宽控制 (3)`
- 特性编号：GWFD-110311

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于用户组TOS的带宽控制_84034129.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测针对HTTP应用基于用户的流量的带宽控制_84034126.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制_84034125.md`

### T20-22

- 状态：`pending`
- 文档数：`3`
- 主题：`2.2 UDG/智能策略控制功能 / GWFD-110312 基于业务累计流量的策略控制`
- 特性编号：GWFD-110312

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110312 基于业务累计流量的策略控制/GWFD-110312 基于业务累计流量的策略控制特性概述_76651884.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110312 基于业务累计流量的策略控制/实现原理_77085621.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110312 基于业务累计流量的策略控制/激活基于业务累计流量的策略控制_84034134.md`

### T20-23

- 状态：`pending`
- 文档数：`5`
- 主题：`2.3 UDG/计费功能 / GWFD-010173 融合计费`
- 特性编号：GWFD-010173

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-010173 融合计费/GWFD-010173 融合计费参考信息_33931912.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-010173 融合计费/GWFD-010173 融合计费特性概述_70301693.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-010173 融合计费/实现原理_70301694.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-010173 融合计费/调测融合计费的费率标识_91966529.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-010173 融合计费/部署UPF_79654301.md`

### T20-24

- 状态：`pending`
- 文档数：`5`
- 主题：`2.3 UDG/计费功能 / GWFD-020300 在线计费`
- 特性编号：GWFD-020300

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020300 在线计费/GWFD-020300 在线计费参考信息_02557786.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020300 在线计费/GWFD-020300 在线计费特性概述_66347600.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020300 在线计费/实现原理/在线计费流程（用户创建承载时下配额）_66692149.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020300 在线计费/实现原理/在线计费流程（用户创建承载时未下配额）_66692150.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020300 在线计费/配置Gy接口在线计费_83167737.md`

### T20-25

- 状态：`pending`
- 文档数：`4`
- 主题：`2.3 UDG/计费功能 / GWFD-020301 内容计费基本功能`
- 特性编号：GWFD-020301

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020301 内容计费基本功能/GWFD-020301 内容计费基本功能参考信息_97488215.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020301 内容计费基本功能/GWFD-020301 内容计费基本功能特性概述_66863837.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020301 内容计费基本功能/实现原理_66863838.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020301 内容计费基本功能/部署UPF_28493406.md`

### T20-26

- 状态：`pending`
- 文档数：`10`
- 主题：`2.3 UDG/计费功能 / GWFD-020302 基于业务时长的计费`
- 特性编号：GWFD-020302

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/GWFD-020302 基于业务时长的计费参考信息_97488216.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/GWFD-020302 基于业务时长的计费特性概述_69148027.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/实现原理/基于业务时长的计费（适用于在线计费）/在线时长计费方式_69148030.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/实现原理/基于业务时长的计费（适用于在线计费）/在线时长计费流程_69148031.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/实现原理/基于业务时长的计费（适用于在线计费）_69148029.md`
6. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/实现原理/基于业务时长的计费（适用于离线计费）/离线时长计费方式_69148033.md`
7. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/实现原理/基于业务时长的计费（适用于离线计费）/离线时长计费流程_69148034.md`
8. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/实现原理/基于业务时长的计费（适用于离线计费）_69148032.md`
9. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/实现原理/基于业务时长的计费（适用于融合计费）_33943344.md`
10. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/部署UPF_79813617.md`

### T20-27

- 状态：`pending`
- 文档数：`3`
- 主题：`2.3 UDG/计费功能 / GWFD-020303 基于业务流量的计费`
- 特性编号：GWFD-020303

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020303 基于业务流量的计费/GWFD-020303 基于业务流量的计费参考信息_97488217.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020303 基于业务流量的计费/GWFD-020303 基于业务流量的计费特性概述_67144065.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020303 基于业务流量的计费/部署UPF_28813738.md`

### T20-28

- 状态：`pending`
- 文档数：`5`
- 主题：`2.3 UDG/计费功能 / GWFD-020304 关联URL核减`
- 特性编号：GWFD-020304

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020304 关联URL核减/GWFD-020304 关联URL核减参考信息_97534422.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020304 关联URL核减/GWFD-020304 关联URL核减特性概述_83120114.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020304 关联URL核减/实现原理_83120115.md`
4. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020304 关联URL核减/激活关联URL核减_83120117.md`
5. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020304 关联URL核减/调测关联URL核减_83120118.md`

### T20-29

- 状态：`pending`
- 文档数：`3`
- 主题：`2.3 UDG/计费功能 / GWFD-020308 7层流量统计`
- 特性编号：GWFD-020308

文件列表：

1. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020308 7层流量统计/GWFD-020308 7层流量统计参考信息_13282496.md`
2. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020308 7层流量统计/GWFD-020308 7层流量统计特性概述_59642319.md`
3. `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020308 7层流量统计/激活7层流量统计_13442390.md`

### T20-30

- 状态：`pending`
- 文档数：`10`
- 主题：`3.1 UNC/智能PCC解决方案 / WSFD-109101 PCC基本功能 (1)`
- 特性编号：WSFD-109101

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/实现原理_29056158.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/激活PCC基本功能/Gx Failover功能_31422950.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/激活PCC基本功能/配置QoS能力开放功能_48518810.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/激活PCC基本功能/配置与PCRF对接数据_30805096.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/激活PCC基本功能/配置动态PCC功能_30805098.md`
7. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/激活PCC基本功能/配置异常场景数据_31422947.md`
8. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/激活PCC基本功能/配置本地PCC功能_30805097.md`
9. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/特性概述_29056157.md`
10. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测PCC业务_31422956.md`

### T20-31

- 状态：`pending`
- 文档数：`10`
- 主题：`3.1 UNC/智能PCC解决方案 / WSFD-109101 PCC基本功能 (2)`
- 特性编号：WSFD-109101

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测PCRF负荷分担功能_31422955.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测QoS能力开放功能_84718093.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测到PCRF的数据_31422954.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/WSFD-109101 PCC基本功能特性概述（适用于5G）_71770359.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/AM策略偶联修改流程_50510739.md`
7. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/AM策略偶联建立流程_50510738.md`
8. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/AM策略偶联终止流程_50510740.md`
9. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/UE策略偶联修改流程_50510745.md`
10. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/UE策略偶联建立流程_50510744.md`

### T20-32

- 状态：`pending`
- 文档数：`5`
- 主题：`3.1 UNC/智能PCC解决方案 / WSFD-109101 PCC基本功能 (3)`
- 特性编号：WSFD-109101

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/UE策略偶联终止流程_50510746.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/异常处理流程_53323998.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/相关概念_71770360.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/激活PCC基本功能_72467890.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/调测PCC基本功能_45059543.md`

### T20-33

- 状态：`pending`
- 文档数：`6`
- 主题：`3.1 UNC/智能PCC解决方案 / WSFD-109102 ADC基本功能`
- 特性编号：WSFD-109102

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109102 ADC基本功能/WSFD-109102 ADC基本功能参考信息_92582138.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109102 ADC基本功能/实现原理(Gx)_92855755.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109102 ADC基本功能/实现原理(N7)_92582135.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109102 ADC基本功能/激活ADC基本功能_92582136.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109102 ADC基本功能/特性概述_92582134.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109102 ADC基本功能/调测ADC基本功能_92582137.md`

### T20-34

- 状态：`pending`
- 文档数：`4`
- 主题：`3.1 UNC/智能PCC解决方案 / WSFD-109103 IPv6 SA`
- 特性编号：WSFD-109103

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109103 IPv6 SA/WSFD-109103 IPv6 SA参考信息_78881328.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109103 IPv6 SA/实现原理_78881325.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109103 IPv6 SA/特性概述_78881304.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109103 IPv6 SA/调测IPv6 SA_78881327.md`

### T20-35

- 状态：`pending`
- 文档数：`6`
- 主题：`3.1 UNC/智能PCC解决方案 / WSFD-109104 基于累计流量的策略控制`
- 特性编号：WSFD-109104

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109104 基于累计流量的策略控制/WSFD-109104 基于累计流量的策略控制参考信息_29056192.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109104 基于累计流量的策略控制/实现原理（Gx）_29961018.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109104 基于累计流量的策略控制/实现原理（N7）_29961017.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109104 基于累计流量的策略控制/激活基于累计流量的策略控制_29056190.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109104 基于累计流量的策略控制/特性概述_29056168.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109104 基于累计流量的策略控制/调测基于累计流量的策略控制_29056191.md`

### T20-36

- 状态：`pending`
- 文档数：`6`
- 主题：`3.1 UNC/智能PCC解决方案 / WSFD-109107 业务触发的QoS保证`
- 特性编号：WSFD-109107

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/WSFD-109107 业务触发的QoS保证参考信息_85397060.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/实现原理/专有QoS Flow相关流程（适用于5G）_85678418.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/实现原理/专有承载相关流程（适用于2_3_4G）_85678417.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/激活业务触发的QoS保证_85397058.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/特性概述_85397056.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/调测业务触发的QoS保证_85397059.md`

### T20-37

- 状态：`pending`
- 文档数：`4`
- 主题：`3.1 UNC/智能PCC解决方案 / WSFD-211005 基于业务感知的带宽控制`
- 特性编号：WSFD-211005

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211005 基于业务感知的带宽控制/WSFD-211005 基于业务感知的带宽控制参考信息_79619228.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211005 基于业务感知的带宽控制/激活基于业务感知的带宽控制_79619226.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211005 基于业务感知的带宽控制/特性概述_79619204.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211005 基于业务感知的带宽控制/调测基于业务感知的带宽控制_79619227.md`

### T20-38

- 状态：`pending`
- 文档数：`6`
- 主题：`3.1 UNC/智能PCC解决方案 / WSFD-211009 基于业务累计流量的策略控制`
- 特性编号：WSFD-211009

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211009 基于业务累计流量的策略控制/WSFD-211009 基于业务累计流量的策略控制参考信息_27915158.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211009 基于业务累计流量的策略控制/实现原理（Gx）_29039989.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211009 基于业务累计流量的策略控制/实现原理（N7）_27915155.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211009 基于业务累计流量的策略控制/激活基于业务累计流量的策略控制_27915156.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211009 基于业务累计流量的策略控制/特性概述_27915154.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211009 基于业务累计流量的策略控制/调测基于业务累计流量的策略控制_27915157.md`

### T20-39

- 状态：`pending`
- 文档数：`10`
- 主题：`3.2 UNC/计费管理功能 / WSFD-011201 支持离线计费 (1)`
- 特性编号：WSFD-011201

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/WSFD-011201 支持离线计费参考信息/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/WSFD-011201 支持离线计费参考信息/WSFD-011201 支持离线计费参考信息（适用于SGSN）_29423865.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/实现原理/CG组网可靠性（GGSN_SGW-C_PGW-C）_95094695.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/实现原理/离线计费业务流程（GGSN_SGW-C_PGW-C）_89122042.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/实现原理/离线计费话单（GGSN_SGW-C_PGW-C）_92172742.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/实现原理/离线计费话单（SGSN）_02556787.md`
7. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/激活离线计费/配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md`
8. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/激活离线计费/配置离线_在线计费方式（GGSN_PGW-C）_95923455.md`
9. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/激活离线计费/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md`
10. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/激活离线计费/配置离线计费参数（SGSN）_01731207.md`

### T20-40

- 状态：`pending`
- 文档数：`10`
- 主题：`3.2 UNC/计费管理功能 / WSFD-011201 支持离线计费 (2)`
- 特性编号：WSFD-011201

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/激活离线计费/配置离线计费方式（SGW-C）_02167102.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/激活离线计费/配置离线计费的费率标识（GGSN_SGW-C_PGW-C）_98555879.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/激活离线计费/配置离线计费费率切换（GGSN_SGW-C_PGW-C）_95923434.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/激活离线计费/配置离线计费费率切换（SGSN）_01731138.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/激活离线计费/配置计费和策略接口选择（GGSN_SGW-C_PGW-C）_97906843.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/激活离线计费/配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md`
7. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/激活离线计费/配置话单可选功能（GGSN_SGW-C_PGW-C）_95923448.md`
8. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/激活离线计费/配置话单可靠性保证（SGSN）_01731121.md`
9. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/激活离线计费/配置话单字段（GGSN_SGW-C_PGW-C）_95923364.md`
10. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/特性概述_25745814.md`

### T20-41

- 状态：`pending`
- 文档数：`10`
- 主题：`3.2 UNC/计费管理功能 / WSFD-011201 支持离线计费 (3)`
- 特性编号：WSFD-011201

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/相关术语/CC_91845211.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/相关术语/RG_87165691.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/相关术语/SID_89122030.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/相关术语/话单_87165689.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/调测离线计费/调测CG指示重定向功能_95923589.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/调测离线计费/调测LastActivity计费_95923556.md`
7. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/调测离线计费/调测到CG的数据_95923534.md`
8. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/调测离线计费/调测时间阈值功能_95923374.md`
9. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/调测离线计费/调测流量阈值功能_95923507.md`
10. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/调测离线计费/调测离线计费参数（SGSN）_95923495.md`

### T20-42

- 状态：`pending`
- 文档数：`4`
- 主题：`3.2 UNC/计费管理功能 / WSFD-011201 支持离线计费 (4)`
- 特性编号：WSFD-011201

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/调测离线计费/调测话单可靠性保证（SGSN）_95923544.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/调测离线计费/调测话单缓存功能_95923427.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/调测离线计费/调测费率切换功能（GGSN_SGW-C_PGW-C）_95923381.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011201 支持离线计费/调测离线计费/调测费率切换功能（SGSN）_95923436.md`

### T20-43

- 状态：`pending`
- 文档数：`10`
- 主题：`3.2 UNC/计费管理功能 / WSFD-011206 支持融合计费 (1)`
- 特性编号：WSFD-011206

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/WSFD-011206 支持融合计费参考信息_74013176.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/实现原理/MEC计费流程_52284255.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/实现原理/互操作计费流程_90776689.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/实现原理/计费事件触发条件_90776688.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/实现原理/计费会话创建流程_01_10001.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/实现原理/计费会话更新流程_01_10002.md`
7. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/实现原理/计费会话通知流程_01_10004.md`
8. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/实现原理/计费会话释放流程_01_10003.md`
9. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/激活支持融合计费/使用全局CCT模板进行融合计费实例_93029782.md`
10. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/激活支持融合计费/使能融合计费功能_77691175.md`

### T20-44

- 状态：`pending`
- 文档数：`10`
- 主题：`3.2 UNC/计费管理功能 / WSFD-011206 支持融合计费 (2)`
- 特性编号：WSFD-011206

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/激活支持融合计费/配置CHF选择方式_92091086.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/激活支持融合计费/配置N40接口的API版本和增强的功能集_31702747.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/激活支持融合计费/配置SMF与CHF交互的条件和内容_93420840.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/激活支持融合计费/配置异常返回码和异常信元动作_93260161.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/激活支持融合计费/配置融合计费模板_93400212.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/激活支持融合计费/配置融合计费费率标识_93360308.md`
7. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/激活支持融合计费/配置计费和策略模式_77825710.md`
8. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/激活支持融合计费/配置计费属性CC_90776700.md`
9. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/激活支持融合计费/配置计费消息缓存_31702748.md`
10. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/激活支持融合计费/配置费率切换_86411191.md`

### T20-45

- 状态：`pending`
- 文档数：`7`
- 主题：`3.2 UNC/计费管理功能 / WSFD-011206 支持融合计费 (3)`
- 特性编号：WSFD-011206

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/特性概述_67655715.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/融合计费可靠性（未部署NCG）_75816427.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/调测支持融合计费/调测融合计费的主备CHF的可靠性_89257222.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/调测支持融合计费/调测融合计费的流量计费功能_89257221.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/调测支持融合计费/调测融合计费的缓存消息回放功能_90005269.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/调测支持融合计费/调测融合计费的计费Trigger上报功能_89257220.md`
7. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206 支持融合计费/调测支持融合计费/调测融合计费的计费会话创建功能_89257219.md`

### T20-46

- 状态：`pending`
- 文档数：`10`
- 主题：`3.2 UNC/计费管理功能 / WSFD-109001 Gy_Diameter在线计费 (1)`
- 特性编号：WSFD-109001

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/实现原理/OCS组网和链路可靠性_95110432.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/实现原理/在线计费DCC会话业务流程_95110431.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/实现原理/在线计费可选功能介绍_01717367.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/实现原理/在线计费的异常处理_95110433.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/实现原理/在线计费自动回切业务流程_01704532.md`
7. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费/配置DCC处理动作_95923447.md`
8. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费/配置OCS组网可靠性配置实例/配置OCS Failover功能_95923411.md`
9. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费/配置OCS组网可靠性配置实例/配置OCS负荷分担_95923468.md`
10. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费/配置OCS组网可靠性配置实例/配置基于CC+用户号段选择OCS_95923602.md`

### T20-47

- 状态：`pending`
- 文档数：`10`
- 主题：`3.2 UNC/计费管理功能 / WSFD-109001 Gy_Diameter在线计费 (2)`
- 特性编号：WSFD-109001

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费/配置到OCS的数据(静态路由+BFD组网)_95923542.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费/配置在线计费模板/配置CCR消息中携带的参数_95923469.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费/配置在线计费模板/配置CCR触发场景_95923545.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费/配置在线计费模板/配置在线计费自动回切功能_95923555.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费/配置在线计费模板_95923574.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费/配置在线计费的费率标识_95923388.md`
7. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费/配置普通在线计费实例_95923459.md`
8. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费/配置离线_在线计费方式（GGSN_PGW-C）_15408914.md`
9. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费/配置计费和策略接口选择（GGSN_SGW-C_PGW-C）_15408913.md`
10. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/激活Gy_Diameter在线计费/配置计费属性CC（GGSN_SGW-C_PGW-C）_15408915.md`

### T20-48

- 状态：`pending`
- 文档数：`10`
- 主题：`3.2 UNC/计费管理功能 / WSFD-109001 Gy_Diameter在线计费 (3)`
- 特性编号：WSFD-109001

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/特性概述_27636707.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/相关术语/DCC_89122031.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/相关术语/URR_91842914.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/调测Gy_Diameter在线计费/调测到OCS的数据_95923404.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/调测Gy_Diameter在线计费/调测在线流量计费_95923491.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/调测Gy_Diameter在线计费/调测在线计费业务触发功能_95923568.md`
7. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/调测Gy_Diameter在线计费/调测在线计费异常返回码动作处理_95923512.md`
8. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/调测Gy_Diameter在线计费/调测在线计费欠费重定向功能_03472799.md`
9. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/调测Gy_Diameter在线计费/调测在线计费自动回切功能_95923505.md`
10. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109001 Gy_Diameter在线计费/调测Gy_Diameter在线计费/调测在线计费费率切换_95923363.md`

### T20-49

- 状态：`pending`
- 文档数：`2`
- 主题：`3.2 UNC/计费管理功能 / WSFD-109002 内容计费基本功能`
- 特性编号：WSFD-109002

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109002 内容计费基本功能/激活内容计费_74013177.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109002 内容计费基本功能/特性概述_66402110.md`

### T20-50

- 状态：`pending`
- 文档数：`6`
- 主题：`3.2 UNC/计费管理功能 / WSFD-109003 基于业务时长的计费`
- 特性编号：WSFD-109003

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109003 基于业务时长的计费/WSFD-109003 基于业务时长的计费参考信息_74013180.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109003 基于业务时长的计费/实现原理/基于业务时长的计费（适用于在线计费）_66402114.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109003 基于业务时长的计费/实现原理/基于业务时长的计费（适用于离线计费）_66402115.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109003 基于业务时长的计费/实现原理/基于业务时长的计费（适用于融合计费）_66402116.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109003 基于业务时长的计费/激活基于业务时长的计费_74013179.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109003 基于业务时长的计费/特性概述_66402112.md`

### T20-51

- 状态：`pending`
- 文档数：`3`
- 主题：`3.2 UNC/计费管理功能 / WSFD-109004 基于业务流量的计费`
- 特性编号：WSFD-109004

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109004 基于业务流量的计费/WSFD-109004 基于业务流量的计费参考信息_74013203.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109004 基于业务流量的计费/激活基于业务流量的计费_74013202.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109004 基于业务流量的计费/特性概述_74013201.md`

### T20-52

- 状态：`pending`
- 文档数：`6`
- 主题：`3.3 UNC/MEC解决方案 / WSFD-108002 基于预定义规则的分流策略控制`
- 特性编号：WSFD-108002

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-108002 基于预定义规则的分流策略控制/WSFD-108002 基于预定义规则的分流策略控制参考信息_28860592.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-108002 基于预定义规则的分流策略控制/实现原理_29033546.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-108002 基于预定义规则的分流策略控制/激活基于预定义规则的分流策略控制_28860590.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-108002 基于预定义规则的分流策略控制/特性概述_28859310.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-108002 基于预定义规则的分流策略控制/调测基于预定义规则的分流策略控制_28860591.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-108002 基于预定义规则的分流策略控制/配置SMF和“UL CL UPF+辅锚点UPF”对接_31367702.md`

### T20-53

- 状态：`pending`
- 文档数：`7`
- 主题：`3.3 UNC/MEC解决方案 / WSFD-223001 基于位置信息的分流策略控制`
- 特性编号：WSFD-223001

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223001 基于位置信息的分流策略控制/WSFD-223001 基于位置信息的分流策略控制参考信息_47717539.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223001 基于位置信息的分流策略控制/WSFD-223001 基于位置信息的分流策略控制特性概述_87840550.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223001 基于位置信息的分流策略控制/实现原理_01277576.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223001 基于位置信息的分流策略控制/调测基于位置信息的分流策略控制（AMF）_47877403.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223001 基于位置信息的分流策略控制/调测基于位置信息的分流策略控制（SMF）_07996028.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223001 基于位置信息的分流策略控制/部署基于位置信息的分流策略控制（AMF）_47837469.md`
7. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223001 基于位置信息的分流策略控制/部署基于位置信息的分流策略控制（SMF）_53995959.md`

### T20-54

- 状态：`pending`
- 文档数：`10`
- 主题：`3.3 UNC/MEC解决方案 / WSFD-223003 基于漫游地动态签约的分流策略控制 (1)`
- 特性编号：WSFD-223003

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223003 基于漫游地动态签约的分流策略控制/WSFD-223003 基于漫游地动态签约的分流策略控制特性参考信息_52923849.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223003 基于漫游地动态签约的分流策略控制/WSFD-223003 基于漫游地动态签约的分流策略控制特性概述_42136946.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223003 基于漫游地动态签约的分流策略控制/信令流程介绍/PDU会话创建使能专网业务流程_85233681.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223003 基于漫游地动态签约的分流策略控制/信令流程介绍/PDU会话重建使能专网业务流程_37553658.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223003 基于漫游地动态签约的分流策略控制/信令流程介绍/专网业务去使能流程_39072900.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223003 基于漫游地动态签约的分流策略控制/信令流程介绍_82779457.md`
7. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223003 基于漫游地动态签约的分流策略控制/特性调测/调测基于漫游地动态签约的分流策略控制（AMF）_82619545.md`
8. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223003 基于漫游地动态签约的分流策略控制/特性调测/调测基于漫游地动态签约的分流策略控制（PCF）_36539972.md`
9. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223003 基于漫游地动态签约的分流策略控制/特性调测/调测基于漫游地动态签约的分流策略控制（SMF）_82779461.md`
10. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223003 基于漫游地动态签约的分流策略控制/特性部署/部署基于漫游地动态签约的分流策略控制（AMF）_82619543.md`

### T20-55

- 状态：`pending`
- 文档数：`2`
- 主题：`3.3 UNC/MEC解决方案 / WSFD-223003 基于漫游地动态签约的分流策略控制 (2)`
- 特性编号：WSFD-223003

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223003 基于漫游地动态签约的分流策略控制/特性部署/部署基于漫游地动态签约的分流策略控制（PCF）_36539970.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223003 基于漫游地动态签约的分流策略控制/特性部署/部署基于漫游地动态签约的分流策略控制（SMF）_82779459.md`

### T20-56

- 状态：`pending`
- 文档数：`6`
- 主题：`3.3 UNC/MEC解决方案 / WSFD-223004 基于动态规则的分流策略控制`
- 特性编号：WSFD-223004

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223004 基于动态规则的分流策略控制/WSFD-223004 基于动态规则的分流策略控制参考信息_47837467.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223004 基于动态规则的分流策略控制/信令流程解读_47597513.md`
3. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223004 基于动态规则的分流策略控制/实现原理_01477554.md`
4. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223004 基于动态规则的分流策略控制/特性概述_46633715.md`
5. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223004 基于动态规则的分流策略控制/调测基于动态规则的分流策略控制_01437552.md`
6. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-223004 基于动态规则的分流策略控制/部署基于动态规则的分流策略控制_01277574.md`

### T20-57

- 状态：`pending`
- 文档数：`2`
- 主题：`3.3 UNC/MEC解决方案 / WSFD-228003 公网私网业务独立计费`
- 特性编号：WSFD-228003

文件列表：

1. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-228003 公网私网业务独立计费/特性概述_72059981.md`
2. `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/MEC解决方案/WSFD-228003 公网私网业务独立计费/特性部署_21979632.md`

## 9. 审核点

请重点审核以下 4 点：

1. `57` 个 task 的拆分是否接受。
2. 每个 task 不超过 `10` 个文档的限制是否满足。
3. 按特性维度的组织方式是否符合期望。
4. "从 v10 拷贝生成 v11 开始逐版迭代"的约定是否明确。

审核通过后，再开始：

1. 拷贝 v10 生成 v11
2. 从 T20-01 开始逐批执行
3. 每完成一批就立即更新 v11 并做整体融合