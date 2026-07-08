---
id: UNC@20.15.2@ConfigObject@USRPROBINDDNAI
type: ConfigObject
name: USRPROBINDDNAI（用户模板关联的DNAI）
nf: UNC
version: 20.15.2
object_name: USRPROBINDDNAI
object_kind: binding
applicable_nf:
- SMF
- PGW-C
- GGSN
status: active
---

# USRPROBINDDNAI（用户模板关联的DNAI）

## 说明

**适用NF：SMF、PGW-C、GGSN**

该命令用于增加用户模板关联的DNAI。

当需要指定用户模板下发某边缘UPF时，可通过本命令绑定User Profile和边缘UPF的DNAI的对应关系来实现。

当一个用户模板绑定到某边缘UPF所对应的DNAI时，该用户模板就只下发给该边缘UPF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-USRPROBINDDNAI]] · ADD USRPROBINDDNAI
- [[command/UNC/20.15.2/LST-USRPROBINDDNAI]] · LST USRPROBINDDNAI
- [[command/UNC/20.15.2/RMV-USRPROBINDDNAI]] · RMV USRPROBINDDNAI

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用户模板关联的DNAI（RMV-USRPROBINDDNAI）_81690720.md`
- 原始手册：`evidence/UNC/20.15.2/增加用户模板关联的DNAI-（ADD-USRPROBINDDNAI）_27051919.md`
- 原始手册：`evidence/UNC/20.15.2/查询用户模板关联的DNAI（LST-USRPROBINDDNAI）_81530800.md`
