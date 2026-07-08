---
id: UNC@20.15.2@MMLCommand@RMV MULDNNULCLMODE
type: MMLCommand
name: RMV MULDNNULCLMODE（删除智能分流ULCL部署模式）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MULDNNULCLMODE
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 智能分流专网DNN管理
status: active
---

# RMV MULDNNULCLMODE（删除智能分流ULCL部署模式）

## 功能

**适用NF：SMF**

该命令用于删除指定智能分流专网DNN的ULCL部署模式。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEDDNN | 智能分流专网DNN | 可选必选说明：必选参数<br>参数含义：该参数指定智能分流专网DNN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MULDNNULCLMODE]] · 智能分流ULCL部署模式（MULDNNULCLMODE）

## 使用实例

删除指定智能分流专网DNN的ULCL部署模式，智能分流专网DNN为“special.dnn”。

```
RMV MULDNNULCLMODE: DEDDNN="special.dnn";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MULDNNULCLMODE.md`
