# GWFD-110910 支持Routing Behind MS特性概述

- [适用NF](#ZH-CN_TOPIC_0274264899__1.3.1.1)
- [定义](#ZH-CN_TOPIC_0274264899__1.3.2.1)
- [客户价值](#ZH-CN_TOPIC_0274264899__1.3.3.1)
- [应用场景](#ZH-CN_TOPIC_0274264899__1.3.4.1)
- [可获得性](#ZH-CN_TOPIC_0274264899__1.3.5.1)
- [与其他特性的交互](#ZH-CN_TOPIC_0274264899__1.3.6.1)
- [对系统的影响](#ZH-CN_TOPIC_0274264899__1.3.7.1)
- [应用限制](#ZH-CN_TOPIC_0274264899__1.3.8.1)
- [原理概述](#ZH-CN_TOPIC_0274264899__1.3.9.1)
- [计费与话单](#ZH-CN_TOPIC_0274264899__1.3.10.1)
- [特性规格](#ZH-CN_TOPIC_0274264899__1.3.11.1)
- [遵循标准](#ZH-CN_TOPIC_0274264899__1.3.12.1)
- [发布历史](#ZH-CN_TOPIC_0274264899__1.3.13.1)

#### [适用NF](#ZH-CN_TOPIC_0274264899)

PGW-U、UPF

#### [定义](#ZH-CN_TOPIC_0274264899)

Routing Behind MS应用于移动VPN网络，是一种通过一台无线设备（MS/UE）将多台终端设备接入网络并与网络侧设备进行双向数据业务的技术方案。该方案不同于NAT技术，无线设备在GPRS/UMTS/EPC/5GC网络激活前，已经在AAA服务器上为其配置了下挂终端设备的网段。无线设备在GPRS/UMTS/EPC/5GC网络激活时，可以获取一个独立的IP地址。其后的多台终端设备在请求访问业务时， UDG 会根据AAA服务器通过UNC下发的网段路由更新本地路由表，以便能找到对应的终端设备，进行下行转发。

华为 UDG 支持基于APN控制Routing Behind MS功能是否使能。

#### [客户价值](#ZH-CN_TOPIC_0274264899)

| 受益方 | 受益描述 |
| --- | --- |
| 运营商 | 满足越来越普及的移动VPN的应用场景。为企业用户提供一种新的移动VPN业务模式，为企业提高工作效率、节省运营成本。 |
| 用户 | 实现了企业分支机构的移动办公，通过一台无线路由器将多个企业用户接入企业内部网络，并支持企业用户与企业内部网络进行双向互访。使企业用户和总部间的互访更加灵活、快速、安全。 |

#### [应用场景](#ZH-CN_TOPIC_0274264899)

Routing Behind MS主要服务于企业的移动VPN用户。

移动VPN用户和普通用户均可通过无线网络中的一台无线设备实现多台设备同时上网的需求，但是这两种技术存在很大差别。

- 普通家庭用户可以使用家用无线路由器来满足家庭中多台设备上网的需求。由于这种数据业务都是由客户端单向发起的，所以只要在无线路由器上进行NAT转换，即使MS/UE的一个上下文激活时只能得到一个主机IP地址，也仍然能够满足多台设备同时上网的需求。
- 移动VPN客户可以是企业分支机构中的多台设备，它们与总部设备之间需要发起双向的数据业务，所以不能使用NAT转换，Routing Behind MS特性就是为了解决这个问题提出的方案。

#### [可获得性](#ZH-CN_TOPIC_0274264899)

**涉及NF**

| **涉及NF** | **支持版本** | **功能说明** |
| --- | --- | --- |
| Wireless Router | 无特殊要求 | 帮助终端设备接入网络并与网络侧设备进行双向数据业务，承担终端设备上下行数据的转发。 |
| PGW-C/SMF | UNC 20.5.0及后续版本 | MS/UE激活时向AAA Server发起鉴权，通过鉴权从AAA Server获取<br>MS/UE<br>对应PC的下行路由，并发送给PGW-U/UPF。 |
| PGW-U/UPF | UDG 20.5.0及后续版本 | 接收MS/UE转发的上行数据，选路到相应的外部网络；接收外部网络的下行数据，根据其目的地址选择GPRS/UMTS/EPC/5GC网络中的传输通道，传给相应的MS/UE。<br>说明：对于启用了Routing Behind MS功能的用户下行报文，会出现目标地址与MS/UE主机地址不一致的情况，PGW-U/UPF需要根据网段路由将这些下行报文关联到MS/UE的PDP上下文/EPS承载/PDU会话上，并将这些下行报文通过此PDP上下文/EPS承载/PDU会话发送到MS/UE，由MS/UE将下行数据转发到目标设备。 |
| AAA Server | 无特殊要求 | 对MS/UE进行鉴权，并在无线设备（MS/UE）激活时为其分配一个激活使用的IP地址，同时在无线设备（MS/UE）下挂终端请求业务时，为终端分配一个可用的IP地址，此IP地址从AAA Server上配置的地址段中选取。 |

**License支持**

本特性只有获得了License许可后才能获得该特性的服务，对应的License控制项为 “82200CKP LKV3G5RBMS01 支持Routing Behind MS”。

本特性加载License后即可使用。

#### [与其他特性的交互](#ZH-CN_TOPIC_0274264899)

| 交互类型 | 相关特性 | 控制项名称 | 交互说明 |
| --- | --- | --- | --- |
| 互斥 | [GWFD-020412 L2TP VPN](../../组网功能/GWFD-020412 L2TP VPN_40342126.md) | 82200BVC LKV3G5L2TP01 L2TP VPN | L2TP VPN通过LNS设备实现了Routing Behind MS功能，所以在同一APN下，L2TP VPN和Routing Behind MS无需同时部署。 |
| 互斥 | [GWFD-010108GWFD-020808GWFD-020808 用户面地址自动检测](../GWFD-010108 用户面地址自动检测_04636901.md) | - | 手机后路由用户不能做用户面地址自动检测。 |
| 互斥 | NAT基本功能 | 82200DAB NAT基本功能（Mbps） | 手机后路由的用户不支持NAT地址转换。 |
| 互斥 | [GWFD-020482 入不转板功能](../../性能优化/GWFD-020482 入不转板功能_28369926.md) | - | 手机后路由用户不支持入不转板功能。 |
| 互斥 | [GWFD-020531 通用DNN漫游分流](../../超级互联功能/GWFD-020531 通用DNN漫游分流_57247580.md) | 82200GCJ LKV3G5STCA01 移动VPN智能分流园区接入 | 手机后路由用户不支持通用DNN漫游分流功能。 |

#### [对系统的影响](#ZH-CN_TOPIC_0274264899)

Routing Behind MS特性只进行简单信元解析和路由转发，对系统影响可忽略。

#### [应用限制](#ZH-CN_TOPIC_0274264899)

只有同时满足以下条件时，Routing Behind MS功能才能正常应用。

- 无线设备（MS/UE）采用RADIUS鉴权方式接入。
- MS/UE激活后获取IPv4地址。
- 网络中部署了支持下发IPv4网段地址的AAA Server。
- MS/UE上可以配置网段地址，并与AAA Server上的网段地址信息一致。

> **说明**
> 目前 UDG 仅支持IPv4用户的Routing Behind MS。

#### [原理概述](#ZH-CN_TOPIC_0274264899)

**相关概念**

- VPN
  虚拟私有网（Virtual Private Network），是私网的延伸，包括共享或者公网上封装、加密和鉴权的链路。VPN连接可以通过互联网提供到私网的远程接入和选路连接。
- 移动VPN
  移动VPN是以传统VPN技术为基础的一种新型接入手段。移动VPN可以为企业用户提供通过无线网络承载远程访问企业内部网络的功能，提供与传统VPN相同的服务。企业用户使用无线终端，通过GPRS/UMTS/EPC/5GC网络专有的APN，利用GPRS/UMTS/EPC/5GC骨干网络和本地接入网络，构建专有通道，访问远程企业内部网络。

**组网结构**

Routing Behind MS特性组网结构如 [图1](#ZH-CN_TOPIC_0274264899__fig2070412529410) 所示。

**图1** Routing Behind MS组网结构

<br>

![](GWFD-110910 支持Routing Behind MS特性概述_74264899.assets/zh-cn_image_0274264907.png "点击放大")

目前有两种技术可以实现Routing Behind MS功能：非L2TP组网和L2TP组网，如 [图1](#ZH-CN_TOPIC_0274264899__fig2070412529410) 所示。

- 非L2TP组网时，UDG支持Routing Behind MS功能。此时UDG需对一个PDP上下文/EPS承载/PDU会话对应的多个IP地址进行处理。
- L2TP组网时，LNS网元支持Routing Behind MS功能。此时作为LAC的UDG可以不感知此功能造成的一个PDP上下文/EPS承载/PDU会话对应的多个IP地址。

> **说明**
> L2TP组网的Routing Behind MS方案中 UDG 作为LAC设备在GTP和L2TP隧道透传数据，可以不感知Routing Behind MS功能造成的一个PDP上下文/EPS承载/PDU会话对应一个或者多个网段IP地址。由于此场景对 UDG 没有特殊要求，只需在PPP再生L2TP组网时关闭用户上行流量anti-spoofing检查功能即可实现，具体内容请参见 [GWFD-020412 L2TP VPN](../../组网功能/GWFD-020412 L2TP VPN_40342126.md) 。

#### [计费与话单](#ZH-CN_TOPIC_0274264899)

本特性不涉及计费与话单。

#### [特性规格](#ZH-CN_TOPIC_0274264899)

| 规格名称 | 规格指标 |
| --- | --- |
| 整机支持无线路由器同时在线最大数 | 20 000 |
| 单用户最大支持30个手机后路由网段 | 30 |

> **说明**
> 以客户规划C类地址为例，一个C类网段包含256个IP地址，每个用户最多能分配256*30= 7680个IP地址。

#### [遵循标准](#ZH-CN_TOPIC_0274264899)

| 标准类别 | 标准编号 | 标准名称 |
| --- | --- | --- |
| 3GPP | TS 23.214 | Architecture enhancements for control and user plane separation of EPC nodes |
| 3GPP | TS 29.244 | Interface between the Control Plane and the User Plane of EPC Nodes |
| IETF | RFC 2865 | Remote Authentication Dial In User Service (RADIUS) |

#### [发布历史](#ZH-CN_TOPIC_0274264899)

| 特性版本 | 发布版本 | 发布说明 |
| --- | --- | --- |
| 01 | 20.5.0 | 首次发布。 |
