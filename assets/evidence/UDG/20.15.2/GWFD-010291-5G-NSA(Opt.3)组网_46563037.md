# GWFD-010291 5G NSA(Opt.3)组网

- [适用NF](#ZH-CN_CONCEPT_0246563037__1.3.1.1)
- [定义](#ZH-CN_CONCEPT_0246563037__1.3.2.1)
- [客户价值](#ZH-CN_CONCEPT_0246563037__1.3.3.1)
- [应用场景](#ZH-CN_CONCEPT_0246563037__1.3.4.1)
- [可获得性](#ZH-CN_CONCEPT_0246563037__1.3.5.1)
- [与其他特性的交互](#ZH-CN_CONCEPT_0246563037__1.3.6.1)
- [对系统的影响](#ZH-CN_CONCEPT_0246563037__1.3.7.1)
- [应用限制](#ZH-CN_CONCEPT_0246563037__1.3.8.1)
- [原理概述](#ZH-CN_CONCEPT_0246563037__1.3.9.1)
- [计费与话单](#ZH-CN_CONCEPT_0246563037__1.3.10.1)
- [特性规格](#ZH-CN_CONCEPT_0246563037__1.3.11.1)
- [遵循标准](#ZH-CN_CONCEPT_0246563037__1.3.12.1)
- [发布历史](#ZH-CN_CONCEPT_0246563037__1.3.13.1)

#### [适用NF](#ZH-CN_CONCEPT_0246563037)

SGW-U、PGW-U

#### [定义](#ZH-CN_CONCEPT_0246563037)

5G NSA (Non-Standalone) Option3/3a/3x组网是指通过升级EPC核心网设备并在LTE无线网络叠加部署NR（New Radio）gNodeB的方式，向5G SA网络架构平滑演进的组网解决方案。利用NSA的双连接（LTE-NR NSA Dual Connectivity ）性质使具有NSA双连接能力的终端与LTE基站和NR基站建立连接，实现数据的分流传输功能。

> **说明**
> NSA: Non-Standalone 非独立组网。就是以现有的LTE无线接入和核心网作为移动性管理和覆盖的锚点，新增5G接入的组网方式。

#### [客户价值](#ZH-CN_CONCEPT_0246563037)

| 受益方 | 受益描述 |
| --- | --- |
| 运营商 | 基于EPC核心网设备向5G网络平滑演进，缩短5G部署周期，节省设备投资。 |
| 用户 | 享受高速宽带无线业务。 |

#### [应用场景](#ZH-CN_CONCEPT_0246563037)

运营商现网已经部署4G网络，在向5G网络演进过程中，采用如下演进方案时可以部署本特性：

部署初期，将EPC核心网设备进行升级，无线网络叠加部署gNodeB。

#### [可获得性](#ZH-CN_CONCEPT_0246563037)

**涉及网元**

| **涉及网元** | **支持版本** | **功能说明** |
| --- | --- | --- |
| eNodeB | 无特殊要求 | - 支持通过E-RAB Modification Indication流程为UE创建或删除双连接。<br>- 能够将用户面数据在eNodeB和gNodeB间分流。 |
| SGW-C/PGW-C | UNC 20.3.2及后续版本 | 根据MME的指示为终端创建不同的用户面传输路径。 |
| SGW-U/PGW-U | UDG 20.3.2及后续版本 | 根据SGW-C/PGW-C的指示创建不同的用户面传输路径。 |

**License支持**

本特性无需获得License许可即可获得该特性的服务。

本特性无需配置即可使用。

#### [与其他特性的交互](#ZH-CN_CONCEPT_0246563037)

本特性不涉及与其他特性的交互。

#### [对系统的影响](#ZH-CN_CONCEPT_0246563037)

本特性对系统无影响。

#### [应用限制](#ZH-CN_CONCEPT_0246563037)

本特性无应用限制。

#### [原理概述](#ZH-CN_CONCEPT_0246563037)

本节包括如下内容：

5G NSA Option3/3a/3x三种组网解决方案，LTE eNodeB为主基站，gNodeB为辅基站。控制面信令都通过LTE eNodeB进行发送，用户面数据被分流到LTE eNodeB和gNodeB发送到UE。根据分流方式不同可以分为：Option3、Option3a和Option3x三种形式。Option3/3a/3x三种组网形式如下图所示：

**图1** Option3/3a/3x组网图

<br>

![](GWFD-010291 5G NSA(Opt.3)组网_46563037.assets/zh-cn_image_0249101617.png)

通常将用户面上下行业务分别承载在LTE和NR上，用LTE的上行覆盖能力弥补NR上行覆盖的不足，将UE的上行数据在LTE发送，而下行数据在NR发送。三种组网场景下用户面数据分流过程如下：

*表1 Option3*

| 数据分流锚点 | 数据分流过程 | 上下行数据流向 | 优缺点 |
| --- | --- | --- | --- |
| eNodeB | eNodeB可直接建立到gNodeB的用户面传输路径，eNodeB根据终端能力在PDCP层分流到gNodeB，网络侧不感知（无需核心网参与）。 | - 上行数据流向UE→eNodeB→EPCUE→gNodeB→eNodeB→EPC<br>- 下行数据流向EPC→eNodeB→UEEPC→eNodeB→gNodeB→UE | - eNodeB性能瓶颈问题上下行数据流均需经过eNodeB的处理，eNodeB的处理性能无疑成为5G网络高带宽、高速率的瓶颈。<br>- eNodeB升级改造成本高需对现网大量eNodeB基站进行改造，耗费成本较高。 |

*表2 Option3a*

| 数据分流锚点 | 数据分流过程 | 上下行数据流向 | 优缺点 |
| --- | --- | --- | --- |
| S-GW | eNodeB通过发起E-RAB Modification Indication流程，触发gNodeB和S-GW建立S1-U传输路径，将需要分流的承载切换到新建的S1-U上，在S-GW处分流到eNodeB和gNodeB。 | - 上行数据流向UE→eNodeB→EPCUE→gNodeB→EPC<br>- 下行数据流向EPC→eNodeB→UEEPC→gNodeB→UE | - 严重的丢包可能性核心网无法实时感知到空口信号变化的情况下，当终端移动到5G基站的小区边缘时，其空口传输能力变低，大量的下行数据有可能会导致丢包。<br>- 网络负载增高当LTE负载很高时，S-GW再向LTE分流必然引起系统负载更高。 |

*表3 Option3x*

| 数据分流锚点 | 数据分流过程 | 上下行数据流向 | 优缺点 |
| --- | --- | --- | --- |
| gNodeB | eNodeB通过发起E-RAB Modification Indication流程，触发gNodeB和S-GW建立S1-U传输路径。除此以外，Option 3x组网场景下gNodeB还可以根据需要将用户面数据在PDCP层分流到eNodeB（例如gNodeB带宽要达到瓶颈时）。如果需要分流，gNodeB直接建立到eNodeB的用户面传输路径，进行用户面数据分流（此步骤无需核心网参与）。 | - 上行数据流向UE→eNodeB→gNodeB→EPCUE→gNodeB→EPCUE→eNodeB→EPC<br>- 下行数据流向EPC→gNodeB→eNodeB→UEEPC→gNodeB→UEEPC→eNodeB→UE | - 移动场景下的高吞吐率和高容量通过LTE承载控制面数据，以保证移动性；NR承载用户面数据，实现高吞吐率和高容量。<br>- 现网改造小，5G体验佳通过gNodeB分流，减少了LTE现网的改造工作量；同时又保证了gNodeB可以基于空口信号情况实时调整分流到eNodeB的数据流量，最大程度保证了终端用户的5G体验。 |

在5G NSA Option3/3a/3x三种组网解决方案中，Option3a/3x两种组网需要在gNodeB与S-GW之间建立S1-U传输路径，以建立NR承载。NR承载创建过程对核心网而言主要是E-RAB MODIFICATION INDICATION处理流程：

<br>![](GWFD-010291 5G NSA(Opt.3)组网_46563037.assets/zh-cn_image_0246563040.png "点击放大")<br>

1. eNodeB根据当前用户业务类型、空口状态等信息判断需要为用户新建NR承载后，向MME发送E-RAB MODIFICATION INDICATION消息将需要分流的承载指向gNodeB。
2. MME向SGW发送MODIFY BEARER REQUEST消息（携带gNodeB IP地址信息），通知SGW将用户面传输路径从eNodeB切换到gNodeB。
3. SGW更新保存gNodeB的IP地址信息后通过MODIFY BEARER RESPONSE消息将更新结果返回给MME。
4. MME通过E-RAB MODIFICATION CONFIRM消息将更新结果通知给eNodeB。

#### [计费与话单](#ZH-CN_CONCEPT_0246563037)

本特性不涉及计费与话单。

#### [特性规格](#ZH-CN_CONCEPT_0246563037)

本特性无特殊规格。

#### [遵循标准](#ZH-CN_CONCEPT_0246563037)

| 标准类别 | 标准编号 | 标准名称 |
| --- | --- | --- |
| 3GPP | 23401 | 3rd Generation Partnership Project;<br>Technical Specification Group Services and System Aspects;<br>General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access |
| 3GPP | 36413 | 3rd Generation Partnership Project;<br>Technical Specification Group Radio Access Network;<br>Evolved Universal Terrestrial Radio Access Network (E-UTRAN);<br>S1 Application Protocol (S1AP) |
| 3GPP | 37340 | 3rd Generation Partnership Project;<br>Technical Specification Group Radio Access Network;<br>Evolved Universal Terrestrial Radio Access (E-UTRA) and NR;<br>Multi-connectivity |

#### [发布历史](#ZH-CN_CONCEPT_0246563037)

| 特性版本 | 发布版本 | 发布说明 |
| --- | --- | --- |
| 01 | 20.3.2 | 首次发布。 |
