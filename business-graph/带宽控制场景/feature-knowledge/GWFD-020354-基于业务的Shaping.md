# GWFD-020354 基于业务的Shaping 知识文档

## 概述

### 特性定义

基于业务的Shaping是指 UDG 通过带宽管理控制器（BWM Controller）对用户的业务流量进行整形控制，使用户报文以较均匀的速度发送。

核心机制：
- UDG 对入网用户的不同业务进行识别和分类
- 对配置了Shaping的业务流量，基于令牌桶机制进行流量整形
- 超出速率规格的报文被缓存（而非丢弃），待令牌桶有足够令牌时再均匀发送
- 目标是实现出口流量的平滑，而非直接限速或丢弃

与Policing（流量监管）的关键区别：Shaping缓存超速报文，Policing直接丢弃超速报文。

> 基于PCC标准架构的流量经营类业务功能，主要基于网络资源、客户的业务感知针对性展开网络运营，是运营商开展MBB商业运营的基础，实际部署时，需要在遵循当地法律允许的目的和范围内提供服务，以保证终端用户的通信自由和业务知情权。

### 适用NF

| NF | 说明 |
|-----|------|
| PGW-U/UPF | 针对入网用户的不同业务，完成相应基于Shaping的带宽控制，实现出口流量的平滑 |
| PCRF/PCF | 只支持下发预定义规则的shaping，实现对用户的带宽控制 |
| MS/UE | 无特殊要求 |

### 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|----------|----------|----------|
| 01 | UDG 20.0.0（20.1.0） | 首次发布 |

UDG 20.0.0及后续版本支持本特性。

### License

| License控制项 | License编号 | 说明 |
|---------------|-------------|------|
| 82200AFN 基于业务的Shaping | LKV3G5SBTS01 | 本特性只有获得了License许可后才能获得该特性的服务 |

开启License开关的MML命令：
```
SET LICENSESWITCH:LICITEM="LKV3G5SBTS01",SWITCH=ENABLE;
```

### 前置条件与依赖

| 依赖类型 | 相关特性 | 控制项 | 说明 |
|----------|---------|--------|------|
| 依赖 | GWFD-110101 SA-Basic | 82209749 SA-Basic | 需要对用户上下行数据进行识别解析，必须开启业务感知功能 |
| 依赖 | GWFD-110311 基于业务感知的带宽控制 | 82209832 基于业务感知的带宽控制 | 依赖于基于业务感知的带宽控制功能对业务的区分与匹配，必须开启基于业务感知的带宽控制 |

前置条件清单：
1. 已开启SA-Basic（GWFD-110101）License
2. 已开启基于业务感知的带宽控制（GWFD-110311）License
3. 已开启基于业务的Shaping（GWFD-020354）License
4. UDG与网络实体之间的网络环境已经构建完成
5. 基于URL场景时：已加载特征库和解析库
6. UDG接入侧/PDN侧的镜像接口已安装第三方抓包工具（调测时）

---

## 核心概念

### 关键术语

| 术语 | 说明 |
|------|------|
| Shaping（流量整形） | 一种主动调整流量输出速率的流量管理方式。对超出流量规格的报文进行缓存，当令牌桶有足够的令牌时，再均匀发送缓存的报文，保证业务流量的稳定 |
| 业务级Shaping | 基于业务类型（TOS值或非TOS业务如URL/协议/协议组）对匹配的业务流量进行整形 |
| 令牌桶（Token Bucket） | 一种流量测量机制。预先设定一定容量，系统按设定的速度向桶中放置令牌。当桶中令牌放满时，多出的令牌溢出，令牌量不再增加。发送报文需要消耗令牌 |
| GTS队列 | General Traffic Shaping队列。当报文速率超过整形速率时，令牌桶中没有足够令牌，产生GTS队列用于缓存报文 |
| ToS业务 | 以ToS（Type of Service）值作为区分条件的业务。可以不进行业务识别和解析，不需要创建五元组，仅根据报文DSCP值确定是否进行流量整形 |
| 非ToS业务 | 以Category Property、L7 Protocol、Protocol Group等非ToS值作为区分条件的业务。需要通过三四层过滤规则、七层协议类型、七层协议特征信息进行识别 |
| BWM Controller | 带宽管理控制器，配置Shaping的控制参数（速率、队列深度、最大五元组数等） |

### 对象模型

