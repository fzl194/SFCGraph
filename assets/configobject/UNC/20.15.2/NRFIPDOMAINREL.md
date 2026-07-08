---
id: UNC@20.15.2@ConfigObject@NRFIPDOMAINREL
type: ConfigObject
name: NRFIPDOMAINREL（BSF索引和IP Domain的关联关系）
nf: UNC
version: 20.15.2
object_name: NRFIPDOMAINREL
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFIPDOMAINREL（BSF索引和IP Domain的关联关系）

## 说明

**适用NF：NRF**

该命令用于新增BSF索引和IP Domain的关联关系。

该命令的使用场景为跨NRF对BSF进行寻址，基于特定IP Domain或IP Domain后缀选择BSF的路由信息，其中BSF的路由需要通过ADD NRFBSFINDEXRT提前配置。

如果针对同一个IP Domain配置了多个不同的BSF索引，那么当前NRF会选取符合条件的所有BSF索引对应NRF组中优先级最高的NRF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFIPDOMAINREL]] · ADD NRFIPDOMAINREL
- [[command/UNC/20.15.2/LST-NRFIPDOMAINREL]] · LST NRFIPDOMAINREL
- [[command/UNC/20.15.2/RMV-NRFIPDOMAINREL]] · RMV NRFIPDOMAINREL

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除BSF索引和IP-Domain的关联关系（RMV-NRFIPDOMAINREL）_45612438.md`
- 原始手册：`evidence/UNC/20.15.2/增加BSF索引和IP-Domain的关联关系（ADD-NRFIPDOMAINREL）_45612430.md`
- 原始手册：`evidence/UNC/20.15.2/查询BSF索引和IP-Domain的关联关系（LST-NRFIPDOMAINREL）_45612434.md`
