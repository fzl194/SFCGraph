---
id: UDG@20.15.2@ConfigObject@FABDIAGINFO
type: ConfigObject
name: FABDIAGINFO（Fabric平面亚健康诊断结果）
nf: UDG
version: 20.15.2
object_name: FABDIAGINFO
object_kind: query_target
status: active
---

# FABDIAGINFO（Fabric平面亚健康诊断结果）

## 说明

- 该命令用于显示Fabric平面亚健康诊断结果。
- Pod级Fabric亚健康：若本Fabric Pod与其他所有Fabric Pod之间产生的亚健康链路数与总链路数的比值大于POD亚健康阈值，则认为该Fabric Pod处于Pod级别的Fabric亚健康，可能是Fabric亚健康汇聚点。POD亚健康阈值可使用[**SET FABDIAGPARA**](设置Pod Fabric平面亚健康诊断参数（SET FABDIAGPARA）_48110865.md)设置，[**LST FABDIAGPARA**](查询Pod Fabric平面亚健康诊断参数（LST FABDIAGPARA）_48150373.md)查询。
- 节点级Fabric亚健康：若本节点上所有Fabric Pod都处于Pod级Fabric亚健康，则认为该节点处于节点级别的Fabric亚健康，可能是Fabric亚健康汇聚点。
- 主机级Fabric亚健康：若本主机上所有Fabric Pod都处于Pod级Fabric亚健康，则认为该主机处于主机级别的Fabric亚健康，可能是Fabric亚健康汇聚点。
- Fabric Pod可使用[**DSP PAENODE**](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)查询，输出结果中的服务地址表示Pod名称。

> **说明**
> 无

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-FABDIAGINFO]] · DSP FABDIAGINFO

## 证据

- 原始手册：`evidence/UDG/20.15.2/FABDIAGINFO.md`
