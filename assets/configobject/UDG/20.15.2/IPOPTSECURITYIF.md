---
id: UDG@20.15.2@ConfigObject@IPOPTSECURITYIF
type: ConfigObject
name: IPOPTSECURITYIF（接口IP选项安全配置）
nf: UDG
version: 20.15.2
object_name: IPOPTSECURITYIF
object_kind: entity
status: active
---

# IPOPTSECURITYIF（接口IP选项安全配置）

## 说明

该命令用于添加指定接口上带路由选项的IP报文的安全配置。接口名称可以通过LST INTERFACE命令获取。

通常情况下带路由选项的IP报文用于网络路径的故障诊断和特殊业务的临时传送。但是路由选项可能被网络攻击者利用，探测网络结构并发动攻击。缺省情况下，设备处理带路由选项的IP报文。为了防止针对这种报文的攻击，可以使用该命令去使能系统处理带路由选项IP报文的功能。

## 操作本对象的命令

- [ADD IPOPTSECURITYIF](command/UDG/20.15.2/ADD-IPOPTSECURITYIF.md)
- [LST IPOPTSECURITYIF](command/UDG/20.15.2/LST-IPOPTSECURITYIF.md)
- [MOD IPOPTSECURITYIF](command/UDG/20.15.2/MOD-IPOPTSECURITYIF.md)
- [RMV IPOPTSECURITYIF](command/UDG/20.15.2/RMV-IPOPTSECURITYIF.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改接口IP选项安全配置（MOD-IPOPTSECURITYIF）_00866365.md`
- 原始手册：`evidence/UDG/20.15.2/删除接口IP选项安全配置（RMV-IPOPTSECURITYIF）_50121722.md`
- 原始手册：`evidence/UDG/20.15.2/增加接口IP选项安全配置（ADD-IPOPTSECURITYIF）_49960954.md`
- 原始手册：`evidence/UDG/20.15.2/查询接口IP选项安全配置（LST-IPOPTSECURITYIF）_49961306.md`
