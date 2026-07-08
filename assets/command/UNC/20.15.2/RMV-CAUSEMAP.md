---
id: UNC@20.15.2@MMLCommand@RMV CAUSEMAP
type: MMLCommand
name: RMV CAUSEMAP（删除原因值映射配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CAUSEMAP
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
- 移动性管理
- 原因值管理
- 原因值映射配置
status: active
---

# RMV CAUSEMAP（删除原因值映射配置）

## 功能

**适用网元：SGSN、MME**

该命令用于删除一个原因值映射配置记录。原因值映射就是将原接口消息中的原因值直接映射到目标接口消息中下发的原因值。

## 注意事项

- 该命令执行后立即生效。
- 当删除一个CAUSEMAP时，不会影响GMMPROCTRL，PMMPROCTRL，EMMPROCTRL，GBSMPROCTRL，IUSMPROCTRL命令的设置。
- 执行该命令，可能会改变通过该映射配置进行原因值控制的异常场景中下发给终端的拒绝原因值，从而导致相应拒绝类话统指标的变化。
- 当软参[“BYTE_EX_B86”BIT5](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B86 BIT5 控制MME发送给UE的Attach Reject消息中携带的EMM _babd70be_99362835.md)、[“BYTE_EX_B86”BIT6](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B86 BIT6 控制MME发送给UE的Detach Request消息中携带的EMM_08cd63ac_99564219.md)、[“BYTE_EX_B86”BIT7](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B86 BIT7 控制MME发送给UE的Service Reject消息中携带的EMM_02416554_01403356.md)、[“BYTE_EX_B86”BIT8](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B86 BIT8 控制MME发送给UE的TAU Reject消息中携带的EMM Cau_4ecaf854_01163560.md)、[“BYTE_EX_B87”BIT1](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B87 BIT1 控制SGSN发送给MS的RAU Reject消息中携带的GMM Ca_d12fb174_99123339.md)、[“BYTE_EX_B87”BIT2](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B87 BIT2 控制在inter-MME TAU流程中由于二次Context Res_a61ceb84_00684116.md)中的任意一个设置为“1”时，如果使用了该配置，进行配置增删改操作时需要同时考虑软参控制的场景。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CAUSEGRPID | 原因值组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定表示一个原因值映射规则集合的唯一数字ID。<br>取值范围：1～127<br>默认值：无<br>说明：所删除原因值组标识必须在CAUSEGRP中存在，否则系统提示没有此原因值标识。建议在RMV CAUSEMAP之前可以先执行<br>[**LST CAUSEGRP**](../原因值映射组配置/查询原因值映射组配置(LST CAUSEGRP)_26145494.md)<br>来确定<br>“CAUSEGRPID”<br>是否存在。 |
| CAUSERANGE | 原因值范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定原因值范围。<br>取值范围：<br>- “DEFAULT(缺省)”<br>- “SPECIAL(特定)”<br>默认值：无 |
| BGCAUSE | 起始原始原因值 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定起始原始原因值。<br>前提条件：该参数在<br>“CAUSERANGE(原因值范围)”<br>设置为<br>“SPECIAL(特定)”<br>时，才需要配置。<br>取值范围：1～65535<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CAUSEMAP]] · 原因值映射配置（CAUSEMAP）

## 使用实例

删除CAUSEGRPID（原因值组标识）为126，CAUSERANGE（原因值范围）为DEFAULT（缺省）的原因值映射记录：

RMV CAUSEMAP: CAUSEGRPID=126, CAUSERANGE=DEFAULT;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CAUSEMAP.md`
