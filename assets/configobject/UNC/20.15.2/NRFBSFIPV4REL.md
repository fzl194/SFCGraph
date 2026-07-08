---
id: UNC@20.15.2@ConfigObject@NRFBSFIPV4REL
type: ConfigObject
name: NRFBSFIPV4REL（BSF索引和IPv4的关联关系）
nf: UNC
version: 20.15.2
object_name: NRFBSFIPV4REL
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFBSFIPV4REL（BSF索引和IPv4的关联关系）

## 说明

**适用NF：NRF**

该命令用于新增BSF索引和IPv4的关联关系。

该命令的使用场景为跨NRF对BSF进行寻址，基于特定IPv4选择BSF的路由信息，其中BSF的路由需要通过ADD NRFBSFINDEXRT提前配置。

如果针对同一个IPV4配置了多个不同的BSF索引，那么当前NRF会选取符合条件的所有BSF索引对应NRF组中优先级最高的NRF。

## 操作本对象的命令

- [ADD NRFBSFIPV4REL](command/UNC/20.15.2/ADD-NRFBSFIPV4REL.md)
- [LST NRFBSFIPV4REL](command/UNC/20.15.2/LST-NRFBSFIPV4REL.md)
- [RMV NRFBSFIPV4REL](command/UNC/20.15.2/RMV-NRFBSFIPV4REL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除BSF索引和IPv4的关联关系（RMV-NRFBSFIPV4REL）_45612436.md`
- 原始手册：`evidence/UNC/20.15.2/增加BSF索引和IPv4的关联关系（ADD-NRFBSFIPV4REL）_45612408.md`
- 原始手册：`evidence/UNC/20.15.2/查询BSF索引和IPv4的关联关系（LST-NRFBSFIPV4REL）_45612432.md`
