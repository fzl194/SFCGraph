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

- [ADD IPFARMSERVER](command/UDG/20.15.2/ADD-IPFARMSERVER.md)
- [DSP IPFARMSERVER](command/UDG/20.15.2/DSP-IPFARMSERVER.md)
- [LST IPFARMSERVER](command/UDG/20.15.2/LST-IPFARMSERVER.md)
- [MOD IPFARMSERVER](command/UDG/20.15.2/MOD-IPFARMSERVER.md)
- [RMV IPFARMSERVER](command/UDG/20.15.2/RMV-IPFARMSERVER.md)

## 关联对象

- [IPFARM](configobject/UDG/20.15.2/IPFARM.md)
- [REDIRAPPENDINFO](configobject/UDG/20.15.2/REDIRAPPENDINFO.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IPFarmServer（MOD-IPFARMSERVER）_86526412.md`
- 原始手册：`evidence/UDG/20.15.2/删除IPFarmServer（RMV-IPFARMSERVER）_86526415.md`
- 原始手册：`evidence/UDG/20.15.2/增加IPFarmServer（ADD-IPFARMSERVER）_82837056.md`
- 原始手册：`evidence/UDG/20.15.2/查询IPFarmServer（LST-IPFARMSERVER）_82837059.md`
- 原始手册：`evidence/UDG/20.15.2/查询IPFarm服务器状态（DSP-IPFARMSERVER）_86526404.md`
