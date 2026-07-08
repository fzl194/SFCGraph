---
id: UDG@20.15.2@ConfigObject@IPFARMSERVER
type: ConfigObject
name: IPFARMSERVER（IPFarmServer）
nf: UDG
version: 20.15.2
object_name: IPFARMSERVER
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# IPFARMSERVER（IPFarmServer）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置IP farm中的IP farm服务器地址，作为重定向Server的目标地址和心跳检测地址。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-IPFARMSERVER]] · ADD IPFARMSERVER
- [[command/UDG/20.15.2/DSP-IPFARMSERVER]] · DSP IPFARMSERVER
- [[command/UDG/20.15.2/LST-IPFARMSERVER]] · LST IPFARMSERVER
- [[command/UDG/20.15.2/MOD-IPFARMSERVER]] · MOD IPFARMSERVER
- [[command/UDG/20.15.2/RMV-IPFARMSERVER]] · RMV IPFARMSERVER

## 关联对象

- [[configobject/UDG/20.15.2/IPFARM]] · IPFARM
- [[configobject/UDG/20.15.2/REDIRAPPENDINFO]] · REDIRAPPENDINFO

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IPFarmServer（MOD-IPFARMSERVER）_86526412.md`
- 原始手册：`evidence/UDG/20.15.2/删除IPFarmServer（RMV-IPFARMSERVER）_86526415.md`
- 原始手册：`evidence/UDG/20.15.2/增加IPFarmServer（ADD-IPFARMSERVER）_82837056.md`
- 原始手册：`evidence/UDG/20.15.2/查询IPFarmServer（LST-IPFARMSERVER）_82837059.md`
- 原始手册：`evidence/UDG/20.15.2/查询IPFarm服务器状态（DSP-IPFARMSERVER）_86526404.md`
