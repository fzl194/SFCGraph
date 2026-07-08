---
id: UNC@20.15.2@ConfigObject@NFCACHE
type: ConfigObject
name: NFCACHE（NF缓存信息）
nf: UNC
version: 20.15.2
object_name: NFCACHE
object_kind: action
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
- SMSF
status: active
---

# NFCACHE（NF缓存信息）

## 说明

**适用NF：AMF、SMF、NRF、NSSF、NCG、SMSF**

该命令用于查询当前NF存储的对端NF信息。当前NF存储的对端NF信息包括如下两部分：

缓存数据：在通过NRF进行NF发现时，NRF向本端NF返回的对端NF信息。如果本端NF订阅了对端NF信息，NRF会在对端NF信息变化时向本端NF发送对端NF信息。这些对端NF信息会在本端NF上进行缓存。在缓存有效时长内，该系统中的NF实例再次服务发现相同NF实例时，可以直接使用缓存中的结果，不需要再去NRF上处理。超过缓存有效时间， 服务发现结果缓存数据将被清除。

本地数据：本地配置的对端NF信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/CLR-NFCACHE]] · CLR NFCACHE
- [[command/UNC/20.15.2/DSP-NFCACHE]] · DSP NFCACHE

## 证据

- 原始手册：`evidence/UNC/20.15.2/NFCACHE.md`
- 原始手册：`evidence/UNC/20.15.2/NFCACHE.md`
