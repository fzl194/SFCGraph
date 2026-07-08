# WSFD-106203 别名APN特性概述（适应于GGSN/PGW-C/SMF）

- [适用NF](#ZH-CN_CONCEPT_0234797879__1.3.1.1)
- [定义](#ZH-CN_CONCEPT_0234797879__1.3.2.1)
- [客户价值](#ZH-CN_CONCEPT_0234797879__1.3.3.1)
- [应用场景](#ZH-CN_CONCEPT_0234797879__1.3.4.1)
- [可获得性](#ZH-CN_CONCEPT_0234797879__1.3.5.1)
- [与其他特性的交互](#ZH-CN_CONCEPT_0234797879__1.3.6.1)
- [对系统的影响](#ZH-CN_CONCEPT_0234797879__1.3.7.1)
- [应用限制](#ZH-CN_CONCEPT_0234797879__1.3.8.1)
- [原理概述](#ZH-CN_CONCEPT_0234797879__1.3.9.1)
- [计费与话单](#ZH-CN_CONCEPT_0234797879__1.3.10.1)
- [特性规格](#ZH-CN_CONCEPT_0234797879__1.3.11.1)
- [遵循标准](#ZH-CN_CONCEPT_0234797879__1.3.12.1)
- [发布历史](#ZH-CN_CONCEPT_0234797879__1.3.13.1)

#### [适用NF](#ZH-CN_CONCEPT_0234797879)

GGSN、 PGW-C、SMF

#### [定义](#ZH-CN_CONCEPT_0234797879)

为了兼容现网中存在使用相同资源的多个APN，提出别名APN的概念。当运营商需要将不同APN的业务都映射到同一APN上或者将某一APN的业务映射到另一APN上时，只需要在 UNC 上配置APN别名映射，就可以将用户侧传来的APN作为别名APN映射到真实APN上，这样不同的APN可以共用相同的系统资源，从而便于系统资源的分配组合。

#### [客户价值](#ZH-CN_CONCEPT_0234797879)

| 受益方 | 受益描述 |
| --- | --- |
| 运营商 | GPRS/UMTS/EPC/5G网络中，运营商不需要全网修改APN的规划和配置，减少了运营商网络配置和维护管理的复杂度。 |
| 用户 | 用户无需在终端上做任何修改，不同APN下的用户就可以共享系统资源。 |

#### [应用场景](#ZH-CN_CONCEPT_0234797879)

终端上的APN设置多种多样，而运营商对这些终端提供相同的APN业务。如果在 UNC 上配置众多的APN或者通知用户更改配置，都将提高运营成本。

通过别名APN功能，将所有已知的APN都映射为同一个APN进行业务，这样不同的APN可以共用相同的系统资源，从而便于系统资源的分配组合。

别名APN主要适用于以下两种场景：

- 运营商合并和重组时，为了兼容现网中使用相同资源的多个APN，可将某APN的业务映射到另一APN上。
- 网络改建时新规划了APN，为了不影响原规划APN的使用，只需将原规划的APN映射到新规划APN上即可。

#### [可获得性](#ZH-CN_CONCEPT_0234797879)

**涉及NF**

| **涉及NF** | **支持版本** | **功能说明** |
| --- | --- | --- |
| GGSN-C/PGW-C/SMF | UNC 20.3.0及后续版本 | 本地配置别名APN到真实APN的映射关系。 |

**License支持**

本特性只有获得了License许可后才能获得该特性的服务，对应的License控制项为 “82200BNM LKV2AAPN01 别名APN-USM” 。

#### [与其他特性的交互](#ZH-CN_CONCEPT_0234797879)

本特性不涉及与其他特性的交互。

#### [对系统的影响](#ZH-CN_CONCEPT_0234797879)

随着别名APN接入用户数的增加，系统资源占用会一直增大，CPU占用率会相应上升。

#### [应用限制](#ZH-CN_CONCEPT_0234797879)

当某个别名APN下还存在用户或会话时，该别名APN不允许直接删除，执行 [**RMV APNALIAS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/别名APN/删除APN别名配置（RMV APNALIAS）_28567655.md) UNC会拒绝该请求。如果想删除此类别名APN，需要先锁定此别名APN，再批量去激活该别名APN下用户，最后删除别名APN。

#### [原理概述](#ZH-CN_CONCEPT_0234797879)

**相关概念**

- APN
  APN（Access Point Name）是GPRS/UMTS/EPS系统定义的网络标识。一方面，GPRS/UMTS/EPS核心网通过APN标识出GGSN/PGW-C；另一方面，APN标识了通过该GGSN/PGW-C所连接的外部PDN（如ISP网络、企业网等）或所关联的某种类型的业务（如Internet接入、WAP业务等）。
  APN由两部分组成：

  - APN NI（Network Identifier）
      APN NI是APN中的必选部分，用于标识需要接入的外部数据网络的类型。APN NI需要在HSS中进行了签约，激活时才允许使用该APNNI。
      APN NI是由一个标记或用点分隔的多个标记组成，例如“huawei.com”或 “service.huawei.com”。
    - APN OI（Operator Identifier）
      APN OI是APN的可选部分，用于标识运营商类型。APN OI的格式完全符合DNS命令规范，由三个标记组成。APN OI使用".gprs"结尾，对于每个运营商，存在一个缺省值的APN OI，此APN OI由IMSI导出，形式为“MNCxxx.MCCyyy.gprs”或“apn.epc.MNCxxx.MCCyyy.3gppnetwork.org”。

- APN与PDN的关系
  对GGSN/PGW-C而言，首先需要知道的是移动用户将被允许通过GGSN/PGW-C接入哪些外部PDN，一旦确定后，就应当规划连接哪些外部PDN的接入点，并在GGSN/PGW-C配置相应APN信息。同时，GPRS/UMTS核心网上的DNS应当进行APN和GGSN/PGW-C IP地址的关联，以保证SGSN/MME能够根据MS/UE提供的APN，寻址到相应的GGSN/PGW-C，从而将MS/UE接入相应的PDN。 UNC 的APN同时也是用户划分的一个单位，基于APN可以配置用户属性策略，比如计费、QoS、安全和业务控制，不同的APN可以有不同的策略，从而实现灵活计费和业务控制，增强运营竞争力。
  > **说明**
  > 2/3/4G场景中，本特性提到的APN均指APN NI。
  >
  > 5G场景中，本特性提到的APN指DNN（Data Network Name），PDN连接对应PDU会话。
  >
  > 3GPP TS23.501 R15定义DNN与APN这两个标识符具有相同的含义，并携带相同的信息，在R15，DNN等价于APN。

**特性原理**

对于别名APN，主要是为了兼容现网中使用相同资源的多个APN。因此， UNC 提供别名APN到真实APN的配置映射，将用户激活时携带的请求APN映射到真实APN上激活，使用真实APN上的业务。

如 [图1](#ZH-CN_CONCEPT_0234797879__fig1429910116162) 所示，配置APN“apn1”和“apn2”为APN“apn5”的别名，则别名APN“apn1”和“apn2”在 UNC 上使用与APN“apn5”相同的资源，并且以APN“apn5”的信息进行统计。

**图1** 别名APN原理图

<br>

![](WSFD-106203 别名APN特性概述（适应于GGSN_PGW-C_SMF）_34797879.assets/zh-cn_image_0234797885_2.png)

#### [计费与话单](#ZH-CN_CONCEPT_0234797879)

使用别名APN功能时，可以配置话单中使用的APN类型为别名APN或者真实APN。

#### [特性规格](#ZH-CN_CONCEPT_0234797879)

| 规格名称 | 规格指标 |
| --- | --- |
| 支持最大别名APN数量（个） | 1000 |
| 一个APN下最多可以配置的APN别名数（个） | 500 |

#### [遵循标准](#ZH-CN_CONCEPT_0234797879)

| 标准类别 | **标准编号** | 标准名称 |
| --- | --- | --- |
| 3GPP | 23.060 | General Packet Radio Service (GPRS) Service Description; Stage 2 |
| 3GPP | 29.060 | General Packet Radio Service (GPRS); GPRS Tunnelling Protocol (GTP) across the Gn and Gp interface |
| 3GPP | 29.061 | Interworking between the Public Land Mobile Network (PLMN) supporting packet based services and Packet Data Networks (PDN) |
| 3GPP | 23.214 | Architecture enhancements for control and user plane separation of EPC nodes |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane of EPC Nodes |

#### [发布历史](#ZH-CN_CONCEPT_0234797879)

| 特性版本 | 发布版本 | 发布说明 |
| --- | --- | --- |
| 1 | 20.3.0 | 首次发布。 |
