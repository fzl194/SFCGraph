# GWFD-010284 UDG Termination

- [适用NF](#ZH-CN_CONCEPT_0162949607__1.3.1.1)
- [定义](#ZH-CN_CONCEPT_0162949607__1.3.2.1)
- [客户价值](#ZH-CN_CONCEPT_0162949607__1.3.3.1)
- [应用场景](#ZH-CN_CONCEPT_0162949607__1.3.4.1)
- [可获得性](#ZH-CN_CONCEPT_0162949607__1.3.5.1)
- [与其他特性的交互](#ZH-CN_CONCEPT_0162949607__1.3.6.1)
- [对系统的影响](#ZH-CN_CONCEPT_0162949607__1.3.7.1)
- [应用限制](#ZH-CN_CONCEPT_0162949607__1.3.8.1)
- [实现原理](#ZH-CN_CONCEPT_0162949607__1.3.9.1)
- [计费与话单](#ZH-CN_CONCEPT_0162949607__1.3.10.1)
- [特性规格](#ZH-CN_CONCEPT_0162949607__1.3.11.1)
- [遵循标准](#ZH-CN_CONCEPT_0162949607__1.3.12.1)
- [发布历史](#ZH-CN_CONCEPT_0162949607__1.3.13.1)

#### [适用NF](#ZH-CN_CONCEPT_0162949607)

UDG

#### [定义](#ZH-CN_CONCEPT_0162949607)

GWFD-010284 UDG Termination 是将已经实例化的VNF (Virtual Network Function) 根据用户的需求终止并删除的过程，是VNF生命周期中实现相关功能的重要操作。

#### [客户价值](#ZH-CN_CONCEPT_0162949607)

| 受益方 | 受益描述 |
| --- | --- |
| 运营商 | 为用户提供将整个网元Termination的功能，方便用户删除已经实例化的VNF。 |
| 用户 | 用户不感知该特性。 |

#### [应用场景](#ZH-CN_CONCEPT_0162949607)

VNF生命周期管理是一组基本操作，包含实例化、扩缩容和Termination等，这些操作对VNF提供其预期的功能来说是必需的。

#### [可获得性](#ZH-CN_CONCEPT_0162949607)

**版本支持**

| 产品 | 支持版本 | 功能说明 |
| --- | --- | --- |
| UDG | 20.9.0<br>及后续版本 | 配合VNFM进行下线前的业务检查。 |
| U2020 | V300R019C10及后续版本 | VNFM和FusionStage要求删除VNF实例对应的基础设施资源和服务资源。 |
| MAE | V100R020C10及后续版本 | VNFM和FusionStage要求删除VNF实例对应的基础设施资源和服务资源。 |
| FusionStage | 6.5.1及后续版本 | VNFM和FusionStage要求删除VNF实例对应的基础设施资源和服务资源。 |

**License支持**

本特性无需获得License许可即可获得该特性的服务。

本特性无需配置即可使用。

#### [与其他特性的交互](#ZH-CN_CONCEPT_0162949607)

本特性不涉及与其他特性的交互。

#### [对系统的影响](#ZH-CN_CONCEPT_0162949607)

![](GWFD-010284 UDG Termination_62949607.assets/notice_3.0-zh-cn.png)

本特性将会卸载 UDG ，卸载后在网用户业务终止、新用户无法接入。

#### [应用限制](#ZH-CN_CONCEPT_0162949607)

本特性无应用限制。

#### [实现原理](#ZH-CN_CONCEPT_0162949607)

**相关概念**

- VNFM（VNF Manager）
  VNFM负责VNF实例的生命周期管理，例如网元的实例化、扩缩容、删除等。
- FusionStage
  基于开源容器集群管理平台Kubernetes的华为应用（Pod）管理系统，用于进行Pod的创建和调度。
- 堆栈
  堆栈是一组应用和服务的集合，作为一个整体进行创建、升级、删除等，是部署模板实例化后的产品形态。一般产品由1~2个堆栈组成。

**UDG Termination流程**

UDG Termination流程如 [图1](#ZH-CN_CONCEPT_0162949607__fig686194163114) 所示。

**图1** UDG Termination流程

<br>

![](GWFD-010284 UDG Termination_62949607.assets/zh-cn_image_0173365468.png "点击放大")

1. 工程师按需执行VNF下线预操作，例如将现网业务割出，导出VNF的硬盘话单，备份VNF的OM等运维信息。
2. 工程师在VNFM界面启动VNF下线操作。
3. VNFM向VNF发送preVNFDeleteNotify消息，通知VNF进行下线前的预处理 。
4. VNF判断没有承载业务，并且没有存储关键数据，则允许下线，返回Notify Completion响应。
5. VNFM调用FusionStage执行生命周期操作，停止堆栈，然后删除堆栈。
6. VNFM在删除业务堆栈成功后，调用FusionStage的接口取消VM节点纳管。
7. VNFM删除VM资源。

#### [计费与话单](#ZH-CN_CONCEPT_0162949607)

本特性不涉及计费与话单。

#### [特性规格](#ZH-CN_CONCEPT_0162949607)

本特性无特殊规格。

#### [遵循标准](#ZH-CN_CONCEPT_0162949607)

| 标准类别 | 标准编号 | 标准名称 |
| --- | --- | --- |
| ETSI | GS NFV-MAN 001 | Network Functions Virtualisation (NFV);Management and Orchestration |
| ETSI | GS NFV-SWA 001 | Network Functions Virtualisation (NFV);Virtual Network Functions Architecture |

#### [发布历史](#ZH-CN_CONCEPT_0162949607)

| 特性版本 | 发布版本 | 发布说明 |
| --- | --- | --- |
| 01 | 20.0.0 | 首次发布。 |
