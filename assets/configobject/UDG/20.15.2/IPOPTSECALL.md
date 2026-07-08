---
id: UDG@20.15.2@ConfigObject@IPOPTSECALL
type: ConfigObject
name: IPOPTSECALL（IP全局选项安全配置）
nf: UDG
version: 20.15.2
object_name: IPOPTSECALL
object_kind: entity
status: active
---

# IPOPTSECALL（IP全局选项安全配置）

## 说明

该命令用于添加IP全局选项安全配置。

通常情况下带路由选项的IP报文用于网络路径的故障诊断和特殊业务的临时传送。但是路由选项可能被网络攻击者利用，探测网络结构并发动攻击。

为了提高安全性，防止系统收到特定报文的攻击，系统可以对带路由选项的IP报文配置全局过滤策略，丢弃报文或正常处理。

如果需要配置单独路由选项过滤规则，请使用SET IPOPTSECURITY进行配置。

当全局过滤策略和单独路由选项过滤策略不一致时，有错误提示信息"选项不一致"。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-IPOPTSECALL]] · ADD IPOPTSECALL
- [[command/UDG/20.15.2/LST-IPOPTSECALL]] · LST IPOPTSECALL
- [[command/UDG/20.15.2/MOD-IPOPTSECALL]] · MOD IPOPTSECALL
- [[command/UDG/20.15.2/RMV-IPOPTSECALL]] · RMV IPOPTSECALL

## 证据

- 原始手册：`evidence/UDG/20.15.2/IPOPTSECALL.md`
- 原始手册：`evidence/UDG/20.15.2/IPOPTSECALL.md`
- 原始手册：`evidence/UDG/20.15.2/IPOPTSECALL.md`
- 原始手册：`evidence/UDG/20.15.2/IPOPTSECALL.md`
