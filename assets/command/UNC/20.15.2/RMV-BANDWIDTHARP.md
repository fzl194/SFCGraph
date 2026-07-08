---
id: UNC@20.15.2@MMLCommand@RMV BANDWIDTHARP
type: MMLCommand
name: RMV BANDWIDTHARP（删除基于带宽的ARP控制配置）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV BANDWIDTHARP（删除基于带宽的ARP控制配置）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用于删除当前APN配置带宽比例差异化服务配置。当需要取消指定用户级别和业务级别对应的拒绝、恢复告警门限时，使用此命令。此命令支持批量删除。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS Profile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |
| SERVICELEVEL | 业务级别 | 可选必选说明：必选参数<br>参数含义：该参数用于指定差异化服务配置的业务级别。<br>数据来源：全网规划<br>取值范围：<br>- GENERAL（通用业务）<br>- CONVERSATIONAL（会话业务）<br>- STM_GBR_MORE25K（下行保证带宽大于等于25kbit/s的流类业务）<br>- STM_GBR_LESS25K（下行保证带宽小于25kbit/s的流类业务）<br>- INT_TC_PRI1（发送控制优先级为1的交互类业务）<br>- INT_TC_PRI2（发送控制优先级为2的交互类业务）<br>- INT_TC_PRI3（发送控制优先级为3的交互类业务）<br>- BACKGROUND（背景业务）<br>默认值：无<br>配置原则：无 |
| USERPRIORITY | 用户级别 | 可选必选说明：必选参数<br>参数含义：该参数用于指定差异化服务配置的用户级别。<br>数据来源：全网规划<br>取值范围：<br>- “HIGH（高）”：高优先级<br>- “NORMAL（中）”：正常优先级<br>- “LOW（低）”：低优先级<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BANDWIDTHARP]] · 基于带宽的ARP控制配置（BANDWIDTHARP）

## 使用实例

假设运营商需要取消已经为APN实例按带宽比例差异化服务的配置，包括与应用级别以及业务级别对应的拒绝告警门限和恢复告警门限信息时，删除BandwidthArp配置：

```
RMV BANDWIDTHARP: QOSPROFILENAME="test", USERPRIORITY=HIGH, SERVICELEVEL=GENERAL;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-BANDWIDTHARP.md`
