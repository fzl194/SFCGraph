---
id: UNC@20.15.2@ConfigObject@DCN
type: ConfigObject
name: DCN
nf: UNC
version: 20.15.2
object_name: DCN
object_kind: entity
applicable_nf:
- MME
status: active
---

# DCN

## 说明

**适用网元：MME**

此命令用于增加专用核心网（Dedicated Core Network）。部署DCN时，先通过此命令在PLMN内配置专用核心网，再通过 [**ADD DCNMAP**](../DCN映射关系/增加DCN映射关系(ADD DCNMAP)_26305638.md) 和 [**ADD DCNMEMBER**](../DCN成员管理/增加DCN成员(ADD DCNMEMBER)_26305640.md) 配置DCN所服务用户范围和DCN所覆盖的网络范围。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-DCN]] · ADD DCN
- [[command/UNC/20.15.2/LST-DCN]] · LST DCN
- [[command/UNC/20.15.2/MOD-DCN]] · MOD DCN
- [[command/UNC/20.15.2/RMV-DCN]] · RMV DCN

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改DCN(MOD-DCN)_26305636.md`
- 原始手册：`evidence/UNC/20.15.2/删除DCN(RMV-DCN)_72345427.md`
- 原始手册：`evidence/UNC/20.15.2/增加DCN(ADD-DCN)_72225505.md`
- 原始手册：`evidence/UNC/20.15.2/查询DCN(LST-DCN)_26145828.md`
