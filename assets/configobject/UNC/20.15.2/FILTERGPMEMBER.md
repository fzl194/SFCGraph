---
id: UNC@20.15.2@ConfigObject@FILTERGPMEMBER
type: ConfigObject
name: FILTERGPMEMBER（过滤器组成员）
nf: UNC
version: 20.15.2
object_name: FILTERGPMEMBER
object_kind: entity
applicable_nf:
- SMF
status: active
---

# FILTERGPMEMBER（过滤器组成员）

## 说明

**适用NF：SMF**

该命令用于在指定过滤组添加一个过滤器，添加的过滤器属于哪一个过滤组由FILTERGPID标识。

过滤器的主要参数为数据流的方向，以及本端对端地址。过滤器主要用于UPF侦测用户指定方向以及指定本端对端地址的数据流。SMF会在N4会话消息中将该信息带给UPF，UPF侦测到满足该过滤器条件的数据流后可以执行特定的操作，比如丢弃。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-FILTERGPMEMBER]] · ADD FILTERGPMEMBER
- [[command/UNC/20.15.2/LST-FILTERGPMEMBER]] · LST FILTERGPMEMBER
- [[command/UNC/20.15.2/RMV-FILTERGPMEMBER]] · RMV FILTERGPMEMBER

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除过滤器组成员（RMV-FILTERGPMEMBER）_09653634.md`
- 原始手册：`evidence/UNC/20.15.2/增加过滤器组成员（ADD-FILTERGPMEMBER）_09652219.md`
- 原始手册：`evidence/UNC/20.15.2/查询过滤器组成员（LST-FILTERGPMEMBER）_09651746.md`
