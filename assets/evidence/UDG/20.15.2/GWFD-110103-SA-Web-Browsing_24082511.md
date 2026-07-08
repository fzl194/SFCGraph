# GWFD-110103 SA-Web Browsing

- [适用NF](#ZH-CN_CONCEPT_0124082511__1.4.1.1)
- [定义](#ZH-CN_CONCEPT_0124082511__1.4.2.1)
- [客户价值](#ZH-CN_CONCEPT_0124082511__1.4.3.1)
- [应用场景](#ZH-CN_CONCEPT_0124082511__1.4.4.1)
- [可获得性](#ZH-CN_CONCEPT_0124082511__1.4.5.1)
- [与其他特性的交互](#ZH-CN_CONCEPT_0124082511__1.4.6.1)
- [对系统的影响](#ZH-CN_CONCEPT_0124082511__1.4.7.1)
- [应用限制](#ZH-CN_CONCEPT_0124082511__1.4.8.1)
- [原理概述](#ZH-CN_CONCEPT_0124082511__1.4.9.1)
- [计费与话单](#ZH-CN_CONCEPT_0124082511__1.4.10.1)
- [特性规格](#ZH-CN_CONCEPT_0124082511__1.4.11.1)
- [遵循标准](#ZH-CN_CONCEPT_0124082511__1.4.12.1)
- [发布历史](#ZH-CN_CONCEPT_0124082511__1.4.13.1)

#### [适用NF](#ZH-CN_CONCEPT_0124082511)

SGW-U、PGW-U、UPF

#### [定义](#ZH-CN_CONCEPT_0124082511)

SA-Web Browsing是指 UDG 支持对Web Browsing报文进行业务感知，判断访问内容，感知业务，对不同业务进行不同的计费和动作处理。

#### [客户价值](#ZH-CN_CONCEPT_0124082511)

| 受益方 | 受益描述 |
| --- | --- |
| 运营商 | 观察用户上网的流量分布，根据报表分析结果采取合适的计费和控制策略。 |
| 用户 | 用户不感知该特性。 |

#### [应用场景](#ZH-CN_CONCEPT_0124082511)

结合报表功能可以观察用户上网的流量分布，根据报表分析结果采取合适的计费和控制策略。

#### [可获得性](#ZH-CN_CONCEPT_0124082511)

**涉及NF**

| 涉及NF | 支持版本 | 功能说明 |
| --- | --- | --- |
| SGW-U/PGW-U/UPF | UDG 20.0.0及后续版本 | 用于对报文进行识别和解析，根据解析结果匹配规则，对不同业务进行不同的计费和动作处理。 |

**License支持**

本特性只有获得了License许可后才能获得该特性的服务，对应的License控制项为 “82209755 LKV3G5SAWB01 SA-Web Browsing”。

该License项控制的协议组包括的协议可以通过 **[LST DFTPROTGRP](../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/三四层规则管理/协议组/查询默认协议组（LST DFTPROTGRP）_82837345.md)** 命令查询。

#### [与其他特性的交互](#ZH-CN_CONCEPT_0124082511)

| 交互类型 | 相关特性 | 控制项名称 | 交互说明 |
| --- | --- | --- | --- |
| 依赖 | [GWFD-110101 SA-Basic](GWFD-110101 SA-Basic_24082506.md) | 82209749 SA-Basic | SA-Basic是SA的基本功能，必须开启。 |

#### [对系统的影响](#ZH-CN_CONCEPT_0124082511)

当在 UDG 上开启SA-Web Browsing特性后， 由于匹配到规则的用户业务流的所有报文都需要进行报文的业务感知，因此系统处理负荷将增加，报文转发性能和吞吐量将下降。

详细性能影响需要基于流量模型进行评估，请联系华为技术支持获取服务。

#### [应用限制](#ZH-CN_CONCEPT_0124082511)

SA-Web Browsing特性依赖于Web Browsing协议识别，Web Browsing协议的应用类型非常多而且不断有新的应用类型出现和更新，需要定期更新SA识别特征库以支持新的Web Browsing协议类型的识别。

#### [原理概述](#ZH-CN_CONCEPT_0124082511)

**Web Browsing 网页浏览类协议特征**

该类协议的主要特征为通过浏览器对特定网页进行浏览，例如：HTTP。

HTTP协议用于在服务器与客户端之间传输超文本文件，超文本文件所遵循的规范称为超文本标记语言HTML（Hypertext Markup Language）。HTTP可以承载传输其他的协议，如RTSP、流媒体。

SA-Web Browsing支持解析的子协议类型个数，由加载的协议特征库决定。

**系统实现**

三四层解析、协议识别和业务流程的详细描述请参见 [GWFD-110101 SA-Basic](GWFD-110101 SA-Basic_24082506.md) 。

**七层解析**

如果 UDG 识别出报文协议为HTTP后，则按照HTTP标准协议对报文进行解析，解析出相应的关键字，如URL和Method，如 [表1](#ZH-CN_CONCEPT_0124082511__tab12) 所示。然后进行七层规则匹配，对报文实施不同的计费和控制策略。

*表1 七层解析*

| 协议 | 上下行 | 关键信息 | 说明 |
| --- | --- | --- | --- |
| HTTP | UP | - Method：Get、Post、Connect、Put、Delete、Options、Head、Trace<br>- host<br>- x-online-host<br>- path<br>- user-agent | 解析Method的Get、Post、Connect、Put、Delete、Options、Head、Trace，获取其完整的host、path、user-agent字段；其他类型的报文都按照other-method进行处理。 |
| HTTP | DOWN | Response code；Content-type(MMS、RTSP)；Content-length；Chunked | 响应报文主要解析响应类型，对于Content-type体现为承载协议非MMS和RTSP的报文无需解析消息体；同时需要通过Content-length和Chunked确认响应是否完整。 |

#### [计费与话单](#ZH-CN_CONCEPT_0124082511)

本特性不涉及计费与话单。

#### [特性规格](#ZH-CN_CONCEPT_0124082511)

本特性无特殊规格。

#### [遵循标准](#ZH-CN_CONCEPT_0124082511)

| 标准类别 | 标准编号 | 标准名称 |
| --- | --- | --- |
| 3GPP | 23.214 | Architecture enhancements for control and user plane separation of EPC nodes |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane of EPC Nodes |
| IETF | 2616 | Hypertext Transfer Protocol -- HTTP/1.1 |

#### [发布历史](#ZH-CN_CONCEPT_0124082511)

| 特性版本 | 发布版本 | 发布说明 |
| --- | --- | --- |
| 01 | 20.0.0 | 首次发布。 |
