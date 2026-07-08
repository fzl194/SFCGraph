---
id: UDG@20.15.2@MMLCommand@SET IPALLOCBYSMFGLBSW
type: MMLCommand
name: SET IPALLOCBYSMFGLBSW（设置基于SMF分配地址全局开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: IPALLOCBYSMFGLBSW
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
- 会话地址管理
- 基于SMF分配地址开关
status: active
---

# SET IPALLOCBYSMFGLBSW（设置基于SMF分配地址全局开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置基于SMF分配地址全局开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH | IPV6SWITCH |
| --- | --- | --- |
| 初始值 | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | IPv4 开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于SMF分配地址的IPv4开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| IPV6SWITCH | IPv6 开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于SMF分配地址的IPv6开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [基于SMF分配地址的全局开关（IPALLOCBYSMFGLBSW）](configobject/UDG/20.15.2/IPALLOCBYSMFGLBSW.md)

## 使用实例

将基于SMF分配地址全局开关设置为允许基于SMF分配：

```
SET IPALLOCBYSMFGLBSW: SWITCH=ENABLE, IPV6SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置基于SMF分配地址全局开关（SET-IPALLOCBYSMFGLBSW）_82837157.md`
