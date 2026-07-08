---
id: UDG@20.15.2@MMLCommand@ADD RPTSVR
type: MMLCommand
name: ADD RPTSVR（配置报表服务器）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: RPTSVR
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 11
category_path:
- 业务报表管理
- 报表服务器管理
- 报表服务器
status: active
---

# ADD RPTSVR（配置报表服务器）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置报表服务器。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为11。
- 当报表消息类型为SUBSCRIPTION时，SUCCESSLT参数无效。FAILURELT和TIMERTHD的乘积为报表服务器的链路故障时间，当参数TIMERTHD取值为0时，链路故障时间设置为一分钟；当乘积大于一小时时，链路故障时间设置为一小时。
- EXP类型报表服务器只允许配置一个。
- 当报表消息类型为EXP时，SVRFUNC参数无效，此类型的服务器仅对SSU生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RPTSVRNAME | 报表服务器名称 | 可选必选说明：必选参数<br>参数含义：设置报表服务器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| RPTSVRTYPE | 报表消息类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置报表消息类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- UFDR：表示报表话单为UFDR格式。<br>- ADR：表示ADR上报使用的报表Server。<br>- SUBSCRIPTION：表示订阅消息下发使用的报表Server。<br>- BASIC：表示上报基础信息使用的报表Server。<br>- BTDR：表示上报基础信息使用的M+服务器类型。<br>- ALLTYPE：表示所有报表话单类型（不含EXP）。<br>- EXP：表示上报体验分析信息使用的报表Server。<br>默认值：ALLTYPE<br>配置原则：无 |
| SUCCESSLT | 心跳检测成功次数阈值 | 可选必选说明：可选参数<br>参数含义：该参数设置达到链路恢复状态的心跳检测成功的次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10，单位是次数。<br>默认值：6<br>配置原则：无 |
| FAILURELT | 心跳检测的失败次数门限 | 可选必选说明：可选参数<br>参数含义：该参数设置达到链路故障状态的心跳检测失败的次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10，单位是次数。<br>默认值：6<br>配置原则：无 |
| TIMERTHD | 心跳消息发送时间间隔 | 可选必选说明：可选参数<br>参数含义：该参数用于设置心跳消息发送时间间隔，取值为0表示关闭心跳发送功能。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1440，单位是秒。<br>默认值：10<br>配置原则：无 |
| SVRFUNC | 服务器功能 | 可选必选说明：可选参数<br>参数含义：该参数用于设置报表服务器功能。<br>数据来源：本端规划<br>取值范围：位域类型。不支持空格，不区分大小写。<br>- RPT：普通报表服务器。<br>- SSU：智能板单据的报表服务器。<br>默认值：RPT-1&SSU-1<br>配置原则：无 |

## 操作的配置对象

- [报表服务器（RPTSVR）](configobject/UDG/20.15.2/RPTSVR.md)

## 使用实例

设置报表服务器名称：

```
ADD RPTSVR: RPTSVRNAME="report01", RPTSVRTYPE=UFDR, SUCCESSLT=2, FAILURELT=2, SVRFUNC=RPT-1&SSU-0;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/配置报表服务器（ADD-RPTSVR）_79568179.md`
