---
id: UNC@20.15.2@ConfigObject@APN
type: ConfigObject
name: APN（APN配置）
nf: UNC
version: 20.15.2
object_name: APN
object_kind: entity
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
status: active
---

# APN（APN配置）

## 说明

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于添加一个新的APN实例。在运营商需要接入外部包交换网络，配置APN和绑定VPN时使用此命令进行配置。2/3/4/5G核心网中采用APN来标识UNC，同时APN定义了UNC可以接入的外部包交换网络。

## 操作本对象的命令

- [ADD APN](command/UNC/20.15.2/ADD-APN.md)
- [LCK APN](command/UNC/20.15.2/LCK-APN.md)
- [LST APN](command/UNC/20.15.2/LST-APN.md)
- [MOD APN](command/UNC/20.15.2/MOD-APN.md)
- [RMV APN](command/UNC/20.15.2/RMV-APN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN配置（MOD-APN）_09653164.md`
- 原始手册：`evidence/UNC/20.15.2/删除APN配置（RMV-APN）_09653148.md`
- 原始手册：`evidence/UNC/20.15.2/增加APN配置（ADD-APN）_09653747.md`
- 原始手册：`evidence/UNC/20.15.2/查询APN配置（LST-APN）_09652599.md`
- 原始手册：`evidence/UNC/20.15.2/锁定APN配置（LCK-APN）_09652640.md`
