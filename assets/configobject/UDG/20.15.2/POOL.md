---
id: UDG@20.15.2@ConfigObject@POOL
type: ConfigObject
name: POOL（地址池）
nf: UDG
version: 20.15.2
object_name: POOL
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# POOL（地址池）

## 说明

**适用NF：PGW-U、UPF**

![](添加地址池（ADD POOL）_82837132.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，如果地址池类型为local且配置RELEASETIME值过大，用户地址会延迟释放，可能会导致地址池中的地址不足，用户可能激活失败。

该命令用于为系统上激活本地分配地址用户或者静态用户接入时创建对应的地址池。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-POOL]] · ADD POOL
- [[command/UDG/20.15.2/LCK-POOL]] · LCK POOL
- [[command/UDG/20.15.2/LST-POOL]] · LST POOL
- [[command/UDG/20.15.2/MOD-POOL]] · MOD POOL
- [[command/UDG/20.15.2/RMV-POOL]] · RMV POOL

## 关联对象

- [[configobject/UDG/20.15.2/POOLBINDGROUP]] · POOLBINDGROUP
- [[configobject/UDG/20.15.2/SECTION]] · SECTION
- [[configobject/UDG/20.15.2/VPNINST]] · VPNINST

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改地址池（MOD-POOL）_86528469.md`
- 原始手册：`evidence/UDG/20.15.2/删除地址池（RMV-POOL）_82837134.md`
- 原始手册：`evidence/UDG/20.15.2/显示地址池（LST-POOL）_82837135.md`
- 原始手册：`evidence/UDG/20.15.2/添加地址池（ADD-POOL）_82837132.md`
- 原始手册：`evidence/UDG/20.15.2/锁定地址池（LCK-POOL）_82837136.md`
