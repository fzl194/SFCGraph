---
id: UNC@20.15.2@ConfigObject@DCNMAP
type: ConfigObject
name: DCNMAP（DCN映射关系）
nf: UNC
version: 20.15.2
object_name: DCNMAP
object_kind: entity
applicable_nf:
- MME
status: active
---

# DCNMAP（DCN映射关系）

## 说明

**适用网元：MME**

当部署DCN时，此命令用于根据用户的签约数据UE Usage Type配置指定DCN所服务的用户范围。UE Usage Type表示UE的使用特征，根据UE Usage Type可以选择特定的专用核心网。执行此命令前需要通过 [**ADD DCN**](../DCN配置/增加DCN(ADD DCN)_72225505.md) 增加专用核心网。

## 操作本对象的命令

- [ADD DCNMAP](command/UNC/20.15.2/ADD-DCNMAP.md)
- [LST DCNMAP](command/UNC/20.15.2/LST-DCNMAP.md)
- [RMV DCNMAP](command/UNC/20.15.2/RMV-DCNMAP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DCN映射关系(RMV-DCNMAP)_72345429.md`
- 原始手册：`evidence/UNC/20.15.2/增加DCN映射关系(ADD-DCNMAP)_26305638.md`
- 原始手册：`evidence/UNC/20.15.2/查询DCN映射关系(LST-DCNMAP)_26145830.md`
