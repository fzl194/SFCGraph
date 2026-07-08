# BGP Auto FRR

- [应用](#ZH-CN_CONCEPT_0161317165__1.3.3.1)

BGP Auto FRR是一种链路故障保护措施，应用于有主备链路的网络拓扑结构中。使能BGP Auto FRR，可以使BGP的两个邻居切换或者两个下一跳切换达到亚秒级的收敛速度。

BGP Auto FRR对于从不同对等体学到的相同前缀的路由，利用最优路由作为主链路进行转发，并自动将次优路由作为备份链路。当主链路出现故障的时候，系统快速响应BGP路由不可达的通知，将转发路径切换到备份链路上。

#### [应用](#ZH-CN_CONCEPT_0161317165)

如 [图1](#ZH-CN_CONCEPT_0161317165__fig_dc_fenix_feature_bgp_00400001) 所示， Device Y将学到的BGP路由发往AS100中的 Device X2和 Device X3，然后 Device X2和 Device X3通过反射器将路由发到 Device X1上， Device X1上收到下一跳为 Device X2和 Device X3的两份路由，配置策略优选其中一条链路上收到的路由，这里假设在 Device X1上优选从 Device X2发来的路由，备份链路是LinkB链路。

**图1** BGP Auto FRR示意图

<br>

![](BGP Auto FRR_61317165.assets/fig_dc_fenix_feature_bgp_00400001_2.png)

在 Device X1上使能Auto FRR，当域内LinkA经过的节点或者链路出现故障的时候， Device X1上到 Device X2的下一跳信息就会失效，触发转发平面迅速将从 Device X1到 Device Y流量快速切换到LinkB上，优先保证流量。同时， Device X1重新按照前缀进行选路，优选从 Device X3发来的路由并更新FIB。
