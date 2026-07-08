# OSPFv3 IP FRR

- [特性背景](#ZH-CN_CONCEPT_0161317191__1.3.3.1)
- [实现原理](#ZH-CN_CONCEPT_0161317191__1.3.4.1)
- [组网应用](#ZH-CN_CONCEPT_0161317191__1.3.5.1)
- [多源路由场景中的OSPFv3 FRR](#ZH-CN_CONCEPT_0161317191__1.3.6.1)

OSPFv3 IP FRR是动态IP FRR，利用全网链路状态数据库，预先计算出备份路径，保存在转发表中，以备在故障时提供流量保护，可将故障恢复时间降低。

OSPFv3 IP FRR可为流量提供链路和节点的保护。

#### [特性背景](#ZH-CN_CONCEPT_0161317191)

随着网络的不断发展，VoIP和在线视频等业务对实时性的要求越来越高，而OSPFv3故障恢复需要经历“故障感知、LSA更新、LSP泛洪、路由计算和下发FIB”这几个过程才能让流量切换到新的链路上，因此故障恢复的时间远远超过了用户感知流量中断的时间，不能满足此类网络业务的实时性要求。

#### [实现原理](#ZH-CN_CONCEPT_0161317191)

OSPFv3 IP FRR利用LFA算法预先计算好备份链路，并与主链路一起加入转发表。当网络出现故障时，OSPFv3 IP FRR可以在控制平面路由收敛前将流量快速切换到备份链路上，保证流量不中断，从而达到保护流量的目的，因此极大的提高了OSPFv3网络的可靠性。

LFA计算备份链路的基本思路是：以可提供备份链路的邻居为根节点，利用SPF算法计算出到目的节点的最短距离。然后，按照标准协议规定的不等式计算出开销最小且无环的备份链路。

OSPFv3 IP FRR支持对需要加入IP路由表的备份路由进行过滤，通过过滤策略的备份路由才会加入到IP路由表，因此，用户可以更灵活的控制加入IP路由表的OSPF备份路由。

将BFD会话与OSPFv3 IP FRR进行绑定，当BFD检测到接口链路故障后，BFD会话状态会变为Down并触发接口进行快速重路由，将流量从故障链路切换到备份链路上，从而达到流量保护的目的。

#### [组网应用](#ZH-CN_CONCEPT_0161317191)

OSPFv3 Auto FRR流量保护分为链路保护和节点链路双保护。

- **链路保护** ：当需要保护的对象是经过特定链路的流量时，流量保护类型为链路保护。
  如 [图1](#ZH-CN_CONCEPT_0161317191__ff3af0a40325043bd8f83fc7a980daa36) 所示，流量从DeviceS到DeviceD进行转发，网络开销值满足链路保护公式，可保证当主链路故障后，DeviceS将流量切换到备份链路DeviceS到DeviceN后可以继续向下游转发，确保流量中断时间降低。
  > **说明**
  > 链路开销必须满足不等式Distance_opt（N，D）<Distance_opt（N，S）+Distance_opt（S，D）。
  >
  > - Distance_opt（X，Y）：节点X到Y之间的最短路径。
  > - S：转发流量的源节点。
  > - N：备份链路的节点。
  > - D：流量转发的目的节点。
  **图1** OSPFv3 IP FRR链路保护

  <br>

  ![](OSPFv3 IP FRR_61317191.assets/zh-cn_image_0161317240.png)

  <br>
- **节点链路双保护** ： [图2](#ZH-CN_CONCEPT_0161317191__f9f945b18611a4649bea833979564152c) 所示的为节点链路双保护。节点链路双保护优先级高于链路保护。
  节点链路双保护需同时满足如下两个条件：
    - 链路开销必须满足Distance_opt（N，D）<Distance_opt（N，S）+Distance_opt（S，D）。
    - 设备的接口开销必须满足Distance_opt（N，D）<Distance_opt（N，E）+Distance_opt（E，D）。
  其中，S是转发流量的源节点，E是发生故障的节点，N是备份链路的节点，D是流量转发的目的节点。
  **图2** OSPFv3 IP FRR节点链路双保护

  <br>

  ![](OSPFv3 IP FRR_61317191.assets/zh-cn_image_0161317329.png)

  <br>

#### [多源路由场景中的OSPFv3 FRR](#ZH-CN_CONCEPT_0161317191)

OSPFv3 IP FRR是通过提供备份链路的邻居为根节点，利用SPF算法计算到达目的节点的最短距离，计算的结果是基于节点的备份下一跳，适合于单源路由场景。随着网络的多元化，某些网络中会部署双ABR或双ASBR，用来增强网络的可靠性，此时就产生了多源路由场景中的OSPFv3 FRR。

> **说明**
> 在多源路由场景下，区域内、区域间、ASE路由场景最终都会归结为对本区域ABR节点发布的Type-3 LSA进行FRR计算，因此，多源路由场景下的OSPFv3 FRR计算方法一致。仅以区域间路由在多源场景下的FRR计算为例进行如下描述。

**图3** 多源路由场景下的OSPFv3 FRR

<br>

![](OSPFv3 IP FRR_61317191.assets/zh-cn_image_0161317313.png)

如 [图3](#ZH-CN_CONCEPT_0161317191__f2d2da1c7b10849dd8c8d1baf8e066d88) 所示，DeviceB和DeviceC作为ABR来转发区域0和区域1间的路由。此时，DeviceE发布一条区域内路由，DeviceB和DeviceC会转换成Type-3 LSA向区域0洪泛。如果在DeviceA上使能OSPFv3 FRR，DeviceA认为有两个邻居DeviceB和DeviceC，由于没有固定的邻居作为根节点，DeviceA无法进行FRR备份下一跳的计算。为了解决这个问题，在DeviceB和DeviceC之间构造一个虚拟节点Virtual Node，将多源路由转换为单源路由，然后按LFA算法计算虚拟节点的备份下一跳，多源路由从其创建的虚拟节点继承备份下一跳。

例如，DeviceB和DeviceC分别发布一条前缀2001:DB8:1::1/64的路由，在DeviceA上使能OSPFv3 FRR，由于2001:DB8:1::1/64存在两个路由源DeviceB和DeviceC，DeviceA无法计算路由2001:DB8:1::1/64的备份下一跳。此时，根据路由2001:DB8:1::1/64的两个路由源创建一个新虚拟节点Virtual Node，与DeviceB和DeviceC分别形成链路，DeviceB指向Virtual Node的链路开销值为0，DeviceC指向Virtual Node的链路开销值为5，Virtual Node指向Device和DeviceC的链路开销值都是最大值Max-cost（65535），Virtual Node上发布一条前缀2001:DB8:1::1/64，开销值是DeviceB和DeviceC发布的路由开销值的较小值。在DeviceA上将DeviceB和DeviceC发布的路由源2001:DB8:1::1/64设置为无效路由源，只用Virtual Node发布的路由源进行计算，将多源路由2001:DB8:1::1/64虚拟成单源路由2001:DB8:1::1/64，然后按LFA算法计算Virtual Node的备份下一跳。
