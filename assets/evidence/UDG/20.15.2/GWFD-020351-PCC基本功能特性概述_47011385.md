# GWFD-020351 PCC基本功能特性概述

- [适用NF](#ZH-CN_TOPIC_0147011385__1.3.1.1)
- [定义](#ZH-CN_TOPIC_0147011385__1.3.2.1)
- [客户价值](#ZH-CN_TOPIC_0147011385__1.3.4.1)
- [应用场景](#ZH-CN_TOPIC_0147011385__1.3.5.1)
- [可获得性](#ZH-CN_TOPIC_0147011385__1.3.6.1)
- [与其他特性的交互](#ZH-CN_TOPIC_0147011385__1.3.7.1)
- [对系统的影响](#ZH-CN_TOPIC_0147011385__1.3.8.1)
- [应用限制](#ZH-CN_TOPIC_0147011385__1.3.9.1)
- [原理概述](#ZH-CN_TOPIC_0147011385__1.3.10.1)
- [计费与话单](#ZH-CN_TOPIC_0147011385__1.3.14.1)
- [特性规格](#ZH-CN_TOPIC_0147011385__1.3.15.1)
- [遵循标准](#ZH-CN_TOPIC_0147011385__1.3.16.1)
- [发布历史](#ZH-CN_TOPIC_0147011385__1.3.17.1)

#### [适用NF](#ZH-CN_TOPIC_0147011385)

PGW-U、UPF

#### [定义](#ZH-CN_TOPIC_0147011385)

PCC（Policy and Charging Control）是策略和计费控制。PCC基本功能用于在用户的业务流程中实现UE策略、移动性策略、会话策略和计费控制，通过区分业务并进行实时QoS控制，合理利用网络资源，提升数据业务流量的经营价值，丰富数据业务市场营销手段。

> **说明**
> PCC部署或改造需要评估现有网络的业务模型、资费策略、网络资源占用情况。具体部署或改造时，请联系华为公司当地办事处获取专门的系统集成服务支持。

#### [客户价值](#ZH-CN_TOPIC_0147011385)

| 受益方 | 受益描述 |
| --- | --- |
| 运营商 | 采用PCC基本功能，运营商可以在网络运营中进行统一的、多维度的策略部署和控制，包括实现业务级的QoS控制和计费、重定向、动态调整策略。在优化网络资源使用和提升网络用户体验的同时，提升管道的智能化水平，增强竞争力。 |
| 用户 | - 终端用户可以选择更为多样化的资费方案。<br>- 终端用户能够体会到更灵活的带宽控制带来的良好上网感受。 |

#### [应用场景](#ZH-CN_TOPIC_0147011385)

**图1** PCC基本功能应用场景

<br>

![](GWFD-020351 PCC基本功能特性概述_47011385.assets/zh-cn_image_0213750406.png)

#### [可获得性](#ZH-CN_TOPIC_0147011385)

**涉及NF**

| 涉及NF | 支持版本 | 功能说明 |
| --- | --- | --- |
| PGW-C/SMF | UNC 20.0.0及后续版本 | - 根据从PCRF/PCF收到的会话管理策略，将SDF（Service Data Flow）与QoS流绑定。<br>- 进行QoS、计费、门控、包路由和转发、流量转向等策略决策。<br>- 执行计费控制，向CHF上报话单。<br>- 运营商未部署PCRF/PCF时，根据本地配置策略进行会话策略控制。 |
| PGW-U/UPF | UDG 20.0.0及后续版本 | 根据PGW-C/SMF传递的PCC策略，执行如下操作：<br>- 执行业务数据流检测，统计业务流量/时长等使用量。<br>- 执行流量上报、QoS控制、带宽管理、重定向等策略控制。 |
| PCRF/PCF | 无特殊要求 | PCRF/PCF的主要功能是完成策略决策，提供基于业务的QoS策略、计费规则，绑定AF（Application Function）会话。<br>- 会话管理相关功能- 对SDF的策略和计费控制：完成策略授权，为PCC规则选择QoS参数，并向PGW-C/SMF下发规则。<br>- PDU会话相关策略控制：将AF会话信息和适用的PCC规则关联到一个PDU会话上。<br>- 向AF上报PDU会话事件：根据AF的请求向AF上报接入类型、 RAT Type，UE所在 PLMN ID等接入网信息。<br>- 非会话管理相关功能- 接入和移动性策略控制。<br>- UE接入选择和UE路由选择策略控制。 |
| SPR（Subscription Profile Repository）/UDR（User Data Repository） | 无特殊要求 | 存储用户数据的单个逻辑存储库，存储用户信息和业务签约信息，为PCF提供策略决策所需的签约输入。 |
| AF | 无特殊要求 | AF是应用功能实体，它可以由运营商部署并提供，也可以由第三方业务提供商提供。AF的主要功能是：<br>- 在UE发生相关应用业务时，向PCRF/PCF传送应用级别的会话信息，用于PCRF/PCF生成相关SDF的策略。<br>- 向PCRF/PCF订阅PDU会话事件通知以及DNAI改变通知，用于AF的业务管理。 |

**License支持**

本特性只有获得了License许可后才能获得该特性的服务，对应的License控制项为 “82209825 LKV3G5PCCB01 PCC 基本功能”。

#### [与其他特性的交互](#ZH-CN_TOPIC_0147011385)

本特性不涉及与其他特性的交互。

#### [对系统的影响](#ZH-CN_TOPIC_0147011385)

- 使用PCC功能，系统性能将下降，具体下降程度需要根据具体话务模型进行分析。
- 用户激活时，PGW-C/SMF需要与PCRF/PCF进行交互，获取用户策略并转换为N4接口的PDR下发到PGW-U/UPF，用户激活性能将下降。
- PGW-U/UPF需要动态处理PCRF/PCF下发的策略，将影响系统的报文处理过程，增加报文处理时延。

详细性能影响需要基于流量模型进行评估，请联系华为技术支持获取服务。

#### [应用限制](#ZH-CN_TOPIC_0147011385)

本特性无应用限制。

#### [原理概述](#ZH-CN_TOPIC_0147011385)

PCC架构主要由策略控制功能（PCRF/PCF）、策略控制执行功能（PGW-C/SMF和PGW-U/UPF）、接入和移动策略执行功能（AMF）、业务策略提供功能（AF）组成。

PCC基本功能的组网及接口如 [图2](#ZH-CN_TOPIC_0147011385__fig125307161217) 所示，用户使用5G业务时，通过LTE或者（R）AN接入网络，PCRF/PCF根据用户签约信息、业务信息或用户状态信息等进行决策，生成控制策略。PCRF/PCF通过N7接口将QoS及计费策略下发给PGW-C/SMF，PGW-C/SMF通过N4接口再下发给PGW-U/UPF，PGW-U/UPF基于用户和业务类型进行限速和门控，并且将QoS信息传递给无线、核心网共同进行端到端资源管理。

**图2** PCC基本功能特性组网结构图

<br>

![](GWFD-020351 PCC基本功能特性概述_47011385.assets/zh-cn_image_0263714500.png)

#### [计费与话单](#ZH-CN_TOPIC_0147011385)

本特性不涉及计费与话单。

#### [特性规格](#ZH-CN_TOPIC_0147011385)

本特性无特殊规格。

#### [遵循标准](#ZH-CN_TOPIC_0147011385)

| 标准类别 | 标准编号 | 标准名称 |
| --- | --- | --- |
| 3GPP | 23501 v15.2.0 | System Architecture for the 5G System; Stage 2 |
| 3GPP | 23502 v15.2.0 | Procedures for the 5G System; Stage 2 |
| 3GPP | 23503 v15.2.0 | Policy and Charging Control Framework for the 5G System; Stage 2 |
| 3GPP | 29507 v15.2.0 | 5G System; Access and Mobility Policy Control Service; Stage 3 |
| 3GPP | 29512 v15.2.0 | 5G System; Session Management Policy Control Service; Stage 3 |
| 3GPP | 29513 v15.2.0 | 5G System; Policy and Charging Control signalling flows and QoS parameter mapping; Stage 3 |

#### [发布历史](#ZH-CN_TOPIC_0147011385)

| 特性版本 | 发布版本 | 发布说明 |
| --- | --- | --- |
| 01 | 20.0.0 | 首次发布。 |
