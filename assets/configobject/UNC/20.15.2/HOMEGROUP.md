---
id: UNC@20.15.2@ConfigObject@HOMEGROUP
type: ConfigObject
name: HOMEGROUP（Home Group）
nf: UNC
version: 20.15.2
object_name: HOMEGROUP
object_kind: entity
applicable_nf:
- PGW-C
- GGSN
status: active
---

# HOMEGROUP（Home Group）

## 说明

**适用NF：PGW-C、GGSN**

该命令用于增加一个Home Group，把能够匹配IMSI/MSISDN号码段组中号段或者计费属性组中计费特征值的用户激活请求消息转发到Home GGSN/PGW去处理。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-HOMEGROUP]] · ADD HOMEGROUP
- [[command/UNC/20.15.2/LST-HOMEGROUP]] · LST HOMEGROUP
- [[command/UNC/20.15.2/MOD-HOMEGROUP]] · MOD HOMEGROUP
- [[command/UNC/20.15.2/RMV-HOMEGROUP]] · RMV HOMEGROUP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Home-Group（MOD-HOMEGROUP）_42693474.md`
- 原始手册：`evidence/UNC/20.15.2/删除Home-Group（RMV-HOMEGROUP）_88733227.md`
- 原始手册：`evidence/UNC/20.15.2/增加Home-Group（ADD-HOMEGROUP）_42853256.md`
- 原始手册：`evidence/UNC/20.15.2/查询Home-Group（LST-HOMEGROUP）_88613381.md`
