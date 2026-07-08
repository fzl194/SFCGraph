---
id: UNC@20.15.2@ConfigObject@IPRESOURCE
type: ConfigObject
name: IPRESOURCE（IP资源）
nf: UNC
version: 20.15.2
object_name: IPRESOURCE
object_kind: entity
applicable_nf:
- NCG
status: active
---

# IPRESOURCE（IP资源）

## 说明

**适用NF：NCG**

该命令用于增加CG侧话单接收、分发和备份时所使用的IP地址等信息，包含添加、删除、修改、查询IP资源命令。

以下应用情况时，需要增加IP资源：

1、接收对端网元发来的话单：CG配置一个IP地址用来接收话单。

2、将话单分发到计费中心：CG采用一个IP地址与计费中心通信。

3、将话单备份到第三方服务器/UDN服务器：CG采用一个IP地址与第三方服务器/UDN服务器通信。

## 操作本对象的命令

- [ADD IPRESOURCE](command/UNC/20.15.2/ADD-IPRESOURCE.md)
- [LST IPRESOURCE](command/UNC/20.15.2/LST-IPRESOURCE.md)
- [MOD IPRESOURCE](command/UNC/20.15.2/MOD-IPRESOURCE.md)
- [RMV IPRESOURCE](command/UNC/20.15.2/RMV-IPRESOURCE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IP资源（MOD-IPRESOURCE）_51174284.md`
- 原始手册：`evidence/UNC/20.15.2/删除IP资源（RMV-IPRESOURCE）_51174283.md`
- 原始手册：`evidence/UNC/20.15.2/增加IP资源（ADD-IPRESOURCE）_51174282.md`
- 原始手册：`evidence/UNC/20.15.2/查询IP资源（LST-IPRESOURCE）_51174285.md`
