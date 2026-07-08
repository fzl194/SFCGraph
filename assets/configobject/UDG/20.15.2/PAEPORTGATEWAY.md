---
id: UDG@20.15.2@ConfigObject@PAEPORTGATEWAY
type: ConfigObject
name: PAEPORTGATEWAY（PAE端口网关信息）
nf: UDG
version: 20.15.2
object_name: PAEPORTGATEWAY
object_kind: entity
identifier_parameters:
- NETWORKINDEX
status: active
---

# PAEPORTGATEWAY（PAE端口网关信息）

## 说明

该命令用于增加指定平面下内联口网关转发地址信息。

> **说明**
> - 该命令执行后立即生效。
>
> - 需要根据网关地址和掩码计算网络地址，并校验是否存在相同记录（即平面ID和网络地址相同），如果存在相同记录，不允许添加。通过该命令添加网关地址时需要确保网关地址已经在网关或交换机上完成配置且路由正常。
>
> - 最多可输入100条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-PAEPORTGATEWAY]] · ADD PAEPORTGATEWAY
- [[command/UDG/20.15.2/DSP-PAEPORTGATEWAY]] · DSP PAEPORTGATEWAY
- [[command/UDG/20.15.2/LST-PAEPORTGATEWAY]] · LST PAEPORTGATEWAY
- [[command/UDG/20.15.2/MOD-PAEPORTGATEWAY]] · MOD PAEPORTGATEWAY
- [[command/UDG/20.15.2/RMV-PAEPORTGATEWAY]] · RMV PAEPORTGATEWAY

## 证据

- 原始手册：`evidence/UDG/20.15.2/PAEPORTGATEWAY.md`
- 原始手册：`evidence/UDG/20.15.2/PAEPORTGATEWAY.md`
- 原始手册：`evidence/UDG/20.15.2/PAEPORTGATEWAY.md`
- 原始手册：`evidence/UDG/20.15.2/PAEPORTGATEWAY.md`
- 原始手册：`evidence/UDG/20.15.2/PAEPORTGATEWAY.md`
