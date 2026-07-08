---
id: UDG@20.15.2@ConfigObject@L2TPRDSCLIENT
type: ConfigObject
name: L2TPRDSCLIENT（APN绑定的L2TP接口）
nf: UDG
version: 20.15.2
object_name: L2TPRDSCLIENT
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# L2TPRDSCLIENT（APN绑定的L2TP接口）

## 说明

**适用NF：PGW-U、UPF**

该命令用于在APN上指定的源端Gi接口绑定关系。在AAA返回L2TP属性启动L2TP业务场景，该接口可用做系统与LNS进行交互时的源端接口。

## 操作本对象的命令

- [ADD L2TPRDSCLIENT](command/UDG/20.15.2/ADD-L2TPRDSCLIENT.md)
- [LST L2TPRDSCLIENT](command/UDG/20.15.2/LST-L2TPRDSCLIENT.md)
- [RMV L2TPRDSCLIENT](command/UDG/20.15.2/RMV-L2TPRDSCLIENT.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除APN绑定的L2TP接口（RMV-L2TPRDSCLIENT）_35373541.md`
- 原始手册：`evidence/UDG/20.15.2/增加APN绑定的L2TP接口（ADD-L2TPRDSCLIENT）_35373540.md`
- 原始手册：`evidence/UDG/20.15.2/查询APN绑定的L2TP接口（LST-L2TPRDSCLIENT）_35373542.md`
