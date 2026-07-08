---
id: UNC@20.15.2@License@LKV2UPTH01
type: License
name: NB-IoT用户面传输通道保活
nf: UNC
version: 20.15.2
license_code: LKV2UPTH01
control_item_id: '82207713'
applicable_nf:
- MME
status: active
---

# NB-IoT用户面传输通道保活

`LKV2UPTH01` · 控制项 82207713 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

NB-IoT终端数据收发频率低、数据包较小且多数情况为单向发送（例如智能抄表），建立、释放S1–U连接和数据无线承载信令开销大，需要一种高效的小数据传输解决方案。3GPP协议针对此类业务定义了用户面优化功能UP-CIoT（User Plane CIoT EPS Optimization）。UP-CIoT的方式是当终端进入ECM-IDLE态时，UE、eNodeB和MME保存用于恢复连接的S1AP关联、UE上下文和承载上下文数据。当需要恢复数传时，无需进行频繁的E-RAB重建，提升数传效率，节省信令开销。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

- IoT海量连接的趋势和IoT终端节能省电是运营商发展IoT业务过程中面临的两大问题。海量连接会增加网络信令开销，能否提升终端节能省电直接影响运营商的业务竞争力。<br>- 针对M2M的小数据传输，MME提供两种优化方案，CP-CIoT方案和UP-CIoT方案。不同的行业终端可以根据自身业务需求，选择适合的数据传输方式，当终端数据量较大或者传输速率要求较高时，可以优先选择UP-CIoT。<br>- 由于业务需要，终端可以触发CP-CIoT向UP-CIoT转换。比如终端软件的更新场景，原本使用的CP-CIoT没法满足数据传输要求，则需要切换成UP-CIoT传输。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-215102 NB-IoT用户面传输通道保活

## 控制的能力

- [WSFD-215102](feature/UNC/20.15.2/WSFD-215102.md)  — 控制项 82207713

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
