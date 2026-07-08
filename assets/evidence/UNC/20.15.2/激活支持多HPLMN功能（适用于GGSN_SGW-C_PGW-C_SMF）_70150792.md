# 激活支持多HPLMN功能（适用于 GGSN/ SGW-C/PGW-C/SMF）

- [操作场景](#ZH-CN_OPI_0170150792__1.3.1)
- [必备事项](#ZH-CN_OPI_0170150792__1.3.2)
- [操作步骤](#ZH-CN_OPI_0170150792__1.3.3)
- [任务示例](#ZH-CN_OPI_0170150792__1.3.4)

## [操作场景](#ZH-CN_OPI_0170150792)

当网络允许属于不同运营商用户共同接入时，为了判断用户的归属的属性，需要配置支持多HPLMN功能。

> **说明**
> 适用于 GGSN、 SGW-C、PGW-C、SMF。

## [必备事项](#ZH-CN_OPI_0170150792)

前提条件

- 请仔细阅读[WSFD-104401 支持多HPLMN功能特性概述](特性概述_69313567.md)。
- 已完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[**ADD NGHPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/Home PLMN信息管理/增加5G Home PLMN（ADD NGHPLMN）_09651693.md)** | 运营商标识（NOID） | 0 | 全网规划 | 新增HPLMN |
| **[**ADD NGHPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/Home PLMN信息管理/增加5G Home PLMN（ADD NGHPLMN）_09651693.md)** | 移动国家码（MCC） | 123 | 全网规划 | 新增HPLMN |
| **[**ADD NGHPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/Home PLMN信息管理/增加5G Home PLMN（ADD NGHPLMN）_09651693.md)** | 移动网络号（MNC） | 011 | 全网规划 | 新增HPLMN |
| **[**ADD NGHPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/Home PLMN信息管理/增加5G Home PLMN（ADD NGHPLMN）_09651693.md)** | 描述信息（DESC） | 00 | 全网规划 | 新增HPLMN |

## [操作步骤](#ZH-CN_OPI_0170150792)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License控制开关。
  **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
3. **可选：**新增HPLMN信息。
  **[**ADD NGHPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/运营商管理/Home PLMN信息管理/增加5G Home PLMN（ADD NGHPLMN）_09651693.md)**

## [任务示例](#ZH-CN_OPI_0170150792)

任务描述

激活支持多HPLMN功能，配置MCC号对应的MNC长度为3，增加两个HPLMN为123011和123012。

脚本

//打开功能开关。

```
SET LICENSESWITCH: LICITEM="LKV2MHSM01", SWITCH=ENABLE;
```

//增加两个HPLMN。

```
ADD NGHPLMN: NOID=0,MCC="123",MNC="011",DESC=00;
ADD NGHPLMN: NOID=0,MCC="123",MNC="012",DESC=01;
```
