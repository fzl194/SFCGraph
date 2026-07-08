---
id: UDG@20.15.2@MMLCommand@SET APNNONIPFUNC
type: MMLCommand
name: SET APNNONIPFUNC（设置APN Non-IP配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNNONIPFUNC
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- M2M管理
- APN的Non-IP配置
status: active
---

# SET APNNONIPFUNC（设置APN Non-IP配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

此命令用于开启或关闭指定APN的网关Non-IP功能。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条APNNonIpFunc。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | NONIPSWITCH | USERPORT |
| --- | --- | --- |
| 初始值 | DISABLE | 5683 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| NONIPSWITCH | APN Non-IP功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于基于APN控制开启和关闭Non-IP功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：<br>- ENABLE：开启基于APN控制Non-IP的功能。<br>- DISABLE：关闭基于APN控制Non-IP的功能。 |
| USERPORT | 用户端口号 | 可选必选说明：可选参数<br>参数含义：指定用户的端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN Non-IP功能配置（APNNONIPFUNC）](configobject/UDG/20.15.2/APNNONIPFUNC.md)

## 关联任务

- [0-00177](task/UDG/20.15.2/0-00177.md)

## 使用实例

使能apn apn1.com的Non-IP功能：

```
SET APNNONIPFUNC:APN="apn1.com",NONIPSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置APN-Non-IP配置（SET-APNNONIPFUNC）_15595100.md`
