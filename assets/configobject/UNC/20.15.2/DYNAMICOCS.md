---
id: UNC@20.15.2@ConfigObject@DYNAMICOCS
type: ConfigObject
name: DYNAMICOCS（动态OCS）
nf: UNC
version: 20.15.2
object_name: DYNAMICOCS
object_kind: action
applicable_nf:
- PGW-C
- SMF
status: active
---

# DYNAMICOCS（动态OCS）

## 说明

**适用NF：PGW-C、SMF**

![](删除动态OCS（CLR DYNAMICOCS）_09896972.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除动态OCS会导致已在线用户无法按照之前的Destination-Host和Destination-Realm封装发送CCR消息。

该命令用于删除动态OCS主机列表表项。

DRA部署场景下，DRA进行OCS寻址，如果寻址到的OCS主机名并未在网关本地配置，则网关会将寻址结果存至动态OCS主机列表。

## 操作本对象的命令

- [CLR DYNAMICOCS](command/UNC/20.15.2/CLR-DYNAMICOCS.md)
- [DSP DYNAMICOCS](command/UNC/20.15.2/DSP-DYNAMICOCS.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除动态OCS（CLR-DYNAMICOCS）_09896972.md`
- 原始手册：`evidence/UNC/20.15.2/查询动态OCS（DSP-DYNAMICOCS）_09896973.md`
