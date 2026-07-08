# 清除接收方向协议报文统计计数（RTR HOSTRCVSTC）

- [命令功能](#ZH-CN_CONCEPT_0000001550281042__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550281042__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550281042__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550281042__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550281042__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550281042)

该命令用于清除接收方向协议报文统计计数。

当清除类型为IF_STC，不指定PROTTYPE参数时，清除所有协议类型的统计信息；当指定PROTTYPE参数时，可以清除指定协议类型的统计信息。

当清除类型为PROT_STC，不指定IFNAME参数时，清除所有接口的统计信息；当指定IFNAME参数时，可以清除指定接口的统计信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001550281042)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550281042)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550281042)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RSTTYPE | 清除类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示清除类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IF_STC：接口上指定协议类型的报文统计信息。<br>- PROT_STC：接口上各协议类型的报文统计信息。<br>默认值：无 |
| IFNAME | 接口名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“RSTTYPE”配置为“PROT_STC”时为可选参数。<br>参数含义：该参数用于表示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| PROTTYPE | 协议类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“RSTTYPE”配置为“IF_STC”时为可选参数。<br>参数含义：该参数用于表示协议类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ARP：ARP协议类型。<br>- STP：STP协议类型。<br>- LACP：LACP协议类型。<br>- LLDP：LLDP协议类型。<br>- ISIS：ISIS协议类型。<br>- LINK_OTHER：其它链路层协议类型。<br>- ICMP：ICMP协议类型。<br>- OSPF：OSPF协议类型。<br>- PIM：PIM协议类型。<br>- IGMP：IGMP协议类型。<br>- VRRP：VRRP协议类型。<br>- RAWIP_OTHER：其它RawIP协议类型。<br>- SNMP：SNMP协议类型。<br>- DHCP：DHCP协议类型。<br>- UDP_OTHER：其它UDP协议类型。<br>- BGP：BGP协议类型。<br>- LDP：LDP协议类型。<br>- TCP_OTHER：其它TCP协议类型。<br>- ICMPV6：ICMPv6协议类型。<br>- OSPFV3：OSPFv3协议类型。<br>- PIMV6：PIMv6协议类型。<br>- MLD：MLD协议类型。<br>- VRRPV6：VRRPv6协议类型。<br>- RAWIPV6_OTHER：其它RawIPv6协议类型。<br>- SNMPV6：SNMPv6协议类型。<br>- DHCPV6：DHCPv6协议类型。<br>- IPV6UDP_OTHER：其它IPv6 UDP协议类型。<br>- BGP4PLUS：BGP4PLUS协议类型。<br>- LDPV6：LDPv6协议类型。<br>- IPV6TCP_OTHER：其它IPv6 TCP协议类型。<br>默认值：无<br>配置原则：如果不输入该参数，则表示所有协议类型。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001550281042)

- 清除接收方向所有接口上的协议报文统计计数：
  ```
  RTR HOSTRCVSTC: RSTTYPE=PROT_STC;
  ```
- 清除接收方向指定接口上的协议报文统计计数：
  ```
  RTR HOSTRCVSTC: RSTTYPE=PROT_STC, IFNAME="GigabitEthernet0/0/1";
  ```
- 清除接收方向指定协议类型的协议报文统计计数：
  ```
  RTR HOSTRCVSTC: RSTTYPE=IF_STC, PROTTYPE=ARP;
  ```
