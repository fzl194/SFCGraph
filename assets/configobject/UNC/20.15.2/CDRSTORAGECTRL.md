---
id: UNC@20.15.2@ConfigObject@CDRSTORAGECTRL
type: ConfigObject
name: CDRSTORAGECTRL（话单存储控制参数）
nf: UNC
version: 20.15.2
object_name: CDRSTORAGECTRL
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# CDRSTORAGECTRL（话单存储控制参数）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

命令用来配置缓存话单文件的超期时间，配置的天数加上周数乘以七为配置的超期总天数。如果一个话单文件被缓存的时间超过配置的超期时间，该话单不会再发往CG/CHF。当配置的超期时间为0时，所有缓存文件不进行超期检测且不上报超期话单缓存告警，CG/CHF状态恢复正常后，所有的缓存话单都将发往CG/CHF。

## 操作本对象的命令

- [LST CDRSTORAGECTRL](command/UNC/20.15.2/LST-CDRSTORAGECTRL.md)
- [SET CDRSTORAGECTRL](command/UNC/20.15.2/SET-CDRSTORAGECTRL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询话单存储控制参数（LST-CDRSTORAGECTRL）_09897002.md`
- 原始手册：`evidence/UNC/20.15.2/设置话单存储控制参数（SET-CDRSTORAGECTRL）_09897001.md`
