# 删除SGSN/SGW/PGW地址段和PLMN标识之间的映射关系（RMV SRVNODEPLMN）

- [命令功能](#ZH-CN_MMLREF_0209653257__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653257__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653257__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653257__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209653257)

**适用NF：PGW-C、SGW-C、GGSN**

该命令用来删除映射表中的SGSN/SGW/PGW IP地址的表项。

## [注意事项](#ZH-CN_MMLREF_0209653257)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209653257)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653257)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | ip类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指示IP类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPV4）”：表示地址类型为IPv4。<br>- “IPV6（IPV6）”：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| SRVNODESTARTV4 | Service Node的起始IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于SGSN/SGW/PGW IP地址段的起始IPV4地址，该配置需要和全网规划一致。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>取值范围：0.0.0.0~255.255.255.255。 |
| SRVNODEENDV4 | Service Node的结束IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于SGSN/SGW/PGW IP地址段的结束IPV4地址，该配置需要和全网规划一致。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>取值范围：0.0.0.0~255.255.255.255。 |
| SRVNODESTARTV6 | Service Node的起始IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于设定Serving Node IP地址段的IPv6起始IP地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| SRVNODEENDV6 | Service Node的结束IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于设定Serving Node IP地址段的IPv6结束IP地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653257)

删除SGSN/SGW/PGW地址段和PLMN标识之间的映射关系实例，ip类型为：IPV4，Service Node的起始IPv4地址为：10.111.111.111，Service Node的结束IPv4地址为：10.111.111.255：

```
RMV SRVNODEPLMN: IPVERSION=IPV4, SRVNODESTARTV4="10.111.111.111", SRVNODEENDV4="10.111.111.255";
```
