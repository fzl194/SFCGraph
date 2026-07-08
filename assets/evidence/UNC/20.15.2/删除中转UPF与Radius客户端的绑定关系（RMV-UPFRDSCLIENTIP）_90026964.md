# 删除中转UPF与Radius客户端的绑定关系（RMV UPFRDSCLIENTIP）

- [命令功能](#ZH-CN_MMLREF_0000001090026964__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001090026964__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001090026964__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001090026964__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001090026964)

![](删除中转UPF与Radius客户端的绑定关系（RMV UPFRDSCLIENTIP）_90026964.assets/notice_3.0-zh-cn_2.png)

删除RADIUS客户端的相关属性可能会导致RADIUS鉴权计费失败等问题。

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除中转UPF与Radius客户端的绑定关系。

## [注意事项](#ZH-CN_MMLREF_0000001090026964)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001090026964)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001090026964)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLIENTYPE | 客户端类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RADIUS客户端类型。<br>数据来源：本端规划<br>取值范围：<br>- “AUTHENTICATION（鉴权客户端）”：表示鉴权客户端。<br>- “ACCOUNTING（计费客户端）”：表示计费客户端。<br>- “ACCT_AND_AUTH（计费和鉴权客户端）”：表示计费和鉴权客户端。<br>默认值：无<br>配置原则：无 |
| IPVERSION | 客户端IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RADIUS客户端IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPv4）”：IPv4<br>- “IPV6（IPv6）”：IPv6<br>默认值：无<br>配置原则：无 |
| CLIENTIPV4 | IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定RADIUS客户端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CLIENTIPV6 | IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定RADIUS客户端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001090026964)

如果想要删除UPF中转RADIUS客户端IP，可以指定客户端类型为鉴权，客户端IP版本为“IPv4”，客户端地址为“192.168.10.1”，例如：

```
RMV UPFRDSCLIENTIP: CLIENTYPE=AUTHENTICATION, IPVERSION=IPV4, CLIENTIPV4="192.168.10.1";
```
