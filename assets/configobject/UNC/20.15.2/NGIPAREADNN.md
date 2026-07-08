---
id: UNC@20.15.2@ConfigObject@NGIPAREADNN
type: ConfigObject
name: NGIPAREADNN（5G IP区域DNN）
nf: UNC
version: 20.15.2
object_name: NGIPAREADNN
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGIPAREADNN（5G IP区域DNN）

## 说明

**适用NF：AMF**

该命令用于为“基于位置的地址分配”功能配置S-NSSAI和DNN。当用户创建PDU会话时，且使用的S-NSSAI和DNN与本命令配置的任意一条S-NSSAI和DNN匹配时，系统就会对该用户启用“基于位置的地址分配”功能。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NGIPAREADNN]] · ADD NGIPAREADNN
- [[command/UNC/20.15.2/LST-NGIPAREADNN]] · LST NGIPAREADNN
- [[command/UNC/20.15.2/RMV-NGIPAREADNN]] · RMV NGIPAREADNN

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除5G-IP区域DNN（RMV-NGIPAREADNN）_96242844.md`
- 原始手册：`evidence/UNC/20.15.2/增加5G-IP区域DNN（ADD-NGIPAREADNN）_96241727.md`
- 原始手册：`evidence/UNC/20.15.2/查询5G-IP区域DNN（LST-NGIPAREADNN）_96242250.md`