基于业务的Shaping涉及以下配置对象及其关系：

```
BWMSERVICE（带宽管理业务）
  ├── 定义业务类型：TOS 或 NONTOS
  ├── TOS类型：BWMSERVICETYPE=TOS, TOSCFGTYPE=TOS_VALUE, TOSVALUE=0~7
  └── 非TOS类型：BWMSERVICETYPE=NONTOS
       ├── PROTOCOL（单协议）: PROTOCOLNAME="http"
       ├── PROTOCOLGROUP（协议组）: PROTGROUPNAME="protgroup_test"
       └── CATEGORY_PROP（分类属性/URL）: CATEPROPNAME="cateprop_test"

BWMUSERGROUP（带宽管理用户组）
  ├── USERGROUPTYPE=SPECIFIC_GROUP
  ├── USERGROUPNAME="usergroup_test"
  ├── USERGROUPPRI=2（用户组优先级）
  └── USERLEVSRVTYPE=TOS 或 NONTOS（用户级业务类型）

APNBINDBWMUSRG（用户组与APN绑定）
  └── 将BWMUSERGROUP绑定到指定APN

BWMCONTROLLER（带宽管理控制器）
  ├── BWMCNAME="bwmc_test"
  ├── CTRLTYPE=SHAPING（固定为SHAPING）
  ├── RATE=50（整形速率，千比特每秒）
  ├── QUEDEPTH=256（队列深度，报文数）
  └── MAXFDNUM=2000（最大五元组数）

BWMRULE（带宽管理规则）
  ├── BWMRULETYPE=SUBSCRIBER_SPECIFIC（用户级规则）
  ├── BWMSERVICENAME（引用BWMSERVICE）
  ├── UPBWMCTRLNAME1（上行控制器）
  ├── DNBWMCTRLNAME1（下行控制器）
  └── BWMRULEPRI=1（规则优先级）
```

业务规则侧对象：

```
FLOWFILTER（流过滤器）── 匹配业务的入口
  ├── FLTBINDFLOWF（三四层过滤器绑定）
  │     └── FILTER（三四层过滤条件：IP/Port/协议）
  └── PROTBINDFLOWF（协议绑定）
        └── L7FILTER（七层过滤器：URL等）

RULE（业务规则）
  ├── POLICYTYPE=BWM
  ├── FILTERINGMODE=FLOWFILTER
  └── POLICYNAME（引用CATEGORYPROP等）

USERPROFILE（用户模板）
  └── RULEBINDING（规则绑定：将RULE绑定到USERPROFILE）
```

### Shaping vs Policing vs BWM

| 维度 | Shaping（流量整形） | Policing（流量监管） | BWM（带宽管理） |
|------|---------------------|---------------------|-----------------|
| 超速报文处理 | **缓存**到GTS队列，待令牌充足时均匀发送 | 直接**丢弃**或重标记 | 泛称，包含Shaping和Policing两种控制类型 |
| 延迟 | 引入额外延迟（报文排队等待） | 无额外延迟（直接丢弃） | 取决于控制类型 |
| 报文丢失 | 仅当GTS队列满时丢弃 | 超速即丢弃 | 取决于控制类型 |
| 流量效果 | 输出流量平滑均匀 | 输出流量呈锯齿状 | 取决于控制类型 |
| 适用场景 | 需要平滑流量、减少突发 | 需要严格限速、保护网络资源 | 统称的带宽控制框架 |

本特性（GWFD-020354）专门针对 **Shaping** 类型，BWMCONTROLLER 的 CTRLTYPE 固定为 SHAPING。

### 基于业务 vs 基于用户 vs 基于TOS

| 维度 | 基于业务的Shaping（本特性） | 说明 |
|------|---------------------------|------|
| 基于TOS | 以报文DSCP值区分业务，不需深度识别 | 轻量、快速，但粒度粗（仅8种TOS等级） |
| 基于URL/协议 | 以七层协议、URL、协议组区分业务 | 需要特征库和深度解析，粒度细 |
| 基于用户 | BWMRULETYPE=SUBSCRIBER_SPECIFIC | **本特性仅在用户级带宽控制规则中生效** |

关键约束：**基于业务的Shaping仅在用户级带宽控制规则中生效**（BWMRULETYPE=SUBSCRIBER_SPECIFIC），不支持用户组级或整机级。

---

## 原理与流程

### 实现原理

#### 1. 业务流量识别

