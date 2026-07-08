---
id: UNC@20.15.2@ConfigObject@OSPFV3AREAAUTH
type: ConfigObject
name: OSPFV3AREAAUTH（OSPFv3区域认证配置）
nf: UNC
version: 20.15.2
object_name: OSPFV3AREAAUTH
object_kind: entity
status: active
---

# OSPFV3AREAAUTH（OSPFv3区域认证配置）

## 说明

该命令用于设置OSPFv3区域所使用的认证模式及验证口令。

![](创建OSPFv3区域认证配置（ADD OSPFV3AREAAUTH）_50120870.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，如果OSPFv3区域认证与邻居配置不同，可能会使此进程的OSPFv3邻接关系中断，造成业务影响。推荐配置满足复杂度的密码，否则有安全隐患。

## 操作本对象的命令

- [ADD OSPFV3AREAAUTH](command/UNC/20.15.2/ADD-OSPFV3AREAAUTH.md)
- [LST OSPFV3AREAAUTH](command/UNC/20.15.2/LST-OSPFV3AREAAUTH.md)
- [MOD OSPFV3AREAAUTH](command/UNC/20.15.2/MOD-OSPFV3AREAAUTH.md)
- [RMV OSPFV3AREAAUTH](command/UNC/20.15.2/RMV-OSPFV3AREAAUTH.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改OSPFv3区域认证配置（MOD-OSPFV3AREAAUTH）_00840949.md`
- 原始手册：`evidence/UNC/20.15.2/创建OSPFv3区域认证配置（ADD-OSPFV3AREAAUTH）_50120870.md`
- 原始手册：`evidence/UNC/20.15.2/删除OSPFv3区域认证配置（RMV-OSPFV3AREAAUTH）_00600997.md`
- 原始手册：`evidence/UNC/20.15.2/查询OSPFv3区域认证配置（LST-OSPFV3AREAAUTH）_49802374.md`
