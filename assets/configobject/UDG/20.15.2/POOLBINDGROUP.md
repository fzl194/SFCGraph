---
id: UDG@20.15.2@ConfigObject@POOLBINDGROUP
type: ConfigObject
name: POOLBINDGROUP（地址池绑定地址池组中的地址池优先级）
nf: UDG
version: 20.15.2
object_name: POOLBINDGROUP
object_kind: binding
applicable_nf:
- PGW-U
- UPF
status: active
---

# POOLBINDGROUP（地址池绑定地址池组中的地址池优先级）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置指定地址池与地址池组的绑定关系。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-POOLBINDGROUP]] · ADD POOLBINDGROUP
- [[command/UDG/20.15.2/LST-POOLBINDGROUP]] · LST POOLBINDGROUP
- [[command/UDG/20.15.2/MOD-POOLBINDGROUP]] · MOD POOLBINDGROUP
- [[command/UDG/20.15.2/RMV-POOLBINDGROUP]] · RMV POOLBINDGROUP

## 关联对象

- [[configobject/UDG/20.15.2/POOL]] · POOL
- [[configobject/UDG/20.15.2/POOLGROUP]] · POOLGROUP

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改地址池绑定地址池组中的地址池优先级（MOD-POOLBINDGROUP）_82837144.md`
- 原始手册：`evidence/UDG/20.15.2/将地址池从地址池组中移除（RMV-POOLBINDGROUP）_82837145.md`
- 原始手册：`evidence/UDG/20.15.2/显示地址池与地址池组绑定关系（LST-POOLBINDGROUP）_82837146.md`
- 原始手册：`evidence/UDG/20.15.2/绑定地址池到地址池组（ADD-POOLBINDGROUP）_82837143.md`
