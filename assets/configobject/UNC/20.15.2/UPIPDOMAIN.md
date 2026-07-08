---
id: UNC@20.15.2@ConfigObject@UPIPDOMAIN
type: ConfigObject
name: UPIPDOMAIN（当前UPF绑定的IP域）
nf: UNC
version: 20.15.2
object_name: UPIPDOMAIN
object_kind: entity
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# UPIPDOMAIN（当前UPF绑定的IP域）

## 说明

**适用NF：PGW-C、SMF、GGSN**

该命令用于将指定UPF绑定到特定的IPDomain，当该UPF作为会话主锚点UPF时，SMF内部会在UE IP前加上该IPDomain前缀，并带给PCF，用于扩展地址池。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-UPIPDOMAIN]] · ADD UPIPDOMAIN
- [[command/UNC/20.15.2/LST-UPIPDOMAIN]] · LST UPIPDOMAIN
- [[command/UNC/20.15.2/MOD-UPIPDOMAIN]] · MOD UPIPDOMAIN
- [[command/UNC/20.15.2/RMV-UPIPDOMAIN]] · RMV UPIPDOMAIN

## 证据

- 原始手册：`evidence/UNC/20.15.2/UPIPDOMAIN.md`
- 原始手册：`evidence/UNC/20.15.2/UPIPDOMAIN.md`
- 原始手册：`evidence/UNC/20.15.2/UPIPDOMAIN.md`
- 原始手册：`evidence/UNC/20.15.2/UPIPDOMAIN.md`
