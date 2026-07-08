# 调测EPS Fallback紧急呼叫

- [操作场景](#ZH-CN_OPI_0226162694__1.3.1)
- [必备事项](#ZH-CN_OPI_0226162694__1.3.2)
- [操作步骤](#ZH-CN_OPI_0226162694__1.3.3)

## [操作场景](#ZH-CN_OPI_0226162694)

本特性是指在UE从5G网络接入时，允许其在IMS域注册，但是当UE要进行紧急通话时，会回落到4G网络通过VoLTE进行紧急通话。在不部署VoNR的情况下提供紧急呼叫语音解决方案。

> **说明**
> 适用于AMF。

## [必备事项](#ZH-CN_OPI_0226162694)

前提条件

- 请仔细阅读[WSFD-102703 EPS Fallback紧急呼叫特性概述](特性概述_26162692.md)。
- 已完成[激活EPS Fallback 紧急呼叫](激活EPS Fallback紧急呼叫_26162693.md)。

数据

该操作无需准备数据。

## [操作步骤](#ZH-CN_OPI_0226162694)

1. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 查询WSFD-102703 EPS Fallback紧急呼叫功能对应的License配置开关是否打开。
    - 如果“SWITCH”为“ENABLE”，请执行[2](../../../../业务专题/5G Core 4_5G互操作解决方案/调测指导/调测LTE到5G SA网络间重选_01_10046.md#ZH-CN_OPI_0190799286__cmd1098161310282)。
    - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
2. UE接入5G网络。
3. UE拨打紧急呼叫电话时，UE在Service Request消息中携带的service type值为emergency services fallback。
  ![](调测EPS Fallback紧急呼叫_26162694.assets/zh-cn_image_0000001138067291_2.png)
  ![](调测EPS Fallback紧急呼叫_26162694.assets/zh-cn_image_0000001137762745_2.png)
4. 如果UE当前的CM State是CM-IDLE，AMF使用Initial Context Setup Request来通知NG RAN触发5G到4G的重选流程，UE发起标准的5G到4G重选流程。重选流程调测参见 [调测5G SA到LTE网络间重选](../../../../业务专题/5G Core 4_5G互操作解决方案/调测指导/调测5G SA到LTE网络间重选_01_10045.md) 。
5. 如果UE当前的CM State是CM-CONNECTED，AMF使用UE Context Modification Request来通知NG RAN触发5G到4G的切换流程，切换流程调测参见 [调测5G SA到LTE网络间切换](../../../../业务专题/5G Core 4_5G互操作解决方案/调测指导/调测5G SA到LTE网络间切换_01_10043.md) 。
  ![](调测EPS Fallback紧急呼叫_26162694.assets/zh-cn_image_0000001090925470_2.png)
6. UE主动发起紧急呼叫语音业务，语音业务执行成功。
  进入 “MML命令行-UNC” 窗口。 执行命令 **[**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** （参数DSPINFOTYPE为DETAILED，WLNETWKTYPE为NW2G3G4G），查询用户在4G网络下的PDN连接。
  如果为IMS的PDU会话，则 “APN或者DNN” 为 “ims” 。
  预期结果：用户在4G网络有紧急呼叫的VoLTE语音专载，且有QCI=5的默认承载。
