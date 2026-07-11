# BGP/MPLS IPv6 VPN

在BGP/MPLS IP VPN网络中，PE和PE之间、PE和CE之间都运行IPv4的路由协议，如BGP，OSPF等等。当VPN客户网络从IPv4演进到IPv6后，PE与CE之间运行上述路由协议不再适用，并且在骨干网上传送的是IPv6 VPN报文。BGP/MPLS IPv6 VPN扩展使得VPN骨干网不必升级到IPv6网络，就可以给客户提供IPv6的VPN服务。

> **说明**
> BGP/MPLS IPv6 VPN组网方案包括两种：
>
> - IPv6 VPN业务由服务提供商的IPv4骨干网来实现，此种方案又被称为6VPE方案。
> - IPv6 VPN业务由服务提供商的IPv6骨干网来实现。
>
> 当前仅支持6VPE方案。

[图1](#ZH-CN_CONCEPT_0000001745030732__zh-cn_concept_0134578943_fig_dc_vrp_mpls-l3vpn-v4_feature_001001) 为BGP/MPLS IPv6 VPN扩展模型，扩展后的网络PE和CE之间运行的是IPv6的路由协议，可以选择以下IPv6路由协议为用户提供IPv6的VPN服务。

- BGP4+
- 静态IPv6路由
- OSPFv3

**图1** BGP/MPLS IPv6 VPN扩展模型

<br>

![](BGP_MPLS IPv6 VPN_45030732.assets/zh-cn_image_0000001745030852.png)

在提供IPv6 VPN服务的同时，PE和PE之间的运营商骨干网仍然运行IPv4协议。这样，可以使运营商网络逐步从IPv4过渡到IPv6。

PE之间使用IPv4地址建立VPNv6邻居，传递VPN-IPv6路由，VPN-IPv6路由可以选择骨干网中的IPv4隧道来承载IPv6 VPN业务。

BGP/MPLS IPv6 VPN除PE和CE之间运行的路由协议与IPv4 VPN不同外，其它所有特性原理都与IPv4相同，见 [**MPLS VPN**](../GWFD-020411 MPLS VPN_45030708.md) 。
