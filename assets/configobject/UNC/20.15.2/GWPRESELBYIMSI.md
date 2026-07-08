---
id: UNC@20.15.2@ConfigObject@GWPRESELBYIMSI
type: ConfigObject
name: GWPRESELBYIMSI（指定用户优选网关）
nf: UNC
version: 20.15.2
object_name: GWPRESELBYIMSI
object_kind: entity
applicable_nf:
- MME
status: active
---

# GWPRESELBYIMSI（指定用户优选网关）

## 说明

**适用网元：MME**

该命令用于增加指定用户优选网关记录。

支持4G附着流程默认承载创建时优先使用配置的S-GW主机名作为比较节点查询DNS来选择指定的S-GW，并且优先选择和该S-GW合一的P-GW或拓扑最近的P-GW，优选失败后会忽略配置再次使用原有方式查询DNS选择S-GW和P-GW。

支持2G/3G PDP激活流程优先使用配置的GGSN主机名作为比较节点查询DNS来选择指定的GGSN，优选失败后会忽略配置再次使用原有方式查询DNS选择GGSN。

该命令的使用场景：需要将指定用户引流到特定S-GW/GGSN，可通过本命令根据IMSI优选指定S-GW/GGSN。该命令仅在拨测场景下使用，大网场景下不建议使用。

## 操作本对象的命令

- [ADD GWPRESELBYIMSI](command/UNC/20.15.2/ADD-GWPRESELBYIMSI.md)
- [LST GWPRESELBYIMSI](command/UNC/20.15.2/LST-GWPRESELBYIMSI.md)
- [MOD GWPRESELBYIMSI](command/UNC/20.15.2/MOD-GWPRESELBYIMSI.md)
- [RMV GWPRESELBYIMSI](command/UNC/20.15.2/RMV-GWPRESELBYIMSI.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改指定用户优选网关（MOD-GWPRESELBYIMSI）_95841541.md`
- 原始手册：`evidence/UNC/20.15.2/删除指定用户优选网关（RMV-GWPRESELBYIMSI）_95723013.md`
- 原始手册：`evidence/UNC/20.15.2/增加指定用户优选网关（ADD-GWPRESELBYIMSI）_59565706.md`
- 原始手册：`evidence/UNC/20.15.2/查询指定用户优选网关（LST-GWPRESELBYIMSI）_59644410.md`
