---
id: UNC@20.15.2@MMLCommand@RMV PDPNUMBERARP
type: MMLCommand
name: RMV PDPNUMBERARP（删除基于PDP数的ARP控制）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PDPNUMBERARP
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- Qos管理
- 基于PDP数的ARP控制
status: active
---

# RMV PDPNUMBERARP（删除基于PDP数的ARP控制）

## 功能

**适用NF：SGW-C、PGW-C、GGSN**

当需要取消指定用户级别和业务级别对应的拒绝、恢复告警门限时，使用此命令。此命令支持批量删除。

## 注意事项

- 该命令执行后立即生效。

- 建议在告警恢复后再删除基于PDP数的ARP控制规则。在告警没有恢复的情况下，删除基于PDP数的ARP控制规则，将导致后续用户无法接入。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS Profile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |
| SERVICELEVEL | 业务级别 | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务级别。<br>数据来源：本端规划<br>取值范围：<br>- GENERAL（通用业务）<br>- CONVERSATIONAL（会话业务）<br>- STM_GBR_MORE25K（下行保证带宽大于等于25kbit/s的流类业务）<br>- STM_GBR_LESS25K（下行保证带宽小于25kbit/s的流类业务）<br>- INT_TC_PRI1（发送控制优先级为1的交互类业务）<br>- INT_TC_PRI2（发送控制优先级为2的交互类业务）<br>- INT_TC_PRI3（发送控制优先级为3的交互类业务）<br>- BACKGROUND（背景业务）<br>默认值：无<br>配置原则：无 |
| USERPRIORITY | 用户级别 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户级别。<br>数据来源：本端规划<br>取值范围：<br>- “HIGH（高）”：高优先级<br>- “NORMAL（中）”：正常优先级<br>- “LOW（低）”：低优先级<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PDPNUMBERARP]] · 基于PDP数的ARP控制（PDPNUMBERARP）

## 使用实例

当运营商需要删除不同的用户级别，业务级别对应的拒绝告警门限和恢复告警门限信息时，使用如下命令：

```
RMV PDPNUMBERARP: QOSPROFILENAME="test", USERPRIORITY=HIGH, SERVICELEVEL=GENERAL;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PDPNUMBERARP.md`
