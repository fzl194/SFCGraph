---
id: UNC@20.15.2@ConfigObject@DMRT
type: ConfigObject
name: DMRT（Diameter域路由配置）
nf: UNC
version: 20.15.2
object_name: DMRT
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# DMRT（Diameter域路由配置）

## 说明

**适用网元：SGSN、MME**

该命令用于新增一条Diameter域路由。域路由是指通过域名来选择对端。建议在 UNC 和Diameter对端通过DRA（Diameter路由代理）连接时使用此命令。如果需要配置域路由和主机路由互为主备，可以通过命令 [**ADD DMRTGRP**](../Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md) 将域路由和主机路由配到同一个Diameter路由组索引中，业务通过引用路由组配置进行选路。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-DMRT]] · ADD DMRT
- [[command/UNC/20.15.2/DSP-DMRT]] · DSP DMRT
- [[command/UNC/20.15.2/LST-DMRT]] · LST DMRT
- [[command/UNC/20.15.2/MOD-DMRT]] · MOD DMRT
- [[command/UNC/20.15.2/RMV-DMRT]] · RMV DMRT

## 证据

- 原始手册：`evidence/UNC/20.15.2/DMRT.md`
- 原始手册：`evidence/UNC/20.15.2/DMRT.md`
- 原始手册：`evidence/UNC/20.15.2/DMRT.md`
- 原始手册：`evidence/UNC/20.15.2/DMRT.md`
- 原始手册：`evidence/UNC/20.15.2/DMRT.md`
