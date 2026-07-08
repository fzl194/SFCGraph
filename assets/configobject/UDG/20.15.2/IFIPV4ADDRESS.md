---
id: UDG@20.15.2@ConfigObject@IFIPV4ADDRESS
type: ConfigObject
name: IFIPV4ADDRESS（接口IPv4地址）
nf: UDG
version: 20.15.2
object_name: IFIPV4ADDRESS
object_kind: entity
status: active
---

# IFIPV4ADDRESS（接口IPv4地址）

## 说明

该命令用于配置接口的IP地址，包括逻辑接口及物理接口。物理接口是真实存在的接口。逻辑接口是指能够实现数据交换功能但物理上不存在、需要通过配置建立的接口。

## 操作本对象的命令

- [ADD IFIPV4ADDRESS](command/UDG/20.15.2/ADD-IFIPV4ADDRESS.md)
- [LST IFIPV4ADDRESS](command/UDG/20.15.2/LST-IFIPV4ADDRESS.md)
- [MOD IFIPV4ADDRESS](command/UDG/20.15.2/MOD-IFIPV4ADDRESS.md)
- [RMV IFIPV4ADDRESS](command/UDG/20.15.2/RMV-IFIPV4ADDRESS.md)

## 关联对象

- [BFDSESSION](configobject/UDG/20.15.2/BFDSESSION.md)
- [GRETUNNEL](configobject/UDG/20.15.2/GRETUNNEL.md)
- [INTERFACE](configobject/UDG/20.15.2/INTERFACE.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改接口IPv4地址（MOD-IFIPV4ADDRESS）_00601333.md`
- 原始手册：`evidence/UDG/20.15.2/删除接口IPv4地址（RMV-IFIPV4ADDRESS）_00841397.md`
- 原始手册：`evidence/UDG/20.15.2/增加接口IPv4地址（ADD-IFIPV4ADDRESS）_00865509.md`
- 原始手册：`evidence/UDG/20.15.2/查询接口IPv4地址（LST-IFIPV4ADDRESS）_49960942.md`
