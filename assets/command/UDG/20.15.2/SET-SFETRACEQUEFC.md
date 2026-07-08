---
id: UDG@20.15.2@MMLCommand@SET SFETRACEQUEFC
type: MMLCommand
name: SET SFETRACEQUEFC（设置VNRS IP消息跟踪的队列流控配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SFETRACEQUEFC
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 跟踪管理
status: active
---

# SET SFETRACEQUEFC（设置VNRS IP消息跟踪的队列流控配置）

## 功能

![](设置VNRS IP消息跟踪的队列流控配置(SET SFETRACEQUEFC)_62471544.assets/notice_3.0-zh-cn.png)

如果设置的队列流控配置不合理，可能会导致跟踪功能不可用或业务呼损。

该命令用来设置VNRS IP消息跟踪的队列流控配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。
- 该命令存在系统初始记录（NP卡加速模式场景无需关注此初始记录），参数的初始设置值如下表：
  | ENABLE | TRIGGERTHD | AUTORECOVERY | RECOVERYTHD | RECOVERYINTERVAL |
  | --- | --- | --- | --- | --- |
  | TRUE（是） | 70 | TRUE（是） | 30 | 5 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENABLE | 队列流控使能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否开启VNRS IP消息跟踪的队列流控功能。<br>数据来源：本端规划<br>取值范围：<br>- “TRUE（是）”：表示队列流控功能开启。<br>- “FALSE（否）”：表示队列流控功能关闭。<br>默认值：无<br>配置原则：无。 |
| TRIGGERTHD | 起控阈值（%） | 可选必选说明：该参数在“队列流控使能开关”配置为“TRUE（是）”时为条件可选参数。<br>参数含义：该参数用于指定触发队列流控的队列使用率阈值。在执行VNRS IP消息跟踪任务期间，如果队列使用率大于等于该参数取值，则触发队列流控。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~100。<br>默认值：无<br>配置原则：<br>**“**<br>起控阈值（%）<br>**”**<br>必须大于<br>**“**<br>恢复阈值（%）<br>**”**<br>。 |
| AUTORECOVERY | 队列流控自动恢复开关 | 可选必选说明：该参数在“队列流控使能开关”配置为“TRUE（是）”时为条件必选参数。<br>参数含义：该参数用于指定触发队列流控后，当满足恢复条件时，能否停止流控且恢复跟踪。<br>数据来源：本端规划<br>取值范围：<br>- “TRUE（是）”：表示能停止流控且恢复跟踪。<br>- “FALSE（否）”：表示不能停止流控且恢复跟踪。<br>默认值：无<br>配置原则：无。 |
| RECOVERYTHD | 恢复阈值（%） | 可选必选说明：该参数在“队列流控自动恢复开关”配置为“TRUE（是）”时为条件可选参数。<br>参数含义：该参数用于指定触发队列流控后，停止流控且恢复跟踪的队列使用率阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~100。<br>默认值：无<br>配置原则：<br>**“**<br>恢复阈值（%）<br>**”**<br>必须小于<br>**“**<br>起控阈值（%）<br>**”**<br>。 |
| RECOVERYINTERVAL | 自动恢复检测时间（min） | 可选必选说明：该参数在“队列流控自动恢复开关”配置为“TRUE（是）”时为条件可选参数。<br>参数含义：该参数用于指定触发队列流控后，对队列使用率的持续检测时间，单位：分钟。如果队列使用率在<br>**“**<br>自动恢复检测时间（min）<br>**”**<br>内持续小于等于“恢复阈值（%）”，则停止流控且恢复跟踪。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~30。<br>默认值：无<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFETRACEQUEFC]] · VNRS IP消息跟踪的队列流控配置（SFETRACEQUEFC）

## 使用实例

```
设置VNRS IP消息跟踪的队列流控配置为开启队列流控功能，起控阈值为70%，开启队列流控自动恢复功能，恢复阈值为30%，自动恢复检测时间为5分钟。
```

```
SET SFETRACEQUEFC: ENABLE=TRUE, TRIGGERTHD=70, AUTORECOVERY=TRUE, RECOVERYTHD=30, RECOVERYINTERVAL=5;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置VNRS-IP消息跟踪的队列流控配置(SET-SFETRACEQUEFC)_62471544.md`
