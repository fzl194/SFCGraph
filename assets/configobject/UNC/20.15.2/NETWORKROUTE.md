---
id: UNC@20.15.2@ConfigObject@NETWORKROUTE
type: ConfigObject
name: NETWORKROUTE（引入路由指定前缀和掩码长度）
nf: UNC
version: 20.15.2
object_name: NETWORKROUTE
object_kind: entity
status: active
---

# NETWORKROUTE（引入路由指定前缀和掩码长度）

## 说明

该命令用于通过Network方式引入BGP外部路由信息。

BGP协议自身不能发现路由，所以需要引入其他协议的路由（如IGP或者静态路由等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。

BGP引入路由时支持Import和Network两种方式：

Import方式是按协议类型，将OSPF路由、静态路由和直连路由等某一协议的路由注入到BGP路由表中。

Network方式比Import方式更精确，将指定前缀和掩码的一条路由注入到BGP路由表中。

## 操作本对象的命令

- [ADD NETWORKROUTE](command/UNC/20.15.2/ADD-NETWORKROUTE.md)
- [LST NETWORKROUTE](command/UNC/20.15.2/LST-NETWORKROUTE.md)
- [MOD NETWORKROUTE](command/UNC/20.15.2/MOD-NETWORKROUTE.md)
- [RMV NETWORKROUTE](command/UNC/20.15.2/RMV-NETWORKROUTE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改引入路由指定前缀和掩码长度（MOD-NETWORKROUTE）_50121266.md`
- 原始手册：`evidence/UNC/20.15.2/删除引入路由指定前缀和掩码长度（RMV-NETWORKROUTE）_00600833.md`
- 原始手册：`evidence/UNC/20.15.2/增加引入路由指定前缀和掩码长度（ADD-NETWORKROUTE）_00866629.md`
- 原始手册：`evidence/UNC/20.15.2/查询引入路由指定前缀和掩码长度（LST-NETWORKROUTE）_49961058.md`
