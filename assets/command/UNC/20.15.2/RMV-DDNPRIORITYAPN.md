---
id: UNC@20.15.2@MMLCommand@RMV DDNPRIORITYAPN
type: MMLCommand
name: RMV DDNPRIORITYAPN（删除基于APN的DDN消息优先级配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DDNPRIORITYAPN
command_category: 配置类
applicable_nf:
- SGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- 基于APN的DDN消息优先级管理
status: active
---

# RMV DDNPRIORITYAPN（删除基于APN的DDN消息优先级配置）

## 功能

**适用NF：SGW-C、SMF**

该命令用于删除基于APN的DDN消息优先级配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DDNPRIORITYAPN]] · 基于APN的DDN消息优先级配置（DDNPRIORITYAPN）

## 使用实例

删除APN为IMS的DDN消息优先级：

```
RMV DDNPRIORITYAPN: APN="IMS";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DDNPRIORITYAPN.md`
