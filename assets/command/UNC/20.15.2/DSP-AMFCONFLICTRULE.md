---
id: UNC@20.15.2@MMLCommand@DSP AMFCONFLICTRULE
type: MMLCommand
name: DSP AMFCONFLICTRULE（显示AMF冲突规则生效状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: AMFCONFLICTRULE
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF冲突配置管理
status: active
---

# DSP AMFCONFLICTRULE（显示AMF冲突规则生效状态）

## 功能

**适用NF：AMF**

该命令用于显示AMF冲突规则生效状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CSTYPE | CS类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CS类型。<br>数据来源：本端规划<br>取值范围：<br>- UEAM（UEAM模块）<br>- LOCM（LOCM模块）<br>- UEM（UEM模块）<br>- AMPOLICY（AMPOLICY模块）<br>默认值：无<br>配置原则：无 |
| PROCTYPE | 流程内部标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程内部类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。不能为非法字符，只允许输入字母，数字，区分大小写。例如：ProcTypeIntraAmfInitialReg。<br>默认值：无<br>配置原则：无 |
| INITEVENTID | 初始事件类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定触发新流程的初始事件类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。不能为非法字符，只允许输入字母，数字，区分大小写。例如：InitIntraRegistration。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFCONFLICTRULE]] · AMF冲突规则（AMFCONFLICTRULE）

## 使用实例

查询该条规则是否生效，规则如下: 在IntraAmfHandover流程中，如果收到了NG-RAN的“RRC Inactive Transition Report”消息，则执行抢占策略。

```
DSP AMFCONFLICTRULE: CSTYPE=UEAM, PROCTYPE="IntraAmfHandover", INITEVENTID="InitN2NotifyEvent";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-AMFCONFLICTRULE.md`
