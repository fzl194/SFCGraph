---
id: UNC@20.15.2@MMLCommand@MOD FAULTRANGRP
type: MMLCommand
name: MOD FAULTRANGRP（修改N3接口故障RAN组）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: FAULTRANGRP
command_category: 配置类
applicable_nf:
- SGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP故障管理
- N3接口故障RAN组管理
status: active
---

# MOD FAULTRANGRP（修改N3接口故障RAN组）

## 功能

**适用NF：SGW-C、SMF**

该命令用于修改N3接口故障RAN组的故障处理配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGRPNAME | RAN组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RAN组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头或结尾，不区分大小写。<br>默认值：无<br>配置原则：无 |
| UPFAULTMODE | UP链路故障处理模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UP链路故障处理模式。<br>数据来源：本端规划<br>取值范围：<br>- “ISOLATION（直接隔离）”：直接隔离故障的基站和UPF之间的链路。<br>- “DETECTION（检测到故障后隔离）”：检测到故障后隔离基站和UPF之间的链路。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FAULTRANGRP]] · N3接口故障RAN组（FAULTRANGRP）

## 使用实例

修改已有N3接口故障RAN组为检测后隔离，组名为"group2"：

```
MOD FAULTRANGRP: RANGRPNAME="group2", UPFAULTMODE=DETECTION;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改N3接口故障RAN组（MOD-FAULTRANGRP）_52628648.md`
