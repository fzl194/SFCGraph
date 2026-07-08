---
id: UNC@20.15.2@ConfigObject@GBIPRMTENDPT
type: ConfigObject
name: GBIPRMTENDPT（对端端点配置）
nf: UNC
version: 20.15.2
object_name: GBIPRMTENDPT
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# GBIPRMTENDPT（对端端点配置）

## 说明

**适用网元：SGSN**

该命令用于增加一个Gb接口对端端点。对端端点权重表用来配置对端IP端点的数据权重和信令权重，在IP网络NSVC链路负荷分担时根据数据权重或者信令权重来选择对端IP端点。

## 操作本对象的命令

- [ADD GBIPRMTENDPT](command/UNC/20.15.2/ADD-GBIPRMTENDPT.md)
- [LST GBIPRMTENDPT](command/UNC/20.15.2/LST-GBIPRMTENDPT.md)
- [MOD GBIPRMTENDPT](command/UNC/20.15.2/MOD-GBIPRMTENDPT.md)
- [RMV GBIPRMTENDPT](command/UNC/20.15.2/RMV-GBIPRMTENDPT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对端端点配置(MOD-GBIPRMTENDPT)_26146014.md`
- 原始手册：`evidence/UNC/20.15.2/删除对端端点配置(RMV-GBIPRMTENDPT)_72345613.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端端点配置(ADD-GBIPRMTENDPT)_26305822.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端端点配置(LST-GBIPRMTENDPT)_72225693.md`
