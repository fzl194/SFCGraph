---
id: UNC@20.15.2@ConfigObject@NFCACHESYNC
type: ConfigObject
name: NFCACHESYNC（操作远端NF缓存同步）
nf: UNC
version: 20.15.2
object_name: NFCACHESYNC
object_kind: action
applicable_nf:
- AMF
- SMF
- NCG
status: active
---

# NFCACHESYNC（操作远端NF缓存同步）

## 说明

![](操作远端NF缓存同步（OPR NFCACHESYNC）_24956644.assets/notice_3.0-zh-cn_2.png)

该命令会根据输入远端NF实例标识尝试构建缓存，新缓存构建成功可能会影响后续对应业务的网元选择。

**适用NF：AMF、SMF、NCG**

该命令用于从NRF获得指定的远端NF信息并构建到缓存数据中。如果本端缓存数据缺失或希望更新缓存中某一网元数据时可以执行该命令。

## 操作本对象的命令

- [OPR NFCACHESYNC](command/UNC/20.15.2/OPR-NFCACHESYNC.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/操作远端NF缓存同步（OPR-NFCACHESYNC）_24956644.md`
