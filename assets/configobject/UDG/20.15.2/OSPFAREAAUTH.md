---
id: UDG@20.15.2@ConfigObject@OSPFAREAAUTH
type: ConfigObject
name: OSPFAREAAUTH（OSPF区域认证配置）
nf: UDG
version: 20.15.2
object_name: OSPFAREAAUTH
object_kind: entity
status: active
---

# OSPFAREAAUTH（OSPF区域认证配置）

## 说明

该命令用于创建OSPF区域认证配置。

![](创建OSPF区域认证配置（ADD OSPFAREAAUTH）_00600897.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，如果OSPF区域认证与邻居配置不同，可能会使此区域的OSPF邻接关系中断，造成业务影响。推荐使用HMAC-SHA256认证算法，并且配置满足复杂度的密码，否则有安全隐患。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-OSPFAREAAUTH]] · ADD OSPFAREAAUTH
- [[command/UDG/20.15.2/LST-OSPFAREAAUTH]] · LST OSPFAREAAUTH
- [[command/UDG/20.15.2/MOD-OSPFAREAAUTH]] · MOD OSPFAREAAUTH
- [[command/UDG/20.15.2/RMV-OSPFAREAAUTH]] · RMV OSPFAREAAUTH

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改OSPF区域认证配置（MOD-OSPFAREAAUTH）_00600321.md`
- 原始手册：`evidence/UDG/20.15.2/创建OSPF区域认证配置（ADD-OSPFAREAAUTH）_00600897.md`
- 原始手册：`evidence/UDG/20.15.2/删除OSPF区域认证配置（RMV-OSPFAREAAUTH）_50121698.md`
- 原始手册：`evidence/UDG/20.15.2/查询OSPF区域认证配置（LST-OSPFAREAAUTH）_49961934.md`
