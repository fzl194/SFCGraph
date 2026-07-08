---
id: UDG@20.15.2@MMLCommand@SET APNSOFTPARA
type: MMLCommand
name: SET APNSOFTPARA（配置APN软参记录）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNSOFTPARA
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 70000
category_path:
- 用户面服务管理
- DN管理
- APN管理
- APN软参配置数据管理
status: active
---

# SET APNSOFTPARA（配置APN软参记录）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置APN下软件参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为70000。
- bit类型软参最大记录数为40000，byte类型最大记录数为20000，string类型最大记录数为10000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DT | 软参记录数据类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN下软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BIT：比特。<br>- BYTE：字节。<br>- STRING：字符串。<br>默认值：无<br>配置原则：<br>- 配置BIT表示需要设置比特类型软件参数。<br>- 配置BYTE表示需要设置字节类型软件参数。<br>- 配置STRING表示需要设置字符串类型软件参数。 |
| BITNUM | Bit索引 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DT”配置为“BIT”时为必选参数。<br>参数含义：该参数用于指定比特类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～64。<br>默认值：无<br>配置原则：无 |
| BYTENUM | Byte索引 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DT”配置为“BYTE”时为必选参数。<br>参数含义：该参数用于指定字节类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～16。<br>默认值：无<br>配置原则：无 |
| STRINGNUM | String索引 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DT”配置为“STRING”时为必选参数。<br>参数含义：该参数用于指定字符串类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～5。<br>默认值：无<br>配置原则：无 |
| BITVALUE | Bit值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DT”配置为“BIT”时为必选参数。<br>参数含义：该参数用于指定比特类型参数的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1。<br>默认值：无<br>配置原则：无 |
| BYTEVALUE | Byte值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DT”配置为“BYTE”时为必选参数。<br>参数含义：该参数用于指定字节类型参数的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无<br>配置原则：无 |
| STRINGVALUE | String值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DT”配置为“STRING”时为必选参数。<br>参数含义：该参数用于指定字符串类型参数的值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNSOFTPARA]] · APN软参记录（APNSOFTPARA）

## 使用实例

当需要设置APN下软参，参数的为字节类型，参数索引为8，参数取值为3，可以使用该命令：

```
SET APNSOFTPARA:APN="huawei.com",DT=BYTE,BYTENUM=8,BYTEVALUE=3;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/配置APN软参记录（SET-APNSOFTPARA）_82837027.md`
