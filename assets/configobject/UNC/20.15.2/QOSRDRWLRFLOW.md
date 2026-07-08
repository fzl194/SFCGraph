---
id: UNC@20.15.2@ConfigObject@QOSRDRWLRFLOW
type: ConfigObject
name: QOSRDRWLRFLOW（WLR引流重定向）
nf: UNC
version: 20.15.2
object_name: QOSRDRWLRFLOW
object_kind: entity
status: active
---

# QOSRDRWLRFLOW（WLR引流重定向）

## 说明

该命令用于将接口收到的报文与WLR引流表进行匹配。如果匹配成功，则将流量引到CSLB_VNFC上；否则，报文查找路由表进行转发。

## 操作本对象的命令

- [ADD QOSRDRWLRFLOW](command/UNC/20.15.2/ADD-QOSRDRWLRFLOW.md)
- [LST QOSRDRWLRFLOW](command/UNC/20.15.2/LST-QOSRDRWLRFLOW.md)
- [RMV QOSRDRWLRFLOW](command/UNC/20.15.2/RMV-QOSRDRWLRFLOW.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除WLR引流重定向（RMV-QOSRDRWLRFLOW）_50281186.md`
- 原始手册：`evidence/UNC/20.15.2/增加WLR引流重定向（ADD-QOSRDRWLRFLOW）_00600289.md`
- 原始手册：`evidence/UNC/20.15.2/查询WLR引流重定向（LST-QOSRDRWLRFLOW）_00841593.md`
