---
id: UNC@20.15.2@MMLCommand@SET TXTIMER
type: MMLCommand
name: SET TXTIMER（设置DCC模板Tx定时器）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: TXTIMER
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
max_records: 101
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- 信用控制
- 信用控制模板
status: active
---

# SET TXTIMER（设置DCC模板Tx定时器）

## 功能

**适用NF：PGW-C、SMF**

![](设置DCC模板Tx定时器（SET TXTIMER）_09896927.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，执行命令配置超时时长不合理可能导致在超时场景下，激活响应的总时长过长，这可能会导致用户激活失败。在前期规划时，建议1：产品配置的等待右侧网元的最大时长小于产品ADD GTPCT3N3命令配置的T3N3时长及左侧（MME/SGSN等）的T3N3时长。建议2：产品配置的等待右侧网元的最大时长小于产品SET SMCOMMTIMER命令配置的TCHARGING（等待计费网关响应定时器）的时长。

该命令用于设置DCC在线计费模板Tx定时器。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为101。
- 在前期规划时，建议1：产品配置的等待右侧网元的最大时长小于产品ADD GTPCT3N3命令配置的T3N3时长及左侧（MME\SGSN等）的T3N3时长，避免右侧网元无响应造成激活响应的总时长过长。建议2：产品配置的等待右侧网元的最大时长小于产品SET SMCOMMTIMER命令配置的TCHARGING （等待计费网关响应定时器）的时长，避免右侧网元响应总时长过长导致用户去活。如果涉及产品与多个右侧网元交互的场景，请联系华为公司研发人员给出推荐值。
- 该命令设定后的数据，需要通过LST DCCTEMPLATE命令进行查看。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | DCCTMPLTNAME | TXTIMERFLAG | TXTIMER | RETRYTIMES | RETRYTIMEOUT |
| --- | --- | --- | --- | --- | --- |
| 初始值 | global | TXTIMER_VALUE | 3 | 4294967295 | 4294967295 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCCTMPLTNAME | DCC模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定操作的DCC在线计费模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD DCCTEMPLATE命令配置生成。<br>- 该命令基于此参数配置DCC在线计费模板的Tx定时器。 |
| TXTIMERFLAG | Tx定时器配置模式 | 可选必选说明：必选参数<br>参数含义：该参数用于设置Tx定时器配置模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TXTIMER_VALUE：tx定时器时长。<br>- APP_RETRANSMIT：应用层重传配置。<br>- INHERIT：继承。<br>默认值：无<br>配置原则：无 |
| TXTIMER | Tx定时器时长（秒） | 可选必选说明：条件必选参数<br>前提条件：该参数在“TXTIMERFLAG”配置为“TXTIMER_VALUE”时为必选参数。<br>参数含义：该参数用于指定Tx定时器时长，用来控制OCS的响应消息的时间；当超过此定时器的超时时间，则认为OCS消息返回失败，系统会做相应的处理。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20，4294967295，单位是秒。<br>默认值：无<br>配置原则：无 |
| RETRYTIMES | 应用重传次数 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TXTIMERFLAG”配置为“APP_RETRANSMIT”时为必选参数。<br>参数含义：该参数用于设置UNC在OCS响应Tx定时器超时后进行应用层重传的重传次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～3。<br>默认值：无<br>配置原则：应用层重传与链路层重传功能重叠，可能导致消息重发次数大于预期，此功能建议不开启。 |
| RETRYTIMEOUT | 应用重传时间间隔（秒） | 可选必选说明：条件必选参数<br>前提条件：该参数在“TXTIMERFLAG”配置为“APP_RETRANSMIT”时为必选参数。<br>参数含义：该参数用于设置UNC在OCS响应在Tx定时器超时后进行应用层重传的重传时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～3，单位是秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TXTIMER]] · DCC模板Tx定时器（TXTIMER）

## 使用实例

设置名为“DccTemplate”的DCC在线计费模板的Tx定时器时长为10秒：

```
SET TXTIMER:DCCTMPLTNAME="DccTemplate",TXTIMERFLAG=TXTIMER_VALUE,TXTIMER=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-TXTIMER.md`
