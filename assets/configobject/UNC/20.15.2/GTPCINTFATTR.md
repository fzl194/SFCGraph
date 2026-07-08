---
id: UNC@20.15.2@ConfigObject@GTPCINTFATTR
type: ConfigObject
name: GTPCINTFATTR（GTP-C IP地址接口属性）
nf: UNC
version: 20.15.2
object_name: GTPCINTFATTR
object_kind: entity
applicable_nf:
- SGSN
- MME
- AMF
status: active
---

# GTPCINTFATTR（GTP-C IP地址接口属性）

## 说明

**适用网元：SGSN、MME、AMF**

该命令用于指定GTPC IP地址在指定的接口使用，或者在指定的用户范围内使用，满足不同的组网部署要求。

本命令需和 [**ADD GTPCLE**](../Gtpc本端实体管理/增加GTP-C本地实体(ADD GTPCLE)_26145966.md) 命令配合，通过 [**ADD GTPCLE**](../Gtpc本端实体管理/增加GTP-C本地实体(ADD GTPCLE)_26145966.md) 命令的组号与本命令的{接口类型+用户范围}关联起来，满足各种组网规划的应用。

应用场景举例1：Sv接口是PS域网元与CS域网元的接口，从网络安全角度考虑，组网上Sv接口划分独立的VPN，避免PS域的其他接口与CS域互通。这就要求Sv接口上使用的GTPC IP地址能够独立指定，与其他接口的GTPC IP地址分开。数据规划时，将Sv接口的GTPC IP地址规划为1号组，其他接口的GTPC IP地址规划为0号组，通过本命令指定Sv接口与1号组关联，其他接口缺省与0号组关联。

应用场景举例2：MME和SGSN融合部署时，组网上将MME的Sx接口与SGSN的GnGp接口隔离，通常划分独立的VPN，这就要求GnGp接口上使用的GTPC IP地址能够独立指定，与Sx接口的GTPC IP地址分开。数据规划时，将GnGp接口的GTPC IP地址规划为2号组，其他接口的GTPC IP地址规划为0号组，通过本命令指定GnGp接口与2号组关联，其他接口缺省与0号组关联。

## 操作本对象的命令

- [ADD GTPCINTFATTR](command/UNC/20.15.2/ADD-GTPCINTFATTR.md)
- [DSP GTPCINTFATTR](command/UNC/20.15.2/DSP-GTPCINTFATTR.md)
- [LST GTPCINTFATTR](command/UNC/20.15.2/LST-GTPCINTFATTR.md)
- [MOD GTPCINTFATTR](command/UNC/20.15.2/MOD-GTPCINTFATTR.md)
- [RMV GTPCINTFATTR](command/UNC/20.15.2/RMV-GTPCINTFATTR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GTP-C-IP地址接口属性(MOD-GTPCINTFATTR)_72345501.md`
- 原始手册：`evidence/UNC/20.15.2/删除GTP-C-IP地址接口属性(RMV-GTPCINTFATTR)_26305710.md`
- 原始手册：`evidence/UNC/20.15.2/增加GTP-C-IP地址接口属性(ADD-GTPCINTFATTR)_72225579.md`
- 原始手册：`evidence/UNC/20.15.2/显示GTP-C-IP地址接口属性(DSP-GTPCINTFATTR)_72225581.md`
- 原始手册：`evidence/UNC/20.15.2/查询GTP-C-IP地址接口属性(LST-GTPCINTFATTR)_26145902.md`
