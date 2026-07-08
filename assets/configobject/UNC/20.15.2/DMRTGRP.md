---
id: UNC@20.15.2@ConfigObject@DMRTGRP
type: ConfigObject
name: DMRTGRP（Diameter路由组）
nf: UNC
version: 20.15.2
object_name: DMRTGRP
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# DMRTGRP（Diameter路由组）

## 说明

**适用网元：SGSN、MME**

该命令用于新增一条Diameter路由组。Diameter路由组是由Diameter域路由和Diameter主机路由组成。通过命令 [**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md) 和 **ADD DMHOSTRT** 配置Diameter域路由和主机路由。当与对端进行Diameter连接时，业务通过命令 [**ADD IMSIHSS**](../../../Diameter应用协议/IMSI-HSS转换信息/增加IMSI-HSS对应关系(ADD IMSIHSS)_26145454.md) 引用此路由组的配置来应用相应路由模式。

## 操作本对象的命令

- [ADD DMRTGRP](command/UNC/20.15.2/ADD-DMRTGRP.md)
- [LST DMRTGRP](command/UNC/20.15.2/LST-DMRTGRP.md)
- [RMV DMRTGRP](command/UNC/20.15.2/RMV-DMRTGRP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Diameter路由组(RMV-DMRTGRP)_72225971.md`
- 原始手册：`evidence/UNC/20.15.2/增加Diameter路由组(ADD-DMRTGRP)_26146292.md`
- 原始手册：`evidence/UNC/20.15.2/查询Diameter路由组(LST-DMRTGRP)_26306104.md`
