---
id: UNC@20.15.2@MMLCommand@SET NCGSOFTPARA
type: MMLCommand
name: SET NCGSOFTPARA（设置NCG软参）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NCGSOFTPARA
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 软件参数管理
status: active
---

# SET NCGSOFTPARA（设置NCG软参）

## 功能

**适用NF：NCG**

该命令用于设置NCG的软件参数信息。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

> **说明**
> 此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| DT | DWORDNUM | DWORDVALUE | BITNUM | BITVALUE | BYTENUM | BYTEVALUE | STRINGNUM | STRINGVALUE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dw | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| Dw | 2 | 0 | 2 | 0 | 2 | 0 | 2 | 0 |
| Dw | 3 | 0 | 3 | 0 | 3 | 0 | 3 | 0 |
| Dw | 4 | 0 | 4 | 0 | 4 | 0 | 4 | 0 |
| Dw | 5 | 0 | 5 | 0 | 5 | 0 | 5 | 0 |
| Dw | 6 | 0 | 6 | 0 | 6 | 0 | 6 | 0 |
| Dw | 7 | 0 | 7 | 0 | 7 | 0 | 7 | 0 |
| Dw | 8 | 0 | 8 | 0 | 8 | 0 | 8 | 0 |
| Dw | 9 | 0 | 9 | 0 | 9 | 0 | 9 | 0 |
| Dw | 10 | 0 | 10 | 0 | 10 | 0 | 10 | 0 |
| Dw | 11 | 0 | 11 | 0 | 11 | 0 | 11 | 0 |
| Dw | 12 | 0 | 12 | 0 | 12 | 0 | 12 | 0 |
| Dw | 13 | 0 | 13 | 0 | 13 | 0 | 13 | 0 |
| Dw | 14 | 0 | 14 | 0 | 14 | 0 | 14 | 0 |
| Dw | 15 | 0 | 15 | 0 | 15 | 0 | 15 | 0 |
| Dw | 16 | 0 | 16 | 0 | 16 | 0 | 16 | 0 |
| Dw | 17 | 0 | 17 | 0 | 17 | 0 | 17 | 0 |
| Dw | 18 | 0 | 18 | 0 | 18 | 0 | 18 | 0 |
| Dw | 19 | 0 | 19 | 0 | 19 | 0 | 19 | 0 |
| Dw | 20 | 0 | 20 | 0 | 20 | 0 | 20 | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DT | 数据类型 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：<br>- Dw（双字）<br>- Bit（比特）<br>- Byte（字节）<br>- String（字符串）<br>默认值：无。<br>配置原则：无 |
| DWORDNUM | Dword索引 | 可选必选说明：该参数在"DT"配置为"Dw"时为条件必选参数。<br>参数含义：该参数表示Dword类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1500。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NCGSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| DWORDVALUE | Dword值 | 可选必选说明：该参数在"DT"配置为"Dw"时为条件必选参数。<br>参数含义：该参数表示Dword类型软件参数的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NCGSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| BITNUM | Bit索引 | 可选必选说明：该参数在"DT"配置为"Bit"时为条件必选参数。<br>参数含义：该参数表示Bit类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4000。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NCGSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| BITVALUE | Bit值 | 可选必选说明：该参数在"DT"配置为"Bit"时为条件必选参数。<br>参数含义：该参数表示Bit类型软件参数的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NCGSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| BYTENUM | Byte索引 | 可选必选说明：该参数在"DT"配置为"Byte"时为条件必选参数。<br>参数含义：该参数表示Byte类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1200。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NCGSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| BYTEVALUE | Byte值 | 可选必选说明：该参数在"DT"配置为"Byte"时为条件必选参数。<br>参数含义：该参数表示Byte类型软件参数的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NCGSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| STRINGNUM | String索引 | 可选必选说明：该参数在"DT"配置为"String"时为条件必选参数。<br>参数含义：该参数表示String类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~30。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NCGSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| STRINGVALUE | String值 | 可选必选说明：该参数在"DT"配置为"String"时为条件必选参数。<br>参数含义：该参数表示String类型软件参数的值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NCGSOFTPARA查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NCGSOFTPARA]] · NCG软参（NCGSOFTPARA）

## 使用实例

- 设置NCG软件参数，数据类型是“Dw”，Dword索引是“1”，Dword值是“3”
  ```
  SET NCGSOFTPARA: DT=Dw, DWORDNUM=1, DWORDVALUE=3;
  ```
- 设置NCG软件参数，数据类型是“Bit”，Bit索引是“1”，Bit值是“1”
  ```
  SET NCGSOFTPARA: DT=Bit, BITNUM=1, BITVALUE=1;
  ```
- 设置NCG软件参数，数据类型是“Byte”，Byte索引是“1”，Byte值是“3”
  ```
  SET NCGSOFTPARA: DT=Byte, BYTENUM=1, BYTEVALUE=3;
  ```
- 设置NCG软件参数，数据类型是“String”，String索引是“1”，String值是“ncg_service”
  ```
  SET NCGSOFTPARA: DT=String, STRINGNUM=1, STRINGVALUE="ncg_service";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置NCG软参（SET-NCGSOFTPARA）_53229141.md`
