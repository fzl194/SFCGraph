# 调测基于IMSI号段的QoS控制（适用于MME）

- [操作场景](#ZH-CN_OPI_0171016816__1.3.1)
- [必备事项](#ZH-CN_OPI_0171016816__1.3.2)
- [操作步骤](#ZH-CN_OPI_0171016816__1.3.3)

## [操作场景](#ZH-CN_OPI_0171016816)

当运营商部署基于IMSI号段的Qos控制时，需对UNC的基于IMSI号段的Qos控制功能进行调测，确保本功能可以正常使用。

> **说明**
> 适用于MME。

## [必备事项](#ZH-CN_OPI_0171016816)

前提条件

- 请仔细阅读[WSFD-105104 基于IMSI号段的QoS控制（适用于MME）](../WSFD-105104 基于IMSI号段的QoS控制（适用于MME）_62745886.md)。
- 完成[激活基于IMSI号段的QoS控制（适用于MME）](激活基于IMSI号段的QoS控制（适用于MME）_70933937.md)。

数据

该操作无需准备数据。

工具

该操作无需准备其他工具。

## [操作步骤](#ZH-CN_OPI_0171016816)

1. 在MME上创建一个用户跟踪，参数“IMSI”填写被跟踪用户A的IMSI。
2. 用户A附着到MME，附着过程中使用QoS限制记录中配置的各AMBR值，查看用户跟踪。
  预期结果：A的用户跟踪内，“Create Session Request”消息中，“apn ambr uplink”和“apn ambr downlink”分别为配置的上行APN-AMBR限制值和下行APN-AMBR限制值。在本例中均为10kbps。“Initial Context Setup Request”消息中，“ue Ambr Uplink”和“ue Ambr Downlink”分别为配置的上行UE-AMBR限制值和下行UE-AMBR限制值。在本例中均为10000kbps。样例如下图所示：
  ![](调测基于IMSI号段的QoS控制（适用于MME）_71016816.assets/zh-cn_image_0170933966_2.png "点击放大")
  ![](调测基于IMSI号段的QoS控制（适用于MME）_71016816.assets/zh-cn_image_0170933967_2.png "点击放大")
3. 用户A发起使用不同APN的多PDN连接请求，PDN连接过程中使用QoS限制记录中配置的各AMBR值，查看用户跟踪。
  预期结果：A的用户跟踪内，“E-RAB Setup Request”消息中，“UE ambr uplink”和“UE ambr downlink”分别为配置的上行UE-AMBR限制值和下行UE-AMBR限制值。在本例中均为20000kbps。样例如下图所示：
  ![](调测基于IMSI号段的QoS控制（适用于MME）_71016816.assets/zh-cn_image_0172473029_2.png "点击放大")
