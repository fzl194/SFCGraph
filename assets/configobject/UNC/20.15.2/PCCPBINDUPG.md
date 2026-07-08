---
id: UNC@20.15.2@ConfigObject@PCCPBINDUPG
type: ConfigObject
name: PCCPBINDUPG（用户模板组和PccProfile的绑定关系）
nf: UNC
version: 20.15.2
object_name: PCCPBINDUPG
object_kind: binding
applicable_nf:
- PGW-C
- SMF
status: active
---

# PCCPBINDUPG（用户模板组和PccProfile的绑定关系）

## 说明

**适用NF：PGW-C、SMF**

本命令用于将PccProfile绑定到UserProfileGroup下，该PccProfile作为本地PCC用户的策略来源，或者会话创建时无法从PCRF/PCF获取有效规则时的策略来源。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PCCPBINDUPG]] · ADD PCCPBINDUPG
- [[command/UNC/20.15.2/LST-PCCPBINDUPG]] · LST PCCPBINDUPG
- [[command/UNC/20.15.2/RMV-PCCPBINDUPG]] · RMV PCCPBINDUPG

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用户模板组和PccProfile的绑定关系（RMV-PCCPBINDUPG）_09897038.md`
- 原始手册：`evidence/UNC/20.15.2/增加用户模板组和PccProfile的绑定关系（ADD-PCCPBINDUPG）_09897037.md`
- 原始手册：`evidence/UNC/20.15.2/查询用户模板组和PccProfile的绑定关系（LST-PCCPBINDUPG）_09897039.md`
