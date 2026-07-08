---
id: UNC@20.15.2@ConfigObject@NRFNFTIMER
type: ConfigObject
name: NRFNFTIMER（指定NF在NRF上的时长信息）
nf: UNC
version: 20.15.2
object_name: NRFNFTIMER
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFNFTIMER（指定NF在NRF上的时长信息）

## 说明

![](增加指定NF在NRF上的时长信息（ADD NRFNFTIMER）_07649542.assets/notice_3.0-zh-cn_2.png)

服务发现缓存有效时长（DISCVALIDTIMER）参数过小时，将会导致网元频繁触发服务发现。订阅有效时长（SUBVALIDTIMER）参数过小时，将会导致网元频繁触发订阅请求。

**适用NF：NRF**

该命令用于增加指定NF的有效时长信息。当该NF来NRF服务发现后，会将服务发现结果进行缓存，并保存NRF返回的服务发现缓存有效时长，已缓存的NF信息可在该NF本地进行服务发现，等待缓存有效时长到期后，该NF才会重新来NRF服务发现。另外该NF发起订阅到NRF后，会根据NRF返回的订阅有效时长来进行续订阅，有效时长到期会重新来NRF订阅。NRF整系统通过SET NRFTIMER命令设置统一有效时长，当整系统有效时长不满足现网实际需求时，可通过该命令设置该NF服务发现缓存有效时长(秒)以及订阅的有效时长(秒)。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFNFTIMER]] · ADD NRFNFTIMER
- [[command/UNC/20.15.2/LST-NRFNFTIMER]] · LST NRFNFTIMER
- [[command/UNC/20.15.2/MOD-NRFNFTIMER]] · MOD NRFNFTIMER
- [[command/UNC/20.15.2/RMV-NRFNFTIMER]] · RMV NRFNFTIMER

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改指定NF在NRF上的时长信息（MOD-NRFNFTIMER）_07170130.md`
- 原始手册：`evidence/UNC/20.15.2/删除指定NF在NRF上的时长信息（RMV-NRFNFTIMER）_60449037.md`
- 原始手册：`evidence/UNC/20.15.2/增加指定NF在NRF上的时长信息（ADD-NRFNFTIMER）_07649542.md`
- 原始手册：`evidence/UNC/20.15.2/查询指定NF在NRF上的时长信息（LST-NRFNFTIMER）_07489930.md`
