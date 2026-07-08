# 设置报文上送优先级（SET SECPOLICYPRIO）

- [命令功能](#ZH-CN_CONCEPT_0000001600601093__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600601093__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600601093__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600601093__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600601093__1.3.5.1)
- [参考信息](#ZH-CN_CONCEPT_0000001600601093__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600601093)

该命令用来配置报文上送优先级。

当上送CPU的报文队列满时，为保护CPU，可以设置报文上送CPU的优先级，优先上送高优先级的报文。

缺省情况下，上送报文的优先级各不相同，可以使用DSP SECCARINFO命令查看。

#### [注意事项](#ZH-CN_CONCEPT_0000001600601093)

- 该命令执行后立即生效。
- 该命令的设定值可通过LST SECPOLICYPRIO命令进行查询。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600601093)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600601093)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略号 | 可选必选说明：必选参数<br>参数含义：安全策略号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无<br>配置原则：需要先添加安全策略。 |
| SECPOLICYTYPE | 安全策略类型 | 可选必选说明：必选参数<br>参数含义：安全策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Tcpip：TCP/IP。<br>- WhiteList：白名单。<br>- BlackList：黑名单。<br>- Index：索引。<br>- UserFlow：用户自定义流。<br>- Protocol：协议。<br>- WhiteListV6：IPv6白名单。<br>默认值：无 |
| SECPOLICYTYPEID | 安全策略类型号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“UserFlow” 或 “Index”时为必选参数。<br>参数含义：安全策略类型号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：如果SECPOLICYTYPE选择Index，需要根据DSP SECCARINFO查看安全CAR系统ID并在[35，1658]区间，[125，158]区间除外。如果SECPOLICYTYPE选择UserFlow，本参数在[1，32]之间。 |
| SECPRIORITY | 安全优先级 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“Protocol”、“Tcpip”、“UserFlow”、“WhiteList”、“BlackList”、“WhiteListV6” 或 “Index”时为必选参数。<br>参数含义：安全优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- low：低。<br>- middle：中。<br>- high：高。<br>默认值：无 |
| SUBPROTOTYPE | 安全协议类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“Protocol”时为必选参数。<br>参数含义：协议类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- bfd：BFD协议。<br>- bgp：BGP协议。<br>- icmp：ICMP协议。<br>- ldp：LDP协议。<br>- ospf：OSPF协议。<br>- arp：ARP协议。<br>- arp-miss：ARP-MISS消息。<br>- gre：GRE协议。<br>- ssh_server：SSH服务器。<br>- ssh_client：SSH客户端。<br>- dhcp：DHCP协议。<br>- dhcpv6：DHCPv6协议。<br>- pim：PIM协议。<br>- igmp：IGMP协议。<br>- ipv4-reserved-mc：IPv4默认保留组播报文。<br>- ipv6-too-big：IPv6超大报文。<br>- ipv4-mc-fib-miss：IPv4组播转发表项MISS协议。<br>- bgpv6：BGPv6报文。<br>- icmpv6：ICMPv6协议。<br>- ospfv3：OSPFv3报文。<br>- na：NA报文。<br>- ns：NS报文。<br>- ra：RA报文。<br>- rs：RS报文。<br>- mld：MLD报文。<br>- ipv6-nd-miss：IPv6 ND-MISS消息。<br>- ipv6-ndh-miss：IPv6 NDH-MISS消息。<br>默认值：无 |
| SUBTCPIPTYPE | 安全TCP/IP类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“Tcpip”时为必选参数。<br>参数含义：TCP/IP防攻击类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TCPSYN：TCPSYN报文。<br>- FRAGMENT：分片报文。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600601093)

配置报文上送优先级：

```
SET SECPOLICYPRIO: SECPOLICYID=1, SECPOLICYTYPE=Tcpip, SECPRIORITY=low, SUBTCPIPTYPE=TCPSYN;
```

#### [参考信息](#ZH-CN_CONCEPT_0000001600601093)

需要先添加安全策略。
