---
id: UNC@20.15.2@ConfigObject@STATICWTPOLICY
type: ConfigObject
name: STATICWTPOLICY（服务类型在POD实例下的静态权重）
nf: UNC
version: 20.15.2
object_name: STATICWTPOLICY
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
- AMF
status: active
---

# STATICWTPOLICY（服务类型在POD实例下的静态权重）

## 说明

![](增加服务类型在POD实例下的静态权重（ADD STATICWTPOLICY）_51175613.assets/notice_3.0-zh-cn_2.png)

如果配置不合理会导致不同POD间负载不均衡。

**适用NF：SGW-C、PGW-C、SMF、GGSN、AMF**

该命令用于增加服务类型在POD实例下的静态权重。

## 操作本对象的命令

- [ADD STATICWTPOLICY](command/UNC/20.15.2/ADD-STATICWTPOLICY.md)
- [LST STATICWTPOLICY](command/UNC/20.15.2/LST-STATICWTPOLICY.md)
- [MOD STATICWTPOLICY](command/UNC/20.15.2/MOD-STATICWTPOLICY.md)
- [RMV STATICWTPOLICY](command/UNC/20.15.2/RMV-STATICWTPOLICY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改服务类型在POD实例下的静态权重（MOD-STATICWTPOLICY）_24015944.md`
- 原始手册：`evidence/UNC/20.15.2/删除服务类型在POD实例下的静态权重（RMV-STATICWTPOLICY）_51175641.md`
- 原始手册：`evidence/UNC/20.15.2/增加服务类型在POD实例下的静态权重（ADD-STATICWTPOLICY）_51175613.md`
- 原始手册：`evidence/UNC/20.15.2/查询服务类型在POD实例下的静态权重（LST-STATICWTPOLICY）_51335393.md`
