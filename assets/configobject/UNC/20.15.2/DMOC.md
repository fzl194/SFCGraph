---
id: UNC@20.15.2@ConfigObject@DMOC
type: ConfigObject
name: DMOC（Diameter流控节点）
nf: UNC
version: 20.15.2
object_name: DMOC
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# DMOC（Diameter流控节点）

## 说明

**适用网元：SGSN、MME**

该命令用于增加Diameter流控节点，在对端Diameter启动流控后，通过该命令增加支持流控的配置信息。

配置规则：根据Diameter流控节点类型不同进行添加。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-DMOC]] · ADD DMOC
- [[command/UNC/20.15.2/LST-DMOC]] · LST DMOC
- [[command/UNC/20.15.2/RMV-DMOC]] · RMV DMOC

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Diameter流控节点(RMV-DMOC)_72226067.md`
- 原始手册：`evidence/UNC/20.15.2/增加Diameter流控节点(ADD-DMOC)_26146388.md`
- 原始手册：`evidence/UNC/20.15.2/查询Diameter流控节点(LST-DMOC)_26306200.md`
