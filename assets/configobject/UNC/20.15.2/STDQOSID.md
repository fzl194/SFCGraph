---
id: UNC@20.15.2@ConfigObject@STDQOSID
type: ConfigObject
name: STDQOSID（标准QoS ID配置）
nf: UNC
version: 20.15.2
object_name: STDQOSID
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
- GGSN
- SMF
status: active
---

# STDQOSID（标准QoS ID配置）

## 说明

**适用NF：SGW-C、PGW-C、GGSN、SMF**

该命令用于增加标准QoS ID配置。根据3GPP协议规定，最初的标准QCI/5QI只有1~9，后续协议演进增加了其他的数值作为标准QoS ID，当需要支持其他的数值作为标准QoS ID时可以通过本命令增加。关于最初的标准QCI/5QI的资源类型参见协议3GPP TS 23.203和3GPP TS 23.501。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-STDQOSID]] · ADD STDQOSID
- [[command/UNC/20.15.2/LST-STDQOSID]] · LST STDQOSID
- [[command/UNC/20.15.2/MOD-STDQOSID]] · MOD STDQOSID
- [[command/UNC/20.15.2/RMV-STDQOSID]] · RMV STDQOSID

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改标准QoS-ID配置（MOD-STDQOSID）_06399923.md`
- 原始手册：`evidence/UNC/20.15.2/删除标准QoS-ID配置（RMV-STDQOSID）_06399929.md`
- 原始手册：`evidence/UNC/20.15.2/增加标准QoS-ID配置（ADD-STDQOSID）_06399909.md`
- 原始手册：`evidence/UNC/20.15.2/查询标准QoS-ID配置（LST-STDQOSID）_06399918.md`
