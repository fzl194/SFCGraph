---
id: UNC@20.15.2@ConfigObject@ACCESSLISTIP
type: ConfigObject
name: ACCESSLISTIP（黑白名单）
nf: UNC
version: 20.15.2
object_name: ACCESSLISTIP
object_kind: entity
applicable_nf:
- GGSN
- SGW-C
- PGW-C
status: active
---

# ACCESSLISTIP（黑白名单）

## 说明

**适用NF：GGSN、SGW-C、PGW-C**

该命令用来配置黑白名单功能中SGSN/S-GW/MME的IP地址。当运营商在部署分组交换网，新增SGSN/MME/S-GW时，如果需要对SGSN/MME/S-GW进行接入控制，使用该命令增加需要被控制网元的IP地址。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ACCESSLISTIP]] · ADD ACCESSLISTIP
- [[command/UNC/20.15.2/LST-ACCESSLISTIP]] · LST ACCESSLISTIP
- [[command/UNC/20.15.2/RMV-ACCESSLISTIP]] · RMV ACCESSLISTIP

## 证据

- 原始手册：`evidence/UNC/20.15.2/ACCESSLISTIP.md`
- 原始手册：`evidence/UNC/20.15.2/ACCESSLISTIP.md`
- 原始手册：`evidence/UNC/20.15.2/ACCESSLISTIP.md`
