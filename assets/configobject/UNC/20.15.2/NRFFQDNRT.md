---
id: UNC@20.15.2@ConfigObject@NRFFQDNRT
type: ConfigObject
name: NRFFQDNRT（FQDN路由）
nf: UNC
version: 20.15.2
object_name: NRFFQDNRT
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFFQDNRT（FQDN路由）

## 说明

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增基于FQDN最长后缀匹配的路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

如果针对同一个FQDN配置了多个不同的下一跳归属NRF组名称，那么当前NRF会选取下一跳所有归属NRF组中优先级最高的NRF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFFQDNRT]] · ADD NRFFQDNRT
- [[command/UNC/20.15.2/LST-NRFFQDNRT]] · LST NRFFQDNRT
- [[command/UNC/20.15.2/RMV-NRFFQDNRT]] · RMV NRFFQDNRT

## 证据

- 原始手册：`evidence/UNC/20.15.2/NRFFQDNRT.md`
- 原始手册：`evidence/UNC/20.15.2/NRFFQDNRT.md`
- 原始手册：`evidence/UNC/20.15.2/NRFFQDNRT.md`
