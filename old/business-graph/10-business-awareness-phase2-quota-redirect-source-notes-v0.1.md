# 业务感知第二条主线原始语料笔记 v0.1

## 1. 本页定位

本页固定第二条主线的直接原始语料、已确认事实和当前已落地的正式 MVP 增量。

当前目标主线：

```text
配额耗尽动作
+ 重定向
```

## 2. 直接原始语料

### 2.1 UDG 业务感知场景举例

文件：

- `output\UDG_Product_Documentation_CH_20.15.2\特性部署\业务专题\UDG业务感知专题\业务感知功能描述\业务感知场景举例_92407896.md`

当前已确认事实：

1. 场景定义不是单纯的“计费”，而是：
   - A 网站视频不计流量
   - 非 A 网站视频正常计费
   - 流量耗尽后重定向到充值页面
2. 规则不是静态全集常驻，而是：
   - 初始启用 `Rule1`、`Rule2`
   - 流量耗尽后，PCF 下发 `Rule3` 并停用 `Rule2`
3. UPF 侧最终行为是：
   - 报文仍优先匹配 `Rule1`
   - 未命中时命中 `Rule3`
   - `Rule3` 的动作是重定向

这份文档直接说明：

```text
业务感知不仅有“识别 + 计费”，
还存在“状态变化 -> 规则切换 -> 动作切换”。
```

### 2.2 UNC 命令：ADD QUOTAEXHAUSTACT

文件：

- `output\UNC 20.15.2 产品文档(裸机容器) 05\OM参考\命令\UNC MML命令\业务服务管理\会话管理\计费管理\融合计费\配额耗尽处理动作\增加配额耗尽后的动作（ADD QUOTAEXHAUSTACT）_95129686.md`

当前已确认事实：

1. 命令功能：
   - 用于增加在线 RG 配额耗尽后的动作
2. 动作枚举：
   - `BLOCK`
   - `REDIRECT`
   - `FORWARD`
3. `ACTION=REDIRECT` 时：
   - `RDVIRTIP`
   - `RDVIRTIPV6`
   为条件可选参数
4. 依赖对象：
   - `CCTMPLTNAME` 使用 `ADD CCT` 配置生成
5. 作用范围：
   - 命令执行后只对新激活用户生效

这份命令文档直接说明：

```text
配额耗尽动作在 SMF/UNC 侧是正式配置对象，
不是业务专题里一句描述，
并且它不是孤立对象，而是依赖 CCT 模板。
```

### 2.3 UNC 业务专题：配置融合计费费率标识

文件：

- `output\UNC 20.15.2 产品文档(裸机容器) 05\网络部署\业务专题\5G Core 计费解决方案\计费解决方案概述\计费方案部署与调测\方案四：部署NCG且基于服务化接口的离线+在线计费组网方案\SMF配置\配置融合计费费率标识_90679673.md`

当前已确认事实：

1. 主链仍是：

```text
URR
-> URRGroup
-> PCCPolicyGrp
-> Rule
-> UserProfile
-> RuleBinding
```

2. 在这条主链上，文档明确把 `ADD QUOTAEXHAUSTACT` 列为：
   - “可选：配置在线 RG 配额耗尽后的默认动作”
3. 文档还明确动作下发后的运行时含义：
   - `BLOCK` -> FAR 动作 `drop`
   - `REDIRECT` -> FAR 动作 `Redirect Information`
   - `FORWARD` -> FAR 动作 `FORW`

这说明：

```text
第二条主线不是脱离第一条主线的新世界，
而是在第一条计费对象链基础上增加“CCT -> 配额耗尽动作层”。
```

### 2.4 UDG 业务专题：七层重定向功能 / 配置PCC策略

文件：

- `output\UDG_Product_Documentation_CH_20.15.2\特性部署\业务专题\UDG业务感知专题\业务感知配置\激活业务感知\规则配置实例\七层重定向功能_92393307.md`
- `output\UDG_Product_Documentation_CH_20.15.2\特性部署\业务专题\UDG业务感知专题\业务感知配置\激活业务感知\规则配置\配置流动作\配置PCC策略_87803995.md`

当前已确认事实：

1. UDG 侧七层重定向完整配置链是：