当来自 S1-U/S5/S8/N3 接口或者 Gi/SGi/N6 接口的业务流到达 UDG 时，UDG 进行业务类型识别：

- **非ToS类业务识别**：UDG通过三四层的过滤规则、七层协议类型、七层协议的特征信息进行识别
- **ToS类业务识别**：UDG通过用户报文的ToS值（DSCP）进行识别，不需要业务感知深度解析

#### 2. 业务控制规则匹配

对于识别出的业务，UDG 根据用户属性和流量属性匹配业务控制规则：

- **用户属性**：用户接入属性RAT、用户归属属性等
- **流量属性**：业务上/下行方向、所处时段等

#### 3. 流量整形执行

匹配到Shaping规则后，UDG 对业务流量进行令牌桶整形：

**流量整形过程**：

```
报文到达 UDG
    │
    ▼
报文速率 <= 速率（RATE）?
    │
    ├── 是 ──▶ 令牌桶有足够令牌 ──▶ 正常转发报文（无GTS队列）
    │
    └── 否 ──▶ 令牌桶令牌不足 ──▶ 产生GTS队列
                                       │
                                       ├── GTS队列未满 ──▶ 报文进入队列缓存
                                       │                     │
                                       │                     ▼
                                       │              GTS按周期调度转发
                                       │              每次转发消耗令牌
                                       │              直到令牌不足或队列清空
                                       │
                                       └── GTS队列已满 ──▶ 后续报文直接丢弃
```

关键参数说明：
- **速率（RATE）**：通过 ADD BWMCONTROLLER 命令配置，标识流量整形后的报文转发速率（千比特/秒）
- **队列深度（QUEDEPTH）**：通过 ADD BWMCONTROLLER 命令配置，标识GTS队列能够缓存的包数
- **最大五元组数（MAXFDNUM）**：限制同时进行Shaping的最大流数

### 业务流程

#### ToS场景完整流程

```
1. 报文到达UDG
2. UDG读取报文DSCP值（ToS值）
3. 匹配BWMSERVICE（BWMSERVICETYPE=TOS, TOSVALUE=x）
4. 匹配BWMRULE（BWMRULETYPE=SUBSCRIBER_SPECIFIC）
5. 执行BWMCONTROLLER的Shaping逻辑
   - 检查令牌桶令牌数
   - 令牌充足：直接转发
   - 令牌不足：进入GTS队列缓存等待
   - GTS队列满：丢弃报文
```

#### 非ToS场景完整流程

```
1. 报文到达UDG
2. UDG进行业务感知识别（需要SA-Basic和特征库支持）
   - 三四层过滤规则匹配（IP/Port/协议）
   - 或七层协议匹配（URL/L7Filter）
   - 或协议组匹配
3. 匹配BWMSERVICE（BWMSERVICETYPE=NONTOS, NONTOSSRVTYPE=PROTOCOL/PROTOCOLGROUP/CATEGORY_PROP）
4. 匹配BWMRULE（BWMRULETYPE=SUBSCRIBER_SPECIFIC）
5. 执行BWMCONTROLLER的Shaping逻辑（同ToS场景）
```

### 协议交互

本特性无额外协议交互。UDG 在数据面本地完成流量整形，不涉及与 PCRF/PCF 的信令交互（PCRF/PCF 只支持下发预定义规则的shaping）。

遵循标准：

| 标准类别 | 标准编号 | 标准名称 |
|----------|----------|----------|
| IETF | RFC 1945 | Hypertext Transfer Protocol -- HTTP/1.0 |
| IETF | RFC 2616 | Hypertext Transfer Protocol -- HTTP/1.1 |

---

## 配置规则

### 激活步骤

#### 通用激活步骤

```
步骤1: 打开License开关
  SET LICENSESWITCH

步骤2: 配置流过滤器（业务匹配入口）
  ADD FLOWFILTER

步骤3: [可选] 配置三四层过滤规则
  ADD FILTER → ADD FLTBINDFLOWF → SET REFRESHSRV

步骤4: [可选] 配置七层过滤条件（URL场景）
  ADD L7FILTER → ADD PROTBINDFLOWF → SET REFRESHSRV

步骤5: [可选] 配置PCC策略组（PCC用户场景）
  ADD PCCPOLICYGRP

步骤6: 配置业务规则
  ADD RULE

步骤7: 配置UserProfile（用户模板与规则绑定）
  ADD USERPROFILE → ADD RULEBINDING

步骤8: [可选] 配置分类属性（URL/Category场景）
  ADD CATEGORYPROP

步骤9: [可选] 配置自定义协议组（协议组场景）
  ADD PROTOCOLGROUP

步骤10: 配置BWM业务
  ADD BWMUSERGROUP → ADD BWMSERVICE → ADD APNBINDBWMUSRG → ADD BWMCONTROLLER

步骤11: 配置带宽管理规则
  ADD BWMRULE
```

