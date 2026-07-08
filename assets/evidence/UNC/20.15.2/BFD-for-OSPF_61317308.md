# BFD for OSPF

网络上的链路故障或拓扑变化都会导致设备重新进行路由计算，所以缩短路由协议的收敛时间对于提高网络的性能是非常重要的。由于链路故障是无法完全避免的，因此，加快故障感知速度并将故障快速通告给路由协议是一种可行的方案。

OSPF通过周期性的向邻居发送Hello报文来实现邻居检测，检测到故障所需时间比较长，超过1秒钟。BFD和OSPF相关联，一旦与邻居之间的链路出现故障，将BFD对链路故障的快速感应通知OSPF协议，从而加快OSPF协议对于网络拓扑变化的响应。

*表1 有无BFD for OSPF功能对比*

| 有无BFD | 链路故障检测机制 | 收敛速度 |
| --- | --- | --- |
| 无BFD | OSPF Dead定时器超时（默认配置40s） | 秒级 |
| 有BFD | BFD会话状态为Down | 毫秒级 |

BFD for OSPF的原理如 [图1](#ZH-CN_CONCEPT_0161317308__f8980f5b9a3fc4f52aba04e52d90762f2) 所示：

**图1** BFD for OSPF

<br>

![](BFD for OSPF_61317308.assets/zh-cn_image_0161317211_2.png)

1. 三台设备间建立OSPF邻居关系。
2. 邻居状态到达Full状态时通知BFD建立BFD会话。
3. Device A到 Device B的路由出接口为interface 1，当这两台设备间的链路出现故障后，BFD首先感知到并通知 Device A。
4. Device A处理邻居Down事件，重新进行路由计算，新的路由出接口为interface 2，经过 Device C到达 Device B。
