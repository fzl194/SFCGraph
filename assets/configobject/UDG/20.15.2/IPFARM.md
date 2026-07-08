---
id: UDG@20.15.2@ConfigObject@IPFARM
type: ConfigObject
name: IPFARM（IPFarm）
nf: UDG
version: 20.15.2
object_name: IPFARM
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# IPFARM（IPFarm）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置重定向或p-cscf类型的IP farm。IP farm是若干个相同VPN的server集合。IP farm可以用于重定向，或p-cscf的连接状态检测机制。重定向类型的IP farm应用于captive portal动作，在动作执行时，会基于SET IPFARMGLOBAL配置的负荷分担模式选择状态正常的IP farm服务器作为重定向的目的服务器。p-cscf类型的IP farm主要用于检测PcscfGroup中各p-cscf的连接状态。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-IPFARM]] · ADD IPFARM
- [[command/UDG/20.15.2/DSP-IPFARM]] · DSP IPFARM
- [[command/UDG/20.15.2/LST-IPFARM]] · LST IPFARM
- [[command/UDG/20.15.2/MOD-IPFARM]] · MOD IPFARM
- [[command/UDG/20.15.2/RMV-IPFARM]] · RMV IPFARM

## 关联对象

- [[configobject/UDG/20.15.2/IPFARMSERVER]] · IPFARMSERVER
- [[configobject/UDG/20.15.2/LOGICINF]] · LOGICINF
- [[configobject/UDG/20.15.2/VPNINST]] · VPNINST

## 证据

- 原始手册：`evidence/UDG/20.15.2/IPFARM.md`
- 原始手册：`evidence/UDG/20.15.2/IPFARM.md`
- 原始手册：`evidence/UDG/20.15.2/IPFARM.md`
- 原始手册：`evidence/UDG/20.15.2/IPFARM.md`
- 原始手册：`evidence/UDG/20.15.2/IPFARM.md`
