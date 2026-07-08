---
id: UDG@20.15.2@MMLCommand@SET RPTRATELT
type: MMLCommand
name: SET RPTRATELT（设置报表消息流控配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: RPTRATELT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务报表管理
- 报表功能管理
- 报表速率控制
status: active
---

# SET RPTRATELT（设置报表消息流控配置）

## 功能

**适用NF：PGW-U、UPF**

此命令用于设置报表消息流控参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | USRRESENDPERIOD | USRRESENDRATE | SIGUFDRRATELT | SSGUSRRSDSW | SSGUSRRSDPERIOD |
| --- | --- | --- | --- | --- | --- |
| 初始值 | 0 | 100 | 300 | DISABLE | 36000 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRRESENDPERIOD | 用户信息定时重发间隔 | 可选必选说明：可选参数<br>参数含义：该参数用于设置RPT主动触发用户信息定时重发间隔，取值为0表示不启动定时重发功能。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1440，单位是秒。<br>默认值：无<br>配置原则：无 |
| USRRESENDRATE | 用户信息重发请求消息流控门限 | 可选必选说明：可选参数<br>参数含义：该参数用于设置用户信息重发请求消息流控门限，取值为0表示不支持用户信息重发请求。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～9999999，单位是个/秒。<br>默认值：无<br>配置原则：无 |
| SIGUFDRRATELT | 触发UFDR Stats的用户更新消息流控门限 | 可选必选说明：可选参数<br>参数含义：该参数用于设置触发UFDR Stats的用户更新消息流控门限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～9999999，单位是个/秒。<br>默认值：无<br>配置原则：无 |
| SSGUSRRSDSW | SSG主动定时重发用户信息功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否使能SSG主动定时重发用户信息的功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能SSG主动定时重发用户信息功能。<br>- ENABLE：使能SSG主动定时重发用户信息功能。<br>默认值：无<br>配置原则：无 |
| SSGUSRRSDPERIOD | SSG主动定时重发用户信息时间间隔 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SSGUSRRSDSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置SSG主动触发用户信息定时重发的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为300～86400，单位是秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [业务报表消息流控配置（RPTRATELT）](configobject/UDG/20.15.2/RPTRATELT.md)

## 使用实例

设置报表消息流控参数：

```
SET RPTRATELT: USRRESENDPERIOD=10, USRRESENDRATE=100;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置报表消息流控配置（SET-RPTRATELT）_06453264.md`
