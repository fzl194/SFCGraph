# GWFD-110102 SA-HTTP Pipeline & WAP Concatenation

- [适用NF](#ZH-CN_CONCEPT_0124082510__1.4.1.1)
- [定义](#ZH-CN_CONCEPT_0124082510__1.4.2.1)
- [客户价值](#ZH-CN_CONCEPT_0124082510__1.4.3.1)
- [应用场景](#ZH-CN_CONCEPT_0124082510__1.4.4.1)
- [可获得性](#ZH-CN_CONCEPT_0124082510__1.4.5.1)
- [与其他特性的交互](#ZH-CN_CONCEPT_0124082510__1.4.6.1)
- [对系统的影响](#ZH-CN_CONCEPT_0124082510__1.4.7.1)
- [应用限制](#ZH-CN_CONCEPT_0124082510__1.4.8.1)
- [原理概述](#ZH-CN_CONCEPT_0124082510__1.4.9.1)
- [计费与话单](#ZH-CN_CONCEPT_0124082510__1.4.10.1)
- [特性规格](#ZH-CN_CONCEPT_0124082510__1.4.11.1)
- [遵循标准](#ZH-CN_CONCEPT_0124082510__1.4.12.1)
- [发布历史](#ZH-CN_CONCEPT_0124082510__1.4.13.1)

#### [适用NF](#ZH-CN_CONCEPT_0124082510)

SGW-U、PGW-U、UPF

#### [定义](#ZH-CN_CONCEPT_0124082510)

SA-HTTP Pipeline是指 UDG 支持对Pipeline模式下的同一个数据流上的每个HTTP业务请求及其对应的响应进行业务感知，按照不同业务进行不同的计费和动作处理。

SA-WAP concatenation是指 UDG 支持对Concatenation模式下的同一个数据流上的每个WAP业务请求及其对应的响应进行业务感知，按照不同业务进行不同的计费和动作处理。

#### [客户价值](#ZH-CN_CONCEPT_0124082510)

| 受益方 | 受益描述 |
| --- | --- |
| 运营商 | 可以对HTTP Pipeline或WAP concatenation报文中的每个请求进行计费，计费更精确。 |
| 用户 | 用户不感知该特性。 |

#### [应用场景](#ZH-CN_CONCEPT_0124082510)

对HTTP Pipeline或WAP concatenation报文中的每个请求进行计费，计费更精确。

#### [可获得性](#ZH-CN_CONCEPT_0124082510)

**涉及NF**

| 涉及NF | 支持版本 | 功能说明 |
| --- | --- | --- |
| SGW-U/PGW-U/UPF | UDG 20.0.0及后续版本 | 用于对报文进行识别和解析，根据解析结果匹配规则，对不同业务进行不同的计费和动作处理。 |

**License支持**

本特性只有获得了License许可后才能获得该特性的服务，对应的License控制项为 “82209754 LKV3G5HPWC01 SA-HTTP Pipeline & WAP Concatenation”。

该License项控制的协议组包括的协议可以通过 **[LST DFTPROTGRP](../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/三四层规则管理/协议组/查询默认协议组（LST DFTPROTGRP）_82837345.md)** 命令查询。

#### [与其他特性的交互](#ZH-CN_CONCEPT_0124082510)

| 交互类型 | 相关特性 | 控制项名称 | 交互说明 |
| --- | --- | --- | --- |
| 依赖 | [GWFD-110101 SA-Basic](GWFD-110101 SA-Basic_24082506.md) | 82209749 SA-Basic | SA-Basic是SA的基本功能，必须开启。 |
| 依赖 | [GWFD-110103 SA-Web Browsing](GWFD-110103 SA-Web Browsing_24082511.md) | 82209755 SA-Web Browsing | 由于要识别HTTP报文实现SA-HTTP Pipeline功能，因此需开启SA-Web Browsing功能。 |
| 依赖 | [GWFD-110105 SA-Mobile](GWFD-110105 SA-Mobile_24082513.md) | 82209757 SA-Mobile | 由于要识别WAP报文实现SA-WAP concatenation功能，因此需开启SA-Mobile功能。 |

#### [对系统的影响](#ZH-CN_CONCEPT_0124082510)

当在 UDG 上开启SA-HTTP Pipeline & WAP concatenation特性后， 由于匹配到规则的用户业务流的所有报文都需要进行报文的业务感知，因此系统处理负荷将增加，报文转发性能和吞吐量将下降。

详细性能影响需要基于流量模型进行评估，请联系华为技术支持获取服务。

#### [应用限制](#ZH-CN_CONCEPT_0124082510)

需要打开pipeline开关，即将 **[BYTE53](../../../../OM参考/软件参数/UDG软件参数/用户面软件参数/软件参数/业务感知管理/BYTE53 设置是否支持pipeline业务_96403707.md)** 号软参置1。

#### [原理概述](#ZH-CN_CONCEPT_0124082510)

**协议特征**

- HTTP Pipeline
  HTTP1.1版本支持流水线模式（Pipeline），该模式下一个数据包中包含多个请求，允许在还没有收到前一个请求的响应之前就发送新的请求，应答时严格按照请求发送的顺序返回响应。
- WAP concatenation
  WAP协议支持concatenation模式，该模式下一个数据包中包含多个请求，允许在还没有收到前一个请求的响应之前就发送新的请求，应答时严格按照请求发送的顺序返回响应。

**系统实现**

三四层解析、协议识别和业务流程的详细描述请参见 [GWFD-110101 SA-Basic](GWFD-110101 SA-Basic_24082506.md) 。

**七层解析**

UDG 识别出报文协议后，对每一个请求和响应进行解析，解析出相应的关键字，如URL、Method、响应码。然后分别进行七层规则匹配，对报文实施不同的计费和控制策略。

#### [计费与话单](#ZH-CN_CONCEPT_0124082510)

本特性不涉及计费与话单。

#### [特性规格](#ZH-CN_CONCEPT_0124082510)

本特性无特殊规格。

#### [遵循标准](#ZH-CN_CONCEPT_0124082510)

| 标准类别 | 标准编号 | 标准名称 |
| --- | --- | --- |
| 3GPP | 23.214 | Architecture enhancements for control and user plane separation of EPC nodes |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane of EPC Nodes |
| IETF | 1945 | Hypertext Transfer Protocol -- HTTP/1.0 |

#### [发布历史](#ZH-CN_CONCEPT_0124082510)

| 特性版本 | 发布版本 | 发布说明 |
| --- | --- | --- |
| 01 | 20.0.0 | 首次发布。 |
