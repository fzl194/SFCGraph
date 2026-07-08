# BFD for OSPFv3

- [定义](#ZH-CN_CONCEPT_0000001575402910__1.3.1.1)
- [目的](#ZH-CN_CONCEPT_0000001575402910__1.3.2.1)
- [原理](#ZH-CN_CONCEPT_0000001575402910__1.3.3.1)

#### [定义](#ZH-CN_CONCEPT_0000001575402910)

双向转发检测BFD（Bidirectional Forwarding Detection）是一种用于检测转发引擎之间通信故障的检测机制。

BFD对两个系统间的、同一路径上的同一种数据协议的连通性进行检测，这条路径可以是物理链路或逻辑链路，包括隧道。

BFD for OSPFv3就是将BFD和OSPFv3协议关联起来，将BFD对链路故障的快速感应通知OSPFv3协议，从而加快OSPFv3协议对于网络拓扑变化的响应。

#### [目的](#ZH-CN_CONCEPT_0000001575402910)

网络上的链路故障或拓扑变化都会导致设备重新进行路由计算，所以缩短路由协议的收敛时间对于提高网络的性能是非常重要的。

由于链路故障是无法完全避免的，因此，加快故障感知速度并将故障快速通告给路由协议是一种可行的方案。BFD和路由协议相关联，一旦链路出现故障，BFD的快速性能够加快路由协议的收敛速度。

*表1 BFD for OSPFv3*

| 有无BFD | 链路故障检测机制 | 收敛速度 |
| --- | --- | --- |
| 无BFD | OSPFv3 Dead定时器超时（默认配置40s） | 秒级 |
| 有BFD | BFD会话状态为Down | 毫秒级 |

#### [原理](#ZH-CN_CONCEPT_0000001575402910)

**图1** BFD for OSPFv3

<br>

![](BFD for OSPFv3_75402910.assets/fig_dc_fenix_nls_ip_feature_ospfv3_000401.png)

BFD for OSPFv3的原理如 [图1](#ZH-CN_CONCEPT_0000001575402910__fig_dc_fenix_nls_ip_feature_ospfv3_000401) 所示：

1. 三台设备间建立OSPF邻居关系。
2. 邻居状态到达Full状态时通知BFD建立BFD会话。
3. DeviceA到DeviceB的路由出接口为interface 1，当这两台设备间的链路出现故障后，BFD首先感知到并通知DeviceA。
4. DeviceA处理邻居Down事件，重新进行路由计算，新的路由出接口为interface 2，经过DeviceC到达DeviceB。
