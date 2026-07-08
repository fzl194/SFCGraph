---
id: UDG@20.15.2@MMLCommand@SET UPTMPATH
type: MMLCommand
name: SET UPTMPATH（设置TM路径相关属性）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UPTMPATH
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
effect_mode: 对新用户生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 路径管理
- TM路径管理
- TM路径参数
status: active
---

# SET UPTMPATH（设置TM路径相关属性）

## 功能

**适用NF：SGW-U、PGW-U**

![](设置TM路径相关属性（SET UPTMPATH）_68602067.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，配置不合理可能导致告警或者用户去活，建议根据现网规划设置。

该命令用来设置TM协议配置属性。包括当前系统支持主动发送TM消息重发时间间隔和最大尝试发送次数，Echo消息重发时间间隔和路径断后发送次数，NE状态空闲检查开关和NE空闲状态超时时间。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ECHOSW | ECHOINTERVAL | T3RESPONSE | N3REQUEST | DEACTIVEFLAG | ECHOTIME | NESTATUSCHKSW | NESTATUSTIMEOUT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | ENABLE | 60 | 3 | 3 | DISABLE | 30 | ENABLE | 2 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ECHOSW | Echo开关 | 可选必选说明：可选参数<br>参数含义：设置系统是否主动发送路径Echo消息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| ECHOINTERVAL | 发送TM心跳请求的间隔时间 | 可选必选说明：可选参数<br>参数含义：设置发送TM心跳请求的间隔时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为60～3600，单位是秒。<br>默认值：无<br>配置原则：无 |
| T3RESPONSE | TM请求消息的重发时间间隔 | 可选必选说明：可选参数<br>参数含义：TM请求消息的重发时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20，单位是秒。<br>默认值：无<br>配置原则：无 |
| N3REQUEST | TM请求消息的最大尝试发送次数 | 可选必选说明：可选参数<br>参数含义：TM请求消息的最大尝试发送次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～6。<br>默认值：无<br>配置原则：无 |
| DEACTIVEFLAG | 是否去活路径上已激活的上下文 | 可选必选说明：可选参数<br>参数含义：用于配置路径断告警产生后是否去激活该路径上已激活的上下文。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| ECHOTIME | 路径断告警后发送echo消息的次数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DEACTIVEFLAG”配置为“ENABLE”时为可选参数。<br>参数含义：指定在路径断告警产生后发送心跳消息的次数，之后执行去激活操作。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～60。<br>默认值：无<br>配置原则：无 |
| NESTATUSCHKSW | NE状态消息空闲检查开关 | 可选必选说明：可选参数<br>参数含义：用于配置是否检查NE状态消息的空闲时长。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| NESTATUSTIMEOUT | NE状态消息空闲超时时长 | 可选必选说明：条件可选参数<br>前提条件：该参数在“NESTATUSCHKSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置NE状态消息空闲检测时长（分钟）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1440，单位是分钟。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPTMPATH]] · TM路径相关属性（UPTMPATH）

## 使用实例

设置Echo开关为开， 发送TM心跳请求的间隔时间设置为60秒， TM请求消息的重发时间间隔设置为20秒，TM请求消息的最大尝试发送次数设置为2，TM路径Down时去活路径上的用户，路径断告警后发送echo消息的次数为5，NE状态消息空闲检查开关设置为关：

```
SET UPTMPATH: ECHOSW=ENABLE, ECHOINTERVAL=60, T3RESPONSE=20, N3REQUEST=2, DEACTIVEFLAG=ENABLE, ECHOTIME=5, NESTATUSCHKSW=DISABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置TM路径相关属性（SET-UPTMPATH）_68602067.md`
