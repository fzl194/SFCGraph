# 激活EPS Fallback

- [操作场景](#ZH-CN_OPI_0202422962__1.3.1)
- [必备事项](#ZH-CN_OPI_0202422962__1.3.2)
- [操作步骤](#ZH-CN_OPI_0202422962__1.3.3)
- [任务示例](#ZH-CN_OPI_0202422962__1.3.4)

## [操作场景](#ZH-CN_OPI_0202422962)

在 UDG 上开启特性的License开关激活EPS Fallback功能。

> **说明**
> 适用于UPF。

## [必备事项](#ZH-CN_OPI_0202422962)

前提条件

- 请仔细阅读[GWFD-020282 EPS Fallback](../GWFD-020282 EPS Fallback_76232251.md)。
- 完成[配置VoLTE基础语音业务](../GWFD-020251 VoLTE基础语音业务/配置VoLTE基础语音业务_65928706.md)。
- 完成 **加载license** （如果有需求，请联系华为技术支持工程师处理）。

数据

无

## [操作步骤](#ZH-CN_OPI_0202422962)

打开本特性的License配置开关。

[**SET LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)

## [任务示例](#ZH-CN_OPI_0202422962)

任务描述

打开本特性的License配置开关，使能EPS Fallback功能。

脚本

打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3G5EPSF01",SWITCH=ENABLE;
```
