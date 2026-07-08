# 删除RADIUS中转UPF会话上下文（RMV RDSPFCPCTX）

- [命令功能](#ZH-CN_MMLREF_0000001135072382__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001135072382__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001135072382__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001135072382__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001135072382)

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除RADIUS中转UPF会话上下文。

## [注意事项](#ZH-CN_MMLREF_0000001135072382)

- 该命令执行后立即生效。

- 该命令会立即删除指定的Radius中转UPF会话。指定对端TEID，不指定对端IP地址时，时会删除TEID相关的所有会话。

#### [操作用户权限](#ZH-CN_MMLREF_0000001135072382)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001135072382)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RMVTYPE | 删除方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定删除类型。<br>数据来源：本端规划<br>取值范围：<br>- IPTYPE（Radius客户端IP类型）<br>- PEERTEID（RADIUS中转UPF会话中UPF分配的N4口TEID）<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：该参数在"RMVTYPE"配置为"IPTYPE"时为条件必选参数。<br>参数含义：表示Radius客户端的IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：无 |
| CLIENTIPV4 | Radius客户端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：表示Radius客户端的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CLIENTIPV6 | Radius客户端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：表示Radius客户端的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例名称 | 可选必选说明：该参数在"RMVTYPE"配置为"IPTYPE"时为条件可选参数。<br>参数含义：该参数用于指示VPN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。区分大小写。<br>默认值：无<br>配置原则：无 |
| PEERTEID | 对端TEID | 可选必选说明：该参数在"RMVTYPE"配置为"PEERTEID"时为条件必选参数。<br>参数含义：表示Radius中转UPF会话中UPF分配的N4口TEID。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| PEERIPTYPE | 对端IP类型 | 可选必选说明：该参数在"RMVTYPE"配置为"PEERTEID"时为条件可选参数。<br>参数含义：表示对端IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4类型的地址）<br>- IPV6（IPv6类型的地址）<br>默认值：无<br>配置原则：无 |
| PEERIPV4ADDR | 对端IPv4地址 | 可选必选说明：该参数在"PEERIPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：表示Radius中转Upf会话中Upf分配的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV6ADDR | 对端IPv6地址 | 可选必选说明：该参数在"PEERIPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：表示Radius中转Upf会话中Upf分配的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001135072382)

删除Radius IP为192.168.0.1的session context:

```
RMV RDSPFCPCTX: RMVTYPE=IPTYPE, IPTYPE=IPV4, CLIENTIPV4="192.168.0.1";
```
