---
id: UNC@20.15.2@MMLCommand@ADD RESERVEDCMD
type: MMLCommand
name: ADD RESERVEDCMD（新增补丁预留配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: RESERVEDCMD
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- SGSN
- MME
- SGW-C
- GGSN
- PGW-C
- SMSF
- NCG
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- 预留配置
status: active
---

# ADD RESERVEDCMD（新增补丁预留配置）

## 功能

**适用NF：AMF、SMF、NRF、SGSN、MME、SGW-C、GGSN、PGW-C、SMSF、NCG、NSSF**

新增补丁预留配置。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CMDNAME | 功能名称 | 可选必选说明：必选参数<br>参数含义：功能名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| PARASTR1 | 字符串参数1 | 可选必选说明：可选参数<br>参数含义：字符串参数1。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| PARASTR2 | 字符串参数2 | 可选必选说明：可选参数<br>参数含义：字符串参数2。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| PARASTR3 | 字符串参数3 | 可选必选说明：可选参数<br>参数含义：字符串参数3。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| PARAUINT1 | 整型参数1 | 可选必选说明：可选参数<br>参数含义：整型参数1。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：0<br>配置原则：无 |
| PARAUINT2 | 整型参数2 | 可选必选说明：可选参数<br>参数含义：整型参数2。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：0<br>配置原则：无 |
| PARAUINT3 | 整型参数3 | 可选必选说明：可选参数<br>参数含义：整型参数3。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：0<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESERVEDCMD]] · 补丁预留配置（RESERVEDCMD）

## 使用实例

新增补丁预留配置，其中功能名称为BALCKLIST，PARASTR1为parameter1，PARASTR2为parameter2，请运行以下命令：

```
ADD RESERVEDCMD: CMDNAME="BALCKLIST", PARASTR1="parameter1", PARASTR2="parameter2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-RESERVEDCMD.md`
