# AMF和LMF/GMLC对接（直接模式）

- [操作场景](#ZH-CN_OPI_0000001621933426__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001621933426__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001621933426__1.3.3)
- [任务示例](#ZH-CN_OPI_0000001621933426__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001621933426)

本操作用于在AMF和LMF/GMLC采用直连方式对接场景，指导在AMF上如何进行配置。

## [必备事项](#ZH-CN_OPI_0000001621933426)

前提条件

已完成AMF初始配置，包括IP路由数据以及AMF基础数据配置参见《UNC初始配置与调测》> [组网对接配置](../../../../../初始配置/UNC初始配置与调测/组网对接配置_29162821.md) 。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD PNFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md) | NF实例标识（NFINSTANCEID） | - LMF_Instance_0<br>- GMLC_Instance_0 | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md) | NF类型（NFTYPE） | - NfLMF<br>- NfGMLC | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md) | NF状态（NFSTATUS） | Registered | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md) | 域名（FQDN） | - lmf0.huawei.com<br>- gmlc0.huawei.com | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md) | PLMN间域名（INTERPLMNFQDN） | - lmf0.mcc460.mnc02.huawei.com<br>- gmlc0.mcc460.mnc02.huawei.com | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md) | IP地址类型（IPADDRESSTYPE） | IPTypeV4 | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md) | IPV4地址1（IPV4ADDRESS1） | - 10.107.65.183<br>- 10.107.65.184 | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md) | 端口号（PORT） | 8080 | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md) | 位置信息（LOCALITY） | SHANGHAI | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFSERVICE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例信息管理/增加对端NF服务实例信息（ADD PNFSERVICE）_09652978.md) | NF实例标识（NFINSTANCEID） | - LMF_Instance_0<br>- GMLC_Instance_0 | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFSERVICE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例信息管理/增加对端NF服务实例信息（ADD PNFSERVICE）_09652978.md) | 服务实例标识（SRVINSTANCEID） | Service_Instance_0 | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFSERVICE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例信息管理/增加对端NF服务实例信息（ADD PNFSERVICE）_09652978.md) | 服务名称（SERVICENAME） | NlmfLoc/NgmlcLoc | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFSERVICE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例信息管理/增加对端NF服务实例信息（ADD PNFSERVICE）_09652978.md) | 协议模式（SCHEMA） | http | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFSERVICE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例信息管理/增加对端NF服务实例信息（ADD PNFSERVICE）_09652978.md) | 服务实例状态（NFSERVICESTATUS） | REGISTERED | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFSERVICE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例信息管理/增加对端NF服务实例信息（ADD PNFSERVICE）_09652978.md) | 域名（FQDN） | - lmf0.huawei.com<br>- gmlc0.huawei.com | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFSERVICE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例信息管理/增加对端NF服务实例信息（ADD PNFSERVICE）_09652978.md) | PLMN间域名（INTERPLMNFQDN） | - lmf0.mcc460.mnc02.huawei.com<br>- gmlc0.mcc460.mnc02.huawei.com | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md) | NF实例标识（NFINSTANCEID） | - LMF_Instance_0<br>- GMLC_Instance_0 | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md) | 服务实例标识（SRVINSTANCEID） | Service_Instance_0 | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md) | 回调URI通知类型（NTFICATIONTYPE） | LocNty | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md) | 回调URI（CALLBACKURI） | - http://10.60.103.60:19999/nlmf-loc/hlmf/v1/provide-location<br>- http://10.60.103.18:19999/ngmlc-loc/hgmlc/v1/provide-location | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md) | N1消息类别（N1MESSAGECLASS） | Lpp | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md) | N2消息类别（N2INFOCLASS） | Nrppa | 全网规划 | - AMF使用本地配置对接LMF、GMLC时的配置。- AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。- LMF和GMLC需要分别配置<br>- [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。 |
| [**SET NFDISCPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/NF发现策略管理/设置NF的服务发现策略（SET NFDISCPLCY）_09651764.md) | 服务发现策略（POLICY） | REMOTE_ONLY | 本端规划 | AMF使用NRF进行服务发现LMF/GMLC。<br>“服务发现策略”<br>取值为非<br>“LOCAL_ONLY”<br>时，都可能使用到NRF选择方式，此次仅为举例。 |
| [**ADD PNFPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例PLMN管理/增加对端NF的PLMN信息（ADD PNFPLMN）_09651368.md) | NF实例标识（NFINSTANCEID） | - LMF_Instance_0<br>- GMLC_Instance_0 | 全网规划 | 增加本地配置的对端NF实例支持的PLMN信息。 |
| [**ADD PNFPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例PLMN管理/增加对端NF的PLMN信息（ADD PNFPLMN）_09651368.md) | 移动国家码（MCC） | 460 | 全网规划 | 增加本地配置的对端NF实例支持的PLMN信息。 |
| [**ADD PNFPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例PLMN管理/增加对端NF的PLMN信息（ADD PNFPLMN）_09651368.md) | 移动网号（MNC） | 03 | 全网规划 | 增加本地配置的对端NF实例支持的PLMN信息。 |

