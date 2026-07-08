---
id: UDG@20.15.2@MMLCommand@SET USRREALLOCNTY
type: MMLCommand
name: SET USRREALLOCNTY（设置主动触发用户位置实时通知功能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: USRREALLOCNTY
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- 位置实时通知
status: active
---

# SET USRREALLOCNTY（设置主动触发用户位置实时通知功能）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置主动触发用户位置实时通知功能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH | USRSAMPLINGRATE |
| --- | --- | --- |
| 初始值 | DISABLE | 10 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 主动触发用户位置实时通知功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置主动触发用户位置实时通知功能是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能主动触发用户位置实时通知功能。<br>- ENABLE：使能主动触发用户位置实时通知功能。<br>默认值：无<br>配置原则：无 |
| USRSAMPLINGRATE | 用户抽样比 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置用户抽样比。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100，单位是百分比。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/USRREALLOCNTY]] · 主动触发用户位置实时通知功能（USRREALLOCNTY）

## 使用实例

设置主动触发用户位置实时通知功能使能：

```
SET USRREALLOCNTY: SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-USRREALLOCNTY.md`
