---
id: UNC@20.15.2@ConfigObject@GWSELBYIMEI
type: ConfigObject
name: GWSELBYIMEI（基于IMEI选择GGSN/P-GW配置）
nf: UNC
version: 20.15.2
object_name: GWSELBYIMEI
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# GWSELBYIMEI（基于IMEI选择GGSN/P-GW配置）

## 说明

**适用网元：SGSN、MME**

该命令用于配置基于IMEI选择GGSN/P-GW功能。

当运营商有基于IMEI来选择特定网关需求时需要使用，例如需要对特定类型的终端选择到特定GGSN/P-GW。

## 操作本对象的命令

- [ADD GWSELBYIMEI](command/UNC/20.15.2/ADD-GWSELBYIMEI.md)
- [LST GWSELBYIMEI](command/UNC/20.15.2/LST-GWSELBYIMEI.md)
- [MOD GWSELBYIMEI](command/UNC/20.15.2/MOD-GWSELBYIMEI.md)
- [RMV GWSELBYIMEI](command/UNC/20.15.2/RMV-GWSELBYIMEI.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于IMEI选择GGSN_P-GW配置(MOD-GWSELBYIMEI)_72225621.md`
- 原始手册：`evidence/UNC/20.15.2/删除基于IMEI选择GGSN_P-GW配置(RMV-GWSELBYIMEI)_26145942.md`
- 原始手册：`evidence/UNC/20.15.2/增加基于IMEI选择GGSN_P-GW配置(ADD-GWSELBYIMEI)_72345541.md`
- 原始手册：`evidence/UNC/20.15.2/查询基于IMEI选择GGSN_P-GW配置(LST-GWSELBYIMEI)_26305752.md`
