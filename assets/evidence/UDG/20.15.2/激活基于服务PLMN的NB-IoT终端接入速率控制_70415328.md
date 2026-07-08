# 激活基于服务PLMN的NB-IoT终端接入速率控制

- [操作场景](#ZH-CN_OPI_0270415328__1.3.1)
- [必备事项](#ZH-CN_OPI_0270415328__1.3.2)
- [操作步骤](#ZH-CN_OPI_0270415328__1.3.3)
- [任务示例](#ZH-CN_OPI_0270415328__1.3.4)

## [操作场景](#ZH-CN_OPI_0270415328)

在 UDG 上激活基于服务PLMN的NB-IoT终端接入速率控制，PGW-U根据MME发来的速率控制信息，对数据包的转发速率进行控制。对于超过门限的数据包，PGW-U进行丢包处理，未超过门限的数据包进行正常的转发处理。

> **说明**
> 适用于SGW-U、PGW-U。

## [必备事项](#ZH-CN_OPI_0270415328)

前提条件

- 请仔细阅读[GWFD-110612 基于服务PLMN的NB-IoT终端接入速率控制](../GWFD-110612 基于服务PLMN的NB-IoT终端接入速率控制_70415325.md)。
- 已开启NB-IoT基本接入功能（详见[激活NB-IoT终端标准接入](../GWFD-010296 NB-IoT终端标准接入/激活NB-IoT终端标准接入_74275194.md)）。
- 完成[激活基于信令面的数据传输](../GWFD-110606 基于信令面的数据传输/激活基于信令面的数据传输_69258754.md)。
- 完成加载License（本特性完整的功能需要同时在SGW-U/PGW-U和MME上开启对应License，如果有需求，请联系华为技术支持工程师处理）。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[ADD APN](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/添加APN配置（ADD APN）_82837014.md)** | APN名称（APN） | apnplmn | 与对端协商 | - 如果需要配置APN下的基于服务PLMN的终端接入速率控制，则配置该APN，否则仅打开License即可。<br>- APN配置需要与控制面保持一致。 |

## [操作步骤](#ZH-CN_OPI_0270415328)

1. 打开本特性的License控制开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)
2. **可选：** 配置基于服务PLMN的NB-IoT终端接入速率控制使用的APN。
  **[ADD APN](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/添加APN配置（ADD APN）_82837014.md)**
  > **说明**
  > 本特性需要同时在MME、SGW-C/PGW-C进行配置以确保能够生效，在MME上可配置速率控制参数，在SGW-C/PGW-C上可以配置如下相关内容：
  >
  > - APN下的基于服务PLMN的终端接入速率控制开关：打开后，当UE使用特定的APN接入且位于特定的PLMN下时，该特性生效。
  > - 全局基于服务PLMN的终端接入速率控制开关：打开后，当UE位于特定的PLMN下时，该特性生效。
  > - Serving PLMN Rate Control相关信息。
  >
  > 详情请查阅相关产品文档。

## [任务示例](#ZH-CN_OPI_0270415328)

任务描述

开启 UDG 上的Serving PLMN速率控制功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM ="LKV3G5PNRC01", SWITCH=ENABLE;
```

//配置Service PLMN速率控制功能使用的APN。

```
ADD APN: APN="apnplmn";
```
