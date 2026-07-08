---
id: UNC@20.15.2@ConfigObject@OSPFV3AUTH
type: ConfigObject
name: OSPFV3AUTH（OSPFv3认证配置）
nf: UNC
version: 20.15.2
object_name: OSPFV3AUTH
object_kind: entity
status: active
---

# OSPFV3AUTH（OSPFv3认证配置）

## 说明

该命令用于在OSPFv3进程下创建认证。

![](创建OSPFv3认证配置（ADD OSPFV3AUTH）_00600605.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，如果OSPFv3进程认证与邻居配置不同，可能会使此进程的OSPFv3邻接关系中断，造成业务影响。推荐配置满足复杂度的密码，否则有安全隐患。

## 操作本对象的命令

- [ADD OSPFV3AUTH](command/UNC/20.15.2/ADD-OSPFV3AUTH.md)
- [LST OSPFV3AUTH](command/UNC/20.15.2/LST-OSPFV3AUTH.md)
- [MOD OSPFV3AUTH](command/UNC/20.15.2/MOD-OSPFV3AUTH.md)
- [RMV OSPFV3AUTH](command/UNC/20.15.2/RMV-OSPFV3AUTH.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改OSPFv3认证配置（MOD-OSPFV3AUTH）_49801514.md`
- 原始手册：`evidence/UNC/20.15.2/创建OSPFv3认证配置（ADD-OSPFV3AUTH）_00600605.md`
- 原始手册：`evidence/UNC/20.15.2/删除OSPFv3认证配置（RMV-OSPFV3AUTH）_00841553.md`
- 原始手册：`evidence/UNC/20.15.2/查询OSPFv3进程认证配置（LST-OSPFV3AUTH）_49961174.md`
