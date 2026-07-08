---
id: UDG@20.15.2@MMLCommand@ADD USERSTATISTICS
type: MMLCommand
name: ADD USERSTATISTICS（增加用户信息统计功能）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: USERSTATISTICS
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
max_records: 1
category_path:
- 业务报表管理
- 用户信息统计管理
- 用户信息统计功能
status: active
---

# ADD USERSTATISTICS（增加用户信息统计功能）

## 功能

**适用NF：PGW-U、UPF**

该命令用于添加用户信息统计功能。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为1。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FUNCTION | 功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置功能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- HIGH_RATE_USRSTATS：高带宽用户统计功能。<br>默认值：无<br>配置原则：无 |
| RECORDMODE | 业务信息记录方式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“FUNCTION”配置为“HIGH_RATE_USRSTATS”时为可选参数。<br>参数含义：该参数用于配置业务信息的记录方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DGBCNT：调试计数器。<br>- HIGH_USR_LEARN：高带宽用户自学习。<br>- DGBCNT_AND_HIGH_USR_LEARN：调试计数器&高带宽用户自学习。<br>默认值：DGBCNT<br>配置原则：无 |
| CALCPERIOD | 用户瞬间速率的计算周期 | 可选必选说明：条件可选参数<br>前提条件：该参数在“FUNCTION”配置为“HIGH_RATE_USRSTATS”时为可选参数。<br>参数含义：该参数用于配置用户瞬间速率的计算周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为100～5000，单位是毫秒。<br>默认值：1000<br>配置原则：无 |
| HBUSERTHRESHOLD | 高带宽用户速率门限（兆比特/秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDMODE”配置为“HIGH_USR_LEARN” 或 “DGBCNT_AND_HIGH_USR_LEARN”时为可选参数。<br>参数含义：该参数用于配置识别高带宽用户的最低速率门限值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为100～5000，单位是兆比特每秒。<br>默认值：600<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@USERSTATISTICS]] · 用户信息统计功能（USERSTATISTICS）

## 使用实例

添加高带宽用户统计功能，业务信息记录方式为DBGCNT，瞬间速率计算周期为1000毫秒：

```
ADD USERSTATISTICS: FUNCTION=HIGH_RATE_USRSTATS, RECORDMODE=DGBCNT, CALCPERIOD=1000;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-USERSTATISTICS.md`
