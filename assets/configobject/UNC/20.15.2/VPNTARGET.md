---
id: UNC@20.15.2@ConfigObject@VPNTARGET
type: ConfigObject
name: VPNTARGET（VPN Target）
nf: UNC
version: 20.15.2
object_name: VPNTARGET
object_kind: entity
status: active
---

# VPNTARGET（VPN Target）

## 说明

该命令用于设置指定VPN地址族参数VPN Target。

BGP IP VPN（L3VPN）使用32位的BGP扩展团体属性－VPN Target（也称为Route Target）来控制VPN路由信息的发布。

每个VPN实例关联一个或多个VPN Target属性。有两类VPN Target属性：

Export Target：本地PE从直接相连site学到IPv4路由后，转换为VPN IPv4路由，并为这些路由设置Export Target属性。Export Target属性作为BGP的扩展团体属性随路由发布。

Import Target：PE收到其它PE发布的VPN-IPv4路由时，检查其Export Target属性。当此属性与PE上某个VPN实例的Import Target匹配时，PE就把路由加入到该VPN实例的路由表。

也就是说，VPN Target属性定义了一条VPN路由可以为哪些site所接收，以及PE可以接收哪些site发送来的路由。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-VPNTARGET]] · ADD VPNTARGET
- [[command/UNC/20.15.2/LST-VPNTARGET]] · LST VPNTARGET
- [[command/UNC/20.15.2/RMV-VPNTARGET]] · RMV VPNTARGET

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除VPN-Target（RMV-VPNTARGET）_49961586.md`
- 原始手册：`evidence/UNC/20.15.2/增加VPN-Target（ADD-VPNTARGET）_00866341.md`
- 原始手册：`evidence/UNC/20.15.2/查询VPN-Target（LST-VPNTARGET）_00600353.md`
