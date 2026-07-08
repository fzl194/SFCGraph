# 设置指定PFCP消息类型固定速率流控信息（SET PFCPFIXEDFC）

- [命令功能](#ZH-CN_MMLREF_0000001520015330__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001520015330__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001520015330__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001520015330__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001520015330)

**适用NF：SMF**

设置指定PFCP消息的固定速率门限。

## [注意事项](#ZH-CN_MMLREF_0000001520015330)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MSGTYPE | FCSWITCH | THRESHOLD |
| --- | --- | --- |
| HEARTBEATREQ | ON | 500 |
| HEARTBEATRSP | ON | 500 |
| ASSOCIATIONSETUPREQ | ON | 500 |
| ASSOCIATIONSETUPRSP | ON | 500 |
| ASSOCIATIONUPDATEREQ | ON | 500 |
| ASSOCIATIONUPDATERSP | ON | 500 |
| ASSOCIATIONRELEASEREQ | ON | 500 |
| ASSOCIATIONRELEASERSP | ON | 500 |
| NOTSUPPORTRSP | ON | 500 |
| NODEREPORTREQ | ON | 500 |
| NODEREPORTRSP | ON | 500 |

#### [操作用户权限](#ZH-CN_MMLREF_0000001520015330)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001520015330)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGTYPE | 流控消息类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置被流控的PFCP消息类型。<br>数据来源：全网规划<br>取值范围：<br>- HEARTBEATREQ（心跳请求）<br>- HEARTBEATRSP（心跳响应）<br>- ASSOCIATIONSETUPREQ（偶联建立请求）<br>- ASSOCIATIONSETUPRSP（偶联建立响应）<br>- ASSOCIATIONUPDATEREQ（偶联更新请求）<br>- ASSOCIATIONUPDATERSP（偶联更新响应）<br>- ASSOCIATIONRELEASEREQ（偶联释放请求）<br>- ASSOCIATIONRELEASERSP（偶联释放响应）<br>- NOTSUPPORTRSP（版本不支持响应）<br>- NODEREPORTREQ（节点上报请求）<br>- NODEREPORTRSP（节点上报响应）<br>默认值：无。<br>配置原则：无 |
| FCSWITCH | 固定速率流控开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制是否开启指定PFCP消息类型固定速率流控功能。<br>数据来源：全网规划<br>取值范围：<br>- OFF（关闭）<br>- ON（开启）<br>默认值：无。<br>配置原则：<br>当希望开启指定消息类型流控功能时，设置为"On"；当希望关闭指定消息类型流控功能时，设置为"Off"。 |
| THRESHOLD | 流控速率门限(个/秒) | 可选必选说明：该参数在"FCSWITCH"配置为"ON"时为条件必选参数。<br>参数含义：该参数用于设置指定PFCP消息的流控速率上限。该参数针对单POD指定消息类型进行流控。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~100000。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PFCPFIXEDFC查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001520015330)

针对HEARTBEATREQ消息类型开启固定速率流控，速率门限是单POD 500个/秒，执行如下命令：

```
%%SET PFCPFIXEDFC: MSGTYPE= HEARTBEATREQ, FCSWITCH=ON, THRESHOLD=500;%%
RETCODE = 0  操作成功

---    END
```
