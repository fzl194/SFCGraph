---
id: UNC@20.15.2@ConfigObject@GLBDIAMREALM
type: ConfigObject
name: GLBDIAMREALM（全局Diameter域）
nf: UNC
version: 20.15.2
object_name: GLBDIAMREALM
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# GLBDIAMREALM（全局Diameter域）

## 说明

**适用NF：PGW-C、SMF**

该命令用于设置IMSI/MSISDN号段与Diameter域信息的映射关系，或指定根据IMSI构造号段的Diameter域信息。

如果不指定IMSI/MSISDN号段，则用于设置系统缺省的Diameter域，或指定系统缺省根据IMSI构造Diameter域。

该配置基于某种应用类型生效。

## 操作本对象的命令

- [ADD GLBDIAMREALM](command/UNC/20.15.2/ADD-GLBDIAMREALM.md)
- [LST GLBDIAMREALM](command/UNC/20.15.2/LST-GLBDIAMREALM.md)
- [MOD GLBDIAMREALM](command/UNC/20.15.2/MOD-GLBDIAMREALM.md)
- [RMV GLBDIAMREALM](command/UNC/20.15.2/RMV-GLBDIAMREALM.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改全局Diameter域（MOD-GLBDIAMREALM）_09897281.md`
- 原始手册：`evidence/UNC/20.15.2/删除全局Diameter域（RMV-GLBDIAMREALM）_09897282.md`
- 原始手册：`evidence/UNC/20.15.2/增加全局Diameter域（ADD-GLBDIAMREALM）_09897280.md`
- 原始手册：`evidence/UNC/20.15.2/查询全局Diameter域（LST-GLBDIAMREALM）_09897283.md`
