---
id: UNC@20.15.2@MMLCommand@SET IUSMPROCTRL
type: MMLCommand
name: SET IUSMPROCTRL（设置Iu模式SM流程控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IUSMPROCTRL
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
- Iu模式SM流程控制参数
status: active
---

# SET IUSMPROCTRL（设置Iu模式SM流程控制参数）

## 功能

![](设置Iu模式SM流程控制参数（SET IUSMPROCTRL）_72345289.assets/notice_3.0-zh-cn_2.png)

下发不合适的原因值可能导致UE无法进行业务。

**适用网元：SGSN**

该命令用于设置Iu模式SM流程控制参数。在用户接入Iu模式时， UNC 可通过该命令控制SM流程进行特殊处理以及特殊场景下指定的原因值下发，以满足运营商实现对现网设备兼容性特殊控制的需求。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 通过该命令配置不合适的原因值下发给UE后，可能导致UE无法进行业务。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROT | 流程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程类型，要根据场景来配置相应的流程。<br>数据来源：整网规划<br>取值范围：<br>- “ACT_PROC(激活流程)”<br>- “MOD_PROC(修改流程)”<br>- “HSS_INIT_SUB_QOS_MOD_PROC(HSS发起的签约QoS修改流程)”<br>系统初始设置值：无 |
| ACTGGSNTMOUT | 激活拒绝原因值（GGSN超时） | 可选必选说明：条件可选参数<br>参数含义：该参数用于当GGSN超时，激活拒绝原因值。<br>前提条件：该参数在<br>“流程类型”<br>参数设置为<br>“激活流程”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0～112<br>系统初始设置值：0<br>配置原则：<br>- 0表示清除原有的配置。<br>- 1~7为非协议定义原因值，不建议使用。 |
| ACTGGSNREJ | 激活拒绝原因值（GGSN拒绝） | 可选必选说明：条件可选参数<br>参数含义：该参数用于激活流程中当GGSN拒绝时，使用一个拒绝原因值映射规则。<br>前提条件：该参数在<br>“流程类型”<br>参数设置为<br>“激活流程”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0～127<br>系统初始设置值：0<br>配置原则：<br>- 0表示清除原有的配置。<br>- 如果该参数取值不为0，必须为[**ADD CAUSEGRP**](../../../../移动性管理/原因值管理/原因值映射组配置/增加原因值映射组配置(ADD CAUSEGRP)_72225173.md)中已经存在的“CAUSEGRPID”。 |
| MODGGSNREJ | 修改拒绝原因值（GGSN拒绝） | 可选必选说明：条件可选参数<br>参数含义：该参数用于修改流程中当GGSN拒绝时，使用一个拒绝原因值映射规则。<br>前提条件：该参数在<br>“流程类型”<br>参数设置为<br>“修改流程”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0～127<br>系统初始设置值：0<br>配置原则：<br>- 0表示清除原有的配置。<br>- 如果该参数取值不为0，必须为[**ADD CAUSEGRP**](../../../../移动性管理/原因值管理/原因值映射组配置/增加原因值映射组配置(ADD CAUSEGRP)_72225173.md)中已经存在的“CAUSEGRPID”。 |
| RABMODFAILFLG | 当RAB修改失败时删除PDP | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定当MS或网络侧发起RAB修改时，如果RAB修改失败，是否删除PDP上下文。<br>前提条件：该参数在<br>“流程类型”<br>参数设置为<br>“修改流程”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”：表示当MS或网络侧发起的RAB修改失败时保留PDP上下文。<br>- “YES(是)”：表示当MS或网络侧发起的RAB修改失败时删除PDP上下文。<br>系统初始设置值：NO(否) |
| PPU | 是否使用保留过程 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定是否在Iu连接/RAB释放后保留实时类承载带宽。<br>前提条件：该参数在<br>“流程类型”<br>参数设置为<br>“修改流程”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：<br>- “YES(是)”：保留。Iu连接释放/RAB释放后，系统保留实时类承载带宽，不改变其上下行Maximum bitrate/Guaranteed bitrate。在网络中有不支持MS-Initiated PDP Context Modification流程的UE时，可以打开该开关，避免Iu连接/RAB释放后，UE无法为带宽被降为0kbit/的PDP Context重新建立RAB进行数据传输。<br>- “NO(否)”：不保留。Iu连接/RAB释放后，系统不保留实时类承载带宽，对实时类PDP Context降低其上下行Maximum bitrate/Guaranteed bitrat为0kbit/s，对于这些速率被降低为0kbit/s的PDP Context，UE必须主动发起MS-Initiated PDP Context Modification重建RAB进行数据传输，普通的Service Request流程不能触发这类PDP Context重建RAB。这种方式是3GPP TS 23.060协议定义的标准处理方式。<br>系统初始设置值：YES(是) |
| SUBQOSCMP | 签约QoS变更判断策略 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制HSS发起签约QoS修改时，SGSN决定是否发起承载修改流程的判断策略。<br>前提条件：该参数在<br>“流程类型”<br>参数设置为<br>“HSS发起的签约QoS修改流程”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “QOS_IN_USE(与正在使用的QoS比较)”<br>- “QOS_SUB(与原签约QoS比较)”<br>系统初始设置值：<br>“QOS_IN_USE(与正在使用的QoS比较)”<br>说明：- “QOS_IN_USE(与正在使用的QoS比较)”:用新的签约EPS QoS与正在使用的EPS QoS进行比较，如果有变化就发起承载修改流程。如果不希望签约EPS QoS变更对已经存在的EPS承载实时生效，以避免对正在进行的业务产生影响，可以选择该取值。<br>- “QOS_SUB(与原签约QoS比较)”:用新的签约EPS QoS与原签约QoS进行比较，如果有变化就发起承载修改流程，3GPP协议定义的标准处理方式。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IUSMPROCTRL]] · Iu模式SM流程控制参数（IUSMPROCTRL）

## 使用实例

设置 “PROT（流程类型）” 为 “MOD_PROC（修改流程）” ， “修改拒绝原因（GGSN拒绝）” 为 “0” ， “RABMODFAILFLG（当RAB修改失败时删除PDP）” 为 “NO (否)” ， “PPU（是否使用保留过程）” 为 “YES (是)” 的Iu模式SM流程控制参数：

SET IUSMPROCTRL: PROT=MOD_PROC, MODGGSNREJ=0, RABMODFAILFLG=NO, PPU=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-IUSMPROCTRL.md`
