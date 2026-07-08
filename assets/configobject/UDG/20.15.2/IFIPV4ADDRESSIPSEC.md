---
id: UDG@20.15.2@ConfigObject@IFIPV4ADDRESSIPSEC
type: ConfigObject
name: IFIPV4ADDRESSIPSEC（接口IPv4地址）
nf: UDG
version: 20.15.2
object_name: IFIPV4ADDRESSIPSEC
object_kind: entity
status: active
---

# IFIPV4ADDRESSIPSEC（接口IPv4地址）

## 说明

该命令用于配置接口的IP地址，包括逻辑接口及物理接口。物理接口是真实存在的接口。逻辑接口是指能够实现数据交换功能但物理上不存在、需要通过配置建立的接口。

> **说明**
> - 该命令执行后立即生效。
>
> - 该接口需要支持配置IP地址。
> - 该命令在版本升级过程中禁止执行。
> - 每个主用接口最大允许配置256个接口IP地址：1个主IP地址和255个从IP地址。
> - 该命令的必选参数IFNAME可通过[**LST INTERFACEIPSEC**](../接口配置/查询接口（LST INTERFACEIPSEC）_80592504.md)命令查询到。
>
> - 最多可输入65535条记录。

## 操作本对象的命令

- [ADD IFIPV4ADDRESSIPSEC](command/UDG/20.15.2/ADD-IFIPV4ADDRESSIPSEC.md)
- [LST IFIPV4ADDRESSIPSEC](command/UDG/20.15.2/LST-IFIPV4ADDRESSIPSEC.md)
- [MOD IFIPV4ADDRESSIPSEC](command/UDG/20.15.2/MOD-IFIPV4ADDRESSIPSEC.md)
- [RMV IFIPV4ADDRESSIPSEC](command/UDG/20.15.2/RMV-IFIPV4ADDRESSIPSEC.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改接口IPv4地址（MOD-IFIPV4ADDRESSIPSEC）_25912251.md`
- 原始手册：`evidence/UDG/20.15.2/删除接口IPv4地址（RMV-IFIPV4ADDRESSIPSEC）_26150761.md`
- 原始手册：`evidence/UDG/20.15.2/增加接口IPv4地址（ADD-IFIPV4ADDRESSIPSEC）_80432522.md`
- 原始手册：`evidence/UDG/20.15.2/查询接口IPv4地址（LST-IFIPV4ADDRESSIPSEC）_80751064.md`
