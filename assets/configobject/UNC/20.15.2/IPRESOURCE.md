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

- [[command/UNC/20.15.2/ADD-IPRESOURCE]] · ADD IPRESOURCE
- [[command/UNC/20.15.2/LST-IPRESOURCE]] · LST IPRESOURCE
- [[command/UNC/20.15.2/MOD-IPRESOURCE]] · MOD IPRESOURCE
- [[command/UNC/20.15.2/RMV-IPRESOURCE]] · RMV IPRESOURCE

## 证据

- 原始手册：`evidence/UNC/20.15.2/IPRESOURCE.md`
- 原始手册：`evidence/UNC/20.15.2/IPRESOURCE.md`
- 原始手册：`evidence/UNC/20.15.2/IPRESOURCE.md`
- 原始手册：`evidence/UNC/20.15.2/IPRESOURCE.md`
