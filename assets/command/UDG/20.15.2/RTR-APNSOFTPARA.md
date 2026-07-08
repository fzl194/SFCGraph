---
id: UDG@20.15.2@MMLCommand@RTR APNSOFTPARA
type: MMLCommand
name: RTR APNSOFTPARA（恢复APN软参记录）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: APNSOFTPARA
command_category: 动作类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- APN管理
- APN软参配置数据管理
status: active
---

# RTR APNSOFTPARA（恢复APN软参记录）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于恢复APN下软件参数信息。

## 注意事项

- 该命令执行后立即生效。
- BIT与BYTE类型软参执行该命令后将恢复成零，STRING类型软参执行该命令后将恢复成NULL。

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

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNSOFTPARA]] · APN软参记录（APNSOFTPARA）

## 使用实例

- 当需要恢复当前索引为8的APN BYTE类软参值为0时：
  ```
  RTR APNSOFTPARA: APN="f1", DT=BYTE, BYTENUM=8;
  ```
- 当需要恢复当前索引为8的APN BIT类软参值为0时：
  ```
  RTR APNSOFTPARA: APN="f1", DT=BIT, BITNUM=8;
  ```
- 当需要恢复当前索引为5的APN STRING类软参值为NULL时：
  ```
  RTR APNSOFTPARA: APN="f1", DT=STRING, STRINGNUM=5;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/恢复APN软参记录（RTR-APNSOFTPARA）_82837029.md`
