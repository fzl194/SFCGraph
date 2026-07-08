# OSPF IP FRR

- [产生原因](#ZH-CN_CONCEPT_0161317347__1.3.2.1)
- [相关概念](#ZH-CN_CONCEPT_0161317347__1.3.3.1)
- [组网应用](#ZH-CN_CONCEPT_0161317347__1.3.4.1)
- [多源路由场景中的OSPF IP FRR](#ZH-CN_CONCEPT_0161317347__1.3.5.1)
- [衍生功能](#ZH-CN_CONCEPT_0161317347__1.3.6.1)

OSPF IP FRR利用全网链路状态数据库，预先计算出备份路径保存在转发表中，以备在故障时提供流量保护，将故障恢复时间降低。

#### [产生原因](#ZH-CN_CONCEPT_0161317347)

随着网络的不断发展，VoIP和在线视频等业务对高质量和实时性的要求越来越高。OSPF协议的故障恢复过程是“故障感知->LSA更新->LSA泛洪->路由计算和下发FIB->故障恢复”，经过这几个过程才能让流量切换到新的链路上，因此故障恢复的时间远远超过了用户感知流量中断的时间，无法满足网络业务的实时性要求。通过OSPF IP FRR可以解决这个问题，OSPF IP FRR是遵循标准协议的动态IP FRR，可为流量提供链路和节点的保护，确保流量中断时间降低，实现链路故障后可以快速切换。

目前主要的FRR技术包括：无环替代冗余算法LFA（Loop-Free Alternate），U-turn，Not-Via，Remote-LFA和MRT，OSPF仅支持LFA。

#### [相关概念](#ZH-CN_CONCEPT_0161317347)

**OSPF IP FRR**

OSPF IP FRR利用LFA算法预先计算好备份下一跳路由，并与主链路路由一起加入转发表。当网络出现故障时，OSPF IP FRR可以在控制平面路由收敛前将流量快速切换到备份链路上，降低故障恢复时间，从而达到保护流量的目的。

**OSPF IP FRR Policy**

OSPF IP FRR Policy是指对需要加入IP路由表的备份路由进行过滤，通过过滤策略的备份路由才会加入到IP路由表中，这样用户可以更灵活的控制加入IP路由表的OSPF备份路由。

**LFA算法**

LFA算法计算备份链路的基本思路是：以可提供备份链路的邻居为根节点，利用SPF算法计算到达目的节点的最短距离，然后按照标准协议规定的不等式计算出开销最小且无环的备份链路。

#### [组网应用](#ZH-CN_CONCEPT_0161317347)

OSPF IP FRR流量保护分为链路保护和节点链路双保护，节点链路双保护的优先级高于链路保护的优先级。

**链路保护**

当需要保护的对象是经过特定链路的流量时，流量保护类型为链路保护。

如 [图1](#ZH-CN_CONCEPT_0161317347__fig784719478237) 所示，流量从DeviceS到DeviceD进行转发，主链路是DeviceS->DeviceE->DeviceD，备份链路是DeviceS->DeviceN->DeviceE->DeviceD。当链路开销满足不等式Distance_opt（N，D）<Distance_opt（N，S）+Distance_opt（S，D）时，配置OSPF IP FRR功能后，可以保证当主链路故障后，DeviceS将流量切换到备份链路转发，确保流量中断降低。

> **说明**
> Distance_opt（X，Y）指节点X到Y之间的最短路径，S是转发流量的源节点，N是备份链路的节点，D是流量转发的目的节点。

**图1** OSPF IP FRR链路保护

<br>

![](OSPF IP FRR_61317347.assets/zh-cn_image_0000001626271601_2.png)

**节点链路双保护**

当需要保护的对象是经过特定节点和链路的流量时，流量保护类型为节点链路双保护。

如 [图2](#ZH-CN_CONCEPT_0161317347__fig1146532213289) 所示，流量从DeviceS到DeviceD进行转发，主链路是DeviceS->DeviceE->DeviceD，备份链路是DeviceS->DeviceN->DeviceD。配置OSPF IP FRR功能后，可以保证当主链路故障后，DeviceS将流量切换到备份链路转发，确保流量中断降低。

节点链路双保护需同时满足如下两个条件：

- 链路开销必须满足Distance_opt（N，D）<Distance_opt（N，S）+Distance_opt（S，D）。
- 设备的接口开销必须满足Distance_opt（N，D）<Distance_opt（N，E）+Distance_opt（E，D）。

> **说明**
> Distance_opt（X，Y）指节点X到Y之间的最短路径，S是转发流量的源节点，E是发生故障的节点，N是备份链路的节点，D是流量转发的目的节点。

**图2** OSPF IP FRR节点链路双保护

<br>

![](OSPF IP FRR_61317347.assets/zh-cn_image_0000001575552430_2.png)

#### [多源路由场景中的OSPF IP FRR](#ZH-CN_CONCEPT_0161317347)

OSPF IP FRR是通过提供备份链路的邻居为根节点，利用SPF算法计算到达目的节点的最短距离，计算的结果是基于节点的备份下一跳，适合于单源路由场景。随着网络的多元化，某些网络中会部署双ABR或双ASBR，用来增强网络的可靠性，此时就产生了多源路由场景中的OSPF IP FRR。

> **说明**
> 在多源路由场景下，区域内、区域间、ASE/NSSA路由场景最终都会归结为对本区域ABR节点发布的Type-3 LSA进行FRR计算，因此，多源路由场景下的OSPF IP FRR计算方法一致。仅以区域间路由在多源场景下的FRR计算为例进行如下描述。

如 [图3](#ZH-CN_CONCEPT_0161317347__fig320410587358) 所示，Device B和Device C作为ABR来转发区域0和区域1间的路由。此时，Device D发布一条区域内路由，Device B和Device C会转换成Type-3 LSA向区域0洪泛。如果在Device A上使能OSPF IP FRR，Device A认为有两个邻居Device B和Device C，由于没有固定的邻居作为根节点，Device A无法进行FRR备份下一跳的计算。为了解决这个问题，在Device B和Device C之间构造一个虚拟节点Virtual Node，将多源路由转换为单源路由，然后按LFA算法计算虚拟节点的备份下一跳，多源路由从其创建的虚拟节点继承备份下一跳。

**图3** 多源路由场景下的OSPF IP FRR

<br>

![](OSPF IP FRR_61317347.assets/zh-cn_image_0000001625952085_2.png)

例如，Device B和Device C分别发布一条前缀10.1.1.0/24的路由，在Device A上使能OSPF IP FRR，由于10.1.1.0/24存在两个路由源Device B和Device C，DeviceA无法计算路由10.1.1.0/24的备份下一跳。

此时，根据路由10.1.1.0/24的两个路由源创建一个新虚拟节点Virtual Node，与DeviceB和DeviceC分别形成链路，DeviceB指向Virtual Node的链路开销值为0，DeviceC指向Virtual Node的链路开销值为5，Virtual Node指向DeviceB和DeviceC的链路开销值都是最大值Max-cost（65535），Virtual Node上发布一条前缀10.1.1.0/24，开销值是DeviceB和DeviceC发布的路由开销值的较小值。在DeviceA上将DeviceB和DeviceC发布的路由源10.1.1.0/24设置为无效路由源，只用Virtual Node发布的路由源进行计算，将多源路由10.1.1.0/24虚拟成单源路由10.1.1.0/24，然后按LFA算法计算Virtual Node的备份下一跳。

#### [衍生功能](#ZH-CN_CONCEPT_0161317347)

将BFD会话与OSPF IP FRR进行绑定，当BFD检测到接口链路故障后，BFD会话状态会变为Down并触发接口进行快速重路由，将流量从故障链路切换到备份链路上，从而达到流量保护的目的。
