---
id: UNC@20.15.2@ConfigObject@NGPAGINGARPPRI
type: ConfigObject
name: NGPAGINGARPPRI（基于ARP的Paging消息在流控期间放通的优先级）
nf: UNC
version: 20.15.2
object_name: NGPAGINGARPPRI
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGPAGINGARPPRI（基于ARP的Paging消息在流控期间放通的优先级）

## 说明

**适用NF：AMF**

该命令用于配置基于ARP识别Paging消息在N2口固定速率流控期间放通的优先级。配置高优先级对应的Paging消息优先被放通，配置低优先级对应的Paging消息优先被流控。

## 操作本对象的命令

- [ADD NGPAGINGARPPRI](command/UNC/20.15.2/ADD-NGPAGINGARPPRI.md)
- [LST NGPAGINGARPPRI](command/UNC/20.15.2/LST-NGPAGINGARPPRI.md)
- [MOD NGPAGINGARPPRI](command/UNC/20.15.2/MOD-NGPAGINGARPPRI.md)
- [RMV NGPAGINGARPPRI](command/UNC/20.15.2/RMV-NGPAGINGARPPRI.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于ARP的Paging消息在流控期间放通的优先级（MOD-NGPAGINGARPPRI）_52388016.md`
- 原始手册：`evidence/UNC/20.15.2/删除基于ARP的Paging消息在流控期间放通的优先级（RMV-NGPAGINGARPPRI）_98627535.md`
- 原始手册：`evidence/UNC/20.15.2/增加基于ARP的Paging消息在流控期间放通的优先级（ADD-NGPAGINGARPPRI）_52388014.md`
- 原始手册：`evidence/UNC/20.15.2/查询基于ARP的Paging消息在流控期间放通的优先级（LST-NGPAGINGARPPRI）_98627533.md`
