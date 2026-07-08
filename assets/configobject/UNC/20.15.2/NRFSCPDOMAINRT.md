---
id: UNC@20.15.2@ConfigObject@NRFSCPDOMAINRT
type: ConfigObject
name: NRFSCPDOMAINRT（SCP Domain最长匹配后缀转发路由）
nf: UNC
version: 20.15.2
object_name: NRFSCPDOMAINRT
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFSCPDOMAINRT（SCP Domain最长匹配后缀转发路由）

## 说明

**适用NF：NRF**

该命令用于新增基于SCP Domain的最长匹配后缀的转发路由。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

如果针对同一个SCP Domain配置了多个不同的下一跳归属NRF组名称，那么当前NRF会选取下一跳所有归属NRF组中优先级最高的NRF。

## 操作本对象的命令

- [ADD NRFSCPDOMAINRT](command/UNC/20.15.2/ADD-NRFSCPDOMAINRT.md)
- [LST NRFSCPDOMAINRT](command/UNC/20.15.2/LST-NRFSCPDOMAINRT.md)
- [RMV NRFSCPDOMAINRT](command/UNC/20.15.2/RMV-NRFSCPDOMAINRT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SCP-Domain最长匹配后缀转发路由（RMV-NRFSCPDOMAINRT）_83743802.md`
- 原始手册：`evidence/UNC/20.15.2/增加SCP-Domain最长匹配后缀转发路由（ADD-NRFSCPDOMAINRT）_29543429.md`
- 原始手册：`evidence/UNC/20.15.2/查询SCP-Domain最长匹配后缀转发路由（LST-NRFSCPDOMAINRT）_29461977.md`
