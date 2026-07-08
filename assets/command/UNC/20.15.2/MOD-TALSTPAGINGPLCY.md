---
id: UNC@20.15.2@MMLCommand@MOD TALSTPAGINGPLCY
type: MMLCommand
name: MOD TALSTPAGINGPLCY（修改TA List寻呼策略配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: TALSTPAGINGPLCY
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- 基于TA List寻呼策略管理
status: active
---

# MOD TALSTPAGINGPLCY（修改TA List寻呼策略配置）

## 功能

**适用网元：MME**

该命令用于修改基于TA List的寻呼策略配置数据。

## 注意事项

- 该命令执行后立即生效。
- 通过该命令关闭指定TA List的LTE精准寻呼后，扩大了寻呼范围，可能增加eNodeB的寻呼负荷。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TALISTID | TA List标号 | 可选必选说明：必选参数<br>参数含义：该参数用于在MME内唯一标识一个跟踪区列表。一个跟踪区列表由若干跟踪区TA组合而成。<br>数据来源：本端规划<br>取值范围：0~65534。<br>默认值：无 |
| CLSPRECISEPAG | 是否关闭精准寻呼 | 可选必选说明：可选参数<br>参数含义：该参数用来配置指定的TA List是否关闭精准寻呼。<br>数据来源：全网规划<br>取值范围：<br>- YES(是)<br>- NO(否)<br>默认值：无<br>说明：该命令配置指定的TA List关闭精准寻呼功能后，针对该TA List的“LTE精准寻呼”功能将失效。 |
| CONFIGTIMER | 是否配置定时器 | 可选必选说明：可选参数<br>参数含义：本参数用于标识是否要基于TA List配置差异化寻呼定时器。<br>数据来源：全网规划<br>取值范围：<br>- YES(是)<br>- NO(否)<br>默认值：无 |
| T3413 | T3413(s) | 可选必选说明：条件可选参数<br>参数含义：此定时器用于控制MME发起寻呼与UE响应的时间间隔。此定时器在MME发送Paging Request消息后启动，在收到Service Request消息后停止，超时后，MME重发Paging Request消息。<br>前提条件：该参数在<br>“是否配置定时器”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：全网规划<br>取值范围：3~12。<br>默认值：无 |
| N3413 | N3413(times) | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定在寻呼流程中，没有收到UE的响应消息，MME重复发送Paging Request消息的最大次数。<br>前提条件：该参数在<br>“是否配置定时器”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0~5。<br>默认值：无 |
| PAGINGDELTA | 重寻呼间隔递增值(s) | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定在寻呼流程中，没有收到Service Request消息，MME重复发送Paging Request消息的间隔递增时间值。<br>前提条件：该参数在<br>“是否配置定时器”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0~20。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TALSTPAGINGPLCY]] · TA List寻呼策略配置（TALSTPAGINGPLCY）

## 使用实例

修改一条TA List寻呼策略配置：

MOD TALSTPAGINGPLCY: TALISTID=1, CLSPRECISEPAG=NO, CONFIGTIMER=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-TALSTPAGINGPLCY.md`
