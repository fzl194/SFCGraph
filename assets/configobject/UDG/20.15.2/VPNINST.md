---
id: UDG@20.15.2@ConfigObject@VPNINST
type: ConfigObject
name: VPNINST（VPN实例）
nf: UDG
version: 20.15.2
object_name: VPNINST
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# VPNINST（VPN实例）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于创建指定的VPN实例。创建VPN实例后，还需要对VPN实例进行一系列的配置，必要的操作是将VPN实例与连向此VPN网络的接口绑定。通过配置接口与VPN实例绑定，该接口成为私网接口，从该接口进入的报文使用VPN实例中的转发信息进行转发。另外此VPN还需要与平台的ADD L3VPNINST添加的VPN命名一致，否则此VPN就会业务不通。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-VPNINST]] · ADD VPNINST
- [[command/UDG/20.15.2/LST-VPNINST]] · LST VPNINST
- [[command/UDG/20.15.2/RMV-VPNINST]] · RMV VPNINST

## 关联对象

- [[configobject/UDG/20.15.2/APN]] · APN
- [[configobject/UDG/20.15.2/IPFARM]] · IPFARM
- [[configobject/UDG/20.15.2/LOGICINF]] · LOGICINF
- [[configobject/UDG/20.15.2/POOL]] · POOL

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除VPN实例（RMV-VPNINST）_82837046.md`
- 原始手册：`evidence/UDG/20.15.2/增加VPN实例（ADD-VPNINST）_82837045.md`
- 原始手册：`evidence/UDG/20.15.2/查询VPN实例（LST-VPNINST）_82837047.md`
