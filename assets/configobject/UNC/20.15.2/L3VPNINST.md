---
id: UNC@20.15.2@ConfigObject@L3VPNINST
type: ConfigObject
name: L3VPNINST（L3VPN实例）
nf: UNC
version: 20.15.2
object_name: L3VPNINST
object_kind: entity
status: active
---

# L3VPNINST（L3VPN实例）

## 说明

该命令用于创建L3VPN实例。

创建VPN可以使用户获得专用虚拟的网络。

专用：VPN网络与底层承载网络之间保持资源独立，即VPN资源不被网络中非该VPN的用户所使用；且VPN能够提供足够的安全保证，确保VPN内部信息不受外部侵扰。

虚拟：VPN用户内部的通信是通过公共网络进行的，而这个公共网络同时也可以被其他非VPN用户使用，VPN用户获得的只是一个逻辑意义上的专网。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-L3VPNINST]] · ADD L3VPNINST
- [[command/UNC/20.15.2/LST-L3VPNINST]] · LST L3VPNINST
- [[command/UNC/20.15.2/MOD-L3VPNINST]] · MOD L3VPNINST
- [[command/UNC/20.15.2/RMV-L3VPNINST]] · RMV L3VPNINST

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改L3VPN实例（MOD-L3VPNINST）_00840733.md`
- 原始手册：`evidence/UNC/20.15.2/删除L3VPN实例（RMV-L3VPNINST）_50120962.md`
- 原始手册：`evidence/UNC/20.15.2/增加L3VPN实例（ADD-L3VPNINST）_49802446.md`
- 原始手册：`evidence/UNC/20.15.2/查询L3VPN实例（LST-L3VPNINST）_49961238.md`
