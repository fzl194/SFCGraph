---
id: UNC@20.15.2@ConfigObject@PERFMULTIDNN
type: ConfigObject
name: PERFMULTIDNN（MultiDNN性能统计对象）
nf: UNC
version: 20.15.2
object_name: PERFMULTIDNN
object_kind: entity
applicable_nf:
- SMF
- PGW-C
status: active
---

# PERFMULTIDNN（MultiDNN性能统计对象）

## 说明

**适用NF：SMF、PGW-C**

该命令用于增加MultiDNN性能统计对象。当需要对指定MultiDNN园区的会话进行性能统计时使用该命令，MultiDNN园区由该命令中的数据网络名称，切片业务类型和切片细分标识唯一确定。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PERFMULTIDNN]] · ADD PERFMULTIDNN
- [[command/UNC/20.15.2/LST-PERFMULTIDNN]] · LST PERFMULTIDNN
- [[command/UNC/20.15.2/RMV-PERFMULTIDNN]] · RMV PERFMULTIDNN

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除MultiDNN性能统计对象（RMV-PERFMULTIDNN）_31551070.md`
- 原始手册：`evidence/UNC/20.15.2/增加MultiDNN性能统计对象（ADD-PERFMULTIDNN）_81671277.md`
- 原始手册：`evidence/UNC/20.15.2/查询MultiDNN性能统计对象（LST-PERFMULTIDNN）_82110977.md`
