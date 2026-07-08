---
id: UNC@20.15.2@ConfigObject@SELCHFGBYIMSI
type: ConfigObject
name: SELCHFGBYIMSI（IMSI与CHF组的绑定关系）
nf: UNC
version: 20.15.2
object_name: SELCHFGBYIMSI
object_kind: entity
applicable_nf:
- SMF
- PGW-C
- GGSN
status: active
---

# SELCHFGBYIMSI（IMSI与CHF组的绑定关系）

## 说明

**适用NF：SMF、PGW-C、GGSN**

该命令用于增加IMSI与CHF组的绑定关系。一般用于拨测场景，将指定IMSI的用户的计费信息发送到指定CHF上，测试CHF的基本功能。

## 操作本对象的命令

- [ADD SELCHFGBYIMSI](command/UNC/20.15.2/ADD-SELCHFGBYIMSI.md)
- [LST SELCHFGBYIMSI](command/UNC/20.15.2/LST-SELCHFGBYIMSI.md)
- [MOD SELCHFGBYIMSI](command/UNC/20.15.2/MOD-SELCHFGBYIMSI.md)
- [RMV SELCHFGBYIMSI](command/UNC/20.15.2/RMV-SELCHFGBYIMSI.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IMSI与CHF组的绑定关系（MOD-SELCHFGBYIMSI）_33863439.md`
- 原始手册：`evidence/UNC/20.15.2/删除IMSI与CHF组的绑定关系（RMV-SELCHFGBYIMSI）_88622274.md`
- 原始手册：`evidence/UNC/20.15.2/增加IMSI与CHF组的绑定关系（ADD-SELCHFGBYIMSI）_88303804.md`
- 原始手册：`evidence/UNC/20.15.2/查询IMSI与CHF组的绑定关系（LST-SELCHFGBYIMSI）_88462354.md`
