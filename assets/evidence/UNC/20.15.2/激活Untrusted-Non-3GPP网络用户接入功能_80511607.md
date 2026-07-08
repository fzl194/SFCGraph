# 激活Untrusted Non-3GPP网络用户接入功能

- [操作场景](#ZH-CN_OPI_0280511607__1.3.1)
- [操作流程](#ZH-CN_OPI_0280511607__1.3.2)

## [操作场景](#ZH-CN_OPI_0280511607)

UNC 作为P-GW部署Untrusted Non-3GPP接入EPC网络，Untrusted Non-3GPP用户可以通过本P-GW接入运营商网络，使用基本的数据业务。

> **说明**
> 适用于PGW-C

## [操作流程](#ZH-CN_OPI_0280511607)

部署Untrusted Non-3GPP接入EPC网络的配置流程如 [图1](#ZH-CN_OPI_0280511607__fig1) 所示。本场景仅介绍 UNC 作为P-GW部署Untrusted Non-3GPP接入EPC网络的最小配置，在最小配置完成后，常用的可选功能/特性配置可按如 [图1](#ZH-CN_OPI_0280511607__fig1) 所示执行。

**图1** Untrusted Non-3GPP接入EPC网络配置流程

<br>

![](激活Untrusted Non-3GPP网络用户接入功能_80511607.assets/zh-cn_image_0280511695_2.png)

<br>

部署Untrusted Non-3GPP接入EPC网络时，需要操作员在 UNC 上进行数据配置实现以下要求：

- 用户接入运营商网络，使用基本的数据业务。
- UNC到OM网络使用配置到OM网络的数据。
- UNC 到Untrusted Non-3GPP GW，请参考 [组网路由配置](../../../../初始配置/UNC初始配置与调测/组网路由配置_24779181.md) 进行配置。
- UNC上到PDN使用配置P-GW/GGSN到PDN的数据。
- UNC使用整机缺省的DNS对用户访问地址进行域名解析。
