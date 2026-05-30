# 业务感知相关命令子集 v0.1

## 1. 本页定位

本页只收业务感知第一条闭包已经直接用到、且在原始语料中有明确支撑的命令子集。

当前主线：

```text
差异化计费
+ 免费业务
+ 默认兜底计费
```

## 2. 当前页和 schema 的关系

本页只收两类 schema 实例：

- `MMLCommand`
- `ConfigObject`

以及两类最直接的命令图谱关系：

- `acts_on`
- 由业务闭包显式使用的 `references / binds / contains` 对象链线索

本页不重新定义命令图谱 schema，正式 schema 仍以：

- `work/business-awareness-result/09-command-graph-build-plan-v0.2.md`

为准。

## 3. UDG 侧命令子集

### 2.1 识别条件构建

| 命令 | 当前作用 | 直接证据 |
| --- | --- | --- |
| ADD IPLIST | 构造 IP 地址集合识别条件 | 套餐1：计费场景 |
| ADD FILTER | 构造三四层过滤条件 | 套餐1：计费场景；规则配置全景 |
| ADD L7FILTER | 构造七层 URL/Host 识别条件 | 套餐1：计费场景；规则配置全景 |
| ADD FLOWFILTER | 组合识别条件为流过滤器 | 套餐1：计费场景；规则配置全景 |
| ADD FLTBINDFLOWF | 绑定 Filter 到 FlowFilter | 套餐1：计费场景；SA-Basic 参考信息 |
| ADD PROTBINDFLOWF | 绑定协议/L7 条件到 FlowFilter | 套餐1：计费场景；SA-Basic 参考信息 |
| ADD FLOWFILTERGRP | 将多个 FlowFilter 组织成组 | 套餐1：计费场景 |

### 2.2 计费动作与规则构建

| 命令 | 当前作用 | 直接证据 |
| --- | --- | --- |
| ADD URR | 定义业务粒度计费 URR | 套餐1：计费场景；SA-Basic 参考信息 |
| ADD URRGROUP | 组织 URR 组 | 套餐1：计费场景；SA-Basic 参考信息 |
| ADD PCCPOLICYGRP | 将 URR 组挂到 PCC 策略组 | 套餐1：计费场景；SA-Basic 参考信息 |
| ADD RULE | 将识别条件与 PCC 策略组绑定成 Rule，并赋予优先级 | 套餐1：计费场景；ADD RULE 原始命令 |
| ADD USERPROFILE | 构造业务套餐承载体 | 套餐1：计费场景；SA-Basic 参考信息 |
| SET URRGRPBINDING | 为 UserProfile 设置缺省 URR 组 | 套餐1：计费场景；SA-Basic 参考信息 |
| ADD RULEBINDING | 将多条 Rule 绑定到同一 UserProfile | 套餐1：计费场景；SA-Basic 参考信息 |
| SET REFRESHSRV | 刷新 UserProfile 生效 | 套餐1：计费场景 |

## 4. UNC/SMF 侧命令子集

### 3.1 特性激活与费率标识配置

| 命令 | 当前作用 | 直接证据 |
| --- | --- | --- |
| SET LICENSESWITCH | 激活内容计费 License | 激活内容计费 |
| ADD URR | 定义在线/离线 URR 和 RG | 配置融合计费费率标识 |
| ADD URRGROUP | 将在线/离线 URR 组织成 URRGroup | 配置融合计费费率标识 |
| ADD PCCPOLICYGRP | 将 URRGroup 绑定到 PCC 策略组 | 配置融合计费费率标识 |
| ADD RULE | 将 PCC 策略组绑定到 Rule | 配置融合计费费率标识 |
| ADD RULEBINDING | 将 Rule 绑定到 UserProfile | 配置融合计费费率标识 |
| SET URRGRPBINDING | 设置 UserProfile 缺省 URRGroup | 配置融合计费费率标识 |

### 3.2 扩展动作

| 命令 | 当前作用 | 当前状态 | 直接证据 |
| --- | --- | --- | --- |
| ADD QUOTAEXHAUSTACT | 定义在线 RG 配额耗尽后动作 | 下一阶段扩展 | 配置融合计费费率标识 |

## 5. 当前命令子集背后的对象链

### 4.1 UDG

```text
IPList
-> Filter / L7Filter / Protocol
-> FlowFilter / FlowFilterGroup
-> URR
-> URRGroup
-> PCCPolicyGrp
-> Rule
-> UserProfile
-> RuleBinding
```

### 4.2 UNC

```text
URR
-> URRGroup
-> PCCPolicyGrp
-> Rule
-> UserProfile
   -> RuleBinding
   -> SET URRGRPBINDING
```

## 6. 当前命令子集的边界

这不是业务感知所有命令。

当前还没有正式并入第一条闭包的命令类型包括：

- 重定向相关命令
- 头增强相关命令
- 带宽控制相关命令
- 安全增强 / 异常下行流量检测相关命令

所以本页定位是：

```text
业务感知第一条计费主线已经确认的直接相关命令子集
```
