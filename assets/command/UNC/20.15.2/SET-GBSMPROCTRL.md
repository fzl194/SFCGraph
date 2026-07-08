---
id: UNC@20.15.2@MMLCommand@SET GBSMPROCTRL
type: MMLCommand
name: SET GBSMPROCTRL（设置Gb模式SM流程控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GBSMPROCTRL
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- SM流程管理
- Gb模式SM流程控制参数
status: active
---

# SET GBSMPROCTRL（设置Gb模式SM流程控制参数）

## 功能

![](设置Gb模式SM流程控制参数（SET GBSMPROCTRL）_26145692.assets/notice_3.0-zh-cn_2.png)

通过该命令配置不合适的原因值下发给MS后，可能导致MS无法进行业务。

**适用网元：SGSN**

该命令用于设置Gb模式SM流程控制参数。在用户接入Gb模式时， UNC 可通过该命令控制SM流程进行特殊处理以及特殊场景下指定的原因值下发，以满足运营商实现对现网设备兼容性特殊控制的需求。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 通过该命令配置不合适的原因值下发给MS后，可能导致MS无法进行业务。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROT | 流程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程类型，要根据场景来配置相应的流程。<br>数据来源：整网规划<br>取值范围：<br>- “ACT_PROC(激活流程)”<br>- “MOD_PROC(修改流程)”<br>- “PFC_PROC(PFC流程)”<br>- “HSS_INIT_SUB_QOS_MOD_PROC(HSS发起的签约QoS修改流程)”<br>系统初始设置值：无 |
| ACTGGSNTMOUT | 激活拒绝原因值（GGSN超时） | 可选必选说明：条件可选参数<br>参数含义：该参数用于当GGSN超时，激活拒绝原因值。<br>前提条件：该参数在<br>“流程类型”<br>参数设置为<br>“激活流程”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围： 0～112<br>系统初始设置值：0<br>说明：0表示清除原有的配置，系统默认下发#30（Activation rejected by GGSN）原因值。1~7为非协议定义原因值，不建议使用。 |
| ACTGGSNREJ | 激活拒绝原因值（GGSN拒绝） | 可选必选说明：条件可选参数<br>参数含义：该参数用于当GGSN拒绝时，激活一个拒绝原因值映射规则。<br>前提条件：该参数在<br>“流程类型”<br>参数设置为<br>“激活流程”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0～127<br>系统初始设置值：0<br>说明：0表示清除原有的配置。如果该参数取值不为0，必须为CAUSEGRP中已经存在的CAUSEGRPID 。 |
| MODGGSNREJ | 修改拒绝原因值（GGSN拒绝） | 可选必选说明：条件可选参数<br>参数含义：该参数用于当GGSN拒绝时，修改一个拒绝原因值映射规则。<br>前提条件：该参数在<br>“流程类型”<br>参数设置为<br>“修改流程”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0～127<br>系统初始设置值：0<br>说明：0表示清除原有的配置。如果该参数取值不为0，必须为CAUSEGRP中已经存在的CAUSEGRPID 。 |
| PFC | PFC流程处理 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定<br>“PFC流程处理”<br>。<br>前提条件：该参数在<br>“流程类型”<br>参数设置为<br>“PFC流程”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “PROTOCOL_DEFINE(协议定义)”<br>- “SELF_DEFINE(自定义)”<br>系统初始设置值：<br>“PROTOCOL_DEFINE(协议定义)”<br>说明：“PROTOCOL_DEFINE(协议定义)”<br>：BSS发起的Download BSS PFC Request流程，PFC流程按照协议描述进行。<br>“SELF_DEFINE(自定义)”<br>：BSS发起的Download BSS PFC Request流程，增加QoS重新协商部分。 |
| SUBQOSCMP | 签约QoS变更判断策略 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制HSS发起签约QoS修改时，SGSN决定是否发起承载修改流程的判断策略。<br>前提条件：该参数在<br>“流程类型”<br>参数设置为<br>“HSS发起的签约QoS修改流程”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “QOS_IN_USE(与正在使用的QoS比较)”<br>- “QOS_SUB(与原签约QoS比较)”<br>系统初始设置值：<br>“QOS_IN_USE(与正在使用的QoS比较)”<br>说明：- “QOS_IN_USE(与正在使用的QoS比较)”:用新的签约EPS QoS与正在使用的EPS QoS进行比较，如果有变化就发起承载修改流程。如果不希望签约EPS QoS变更对已经存在的EPS承载实时生效，以避免对正在进行的业务产生影响，可以选择该取值。<br>- “QOS_SUB(与原签约QoS比较)”:用新的签约EPS QoS与原签约QoS进行比较，如果有变化就发起承载修改流程，3GPP协议定义的标准处理方式。 |

## 操作的配置对象

- [Gb模式SM流程控制参数（GBSMPROCTRL）](configobject/UNC/20.15.2/GBSMPROCTRL.md)

## 使用实例

设置 “PROT（流程类型）” 为 “MOD_PROC（修改流程）” ， “修改拒绝原因（GGSN拒绝）” 为 “3” 的Gb模式SM流程控制参数：

SET GBSMPROCTRL: PROT=MOD_PROC, MODGGSNREJ=3;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置Gb模式SM流程控制参数（SET-GBSMPROCTRL）_26145692.md`
