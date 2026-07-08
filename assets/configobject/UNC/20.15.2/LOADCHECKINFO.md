---
id: UNC@20.15.2@ConfigObject@LOADCHECKINFO
type: ConfigObject
name: LOADCHECKINFO（CSLB负载不均衡检测功能的参数）
nf: UNC
version: 20.15.2
object_name: LOADCHECKINFO
object_kind: global_setting
status: active
---

# LOADCHECKINFO（CSLB负载不均衡检测功能的参数）

## 说明

该命令用于设置CSLB负载不均衡检测功能的相关参数。当打开CSLB负载不均衡检测开关时，系统会根据此命令配置的阈值对CSLB当前的CPU使用率及收包数进行检测，并上报“ALM-100558 服务负荷分担不均衡”告警。

## 操作本对象的命令

- [LST LOADCHECKINFO](command/UNC/20.15.2/LST-LOADCHECKINFO.md)
- [SET LOADCHECKINFO](command/UNC/20.15.2/SET-LOADCHECKINFO.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CSLB负载不均衡检测功能的参数（LST-LOADCHECKINFO）_97964757.md`
- 原始手册：`evidence/UNC/20.15.2/设置CSLB负载不均衡检测功能的参数（SET-LOADCHECKINFO）_48483930.md`
