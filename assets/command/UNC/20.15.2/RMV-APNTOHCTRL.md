---
id: UNC@20.15.2@MMLCommand@RMV APNTOHCTRL
type: MMLCommand
name: RMV APNTOHCTRL（删除APN粒度的智家随行会话控制）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNTOHCTRL
command_category: 配置类
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 智家随行会话管理
status: active
---

# RMV APNTOHCTRL（删除APN粒度的智家随行会话控制）

## 功能

该命令用于删除APN粒度的智家随行会话控制。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定智家随行会话的APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNTOHCTRL]] · APN粒度的智家随行会话控制（APNTOHCTRL）

## 使用实例

删除APN粒度的智家随行会话控制，APN名称为“toh.apn”。

```
RMV APNTOHCTRL: APN="toh.apn";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APN粒度的智家随行会话控制（RMV-APNTOHCTRL）_21861985.md`
