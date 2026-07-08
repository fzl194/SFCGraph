---
id: UNC@20.15.2@ConfigObject@BTRUNCSTATUS
type: ConfigObject
name: BTRUNCSTATUS（宽带集群系统TSN状态）
nf: UNC
version: 20.15.2
object_name: BTRUNCSTATUS
object_kind: query_target
applicable_nf:
- MME
status: active
---

# BTRUNCSTATUS（宽带集群系统TSN状态）

## 说明

**适用NF：MME**

该命令用于查看宽带集群系统的容灾状态。当宽带集群系统启用异地容灾功能时，MME在Tm1接口与一或多个TSN进行双向的定时探测，TSN侧通过探测消息下发自身状态给MME，指示MME自身的状态发生了变更；MME侧通过TSN的通知或者自己探测的结果来变更自身保存的TSN状态。当宽带集群系统处于容灾主或者单站主状态时，允许接入业务；当系统处于容灾备或检测备状态时，不允许接入业务。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-BTRUNCSTATUS]] · DSP BTRUNCSTATUS

## 证据

- 原始手册：`evidence/UNC/20.15.2/BTRUNCSTATUS.md`
