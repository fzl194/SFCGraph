---
id: UNC@20.15.2@MMLCommand@SET SMS
type: MMLCommand
name: SET SMS（设置SMS配置信息）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMS
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
- 短消息
- 短消息配置
status: active
---

# SET SMS（设置SMS配置信息）

## 功能

**适用网元：SGSN**

该命令用于设置SMS相关的参数配置。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 由于受Gd接口中底层定时器时长的限制(28秒)，参数“短消息最大重发次数(SMSMRT)”和“SMMT等待CP_ACK定时器(TR3)”之间应该满足以下的制约关系：(SMSMRT+1) TR3 < 28000。
- QoS参数取系统初始设置值即可，不需要改动。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RC | QoS可靠性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定2G SMS QoS可靠性指标。<br>数据来源：整网规划<br>取值范围：1~5<br>系统初始设置值：1 |
| PRI | QoS优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定2G SMS QoS优先级指标。<br>数据来源：整网规划<br>取值范围：1~3<br>系统初始设置值：1 |
| DC | QoS延迟等级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定2G SMS QoS延迟等级指标。<br>数据来源：整网规划<br>取值范围：1~4<br>系统初始设置值：1 |
| PT | QoS最大吞吐量 | 可选必选说明：可选参数<br>参数含义：该参数用于指定2G SMS QoS最大吞吐量指标。<br>数据来源：整网规划<br>取值范围：1~9<br>系统初始设置值：9 |
| MT | QoS平均吞吐量 | 可选必选说明：可选参数<br>参数含义：该参数用于指定2G SMS QoS平均吞吐量指标。<br>数据来源：整网规划<br>取值范围：1~18<br>系统初始设置值：18 |
| SMSMRT | 短消息最大试发次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定短消息最大重发次数。<br>数据来源：整网规划<br>取值范围：1~3<br>系统初始设置值：3 |
| TR1 | SMMO等待RP_ACK定时器（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMMO流程中等待短消息中心返回响应消息RP_ACK的时间。<br>数据来源：整网规划<br>取值范围：1000~65535<br>系统初始设置值：20000 |
| TR2 | SMMO等待CP_ACK定时器（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMMO流程中等待手机返回响应消息CP_ACK的时间。<br>数据来源：整网规划<br>取值范围：1000~65535<br>系统初始设置值：6500 |
| TR3 | SMMT等待CP_ACK定时器（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMMT流程中等待手机返回响应消息CP_ACK的时间。<br>数据来源：整网规划<br>取值范围：1000~65535<br>系统初始设置值：6500 |
| TR4 | SMMT等待CP_DATA定时器（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMMT流程中等待手机返回响应消息CP_DATA的时间。<br>数据来源：整网规划<br>取值范围：1000~65535<br>系统初始设置值：10000 |
| RSMSCT | S-SMO-CDR中记录的短消息中心 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S-SMO-CDR中记录短消息中心号码的方式。<br>数据来源：整网规划<br>取值范围：<br>- “BEFORECORRECT(请求的短消息中心)”<br>- “AFTERCORRECT(纠正的短消息中心)”<br>系统初始设置值：<br>“BEFORECORRECT(请求的短消息中心)” |
| SMSODBSCHEME | SMS ODB 限制方案 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMS ODB（Operator-Determined-Barring） 限制方案 。<br>数据来源：整网规划<br>取值范围：<br>- “DESTNUM(根据目的号码限制)”<br>- “SMSCNUM(根据短信中心号码限制)”<br>系统初始设置值：<br>“DESTNUM(根据目的号码限制)” |

## 操作的配置对象

- [SMS配置信息（SMS）](configobject/UNC/20.15.2/SMS.md)

## 使用实例

设置SMS表里的数据：

SET SMS: RC=1, PRI=1, DC=1, PT=9, MT=18, SMSMRT=3, TR1=20000, TR2=6500, TR3=6500, TR4=20000, RSMSCT=BEFORECORRECT, SMSODBSCHEME=DESTNUM;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SMS配置信息(SET-SMS)_72345329.md`
