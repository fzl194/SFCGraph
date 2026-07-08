---
id: UNC@20.15.2@ConfigObject@MVNORES
type: ConfigObject
name: MVNORES（MVNO资源配置信息）
nf: UNC
version: 20.15.2
object_name: MVNORES
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# MVNORES（MVNO资源配置信息）

## 说明

**适用网元：SGSN、MME**

该命令用于增加MVNO的用户资源。MVNO的用户资源配置了这个MVNO可以附着和激活的最大用户数。MVNO的用户资源有：2G最大附着用户数、3G最大附着用户数、4G最大附着用户数、2G最大PDP激活数、3G最大PDP激活数、4G最大激活承载数。如果配置了一个MVNO，但是不给这个MVNO配置用户资源，MVNO的用户不能进行PS业务。

## 操作本对象的命令

- [ADD MVNORES](command/UNC/20.15.2/ADD-MVNORES.md)
- [LST MVNORES](command/UNC/20.15.2/LST-MVNORES.md)
- [MOD MVNORES](command/UNC/20.15.2/MOD-MVNORES.md)
- [RMV MVNORES](command/UNC/20.15.2/RMV-MVNORES.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改MVNO资源配置信息(MOD-MVNORES)_72225745.md`
- 原始手册：`evidence/UNC/20.15.2/删除MVNO资源配置信息(RMV-MVNORES)_26146066.md`
- 原始手册：`evidence/UNC/20.15.2/增加MVNO资源配置信息(ADD-MVNORES)_72345665.md`
- 原始手册：`evidence/UNC/20.15.2/查询MVNO资源配置信息(LST-MVNORES)_26305876.md`
