# GWFD-110107 SA-Streaming

- [适用NF](#ZH-CN_CONCEPT_0124082515__1.4.1.1)
- [定义](#ZH-CN_CONCEPT_0124082515__1.4.2.1)
- [客户价值](#ZH-CN_CONCEPT_0124082515__1.4.3.1)
- [应用场景](#ZH-CN_CONCEPT_0124082515__1.4.4.1)
- [可获得性](#ZH-CN_CONCEPT_0124082515__1.4.5.1)
- [与其他特性的交互](#ZH-CN_CONCEPT_0124082515__1.4.6.1)
- [对系统的影响](#ZH-CN_CONCEPT_0124082515__1.4.7.1)
- [应用限制](#ZH-CN_CONCEPT_0124082515__1.4.8.1)
- [原理概述](#ZH-CN_CONCEPT_0124082515__1.4.9.1)
- [计费与话单](#ZH-CN_CONCEPT_0124082515__1.4.10.1)
- [特性规格](#ZH-CN_CONCEPT_0124082515__1.4.11.1)
- [遵循标准](#ZH-CN_CONCEPT_0124082515__1.4.12.1)
- [发布历史](#ZH-CN_CONCEPT_0124082515__1.4.13.1)

#### [适用NF](#ZH-CN_CONCEPT_0124082515)

SGW-U、PGW-U、UPF

#### [定义](#ZH-CN_CONCEPT_0124082515)

SA-Streaming是指 UDG 支持对Streaming报文进行业务感知，判断访问内容，感知业务，对不同业务进行不同的计费和动作处理。

#### [客户价值](#ZH-CN_CONCEPT_0124082515)

| 受益方 | 受益描述 |
| --- | --- |
| 运营商 | 对于Streaming应用提供较大带宽，提升用户观看视频的感受，吸引更多的客户使用运营商网络。 |
| 用户 | 用户不感知该特性。 |

#### [应用场景](#ZH-CN_CONCEPT_0124082515)

对于Streaming应用提供较大带宽，提升用户观看视频的感受，吸引更多的客户使用运营商网络。

#### [可获得性](#ZH-CN_CONCEPT_0124082515)

**涉及NF**

| 涉及NF | 支持版本 | 功能说明 |
| --- | --- | --- |
| SGW-U/PGW-U/UPF | UDG 20.0.0及后续版本 | 用于对报文进行识别和解析，根据解析结果匹配规则，对不同业务进行不同的计费和动作处理。 |

**License支持**

本特性只有获得了License许可后才能获得该特性的服务，对应的License控制项为 “82209759 LKV3G5SAST01 SA-Streaming”。

该License项控制的协议组包括的协议可以通过 **[LST DFTPROTGRP](../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务过滤器管理/三四层规则管理/协议组/查询默认协议组（LST DFTPROTGRP）_82837345.md)** 命令查询。

#### [与其他特性的交互](#ZH-CN_CONCEPT_0124082515)

| 交互类型 | 相关特性 | 控制项名称 | 交互说明 |
| --- | --- | --- | --- |
| 依赖 | [GWFD-110101 SA-Basic](GWFD-110101 SA-Basic_24082506.md) | 82209749 SA-Basic | SA-Basic是SA的基本功能，必须开启。 |

#### [对系统的影响](#ZH-CN_CONCEPT_0124082515)

当在 UDG 上开启SA-Streaming特性后， 由于匹配到规则的用户业务流的所有报文都需要进行报文的业务感知，因此系统处理负荷将增加，报文转发性能和吞吐量将下降。

详细性能影响需要基于流量模型进行评估，请联系华为技术支持获取服务。

#### [应用限制](#ZH-CN_CONCEPT_0124082515)

SA-Streaming特性依赖于Streaming协议识别，Streaming协议的应用类型非常多而且不断有新的应用类型出现和更新，需要定期更新SA识别特征库以支持新的Streaming协议类型的识别。

#### [原理概述](#ZH-CN_CONCEPT_0124082515)

**Streaming 流媒体类协议特征**

该类协议的主要特征为通过浏览器或特定播放工具实现视频或音频流的播放和访问。例如： RTSP和MMSP 。

RTSP是一种客户端/服务器应用级协议。这种协议用来控制数据的实时传输。

MMSP协议用于访问媒体服务器上的单播内容,它是连接媒体单播服务的默认方法，应用范围比较小。它既可以承载信令，又可以承载数据。MMSP建立在UDP或TCP传输层上，属于应用层。

SA-Streaming支持解析的子协议类型个数，由加载的协议特征库决定。

**系统实现**

三四层解析、协议识别和业务流程的详细描述请参见 [GWFD-110101 SA-Basic](GWFD-110101 SA-Basic_24082506.md) 。

**七层解析**

- 如果 UDG 识别出报文协议为RTSP后,则按照RTSP标准协议对报文进行解析，解析出相应的关键字，如URL和Method字段中的Describe、Setup、Play、Pause。
- 如果 UDG 识别出报文协议为MMSP后，则按照MMSP标准协议对报文进行解析，解析出以下关键信息：
    - TransportMode (TCP或UDP)
    - FileName (访问的文件名)
    - S2CPlayIncarnation (是否允许采用PACKET-PAIR测试方法：UDP或者TCP测试)
    - FileAttributes (文件属性)
    - SubScriberName (请求会话信息、HOST名、端口号)
    - IpAddr、Port (IP地址和端口号)

然后进行七层规则匹配，对报文实施不同的计费和控制策略。

#### [计费与话单](#ZH-CN_CONCEPT_0124082515)

本特性不涉及计费与话单。

#### [特性规格](#ZH-CN_CONCEPT_0124082515)

本特性无特殊规格。

#### [遵循标准](#ZH-CN_CONCEPT_0124082515)

| 标准类别 | 标准编号 | 标准名称 |
| --- | --- | --- |
| 3GPP | 23.214 | Architecture enhancements for control and user plane separation of EPC nodes |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane of EPC Nodes |
| IETF | 2326 | Real Time Streaming Protocol |

#### [发布历史](#ZH-CN_CONCEPT_0124082515)

| 特性版本 | 发布版本 | 发布说明 |
| --- | --- | --- |
| 01 | 20.0.0 | 首次发布。 |
