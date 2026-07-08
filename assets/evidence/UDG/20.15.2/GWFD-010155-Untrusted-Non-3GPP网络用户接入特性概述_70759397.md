# GWFD-010155 Untrusted Non-3GPP网络用户接入特性概述

- [适用NF](#ZH-CN_TOPIC_0270759397__1.3.1.1)
- [定义](#ZH-CN_TOPIC_0270759397__1.3.2.1)
- [客户价值](#ZH-CN_TOPIC_0270759397__1.3.3.1)
- [应用场景](#ZH-CN_TOPIC_0270759397__1.3.4.1)
- [可获得性](#ZH-CN_TOPIC_0270759397__1.3.5.1)
- [与其他特性的交互](#ZH-CN_TOPIC_0270759397__1.3.6.1)
- [对系统的影响](#ZH-CN_TOPIC_0270759397__1.3.7.1)
- [应用限制](#ZH-CN_TOPIC_0270759397__1.3.8.1)
- [原理概述](#ZH-CN_TOPIC_0270759397__1.3.9.1)
- [计费与话单](#ZH-CN_TOPIC_0270759397__1.3.10.1)
- [特性规格](#ZH-CN_TOPIC_0270759397__1.3.11.1)
- [遵循标准](#ZH-CN_TOPIC_0270759397__1.3.12.1)
- [发布历史](#ZH-CN_TOPIC_0270759397__1.3.13.1)

#### [适用NF](#ZH-CN_TOPIC_0270759397)

PGW-U

#### [定义](#ZH-CN_TOPIC_0270759397)

Untrusted Non-3GPP网络用户接入特性使WiFi用户可以通过ePDG接入EPC网络连接PDN并进行各种数据业务。

#### [客户价值](#ZH-CN_TOPIC_0270759397)

| 受益方 | 受益描述 |
| --- | --- |
| 运营商 | 使WiFi用户可以接入EPC网络，实现WiFi接入和LTE接入用户的统一管理，实现Untrusted Non-3GPP与3GPP网络的融合。保证现有WiFi网络建设的投资价值，便于运营商有效地进行网络规划，将现有网络平滑地过渡到统一的分组核心网络。 |
| 用户 | WiFi用户可以享用EPC网络提供的数据业务。 |

#### [应用场景](#ZH-CN_TOPIC_0270759397)

Untrusted Non-3GPP网络接入支持非漫游/Home Routed漫游/Local Breakout漫游三种网络架构。

- 非漫游网络架构：用户在HPLMN中接入，通过HPLMN的PGW-U与PDN进行连接。
- Home Routed漫游：用户在VPLMN中接入，通过HPLMN的PGW-U与PDN进行连接。
- Local Breakout漫游：用户在VPLMN中接入，通过VPLMN的PGW-U与PDN进行连接。

#### [可获得性](#ZH-CN_TOPIC_0270759397)

**涉及NF**

| **涉及NF** | **支持版本** | **功能说明** |
| --- | --- | --- |
| UE | 无特殊要求 | WiFi终端，支持WiFi网络接入功能。 |
| ePDG | 无特殊要求 | 能够连接到3GPP AAA Server和PGW-C/PGW-U，为UE提供信令和数据业务通道。 |
| PGW-C | UNC 20.5.0及后续版本 | 通过S2b接口和WiFi网络的ePDG完成信令的互通，通过S6b接口和3GPP AAA Server互通。 |
| PGW-U | UDG 20.5.0及后续版本 | 通过S2b接口和WiFi网络的ePDG完成数据业务的互通，为UE接入外部数据网提供基本承载功能。<br>接收Untrusted Non-3GPP用户发送的数据，选路到相应的外部网络；或接收外部网络的数据，根据其目的地址选择EPC网络中的传输通道，传给相应的ePDG。 |
| HSS | 无特殊要求 | UE从Untrusted Non-3GPP网络接入时，对其进行鉴权和用户管理。 |
| 3GPP AAA Server | 无特殊要求 | UE从Untrusted Non-3GPP网络接入时，为其提供静态QoS信息。 |

**License支持**

本特性无需获得License许可即可获得该特性的服务。

#### [与其他特性的交互](#ZH-CN_TOPIC_0270759397)

| **交互类型** | **相关特性** | **控制项名称** | **交互说明** |
| --- | --- | --- | --- |
| 互斥 | [GWFD-020531 通用DNN漫游分流](../../超级互联功能/GWFD-020531 通用DNN漫游分流_57247580.md) | 82200GCJ LKV3G5STCA01 移动VPN智能分流园区接入 | 通用DNN漫游分流只支持4G/5G接入，不支持其他接入方式。 |

#### [对系统的影响](#ZH-CN_TOPIC_0270759397)

Untrusted Non-3GPP网络用户接入时， UDG 只进行简单信元解析和路由转发，对系统无影响。

#### [应用限制](#ZH-CN_TOPIC_0270759397)

本特性无应用限制。

#### [原理概述](#ZH-CN_TOPIC_0270759397)

在非漫游和Home Routed漫游网络中，ePDG与HPLMN中的PGW-C/PGW-U配合完成Untrusted Non-3GPP用户接入3GPP EPC网络；在Local Breakout漫游网络中，ePDG与VPLMN中的PGW-C/PGW-U配合完成Untrusted Non-3GPP用户接入3GPP EPC网络。

- PGW-C/PGW-U在S2b接口使用GTPv2协议，完成Untrusted Non-3GPP用户接入EPC网络。
- PGW-C/PGW-U根据UE的请求为其分配一个或多个IP地址。
  > **说明**
  > - 如果UE同时请求IPv4和IPv6地址，PGW-C/PGW-U将为其分配两种地址。如果运营商规定针对某一APN仅能分配IPv4或IPv6地址，PGW-C/PGW-U将为其分配IPv4地址或IPv6地址。
  > - 如果UE只要求IPv4或IPv6地址，PGW-C/PGW-U将为其相应分配。
- ePDG和PGW-U之间建立起GTP-U隧道，PGW-U通过此隧道完成用户数据报文转发。

Untrusted Non-3GPP网络接入EPC的非漫游网络架构如 [图1](#ZH-CN_TOPIC_0270759397__fig1218785485416) 所示，Home Routed漫游网络架构如 [图2](#ZH-CN_TOPIC_0270759397__fig85861519105414) 所示，Local Breakout漫游网络架构如 [图3](#ZH-CN_TOPIC_0270759397__fig970025425218) 所示。

**图1** Untrusted Non-3GPP网络用户接入组网结构（非漫游）

<br>

![](GWFD-010155 Untrusted Non-3GPP网络用户接入特性概述_70759397.assets/zh-cn_image_0274366457.png)

**图2** Untrusted Non-3GPP网络用户接入组网结构（漫游—Home Routed）

<br>

![](GWFD-010155 Untrusted Non-3GPP网络用户接入特性概述_70759397.assets/zh-cn_image_0274366428.png)

**图3** Untrusted Non-3GPP网络用户接入组网结构（漫游—Local Breakout）

<br>

![](GWFD-010155 Untrusted Non-3GPP网络用户接入特性概述_70759397.assets/zh-cn_image_0274367797.png)

#### [计费与话单](#ZH-CN_TOPIC_0270759397)

本特性不涉及计费与话单。

#### [特性规格](#ZH-CN_TOPIC_0270759397)

本特性无特殊规格。

#### [遵循标准](#ZH-CN_TOPIC_0270759397)

| 标准类别 | 标准编号 | 标准名称 |
| --- | --- | --- |
| 3GPP | TS 23.402 | Architecture enhancements for non-3GPP accesses (Release 12) |
| 3GPP | TS 29.274 | 3GPP Evolved Packet System (EPS); Evolved General Packet Radio Service (GPRS) Tunnelling Protocol for Control plane (GTPv2-C); Stage 3 (Release 12) |
| 3GPP | TS 23.139 | system - fixed broadband access network interworking; Stage 2 |

#### [发布历史](#ZH-CN_TOPIC_0270759397)

| 特性版本 | 发布版本 | 发布说明 |
| --- | --- | --- |
| 01 | 20.5.0 | 首次发布。 |
