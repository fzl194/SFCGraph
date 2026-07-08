---
id: UNC@20.15.2@ConfigObject@INTELLISUFFIX
type: ConfigObject
name: INTELLISUFFIX（智能业务后缀）
nf: UNC
version: 20.15.2
object_name: INTELLISUFFIX
object_kind: entity
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# INTELLISUFFIX（智能业务后缀）

## 说明

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加一个智能业务后缀，该后缀用于与PCF下发的rulename后缀进行匹配，匹配成功则为该会话优选支持智能业务的UPF。

## 操作本对象的命令

- [ADD INTELLISUFFIX](command/UNC/20.15.2/ADD-INTELLISUFFIX.md)
- [LST INTELLISUFFIX](command/UNC/20.15.2/LST-INTELLISUFFIX.md)
- [RMV INTELLISUFFIX](command/UNC/20.15.2/RMV-INTELLISUFFIX.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除智能业务后缀（RMV-INTELLISUFFIX）_72857885.md`
- 原始手册：`evidence/UNC/20.15.2/增加智能业务后缀（ADD-INTELLISUFFIX）_22378012.md`
- 原始手册：`evidence/UNC/20.15.2/查询智能业务后缀（LST-INTELLISUFFIX）_22697900.md`
