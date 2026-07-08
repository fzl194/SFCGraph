---
id: UNC@20.15.2@MMLCommand@ADD PRER8REMARK
type: MMLCommand
name: ADD PRER8REMARK（增加Pre-R8 QoS到TOS/DSCP的映射规则）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD PRER8REMARK（增加Pre-R8 QoS到TOS/DSCP的映射规则）

## 功能

**适用NF：GGSN**

该命令用来配置UNC全局的或者基于QosProfile的QoS映射规则。基于QosProfile的QoS映射规则可与APN实例绑定，用来控制此APN下会话的QoS映射规则。UNC支持将用户在会话激活或者更新过程中协商的QoS参数映射为IP报文头中的TOS（服务类型）域或者DSCP（区别服务编码点），这样用户的数据报文在传送过程中，UNC将映射出的TOS或者DSCP填写到用户数据报文的IP头中，该IP报文在传送过程将根据TOS或者DSCP编码获得不同的处理优先级，从而满足服务质量的要求。

## 注意事项

- 该命令执行后只对新激活用户生效。

- RFC2597推荐的BE编码点：000000；RFC2598推荐的EF编码点：101110。

- 最多可输入1000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QosProfile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |
| SERVICELEVEL | 业务级别 | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务级别。<br>数据来源：本端规划<br>取值范围：<br>- “CONVERSATIONAL（会话业务）”：会话业务。<br>- “STM_GBR_MORE25K（下行保证带宽大于等于25kbit/s的流类业务）”：下行保证带宽大于等于25kbit/s的流类业务。<br>- “STM_GBR_LESS25K（下行保证带宽小于25kbit/s的流类业务）”：下行保证带宽小于25kbit/s的流类业务。<br>- “INT_TC_PRI1（发送控制优先级为1的交互类业务）”：发送控制优先级为1的交互类业务。<br>- “INT_TC_PRI2（发送控制优先级为2的交互类业务）”：发送控制优先级为2的交互类业务。<br>- “INT_TC_PRI3（发送控制优先级为3的交互类业务）”：发送控制优先级为3的交互类业务。<br>- “BACKGROUND（背景业务）”：背景业务。<br>- “GENERAL（通用业务）”：通用业务。<br>默认值：无<br>配置原则：无 |
| USERPRIORITY | 用户级别 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户级别。<br>数据来源：本端规划<br>取值范围：<br>- “GENERAL（通用用户）”：通用用户。<br>- “HIGH（高端用户）”：高端用户。<br>- “NORMAL（普通用户）”：普通用户。<br>- “LOW（低端用户）”：低端用户。<br>默认值：无<br>配置原则：无 |
| REMARKTYPE | 标记类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置映射到DSCP或者TOS。<br>数据来源：全网规划<br>取值范围：<br>- “DSCP（DSCP）”：映射到DSCP。<br>- “TOS（TOS）”：映射到TOS<br>默认值：无<br>配置原则：无 |
| DSCP | DSCP | 可选必选说明：该参数在"REMARKTYPE"配置为"DSCP"时为条件必选参数。<br>参数含义：该参数用于设置映射到DSCP的值。<br>数据来源：全网规划<br>取值范围：<br>- “EF（EF）”：对应的DSCP的值为46。<br>- “AF（AF）”：对应的DSCP的值由参数AF级别和AF丢弃优先级界定。<br>- “BE（BE）”：对应的DSCP的值为0。<br>- “CS6（CS6）”：对应的DSCP的值为48。<br>- “CS7（CS7）”：对应的DSCP的值为56。<br>- “DSCP_VALUE（DSCP_VALUE）”：映射的DSCP值。<br>默认值：无<br>配置原则：无 |
| AFCLASS | AF级别 | 可选必选说明：该参数在"DSCP"配置为"AF"时为条件必选参数。<br>参数含义：该参数用于设置AF队列序号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~4。<br>默认值：无<br>配置原则：无 |
| AFDROPPREC | AF丢弃优先级 | 可选必选说明：该参数在"DSCP"配置为"AF"时为条件必选参数。<br>参数含义：该参数用于设置AF丢弃优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~3。<br>默认值：无<br>配置原则：无 |
| TOSVALUE | TOS值 | 可选必选说明：该参数在"REMARKTYPE"配置为"TOS"时为条件必选参数。<br>参数含义：该参数用于设置映射到TOS的值。分别对应IP优先级的8个队列ID，优先级高的报文先于优先级低的报文发送。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~7。<br>默认值：无<br>配置原则：无 |
| DSCPVALUE | DSCP值 | 可选必选说明：该参数在"DSCP"配置为"DSCP_VALUE"时为条件必选参数。<br>参数含义：该参数用于设置DSCP。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PRER8REMARK]] · Pre-R8 QoS到TOS/DSCP的映射规则（PRER8REMARK）

## 使用实例

添加QoS Profile名称为“profile”，会话级别为“CONVERSATIONAL”，用户级别为“HIGH”的QoS到DSCP的映射信息，标记类型为“DSCP”,参数“DSCP”为“BE”：

```
ADD PRER8REMARK: QOSPROFILENAME="profile", SERVICELEVEL=CONVERSATIONAL, USERPRIORITY=HIGH, REMARKTYPE=DSCP, DSCP=BE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Pre-R8-QoS到TOS_DSCP的映射规则（ADD-PRER8REMARK）_09654400.md`
