---
id: UNC@20.15.2@ConfigObject@NRFNFLSTCTLPLY
type: ConfigObject
name: NRFNFLSTCTLPLY（NFINFOLIST处理策略）
nf: UNC
version: 20.15.2
object_name: NRFNFLSTCTLPLY
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFNFLSTCTLPLY（NFINFOLIST处理策略）

## 说明

**适用NF：NRF**

该命令用于设置NF携带NFINFOLIST注册、更新、发现策略。

当前该命令支持网元类型为SMF，NWDAF，SMF在注册、更新请求中，NfProfile可携带smfInfo以及smfInfoList，其中smfInfoList可包含多条smfInfo。

当网络中NF均支持特性“WSFD-205015 SMF支持多服务区”时，可通过本命令设置SMF注册更新校验策略，从而实现基于位置区域优选SMF。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NRFNFLSTCTLPLY]] · LST NRFNFLSTCTLPLY
- [[command/UNC/20.15.2/SET-NRFNFLSTCTLPLY]] · SET NRFNFLSTCTLPLY

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NFINFOLIST处理策略（LST-NRFNFLSTCTLPLY）_23622950.md`
- 原始手册：`evidence/UNC/20.15.2/设置NFINFOLIST处理策略（SET-NRFNFLSTCTLPLY）_70382401.md`
