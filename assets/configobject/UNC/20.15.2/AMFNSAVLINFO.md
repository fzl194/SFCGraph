---
id: UNC@20.15.2@ConfigObject@AMFNSAVLINFO
type: ConfigObject
name: AMFNSAVLINFO（授权后的网络切片可用性信息）
nf: UNC
version: 20.15.2
object_name: AMFNSAVLINFO
object_kind: query_target
applicable_nf:
- AMF
status: active
---

# AMFNSAVLINFO（授权后的网络切片可用性信息）

## 说明

**适用NF：AMF**

该命令用于查询AMF上授权后的网络切片可用性信息或无线侧单独上报的切片信息。所谓“授权后”的网络切片可用性信息即AMF通过NSSF获取的各跟踪区所支持网络切片信息。切片获取的数据源可以通过SET NSSELPARA命令中的CAMPUSNSSRC进行设置。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-AMFNSAVLINFO]] · DSP AMFNSAVLINFO

## 证据

- 原始手册：`evidence/UNC/20.15.2/AMFNSAVLINFO.md`
