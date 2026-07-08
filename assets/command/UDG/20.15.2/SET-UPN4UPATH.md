---
id: UDG@20.15.2@MMLCommand@SET UPN4UPATH
type: MMLCommand
name: SET UPN4UPATH（设置N4U路径相关属性）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UPN4UPATH
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 路径管理
- GTP路径管理
- GTP协议参数管理
- N4U路径全局参数
status: active
---

# SET UPN4UPATH（设置N4U路径相关属性）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](设置N4U路径相关属性（SET UPN4UPATH）_18761567.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，配置UPF主动向SMF发送GTP请求消息的重发时间间隔和最大尝试发送次数，如果配置不合理，可能导致用户激活失败或资源残留。

该命令用来设置N4U路径的Echo探测属性。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- N4ECHOSW设置为使能ENABLE时，参数N4ECHOTIME、N4ECHOINTERVAL、DEACTIVEFLAG、N4T3RESPONSE、N4N3REQUEST才能生效。
- 在基站数目较多时，建议配置较大ECHOINTERVAL，防止单位时间内发送太多ECHO消息导致系统CPU上升影响基本业务。
- 如果基站数目较多但配置ECHOINTERVAL较小，会自动调整ECHOINTERVAL为180s来控制ECHO发送。
- 如果配置路径断告警产生后不去激活该路径上已激活的上下文，可能导致资源残留。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | N4ECHOINTERVAL | N4T3RESPONSE | N4N3REQUEST | DEACTIVEFLAG | N4ECHOTIME | N4ECHOSW |
| --- | --- | --- | --- | --- | --- | --- |
| 初始值 | 60 | 3 | 5 | ENABLE | 0 | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| N4ECHOINTERVAL | N4接口发送GTP心跳请求的间隔时间 | 可选必选说明：可选参数<br>参数含义：设置发送N4接口GTP心跳请求的间隔时间。该参数在设置之后在下个心跳周期开始生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为60～3600，单位是秒。<br>默认值：无<br>配置原则：无 |
| N4T3RESPONSE | N4接口的GTP请求消息的重发时间间隔 | 可选必选说明：可选参数<br>参数含义：N4 GTP请求消息的重发时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20，单位是秒。<br>默认值：无<br>配置原则：无 |
| N4N3REQUEST | N4接口的GTP请求消息的最大尝试发送次数 | 可选必选说明：可选参数<br>参数含义：N4 GTP请求消息的最大尝试发送次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～6。<br>默认值：无<br>配置原则：无 |
| DEACTIVEFLAG | 是否去活路径上已激活的上下文 | 可选必选说明：可选参数<br>参数含义：用于配置路径断告警产生后是否去激活该路径上已激活的上下文。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：<br>- ENABLE：配置路径断告警产生后去激活该路径上已激活的上下文。<br>- DISABLE：配置路径断告警产生后不去激活该路径上已激活的上下文。 |
| N4ECHOTIME | N4接口的GTP-U路径断告警后发送echo消息的次数 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DEACTIVEFLAG”配置为“ENABLE”时为必选参数。<br>参数含义：指定在N4接口的GTP-U路径断告警产生后发送心跳消息的次数，之后执行去激活操作。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～60。<br>默认值：无<br>配置原则：当DEACTIVEFLAG参数设置为ENABLE时，该参数为必选参数。 |
| N4ECHOSW | Echo开关 | 可选必选说明：可选参数<br>参数含义：设置系统是否主动发送N4接口的v1版本数据路径Echo消息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [N4U路径相关属性（UPN4UPATH）](configobject/UDG/20.15.2/UPN4UPATH.md)

## 关联任务

- [0-00052](task/UDG/20.15.2/0-00052.md)

## 使用实例

设置系统主动发送N4U数据路径Echo消息：

```
SET UPN4UPATH:N4ECHOSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置N4U路径相关属性（SET-UPN4UPATH）_18761567.md`
