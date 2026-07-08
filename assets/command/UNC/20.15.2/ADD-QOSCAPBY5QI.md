---
id: UNC@20.15.2@MMLCommand@ADD QOSCAPBY5QI
type: MMLCommand
name: ADD QOSCAPBY5QI（增加基于5QI的QosFlow QoS限制配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: QOSCAPBY5QI
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 基于IMSI号段的QoS管理
- 基于5QI的Qos Flow QoS限制配置
status: active
---

# ADD QOSCAPBY5QI（增加基于5QI的QosFlow QoS限制配置）

## 功能

**适用NF：SMF**

该命令用于增加基于5QI的QosFlow QoS限制的相关配置参数。

## 注意事项

- 命令执行后只对新接入用户生效。

- 最多可输入2048条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数表示用于QosFlow QoS限制配置的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- INVALIDSUBRANGE（无效的用户范围）<br>- IMSI_PREFIX（指定IMSI前缀的用户）<br>- VISITING（拜访用户）<br>- ROAMING（漫游用户）<br>- HOME_USER（本网用户）<br>- ALL_USER（所有用户）<br>- HOME_NOLOCAL_USER（本网非本省用户）<br>默认值：无<br>配置原则：<br>“SUBRANGE（用户范围）”的优先级从高到低为：“IMSI_PREFIX（指定IMSI前缀）”，"HOME_NOLOCAL_USER"（本网非本省用户），“HOME_USER（本网用户）”或“ROAMING（漫游用户）”或“VISITING（拜访用户）”，“ALL_USER（所有用户）”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于系统根据对用户的IMSI前缀进行匹配，从而区分不同的用户群。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| QOS5QI | 标准5QI | 可选必选说明：必选参数<br>参数含义：该参数用于指定系统对用户QosFlow的5QI限制。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |
| QOS5QIPL | 5QI的优先级别 | 可选必选说明：可选参数<br>参数含义：该参数表示5QI优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~127。<br>默认值：无<br>配置原则：无 |
| ARPPRL | ARP的优先级别 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户的ARP优先级别限制。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |
| ARPPCI | ARP的抢占能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户的ARP抢占能力限制。<br>数据来源：全网规划<br>取值范围：<br>- INVALID（无效的ARPPCI）<br>- “MAY_PREEMPT（抢占）”：允许该承载抢占其他ARP的优先级别较低的承载的资源<br>- “NOT_PREEMPT（不抢占）”：不允许该承载抢占其他ARP的优先级别较低的承载的资源<br>默认值：无<br>配置原则：无 |
| ARPPVI | ARP的被抢占能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户的ARP被抢占能力限制。<br>数据来源：全网规划<br>取值范围：<br>- INVALID（无效的ARPPVI）<br>- “PREEMPTABLE（可抢占）”：允许其他优先级别较高的承载抢占该承载的资源。<br>- “NOT_PREEMPTABLE（不可抢占）”：不允许其他优先级别较高的承载抢占该承载的资源<br>默认值：无<br>配置原则：无 |
| MFBRUL | 上行最大速率 (千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的GBR QoS Flow的上行最大速率。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65000000。<br>默认值：无<br>配置原则：<br>该参数在“QOS5QI”取值为GBR类型才生效。 |
| MFBRDL | 下行最大速率 (千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的GBR QoS Flow的下行最大速率。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65000000。<br>默认值：无<br>配置原则：<br>该参数在“QOS5QI”取值为GBR类型才生效。 |
| GFBRUL | 上行保证速率 (千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的GBR QoS Flow的上行保证速率。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65000000。<br>默认值：无<br>配置原则：<br>该参数在“QOS5QI”取值为GBR类型才生效。 |
| GFBRDL | 下行保证速率 (千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的GBR QoS Flow的下行保证速率。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65000000。<br>默认值：无<br>配置原则：<br>该参数在“QOS5QI”取值为GBR类型才生效。 |

## 操作的配置对象

- [基于5QI的QosFlow QoS限制配置。（QOSCAPBY5QI）](configobject/UNC/20.15.2/QOSCAPBY5QI.md)

## 使用实例

增加基于5QI的QosFlow QoS限制配置，用户范围为“IMSI_PREFIX”，IMSI前缀为“3080107000”，QOS5QI为“9”，5QI的优先级别为“10”，ARP的优先级别为“5”，ARP的抢占能力为“Not Preempt”，ARP的被抢占能力为“Preemptable”：

```
ADD QOSCAPBY5QI:SUBRANGE=IMSI_PREFIX, IMSIPRE="3080107000", QOS5QI=9,QOS5QIPL=10,ARPPRL=5,ARPPCI=NOT_PREEMPT,ARPPVI=PREEMPTABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加基于5QI的QosFlow-QoS限制配置（ADD-QOSCAPBY5QI）_76079620.md`