### MML命令清单

| 命令 | 用途 | 使用场景 |
|------|------|----------|
| SET LICENSESWITCH | 打开License开关 | 所有场景，必须第一步 |
| ADD FLOWFILTER | 配置流过滤器 | 所有场景 |
| ADD FILTER | 配置三四层过滤条件 | 需要IP/Port/协议过滤时 |
| ADD FLTBINDFLOWF | 绑定过滤器到流过滤器 | 使用三四层过滤时 |
| ADD L7FILTER | 配置七层过滤器（URL） | URL场景 |
| ADD PROTBINDFLOWF | 绑定协议/七层过滤器到流过滤器 | URL场景 |
| SET REFRESHSRV | 刷新使新配置生效 | 三四层和七层过滤配置后 |
| ADD PCCPOLICYGRP | 配置PCC策略组 | PCC用户场景 |
| ADD RULE | 配置业务规则 | 所有场景 |
| ADD USERPROFILE | 创建用户模板 | 所有场景 |
| ADD RULEBINDING | 绑定规则到用户模板 | 所有场景 |
| ADD CATEGORYPROP | 配置分类属性 | URL/Category场景 |
| ADD PROTOCOLGROUP | 配置自定义协议组 | 协议组场景 |
| ADD BWMSERVICE | 配置带宽管理业务 | 所有场景 |
| ADD BWMUSERGROUP | 配置带宽管理用户组 | 所有场景 |
| ADD APNBINDBWMUSRG | 绑定用户组到APN | 所有场景 |
| ADD BWMCONTROLLER | 配置带宽管理控制器 | 所有场景 |
| ADD BWMRULE | 配置带宽管理规则 | 所有场景 |

### 参数说明

#### BWMCONTROLLER 核心参数

| 参数 | MML参数名 | 取值样例 | 说明 |
|------|-----------|----------|------|
| 带宽管理控制器名称 | BWMCNAME | bwmc_test | 本端规划，唯一标识 |
| 带宽管理控制类型 | CTRLTYPE | **SHAPING** | 固定取值，本特性必须为SHAPING |
| 速率（千比特每秒） | RATE | 50 | 流量整形速率阈值。超过该速率的报文进行整形 |
| 队列深度（报文数） | QUEDEPTH | 256 | GTS队列能缓存的包数。队列满后报文丢弃 |
| 最大五元组数 | MAXFDNUM | 2000 | 同时进行Shaping的最大流数 |

#### BWMSERVICE 参数（按业务类型）

**ToS业务**：

| 参数 | MML参数名 | 取值样例 | 说明 |
|------|-----------|----------|------|
| 带宽控制业务名称 | BWMSERVICENAME | bwmservice_test | 本端规划 |
| 业务类型 | BWMSERVICETYPE | **TOS** | 固定 |
| Tos配置类型 | TOSCFGTYPE | TOS_VALUE | 固定 |
| 服务类型 | TOSVALUE | 0 | TOS值：BE(0), AF1(1), AF2(2), AF3(3), AF4(4), EF(5), CS6(6), CS7(7) |

**非ToS业务 - 协议类型**：

| 参数 | MML参数名 | 取值样例 | 说明 |
|------|-----------|----------|------|
| 业务类型 | BWMSERVICETYPE | **NONTOS** | 固定 |
| 非TOS业务类型 | NONTOSSRVTYPE | **PROTOCOL** | 单协议 |
| 协议名称 | PROTOCOLNAME | http | 应用协议名称 |

**非ToS业务 - 协议组类型**：

| 参数 | MML参数名 | 取值样例 | 说明 |
|------|-----------|----------|------|
| 业务类型 | BWMSERVICETYPE | **NONTOS** | 固定 |
| 非TOS业务类型 | NONTOSSRVTYPE | **PROTOCOLGROUP** | 协议组 |
| 协议组名称 | PROTGROUPNAME | protgroup_test | 使用ADD PROTOCOLGROUP定义 |

