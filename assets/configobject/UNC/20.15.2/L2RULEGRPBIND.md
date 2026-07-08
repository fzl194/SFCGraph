---
id: UNC@20.15.2@ConfigObject@L2RULEGRPBIND
type: ConfigObject
name: L2RULEGRPBIND（层二规则组与用户的绑定关系）
nf: UNC
version: 20.15.2
object_name: L2RULEGRPBIND
object_kind: binding
applicable_nf:
- SMF
status: active
---

# L2RULEGRPBIND（层二规则组与用户的绑定关系）

## 说明

**适用NF：SMF**

该命令用于增加层二规则组与用户的绑定关系。将层二规则组与指定的用户绑定，用户的IMSI通过ADD IMSIMSISDNSEG命令配置。当用户在以太网接入时，SMF根据用户绑定的层二规则组中绑定的层二规则创建专载。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-L2RULEGRPBIND]] · ADD L2RULEGRPBIND
- [[command/UNC/20.15.2/LST-L2RULEGRPBIND]] · LST L2RULEGRPBIND
- [[command/UNC/20.15.2/MOD-L2RULEGRPBIND]] · MOD L2RULEGRPBIND
- [[command/UNC/20.15.2/RMV-L2RULEGRPBIND]] · RMV L2RULEGRPBIND

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改层二规则组与用户的绑定关系（MOD-L2RULEGRPBIND）_70382353.md`
- 原始手册：`evidence/UNC/20.15.2/删除层二规则组与用户的绑定关系（RMV-L2RULEGRPBIND）_23622998.md`
- 原始手册：`evidence/UNC/20.15.2/增加层二规则组与用户的绑定关系（ADD-L2RULEGRPBIND）_23782726.md`
- 原始手册：`evidence/UNC/20.15.2/查询层二规则组与用户的绑定关系（LST-L2RULEGRPBIND）_70462545.md`
