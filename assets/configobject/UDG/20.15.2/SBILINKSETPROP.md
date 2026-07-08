---
id: UDG@20.15.2@ConfigObject@SBILINKSETPROP
type: ConfigObject
name: SBILINKSETPROP（SBI链路集策略）
nf: UDG
version: 20.15.2
object_name: SBILINKSETPROP
object_kind: entity
status: active
---

# SBILINKSETPROP（SBI链路集策略）

## 说明

该命令用于增加服务化接口链路集策略。

> **说明**
> - 该命令执行后立即生效。
>
> - 如果使用[**ADD SBILINKSETPROP**](增加SBI链路集策略（ADD SBILINKSETPROP）_29053325.md)增加SBI链路集策略，则需要使用[**ADD SBILINKCFG**](../服务化接口链路属性管理/增加SBI接口链路属性配置（ADD SBILINKCFG）_83813628.md)增加SBI接口链路配置，否则SBI链路集策略不生效。
> - 如果使用[**ADD SBILINKCFG**](../服务化接口链路属性管理/增加SBI接口链路属性配置（ADD SBILINKCFG）_83813628.md)配置的对端NF类型是SCP或SEPP，无法按照整系统控制链路数。
> - SYSCTRLFLG设置为是，指定链路集中的链路建立是按整系统控制；设置为否，指定链路集中的链路建立是按单进程控制。
>
> - 最多可输入255条记录。

## 操作本对象的命令

- [ADD SBILINKSETPROP](command/UDG/20.15.2/ADD-SBILINKSETPROP.md)
- [LST SBILINKSETPROP](command/UDG/20.15.2/LST-SBILINKSETPROP.md)
- [MOD SBILINKSETPROP](command/UDG/20.15.2/MOD-SBILINKSETPROP.md)
- [RMV SBILINKSETPROP](command/UDG/20.15.2/RMV-SBILINKSETPROP.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改SBI链路集策略（MOD-SBILINKSETPROP）_29053335.md`
- 原始手册：`evidence/UDG/20.15.2/删除SBI链路集策略（RMV-SBILINKSETPROP）_29291777.md`
- 原始手册：`evidence/UDG/20.15.2/增加SBI链路集策略（ADD-SBILINKSETPROP）_29053325.md`
- 原始手册：`evidence/UDG/20.15.2/查询SBI链路集策略（LST-SBILINKSETPROP）_28971843.md`
