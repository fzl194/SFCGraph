---
id: UDG@20.15.2@ConfigObject@APN
type: ConfigObject
name: APN（APN配置）
nf: UDG
version: 20.15.2
object_name: APN
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# APN（APN配置）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于添加一个新的APN实例。在运营商需要接入数据网络，配置APN和绑定VPN时使用此命令进行配置。GPRS/UMTS/EPC/5GC核心网中采用APN来标识系统，同时APN定义了系统可以接入的数据网络。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-APN]] · ADD APN
- [[command/UDG/20.15.2/LCK-APN]] · LCK APN
- [[command/UDG/20.15.2/LST-APN]] · LST APN
- [[command/UDG/20.15.2/MOD-APN]] · MOD APN
- [[command/UDG/20.15.2/RMV-APN]] · RMV APN

## 关联对象

- [[configobject/UDG/20.15.2/ACLBINDAPN]] · ACLBINDAPN
- [[configobject/UDG/20.15.2/APNBINDBWMUSRG]] · APNBINDBWMUSRG
- [[configobject/UDG/20.15.2/APNIMSATTR]] · APNIMSATTR
- [[configobject/UDG/20.15.2/APNIMSSIGFLTR]] · APNIMSSIGFLTR
- [[configobject/UDG/20.15.2/APNTETHERDETSW]] · APNTETHERDETSW
- [[configobject/UDG/20.15.2/POOLGRPMAP]] · POOLGRPMAP
- [[configobject/UDG/20.15.2/VPNINST]] · VPNINST

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改APN配置（MOD-APN）_86526458.md`
- 原始手册：`evidence/UDG/20.15.2/删除APN配置（RMV-APN）_86526622.md`
- 原始手册：`evidence/UDG/20.15.2/查询APN配置（LST-APN）_82837017.md`
- 原始手册：`evidence/UDG/20.15.2/添加APN配置（ADD-APN）_82837014.md`
- 原始手册：`evidence/UDG/20.15.2/设置APN锁定配置（LCK-APN）_82837018.md`
