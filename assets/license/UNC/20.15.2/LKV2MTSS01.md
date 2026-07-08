---
id: UNC@20.15.2@License@LKV2MTSS01
type: License
name: SRVCC的MSC拓扑选择
nf: UNC
version: 20.15.2
license_code: LKV2MTSS01
control_item_id: '82207700'
applicable_nf:
- MME
status: active
---

# SRVCC的MSC拓扑选择

`LKV2MTSS01` · 控制项 82207700 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

UE在E-UTRAN网络下同时在PS域和CS域进行注册且在IMS域进行注册。在下列场景下，MME在SRVCC流程中为UE选择SGs/Sv接口合一节点的MSC，使选择的Sv接口的MSC与用户在CS域注册的MSC/VLR是同一个，保证数据业务和语音通话能正常进行：<br>- 用户语音业务通过SRVCC流程切换到GSM/UMTS网络。<br>- 用户语音业务过程中伴随数据业务，数据业务触发CSFB时，需要语音业务通过SRVCC流程切换到GSM/UMTS网络。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

网络部署了SGs和Sv接口融合，UE在E-UTRAN网络中在PS域、CS域和IMS域同时注册。当UE在LTE和GSM/UMTS网络切换做业务时，如果UE在SGs接口和Sv接口的业务分别锚定在不同的MSC且MSC之间不能转发，可能导致业务中断。例如，用户进行语音业务，发起SRVCC流程切换到GSM/UMTS网络进行通话，待通话结束后UE重新回到LTE网络，在成功注册到LTE网络前收到CS域语音被叫，Sv接口选择的MSC与UE在CS域注册时的MSC/VLR不同时，会导致CS语音被叫失败。因此，MME通过MSC的拓扑选择，在Sv接口选择的MSC与UE在CS域注册时的MSC/VLR为同一个，可保证语音业务和需要回落到GSM/UMTS网络的业务正常进行。

## 相关控制项（原文，未解释为边）

依赖WSFD-102001 VoLTE基础语音业务

## 对应特性（原文）

WSFD-201007 SRVCC的MSC拓扑选择

## 控制的能力

- [WSFD-201007](feature/UNC/20.15.2/WSFD-201007.md)  — 控制项 82207700

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
