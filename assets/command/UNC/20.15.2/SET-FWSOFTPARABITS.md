---
id: UNC@20.15.2@MMLCommand@SET FWSOFTPARABITS
type: MMLCommand
name: SET FWSOFTPARABITS（设置软件参数比特位）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: FWSOFTPARABITS
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 软参配置管理
status: active
---

# SET FWSOFTPARABITS（设置软件参数比特位）

## 功能

该命令用于设置ServiceFabric软件参数。

## 注意事项

- 该命令执行后立即生效。

- 软参索引取值区间：1-2048。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARATYPE | 数据类型 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：<br>- DWORD（双字）<br>- DWORD_EX（扩展双字）<br>默认值：无。<br>配置原则：无 |
| DWORDNUM | DWORD参数索引 | 可选必选说明：该参数在"PARATYPE"配置为"DWORD"、"DWORD_EX"时为条件必选参数。<br>参数含义：该参数表示Common Dword类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~2048。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST FWSOFTPARABITS查询当前参数配置值。<br>配置原则：无 |
| VALUE | 软参记录值 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数的值。<br>数据来源：本端规划<br>取值范围：<br>- VALUE_0（0）<br>- VALUE_1（1）<br>默认值：无。<br>配置原则：无 |
| POSITION | 比特位 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数比特位的位置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~32。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [ServiceFabric软参比特位（FWSOFTPARABITS）](configobject/UNC/20.15.2/FWSOFTPARABITS.md)

## 使用实例

设置双字类型1号软参Bit1值为0:

```
SET FWSOFTPARABITS: PARATYPE=DWORD, DWORDNUM=1, VALUE=VALUE_0, POSITION=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置软件参数比特位（SET-FWSOFTPARABITS）_37580503.md`
