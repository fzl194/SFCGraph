# GWFD-020101 支持Reflective QoS

- [适用NF](#ZH-CN_CONCEPT_0288816803__1.3.1.1)
- [定义](#ZH-CN_CONCEPT_0288816803__1.3.2.1)
- [客户价值](#ZH-CN_CONCEPT_0288816803__1.3.3.1)
- [应用场景](#ZH-CN_CONCEPT_0288816803__1.3.4.1)
- [可获得性](#ZH-CN_CONCEPT_0288816803__1.3.5.1)
- [与其他特性的交互](#ZH-CN_CONCEPT_0288816803__1.3.6.1)
- [对系统的影响](#ZH-CN_CONCEPT_0288816803__1.3.7.1)
- [应用限制](#ZH-CN_CONCEPT_0288816803__1.3.8.1)
- [原理概述](#ZH-CN_CONCEPT_0288816803__1.3.9.1)
- [计费与话单](#ZH-CN_CONCEPT_0288816803__1.3.10.1)
- [特性规格](#ZH-CN_CONCEPT_0288816803__1.3.11.1)
- [遵循标准](#ZH-CN_CONCEPT_0288816803__1.3.12.1)
- [发布历史](#ZH-CN_CONCEPT_0288816803__1.3.13.1)

#### [适用NF](#ZH-CN_CONCEPT_0288816803)

UPF

#### [定义](#ZH-CN_CONCEPT_0288816803)

Reflective QoS是指对满足条件的上行数据包，无需网络侧下发QoS rule，UE通过收到的下行数据包推演出对应的上行的QoS rule，相应将上行数据包映射到QoS flow上的机制。Reflective QoS适用于IP类型的PDU会话。

#### [客户价值](#ZH-CN_CONCEPT_0288816803)

| 受益方 | 受益描述 |
| --- | --- |
| 运营商 | 减少信令开销，节省网络资源。 |
| 用户 | 用户不感知该特性。 |

#### [应用场景](#ZH-CN_CONCEPT_0288816803)

Reflective QoS机制适用于不需要保证带宽的业务，如网页浏览等。

#### [可获得性](#ZH-CN_CONCEPT_0288816803)

**涉及NF**

| 涉及NF | 支持版本 | 功能说明 |
| --- | --- | --- |
| AMF | 无特殊要求 | - 通过N2节点将SMF提供的含RQA（Reflective QoS Attribute）的QoS profile传递给(R)AN。<br>- 将UDM上获取的签约数据参数UE-AMBR传递给(R)AN。 |
| SMF | 无特殊要求 | - 控制QoS flow。<br>- 提供QoS profile给(R)AN。<br>- 提供RQI（Reflective QoS Indication）、DL PDR（Packet Detection Rule）和策略执行给UPF。 |
| UPF | UDG 20.0.0及后续版本 | 在下行数据包包头中添加RQA、QFI（QoS Flow ID）。 |
| (R)AN | 无特殊要求 | - 根据QFI将数据包映射到无线承载上。<br>- 根据无线承载上接收到的数据包的QFI，在N3隧道头上标记QFI。 |
| UE | 无特殊要求 | - 支持Reflective QoS能力。<br>- 支持根据QoS rule将数据包映射到QoS flow，并负责QoS flow到无线资源的映射。 |
| PCF | 无特殊要求 | 下发移动性管理的策略控制功能。 |
| UDM | 无特殊要求 | 负责QoS相关签约数据注册、订阅和下发功能。 |

**License支持**

本特性只有获得了License许可后才能获得该特性的服务，对应的License控制项为 “82209870 LKV3G5SRQS01 支持Reflective QoS”。

#### [与其他特性的交互](#ZH-CN_CONCEPT_0288816803)

本特性不涉及与其他特性的交互。

#### [对系统的影响](#ZH-CN_CONCEPT_0288816803)

本特性对系统无影响。

#### [应用限制](#ZH-CN_CONCEPT_0288816803)

本特性无应用限制。

#### [原理概述](#ZH-CN_CONCEPT_0288816803)

5G QoS机制包括信令控制QoS机制 （原理详见 [5GC QoS](GWFD-010201 QoS与流量管理/实现原理/3GPP QoS/5GC QoS_72271794.md) ） 和Reflective QoS机制，两者可以在同一个PDU会话中并存。

信令控制QoS机制中，QoS rule由SMF通过信令下发给UE。Reflective QoS机制中，上行数据的QoS rule由UE根据下行数据包推演得出，无需通过信令控制QoS机制下发，如 [图1](#ZH-CN_CONCEPT_0288816803__fig104011332668) 所示。

**图1** Reflective QoS示意图

<br>

![](GWFD-020101 支持Reflective QoS_88816803.assets/zh-cn_image_0288816912.png)

> **说明**
> - RQI（Reflective QoS Indication）是UPF在N3/N9接口的数据包头上添加的反射QoS属性。
> - QFI（QoS Flow ID）是封装在N3/N9接口的数据包头上，用来标识一个QoS Flow。

UE收到带有RQI/QFI标识的数据包后，通过自行推演QoS rule来实现Reflective QoS，QoS rule的推演原理如 [图2](#ZH-CN_CONCEPT_0288816803__fig127318593461) 所示。

**图2** QoS rule推演原理

<br>

![](GWFD-020101 支持Reflective QoS_88816803.assets/zh-cn_image_0288817090.png)

> **说明**
> - SDF（Service Data Flow）是一组IP数据流，该组数据流具有相同的QoS。SDF模板可以将用户面流量分类，并映射到QoS流。
> - RQA（Reflective QoS Attribute）是Reflective QoS的属性，是一个可选参数。当QoS flow中指示了Reflective QoS属性，则(R)AN将RQI与QoS flow进行关联，用于指明该QoS flow是受制于Reflective QoS。 RQA在(R)AN建立UE上下文或在QoS flow增加和删除的时候，AMF通过N2节点通知给(R)AN。

#### [计费与话单](#ZH-CN_CONCEPT_0288816803)

本特性不涉及计费与话单。

#### [特性规格](#ZH-CN_CONCEPT_0288816803)

本特性无特殊规格。

#### [遵循标准](#ZH-CN_CONCEPT_0288816803)

| 标准类别 | 标准编号 | 标准名称 |
| --- | --- | --- |
| 3GPP | 23.501 | 3rd Generation Partnership Project；Technical Specification Group Services and System Aspects；System Architecture for the 5G System |

#### [发布历史](#ZH-CN_CONCEPT_0288816803)

| 特性版本 | 发布版本 | 发布说明 |
| --- | --- | --- |
| 01 | 20.0.0 | 首次发布。 |
