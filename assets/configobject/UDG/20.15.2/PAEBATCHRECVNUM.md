---
id: UDG@20.15.2@ConfigObject@PAEBATCHRECVNUM
type: ConfigObject
name: PAEBATCHRECVNUM（PAE批量接收报文数）
nf: UDG
version: 20.15.2
object_name: PAEBATCHRECVNUM
object_kind: global_setting
status: active
---

# PAEBATCHRECVNUM（PAE批量接收报文数）

## 说明

![](设置PAE批量收包的数量（SET PAEBATCHRECVNUM）_35145969.assets/notice_3.0-zh-cn.png)

PAE的批收数与转发性能有关，设置不当会降低转发性能。

该命令用于设置PAE批量收包的数量。

> **说明**
> - 该命令执行后立即生效。
>
> - 设置批收数的对象包括：普通channel、svc channel、外联口channel、外联口、fabric口。

## 操作本对象的命令

- [DSP PAEBATCHRECVNUM](command/UDG/20.15.2/DSP-PAEBATCHRECVNUM.md)
- [LST PAEBATCHRECVNUM](command/UDG/20.15.2/LST-PAEBATCHRECVNUM.md)
- [SET PAEBATCHRECVNUM](command/UDG/20.15.2/SET-PAEBATCHRECVNUM.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示PAE批量接收报文数（DSP-PAEBATCHRECVNUM）_35145961.md`
- 原始手册：`evidence/UDG/20.15.2/查询PAE批量收包的数量（LST-PAEBATCHRECVNUM）_35145965.md`
- 原始手册：`evidence/UDG/20.15.2/设置PAE批量收包的数量（SET-PAEBATCHRECVNUM）_35145969.md`
