---
id: UDG@20.15.2@MMLCommand@SET FWSOFTPARA
type: MMLCommand
name: SET FWSOFTPARA（设置ServiceFabric软参）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: FWSOFTPARA
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 软参配置管理
status: active
---

# SET FWSOFTPARA（设置ServiceFabric软参）

## 功能

该命令用于设置ServiceFabric软件参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 软参索引取值区间：1-2048。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARAMETERSTYPE | 参数类型 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数的类型。<br>数据来源：本端规划<br>取值范围：<br>- DWORD（双字）<br>- DWORD_EX（扩展双字）<br>默认值：无。<br>配置原则：无 |
| DWORDINDEX | DWORD索引 | 可选必选说明：该参数在"PARAMETERSTYPE"配置为"DWORD"时为条件必选参数。<br>参数含义：该参数表示Dword类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~2048。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST FWSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| DWORDVALUE | DWORD取值 | 可选必选说明：该参数在"PARAMETERSTYPE"配置为"DWORD"时为条件必选参数。<br>参数含义：该参数表示Dword类型软件参数的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST FWSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| EXTENDDWORDINDEX | 扩展DWORD索引 | 可选必选说明：该参数在"PARAMETERSTYPE"配置为"DWORD_EX"时为条件必选参数。<br>参数含义：该参数表示Dword extend类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~2048。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST FWSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| EXTENDDWORDVALUE | 扩展DWORD取值 | 可选必选说明：该参数在"PARAMETERSTYPE"配置为"DWORD_EX"时为条件必选参数。<br>参数含义：该参数表示Dword extend类型软件参数的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST FWSOFTPARA查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FWSOFTPARA]] · ServiceFabric软参（FWSOFTPARA）

## 使用实例

设置软参值

```
SET FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=20, DWORDVALUE=20;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-FWSOFTPARA.md`
