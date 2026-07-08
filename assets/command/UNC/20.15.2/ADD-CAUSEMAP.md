---
id: UNC@20.15.2@MMLCommand@ADD CAUSEMAP
type: MMLCommand
name: ADD CAUSEMAP（增加原因值映射配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CAUSEMAP
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 原因值管理
- 原因值映射配置
status: active
---

# ADD CAUSEMAP（增加原因值映射配置）

## 功能

**适用网元：SGSN、MME**

此命令用于增加一个原因值映射配置记录。原因值映射就是将原接口消息中的原因值直接映射到目标接口消息中下发的原因值。

## 注意事项

- 此命令执行后立即生效。
- 此命令的最大记录数为1024。
- 执行此命令可能会改变通过该映射配置进行原因值控制的异常场景中下发给终端的拒绝原因值，从而导致相应拒绝类话统指标的变化。
- 当Attach、RAU/TAU流程中HLR/HSS或MSC发送消息携带的原因值有多种情况时，将采用ADD CAUSEMAP命令配置对应的原因值映射规则。原因值映射规则请参见[MME与HSS交互错误码映射关系表](../../../../../../../../../../extracted_UNC 20.15.2 产品文档(裸机容器) 05/resources/mml/document/resource/mmeandhssinteractionerrorcodemappingtable.xls)。
- 配置下发的原因值可能会对终端行为产生影响，在配置前评估影响。关于不同原因值的含义及对终端行为的影响请参见协议3GPP TS 24.008或3GPP TS 24.301。
- 当软参[“BYTE_EX_B86”BIT5](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B86 BIT5 控制MME发送给UE的Attach Reject消息中携带的EMM _babd70be_99362835.md)、[“BYTE_EX_B86”BIT6](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B86 BIT6 控制MME发送给UE的Detach Request消息中携带的EMM_08cd63ac_99564219.md)、[“BYTE_EX_B86”BIT7](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B86 BIT7 控制MME发送给UE的Service Reject消息中携带的EMM_02416554_01403356.md)、[“BYTE_EX_B86”BIT8](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B86 BIT8 控制MME发送给UE的TAU Reject消息中携带的EMM Cau_4ecaf854_01163560.md)、[“BYTE_EX_B87”BIT1](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B87 BIT1 控制SGSN发送给MS的RAU Reject消息中携带的GMM Ca_d12fb174_99123339.md)、[“BYTE_EX_B87”BIT2](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B87 BIT2 控制在inter-MME TAU流程中由于二次Context Res_a61ceb84_00684116.md)中的任意一个设置为“1”时，如果使用了该配置，进行配置增删改操作时需要同时考虑软参控制的场景。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CAUSEGRPID | 原因值组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定表示一个原因值映射规则集合的唯一数字ID。<br>数据来源：整网规划<br>取值范围：1～127<br>默认值：无<br>配置原则：所增加原因值组标识必须在CAUSEGRP中存在，否则系统提示没有此原因值标识。建议在ADD CAUSEMAP之前可以先执行<br>[**LST CAUSEGRP**](../原因值映射组配置/查询原因值映射组配置(LST CAUSEGRP)_26145494.md)<br>来确定<br>“CAUSEGRPID”<br>是否存在。 |
| CAUSERANGE | 原因值范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定原因值范围。<br>数据来源：整网规划<br>取值范围：<br>- “DEFAULT(缺省)”：表示无需指定某一特定接口的起始和终止原始原因值。<br>- “SPECIAL(特定)”：表示需指定某一特定接口的起始原始原因值。<br>默认值：<br>“DEFAULT(缺省)”<br>配置原则：<br>- 一个“CAUSEGRPID(原因值组标识)”只能对应一个“DEFAULT(缺省)”配置。“SPECIAL(特定)”可以配置多个。如果同时配置了“DEFAULT(缺省)”和“SPECIAL(特定)”的记录，则优先使用“SPECIAL(特定)”记录。<br>- 同一个原因值组内的“原因值范围”之间不能重叠。<br>说明：例如：执行<br>ADD CAUSEMAP: CAUSEGRPID=1, CAUSERANGE=SPECIAL, BGCAUSE=1, EDCAUSE=99, TCAUSE=99;<br>再执行<br>ADD CAUSEMAP: CAUSEGRPID=1, CAUSERANGE=SPECIAL, BGCAUSE=98, EDCAUSE=100, TCAUSE=100;<br>会提示原因值范围重叠。 |
| BGCAUSE | 起始原始原因值 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定某一特定接口的起始原始原因值。<br>前提条件：该参数在<br>“CAUSERANGE(原因值范围)”<br>参数设置为<br>“SPECIAL(特定)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～65535<br>默认值：无<br>配置原则：<br>- “BGCAUSE(起始原始原因值)”小于等于“EDCAUSE(终止原始原因值)”。<br>- 当原始原因值表示S6a/S6d错误码时，目前支持29272协议定义的所有错误码5001、5420、5421、5004、5422、5423、4181以及Diameter基础协议RFC 3588定义的错误码5003，暂不支持其他Diameter基础协议定义的错误码。对于不支持的错误码，默认下发原因值#17 （Network failure）。如果误配了错误码5005，不支持的错误码会在AIR流程中用5005映射的目标原因值下发。如果误配了错误码5012，不支持的错误码会在ULR流程中用5012映射的原因值下发。原因值映射规则请参见[MME与HSS交互错误码映射关系表](../../../../../../../../../../extracted_UNC 20.15.2 产品文档(裸机容器) 05/resources/mml/document/resource/mmeandhssinteractionerrorcodemappingtable_0000002309067513.xls)。<br>- [Context Response错误码映射关系表](../../../../../../../../../../extracted_UNC 20.15.2 产品文档(裸机容器) 05/resources/mml/document/resource/gtpcv2interfaceerrorcodemappingtable.xlsx)。 |
| EDCAUSE | 终止原始原因值 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定某一特定接口的终止原始原因值。<br>前提条件：该参数在<br>“CAUSERANGE(原因值范围)”<br>参数设置为<br>“SPECIAL(特定)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～65535<br>默认值：无<br>配置原则：<br>- “EDCAUSE(终止原始原因值)”大于等于“BGCAUSE(起始原始原因值)”。<br>- 如果未输入“终止原始原因值”或输入值等于“起始原始原因值”，则表示某个固定的原因值。 |
| TCAUSE | 目标原因值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定下发到目标网元的原因值。<br>数据来源：整网规划<br>取值范围：1～65535<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CAUSEMAP]] · 原因值映射配置（CAUSEMAP）

## 使用实例

增加原因值映射配置：CAUSEGRPID（原因值组标识）为126，CAUSERANGE（原因值范围）为DEFAULT（缺省），TCAUSE（目标原因值）为27：

ADD CAUSEMAP: CAUSEGRPID=126, CAUSERANGE=DEFAULT, TCAUSE=27;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-CAUSEMAP.md`
