---
id: UDG@20.15.2@ConfigObject@LDPFECLIST
type: ConfigObject
name: LDPFECLIST（FEC列表）
nf: UDG
version: 20.15.2
object_name: LDPFECLIST
object_kind: entity
status: active
---

# LDPFECLIST（FEC列表）

## 说明

该命令用于添加FEC列表。FEC列表是多个FEC节点地址的集合，用于指导动态BFD会话的建立。以FEC列表方式触发建立BFD会话能够精确控制对哪些LDP Tunnel进行检测，从而一定程度上控制网络的开销。采用此方式，首先要建立一个FEC列表，并向列表中添加相应的FEC节点，然后配置BFD引用此列表即可。

## 操作本对象的命令

- [ADD LDPFECLIST](command/UDG/20.15.2/ADD-LDPFECLIST.md)
- [LST LDPFECLIST](command/UDG/20.15.2/LST-LDPFECLIST.md)
- [RMV LDPFECLIST](command/UDG/20.15.2/RMV-LDPFECLIST.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除FEC列表（RMV-LDPFECLIST）_50121438.md`
- 原始手册：`evidence/UDG/20.15.2/查询FEC列表配置（LST-LDPFECLIST）_49801438.md`
- 原始手册：`evidence/UDG/20.15.2/添加FEC列表（ADD-LDPFECLIST）_00841377.md`
