---
id: UNC@20.15.2@MMLCommand@ADD SMFALLOWEDARPS
type: MMLCommand
name: ADD SMFALLOWEDARPS（增加5G用户允许的ARP列表）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SMFALLOWEDARPS
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
- 5GC允许接入的ARPs
status: active
---

# ADD SMFALLOWEDARPS（增加5G用户允许的ARP列表）

## 功能

**适用NF：SMF**

该命令用于配置5G用户允许接入的ARP列表。当产品作为V-SMF/I-SMF形态时，通过该配置可以实现QoS管控功能。

## 注意事项

- 命令执行后只对新接入用户生效。

- 最多可输入2048条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSINDEX | 用户QOS索引 | 可选必选说明：必选参数<br>参数含义：该参数表示允许用户接入的ARP列表索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| ARPPL | ARP的优先级别 | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的ARP优先级。<br>数据来源：全网规划<br>取值范围：本配置采用白名单机制，如果不配本参数，则表示不允许接入。<br>- ARPPL1（ARP优先级别1）<br>- ARPPL2（ARP优先级别2 ）<br>- ARPPL3（ARP优先级别3）<br>- ARPPL4（ARP优先级别4）<br>- ARPPL5（ARP优先级别5）<br>- ARPPL6（ARP优先级别6）<br>- ARPPL7（ARP优先级别7）<br>- ARPPL8（ARP优先级别8）<br>- ARPPL9（ARP优先级别9）<br>- ARPPL10（ARP优先级别10）<br>- ARPPL11（ARP优先级别11）<br>- ARPPL12（ARP优先级别12）<br>- ARPPL13（ARP优先级别13）<br>- ARPPL14（ARP优先级别14）<br>- ARPPL15（ARP优先级别15）<br>默认值：无<br>配置原则：无 |
| ARPPCI | ARP的抢占能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的ARP抢占能力。<br>数据来源：全网规划<br>取值范围：本配置采用白名单机制，如果不配本参数，则表示不允许接入。<br>- NOT_PREEMPT（不抢占）<br>- MAY_PREEMPT（抢占）<br>默认值：无<br>配置原则：无 |
| ARPPVI | ARP的被抢占能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的ARP被抢占能力。<br>数据来源：全网规划<br>取值范围：本配置采用白名单机制，如果不配本参数，则表示不允许接入。<br>- NOT_PREEMPTABLE（不可抢占）<br>- PREEMPTABLE（可抢占）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFALLOWEDARPS]] · 5G用户允许的ARP列表（SMFALLOWEDARPS）

## 使用实例

如果想增加一条"允许用户接入的ARP列表索引"为1，"ARP的优先级别"为ARPPL1的5G用户允许的ARP列表，执行如下命令:

```
ADD SMFALLOWEDARPS:QOSINDEX=1,ARPPL=ARPPL1-1&ARPPL2-0&ARPPL3-0&ARPPL4-0&ARPPL5-0&ARPPL6-0&ARPPL7-0&ARPPL8-0&ARPPL9-0&ARPPL10-0&ARPPL11-0&ARPPL12-0&ARPPL13-0&ARPPL14-0&ARPPL15-0,ARPPCI=MAY_PREEMPT-1,ARPPVI=NOT_PREEMPTABLE-0&PREEMPTABLE-1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SMFALLOWEDARPS.md`
