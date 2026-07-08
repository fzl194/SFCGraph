---
id: UNC@20.15.2@ConfigObject@RDSSVR
type: ConfigObject
name: RDSSVR（RADIUS服务器）
nf: UNC
version: 20.15.2
object_name: RDSSVR
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# RDSSVR（RADIUS服务器）

## 说明

**适用NF：PGW-C、SMF**

该命令用来新增配置RADIUS服务器组下的RADIUS服务器，RADIUS服务器类型包括RADIUS鉴权服务器和RADIUS计费服务器，可以配置主备和抄送服务器，一个RADIUS服务器组的鉴权服务器最多可配置16个主鉴权服务器，16个备鉴权服务器和64个鉴权抄送服务器，计费服务器最多可配置16个主计费服务器，16个备计费服务器和64个计费抄送服务器。服务器的序号按照新增的顺序递增排序，当新增对端的RADIUS服务器，同步新增本端配置时需要使用此命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-RDSSVR]] · ADD RDSSVR
- [[command/UNC/20.15.2/LST-RDSSVR]] · LST RDSSVR
- [[command/UNC/20.15.2/MOD-RDSSVR]] · MOD RDSSVR
- [[command/UNC/20.15.2/RMV-RDSSVR]] · RMV RDSSVR

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改RADIUS服务器（MOD-RDSSVR）_09896757.md`
- 原始手册：`evidence/UNC/20.15.2/删除RADIUS服务器（RMV-RDSSVR）_09896758.md`
- 原始手册：`evidence/UNC/20.15.2/增加RADIUS服务器（ADD-RDSSVR）_09896756.md`
- 原始手册：`evidence/UNC/20.15.2/查询RADIUS服务器（LST-RDSSVR）_09896759.md`