```text
L7Filter
-> FlowFilter
-> Redirect
-> PCCActionProp
-> PccPolicyGrp
-> Rule
-> UserProfile
-> RuleBinding
```

2. `配置PCC策略` 明确说明：
   - 识别条件命中后，动作可以是计费、URL 重定向、阻断
   - `ADD REDIRECT`
   - `ADD PCCACTIONPROP`
   - `ADD PCCPOLICYGRP`
   构成 UDG 侧动作配置的通用路径

这说明：

```text
第二条主线不是只有 SMF 上的配额耗尽动作，
还必须补上 UDG/UPF 侧的动作执行链。
```

## 3. 当前对第二条主线的约束判断

### 3.1 不能直接复用第一条闭包的 schema 实例

原因：

- 第一条闭包主要是：
  - `差异化计费`
  - `免费业务`
  - `默认兜底计费`
- 第二条闭包会新增：
  - 状态变化
  - 规则切换
  - 配额耗尽动作
  - 重定向动作

所以第二条主线至少会新增这些语义对象实例：

- `BA.QuotaSemantics`
- `BA.PolicyActionSemantics`
- `BA.RuntimeSemantics`

### 3.2 不能只从命令文档抽

原因：

- `ADD QUOTAEXHAUSTACT` 能告诉我们动作枚举和参数
- 但不能告诉我们：
  - 什么时候切换到这条动作规则
  - 动作和业务场景的关系
  - UPF 上最终的规则切换过程

这些必须依赖：

- UDG 业务感知场景举例
- UNC 费率标识配置专题

### 3.3 UNC 命令与特性：CCT 融合计费模板

文件：

- `output\UNC 20.15.2 产品文档(裸机容器) 05\OM参考\命令\UNC MML命令\业务服务管理\会话管理\计费管理\融合计费\融合计费模板\增加融合计费模板（ADD CCT）_09653176.md`
- `output\UNC 20.15.2 产品文档(裸机容器) 05\网络部署\特性部署\UNC特性指南\计费管理功能\WSFD-011206 支持融合计费\激活支持融合计费\配置融合计费模板_93400212.md`

当前已确认事实：

1. `ADD CCT` 用于新增融合计费模板，配置融合计费相关参数。
2. CCT 中包含配额空闲时间、流量/时间/事件阈值、RG/PDU/QF 级阈值、最终配额动作、无配额触发等参数。
3. CCT 可按不同粒度绑定：
   - `UserProfile` 粒度
   - `DNN` 粒度
   - `CC` 粒度
   - 整机通用参数
4. 文档明确给出优先级：

```text
UserProfile > DNN > Charging Characteristics > 整机通用参数
```

这说明：

```text
配额耗尽不是单独的命令动作，
它受 CCT 模板及模板绑定粒度约束。
```

### 3.4 UDG/UNC PCC 基本功能

文件：

- `output\UDG_Product_Documentation_CH_20.15.2\特性部署\特性指南\UDG特性指南\智能策略控制功能\GWFD-020351 PCC基本功能\GWFD-020351 PCC基本功能特性概述_47011385.md`
- `output\UDG_Product_Documentation_CH_20.15.2\特性部署\特性指南\UDG特性指南\智能策略控制功能\GWFD-020351 PCC基本功能\激活PCC基本功能\配置本地PCC功能_74096529.md`
- `output\UNC 20.15.2 产品文档(裸机容器) 05\网络部署\特性部署\UNC特性指南\智能PCC解决方案\WSFD-109101 PCC基本功能\PCC基本功能（5G）\WSFD-109101 PCC基本功能特性概述（适用于5G）_71770359.md`

当前已确认事实：

1. UDG/UPF 侧 PCC 基本功能执行：
   - 业务数据流检测
   - 使用量统计
   - 流量上报
   - QoS 控制
   - 带宽管理
   - 重定向等策略控制
2. UNC/SMF 侧 PCC 基本功能负责：
   - 接收或本地生成会话管理策略
   - 生成 PDR 下发给 UPF
   - 支持动态 PCC、本地 PCC、策略更新
3. UDG 本地 PCC 配置文档明确说明：
   - UDG 上需要配置 `rule` 和 `UserProfile`
   - 具体规则内容根据业务策略确定
   - 规则配置方法参见业务感知配置

