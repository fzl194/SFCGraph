---
id: UNC@20.15.2@MMLCommand@DSP REGNFPROFILE
type: MMLCommand
name: DSP REGNFPROFILE（显示网元概述信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: REGNFPROFILE
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- SMSF
- NCG
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF概述信息管理
status: active
---

# DSP REGNFPROFILE（显示网元概述信息）

## 功能

**适用NF：AMF、SMF、NRF、SMSF、NCG、NSSF**

该命令用于显示本端NF向NRF注册过的网元概述信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询条件 | 可选必选说明：可选参数<br>参数含义：查询条件，默认查询所有本端网元，选择NfType为查询条件需要填写网元类型，选择NfInstanceID为查询条件需要填写网元实例ID。<br>数据来源：本端规划<br>取值范围：<br>- ALL（默认显示所有结果）<br>- NFTYPE（根据网元类型查询）<br>- NFINSTANCEID（根据网元实例ID查询）<br>默认值：ALL<br>配置原则：无 |
| NFINSTANCEID | NF实例ID | 可选必选说明：该参数在"QUERYTYPE"配置为"NFINSTANCEID"时为条件必选参数。<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。本参数的构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，例如，AMF_Instance_0。本参数应与LST NFPROFILE命令查询结果中的“NF实例名称”一致。<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"NFTYPE"时为条件必选参数。<br>参数含义：该参数用于指定NF类型。<br>数据来源：本端规划<br>取值范围：<br>- AMF（AMF）<br>- SMF（SMF）<br>- NRF（NRF）<br>- NSSF（NSSF）<br>- SMSF（SMSF）<br>- NCG（NCG）<br>- NEF（NEF）<br>- NWDAF（NWDAF）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@REGNFPROFILE]] · 网元概述信息（REGNFPROFILE）

## 使用实例

查询当前本端网元的概述信息。

```
DSP REGNFPROFILE:;
DSP REGNFPROFILE: QUERYTYPE=NFTYPE, NFTYPE=AMF;
DSP REGNFPROFILE: QUERYTYPE=NFINSTANCEID, NFINSTANCEID="AMF_Instance_0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-REGNFPROFILE.md`