## [操作步骤](#ZH-CN_OPI_0000001621933426)

1. 进入 “MML命令行-UNC” 窗口。
2. **可选：**AMF使用本地配置方式，AMF本地配置LMF/GMLC实例和服务实例信息。
  > **说明**
  > - AMF使用的LMF、GMLC可以通过本地配置方式对接，也可以通过NRF查找，需要根据实际现网规划选择对应的方式。[2](#ZH-CN_OPI_0000001621933426__cmd1141302389)为本地配置方式，[3](#ZH-CN_OPI_0000001621933426__cmd53092632915)为通过NRF查找时的可选配置。AMF通过[**SET NFDISCPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/NF发现策略管理/设置NF的服务发现策略（SET NFDISCPLCY）_09651764.md)命令的“POLICY”参数取值来决定优先使用哪种方式选择LMF/GMLC。
  > - 对于AMF选择LMF，AMF也可以通过SUPI/GPSI号段或切片信息本地选择LMF，对接配置请参考[激活基于号段选择LMF](../../WSFD-106406 基于号段选择LMF/激活基于号段选择LMF_69042496.md)、[激活LMF选择功能](../../WSFD-106407 LMF选择功能/激活LMF选择功能_58578942.md)，如果还需要配置特有信息、服务实例回调信息等，请参考本页面。
  > - AMF使用本地配置方式时需要配置[**ADD PNFPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例PLMN管理/增加对端NF的PLMN信息（ADD PNFPLMN）_09651368.md)命令。
  > - 如果不进行本地配置，AMF自动使用NRF查找方式根据LMF/GMLC的目标NFType选择。
    - 配置LMF/GMLC实例基础信息。
      [**ADD PNFPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端NF实例概述信息管理/增加对端NF实例概述信息（ADD PNFPROFILE）_09653772.md)
    - **可选：**配置LMF/GMLC实例特有信息。
      > **说明**
      > 根据现网业务需要配置LMF/GMLC的特有属性信息，例如针对LMF/GMLC如果只支持某种特有外部客户端类型，则需要配置如下命令。
      **[ADD PNFLMFINFO](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端LMF信息管理/增加对端LMF的信息（ADD PNFLMFINFO）_02870338.md)**
      **[ADD PNFGMLCINFO](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端GMLC信息管理/增加对端GMLC的信息（ADD PNFGMLCINFO）_02910210.md)**
    - 配置LMF/GMLC支持的服务实例信息。
      [**ADD PNFSERVICE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例信息管理/增加对端NF服务实例信息（ADD PNFSERVICE）_09652978.md)
    - **可选：**配置LMF/GMLC支持的服务实例回调信息。
      > **说明**
      > 此配置适用于订阅通知场景，如果LMF/GMLC订阅了AMF，则AMF通过此配置向对应的回调信息发送订阅通知。
      [**ADD PNFSRVNTFSUBS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/对端服务实例回调管理/增加对端NF服务实例的回调信息（ADD PNFSRVNTFSUBS）_09652612.md)
3. **可选：**AMF使用NRF服务发现方式选择LMF/GMLC。
  [**SET NFDISCPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/NF发现策略管理/设置NF的服务发现策略（SET NFDISCPLCY）_09651764.md)

## [任务示例](#ZH-CN_OPI_0000001621933426)

任务描述

开启网络侧发起的5G位置定位服务，AMF本地配置LMF/GMLC实例和服务实例：

- 增加对端LMF实例的概述信息，NF实例标识为LMF_Instance_0，NF类型为NfLMF，NF状态为Registered，域名为lmf0.huawei.com，PLMN间域名FQDN为lmf0.mcc460.mnc02.huawei.com，IP地址类型为IPv4，IPV4ADDRESS1为10.107.65.183，PORT为8080，LOCALITY为SHANGHAI。
  增加对端LMF的服务实例信息，NF实例标识为LMF_Instance_0，服务实例标识为Service_Instance_0，服务名为NlmfLoc，支持的协议为http。
  增加对端NF的服务实例回调信息，NF实例标识为LMF_Instance_0，服务实例标识为Service_Instance_0，通知类型为LocNty，回调URI为"http://10.60.103.60:19999/nlmf-loc/hlmf/v1/provide-location"。
- 增加对端GMLC实例的概述信息，NF实例标识为GMLC_Instance_0，NF类型为NfGMLC，NF状态为Registered，域名为huawei.com，PLMN间域名FQDN为huawei1.com，IP地址类型为IPv4，IPV4ADDRESS1为10.107.65.184，PORT为8080，LOCALITY为SHANGHAI。
  增加对端LMF的服务实例信息，NF实例标识为GMLC_Instance_0，服务实例标识为Service_Instance_1，服务名为NgmlcLoc，支持的协议为http。
  增加对端NF的服务实例回调信息，NF实例标识为GMLC_Instance_0，服务实例标识为Service_Instance_1，通知类型为LocNty，回调URI为"http://10.60.103.18:19999/ngmlc-loc/hgmlc/v1/provide-location"。

脚本

//AMF本地配置LMF实例和服务实例。

```
ADD PNFPROFILE: NFINSTANCEID="LMF_Instance_0", NFTYPE=NfLMF, NFSTATUS=Registered, FQDN="lmf0.huawei.com", INTERPLMNFQDN="lmf0.mcc460.mnc02.huawei.com", IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS1="10.107.65.183", PORT=8080, LOCALITY="SHANGHAI";
```

```
ADD PNFSERVICE: NFINSTANCEID="LMF_Instance_0", SRVINSTANCEID="Service_Instance_0", SERVICENAME=NlmfLoc, SCHEMA=http, NFSERVICESTATUS=REGISTERED, FQDN="lmf0.huawei.com", INTERPLMNFQDN="lmf0.mcc460.mnc02.huawei.com";
```

```
ADD PNFSRVNTFSUBS: NFINSTANCEID="LMF_Instance_0", SRVINSTANCEID="Service_Instance_0", NTFICATIONTYPE=LocNty, CALLBACKURI="http://10.60.103.60:19999/nlmf-loc/hlmf/v1/provide-location", N1MESSAGECLASS=Lpp, N2INFOCLASS=Nrppa;
```

//AMF本地配置GMLC实例和服务实例。

```
ADD PNFPROFILE: NFINSTANCEID="GMLC_Instance_0", NFTYPE=NfGMLC, NFSTATUS=Registered, FQDN="gmlc0.huawei.com", INTERPLMNFQDN="gmlc0.mcc460.mnc02.huawei.com", IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS1="10.107.65.184", PORT=8080, LOCALITY="SHANGHAI";
```

```
ADD PNFSERVICE: NFINSTANCEID="GMLC_Instance_0", SRVINSTANCEID="Service_Instance_1", SERVICENAME=NgmlcLoc, SCHEMA=http, NFSERVICESTATUS=REGISTERED, FQDN="gmlc0.huawei.com", INTERPLMNFQDN="gmlc0.mcc460.mnc02.huawei.com";
```

```
ADD PNFSRVNTFSUBS: NFINSTANCEID="GMLC_Instance_0", SRVINSTANCEID="Service_Instance_1", NTFICATIONTYPE=LocNty, CALLBACKURI="http://10.60.103.18:19999/ngmlc-loc/hgmlc/v1/provide-location", N1MESSAGECLASS=Lpp, N2INFOCLASS=Nrppa;
```
