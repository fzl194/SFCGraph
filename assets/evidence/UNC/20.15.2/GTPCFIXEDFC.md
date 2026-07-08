# 设置指定消息类型固定速率流控信息（SET GTPCFIXEDFC）

- [命令功能](#ZH-CN_MMLREF_0000001135636465__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001135636465__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001135636465__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001135636465__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001135636465)

![](设置指定消息类型固定速率流控信息（SET GTPCFIXEDFC）_35636465.assets/notice_3.0-zh-cn_2.png)

存在较大操作风险，执行不当会导致业务受损或中断。

**适用NF：SGW-C、PGW-C**

设置指定消息类型的固定速率门限，超过门限的消息将会被UNC丢弃，以减少其它网元对UNC的信令冲击，以及UNC对周边网元的信令冲击。

## [注意事项](#ZH-CN_MMLREF_0000001135636465)

- 该命令执行后立即生效。

- 当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MSGTYPE | FCSWITCH | THRESHOLD |
| --- | --- | --- |
| CREATESESSIONREQUEST | ON | 1200 |
| MODIFYBEARERREQUEST | ON | 15000 |
| ALLMSGTYPE | ON | 30000 |

#### [操作用户权限](#ZH-CN_MMLREF_0000001135636465)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001135636465)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGTYPE | 流控消息类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置GTP-C接口被流控的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- “CREATESESSIONREQUEST（Create Session Request）”：表示Create Session Request消息<br>- “MODIFYBEARERREQUEST（Modify Bearer Request）”：表示Modify Bearer Request消息<br>- “ALLMSGTYPE（All Message Type）”：表示所有消息类型<br>默认值：无。<br>配置原则：无 |
| FCSWITCH | 固定速率流控开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置指定消息类型流控功能开关。<br>数据来源：全网规划<br>取值范围：<br>- “ON（开启）”：开启GTP-C接口的“固定速率流控”功能。<br>- “OFF（关闭）”：关闭GTP-C接口的“固定速率流控”功能。<br>默认值：无。<br>配置原则：<br>当希望开启指定消息类型流控功能时，设置为"ON"；当希望关闭指定消息类型流控功能时，设置为"OFF"。 |
| THRESHOLD | 流控速率门限(个/秒) | 可选必选说明：该参数在"FCSWITCH"配置为"ON"时为条件必选参数。<br>参数含义：该参数用于设置单sm-pod指定消息的接收流控速率上限。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~1000000。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GTPCFIXEDFC查询当前参数配置值。<br>配置原则：<br>该参数按sm-pod单POD粒度设置。 |

## [使用实例](#ZH-CN_MMLREF_0000001135636465)

针对的Create Session Request开启固定速率流控，速率门限是单sm-pod 4000个/秒。执行如下命令：

```
SET GTPCFIXEDFC:MSGTYPE=CREATESESSIONREQUEST,FCSWITCH=ON,THRESHOLD=4000;
```
