---
id: UDG@20.15.2@ConfigObject@IPOPTSECURITY
type: ConfigObject
name: IPOPTSECURITY（IP选项安全配置）
nf: UDG
version: 20.15.2
object_name: IPOPTSECURITY
object_kind: global_setting
status: active
---

# IPOPTSECURITY（IP选项安全配置）

## 说明

该命令用于设置带路由选项的IP报文的安全配置。

通常情况下带路由选项的IP报文用于网络路径的故障诊断和特殊业务的临时传送。但是路由选项可能被网络攻击者利用，探测网络结构并发动攻击。所以需要利用命令行控制系统是否处理这些带路由选项的IP报文。

缺省情况下，设备处理带路由选项的IP报文。当为了防止针对这种报文的攻击时，可以去使能系统处理带路由选项IP报文的功能。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-IPOPTSECURITY]] · LST IPOPTSECURITY
- [[command/UDG/20.15.2/SET-IPOPTSECURITY]] · SET IPOPTSECURITY

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IP选项安全配置（LST-IPOPTSECURITY）_00440645.md`
- 原始手册：`evidence/UDG/20.15.2/设置IP选项安全配置（SET-IPOPTSECURITY）_00865745.md`
