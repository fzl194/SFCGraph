---
id: UDG@20.15.2@ConfigObject@QOSSHAPEQDEPTH
type: ConfigObject
name: QOSSHAPEQDEPTH（Qos Shape缓存队列深度与流量速率的对应关系）
nf: UDG
version: 20.15.2
object_name: QOSSHAPEQDEPTH
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# QOSSHAPEQDEPTH（Qos Shape缓存队列深度与流量速率的对应关系）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于配置流量做shaping时的缓存队列深度与流量速率的对应关系。用户流量速率与这个对应关系表进行比较得到缓存队列深度。队列深度，即最多缓存的报文个数。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-QOSSHAPEQDEPTH]] · ADD QOSSHAPEQDEPTH
- [[command/UDG/20.15.2/LST-QOSSHAPEQDEPTH]] · LST QOSSHAPEQDEPTH
- [[command/UDG/20.15.2/MOD-QOSSHAPEQDEPTH]] · MOD QOSSHAPEQDEPTH
- [[command/UDG/20.15.2/RMV-QOSSHAPEQDEPTH]] · RMV QOSSHAPEQDEPTH

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改Qos-Shape缓存队列深度与流量速率的对应关系（MOD-QOSSHAPEQDEPTH）_86528786.md`
- 原始手册：`evidence/UDG/20.15.2/删除Qos-Shape缓存队列深度与流量速率的对应关系（RMV-QOSSHAPEQDEPTH）_82837676.md`
- 原始手册：`evidence/UDG/20.15.2/查询Qos-Shape缓存队列深度与流量速率的对应关系（LST-QOSSHAPEQDEPTH）_86528799.md`
- 原始手册：`evidence/UDG/20.15.2/添加Qos-Shape缓存队列深度与流量速率的对应关系（ADD-QOSSHAPEQDEPTH）_82837674.md`
