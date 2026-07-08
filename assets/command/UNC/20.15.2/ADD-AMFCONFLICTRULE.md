---
id: UNC@20.15.2@MMLCommand@ADD AMFCONFLICTRULE
type: MMLCommand
name: ADD AMFCONFLICTRULE（增加AMF冲突规则）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: AMFCONFLICTRULE
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF冲突配置管理
status: active
---

# ADD AMFCONFLICTRULE（增加AMF冲突规则）

## 功能

![](增加AMF冲突规则（ADD AMFCONFLICTRULE）_10622468.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，增加冲突规则可能影响现有业务对冲突场景的判断和解决策略，如果需要使用该命令，请联系华为技术支持。

**适用NF：AMF**

该命令用于增加AMF在特定冲突场景下的冲突处理规则。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CSTYPE | CS类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CS的类型。<br>数据来源：本端规划<br>取值范围：<br>- UEAM（UEAM模块）<br>- LOCM（LOCM模块）<br>- UEM（UEM模块）<br>- AMPOLICY（AMPOLICY模块）<br>默认值：无<br>配置原则：无 |
| PROCTYPE | 流程内部标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程内部标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。不能为非法字符，只允许输入字母，数字，区分大小写。例如：ProcTypeIntraAmfInitialReg。<br>默认值：无<br>配置原则：无 |
| INITEVENTID | 初始事件类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定触发新流程的初始事件类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。不能为非法字符，只允许输入字母，数字，区分大小写。例如：InitIntraRegistration。<br>默认值：无<br>配置原则：无 |
| RULE | 冲突流程规则 | 可选必选说明：必选参数<br>参数含义：该参数用于指定冲突流程规则。<br>数据来源：本端规划<br>取值范围：任意类型，取值范围是0~4096。不能为非法字符，只允许输入JSON格式范围内的合法字符，区分大小写。例如：{"Name": "When","Children": [{ "Name": "ResultPreempt" }]}。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [AMF冲突规则（AMFCONFLICTRULE）](configobject/UNC/20.15.2/AMFCONFLICTRULE.md)

## 使用实例

在IntraAmfHandover流程中，收到了NG-RAN的“RRC Inactive Transition Report”消息，如果希望执行抢占策略，则执行如下命令。

```
ADD AMFCONFLICTRULE: CSTYPE=UEAM, PROCTYPE="IntraAmfHandover", INITEVENTID="InitN2NotifyEvent", RULE="{\"Name\":\"When\",\"Children\":[{\"Name\":\"ResultPreempt\"}]}";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加AMF冲突规则（ADD-AMFCONFLICTRULE）_10622468.md`
