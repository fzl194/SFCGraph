# 激活Direct Tunnel功能

- [操作场景](#ZH-CN_OPI_0229215371__1.3.1)
- [必备事项](#ZH-CN_OPI_0229215371__1.3.2)
- [操作步骤](#ZH-CN_OPI_0229215371__1.3.3)
- [验证方法](#ZH-CN_OPI_0229215371__1.3.4)
- [任务示例](#ZH-CN_OPI_0229215371__1.3.5)

## [操作场景](#ZH-CN_OPI_0229215371)

> **说明**
> 适用于PGW-U。

新建网络，需要部署Direct Tunnel时，如果满足如下条件，推荐使用本方案：

接入网与核心网的承载网合一。

## [必备事项](#ZH-CN_OPI_0229215371)

前提条件

- 完成各网元的软件升级。
- 完成各网元的基本配置。
- 完成配置PGW-C到SGSN的数据。
- 完成配置PGW-U到SGSN/RNC的数据。

数据

该操作无需准备数据。

## [操作步骤](#ZH-CN_OPI_0229215371)

1. 配置RNC。
  RNC的Direct Tunnel配置，除需添加到PGW-U和PGW-C的路由外，与Indirect Tunnel模式下的Iu-PS接口配置无异。相关配置请参考RNC相关产品手册。
2. 配置SGSN。
  SGSN的Direct Tunnel配置，除个别参数外，与Indirect Tunnel配置无异。相关配置请参考 “ UNC 产品文档 > UNC初始配置与调测 > 配置对接数据 > 配置逻辑接口及业务数据 > 融合网络 > 配置SGSN ” 。
3. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)

## [验证方法](#ZH-CN_OPI_0229215371)

1. 查看IP路由信息。
2. 使用相关命令ping到各网元IP，如果可以ping通，则配置成功。
3. 查看Iu、Gn接口消息跟踪，看是否有数据上报。

## [任务示例](#ZH-CN_OPI_0229215371)

任务描述

配置Direct Tunnel功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3G5DTTL01",SWITCH=ENABLE;
```
