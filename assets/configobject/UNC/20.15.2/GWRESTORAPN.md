---
id: UNC@20.15.2@ConfigObject@GWRESTORAPN
type: ConfigObject
name: GWRESTORAPN（网关容灾APN）
nf: UNC
version: 20.15.2
object_name: GWRESTORAPN
object_kind: entity
applicable_nf:
- MME
status: active
---

# GWRESTORAPN（网关容灾APN）

## 说明

**适用网元：MME**

本命令用于增加在S-GW或P-GW故障场景下需要恢复的业务的APN网络标识，即APNNI。启用“S-GW/P-GW故障下的业务恢复”特性后，若受影响的业务所对应的APN网络标识与本命令增加的APN网络标识相同，则恢复此类业务的PDN连接。

## 操作本对象的命令

- [ADD GWRESTORAPN](command/UNC/20.15.2/ADD-GWRESTORAPN.md)
- [LST GWRESTORAPN](command/UNC/20.15.2/LST-GWRESTORAPN.md)
- [RMV GWRESTORAPN](command/UNC/20.15.2/RMV-GWRESTORAPN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除网关容灾APN(RMV-GWRESTORAPN)_26305892.md`
- 原始手册：`evidence/UNC/20.15.2/增加网关容灾APN(ADD-GWRESTORAPN)_72225761.md`
- 原始手册：`evidence/UNC/20.15.2/查询网关容灾APN(LST-GWRESTORAPN)_72345683.md`
