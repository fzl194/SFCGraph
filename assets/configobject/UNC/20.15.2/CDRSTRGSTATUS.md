---
id: UNC@20.15.2@ConfigObject@CDRSTRGSTATUS
type: ConfigObject
name: CDRSTRGSTATUS（话单缓存目录状态）
nf: UNC
version: 20.15.2
object_name: CDRSTRGSTATUS
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# CDRSTRGSTATUS（话单缓存目录状态）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

该命令用来配置话单缓存目录状态。对话单缓存目录charge1或者charge2中的话单文件进行操作之前，必须在锁定该目录之后才可进行。操作完毕后，要将缓存目录charge1或者charge2解锁。

## 操作本对象的命令

- [[command/UNC/20.15.2/CLR-CDRSTRGSTATUS]] · CLR CDRSTRGSTATUS
- [[command/UNC/20.15.2/LST-CDRSTRGSTATUS]] · LST CDRSTRGSTATUS
- [[command/UNC/20.15.2/SET-CDRSTRGSTATUS]] · SET CDRSTRGSTATUS

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询话单缓存目录状态（LST-CDRSTRGSTATUS）_09897007.md`
- 原始手册：`evidence/UNC/20.15.2/清除话单缓存目录状态（CLR-CDRSTRGSTATUS）_70712108.md`
- 原始手册：`evidence/UNC/20.15.2/设置话单缓存目录状态（SET-CDRSTRGSTATUS）_09897006.md`
