---
id: UNC@20.15.2@ConfigObject@GWSELBYCC
type: ConfigObject
name: GWSELBYCC（基于CC选择GGSN/P-GW）
nf: UNC
version: 20.15.2
object_name: GWSELBYCC
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# GWSELBYCC（基于CC选择GGSN/P-GW）

## 说明

**适用网元：SGSN、MME**

该命令用于增加基于特定CC的GGSN/P-GW选择策略，即为不同APN及CC的本网用户配置不同的GGSN/P-GW选择方法，以满足运营商对不同用户选择不同GGSN/P-GW，灵活部署网络的需求。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GWSELBYCC]] · ADD GWSELBYCC
- [[command/UNC/20.15.2/LST-GWSELBYCC]] · LST GWSELBYCC
- [[command/UNC/20.15.2/RMV-GWSELBYCC]] · RMV GWSELBYCC

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除基于CC选择GGSN_P-GW(RMV-GWSELBYCC)_72225627.md`
- 原始手册：`evidence/UNC/20.15.2/增加基于CC选择GGSN_P-GW(ADD-GWSELBYCC)_26145948.md`
- 原始手册：`evidence/UNC/20.15.2/查询基于CC选择GGSN_P-GW(LST-GWSELBYCC)_26305758.md`
