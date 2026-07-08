---
id: UNC@20.15.2@MMLCommand@RMV RESERVEDMOC3
type: MMLCommand
name: RMV RESERVEDMOC3（删除补丁预留MOC3）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RESERVEDMOC3
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- SMSF
- SGSN
- MME
- SGW-C
- PGW-C
- GGSN
- NCG
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- MOC预留
status: active
---

# RMV RESERVEDMOC3（删除补丁预留MOC3）

## 功能

**适用NF：AMF、SMF、NRF、SMSF、SGSN、MME、SGW-C、PGW-C、GGSN、NCG、NSSF**

删除补丁预留MOC3。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARAIDX | 参数索引 | 可选必选说明：必选参数<br>参数含义：参数索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| PARAMETER1 | 参数1 | 可选必选说明：可选参数<br>参数含义：参数1。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| PARAMETER2 | 参数2 | 可选必选说明：可选参数<br>参数含义：参数2。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| PARAMETER3 | 参数3 | 可选必选说明：可选参数<br>参数含义：参数3。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| PARAMETER4 | 参数4 | 可选必选说明：可选参数<br>参数含义：参数4。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| PARAMETER5 | 参数5 | 可选必选说明：可选参数<br>参数含义：参数5。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESERVEDMOC3]] · 补丁预留MOC3（RESERVEDMOC3）

## 使用实例

删除补丁预留MOC3，其中PARAIDX为32，PARAMETER1为parameter1，PARAMETER2为parameter2，PARAMETER3为parameter3，PARAMETER4为parameter4，PARAMETER5为parameter5，请运行以下命令：

```
RMV RESERVEDMOC3: PARAIDX=32, PARAMETER1="parameter1", PARAMETER2="parameter2", PARAMETER3="parameter3", PARAMETER4="parameter4", PARAMETER5="parameter5";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RESERVEDMOC3.md`
