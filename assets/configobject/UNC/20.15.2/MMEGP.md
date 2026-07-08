---
id: UNC@20.15.2@ConfigObject@MMEGP
type: ConfigObject
name: MMEGP（MME群组）
nf: UNC
version: 20.15.2
object_name: MMEGP
object_kind: entity
applicable_nf:
- MME
status: active
---

# MMEGP（MME群组）

## 说明

**适用网元：MME**

此命令用于增加MME群组记录。MME群组用于定义一组MME组成的MME区域，以该区域为粒度进行业务策略控制。需要结合 [**ADD MMEGPMEM**](../MME群组成员配置/增加MME群组成员(ADD MMEGPMEM)_26305434.md) 命令为MME群组添加成员。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-MMEGP]] · ADD MMEGP
- [[command/UNC/20.15.2/LST-MMEGP]] · LST MMEGP
- [[command/UNC/20.15.2/MOD-MMEGP]] · MOD MMEGP
- [[command/UNC/20.15.2/RMV-MMEGP]] · RMV MMEGP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改MME群组(MOD-MMEGP)_26305432.md`
- 原始手册：`evidence/UNC/20.15.2/删除MME群组(RMV-MMEGP)_72345219.md`
- 原始手册：`evidence/UNC/20.15.2/增加MME群组(ADD-MMEGP)_72225301.md`
- 原始手册：`evidence/UNC/20.15.2/显示MME群组(LST-MMEGP)_26145622.md`
