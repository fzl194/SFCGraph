---
id: UNC@20.15.2@ConfigObject@SRVNODERATPRI
type: ConfigObject
name: SRVNODERATPRI（获取RAT Type的优先级）
nf: UNC
version: 20.15.2
object_name: SRVNODERATPRI
object_kind: global_setting
applicable_nf:
- GGSN
status: active
---

# SRVNODERATPRI（获取RAT Type的优先级）

## 说明

**适用NF：GGSN**

该命令用来配置获取RAT Type的两种方式的优先级。其执行的结果是覆盖式的。使用该命令配置了优先级顺序后，系统就按照此顺序来获取RAT类型，若高优先级失败，则使用低优先级的获取方式。

## 操作本对象的命令

- [LST SRVNODERATPRI](command/UNC/20.15.2/LST-SRVNODERATPRI.md)
- [SET SRVNODERATPRI](command/UNC/20.15.2/SET-SRVNODERATPRI.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询获取RAT-Type的优先级（LST-SRVNODERATPRI）_09651736.md`
- 原始手册：`evidence/UNC/20.15.2/设置获取RAT-Type的优先级（SET-SRVNODERATPRI）_09652385.md`
