---
id: UNC@20.15.2@ConfigObject@CDRSTRGINFO
type: ConfigObject
name: CDRSTRGINFO（缓存话单信息）
nf: UNC
version: 20.15.2
object_name: CDRSTRGINFO
object_kind: query_target
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# CDRSTRGINFO（缓存话单信息）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

此命令用于查看硬盘计费缓存文件的情况，如果在命令中指定PODNAME，则显示指定PODNAME的硬盘的计费缓存情况，若不指定，则返回所有硬盘的计费缓存情况。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-CDRSTRGINFO]] · DSP CDRSTRGINFO

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询缓存话单信息（DSP-CDRSTRGINFO）_09897004.md`
