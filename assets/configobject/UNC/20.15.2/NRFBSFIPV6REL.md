---
id: UNC@20.15.2@ConfigObject@NRFBSFIPV6REL
type: ConfigObject
name: NRFBSFIPV6REL（BSF索引和IPv6的关联关系）
nf: UNC
version: 20.15.2
object_name: NRFBSFIPV6REL
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFBSFIPV6REL（BSF索引和IPv6的关联关系）

## 说明

**适用NF：NRF**

该命令用于新增BSF索引和IPv6的关联关系。

该命令的使用场景为跨NRF对BSF进行寻址，基于特定IPv6选择BSF的路由信息，其中BSF的路由需要通过ADD NRFBSFINDEXRT提前配置。

如果针对同一个IPV6配置了多个不同的BSF索引，那么当前NRF会选取符合条件的所有BSF索引对应NRF组中优先级最高的NRF。

## 操作本对象的命令

- [ADD NRFBSFIPV6REL](command/UNC/20.15.2/ADD-NRFBSFIPV6REL.md)
- [LST NRFBSFIPV6REL](command/UNC/20.15.2/LST-NRFBSFIPV6REL.md)
- [RMV NRFBSFIPV6REL](command/UNC/20.15.2/RMV-NRFBSFIPV6REL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除BSF索引和IPv6的关联关系（RMV-NRFBSFIPV6REL）_45612437.md`
- 原始手册：`evidence/UNC/20.15.2/增加BSF索引和IPv6的关联关系（ADD-NRFBSFIPV6REL）_45612409.md`
- 原始手册：`evidence/UNC/20.15.2/查询BSF索引和IPv6的关联关系（LST-NRFBSFIPV6REL）_45612433.md`
