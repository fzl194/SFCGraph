---
id: UNC@20.15.2@MMLCommand@SET COMMONSOFTPARAOFBIT
type: MMLCommand
name: SET COMMONSOFTPARAOFBIT（设置公共软件参数比特位）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: COMMONSOFTPARAOFBIT
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 软件参数管理
status: active
---

# SET COMMONSOFTPARAOFBIT（设置公共软件参数比特位）

## 功能

该命令用于设置公共软件参数的比特位。

## 注意事项

- 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DT | 数据类型 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：<br>- “DwCom（公共双字）”：公共双字<br>默认值：无。<br>配置原则：无 |
| DWORDCOMNUM | Common Dword索引 | 可选必选说明：该参数在"DT"配置为"DwCom"时为条件必选参数。<br>参数含义：该参数表示Common Dword类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1500。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST COMMONSOFTPARAOFBIT查询当前参数配置值。<br>配置原则：无 |
| VALUE | 软参记录值 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数的值。<br>数据来源：本端规划<br>取值范围：<br>- VALUE_0（0）<br>- VALUE_1（1）<br>默认值：无。<br>配置原则：无 |
| POSITION | 比特位 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数比特位的位置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~32。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/COMMONSOFTPARAOFBIT]] · 公共软件参数比特位（COMMONSOFTPARAOFBIT）

## 使用实例

设置公共双字类型1号软参Bit1值为0:

```
SET COMMONSOFTPARAOFBIT: DT=DwCom, DWORDCOMNUM=1, VALUE=VALUE_0, POSITION=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置公共软件参数比特位（SET-COMMONSOFTPARAOFBIT）_26494601.md`
