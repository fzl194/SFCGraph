---
id: UDG@20.15.2@MMLCommand@OPR FEIEXTPORTPKTDEBUGRULE
type: MMLCommand
name: OPR FEIEXTPORTPKTDEBUGRULE（设置外联口报文调测规则）
nf: UDG
version: 20.15.2
verb: OPR
object_keyword: FEIEXTPORTPKTDEBUGRULE
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 外联口报文调测
status: active
---

# OPR FEIEXTPORTPKTDEBUGRULE（设置外联口报文调测规则）

## 功能

在报文调测的场景中，该命令用于设置外联口报文调测规则。

## 注意事项

- 跨层联动抓包、外联口抓包功能和染色跟踪功能不可以同时开启，否则可能导致功能无法正常使用。
- 每次报文调测结束后，将会在报文调测文件插入一个源mac、目的mac地址为全0的空报文，该报文中写入了因流控而未抓取的报文数量，若报文为全0表示未触发流控。
- 在外联口报文速率较高的场景下可能触发全流控，即流控后此次任务无法再匹配到报文。可以通过上述的空报文查看流控具体情况。
- 在填写命令参数时，源IP、源端口及其掩码应填写对端的IP、端口及其掩码信息，目的IP、目的端口及其掩码应填写本端的IP、端口及其掩码信息。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULEID | 规则ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示外联口报文调测的规则ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～2。<br>默认值：无 |
| OPERATE | 操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示外联口报文调测的操作类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Add：添加规则。<br>- Delete：删除规则。<br>默认值：无 |
| PKTTYPE | 报文类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“OPERATE”配置为“Add”时为必选参数。<br>参数含义：该参数用于表示外联口报文调测的报文类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- All：所有报文。此时不允许配置TUNNELLEN和INNERETHLEN。<br>- IPv4：IPv4报文。TUNNELLEN不配置或配置为0时，表示外层报文类型；否则表示内层报文类型。<br>- IPv6：IPv6报文。TUNNELLEN不配置或配置为0时，表示外层报文类型；否则表示内层报文类型。<br>- EtherType：指定以太类型的报文。TUNNELLEN不配置或配置为0时，表示外层报文类型；否则表示内层报文类型，此时不能指定IP及端口信息。<br>默认值：无 |
| PROTOCOLV4 | IPv4应用层协议 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于表示外联口报文调测的IPv4应用层协议。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- All：所有报文。<br>- ProtocolID：指定协议ID。<br>- ProtocolType：指定协议类型。<br>默认值：无 |
| PROTOCOLV6 | IPv6应用层协议 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于表示外联口报文调测的IPv6应用层协议。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- All：所有报文。<br>- ProtocolID：指定协议ID。<br>- ProtocolType：指定协议类型。<br>默认值：无 |
| PROTOCOLTYPEV4 | IPv4应用层协议类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLV4”配置为“ProtocolType”时为必选参数。<br>参数含义：该参数用于表示外联口报文调测的IPv4应用层协议类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ospf：OSPF报文。<br>- icmp：ICMP报文。<br>- igmp：IGMP报文。<br>- gre：GRE报文。<br>- ipinip：IPINIP报文。<br>- tcp：TCP报文。<br>- udp：UDP报文。<br>默认值：无 |
| PROTOCOLTYPEV6 | IPv6应用层协议类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLV6”配置为“ProtocolType”时为必选参数。<br>参数含义：该参数用于表示外联口报文调测的IPv6应用层协议类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- grev6：GREv6报文。<br>- hop-by-hop：HOP-BY-HOP报文。<br>- icmpv6：ICMPv6报文。<br>- ipv6-ah：IPv6-AH报文。<br>- ipv6-esp：IPv6-ESP报文。<br>- ospfv3：OSPFv3报文。<br>- tcp：TCP报文。<br>- udp：UDP报文。<br>默认值：无 |
| PROTOID | 协议号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLV4”配置为“ProtocolID”时为必选参数。<br>可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLV6”配置为“ProtocolID”时为必选参数。<br>参数含义：该参数用于表示外联口报文调测的协议号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |
| SRCIP | 源IP | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPv4”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的源IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| SRCIPMASK | 源IP掩码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPv4”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的源IPv4地址掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| DESTIP | 目的IP | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPv4”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的目的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| DESTIPMASK | 目的IP掩码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPv4”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的目的IPv4地址掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| SRCIPV6 | 源IPv6 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPv6”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的源IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| SRCIPV6MASKLEN | 源IPv6前缀长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPv6”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的源IPv6地址前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无<br>配置原则：如果不设置该参数，则外联口报文调测规则不指定源IPv6前缀长度。 |
| DESTIPV6 | 目的IPv6 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPv6”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的目的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| DESTIPV6MASKLEN | 目的IPv6前缀长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPv6”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的目的IPv6地址前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无<br>配置原则：如果不设置该参数，则外联口报文调测规则不指定目的IPv6前缀长度。 |
| SRCPORT | 源端口 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOLTYPEV4”配置为“udp” 或 “tcp”时为可选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOLTYPEV6”配置为“udp” 或 “tcp”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的源端口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：如果不设置该参数，则外联口报文调测规则不指定源端口。 |
| SRCPORTMASK | 源端口掩码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOLTYPEV4”配置为“udp” 或 “tcp”时为可选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOLTYPEV6”配置为“udp” 或 “tcp”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的源端口掩码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：如果不设置该参数，则外联口报文调测规则不指定源端口掩码。 |
| DESTPORT | 目的端口 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOLTYPEV4”配置为“udp” 或 “tcp”时为可选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOLTYPEV6”配置为“udp” 或 “tcp”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的目的端口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：如果不设置该参数，则外联口报文调测规则不指定目的端口。 |
| DESTPORTMASK | 目的端口掩码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOLTYPEV4”配置为“udp” 或 “tcp”时为可选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOLTYPEV6”配置为“udp” 或 “tcp”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的目的端口掩码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：如果不设置该参数，则外联口报文调测规则不指定目的端口掩码。 |
| ETHERTYPE | 以太类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PKTTYPE”配置为“EtherType”时为必选参数。<br>参数含义：该参数用于表示外联口报文调测的以太类型值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| TUNNELLEN | 内层报文头相对于外层IP头的偏移量 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPv4”、“IPv6” 或 “EtherType”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的内层报文头相对于外层IP头的偏移量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| INNERETHLEN | 内层ETH头长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPv4”、“IPv6” 或 “EtherType”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的内层ETH头长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FEIEXTPORTPKTDEBUGRULE]] · 外联口报文调测规则（FEIEXTPORTPKTDEBUGRULE）

## 使用实例

设置外联口报文调测规则：

```
OPR FEIEXTPORTPKTDEBUGRULE: RULEID=1, OPERATE=Add, PKTTYPE=IPv4, PROTOCOLV4=ProtocolType, PROTOCOLTYPEV4=tcp, SRCIP="192.168.1.1", SRCIPMASK="255.255.255.0", DESTIP="192.168.1.2", DESTIPMASK="255.255.255.0", SRCPORT=100, SRCPORTMASK=65535, DESTPORT=200, DESTPORTMASK=65535, TUNNELLEN=0, INNERETHLEN=0;
RETCODE = 0  操作成功。
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置外联口报文调测规则（OPR-FEIEXTPORTPKTDEBUGRULE）_00600837.md`