**非ToS业务 - 分类属性（URL）类型**：

| 参数 | MML参数名 | 取值样例 | 说明 |
|------|-----------|----------|------|
| 业务类型 | BWMSERVICETYPE | **NONTOS** | 固定 |
| 非TOS业务类型 | NONTOSSRVTYPE | **CATEGORY_PROP** | 分类属性 |
| 分类属性名称 | CATEPROPNAME | cateprop_test | 使用ADD CATEGORYPROP定义 |

#### BWMUSERGROUP 参数

| 参数 | MML参数名 | 取值样例 | 说明 |
|------|-----------|----------|------|
| 用户组类型 | USERGROUPTYPE | SPECIFIC_GROUP | 固定 |
| 用户组名称 | USERGROUPNAME | usergroup_test | 本端规划 |
| 用户组优先级 | USERGROUPPRI | 2 | 本端规划 |
| 用户级业务类型 | USERLEVSRVTYPE | TOS 或 NONTOS | 与BWMSERVICE类型对应 |

#### BWMRULE 参数

| 参数 | MML参数名 | 取值样例 | 说明 |
|------|-----------|----------|------|
| 用户组类型 | USERGROUPTYPE | SPECIFIC_GROUP | 固定 |
| 用户组名称 | USERGROUPNAME | usergroup_test | 引用BWMUSERGROUP |
| 带宽管理规则类型 | BWMRULETYPE | **SUBSCRIBER_SPECIFIC** | **必须为用户级**（本特性限制） |
| 带宽管理规则名称 | BWMRULENAME | bwmrule_test | 本端规划 |
| 带宽控制业务名称 | BWMSERVICENAME | bwmservice_test | 引用BWMSERVICE |
| 上行控制器名称 | UPBWMCTRLNAME1 | bwmc_test | 引用BWMCONTROLLER |
| 下行控制器名称 | DNBWMCTRLNAME1 | bwmc_test | 引用BWMCONTROLLER |
| 规则优先级 | BWMRULEPRI | 1 | 同一用户级下不能重复 |

### 约束条件

1. **仅在用户级带宽控制规则中生效**：BWMRULETYPE 必须为 SUBSCRIBER_SPECIFIC，不支持 GROUP_SPECIFIC 或整机级
2. **License依赖链**：必须依次开启 SA-Basic → 基于业务感知的带宽控制 → 基于业务的Shaping
3. **非ToS场景需要特征库**：URL/协议匹配需要已加载特征库和解析库
4. **系统性能影响**：用户报文需要缓存或解析，系统吞吐量将下降，并带来一定延迟
5. **规则优先级唯一性**：同一个用户级下的带宽管理规则优先级不能相同
6. **USERLEVSRVTYPE一致性**：BWMUSERGROUP 的 USERLEVSRVTYPE 应与 BWMSERVICE 的 BWMSERVICETYPE 对应（TOS场景配TOS，非TOS场景配NONTOS）
7. **SET REFRESHSRV延迟**：配置L7Filter后系统自动在60s后生效，可通过 SET REFRESHSRV 立即刷新
8. **无计费话单**：本特性不涉及计费与话单
9. **无告警/软参/测量指标**：本特性无相关告警、软参和测量指标

---

## 配置案例

### 典型场景1：针对TOS基于用户的流量整形

**场景描述**：保护带宽资源不被P2P/VoIP流量吞噬，确保应用公平分享带宽资源。基于TOS作为区分业务的条件，UDG 可以不进行业务识别和解析，仅根据报文DSCP值确定是否对其进行流量整形。

**适用NF**：PGW-U、UPF

**配置数据规划**：

| 参数 | 取值 |
|------|------|
| BWMSERVICENAME | bwmservice_test |
| BWMSERVICETYPE | TOS |
| TOSCFGTYPE | TOS_VALUE |
| TOSVALUE | 0（BE） |
| USERGROUPNAME | usergroup_test |
| USERGROUPPRI | 2 |
| USERLEVSRVTYPE | TOS |
| APN | huawei.com |
| BWMCNAME | bwmc_test |
| CTRLTYPE | SHAPING |
| RATE | 50（千比特/秒） |
| QUEDEPTH | 256 |
| MAXFDNUM | 2000 |
| BWMRULETYPE | SUBSCRIBER_SPECIFIC |
| BWMRULENAME | bwmrule_test |
| BWMRULEPRI | 1 |

