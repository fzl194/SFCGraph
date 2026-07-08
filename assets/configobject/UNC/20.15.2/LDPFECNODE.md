---
id: UNC@20.15.2@ConfigObject@LDPFECNODE
type: ConfigObject
name: LDPFECNODE（FEC节点）
nf: UNC
version: 20.15.2
object_name: LDPFECNODE
object_kind: entity
status: active
---

# LDPFECNODE（FEC节点）

## 说明

该命令用于向FEC列表中添加FEC节点。FEC列表是多个FEC节点地址的集合，用于指导动态BFD会话的建立。以FEC列表方式触发建立BFD会话能够精确控制对哪些LDP Tunnel进行检测，从而一定程度上控制网络的开销。采用此方式，首先要建立一个FEC列表，并向列表中添加相应的FEC节点，然后配置BFD引用此列表即可。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-LDPFECNODE]] · ADD LDPFECNODE
- [[command/UNC/20.15.2/LST-LDPFECNODE]] · LST LDPFECNODE
- [[command/UNC/20.15.2/RMV-LDPFECNODE]] · RMV LDPFECNODE

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除FEC节点（RMV-LDPFECNODE）_49961710.md`
- 原始手册：`evidence/UNC/20.15.2/查询FEC节点配置（LST-LDPFECNODE）_49961106.md`
- 原始手册：`evidence/UNC/20.15.2/添加FEC节点（ADD-LDPFECNODE）_50281126.md`
