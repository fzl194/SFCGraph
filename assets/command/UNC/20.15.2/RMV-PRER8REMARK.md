---
id: UNC@20.15.2@MMLCommand@RMV PRER8REMARK
type: MMLCommand
name: RMV PRER8REMARK（删除Pre-R8 QoS到TOS/DSCP的映射规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PRER8REMARK
command_category: 配置类
applicable_nf:
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- PreR8 QoS配置
- PreR8 Qos映射ToS_DSCP
status: active
---

# RMV PRER8REMARK（删除Pre-R8 QoS到TOS/DSCP的映射规则）

## 功能

**适用NF：GGSN**

该命令用于删除QoS参数映射到IP报文头中的TOS（服务类型）或者DSCP（区别服务编码点）的映射配置。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QosProfile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |
| SERVICELEVEL | 业务级别 | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务级别。<br>数据来源：本端规划<br>取值范围：<br>- “CONVERSATIONAL（会话业务）”：会话业务。<br>- “STM_GBR_MORE25K（下行保证带宽大于等于25kbit/s的流类业务）”：下行保证带宽大于等于25kbit/s的流类业务。<br>- “STM_GBR_LESS25K（下行保证带宽小于25kbit/s的流类业务）”：下行保证带宽小于25kbit/s的流类业务。<br>- “INT_TC_PRI1（发送控制优先级为1的交互类业务）”：发送控制优先级为1的交互类业务。<br>- “INT_TC_PRI2（发送控制优先级为2的交互类业务）”：发送控制优先级为2的交互类业务。<br>- “INT_TC_PRI3（发送控制优先级为3的交互类业务）”：发送控制优先级为3的交互类业务。<br>- “BACKGROUND（背景业务）”：背景业务。<br>- “GENERAL（通用业务）”：通用业务。<br>默认值：无<br>配置原则：无 |
| USERPRIORITY | 用户级别 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户级别。<br>数据来源：本端规划<br>取值范围：<br>- “GENERAL（通用用户）”：通用用户。<br>- “HIGH（高端用户）”：高端用户。<br>- “NORMAL（普通用户）”：普通用户。<br>- “LOW（低端用户）”：低端用户。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PRER8REMARK]] · Pre-R8 QoS到TOS/DSCP的映射规则（PRER8REMARK）

## 使用实例

删除QoS Profile名称为profile的QoS的DSCP的映射信息：

```
RMV PRER8REMARK: QOSPROFILENAME="profile", SERVICELEVEL=GENERAL, USERPRIORITY=HIGH;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Pre-R8-QoS到TOS_DSCP的映射规则（RMV-PRER8REMARK）_09652655.md`
