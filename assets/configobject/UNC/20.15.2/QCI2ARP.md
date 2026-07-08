---
id: UNC@20.15.2@ConfigObject@QCI2ARP
type: ConfigObject
name: QCI2ARP（标准QCI到ARP的映射规则）
nf: UNC
version: 20.15.2
object_name: QCI2ARP
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
status: active
---

# QCI2ARP（标准QCI到ARP的映射规则）

## 说明

**适用NF：PGW-C、SMF**

该命令用于配置ARP和标准QCI的对应关系，从而通过标准QCI来映射出相应的承载ARP取值。

## 操作本对象的命令

- [LST QCI2ARP](command/UNC/20.15.2/LST-QCI2ARP.md)
- [SET QCI2ARP](command/UNC/20.15.2/SET-QCI2ARP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询标准QCI到ARP的映射规则（LST-QCI2ARP）_09653066.md`
- 原始手册：`evidence/UNC/20.15.2/设置标准QCI到ARP的映射规则（SET-QCI2ARP）_09652269.md`
