# BGP Best-external

- [产生原因](#ZH-CN_CONCEPT_0161317278__1.3.1.1)
- [相关概念](#ZH-CN_CONCEPT_0161317278__1.3.2.1)
- [主备PE典型组网](#ZH-CN_CONCEPT_0161317278__1.3.3.1)
- [主备RR典型组网](#ZH-CN_CONCEPT_0161317278__1.3.4.1)
- [适用场景](#ZH-CN_CONCEPT_0161317278__1.3.5.1)
- [使用价值](#ZH-CN_CONCEPT_0161317278__1.3.6.1)

#### [产生原因](#ZH-CN_CONCEPT_0161317278)

根据现有的选路规则，当到达同一目的地址存在多条路由时，BGP会优选出一条最优路由发送给邻居。

> **说明**
> BGP选路策略的详细介绍请参见《BGP基本原理》

但是，在主备PE（Provider Edge）或主备RR（Route Reflector）场景中，现有的BGP选路规则有可能造成无备用链路可用，从而导致链路故障时路由收敛时间过长。为了解决这一问题，设计实现了BGP Best-external特性。

#### [相关概念](#ZH-CN_CONCEPT_0161317278)

BGP Best-external：在使能了BGP Best-external特性的设备上，若其优选出的路由是IBGP路由，则选出次优路由发布给邻居，从而实现链路故障时路由的快速收敛。

Best-external路由：在使能了BGP Best-external特性的设备上，BGP选出的次优路由。

#### [主备PE典型组网](#ZH-CN_CONCEPT_0161317278)

如 [图1](#ZH-CN_CONCEPT_0161317278__fig_dc_fenix_feature_bgp_003401) 所示，CE1双归到PE1和PE2，为PE1设置较高的Local_Pref属性值。PE1和PE2分别与CE1建立EBGP邻居，PE1、PE2和PE3之间建立IBGP邻居。PE1和PE2分别从CE1收到同一条路由（例如10.1.1.1/32），同时PE2收到从PE1转发来的这条路由。由于PE1的Local_Pref属性值较高，PE2优选PE1传来的路由。根据路由传递规则，PE2不会再向PE3发送这条路由，即PE3只能收到一条PE1传来的一条路由。这样，一旦链路发生故障，路由需进行重新收敛才能把流量切换到备用链路上。

**图1** 主备PE典型组网

<br>

![](BGP Best-external_61317278.assets/fig_dc_fenix_feature_bgp_003401_2.png)

通过在PE2上使能BGP Best-external特性，可以使PE2选出最优的EBGP路由（CE1传来的路由）发送给PE3，形成备用链路。使能BGP Best-external特性前后路由传递与链路故障时的收敛情况如 [表1](#ZH-CN_CONCEPT_0161317278__table_dc_fenix_feature_bgp_003401) 所示。

*表1 使能BGP Best-external特性前后路由传递与链路故障时的收敛情况*

| 特性使能情况 | 路由传递情况 | 路由优选情况 | 链路故障时路由收敛情况 |
| --- | --- | --- | --- |
| 使能BGP Best-external特性前 | PE1只能收到一条路由：<br>CE1→PE1→PE3 | 优选通过路径CE1→PE1→PE3传来的路由 | PE1、PE2重新选路后，才可选出备用链路 |
| 使能BGP Best-external特性后 | PE3收到两条路由：<br>CE1→PE1→PE3<br>CE1→PE2→PE3 | 优选通过路径CE1→PE1→PE3传来的路由 | 流量可以直接切换到备用链路上 |

#### [主备RR典型组网](#ZH-CN_CONCEPT_0161317278)

如 [图2](#ZH-CN_CONCEPT_0161317278__fig_dc_fenix_feature_bgp_003402) 所示，RR1与RR2，RR1、RR2与 Device B、 Device C分别建立IBGP邻居， Device B是RR1和RR2的客户机。RR1和RR2分别从 Device B收到同一条路由（例如10.1.1.1/32），同时RR2从RR1收到转发来的这条路由。由于RR1的Local_Pref属性值较高，RR2优选RR1传来的路由。根据路由传递的规则，RR2不会再向 Device C发送这条路由，即 Device C只能收到RR1传来的一条路由。这样，一旦链路发生故障，路由需进行重新收敛才能把流量切换到备用链路上。

**图2** 主备RR典型组网

<br>

![](BGP Best-external_61317278.assets/fig_dc_fenix_feature_bgp_003402_2.png)

通过在RR2上使能BGP Best-external特性，可以使RR2选出最优的EBGP路由（ Device B传来的路由）发送给 Device C，形成备用链路。使能BGP Best-external特性前后路由传递与链路故障时的收敛情况如 [表2](#ZH-CN_CONCEPT_0161317278__table_dc_fenix_feature_bgp_003402) 所示。

*表2 使能BGP Best-external特性前后路由传递与链路故障时的收敛情况*

| 特性使能情况 | 路由传递情况 | 路由优选情况 | 链路故障时路由收敛情况 |
| --- | --- | --- | --- |
| 使能BGP Best-external特性前 | Device<br>C只能收到一条路由：<br>Device<br>A→<br>Device<br>B→RR1→<br>Device<br>C | 优选通过路径<br>Device<br>A→<br>Device<br>B→RR1→<br>Device<br>C传来的路由 | RR1、RR2重新选路后，才可选出备用链路 |
| 使能BGP Best-external特性后 | Device<br>C收到两条路由：<br>Device<br>A→<br>Device<br>B→RR1→<br>Device<br>C<br>Device<br>A→<br>Device<br>B→RR2→<br>Device<br>C | 优选通过路径<br>Device<br>A→<br>Device<br>B→RR1→<br>Device<br>C传来的路由 | 流量可以直接切换到备用链路上 |

#### [适用场景](#ZH-CN_CONCEPT_0161317278)

主备PE（Provider Edge）或主备RR（Route Reflector）等需要向邻居发布次优路由（Best-external路由）来实现链路故障时路由快速收敛的情景。

#### [使用价值](#ZH-CN_CONCEPT_0161317278)

随着网络的不断发展，语音、在线视频和金融等业务对实时性的要求越来越高。部署BGP Best-external特性后，若设备选出的路由是IBGP路由，则选出次优路由发布给邻居，从而实现链路故障时路由的快速收敛，减小流量中断对于业务的影响。