这说明：

```text
PCC 基本功能不是一个具体业务，
而是支撑业务感知动作执行、规则下发和规则更新的横向能力。
```

### 3.5 UDG 命令：ADD PCCPOLICYGRP

文件：

- `output\UDG_Product_Documentation_CH_20.15.2\OM参考\命令\UDG MML命令\用户面服务管理\业务控制策略\PCC控制策略\PCC策略组\增加PCC策略组（ADD PCCPOLICYGRP）_82837606.md`

当前已确认事实：

1. PCC 策略组可以包含：
   - `URRGroup`
   - `PCCActionProp`
   - `QosProp`
   - 扩展属性等
2. PCC 策略组支持默认组合和基于 `ServiceProp` 的非默认组合。
3. 文档明确 `PCCACTPROPNAME` 来源于 `ADD PCCACTIONPROP`。
4. 文档明确 `URRGROUPNAME` 来源于 `ADD URRGROUP`。

这说明：

```text
PccPolicyGrp 是动作汇聚对象，
不是单纯的计费绑定对象。
它可以同时承接计费、重定向、QoS 等动作。
```

## 4. 本轮已落地的正式 MVP 增量

### 4.1 新增 NetworkScenario

| 场景ID | 场景名称 | 说明 |
| --- | --- | --- |
| `NS-BA-004` | 配额耗尽动作 | 在线 RG 配额耗尽后触发 `BLOCK` / `REDIRECT` / `FORWARD`。 |
| `NS-BA-005` | 配额耗尽后重定向 | 流量耗尽后从正常计费规则切换到重定向动作。 |
| `NS-BA-006` | 七层重定向 | 根据 URL/Host 等七层识别条件执行 URL 重定向。 |

### 4.2 新增 DeliverySolution

| 方案ID | 方案名称 | 说明 |
| --- | --- | --- |
| `DS-BA-002` | 配额耗尽后重定向 | 在第一条差异化计费链基础上增加 CCT、配额耗尽动作和 UDG 重定向动作链。 |

### 4.3 新增 Capability

| 能力ID | 能力名称 | 证据来源 |
| --- | --- | --- |
| `Capability:BA:PccPolicyControlCP` | 控制面 PCC 策略控制能力 | UNC PCC 基本功能 |
| `Capability:BA:PccPolicyExecutionUP` | 用户面 PCC 策略执行能力 | UDG PCC 基本功能 |
| `Capability:BA:QuotaExhaustAction` | 配额耗尽动作控制能力 | `ADD CCT` / `ADD QUOTAEXHAUSTACT` |
| `Capability:BA:RedirectActionUP` | 用户面重定向动作能力 | UDG 七层重定向 / PCC 策略 |

### 4.4 新增对象链

| 链ID | 对象链 | 用途 |
| --- | --- | --- |
| `CHAIN-UNC-BA-003` | `CCT -> QuotaExhaustAction -> BLOCK/REDIRECT/FORWARD` | 表达 UNC/SMF 侧配额耗尽动作控制。 |
| `CHAIN-UDG-BA-004` | `L7Filter -> FlowFilter -> Redirect -> PCCActionProp -> PccPolicyGrp -> Rule -> UserProfile -> RuleBinding` | 表达 UDG/UPF 侧七层重定向动作链。 |

## 5. 下一步应该怎么做

当前最合理的下一步是对 `DS-BA-002` 做核查，而不是继续扩展新主题。

核查重点：

1. `NS-BA-004/005/006` 是否应该是三个场景，还是应合并为一个场景下的三个阶段。
2. `CCT -> QuotaExhaustAction` 与 `Redirect -> PCCActionProp -> PccPolicyGrp` 是否应该在业务层形成一个统一方案，还是分别属于控制面和用户面的两个可选分支。
3. `GWFD-020351` 和 `WSFD-109101` 是否作为业务感知必需特性，还是作为 PCC 横向支撑特性，只在涉及策略更新/重定向时出现。
4. 业务图谱中是否需要显式加入 `RuntimeFlow` 对象，用来承载“流量耗尽后 PCF/SMF 更新策略，UPF 从 Rule2 切换到 Rule3”的运行时过程。
