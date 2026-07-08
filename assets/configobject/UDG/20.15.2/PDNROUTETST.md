---
id: UDG@20.15.2@ConfigObject@PDNROUTETST
type: ConfigObject
name: PDNROUTETST（PDN侧路由探测）
nf: UDG
version: 20.15.2
object_name: PDNROUTETST
object_kind: action
applicable_nf:
- PGW-U
- UPF
status: active
---

# PDNROUTETST（PDN侧路由探测）

## 说明

**适用NF：PGW-U、UPF**

该命令用来控制UPF停止向PDN服务器发送探测消息，立刻结束探测。

## 操作本对象的命令

- [STP PDNROUTETST](command/UDG/20.15.2/STP-PDNROUTETST.md)
- [STR PDNROUTETST](command/UDG/20.15.2/STR-PDNROUTETST.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/停止PDN侧路由探测（STP-PDNROUTETST）_70824403.md`
- 原始手册：`evidence/UDG/20.15.2/启动PDN侧路由探测（STR-PDNROUTETST）_70824402.md`
