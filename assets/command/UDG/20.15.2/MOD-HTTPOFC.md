---
id: UDG@20.15.2@MMLCommand@MOD HTTPOFC
type: MMLCommand
name: MOD HTTPOFC（修改HTTP局向）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: HTTPOFC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP局向管理
status: active
---

# MOD HTTPOFC（修改HTTP局向）

## 功能

该命令用于修改HTTP局向。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFCIDX | 局向索引 | 可选必选说明：必选参数<br>参数含义：该参数用于设置局向索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：无 |
| OFCTYPE | 局向类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置局向类型。<br>数据来源：本端规划<br>取值范围：<br>- “NFTYPE（基于网元类型）”：基于网元类型<br>- “IPGROUP（基于IP组）”：基于IP组<br>默认值：无<br>配置原则：<br>该参数不支持修改。 |
| NFITEM | 基于NFTYPE控制项 | 可选必选说明：该参数在"OFCTYPE"配置为"NFTYPE"时为条件可选参数。<br>参数含义：该参数用于设置局向类型为"NFTYPE"时流控类型。<br>数据来源：本端规划<br>取值范围：<br>- “HTRINTF（HTRINTF）”：基于接口类型HTR流控<br>- “FIXSPDFCINTF（FIXSPDFCINTF）”：基于接口类型固定速率流控<br>默认值：无<br>配置原则：<br>该参数支持单独勾选和全选，其中基于接口类型HTR流控和基于接口类型固定速率流控要生效，需要满足对应的生效条件。 |
| IPGRPITEM | 基于IP组控制项 | 可选必选说明：该参数在"OFCTYPE"配置为"IPGROUP"时为条件可选参数。<br>参数含义：该参数用于设置局向类型为"IPGROUP"时流控类型。<br>数据来源：本端规划<br>取值范围：<br>- “HTRIPGRP（HTRIPGRP）”：基于IP组HTR流控<br>默认值：无<br>配置原则：无 |
| OFCNAME | 局向名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置局向名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [HTTP局向（HTTPOFC）](configobject/UDG/20.15.2/HTTPOFC.md)

## 使用实例

- 修改接口类型HTTP局向配置，可以用如下命令：
  ```
  MOD HTTPOFC: OFCIDX=1, OFCTYPE = NFTYPE, OFCNAME = "N12";
  ```
- 修改IP组类型HTTP局向配置，可以用如下命令：
  ```
  MOD HTTPOFC: OFCIDX=2, OFCTYPE = IPGROUP, OFCNAME = "AMF2UDMIPGRP";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改HTTP局向（MOD-HTTPOFC）_86030329.md`
