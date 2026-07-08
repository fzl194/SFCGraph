---
id: UDG@20.15.2@License@LKV3G5V6NF01
type: License
name: N6/Gi/SGi接口IPv6组网
nf: UDG
version: 20.15.2
license_code: LKV3G5V6NF01
control_item_id: '81203213'
license_domain: UDG
control_item_type: function
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# N6/Gi/SGi接口IPv6组网

`LKV3G5V6NF01` · 控制项 81203213 · function · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

UDG<br>支持在PDN侧基于IPv6（Internet Protocol Version 6）技术的组网，连接PDN网络的物理接口可以配置为IPv6地址，同时还支持PMTU（Path Maximum Transmission Unit）探测及IPv6动态路由协议，包括OSPFv3、ISIS IPv6和BGP4+。

## 实现描述

PMTU<br>PMTU是从源端到目的端路径上合适的IPv6 MTU值，源端按照该值发送报文，使得报文在整个传输过程中不需要分片，减轻中间路由设备的工作压力，以便有效地利用网络资源并得到最佳的吞吐量。<br>UDG<br>支持以下两种方式确定PMTU：<br>- 手工配置静态PMTUUDG<br>支持为指定的目的IPv6地址配置静态的PMTU值。当<br>UDG<br>从接口发送报文时，将比较该接口的MTU与指定目的IPv6地址的静态PMTU值，当报文长度大于二者中最小值时，采用该最小值对报文进行分片。<br>- PMTU发现（Path MTU Discovery）UDG<br>支持源端到目的端PMTU的动态发现，源端使用这个MTU值发送后续报文到目的端。<br>UDG<br>支持PMTU老化时间的配置，当老化时间到达时，动态确定的PMTU值将被删除，源端通过PMTU发现机制重新确定发送报文的MTU值。<br>PMTU发现的工作过程是：源端主机先使用自己的MTU值向目的主机发送报文，如果中间路由设备给源端返回一个错误消息，其中包括该设备的MTU值，源端主机使用该MTU值来重新发送这个报文，如此反复，直到目的端主机收到这个报文，从而确定网络中两台主机之间能够处理的最大报文的大小。在PMTU发现过程结束之前，可能会出现反复发送报文和收到报文太大消息，这是因为可能会不断发现更远的路径链路有更小的IPv6 MTU。<br>IPv6路由<br>UDG<br>支持以下几种IPv6路由协议：<br>- IPv6静态路由IPv6静态路由与IPv4静态路由类似，适合于结构比较简单的IPv6网络。主要区别是目的地址和下一跳地址不同，IPv6静态路由使用IPv6地址，IPv4静态路由使用IPv4地址。<br>- OSPFv3OSPFv3是OSPF（Open Shortest Path First）版本3的简称，主要提供对IPv6的支持，遵循的标准为RFC2740（OSPF for IPv6）。<br>- ISIS IPv6支持IPv6路由的处理和计算。主要是新添加的支持IPv6路由信息的两个TLVs（Type-Length- Values）和一个新的NLPID（Network Layer Protocol Identifier）。新增的两个TLV分别是：- IPv6 Reachability类型值为236（0xEC），通过定义路由信息前缀、度量值等信息来说明网络的可达性。<br>- IPv6 Interface Address类型值为232（0xE8），它相当于IPv4中的“IP Interface Address”TLV，只不过把原来的32比特的IPv4地址改为128比特的IPv6地址。NLPID是标识网络层协议报文的一个8比特字段，IPv6的NLPID值为142（0x8E）。如果IS-IS支持IPv6，那么向外发布IPv6路由时必须携带NLPID值。<br>- BGP4+BGP4+是一种用于自治系统AS（Autonomous System）之间的动态路由协议，它是对BGP的扩展。传统的BGP4只能管理IPv4的路由信息，对于使用其它网络层协议（如IPv6等）的应用，在跨自治系统传播路由信息时就受到一定限制。为了提供对多种网络层协议的支持，IETF对BGP4进行了扩展，形成BGP4+，目前的BGP4+标准是RFC2858（Multiprotocol Extensions for BGP-4，BGP-4多协议扩展）。为了实现对IPv6协议的支持，BGP4+需要将IPv6协议的信息反映到NLRI（Network Layer Reachable Information）属性及Next_Hop属性中。BGP4+中引入的两个NLRI属性分别是：- MP_REACH_NLRI：Multiprotocol Reachable NLRI，多协议可达NLRI。用于发布可达路由及下一跳信息。<br>- MP_UNREACH_NLRI：Multiprotocol Unreachable NLRI，多协议不可达NLRI。用于撤销不可达路由。BGP4+中的Next_Hop属性用IPv6地址来表示，可以是IPv6全球单播地址或者下一跳的链路本地单播地址。BGP4+利用BGP的多协议扩展属性，达到在IPv6网络中应用的目的，BGP协议原有的消息机制和路由机制并没有改变。

## 取值范围

0～1

## 默认值

1

## 应用场景

开展IPv6业务应用。解决IPv4地址枯竭问题。

## 相关控制项（原文，未解释为边）

IPv6承载上下文

## 对应特性（原文）

GWFD-020402 N6/Gi/SGi接口IPv6组网

## 控制的能力

- [GWFD-020402](feature/UDG/20.15.2/GWFD-020402.md)  — 控制项 81203213

## 证据

- 原始手册：`evidence/UDG/20.15.2/功能控制项_69147292.md`
