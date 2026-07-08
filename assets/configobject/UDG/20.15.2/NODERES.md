---
id: UDG@20.15.2@ConfigObject@NODERES
type: ConfigObject
name: NODERES（节点资源信息）
nf: UDG
version: 20.15.2
object_name: NODERES
object_kind: query_target
status: active
---

# NODERES（节点资源信息）

## 说明

本命令用于查询节点的资源信息。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

> **说明**
> - 查询节点“DISK(磁盘)”类型资源时，因内存分区不需要统计IO数据，所以读IOPS、写IOPS、读速率、写速率、存储延迟显示为NA。
> - 查询所有节点指定资源信息时，若某一节点状态异常导致查询失败，该节点的所有查询信息都会显示NULL。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-NODERES]] · DSP NODERES

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询节点资源信息（DSP-NODERES）_86553878.md`
