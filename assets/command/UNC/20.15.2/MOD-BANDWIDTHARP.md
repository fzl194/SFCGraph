---
id: UNC@20.15.2@MMLCommand@MOD BANDWIDTHARP
type: MMLCommand
name: MOD BANDWIDTHARP（修改基于带宽的ARP控制配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: BANDWIDTHARP
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- Qos管理
- 基于带宽的ARP控制
status: active
---

# MOD BANDWIDTHARP（修改基于带宽的ARP控制配置）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用于修改指定APN配置带宽比例差异化服务。当需要为指定的用户级别、业务级别配置不同的拒绝、恢复告警门限时，使用此命令。

## 注意事项

- 该命令执行后立即生效。

- 参数RESTORELIMIT的值必须小于参数REJECTLIMIT的值。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS Profile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |
| SERVICELEVEL | 业务级别 | 可选必选说明：必选参数<br>参数含义：该参数用于指定差异化服务配置的业务级别。<br>数据来源：全网规划<br>取值范围：<br>- GENERAL（通用业务）<br>- CONVERSATIONAL（会话业务）<br>- STM_GBR_MORE25K（下行保证带宽大于等于25kbit/s的流类业务）<br>- STM_GBR_LESS25K（下行保证带宽小于25kbit/s的流类业务）<br>- INT_TC_PRI1（发送控制优先级为1的交互类业务）<br>- INT_TC_PRI2（发送控制优先级为2的交互类业务）<br>- INT_TC_PRI3（发送控制优先级为3的交互类业务）<br>- BACKGROUND（背景业务）<br>默认值：无<br>配置原则：无 |
| USERPRIORITY | 用户级别 | 可选必选说明：必选参数<br>参数含义：该参数用于指定差异化服务配置的用户级别。<br>数据来源：全网规划<br>取值范围：<br>- “HIGH（高）”：高优先级<br>- “NORMAL（中）”：正常优先级<br>- “LOW（低）”：低优先级<br>默认值：无<br>配置原则：无 |
| REJECTLIMIT | 拒绝告警门限(%) | 可选必选说明：必选参数<br>参数含义：该参数用于指定差异化服务配置的拒绝告警门限。表示占最大用户数的百分比。特定用户级别、业务级别的用户数增长达到拒绝告警门限时，拒绝继续接入该类用户，并产生告警。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是2~100。<br>默认值：无<br>配置原则：无 |
| RESTORELIMIT | 恢复告警门限(%) | 可选必选说明：必选参数<br>参数含义：该参数用于指定差异化服务配置的恢复告警门限。表示占最大用户数的百分比。特定用户级别、业务级别的用户数下降达到恢复告警门限时，允许继续接入该类用户，并恢复告警。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~99。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BANDWIDTHARP]] · 基于带宽的ARP控制配置（BANDWIDTHARP）

## 使用实例

假设运营商需要为APN实例按带宽比例差异化服务修改与应用级别以及业务级别对应的拒绝告警门限和恢复告警门限信息时，修改BandwidthArp配置：

```
MOD BANDWIDTHARP: QOSPROFILENAME="test", USERPRIORITY=HIGH, SERVICELEVEL=GENERAL, REJECTLIMIT=60, RESTORELIMIT=30;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-BANDWIDTHARP.md`
