---
id: UNC@20.15.2@ConfigObject@NSELST
type: ConfigObject
name: NSELST（NSE列表）
nf: UNC
version: 20.15.2
object_name: NSELST
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# NSELST（NSE列表）

## 说明

**适用网元：SGSN**

该命令用于增加一个待处理的NSEI到NSE列表，作为后续 [**RMV NSEUSR**](删除NSE列表下的用户(RMV NSEUSR)_26305832.md) 的输入。用户可以先使用 [**ADD NSELST**](增加NSE列表(ADD NSELST)_72345621.md) 添加所有需要处理的NSEI到NSE列表，然后执行 [**RMV NSEUSR**](删除NSE列表下的用户(RMV NSEUSR)_26305832.md) 。系统会逐个扫描NSE列表中的所有NSEI，分离系统中属于这些NSE的用户。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NSELST]] · ADD NSELST
- [[command/UNC/20.15.2/LST-NSELST]] · LST NSELST
- [[command/UNC/20.15.2/RMV-NSELST]] · RMV NSELST

## 证据

- 原始手册：`evidence/UNC/20.15.2/NSELST.md`
- 原始手册：`evidence/UNC/20.15.2/NSELST.md`
- 原始手册：`evidence/UNC/20.15.2/NSELST.md`
