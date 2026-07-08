---
id: UNC@20.15.2@MMLCommand@SET SOFTPARAOFBIT
type: MMLCommand
name: SET SOFTPARAOFBIT（设置软件参数表比特位）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SOFTPARAOFBIT
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
- 软件参数比特位
status: active
---

# SET SOFTPARAOFBIT（设置软件参数表比特位）

## 功能

![](设置软件参数表比特位(SET SOFTPARAOFBIT)_72345783.assets/notice_3.0-zh-cn_2.png)

请参考软件参数说明书。

**适用网元：SGSN、MME**

该命令用于设置软件参数表比特位。

在设置产品功能开关或者流程开关时，需要执行此命令。

## 注意事项

- 系统初次上电运行时，会执行系统初始设置值。
- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DT | 参数类型 | 可选必选说明：必选参数<br>参数含义：软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：<br>- “BYTE（单字节类型）”<br>- “DWORD（无符号整数类型）”<br>- “BYTE_EX（扩展单字节类型）”<br>- “DWORD_EX（扩展无符号整数类型）”<br>- “BYTE_EX_B（扩展单字节类型B）”<br>- “DWORD_EX_B（扩展无符号整数类型B）”<br>系统初始设置值：无 |
| PARANUM | 参数索引 | 可选必选说明：必选参数<br>参数含义：软件参数的索引。<br>数据来源：本端规划<br>取值范围：1~512<br>系统初始设置值：无<br>配置原则：<br>- 当参数类型取值为“BYTE”时，参数索引的取值范围是“1~240”。<br>- 当参数类型取值为“DWORD”时，参数索引的取值范围是“1~60”。<br>- 当参数类型取值为“BYTE_EX”时，参数索引的取值范围是“1~224”。<br>- 当参数类型取值为“DWORD_EX”时，参数索引的取值范围是“1~56”。<br>- 当参数类型取值为“BYTE_EX_B”时，参数索引的取值范围是“1~464”。<br>- 当参数类型取值为“DWORD_EX_B”时，参数索引的取值范围是“1~116”。 |
| VALUE | 参数值 | 可选必选说明：必选参数<br>参数含义：软件参数比特位的值。<br>数据来源：本端规划<br>取值范围：<br>- VALUE_0(0)<br>- VALUE_1(1)<br>系统初始设置值：无 |
| POSITION | 比特位 | 可选必选说明：必选参数<br>参数含义：软件参数比特位的位置。<br>数据来源：本端规划<br>取值范围：1~32<br>系统初始设置值：无<br>配置原则：<br>- 当参数类型取值为“BYTE”，“BYTE_EX”或“BYTE_EX_B”时，比特位的取值范围是“1~8”。<br>- 当参数类型取值为“DWORD”，“DWORD_EX”或“DWORD_EX_B”时，比特位的取值范围是“1~32”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SOFTPARAOFBIT]] · 软件参数表比特位（SOFTPARAOFBIT）

## 使用实例

设置单字节类型1号软参Bit1值为0:

SET SOFTPARAOFBIT: DT=BYTE, PARANUM=1, VALUE=VALUE_0, POSITION=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置软件参数表比特位(SET-SOFTPARAOFBIT)_72345783.md`
