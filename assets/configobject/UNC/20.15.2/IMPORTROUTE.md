---
id: UNC@20.15.2@ConfigObject@IMPORTROUTE
type: ConfigObject
name: IMPORTROUTE（指定协议中的入口路由配置）
nf: UNC
version: 20.15.2
object_name: IMPORTROUTE
object_kind: entity
status: active
---

# IMPORTROUTE（指定协议中的入口路由配置）

## 说明

BGP协议自身不能发现路由，所以需要引入其他协议的路由（如IGP或者静态路由等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。

BGP引入路由时支持Import和Network两种方式：

Import方式是按协议类型，将OSPF路由、静态路由和直连路由等某一协议的路由注入到BGP路由表中。

Network方式比Import方式更精确，将指定前缀和掩码的一条路由注入到BGP路由表中。

该命令用于使用Import方式引入其他协议路由信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-IMPORTROUTE]] · ADD IMPORTROUTE
- [[command/UNC/20.15.2/LST-IMPORTROUTE]] · LST IMPORTROUTE
- [[command/UNC/20.15.2/MOD-IMPORTROUTE]] · MOD IMPORTROUTE
- [[command/UNC/20.15.2/RMV-IMPORTROUTE]] · RMV IMPORTROUTE

## 证据

- 原始手册：`evidence/UNC/20.15.2/IMPORTROUTE.md`
- 原始手册：`evidence/UNC/20.15.2/IMPORTROUTE.md`
- 原始手册：`evidence/UNC/20.15.2/IMPORTROUTE.md`
- 原始手册：`evidence/UNC/20.15.2/IMPORTROUTE.md`
