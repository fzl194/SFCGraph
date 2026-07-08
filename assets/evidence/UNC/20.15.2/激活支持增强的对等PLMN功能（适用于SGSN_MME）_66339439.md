# 激活支持增强的对等PLMN功能（适用于SGSN/MME）

- [操作场景](#ZH-CN_OPI_0166339439__1.3.1)
- [必备事项](#ZH-CN_OPI_0166339439__1.3.2)
- [操作步骤](#ZH-CN_OPI_0166339439__1.3.3)
- [任务示例](#ZH-CN_OPI_0166339439__1.3.4)

## [操作场景](#ZH-CN_OPI_0166339439)

本操作指导介绍在运行网络中激活支持增强的对等PLMN功能的操作过程。

对等PLMN（Equivalent PLMN）是指可向用户提供和本网相同服务的PLMN。对等PLMN列表中各PLMN，在用户进行PLMN重选、小区重选、切换等流程中完全等价。支持增强的对等PLMN功能，是指 UNC 可以向终端下发“对等PLMN列表”，允许终端根据这个列表记录，自行选择网络资源来为其提供服务。

> **说明**
> 适用于 SGSN、 MME。

## [必备事项](#ZH-CN_OPI_0166339439)

前提条件

- 需要终端设备支持3GPP R99及以上协议版本。
- 请仔细阅读[WSFD-010108 支持增强的对等PLMN功能特性概述](特性概述_66339436.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD PEERPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/对等PLMN管理/增加对等PLMN配置(ADD PEERPLMN)_26305906.md) | 区域范围（AREA） | PLMN | 全网规划 | PLMN和与其对等的PLMN参数 |
| [**ADD PEERPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/对等PLMN管理/增加对等PLMN配置(ADD PEERPLMN)_26305906.md) | 对等PLMN1~对等PLMN15（EPLMN1~EPLMN15） | 123456 | 全网规划 | PLMN和与其对等的PLMN参数 |
| [**ADD PEERPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/对等PLMN管理/增加对等PLMN配置(ADD PEERPLMN)_26305906.md) | 移动国家码（MCC） | 134 | 全网规划 | PLMN和与其对等的PLMN参数 |
| [**ADD PEERPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/对等PLMN管理/增加对等PLMN配置(ADD PEERPLMN)_26305906.md) | 移动网号（MNC） | 56 | 全网规划 | PLMN和与其对等的PLMN参数 |

## [操作步骤](#ZH-CN_OPI_0166339439)

1. 进入 “MML命令行-UNC” 窗口。
2. 增加对等PLMN。
  [**ADD PEERPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/对等PLMN管理/增加对等PLMN配置(ADD PEERPLMN)_26305906.md)
  > **说明**
  > 参数 “EPLMN1” 到 “EPLMN15” 不可以重复。

## [任务示例](#ZH-CN_OPI_0166339439)

任务描述

在运营商A的 UNC 上增加一条运营商B的对等PLMN1配置记录，HPLMN_0的签约用户就可以选择从运营商B的EPLMN_1中接入。区域范围为“指定PLMN区域”，用户范围为“所有用户”，对等PLMN1为“123456”。

![](激活支持增强的对等PLMN功能（适用于SGSN_MME）_66339439.assets/zh-cn_image_0183226371_2.png)

脚本

```
ADD PEERPLMN: AREA=PLMN, MCC="134", MNC="56", SUBRANGE=ALL_USER, EPLMN1="123456";
```
