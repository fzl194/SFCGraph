---
id: UNC@20.15.2@ConfigObject@DHCPBINDPOOLGRP
type: ConfigObject
name: DHCPBINDPOOLGRP（DHCP服务器组与地址池组绑定关系）
nf: UNC
version: 20.15.2
object_name: DHCPBINDPOOLGRP
object_kind: binding
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# DHCPBINDPOOLGRP（DHCP服务器组与地址池组绑定关系）

## 说明

**适用NF：PGW-C、SMF、GGSN**

该命令用于将DHCP服务器组与地址池组相关联。当需要UNC上激活DHCP服务器分配地址的用户时，使用该命令将UNC上配置的远端地址池组和DHCP服务器组相关联。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-DHCPBINDPOOLGRP]] · ADD DHCPBINDPOOLGRP
- [[command/UNC/20.15.2/LST-DHCPBINDPOOLGRP]] · LST DHCPBINDPOOLGRP
- [[command/UNC/20.15.2/RMV-DHCPBINDPOOLGRP]] · RMV DHCPBINDPOOLGRP

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DHCP服务器组与地址池组绑定关系（RMV-DHCPBINDPOOLGRP）_87302922.md`
- 原始手册：`evidence/UNC/20.15.2/增加DHCP服务器组与地址池组绑定关系（ADD-DHCPBINDPOOLGRP）_32382543.md`
- 原始手册：`evidence/UNC/20.15.2/查询DHCP服务器组与地址池组绑定关系（LST-DHCPBINDPOOLGRP）_32102615.md`
