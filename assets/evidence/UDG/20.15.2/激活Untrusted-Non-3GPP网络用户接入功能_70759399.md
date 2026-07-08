# 激活Untrusted Non-3GPP网络用户接入功能

- [操作场景](#ZH-CN_OPI_0270759399__1.3.1)
- [操作流程](#ZH-CN_OPI_0270759399__1.3.2)

## [操作场景](#ZH-CN_OPI_0270759399)

UDG 作为PGW-U部署Untrusted Non-3GPP接入EPC网络，Untrusted Non-3GPP用户可以通过PGW-U接入运营商网络，使用基本的数据业务。

> **说明**
> 适用于PGW-U。

## [操作流程](#ZH-CN_OPI_0270759399)

部署Untrusted Non-3GPP接入EPC网络的配置流程如 [图1](#ZH-CN_OPI_0270759399__fig1448412383515) 所示。本场景仅介绍 UDG 作为P-GW部署Untrusted Non-3GPP接入EPC网络的最小配置，在最小配置完成后，常用的可选功能/特性配置可按如 [图1](#ZH-CN_OPI_0270759399__fig1448412383515) 所示执行。

**图1** Untrusted Non-3GPP接入EPC网络配置流程

<br>

![](激活Untrusted Non-3GPP网络用户接入功能_70759399.assets/zh-cn_image_0274367796.png)

部署Untrusted Non-3GPP接入EPC网络时，需要操作员在 UDG 上进行数据配置实现以下要求：

- 用户接入运营商网络，使用基本的数据业务。
- UDG到OM网络使用配置到OM网络的数据。
- UDG 到Untrusted Non-3GPP GW，参考 [配置PGW-U到Untrusted Non-3GPP GW的数据（VPN+OSPF动态路由组网）（虚机容器）](激活Untrusted Non-3GPP网络用户接入功能/配置PGW-U到Untrusted Non-3GPP GW的数据（VPN+OSPF动态路由组网）（虚机容器）_72489252.md) 和 [配置PGW-U到Untrusted Non-3GPP GW的数据（VPN缺省路由组网）](激活Untrusted Non-3GPP网络用户接入功能/配置PGW-U到Untrusted Non-3GPP GW的数据（VPN缺省路由组网）_72489253.md) 进行配置。
- UDG上到PDN使用配置PGW-U到PDN的数据。
- 用户地址分配方式为本地地址池分配IPv4地址，参考[激活用户面地址分配](../GWFD-010105 用户面地址分配/激活用户面地址分配_87605803.md)。
- UDG使用整机缺省的DNS对用户访问地址进行域名解析。
