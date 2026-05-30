# 业务感知原始语料盘点范围与筛选规则

## 1. 任务目标

本轮工作不是直接构建业务感知业务图谱，而是先找全业务感知相关的原始语料边界。

需要产出的清单分为三类：

1. 特性候选目录
2. 命令候选目录与具体命令
3. 散落的相关 md 文件

## 2. 原始入口

依据 [claude-study/context/source-locations.md](D:/mywork/KnowledgeBase/Graph/claude-study/context/source-locations.md)：

- `output/UDG_Product_Documentation_CH_20.15.2`
- `output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南`
- `output/UNC 20.15.2 产品文档(裸机容器) 05`
- `output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令`
- `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署`

## 3. 筛选原则

### 3.1 核心直接相关

满足以下任一条件的目录或文件，进入主清单：

1. 直接以 `业务感知`、`SA`、`PCC`、`内容计费`、`融合计费`、`基于业务感知的带宽控制` 为主题。
2. 直接定义业务感知的关键对象链或动作链，例如：
   `Rule`、`UserProfile`、`RuleBinding`、`URR`、`URRGroup`、`PCCPolicyGrp`、`QuotaExhaustAct`。
3. 直接承载业务感知主要场景：
   `差异化计费`、`免费业务`、`配额耗尽后的体验控制`、`访问限制`、`重定向`、`带宽控制`。

### 3.2 强相关支撑

以下材料不一定主标题写业务感知，但应进入候选清单：

1. 业务感知依赖的识别类特性：
   `HTTPS业务地址识别`、`HTTP2/HTTP3 Host识别`、`URL过滤` 等。
2. 业务感知依赖的动作类特性：
   `HTTP智能重定向`、`用户Portal`、`基于累计流量的策略控制`、`增强ADC基本功能` 等。
3. 对业务感知起到约束、验证、调测作用的参考信息、调测页、配置映射页。

### 3.3 外围补充

外围材料不进入主特性清单，但要进入相关文件清单：

1. 业务专题
2. 5G 基础知识解读
3. 高危操作
4. 软件参数
5. 调测方法

## 4. 盘点策略

本轮按四条线推进：

1. `UDG 特性线`
2. `UNC 特性线`
3. `命令线`
4. `散落文件线`

当前先做前两条，确认特性边界后，再反推命令和散落文件。

## 5. 输出文件

1. [01-feature-candidates.md](D:/mywork/KnowledgeBase/Graph/myoutput/business-awareness-discovery/01-feature-candidates.md)
2. `02-command-candidates.md`
3. `03-related-md-files.md`
4. 本文件
