# 调测基于IMSI号段的QoS控制（适用于SMF）

- [操作场景](#ZH-CN_OPI_0000001435544181__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001435544181__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001435544181__1.3.3)

## [操作场景](#ZH-CN_OPI_0000001435544181)

当运营商部署基于IMSI号段的Qos控制时，需对UNC的基于IMSI号段的Qos控制功能进行调测，确保本功能可以正常使用。

> **说明**
> 适用于SMF。

## [必备事项](#ZH-CN_OPI_0000001435544181)

前提条件

- 请仔细阅读[WSFD-105104 基于IMSI号段的QoS控制（适用于SMF）](../WSFD-105104 基于IMSI号段的QoS控制（适用于SMF）_85024048.md)。
- 完成[激活基于IMSI号段的QoS控制（适用于SMF）](激活基于IMSI号段的QoS控制（适用于SMF）_84864432.md)。

数据

该操作无需准备数据。

工具

该操作无需准备其他工具。

## [操作步骤](#ZH-CN_OPI_0000001435544181)

1. 创建一个用户跟踪，参数“IMSI”填写被跟踪用户A的IMSI。
2. 用户A发起PDU会话，会话过程中使用QoS限制记录中配置的各AMBR值，查看用户跟踪。
  预期结果：A的用户跟踪内，“Namf_communication_N1N2MessageTransfer Request”消息中，“session-AMBR-for-uplink”和“session-AMBR-for-downlink”分别为配置的上行APN-AMBR限制值和下行APN-AMBR限制值。样例如下图所示：
  ![](调测基于IMSI号段的QoS控制（适用于SMF）_35544181.assets/zh-cn_image_0000001437863861_2.png)
  > **说明**
  > 此样例中上下行APN-AMBR限制值单位为1kbps，不同场景单位不同，如0x6（6）则对应单位为1mbps，具体请参见协议3GPP 24.501。
