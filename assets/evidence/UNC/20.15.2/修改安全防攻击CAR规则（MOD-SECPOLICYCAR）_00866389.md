# 修改安全防攻击CAR规则（MOD SECPOLICYCAR）

- [命令功能](#ZH-CN_CONCEPT_0000001600866389__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600866389__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600866389__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600866389__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600866389__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600866389)

该命令用来修改报文CAR动作规则。

#### [注意事项](#ZH-CN_CONCEPT_0000001600866389)

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600866389)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600866389)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：必选参数<br>参数含义：策略编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无 |
| SECPOLICYTYPE | 安全策略类型 | 可选必选说明：必选参数<br>参数含义：安全策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Tcpip：TCP/IP策略。<br>- WhiteList：白名单策略。<br>- BlackList：黑名单策略。<br>- Index：索引策略。<br>- UserFlow：用户自定义流策略。<br>- Protocol：协议策略。<br>- WhiteListV6：IPv6白名单。<br>默认值：无 |
| SECPOLICYTYPEID | 安全策略类型编号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“Index” 或 “UserFlow”时为必选参数。<br>参数含义：安全策略类型编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：<br>- 需要根据LST SECPOLICYCAR查看对应的ID。<br>- 如果SECPOLICYTYPE选择Tcpip/Protocol/WhiteList/BlackList/WhiteListV6，则本项不选。如果SECPOLICYTYPE选择Index/UserFlow则本项必选。<br>- 如果SECPOLICYTYPE选择Index，需要根据DSP SECCARINFO查看安全CAR系统ID并在[35，1658]区间，[125，158]区间除外。如果SECPOLICYTYPE选择UserFlow，本参数在[1，32]之间。 |
| SECPOLICYCIR | 安全策略承诺信息速率 | 可选必选说明：可选参数<br>参数含义：策略承诺信息速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1000000。<br>默认值：无 |
| SECPOLICYCBS4SH | 安全策略承诺突发尺寸 | 可选必选说明：可选参数<br>参数含义：策略承诺突发尺寸。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～9000000。<br>默认值：无 |
| SECMINPKTLEN | 安全最小包补偿长度 | 可选必选说明：可选参数<br>参数含义：最小包补偿长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～9600。<br>默认值：无 |
| SUBPROTOTYPE | 安全协议类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“Protocol”时为必选参数。<br>参数含义：协议类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- bfd：BFD协议。<br>- bgp：BGP协议。<br>- icmp：ICMP协议。<br>- ldp：LDP协议。<br>- ospf：OSPF协议。<br>- arp：ARP协议。<br>- arp-miss：ARP-MISS消息。<br>- gre：GRE协议。<br>- ssh_server：SSH服务器。<br>- ssh_client：SSH客户端。<br>- dhcp：DHCP协议。<br>- dhcpv6：DHCPv6协议。<br>- pim：PIM协议。<br>- igmp：IGMP协议。<br>- ipv4-reserved-mc：IPv4默认保留组播报文。<br>- ipv6-too-big：IPv6超大报文。<br>- ipv4-mc-fib-miss：IPv4组播转发表项MISS协议。<br>- bgpv6：BGPv6报文。<br>- icmpv6：ICMPv6协议。<br>- ospfv3：OSPFv3报文。<br>- na：NA报文。<br>- ns：NS报文。<br>- ra：RA报文。<br>- rs：RS报文。<br>- mld：MLD报文。<br>- ipv6-nd-miss：IPv6 ND-MISS消息。<br>- ipv6-ndh-miss：IPv6 NDH-MISS消息。<br>默认值：无<br>配置原则：如果SECPOLICYTYPE选择Protocol，则此项必选其一。 |
| SUBTCPIPTYPE | 安全TCP/IP类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“Tcpip”时为必选参数。<br>参数含义：TCP/IP防攻击类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TCPSYN：TCPSYN报文。<br>- FRAGMENT：分片报文。<br>默认值：无<br>配置原则：SECPOLICYTYPE选择Tcpip，则此项必选其一，且该参数枚举值必须与ADD SECPOLICYCAR命令对应的枚举值相同。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600866389)

修改一个安全CAR规则：

```
MOD SECPOLICYCAR: SECPOLICYID=1, SECPOLICYTYPE=Tcpip, SECPOLICYCIR=150, SUBTCPIPTYPE=FRAGMENT;
```
