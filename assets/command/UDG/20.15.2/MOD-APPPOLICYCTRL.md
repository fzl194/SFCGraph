---
id: UDG@20.15.2@MMLCommand@MOD APPPOLICYCTRL
type: MMLCommand
name: MOD APPPOLICYCTRL（修改基于应用的质差上报策略）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: APPPOLICYCTRL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 智能板管理
- vvip
- 基于应用的质差策略
status: active
---

# MOD APPPOLICYCTRL（修改基于应用的质差上报策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改基于应用的质差上报策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPIDNAME | 应用ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定重点业务保障的应用组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，区分大小写，长度为1-63位。<br>默认值：无<br>配置原则：无 |
| SUBAPPIDNAME | 子应用ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定重点业务保障的应用名称。<br>数据来源：全网规划<br>取值范围：字符串类型，区分大小写，长度为1-63位。<br>默认值：无<br>配置原则：无 |
| DEFPRTGRPNAME | 自定义协议组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定自定义的三级协议组名称。<br>数据来源：本端规划<br>取值范围：参数来源于ADD SSUPROTCOLGROUP中的DEFPRTGRPNAME。<br>默认值：无<br>配置原则：无 |
| QOEDETPRD | 基于应用的质差上报周期 | 可选必选说明：可选参数<br>参数含义：该参数指定该应用下UPF检测用户业务发生质差时向NWDAF上报单据的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~300，单位为秒，必须大于等于SET VVIPBASICFUNC中配置的SAMPLEPERIOD。建议按5秒、10秒和15秒的粒度配置。<br>默认值：无<br>配置原则：无 |
| NONQOEDETPRD | 基于应用的非质差上报周期 | 可选必选说明：可选参数<br>参数含义：该参数指定该应用下UPF检测用户业务未发生质差时向NWDAF上报单据的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~300，单位为秒。1. 必须大于等于SET VVIPBASICFUNC中配置的SAMPLEPERIOD。2. 建议按60秒粒度配置。3. 体验单据配置周期应当大于BYTE1115中配置的应用结束时延时间，如果BYTE1115未配置，体验单据配置周期应当大于BYTE1115默认值（2秒）。<br>默认值：无<br>配置原则：无 |
| MOS | 平均意见分 | 可选必选说明：可选参数<br>参数含义：该参数用于配置平均意见分，UPF检测到应用实际的平均意见分不大于该值时，认为该应用质差。<br>数据来源：本端规划<br>取值范围：字符串类型，长度不超过3个字符。<br>默认值：无<br>配置原则：<br>- 请填写浮点数，精确到十分位，取值范围为1～5。<br>- 输入一个空格表示清除已设置的值。 |
| QOERPTPOLICY | 应用质差上报策略 | 可选必选说明：可选参数<br>参数含义：该参数用于设置应用质差时的单据上报策略。<br>数据来源：本端规划<br>取值范围：<br>- QOE_REPORT_ONCE：检测到质差时新流触发上报。<br>- QOE_REPORT_PERIOD：检测到质差时周期触发上报。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APPPOLICYCTRL]] · 基于应用的质差上报策略（APPPOLICYCTRL）

## 使用实例

- 修改应用ID为zhibo，子应用ID为huya的自定义协议组名称为testadc，执行如下命令：
  ```
  MOD APPPOLICYCTRL: APPIDNAME="zhibo", SUBAPPIDNAME="huya", DEFPRTGRPNAME="testadc";
  ```
- 删除应用ID为zhibo，子应用ID为huya配置的MOS值，可以通过MOD APPPOLICYCTRL命令在MOS参数字段中输入一个空格实现，执行命令如下：
  ```
  MOD APPPOLICYCTRL: APPIDNAME="zhibo", SUBAPPIDNAME="huya", MOS=" ";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改基于应用的质差上报策略（MOD-APPPOLICYCTRL）_15739989.md`
