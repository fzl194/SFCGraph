---
id: UNC@20.15.2@ConfigObject@SQOSREMARK
type: ConfigObject
name: SQOSREMARK（重标记配置）
nf: UNC
version: 20.15.2
object_name: SQOSREMARK
object_kind: entity
status: active
---

# SQOSREMARK（重标记配置）

## 说明

该命令用来增加重标记。

可以对匹配的报文进行DSCP、DF、TOS、IP-precedence等重标记。在一个流行为下只能添加一次Remark动作，再添加或修改Remark动作时需要使用MOD SQOSREMARK命令。

## 操作本对象的命令

- [ADD SQOSREMARK](command/UNC/20.15.2/ADD-SQOSREMARK.md)
- [LST SQOSREMARK](command/UNC/20.15.2/LST-SQOSREMARK.md)
- [MOD SQOSREMARK](command/UNC/20.15.2/MOD-SQOSREMARK.md)
- [RMV SQOSREMARK](command/UNC/20.15.2/RMV-SQOSREMARK.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改重标记配置（MOD-SQOSREMARK）_00600285.md`
- 原始手册：`evidence/UNC/20.15.2/删除重标记配置（RMV-SQOSREMARK）_00601341.md`
- 原始手册：`evidence/UNC/20.15.2/增加重标记配置（ADD-SQOSREMARK）_00441017.md`
- 原始手册：`evidence/UNC/20.15.2/查询重标记配置（LST-SQOSREMARK）_00441201.md`
