---
id: UNC@20.15.2@ConfigObject@TAGP
type: ConfigObject
name: TAGP（TA群组）
nf: UNC
version: 20.15.2
object_name: TAGP
object_kind: entity
applicable_nf:
- MME
status: active
---

# TAGP（TA群组）

## 说明

**适用网元：MME**

此命令用于增加跟踪区群组记录。跟踪区群组用于定义一组TA组成的区域，以该区域为粒度进行业务策略控制。需要结合 [**ADD TAGPMEM**](../跟踪区群组成员管理/增加TA群组成员(ADD TAGPMEM)_72225263.md) 命令为跟踪区群组添加成员。

## 操作本对象的命令

- [ADD TAGP](command/UNC/20.15.2/ADD-TAGP.md)
- [LST TAGP](command/UNC/20.15.2/LST-TAGP.md)
- [MOD TAGP](command/UNC/20.15.2/MOD-TAGP.md)
- [RMV TAGP](command/UNC/20.15.2/RMV-TAGP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改TA群组(MOD-TAGP)_72225261.md`
- 原始手册：`evidence/UNC/20.15.2/删除TA群组(RMV-TAGP)_26305392.md`
- 原始手册：`evidence/UNC/20.15.2/增加TA群组(ADD-TAGP)_26145580.md`
- 原始手册：`evidence/UNC/20.15.2/查询TA群组(LST-TAGP)_72345179.md`
