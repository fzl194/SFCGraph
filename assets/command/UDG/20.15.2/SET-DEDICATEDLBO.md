---
id: UDG@20.15.2@MMLCommand@SET DEDICATEDLBO
type: MMLCommand
name: SET DEDICATEDLBO（设置系统是否开启专网UPF动态分流功能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: DEDICATEDLBO
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 动态分流业务控制
- 动态分流功能接入控制
status: active
---

# SET DEDICATEDLBO（设置系统是否开启专网UPF动态分流功能）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来设置系统是否开启专网UPF动态分流功能。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ULCLSWITCH |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ULCLSWITCH | 专网UPF动态分流功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定系统是否开启专网UPF动态分流功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DEDICATEDLBO]] · 系统是否开启专网UPF动态分流功能（DEDICATEDLBO）

## 使用实例

设置系统开启专网UPF动态分流功能，可以使用该命令设置：

```
SET DEDICATEDLBO: ULCLSWITCH= ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置系统是否开启专网UPF动态分流功能（SET-DEDICATEDLBO）_49785469.md`
