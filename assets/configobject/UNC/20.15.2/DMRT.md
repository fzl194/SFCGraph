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

- [ADD DMRT](command/UNC/20.15.2/ADD-DMRT.md)
- [DSP DMRT](command/UNC/20.15.2/DSP-DMRT.md)
- [LST DMRT](command/UNC/20.15.2/LST-DMRT.md)
- [MOD DMRT](command/UNC/20.15.2/MOD-DMRT.md)
- [RMV DMRT](command/UNC/20.15.2/RMV-DMRT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Diameter域路由配置(MOD-DMRT)_26146290.md`
- 原始手册：`evidence/UNC/20.15.2/删除Diameter域路由配置(RMV-DMRT)_72345889.md`
- 原始手册：`evidence/UNC/20.15.2/增加Diameter域路由配置(ADD-DMRT)_26306100.md`
- 原始手册：`evidence/UNC/20.15.2/显示Diameter域路由状态(DSP-DMRT)_26306102.md`
- 原始手册：`evidence/UNC/20.15.2/查询Diameter域路由配置(LST-DMRT)_72225969.md`
