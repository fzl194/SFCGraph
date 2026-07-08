---
id: UNC@20.15.2@ConfigObject@AGENTIP
type: ConfigObject
name: AGENTIP（远端地址池代理IP信息）
nf: UNC
version: 20.15.2
object_name: AGENTIP
object_kind: entity
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# AGENTIP（远端地址池代理IP信息）

## 说明

**适用NF：PGW-C、SMF、GGSN**

该命令用于添加远端地址池的代理IP地址和IP地址请求消息中必须携带的代理IP地址。

DHCP服务器查找包含该代理IP地址的地址池，按照DHCP服务器上的地址分配策略分配IP地址给UNC，再由UNC下发给UE。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-AGENTIP]] · ADD AGENTIP
- [[command/UNC/20.15.2/LST-AGENTIP]] · LST AGENTIP
- [[command/UNC/20.15.2/RMV-AGENTIP]] · RMV AGENTIP

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除远端地址池代理IP信息（RMV-AGENTIP）_87143004.md`
- 原始手册：`evidence/UNC/20.15.2/增加远端地址池代理IP信息（ADD-AGENTIP）_32224047.md`
- 原始手册：`evidence/UNC/20.15.2/查询远端地址池代理IP信息（LST-AGENTIP）_87302920.md`
