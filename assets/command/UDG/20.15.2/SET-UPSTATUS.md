---
id: UDG@20.15.2@MMLCommand@SET UPSTATUS
type: MMLCommand
name: SET UPSTATUS（设置UP 状态信息）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UPSTATUS
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- UP信息管理
- UP状态
status: active
---

# SET UPSTATUS（设置UP 状态信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置UPF工作状态。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 在使用本命令触发系统进行系统停工上报前，需要确保Sx（包括Sxa/Sxb）和N4链路状态正常。
- 在系统存在用户的情况下，执行该命令会失败。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | STATUS | FORCE |
| --- | --- | --- |
| 初始值 | UP | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATUS | UP状态 | 可选必选说明：必选参数<br>参数含义：UPF状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- UP：表示系统状态UP。<br>- DOWN：表示系统状态down。<br>默认值：无<br>配置原则：如果参数设置为UP，会触发系统进行系统开工流程的上报。如果参数设置为DOWN，会触发系统进行系统停工流程的上报。系统停工完成后，新用户无法在本系统上激活。 |
| FORCE | 强制停工开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“STATUS”配置为“DOWN”时为可选参数。<br>参数含义：该参数用于配置是否强制停工。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UP 状态（UPSTATUS）](configobject/UDG/20.15.2/UPSTATUS.md)

## 使用实例

配置UPF工作状态为UP：

```
SET UPSTATUS: STATUS=UP;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置UP-状态信息（SET-UPSTATUS）_82837250.md`
