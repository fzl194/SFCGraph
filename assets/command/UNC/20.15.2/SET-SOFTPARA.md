---
id: UNC@20.15.2@MMLCommand@SET SOFTPARA
type: MMLCommand
name: SET SOFTPARA（设置软件参数表）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SOFTPARA
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 软件参数管理
- 软件参数
status: active
---

# SET SOFTPARA（设置软件参数表）

## 功能

![](设置软件参数表(SET SOFTPARA)_26146182.assets/notice_3.0-zh-cn_2.png)

请参考软件参数说明书。

**适用网元：SGSN、MME**

该命令用于配置软件参数信息。

## 注意事项

- 该命令执行后立即生效。
- 系统初次上电运行时，会执行系统初始设置值。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DT | 参数类型 | 可选必选说明：必选参数<br>参数含义：软件参数的数据类型。<br>数据来源：本端规划。<br>取值范围：<br>- “BYTE(单字节类型)”<br>- “DWORD(无符号整数类型)”<br>- “STR(字符串类型)”<br>- “BYTE_EX(扩展单字节类型)”<br>- “DWORD_EX(扩展无符号整数类型)”<br>- “STR_EX(扩展字符串类型)”<br>- “BYTE_EX_B(扩展单字节类型B)”<br>- “DWORD_EX_B(扩展无符号整数类型B)”<br>- “STR_EX_B(扩展字符串类型B)”<br>系统初始设置值：无 |
| PARANUM | 参数索引 | 可选必选说明：必选参数<br>参数含义：软件参数的索引。<br>数据来源：本端规划。<br>取值范围:1~512<br>系统初始设置值：无<br>配置原则：<br>- 当参数类型取值为“BYTE”时，参数索引的取值范围是“1~240”。<br>- 当参数类型取值为“DWORD”时，参数索引的取值范围是“1~60”。<br>- 当参数类型取值为“STR”时，参数索引的取值是“1”。<br>- 当参数类型取值为“BYTE_EX”时，参数索引的取值范围是“1~224”。<br>- 当参数类型取值为“DWORD_EX”时，参数索引的取值范围是“1~56”。<br>- 当参数类型取值为“STR_EX”时，参数索引的取值是“1”。<br>- 当参数类型取值为“BYTE_EX_B”时，参数索引的取值范围是“1~464”。<br>- 当参数类型取值为“DWORD_EX_B”时，参数索引的取值范围是“1~116”。<br>- 当参数类型取值为“STR_EX_B”时，参数索引的取值范围是“1”。 |
| VALUE | 参数值 | 可选必选说明：必选参数<br>参数含义：软件参数的取值。<br>数据来源：本端规划。<br>取值范围：<br>- 当参数类型取值为“BYTE”，“BYTE_EX”或“BYTE_EX_B”时，参数值的取值范围是“0~255”。<br>- 当参数类型取值为“DWORD”，“DWORD_EX”或“DWORD_EX_B”时，参数值的取值范围是“0~4294967295”。<br>- 当参数类型取值为“STR”，“STR_EX”或“STR_EX_B”时，参数值的取值范围是“1~31个字符”。<br>系统初始设置值：0 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SOFTPARA]] · 软件参数表（SOFTPARA）

## 使用实例

设置软参，参数类型是 “BYTE” ，参数索引为 “181” ，参数值为 “3” ：

SET SOFTPARA: DT=BYTE, PARANUM=181, VALUE="3";

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SOFTPARA.md`
