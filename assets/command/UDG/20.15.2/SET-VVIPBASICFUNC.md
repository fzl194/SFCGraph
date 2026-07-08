---
id: UDG@20.15.2@MMLCommand@SET VVIPBASICFUNC
type: MMLCommand
name: SET VVIPBASICFUNC（设置重点业务保障基本功能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: VVIPBASICFUNC
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
max_records: 1
category_path:
- 智能板管理
- vvip
- 重点业务保障基本功能
status: active
---

# SET VVIPBASICFUNC（设置重点业务保障基本功能）

## 功能

**适用NF：PGW-U、UPF**

![](设置重点业务保障基本功能（SET VVIPBASICFUNC）_10221270.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，SWITCH开关置为DISABLE后，重点业务保障基本功能将会失效。

此命令用于设置重点业务保障基本功能的开关及上报周期等参数。

## 注意事项

- 该命令执行后60s生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH | QOERPTPERIOD | NONQOERPTPERIOD | REPORTSCOPE | SAMPLEPERIOD | RPTUSERTYPE |
| --- | --- | --- | --- | --- | --- | --- |
| 初始值 | DISABLE | 5 | 300 | ALL_QOE_REPORT | 5 | RPT_FOR5GUSER |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 重点业务保障基本功能 | 可选必选说明：必选参数<br>参数含义：该参数是配置重点业务保障基本功能的开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能重点业务保障基本功能。<br>- ENABLE：使能重点业务保障基本功能。<br>默认值：无<br>配置原则：无 |
| QOERPTPERIOD | 质差上报周期（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数指定UPF检测用户业务发生质差时向NWDAF上报单据的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~300，单位为秒，建议按5秒、10秒和15秒的粒度配置。<br>默认值：无<br>配置原则：QOERPTPERIOD的值要大于等于SAMPLEPERIOD的值。 |
| NONQOERPTPERIOD | 非质差上报周期（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数指定UPF向NWDAF上报重点业务保障用户体验单据的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~300，单位为秒。1. 建议按300秒粒度配置。2. 体验单据配置周期应当大于BYTE1115中配置的应用结束时延时间，如果BYTE1115未配置，体验单据配置周期应当大于BYTE1115默认值（2秒）。<br>默认值：无<br>配置原则：NONQOERPTPERIOD的值要大于等于SAMPLEPERIOD的值。 |
| REPORTSCOPE | 质差报表上报范围 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数指定质差报表上报的范围。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL_QOE_REPORT：支持上报质差单据和体验单据。<br>- ONLY_QOE_REPORT：支持发生质差时上报质差单据。<br>默认值：无<br>配置原则：无 |
| SAMPLEPERIOD | 采集单据周期（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数指定UPF进行质差检测的单据采样周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~300。<br>默认值：无<br>配置原则：SAMPLEPERIOD的值要小于等于QOERPTPERIOD的值。 SAMPLEPERIOD的值要小于等于NONQOERPTPERIOD的值。 |
| RPTUSERTYPE | 上报用户类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数指定质差报表支持上报的用户类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RPT_FOR5GUSER：支持上报5G用户单据。<br>- RPT_FOR45GUSER：支持上报4G和5G用户单据。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VVIPBASICFUNC]] · 重点业务保障基本功能（VVIPBASICFUNC）

## 使用实例

设置重点业务保障基本功能，开启重点业务保障基本功能开关，配置质差上报周期为5秒，非质差上报周期300秒，质差上报范围为ALL_QOE_REPORT，采集单据周期为5秒，用户为5G用户，执行如下命令：

```
SET VVIPBASICFUNC: SWITCH=ENABLE, QOERPTPERIOD=5, NONQOERPTPERIOD=300, REPORTSCOPE=ALL_QOE_REPORT, SAMPLEPERIOD=5, RPTUSERTYPE=RPT_FOR5GUSER;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置重点业务保障基本功能（SET-VVIPBASICFUNC）_10221270.md`