**完整MML脚本**：

```mml
// 步骤1：打开本特性的License配置开关
SET LICENSESWITCH:LICITEM="LKV3G5SBTS01",SWITCH=ENABLE;

// 步骤2：配置带宽管理的业务范围（TOS类型，ToS值为0=BE）
ADD BWMSERVICE:BWMSERVICENAME="bwmservice_test",BWMSERVICETYPE=TOS,TOSCFGTYPE=TOS_VALUE,TOSVALUE=0;

// 步骤3：配置带宽管理的用户范围
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="usergroup_test",USERGROUPPRI=2,USERLEVSRVTYPE=TOS;

// 步骤4：绑定用户组到APN
ADD APNBINDBWMUSRG:USERGROUPNAME="usergroup_test",APN="huawei.com";

// 步骤5：配置BWM控制器（Shaping参数）
ADD BWMCONTROLLER:BWMCNAME="bwmc_test",CTRLTYPE=SHAPING,RATE=50,QUEDEPTH=256,MAXFDNUM=2000;

// 步骤6：配置带宽管理规则（用户级）
ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="usergroup_test",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmrule_test",BWMSERVICENAME="bwmservice_test",UPBWMCTRLNAME1="bwmc_test",DNBWMCTRLNAME1="bwmc_test",BWMRULEPRI=1;
```

**效果**：UDG 对 usergroup_test 用户组下各用户的 TOS 值为 BE(0) 的上行、下行用户面数据流量进行流量整形，整形速率为 50 kbps。

---

### 典型场景2：针对URL应用基于用户的流量整形

**场景描述**：用户访问特定URL的业务时，需要公平分享带宽资源，对流量进行整形。

**适用NF**：PGW-U、UPF

**前置条件**：已加载特征库和解析库

#### 2.1 基于URL分类属性的完整配置

**完整MML脚本**：

```mml
// 步骤1：打开License开关
SET LICENSESWITCH:LICITEM="LKV3G5SBTS01",SWITCH=ENABLE;

// 步骤2：配置三四层过滤规则（可选，仅采用七层过滤时可跳过）
ADD FILTER:FILTERNAME="filter_test1",L34PROTTYPE=STRING,L34PROTOCOL=TCP,MSIPMODE=IP,MSIP="0.0.0.0",MSIPMASKTYPE=IPTYPE,MSIPMASK="255.255.255.255",SVRIPMODE=IP,SVRIP="10.10.10.20",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.0.0",MSSTARTPORT=0,MSENDPORT=65535,SVRSTARTPORT=80,SVRENDPORT=80;
ADD FILTER:FILTERNAME="filter_test2",L34PROTTYPE=STRING,L34PROTOCOL=TCP,MSIPMODE=IP,MSIP="0.0.0.0",MSIPMASKTYPE=IPTYPE,MSIPMASK="255.255.255.255",SVRIPMODE=IP,SVRIP="10.10.10.20",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.0.0",MSSTARTPORT=0,MSENDPORT=65535,SVRSTARTPORT=8080,SVRENDPORT=8080;
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test1";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test2";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 步骤3：配置七层过滤条件（URL匹配）
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test1",URL="www.huawei.com/*";
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test2",URL="www.example.com";
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",PROTOCOLNAME="http",L7FILTERNAME="l7filter_test";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 步骤4：配置分类属性
ADD CATEGORYPROP:CATEPROPNAME="cateprop_test";

// 步骤5：配置流量整形使用的业务规则
ADD RULE:RULENAME="rule_test2",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilter_test",PRIORITY=20,POLICYNAME="cateprop_test";

// 步骤6：配置BWM使用的UserProfile
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test2";

// 步骤7：配置带宽管理的业务范围（分类属性类型）
ADD BWMSERVICE:BWMSERVICENAME="bwmservice_test",BWMSERVICETYPE=NONTOS,NONTOSSRVTYPE=CATEGORY_PROP,CATEPROPNAME="cateprop_test";

// 步骤8：配置带宽管理的用户范围及流量整形参数
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="usergroup_test",USERGROUPPRI=2,USERLEVSRVTYPE=NONTOS;
ADD APNBINDBWMUSRG:USERGROUPNAME="usergroup_test",APN="huawei.com";
ADD BWMCONTROLLER:BWMCNAME="bwmc_test",CTRLTYPE=SHAPING,RATE=50,QUEDEPTH=256,MAXFDNUM=2000;

// 步骤9：配置带宽管理规则
ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="usergroup_test",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmrule_test",BWMSERVICENAME="bwmservice_test",UPBWMCTRLNAME1="bwmc_test",DNBWMCTRLNAME1="bwmc_test",BWMRULEPRI=1;
```

