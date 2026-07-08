---
id: UDG@20.15.2@MMLCommand@SET SOFTPARAOFBIT
type: MMLCommand
name: SET SOFTPARAOFBIT（设置软件参数表比特位的值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SOFTPARAOFBIT
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务软参管理
- 软件参数比特位
status: active
---

# SET SOFTPARAOFBIT（设置软件参数表比特位的值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置软件参数表比特位。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DT2 | 软参记录数据类型 | 可选必选说明：必选参数<br>参数含义：软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>默认值：无<br>配置原则：<br>- 配置BYTE表示需要设置字节类型软件参数。<br>- 配置DWORD表示需要设置双字类型软件参数。 |
| BYTENUM | Byte索引 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DT2”配置为“BYTE”时为必选参数。<br>参数含义：字节类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1200。取值范围在1到1200之间的整数。<br>默认值：无<br>配置原则：无 |
| DWORDNUM | DWord索引 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DT2”配置为“DWORD”时为必选参数。<br>参数含义：双字类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～180。取值范围在1到180之前的整数。<br>默认值：无<br>配置原则：无 |
| BYTEPOSITION | Byte软参BIT位位置 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DT2”配置为“BYTE”时为必选参数。<br>参数含义：Byte软参指定的BIT位位置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～8。<br>默认值：无<br>配置原则：无 |
| DWORDPOSITION | Dword软参BIT位位置 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DT2”配置为“DWORD”时为必选参数。<br>参数含义：Dword软参指定的BIT位位置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32。<br>默认值：无<br>配置原则：无 |
| BYTEVALUE | Byte值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DT2”配置为“BYTE”时为必选参数。<br>参数含义：字节类型参数的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1。取值范围在0到1之间的整数。<br>默认值：无<br>配置原则：无 |
| DWORDVALUE | Dword值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DT2”配置为“DWORD”时为必选参数。<br>参数含义：双字类型参数的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1。取值范围在0到1之间的整数。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SOFTPARAOFBIT]] · 软件参数指定比特位的值（SOFTPARAOFBIT）

## 关联任务

- [[UDG@20.15.2@Task@0-00137]]

## 使用实例

设置单字节类型1号软参Bit1位的值为1：

```
SET SOFTPARAOFBIT: DT2=BYTE, BYTENUM=1, BYTEPOSITION=1, BYTEVALUE=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置软件参数表比特位的值（SET-SOFTPARAOFBIT）_82837317.md`
