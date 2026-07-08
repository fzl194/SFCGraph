---
id: UNC@20.15.2@ConfigObject@VPNINST
type: ConfigObject
name: VPNINST（VPN实例）
nf: UNC
version: 20.15.2
object_name: VPNINST
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
status: active
---

# VPNINST（VPN实例）

## 说明

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于创建指定的VPN实例。创建VPN实例后，还需要对VPN实例进行一系列的配置，必要的操作如下：

- 将VPN实例与PE上连向VPN网络的接口绑定。
- 通过配置接口与VPN实例绑定，该接口成为私网接口，从该接口进入的报文使用VPN实例中的转发信息进行转发。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-VPNINST]] · ADD VPNINST
- [[command/UNC/20.15.2/LST-VPNINST]] · LST VPNINST
- [[command/UNC/20.15.2/RMV-VPNINST]] · RMV VPNINST

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除VPN实例（RMV-VPNINST）_09651424.md`
- 原始手册：`evidence/UNC/20.15.2/增加VPN实例（ADD-VPNINST）_09653755.md`
- 原始手册：`evidence/UNC/20.15.2/查询VPN实例（LST-VPNINST）_09651519.md`
