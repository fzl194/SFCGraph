---
id: UNC@20.15.2@ConfigObject@GLBPCRFGROUP
type: ConfigObject
name: GLBPCRFGROUP（全局PCRF组绑定关系）
nf: UNC
version: 20.15.2
object_name: GLBPCRFGROUP
object_kind: entity
applicable_nf:
- PGW-C
- GGSN
status: active
---

# GLBPCRFGROUP（全局PCRF组绑定关系）

## 说明

**适用NF：PGW-C、GGSN**

此命令用来将指定PCRF分组和指定的号段绑定，并且绑定优先级。 同时指定PCRF组名和号段名，则将指定PCRF组和号段绑定。在业务处理过程中，如果APN下PCC使能开关为INHERIT，并且全局PCC使能开关为ENABLE，则优先按照PCRF组和号段的绑定关系进行PCRF组的选择，只有当所有号段都匹配不成功时，才会选用系统缺省的PCRF组。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GLBPCRFGROUP]] · ADD GLBPCRFGROUP
- [[command/UNC/20.15.2/LST-GLBPCRFGROUP]] · LST GLBPCRFGROUP
- [[command/UNC/20.15.2/MOD-GLBPCRFGROUP]] · MOD GLBPCRFGROUP
- [[command/UNC/20.15.2/RMV-GLBPCRFGROUP]] · RMV GLBPCRFGROUP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改全局PCRF组绑定关系（MOD-GLBPCRFGROUP）_09897117.md`
- 原始手册：`evidence/UNC/20.15.2/删除全局PCRF组绑定关系（RMV-GLBPCRFGROUP）_09897118.md`
- 原始手册：`evidence/UNC/20.15.2/增加全局PCRF组绑定关系（ADD-GLBPCRFGROUP）_09897116.md`
- 原始手册：`evidence/UNC/20.15.2/查询全局PCRF组绑定关系（LST-GLBPCRFGROUP）_09897119.md`