#### 2.2 基于单协议的流量整形

```mml
// 配置带宽管理的业务范围（单协议类型）
ADD BWMSERVICE:BWMSERVICENAME="bwmservice_test",BWMSERVICETYPE=NONTOS,NONTOSSRVTYPE=PROTOCOL,PROTOCOLNAME="http";

// 配置带宽管理的用户范围及流量整形参数
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="usergroup_test",USERGROUPPRI=2,USERLEVSRVTYPE=NONTOS;
ADD APNBINDBWMUSRG:USERGROUPNAME="usergroup_test",APN="huawei.com";
ADD BWMCONTROLLER:BWMCNAME="bwmc_test",CTRLTYPE=SHAPING,RATE=50,QUEDEPTH=256,MAXFDNUM=2000;

// 配置带宽管理规则
ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="usergroup_test",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmrule_test",BWMSERVICENAME="bwmservice_test",UPBWMCTRLNAME1="bwmc_test",DNBWMCTRLNAME1="bwmc_test",BWMRULEPRI=1;
```

#### 2.3 基于协议组的流量整形

协议组中包含多个协议，多个协议**共享**流量整形速率。

```mml
// 配置自定义协议组
ADD PROTOCOLGROUP:PROTGROUPNAME="protgroup_test",PROTOCOLNAME="p2p";
ADD PROTOCOLGROUP:PROTGROUPNAME="protgroup_test",PROTOCOLNAME="email";

// 配置带宽管理的业务范围（协议组类型）
ADD BWMSERVICE:BWMSERVICENAME="bwmservice_test",BWMSERVICETYPE=NONTOS,NONTOSSRVTYPE=PROTOCOLGROUP,PROTGROUPNAME="protgroup_test";

// 配置带宽管理的用户范围及流量整形参数
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="usergroup_test",USERGROUPPRI=2,USERLEVSRVTYPE=NONTOS;
ADD APNBINDBWMUSRG:USERGROUPNAME="usergroup_test",APN="huawei.com";
ADD BWMCONTROLLER:BWMCNAME="bwmc_test",CTRLTYPE=SHAPING,RATE=50,QUEDEPTH=256,MAXFDNUM=2000;

// 配置带宽管理规则
ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="usergroup_test",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmrule_test",BWMSERVICENAME="bwmservice_test",UPBWMCTRLNAME1="bwmc_test",DNBWMCTRLNAME1="bwmc_test",BWMRULEPRI=1;
```

---

## 验证与调测

### 调测场景

用户进行P2P业务时，用户的访问流量需要控制在512kbps内。

### 调测前提条件

- 已完成激活基于业务的Shaping配置
- UDG接入侧/PDN侧的镜像接口已安装第三方抓包工具

### 调测数据

| 类别 | 参数名称 | 取值样例 | 说明 |
|------|----------|----------|------|
| 用户信息查询 | IMSI | 460000123456789 | 测试终端自带 |
| APN | APN | huawei.com | 取自激活配置中的APN实例名 |
| BWMUSERGROUP | USERGROUPNAME | usergroup_test | 取自激活配置中的BwmUserGroup实例名 |

### 调测步骤

**步骤1：验证License开关**

```
LST LICENSESWITCH:LICITEM="LKV3G5SBTS01";
```

- SWITCH为ENABLE：继续下一步
- SWITCH为DISABLE：执行 SET LICENSESWITCH 打开开关

**步骤2：验证特征库加载状态**

```
DSP SIGNATUREDB
```

期望输出：
```
协议识别特征库信息
------------------
   特征库加载模式  =  更新为最新的特征库版本
     特征库版本号  =  01.0002.1071.01
   特征库加载状态  =  加载完成
```

加载失败则检查特征库文件后重新加载。

**步骤3：验证BWM用户组配置**

```
LST BWMUSERGROUP:QRYUSRGRPTYPE=SPECIFIC_GROUP,USERGROUPNAME="usergroup_test";
```

