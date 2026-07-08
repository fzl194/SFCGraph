---
id: UDG@20.15.2@ConfigObject@HTTPVPNMAP
type: ConfigObject
name: HTTPVPNMAP（HTTP VPN映射关系）
nf: UDG
version: 20.15.2
object_name: HTTPVPNMAP
object_kind: entity
status: active
---

# HTTPVPNMAP（HTTP VPN映射关系）

## 说明

该命令用于增加HTTP对端地址与本端VPN的映射关系。当使用多VPN组网，基于对端地址选择本端VPN和IP地址时，需要使用该命令配置对端地址与本端VPN的映射关系。

> **说明**
> - 该命令执行后立即生效。
>
> - 最多可输入512条记录。

## 操作本对象的命令

- [ADD HTTPVPNMAP](command/UDG/20.15.2/ADD-HTTPVPNMAP.md)
- [LST HTTPVPNMAP](command/UDG/20.15.2/LST-HTTPVPNMAP.md)
- [RMV HTTPVPNMAP](command/UDG/20.15.2/RMV-HTTPVPNMAP.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除HTTP-VPN映射关系（RMV-HTTPVPNMAP）_99472510.md`
- 原始手册：`evidence/UDG/20.15.2/增加HTTP-VPN映射关系（ADD-HTTPVPNMAP）_46111673.md`
- 原始手册：`evidence/UDG/20.15.2/查询HTTP-VPN映射关系（LST-HTTPVPNMAP）_46031597.md`
