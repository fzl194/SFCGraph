---
id: UNC@20.15.2@ConfigObject@ALLOWDNN
type: ConfigObject
name: ALLOWDNN（允许本地专网分流的DNN）
nf: UNC
version: 20.15.2
object_name: ALLOWDNN
object_kind: entity
applicable_nf:
- AMF
status: active
---

# ALLOWDNN（允许本地专网分流的DNN）

## 说明

**适用NF：AMF**

该命令用于增加允许进行本地专网分流的UE请求DNN和替换DNN，UE请求DNN和替换DNN都匹配时，才会创建或重建对应的本地分流PDU会话。

## 操作本对象的命令

- [ADD ALLOWDNN](command/UNC/20.15.2/ADD-ALLOWDNN.md)
- [LST ALLOWDNN](command/UNC/20.15.2/LST-ALLOWDNN.md)
- [RMV ALLOWDNN](command/UNC/20.15.2/RMV-ALLOWDNN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除允许本地专网分流的DNN（RMV-ALLOWDNN）_42342470.md`
- 原始手册：`evidence/UNC/20.15.2/增加允许本地专网分流的DNN（ADD-ALLOWDNN）_42502264.md`
- 原始手册：`evidence/UNC/20.15.2/查询允许本地专网分流的DNN（LST-ALLOWDNN）_88382225.md`
