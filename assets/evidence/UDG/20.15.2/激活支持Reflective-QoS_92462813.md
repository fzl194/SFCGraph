# 激活支持Reflective QoS

- [操作场景](#ZH-CN_OPI_0292462813__1.3.1)
- [必备事项](#ZH-CN_OPI_0292462813__1.3.2)
- [操作步骤](#ZH-CN_OPI_0292462813__1.3.3)
- [任务示例](#ZH-CN_OPI_0292462813__1.3.4)

## [操作场景](#ZH-CN_OPI_0292462813)

在 UDG 上开启特性的License开关激活支持Reflective QoS功能。

> **说明**
> 适用于UPF。

## [必备事项](#ZH-CN_OPI_0292462813)

前提条件

- 请仔细阅读[GWFD-020101 支持Reflective QoS](../GWFD-020101 支持Reflective QoS_88816803.md)。
- 完成 **加载license** （如果有需求，请联系华为技术支持工程师处理）。

数据

无

## [操作步骤](#ZH-CN_OPI_0292462813)

1. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)

## [任务示例](#ZH-CN_OPI_0292462813)

任务描述

打开本特性的License配置开关，使能支持Reflective QoS功能。

脚本

打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3G5SRQS01",SWITCH=ENABLE;
```
