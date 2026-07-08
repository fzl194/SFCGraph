---
id: UNC@20.15.2@ConfigObject@RESELECTUPCAUSE
type: ConfigObject
name: RESELECTUPCAUSE（重选UPF故障原因值）
nf: UNC
version: 20.15.2
object_name: RESELECTUPCAUSE
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
status: active
---

# RESELECTUPCAUSE（重选UPF故障原因值）

## 说明

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于增加重选UPF的故障原因值。在SMF对接多个UPF时，当PFCP会话建立失败，UPF在PFCP会话建立响应消息中携带故障原因值。如果已通过本命令配置对应的故障原因值，SMF支持根据故障原因值触发UPF重选。

## 操作本对象的命令

- [ADD RESELECTUPCAUSE](command/UNC/20.15.2/ADD-RESELECTUPCAUSE.md)
- [LST RESELECTUPCAUSE](command/UNC/20.15.2/LST-RESELECTUPCAUSE.md)
- [RMV RESELECTUPCAUSE](command/UNC/20.15.2/RMV-RESELECTUPCAUSE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除重选UPF故障原因值（RMV-RESELECTUPCAUSE）_06399928.md`
- 原始手册：`evidence/UNC/20.15.2/增加重选UPF的故障原因值（ADD-RESELECTUPCAUSE）_06399908.md`
- 原始手册：`evidence/UNC/20.15.2/查询重选UPF故障原因值（LST-RESELECTUPCAUSE）_06399917.md`
