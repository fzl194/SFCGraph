---
id: UNC@20.15.2@ConfigObject@NFSRVNTFSUBS
type: ConfigObject
name: NFSRVNTFSUBS（服务回调信息）
nf: UNC
version: 20.15.2
object_name: NFSRVNTFSUBS
object_kind: entity
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
status: active
---

# NFSRVNTFSUBS（服务回调信息）

## 说明

**适用NF：AMF、SMF、NRF、NSSF、NCG**

该命令用于添加服务实例回调信息。在NF向NRF注册时，可以针对NF支持的每个服务实例提供默认的通知注册信息（defaultNotificationSubscription），供NF服务生产者向未在NF服务生产者中显式注册的NF服务消费者提供回调URI（Uniform Resource Identifier，通用资源标识符）信息。例如，作为隐式订阅的解决。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NFSRVNTFSUBS]] · ADD NFSRVNTFSUBS
- [[command/UNC/20.15.2/LST-NFSRVNTFSUBS]] · LST NFSRVNTFSUBS
- [[command/UNC/20.15.2/MOD-NFSRVNTFSUBS]] · MOD NFSRVNTFSUBS
- [[command/UNC/20.15.2/RMV-NFSRVNTFSUBS]] · RMV NFSRVNTFSUBS

## 证据

- 原始手册：`evidence/UNC/20.15.2/NFSRVNTFSUBS.md`
- 原始手册：`evidence/UNC/20.15.2/NFSRVNTFSUBS.md`
- 原始手册：`evidence/UNC/20.15.2/NFSRVNTFSUBS.md`
- 原始手册：`evidence/UNC/20.15.2/NFSRVNTFSUBS.md`
