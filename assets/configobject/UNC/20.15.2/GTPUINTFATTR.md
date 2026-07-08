---
id: UNC@20.15.2@ConfigObject@GTPUINTFATTR
type: ConfigObject
name: GTPUINTFATTR（GTP-U IP地址接口属性）
nf: UNC
version: 20.15.2
object_name: GTPUINTFATTR
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# GTPUINTFATTR（GTP-U IP地址接口属性）

## 说明

**适用网元：SGSN、MME**

该命令用于指定GTPU IP地址在指定的接口或者在指定的用户范围内使用，以满足不同的组网部署要求。

本命令需和 [**ADD GTPULE**](../Gtpu本端实体管理/增加GTP-U本地实体(ADD GTPULE)_72345581.md) 命令配合使用，通过 [**ADD GTPULE**](../Gtpu本端实体管理/增加GTP-U本地实体(ADD GTPULE)_72345581.md) 命令的 “组号” 与本命令的{ “接口类型” + “用户范围” }关联起来，满足各种组网规划的应用。

应用场景举例1：GnGp SGSN组网时，将GnGp接口与Iu接口隔离，通常划分独立的VPN，这就要求Iu接口上使用的GTPU IP地址能够独立指定，与GnGp接口的GTPU IP地址分开。比如数据规划时，将Iu接口的GTPU IP地址规划为32号组，其他接口的GTPU IP地址规划为0号组，通过本命令指定Iu接口与32号组关联，其他接口缺省与0号组关联。

## 操作本对象的命令

- [ADD GTPUINTFATTR](command/UNC/20.15.2/ADD-GTPUINTFATTR.md)
- [DSP GTPUINTFATTR](command/UNC/20.15.2/DSP-GTPUINTFATTR.md)
- [LST GTPUINTFATTR](command/UNC/20.15.2/LST-GTPUINTFATTR.md)
- [MOD GTPUINTFATTR](command/UNC/20.15.2/MOD-GTPUINTFATTR.md)
- [RMV GTPUINTFATTR](command/UNC/20.15.2/RMV-GTPUINTFATTR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GTP-U-IP地址接口属性(MOD-GTPUINTFATTR)_26305794.md`
- 原始手册：`evidence/UNC/20.15.2/删除GTP-U-IP地址接口属性(RMV-GTPUINTFATTR)_72225663.md`
- 原始手册：`evidence/UNC/20.15.2/增加GTP-U-IP地址接口属性(ADD-GTPUINTFATTR)_26145984.md`
- 原始手册：`evidence/UNC/20.15.2/显示GTP-U-IP地址接口属性(DSP-GTPUINTFATTR)_26145986.md`
- 原始手册：`evidence/UNC/20.15.2/查询GTP-U-IP地址接口属性(LST-GTPUINTFATTR)_72345585.md`