期望输出：
```
用户组信息
----------
        用户组名称  =  usergroup_test
        用户组类型  =  Specific User Group
      用户组优先级  =  2
    用户级业务类型  =  TOS
  用户组级业务类型  =  TOS
```

**步骤4：验证APN绑定**

```
LST APNBINDBWMUSRG
```

期望输出：
```
用户组APN绑定信息
-----------------
 用户组名称  =  usergroup_test
        APN  =  huawei.com
```

**步骤5：验证BWM规则**

```
LST BWMRULE
```

检查要点：
1. BWMRule下配置的BwmService是否正确（如p2p）
2. BwmRule是否为用户级规则（SUBSCRIBER_SPECIFIC）
3. BWMRule下配置的BwmController

**步骤6：验证BWM控制器**

```
LST BWMCONTROLLER
```

期望输出：
```
带宽管理控制器信息
------------------
               带宽管理控制器名称  =  bwmc_test
                 带宽管理控制类型  =  Shaping
          速率（千比特/秒）  =  50
               队列深度（包）  =  256
               最大五元组数  =  2000
```

验证效果：用户进行TOS值为BE的业务，使用流量检测工具查看带宽控制结果，流量被控制在整形速率以内。

**步骤7：监控整形缓存使用率**

```
DSP SHAPINGBUFUSED
```

期望输出：
```
整形缓存使用信息
--------
POD名称                使用的缓存数  总缓存数  IPSQM使用的缓存数  IPSQM总缓存数

isu-pod-0178-32-2-101  0             200032    0                  85128
isu-pod-2178-32-2-121  0             200032    0                  85128
```

关键指标：
- **使用的缓存数**：已使用的Shaping Buffer数目
- **总缓存数**：Shaping Buffer总数
- **告警阈值**：如果已使用数目超过总数的 **80%**，需要调整队列深度（QUEDEPTH）

---

## 参考信息

### 与其他特性的关系

| 关系类型 | 特性 | 控制项 | 交互说明 |
|----------|------|--------|----------|
| **依赖** | GWFD-110101 SA-Basic | 82209749 SA-Basic | 需要对用户上下行数据进行识别解析，必须开启业务感知功能 |
| **依赖** | GWFD-110311 基于业务感知的带宽控制 | 82209832 基于业务感知的带宽控制 | 依赖该功能对业务的区分与匹配，必须开启 |
| 对比 | GWFD-110313 基于智能Shaping的组级带宽控制 | - | GWFD-110313 是**组级**Shaping，本特性是**用户级**Shaping；本特性仅在用户级规则生效 |
| 对比 | GWFD-110311 基于业务感知的带宽控制 | - | GWFD-110311 同时支持Shaping和Policing，本特性专注于Shaping |

### 客户价值

| 受益方 | 受益描述 |
|--------|----------|
| 运营商 | 减少运维和扩容成本，减轻运营负载 |
| 用户 | 优化上网体验，上网速率保持均匀 |

### 对系统的影响

用户报文需要缓存或者解析，系统吞吐量将下降，并会带来一定的延迟。详细性能影响需要基于流量模型进行评估，请联系华为技术支持获取服务。

### 应用场景

本特性适用以下场景：用户业务占用大量网络带宽资源，造成带宽拥塞。

### 应用限制

- 仅在用户级带宽控制规则中生效（BWMRULETYPE=SUBSCRIBER_SPECIFIC）

---

## 知识来源

### 文档清单

| 序号 | 文档名称 | 文档类型 | 原始路径 |
|------|----------|----------|----------|
| 1 | GWFD-020354 基于业务的Shaping特性概述 | 特性概述 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/GWFD-020354 基于业务的Shaping特性概述_83823121.md |
| 2 | 实现原理 | 实现原理 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/实现原理_83823122.md |
| 3 | GWFD-020354 基于业务的Shaping参考信息 | 参考信息 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/GWFD-020354 基于业务的Shaping参考信息_83195649.md |
| 4 | 针对TOS基于用户的流量整形 | 激活配置 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/激活基于业务的Shaping/针对TOS基于用户的流量整形_83195647.md |
| 5 | 针对URL应用基于用户的流量整形配置 | 激活配置 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/激活基于业务的Shaping/针对URL应用基于用户的流量整形配置_83195646.md |
| 6 | 调测基于业务的Shaping | 调测指南 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/调测基于业务的Shaping_83195648.md |
