---
id: UDG@20.15.2@ConfigObject@GREKPLVSTAT
type: ConfigObject
name: GREKPLVSTAT（GRE隧道KeepAlive报文计数）
nf: UDG
version: 20.15.2
object_name: GREKPLVSTAT
object_kind: action
status: active
---

# GREKPLVSTAT（GRE隧道KeepAlive报文计数）

## 说明

该命令用于显示GRE隧道的Keepalive报文计数。

使用GRE隧道的Keepalive功能，在业务模块选择承载隧道时，可防止选择对端不可达的GRE隧道，避免造成数据丢失。为了获取隧道Keepalive的状态，可使用该命令显示Keepalive报文计数。

## 操作本对象的命令

- [DSP GREKPLVSTAT](command/UDG/20.15.2/DSP-GREKPLVSTAT.md)
- [RTR GREKPLVSTAT](command/UDG/20.15.2/RTR-GREKPLVSTAT.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询GRE隧道KeepAlive报文计数（DSP-GREKPLVSTAT）_49802218.md`
- 原始手册：`evidence/UDG/20.15.2/重置GRE隧道KeepAlive报文计数（RTR-GREKPLVSTAT）_49801614.md`
