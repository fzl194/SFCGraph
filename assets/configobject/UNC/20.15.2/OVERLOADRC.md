---
id: UNC@20.15.2@ConfigObject@OVERLOADRC
type: ConfigObject
name: OVERLOADRC（判断对端过载的返回码）
nf: UNC
version: 20.15.2
object_name: OVERLOADRC
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# OVERLOADRC（判断对端过载的返回码）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

![](设置判断对端过载的返回码（SET OVERLOADRC）_09896711.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，该命令会影响Gx，Gy接口智能流控算法，如果配置错误，会导致流控失效，影响用户接入。配置此值需要慎重。

此命令用来配置Gx，Gy接口智能流控时，判断对端过载的返回码列表。

如果对端网元PCRF或者OCS没有按照协议标准实现，过载时的错误返回码不是3004(Diameter too busy)，此时需要使用此命令配置对端过载时的返回码。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-OVERLOADRC]] · LST OVERLOADRC
- [[command/UNC/20.15.2/SET-OVERLOADRC]] · SET OVERLOADRC

## 证据

- 原始手册：`evidence/UNC/20.15.2/OVERLOADRC.md`
- 原始手册：`evidence/UNC/20.15.2/OVERLOADRC.md`
