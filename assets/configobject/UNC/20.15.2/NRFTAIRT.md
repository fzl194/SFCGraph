---
id: UNC@20.15.2@ConfigObject@NRFTAIRT
type: ConfigObject
name: NRFTAIRT（TAI路由）
nf: UNC
version: 20.15.2
object_name: NRFTAIRT
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFTAIRT（TAI路由）

## 说明

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增基于TAI的路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

若服务发现过程中，NF携带TAI发现参数，匹配到的多个TAI配置指向不同的下一跳NRF组，那么当前NRF会选取下一跳所有归属NRF组中优先级最高的NRF，若优先级相同，NRF随机选取一个下一跳归属NRF组中的NRF。

若此命令与ADD NRFWILDCARDATTR命令配置了多个不同的下一跳归属NRF组名称，那么当前NRF会选取下一跳所有归属NRF组中优先级最高的NRF。

## 操作本对象的命令

- [ADD NRFTAIRT](command/UNC/20.15.2/ADD-NRFTAIRT.md)
- [LST NRFTAIRT](command/UNC/20.15.2/LST-NRFTAIRT.md)
- [MOD NRFTAIRT](command/UNC/20.15.2/MOD-NRFTAIRT.md)
- [RMV NRFTAIRT](command/UNC/20.15.2/RMV-NRFTAIRT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改TAI路由（MOD-NRFTAIRT）_09653134.md`
- 原始手册：`evidence/UNC/20.15.2/删除TAI路由（RMV-NRFTAIRT）_09653227.md`
- 原始手册：`evidence/UNC/20.15.2/增加TAI路由（ADD-NRFTAIRT）_09652595.md`
- 原始手册：`evidence/UNC/20.15.2/查询TAI路由（LST-NRFTAIRT）_09653255.md`
