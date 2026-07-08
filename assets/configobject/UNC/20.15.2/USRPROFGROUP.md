---
id: UNC@20.15.2@ConfigObject@USRPROFGROUP
type: ConfigObject
name: USRPROFGROUP（用户模板组）
nf: UNC
version: 20.15.2
object_name: USRPROFGROUP
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# USRPROFGROUP（用户模板组）

## 说明

**适用NF：PGW-C、SMF**

该命令用于配置一个用户模板组。可使用该用户模板组绑定多个PccProfile和UserProfile，并将该用户模板组绑定到用户APN。用户激活时，可根据APN选择到用户模板组，从而选择可用策略。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-USRPROFGROUP]] · ADD USRPROFGROUP
- [[command/UNC/20.15.2/LST-USRPROFGROUP]] · LST USRPROFGROUP
- [[command/UNC/20.15.2/RMV-USRPROFGROUP]] · RMV USRPROFGROUP

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用户模板组（RMV-USRPROFGROUP）_09897221.md`
- 原始手册：`evidence/UNC/20.15.2/增加用户模板组（ADD-USRPROFGROUP）_09897220.md`
- 原始手册：`evidence/UNC/20.15.2/查询用户模板组（LST-USRPROFGROUP）_09897222.md`
