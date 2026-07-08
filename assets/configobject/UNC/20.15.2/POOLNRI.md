---
id: UNC@20.15.2@ConfigObject@POOLNRI
type: ConfigObject
name: POOLNRI（POOL区NRI配置信息）
nf: UNC
version: 20.15.2
object_name: POOLNRI
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# POOLNRI（POOL区NRI配置信息）

## 说明

**适用网元：SGSN**

当使用Iu-flex/Gb-flex功能时，此命令用于配置本POOL区内非本SGSN的NRI属性配置信息。Iu-flex/Gb-flex指一个RAN连接同一个功能域（CS或者PS）的多个CN节点的功能。Iu-flex/Gb-flex新增的功能包括：RAN节点的消息路由功能；各个CN节点的负载平衡功能；缺省SGSN功能；后向兼容的功能等。POOL区指一个由多个路由区组成的区域，有一组（多个）SGSN为这个区域的MS服务，需要为每个SGSN配置一个或多个不同的NRI，用来标识每个SGSN。

系统开启Iu-flex/Gb-flex功能，当发生Inter SGSN的附着或者路由区更新流程时，本SGSN可以根据P-TMSI中的NRI在本表中查找OLD SGSN的信令面IP地址。关于flex功能描述，请参考3GPP规范23.236。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-POOLNRI]] · ADD POOLNRI
- [[command/UNC/20.15.2/LST-POOLNRI]] · LST POOLNRI
- [[command/UNC/20.15.2/MOD-POOLNRI]] · MOD POOLNRI
- [[command/UNC/20.15.2/RMV-POOLNRI]] · RMV POOLNRI

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改POOL区NRI配置信息(MOD-POOLNRI)_72345707.md`
- 原始手册：`evidence/UNC/20.15.2/删除POOL区NRI配置信息(RMV-POOLNRI)_26305916.md`
- 原始手册：`evidence/UNC/20.15.2/增加POOL区NRI配置信息(ADD-POOLNRI)_72225785.md`
- 原始手册：`evidence/UNC/20.15.2/查询POOL区NRI配置信息(LST-POOLNRI)_26146108.md`
