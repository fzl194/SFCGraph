---
id: UDG@20.15.2@MMLCommand@RMV CHRRPTAPN
type: MMLCommand
name: RMV CHRRPTAPN（删除指定某个APN做本地存储CHR表单的策略）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CHRRPTAPN
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 呼叫日志管理
- 基于APN的CHR本地存盘配置
status: active
---

# RMV CHRRPTAPN（删除指定某个APN做本地存储CHR表单的策略）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除指定某个APN做本地存储CHR表单的策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：输入的APN名称必须是ADD APN已配置的APN名称。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CHRRPTAPN]] · 指定某个APN做本地存储CHR表单的策略（CHRRPTAPN）

## 使用实例

删除APN为apn1.com下做本地存储CHR表单的策略：

```
RMV CHRRPTAPN:APN="apn1.com";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除指定某个APN做本地存储CHR表单的策略（RMV-CHRRPTAPN）_52120359.md`
