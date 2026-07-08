---
id: UNC@20.15.2@MMLCommand@SET SMFAPNSOFTPARA
type: MMLCommand
name: SET SMFAPNSOFTPARA（设置SMF的APN软参记录）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMFAPNSOFTPARA
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 软件参数管理
status: active
---

# SET SMFAPNSOFTPARA（设置SMF的APN软参记录）

## 功能

**适用NF：SMF**

该命令用于设置APN下软件参数。

## 注意事项

- 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无。<br>配置原则：无 |
| DT | 软参记录数据类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN下软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：<br>- Dw（双字）<br>- Bit（比特）<br>- Byte（字节）<br>- String（字符串）<br>默认值：无。<br>配置原则：<br>配置BIT表示需要设置比特类型软件参数。<br>配置BYTE表示需要设置字节类型软件参数。<br>配置STRING表示需要设置字符串类型软件参数。 |
| BITNUM | Bit索引 | 可选必选说明：该参数在"DT"配置为"Bit"时为条件必选参数。<br>参数含义：该参数用于指定比特类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~64。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFAPNSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| BYTENUM | Byte索引 | 可选必选说明：该参数在"DT"配置为"Byte"时为条件必选参数。<br>参数含义：该参数用于指定字节类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~16。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFAPNSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| STRINGNUM | String索引 | 可选必选说明：该参数在"DT"配置为"String"时为条件必选参数。<br>参数含义：该参数用于指定字符串类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~10。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFAPNSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| DWORDNUM | Dword索引 | 可选必选说明：该参数在"DT"配置为"Dw"时为条件必选参数。<br>参数含义：该参数表示Dword类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~16。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFAPNSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| BITVALUE | Bit值 | 可选必选说明：该参数在"DT"配置为"Bit"时为条件必选参数。<br>参数含义：该参数用于指定比特类型参数的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFAPNSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| BYTEVALUE | Byte值 | 可选必选说明：该参数在"DT"配置为"Byte"时为条件必选参数。<br>参数含义：该参数用于指定字节类型参数的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFAPNSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| STRINGVALUE | String值 | 可选必选说明：该参数在"DT"配置为"String"时为条件必选参数。<br>参数含义：该参数用于指定字符串类型参数的值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~432。当前版本支持的输入长度为1~31。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFAPNSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| DWORDVALUE | Dword值 | 可选必选说明：该参数在"DT"配置为"Dw"时为条件必选参数。<br>参数含义：该参数表示Dword类型软件参数的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFAPNSOFTPARA查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [SMF APN软参记录（SMFAPNSOFTPARA）](configobject/UNC/20.15.2/SMFAPNSOFTPARA.md)

## 使用实例

当需要设置APN下软参，参数的为字节类型，参数索引为8，参数取值为3，可以使用该命令：

```
SET SMFAPNSOFTPARA: APN="huawei.com", DT=Byte, BYTENUM=8, BYTEVALUE=3;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SMF的APN软参记录（SET-SMFAPNSOFTPARA）_25121213.md`
