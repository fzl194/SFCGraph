# BFD for BGP

- [组网](#ZH-CN_CONCEPT_0161317155__1.3.4.1)

BFD（Bidirectional Forwarding Detection）可为BGP协议提供更快速的链路故障检测。BGP协议通过周期性的向对等体发送报文来实现邻居检测机制。但这种机制检测到故障所需时间比较长，超过1秒钟。当数据达到G bit/s的速率等级时，这种机制的检测时间将导致大量数据丢失，无法满足电信级网络高可靠性的需求。

因此，BGP协议通过引入BFD for BGP特性，利用BFD的快速检测机制（检测到故障的时间可以达到毫秒级）即迅速发现BGP对等体间链路的故障，并报告给BGP协议，从而实现BGP路由的快速收敛。

> **说明**
> BFD for BGP功能只支持BGP单跳场景，不支持多跳场景。

#### [组网](#ZH-CN_CONCEPT_0161317155)

如 [图1](#ZH-CN_CONCEPT_0161317155__fig_dc_fenix_feature_bgp_001501) 所示， Device A和 Device B分别属于AS100和AS200，两台 UDG 直接相连并建立EBGP连接。

使用BFD检测 Device A和 Device B之间的BGP邻居关系，当 Device A和 Device B之间的链路发生故障时，BFD能够快速检测到故障并通告给BGP协议。

**图1** BFD for BGP组网图

<br>

![](BFD for BGP_61317155.assets/zh-cn_image_0161317179.png)
