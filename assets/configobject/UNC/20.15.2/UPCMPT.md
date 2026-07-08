---
id: UNC@20.15.2@ConfigObject@UPCMPT
type: ConfigObject
name: UPCMPT（UP节点协议兼容性配置）
nf: UNC
version: 20.15.2
object_name: UPCMPT
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
status: active
---

# UPCMPT（UP节点协议兼容性配置）

## 说明

![](增加UP节点协议兼容性配置（ADD UPCMPT）_35519267.assets/notice_3.0-zh-cn_2.png)

仅对接OpenUPF(异厂商UPF)需要配置，华为UPF不需要配置此UPCMPT，否则会导致建链失败。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于增加UP节点协议兼容性配置。

## 操作本对象的命令

- [ADD UPCMPT](command/UNC/20.15.2/ADD-UPCMPT.md)
- [LST UPCMPT](command/UNC/20.15.2/LST-UPCMPT.md)
- [MOD UPCMPT](command/UNC/20.15.2/MOD-UPCMPT.md)
- [RMV UPCMPT](command/UNC/20.15.2/RMV-UPCMPT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改UP节点协议兼容性配置（MOD-UPCMPT）_88377448.md`
- 原始手册：`evidence/UNC/20.15.2/删除UP节点协议兼容性配置（RMV-UPCMPT）_35374749.md`
- 原始手册：`evidence/UNC/20.15.2/增加UP节点协议兼容性配置（ADD-UPCMPT）_35519267.md`
- 原始手册：`evidence/UNC/20.15.2/查询UP节点协议兼容性配置（LST-UPCMPT）_88377446.md`
