# GWFD-020406 IPv6 Prefix Delegation特性概述

- [适用NF](#ZH-CN_TOPIC_0279370029__1.3.1.1)
- [定义](#ZH-CN_TOPIC_0279370029__1.3.2.1)
- [客户价值](#ZH-CN_TOPIC_0279370029__1.3.3.1)
- [应用场景](#ZH-CN_TOPIC_0279370029__1.3.4.1)
- [可获得性](#ZH-CN_TOPIC_0279370029__1.3.5.1)
- [与其他特性的交互](#ZH-CN_TOPIC_0279370029__1.3.8.1)
- [对系统的影响](#ZH-CN_TOPIC_0279370029__1.3.9.1)
- [应用限制](#ZH-CN_TOPIC_0279370029__1.3.10.1)
- [原理概述](#ZH-CN_TOPIC_0279370029__1.3.11.1)
- [计费与话单](#ZH-CN_TOPIC_0279370029__1.3.12.1)
- [特性规格](#ZH-CN_TOPIC_0279370029__1.3.13.1)
- [遵循标准](#ZH-CN_TOPIC_0279370029__1.3.14.1)
- [发布历史](#ZH-CN_TOPIC_0279370029__1.3.15.1)

#### [适用NF](#ZH-CN_TOPIC_0279370029)

PGW-U、UPF

#### [定义](#ZH-CN_TOPIC_0279370029)

UDG 支持IPv6 Prefix Delegation功能，以便IPv6移动终端可以作为一个无线移动路由器来使用。

#### [客户价值](#ZH-CN_TOPIC_0279370029)

| **受益方** | **受益描述** |
| --- | --- |
| 运营商 | 基于IPv6场景部署，扩展业务范围，可为用户提供IPv6移动路由器服务，吸引有此类需求的用户。 |
| 用户 | 通过MS/UE（作为无线移动路由器）将多个终端接入网络，帮助家庭或小型企业用户实现移动接入服务。 |

#### [应用场景](#ZH-CN_TOPIC_0279370029)

华为 UDG 支持Routing Behind MS功能，可以满足在IPv4组网条件下通过一台无线设备（MS/UE）将多台终端设备接入网络并与网络侧设备进行双向数据业务的技术方案。

随着IPv6技术的迅猛发展，为了满足在IPv6组网条件下通过一台无线设备（MS/UE）将多台终端设备接入网络并与网络侧设备进行双向数据业务的技术方案，华为 UDG 提供了IPv6 Prefix Delegation功能，为更多的家庭或小型企业用户提供了服务，同时也丰富了IPv6解决方案体系，提供了更为完善的组网方案。

IPv6 Prefix Delegation功能为用户提供两种IPv6 delegated-prefix的分配方式：

- Radius Server分配用户地址、 UDG 上配置前缀小于64位的地址池场景，SMF/PGW-C在会话建立请求中将UE IP Address中Ipv6D flag置位，携带Ipv6 Address并且携带Ipv6 Prefix Delegation Bits field指示Ipv6地址前缀长度。
- PGW-U/UPF分配用户地址场景，PGW-U/UPF上配置Ipv6地址前缀小于64位的地址池，SMF/PGW-C在会话建立请求中将UE IP Address的CHV6置位。PGW-U/UPF在会话建立响应中UE IP Address的Ipv6D flag置位，携带Ipv6 Address和Ipv6 Prefix Delegation Bits field。

> **说明**
> IPv6 Prefix Delegation功能不支持从DHCP Server获取并分配IPv6 delegated-prefix。

**图1** IPv6 Prefix Delegation特性组网结构

<br>

![](GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.assets/zh-cn_image_0292532421.png)

#### [可获得性](#ZH-CN_TOPIC_0279370029)

**涉及NF**

| **涉及NF** | **支持版本** | **功能说明** |
| --- | --- | --- |
| MS/UE | 无特殊要求 | 激活成功后，通过一个PDP/承载上下文/PDU会话获取一个网段地址，用于为与其连接的多台终端设备下发独立的IPv6地址前缀。 |
| PGW-C/SMF | UNC 20.5.0及后续版本 | 与PCF、OCS、CHF等周边网元交互，获取策略控制信息、生成话单等。 |
| PGW-U/UPF | UDG 20.5.0及后续版本 | 对报文进行识别和解析，根据解析结果匹配规则，对不同IPv6业务进行不同的计费和动作处理。 |
| AAA Server | 无特殊要求 | 对用户进行接入鉴权，并且在系统采用RADIUS地址分配方式的时候，为用户分配IPv6地址前缀和IPv6 delegated-prefix。 |

**License** **支持**

本特性只有获得了License许可后才能获得该特性的服务，对应的License控制项为 “82200CKF LKV3G5P6PD01 IPv6 Prefix Delegation ”。

#### [与其他特性的交互](#ZH-CN_TOPIC_0279370029)

| **交互类型** | **相关特性** | **控制项名称** | **交互说明** |
| --- | --- | --- | --- |
| 依赖 | [GWFD-020401 IPv6承载上下文](../GWFD-020401 IPv6承载上下文_67107266.md) | 82209828 IPv6承载上下文 | UDG<br>需要建立IPv6承载上下文，因此需开启IPv6承载上下文特性。 |
| 依赖 | [GWFD-020403 IPv4v6双栈接入](../GWFD-020403 IPv4v6双栈接入_67108868.md) | 82209829 IPv4v6双栈接入 | 如果需要对IPv4v6双栈接入用户的业务进行解析，则需要先开启IPv4v6双栈接入特性。 |
| 互斥 | [GWFD-020412 L2TP VPN](../../组网功能/GWFD-020412 L2TP VPN_40342126.md) | 82200BVC L2TP VPN | L2TP VPN通过LNS设备实现了手机后路由功能，所以在同一APN下，L2TP VPN和手机后路由功能无需同时部署。 |
| 互斥 | [GWFD-010108GWFD-020808GWFD-020808 用户面地址自动检测](../../基本接入功能/GWFD-010108 用户面地址自动检测_04636901.md) | - | 手机后路由用户不能做用户面地址自动检测。 |
| 互斥 | NAT基本功能 | 82200DAB NAT基本功能（Mbps） | 手机后路由的用户不支持NAT地址转换。 |
| 互斥 | [GWFD-020482 入不转板功能](../../性能优化/GWFD-020482 入不转板功能_28369926.md) | - | 手机后路由用户不支持入不转板功能。 |
| 互斥 | [GWFD-020531 通用DNN漫游分流](../../超级互联功能/GWFD-020531 通用DNN漫游分流_57247580.md) | 82200GCJ LKV3G5STCA01 移动VPN智能分流园区接入 | 手机后路由用户不支持通用DNN漫游分流功能。 |

#### [对系统的影响](#ZH-CN_TOPIC_0279370029)

IPv6 Prefix Delegation特性只进行简单信元解析和路由转发，对系统影响可忽略。

#### [应用限制](#ZH-CN_TOPIC_0279370029)

- 本地地址池方式为用户分配IPv6 delegated-prefix时，同一APN下的IPv6 delegated-prefix长度必须相同。外部网元（SMF/RADIUS）为用户分配IPv6 delegated-prefix时，同一APN下的IPv6 delegated-prefix长度可以不同。
- IPv6 delegated-prefix功能中用户分配的地址前缀范围为49~64之间，不包含64位。

#### [原理概述](#ZH-CN_TOPIC_0279370029)

IPv6 Prefix Delegation功能中 UDG 为用户分配携带IPv6地址前缀长度的IPv6地址，按照地址分配方式分为以下场景。

- 外部用户（SMF、Radius Server）分配用户地址场景，SMF/PGW-C在会话建立请求中将UE IP Address中“IPv6D”置位，携带IPv6 Address并且携带“IPv6 Prefix Delegation Bits field”指示IPv6地址前缀长度。
- 本地用户面分配地址场景，UPF/PGW-U上配置IPv6地址前缀小于64位的地址池，SMF/PGW-C在会话建立请求中将UE IP Address的“CHV6”置位。UPF/PGW-U在会话建立响应中UE IP Address的“IPv6D”置位，携带IPv6 Address和“IPv6 Prefix Delegation Bits field”。

IP Address信元结构如 [图2](#ZH-CN_TOPIC_0279370029__fig1267415492190) 所示。

**图2** UE IP Address信元结构

<br>

![](GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.assets/zh-cn_image_0279699959.png)

#### [计费与话单](#ZH-CN_TOPIC_0279370029)

本特性不涉及计费与话单。

#### [特性规格](#ZH-CN_TOPIC_0279370029)

本特性不涉及特性规格。

#### [遵循标准](#ZH-CN_TOPIC_0279370029)

| 标准类别 | 标准名称 | 标准名称 |
| --- | --- | --- |
| IETF | RFC 3315 | RFC 3315 Dynamic Host Configuration Protocol for IPv6 (DHCPv6) |
| 3GPP | 23.060 | 3GPP TS 23.060 General Packet Radio Service (GPRS) Service Description; Stage 2 |
| 3GPP | 29.244 | 3GPP TS 29.244 Interface between the Control Plane and the User Plane of EPC Nodes |

#### [发布历史](#ZH-CN_TOPIC_0279370029)

| **特性版本** | **发布版本** | **发布说明** |
| --- | --- | --- |
| 01 | 20.5.0 | 首次发布。 |
