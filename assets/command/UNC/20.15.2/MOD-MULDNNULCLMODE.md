---
id: UNC@20.15.2@MMLCommand@MOD MULDNNULCLMODE
type: MMLCommand
name: MOD MULDNNULCLMODE（修改智能分流ULCL部署模式）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD MULDNNULCLMODE（修改智能分流ULCL部署模式）

## 功能

**适用NF：SMF**

该命令用于修改指定智能分流专网DNN的ULCL部署模式。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEDDNN | 智能分流专网DNN | 可选必选说明：必选参数<br>参数含义：该参数指定智能分流专网DNN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| ULCLDEPLOYMODE | ULCL部署模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ULCL部署模式。<br>数据来源：本端规划<br>取值范围：<br>- “PSASHUNTMUST（只使用主锚点分流）”：只使用主锚点分流。<br>- “AREADEDUPFPREFER（指定区域优先使用专网UPF分流）”：指定区域优先专网UPF分流。如果没有专网UPF，则使用大网会话主锚点分流。如果园区ULCL也具备对接公网的能力，SMF也优先选择这类UPF，选不到的情况下会尝试选择同时具备对接园区内网能力的ULCL。<br>默认值：无<br>配置原则：<br>如果要求当企业园区用户在所在园区接入时用户数据减少迂回和不出园区，可配置为AREADEDUPFPREFER，否则配置为PSASHUNTMUST。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MULDNNULCLMODE]] · 智能分流ULCL部署模式（MULDNNULCLMODE）

## 使用实例

修改指定智能分流专网DNN的ULCL部署模式，智能分流专网DNN为“special.dnn”，ULCL部署模式为“只使用主锚点分流”，修改为“指定区域优先专网UPF分流”。

```
MOD MULDNNULCLMODE: DEDDNN="special.dnn",ULCLDEPLOYMODE=AREADEDUPFPREFER;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-MULDNNULCLMODE.md`
