---
id: UDG@20.15.2@MMLCommand@RMV PRINETPOLICY
type: MMLCommand
name: RMV PRINETPOLICY（删除专网控制策略）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PRINETPOLICY
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 专网策略配置
- 专网控制策略
status: active
---

# RMV PRINETPOLICY（删除专网控制策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用来删除专网控制策略。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 如果只输入APN，则会删除该APN下所有的专网控制策略。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DNAI | 数据网络接入标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定数据网络接入标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。名称中不能包含空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PRINETPOLICY]] · 专网控制策略（PRINETPOLICY）

## 使用实例

删除一条专网控制策略：

```
RMV PRINETPOLICY: APN="test1", DNAI="123456";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除专网控制策略（RMV-PRINETPOLICY）_19641394.md`
