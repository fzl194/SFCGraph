# 调测基于服务PLMN的NB-IoT终端接入速率控制

- [操作场景](#ZH-CN_OPI_0270415329__1.3.1)
- [必备事项](#ZH-CN_OPI_0270415329__1.3.2)
- [操作步骤](#ZH-CN_OPI_0270415329__1.3.3)

## [操作场景](#ZH-CN_OPI_0270415329)

当运营商部署基于服务PLMN的NB-IoT终端接入速率控制业务时，需对该功能进行调测。

> **说明**
> 适用于SGW-U、PGW-U。

## [必备事项](#ZH-CN_OPI_0270415329)

前提条件

- 请仔细阅读[GWFD-110612 基于服务PLMN的NB-IoT终端接入速率控制](../GWFD-110612 基于服务PLMN的NB-IoT终端接入速率控制_70415325.md)。
- 完成[GWFD-110612 基于服务PLMN的NB-IoT终端接入速率控制](../GWFD-110612 基于服务PLMN的NB-IoT终端接入速率控制_70415325.md)。

数据

不涉及。

## [操作步骤](#ZH-CN_OPI_0270415329)

1. 请确认NB-IoT基本功能已开启（详见 [激活NB-IoT终端标准接入](../GWFD-010296 NB-IoT终端标准接入/激活NB-IoT终端标准接入_74275194.md) ），并使用 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09587900.md) 命令查询是否开启了基于附PLMN的NB-IoT终端接入速率控制功能。
  ```
  LST LICENSESWITCH: LICITEM="LKV3G5PNRC01";
  ```
    - 如果 “Switch” 为 “ENABLE” ，则调测完成。
    - 如果 “Switch” 为 “DISABLE” ，则执行 [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md) 命令打开本特性对应的License配置开关。
2. 收集问题信息并寻求技术支持，归纳所有信息并联系华为技术支持解决。
