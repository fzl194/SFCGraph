---
id: UNC@20.15.2@ConfigObject@SGSNCHARACT
type: ConfigObject
name: SGSNCHARACT（GnGp SGSN属性配置信息）
nf: UNC
version: 20.15.2
object_name: SGSNCHARACT
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# SGSNCHARACT（GnGp SGSN属性配置信息）

## 说明

**适用网元：SGSN**

- 该命令用于配置对端SGSN的属性信息。当本端SGSN和对端SGSN对接时，使用该命令配置对端SGSN支持的QoS版本。
- 该命令中属性“SGSN支持的QoS版本”标识本SGSN在与该对端SGSN进行Inter RAU或Relocation流程，发送消息时可以携带的QoS信元的最高协议版本。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SGSNCHARACT]] · ADD SGSNCHARACT
- [[command/UNC/20.15.2/LST-SGSNCHARACT]] · LST SGSNCHARACT
- [[command/UNC/20.15.2/MOD-SGSNCHARACT]] · MOD SGSNCHARACT
- [[command/UNC/20.15.2/RMV-SGSNCHARACT]] · RMV SGSNCHARACT

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GnGp-SGSN属性配置信息(MOD-SGSNCHARACT)_72345555.md`
- 原始手册：`evidence/UNC/20.15.2/删除GnGp-SGSN属性配置信息(RMV-SGSNCHARACT)_26305764.md`
- 原始手册：`evidence/UNC/20.15.2/增加GnGp-SGSN属性配置信息(ADD-SGSNCHARACT)_72225633.md`
- 原始手册：`evidence/UNC/20.15.2/查询GnGp-SGSN属性配置信息(LST-SGSNCHARACT)_26145956.md`
