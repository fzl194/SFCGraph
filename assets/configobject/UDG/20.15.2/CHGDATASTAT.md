---
id: UDG@20.15.2@ConfigObject@CHGDATASTAT
type: ConfigObject
name: CHGDATASTAT（计费数据统计信息）
nf: UDG
version: 20.15.2
object_name: CHGDATASTAT
object_kind: action
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# CHGDATASTAT（计费数据统计信息）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

用来查询计费数据统计信息，比如预定义URR流量上报信息、UserProfile安装次数、整体转发和计费流量差异比例信息、缺省费率流量增量信息、子协议Top30的流量增量信息、预定义规则Top20的匹配次数增量信息、URR Top20的流量增量信息。

## 操作本对象的命令

- [CLR CHGDATASTAT](command/UDG/20.15.2/CLR-CHGDATASTAT.md)
- [DSP CHGDATASTAT](command/UDG/20.15.2/DSP-CHGDATASTAT.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示计费数据统计信息（DSP-CHGDATASTAT）_75387238.md`
- 原始手册：`evidence/UDG/20.15.2/清除计费数据统计信息（CLR-CHGDATASTAT）_75626870.md`
