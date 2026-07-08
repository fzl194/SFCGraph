---
id: UNC@20.15.2@ConfigObject@LINKMIGRATION
type: ConfigObject
name: LINKMIGRATION（一次链路迁移操作）
nf: UNC
version: 20.15.2
object_name: LINKMIGRATION
object_kind: action
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
status: active
---

# LINKMIGRATION（一次链路迁移操作）

## 说明

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于在链路分布不均的场景下激活一次链路迁移，涉及的链路接口类型为Ga/Gx/Gy/S6b。链路迁移策略可以通过调试命令OPR DBGDATA的子命令calseqmigpolicy进行查询。

## 操作本对象的命令

- [[command/UNC/20.15.2/ACT-LINKMIGRATION]] · ACT LINKMIGRATION

## 证据

- 原始手册：`evidence/UNC/20.15.2/LINKMIGRATION.md`
