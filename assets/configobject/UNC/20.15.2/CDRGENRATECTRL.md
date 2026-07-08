---
id: UNC@20.15.2@ConfigObject@CDRGENRATECTRL
type: ConfigObject
name: CDRGENRATECTRL（话单产生速率）
nf: UNC
version: 20.15.2
object_name: CDRGENRATECTRL
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# CDRGENRATECTRL（话单产生速率）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

SET CDRGENRATECTRL此命令用来配置UNC计费数据产生速率。UNC会根据用户数和系统运行状况综合处理计费数据产生速率，如果认为系统默认计费数据产生速率不合适，可以通过此命令设置计费数据实际产生速率。如果CDRGENRATE参数设置为50，表示计费数据实际产生速率是系统默认值的50%。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-CDRGENRATECTRL]] · LST CDRGENRATECTRL
- [[command/UNC/20.15.2/SET-CDRGENRATECTRL]] · SET CDRGENRATECTRL

## 证据

- 原始手册：`evidence/UNC/20.15.2/CDRGENRATECTRL.md`
- 原始手册：`evidence/UNC/20.15.2/CDRGENRATECTRL.md`
