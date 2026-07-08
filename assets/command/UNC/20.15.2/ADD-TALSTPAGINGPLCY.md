---
id: UNC@20.15.2@MMLCommand@ADD TALSTPAGINGPLCY
type: MMLCommand
name: ADD TALSTPAGINGPLCY（增加TA List寻呼策略配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TALSTPAGINGPLCY
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 2000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- 基于TA List寻呼策略管理
status: active
---

# ADD TALSTPAGINGPLCY（增加TA List寻呼策略配置）

## 功能

**适用网元：MME**

该命令用于设置增加TA List的寻呼策略配置数据。通过该命令可以配置指定的TA List是否关闭精准寻呼、是否配置TA List范围的寻呼定时器。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为2000。
- 通过该命令关闭指定TA List的LTE精准寻呼后，扩大了寻呼范围，可能增加eNodeB的寻呼负荷。
- 该命令受“LTE精准寻呼”License控制，只有获得了License许可后本配置的功能才能生效，对应的License控制项为“LTE精准寻呼”。
- 配置该命令后，针对特定的TA List，[**SET EMM**](../../移动性管理/MM协议参数管理/S1模式MM协议参数/设置S1模式MM协议参数(SET EMM)_72225207.md)中配置的“T3413”“N3413”“PAGINGDELTA”值将失效。
- 该命令不适用于NB-IoT用户。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TALISTID | TA List标号 | 可选必选说明：必选参数<br>参数含义：该参数用于在MME内唯一标识一个跟踪区列表。一个跟踪区列表由若干跟踪区TA组合而成。<br>数据来源：本端规划<br>取值范围：0~65534。<br>默认值：无<br>配置原则：本参数配置前须先在<br>[**ADD TALST**](../../移动性管理/TA List管理/增加跟踪区列表(ADD TALST)_26305388.md)<br>中配置。 |
| CLSPRECISEPAG | 是否关闭精准寻呼 | 可选必选说明：可选参数<br>参数含义：该参数用来配置指定的TA List是否关闭精准寻呼。<br>数据来源：全网规划<br>取值范围：<br>- YES(是)<br>- NO(否)<br>默认值：YES(是)<br>说明：该命令配置指定的TA List关闭精准寻呼功能后，针对该TA List的“LTE精准寻呼”功能将失效。 |
| CONFIGTIMER | 是否配置定时器 | 可选必选说明：可选参数<br>参数含义：本参数用于标识是否要基于TA List配置差异化寻呼定时器。<br>数据来源：全网规划<br>取值范围：<br>- YES(是)<br>- NO(否)<br>默认值：NO(否)<br>配置原则：需要针对特定的TA List设置差异化的寻呼间隔时，该参数设置为<br>“YES(是)”<br>，此时TA List范围的寻呼使用本条命令配置的<br>“T3413”<br>“N3413”<br>“PAGINGDELTA”<br>，否则TA List范围的寻呼仍使用<br>[**SET EMM**](../../移动性管理/MM协议参数管理/S1模式MM协议参数/设置S1模式MM协议参数(SET EMM)_72225207.md)<br>中配置的<br>“T3413”<br>“N3413”<br>“PAGINGDELTA”<br>。 |
| T3413 | T3413(s) | 可选必选说明：条件必选参数<br>参数含义：此定时器用于控制MME发起寻呼与UE响应的时间间隔。此定时器在MME发送Paging Request消息后启动，在收到Service Request消息后停止，超时后，MME重发Paging Request消息。<br>前提条件：该参数在<br>“是否配置定时器”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：全网规划<br>取值范围：3~12。<br>默认值：无 |
| N3413 | N3413(times) | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定在寻呼流程中，没有收到UE的响应消息，MME重复发送Paging Request消息的最大次数。<br>前提条件：该参数在<br>“是否配置定时器”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0~5。<br>默认值：无 |
| PAGINGDELTA | 重寻呼间隔递增值(s) | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定在寻呼流程中，没有收到Service Request消息，MME重复发送Paging Request消息的间隔递增时间值。<br>前提条件：该参数在<br>“是否配置定时器”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0~20。<br>默认值：0 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TALSTPAGINGPLCY]] · TA List寻呼策略配置（TALSTPAGINGPLCY）

## 使用实例

增加一条TA List寻呼策略配置：

ADD TALSTPAGINGPLCY: TALISTID=1, CLSPRECISEPAG=YES, CONFIGTIMER=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-TALSTPAGINGPLCY.md`
