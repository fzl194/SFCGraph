---
id: UNC@20.15.2@ConfigObject@LOCALNRI
type: ConfigObject
name: LOCALNRI（本局NRI配置信息）
nf: UNC
version: 20.15.2
object_name: LOCALNRI
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# LOCALNRI（本局NRI配置信息）

## 说明

**适用网元：SGSN**

当使用Iu-flex功能时，需要配置SGSN的NRI，该命令用于配置本SGSN的NRI属性。Iu-flex指一个RAN连接同一个功能域（CS或者PS）的多个CN节点的功能。Iu-flex新增的功能包括：RAN节点的消息路由功能；各个CN节点的负载平衡功能；缺省SGSN功能；后向兼容的功能等。系统开启Iu-flex功能，当发生附着或者路由区更新流程时，本SGSN可以根据P-TMSI中的NRI是否在本表中来确定是否为Inter流程。关于Iu-flex功能描述，请参考3GPP协议23.236。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-LOCALNRI]] · ADD LOCALNRI
- [[command/UNC/20.15.2/BLK-LOCALNRI]] · BLK LOCALNRI
- [[command/UNC/20.15.2/LST-LOCALNRI]] · LST LOCALNRI
- [[command/UNC/20.15.2/RMV-LOCALNRI]] · RMV LOCALNRI
- [[command/UNC/20.15.2/UBL-LOCALNRI]] · UBL LOCALNRI

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除本局NRI配置信息(RMV-LOCALNRI)_26146100.md`
- 原始手册：`evidence/UNC/20.15.2/增加本局NRI配置信息(ADD-LOCALNRI)_72345699.md`
- 原始手册：`evidence/UNC/20.15.2/查询本局NRI配置信息(LST-LOCALNRI)_72225779.md`
- 原始手册：`evidence/UNC/20.15.2/解闭本局NRI配置信息(UBL-LOCALNRI)_72345701.md`
- 原始手册：`evidence/UNC/20.15.2/闭塞本局NRI配置信息(BLK-LOCALNRI)_26305910.md`
