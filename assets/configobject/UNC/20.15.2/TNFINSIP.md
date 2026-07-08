---
id: UNC@20.15.2@ConfigObject@TNFINSIP
type: ConfigObject
name: TNFINSIP（目标NF实例IP地址）
nf: UNC
version: 20.15.2
object_name: TNFINSIP
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- NCG
- SMSF
status: active
---

# TNFINSIP（目标NF实例IP地址）

## 说明

![](增加目标NF实例IP地址（ADD TNFINSIP）_09654443.assets/notice_3.0-zh-cn_2.png)

配置相同TNFINSINDEX时PORT必须一致。如果配置相同TNFINSINDEX但是不同PORT的TNFINSIP，会覆盖对端NF实例配置中的PORT，导致对端NF实例配置中的IP使用不匹配的PORT。

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF**

该命令用于增加目标NF实例的IP地址配置。

## 操作本对象的命令

- [ADD TNFINSIP](command/UNC/20.15.2/ADD-TNFINSIP.md)
- [LST TNFINSIP](command/UNC/20.15.2/LST-TNFINSIP.md)
- [RMV TNFINSIP](command/UNC/20.15.2/RMV-TNFINSIP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除目标NF实例IP地址（RMV-TNFINSIP）_09652384.md`
- 原始手册：`evidence/UNC/20.15.2/增加目标NF实例IP地址（ADD-TNFINSIP）_09654443.md`
- 原始手册：`evidence/UNC/20.15.2/查询目标NF实例IP地址（LST-TNFINSIP）_09651383.md`
