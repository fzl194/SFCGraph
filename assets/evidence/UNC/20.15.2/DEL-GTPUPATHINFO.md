# 删除GTPU路径（DEL GTPUPATHINFO）

- [命令功能](#ZH-CN_MMLREF_0000001214280394__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001214280394__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001214280394__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001214280394__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001214280394)

![](删除GTPU路径（DEL GTPUPATHINFO）_14280394.assets/notice_3.0-zh-cn_2.png)

执行该命令会删除GTPU路径，影响基于该接口的业务，可能会引起业务呼损。

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于手动删除GTPU路径。

## [注意事项](#ZH-CN_MMLREF_0000001214280394)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001214280394)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001214280394)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DELETETYPE | 删除类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定删除GTPU路径数据的参数类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL（所有路径）<br>- IPADDR（对端GTPU地址）<br>- NFINSTANCENAME（UP唯一标识）<br>默认值：无<br>配置原则：无 |
| ID | UPF实例名称 | 可选必选说明：该参数在"DELETETYPE"配置为"NFINSTANCENAME"时为条件必选参数。<br>参数含义：该参数用于指定UPF的实例名称，用于唯一标识一个UP。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：该参数在"DELETETYPE"配置为"IPADDR"时为条件必选参数。<br>参数含义：该参数用于指定GTPU的IP类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：无 |
| IPADDRV4 | 对端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定GTPU对端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPADDRV6 | 对端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定GTPU对端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001214280394)

如需要删除对端地址为10.0.0.1的GTPU路径。

```
DEL GTPUPATHINFO: DELETETYPE=IPADDR, IPTYPE=IPV4, IPADDRV4="10.0.0.1";
```
