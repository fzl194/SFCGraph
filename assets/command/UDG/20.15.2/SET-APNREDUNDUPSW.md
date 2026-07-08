---
id: UDG@20.15.2@MMLCommand@SET APNREDUNDUPSW
type: MMLCommand
name: SET APNREDUNDUPSW（配置APN路由冗余上行报文隧道转发功能开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNREDUNDUPSW
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 静态地址用户路由冗余
- APN静态路由冗余上行报文隧道转发功能配置
status: active
---

# SET APNREDUNDUPSW（配置APN路由冗余上行报文隧道转发功能开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置APN路由冗余上行报文隧道转发功能开关。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条。
- 该命令只能在备UPF才能配置。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | IPV4SWITCH | IPV6SWITCH |
| --- | --- | --- |
| 初始值 | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPV4SWITCH | APN支持IPV4上行转发功能 | 可选必选说明：可选参数<br>参数含义：配置指定APN是否支持IPv4上行报文隧道转发功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| IPV6SWITCH | APN支持IPV6上行转发功能 | 可选必选说明：可选参数<br>参数含义：配置指定APN是否支持IPv6上行报文隧道转发功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNREDUNDUPSW]] · 指定APN静态地址路由冗余上行报文隧道转发功能开关（APNREDUNDUPSW）

## 使用实例

假设用户需要APN “huawei.com”支持路由冗余上行隧道转发功能时，使用该命令配置：

```
SET APNREDUNDUPSW: APN="huawei.com", IPV4SWITCH=ENABLE, IPV6SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/配置APN路由冗余上行报文隧道转发功能开关（SET-APNREDUNDUPSW）_75097449.md`
