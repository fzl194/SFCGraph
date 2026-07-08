---
id: UDG@20.15.2@MMLCommand@SET APNDLBUFTIME
type: MMLCommand
name: SET APNDLBUFTIME（设置基于APN的下行数据缓存时长）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNDLBUFTIME
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- GTP隧道管理
- APN的下行数据缓存时长
status: active
---

# SET APNDLBUFTIME（设置基于APN的下行数据缓存时长）

## 功能

**适用NF：UPF**

此命令用来配置APN下的普通用户下行报文缓存时长。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条ApnDLBufTime。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | NORMALUSER | NBIoTUser | REDCAPNRUSER |
| --- | --- | --- | --- |
| 初始值 | 6 | 6 | 6 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| NORMALUSER | 普通用户下行数据缓存时长 | 可选必选说明：可选参数<br>参数含义：APN下的普通用户下行报文缓存时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～15，单位是秒。<br>默认值：无<br>配置原则：无 |
| NBIOTUSER | NB-IoT用户下行数据缓存时长 | 可选必选说明：可选参数<br>参数含义：APN下的NB-IoT用户下行报文缓存时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～200，单位是秒。<br>默认值：无<br>配置原则：无 |
| REDCAPNRUSER | RedCap-NR用户下行数据缓存时长 | 可选必选说明：可选参数<br>参数含义：APN下的RedCap-NR用户下行报文缓存时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～200，单位是秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNDLBUFTIME]] · APN的下行数据缓存时长配置（APNDLBUFTIME）

## 关联任务

- [[UDG@20.15.2@Task@0-00174]]

## 使用实例

配置APN apn1.com下的普通用户下行报文缓存时长：

```
SET APNDLBUFTIME: APN="apn1.com", NORMALUSER=9;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-APNDLBUFTIME.md`
