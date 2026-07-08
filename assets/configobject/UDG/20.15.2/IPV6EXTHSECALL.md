---
id: UDG@20.15.2@ConfigObject@IPV6EXTHSECALL
type: ConfigObject
name: IPV6EXTHSECALL（IPv6扩展头选项安全配置）
nf: UDG
version: 20.15.2
object_name: IPV6EXTHSECALL
object_kind: entity
status: active
---

# IPV6EXTHSECALL（IPv6扩展头选项安全配置）

## 说明

该命令用于添加IPv6扩展头选项安全配置。

通常情况下带IPv6扩展选项报文用于网络路径的故障诊断和特殊业务的临时传送。但是扩展选项可能被网络攻击者利用，探测网络结构并发动攻击。

为了提高安全性，防止系统收到特定报文的攻击，系统可以对报文特定扩展首部配置过滤策略，丢弃报文或正常处理。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-IPV6EXTHSECALL]] · ADD IPV6EXTHSECALL
- [[command/UDG/20.15.2/LST-IPV6EXTHSECALL]] · LST IPV6EXTHSECALL
- [[command/UDG/20.15.2/MOD-IPV6EXTHSECALL]] · MOD IPV6EXTHSECALL
- [[command/UDG/20.15.2/RMV-IPV6EXTHSECALL]] · RMV IPV6EXTHSECALL

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IPv6扩展头选项安全配置（MOD-IPV6EXTHSECALL）_00600801.md`
- 原始手册：`evidence/UDG/20.15.2/删除IPv6扩展头选项安全配置（RMV-IPV6EXTHSECALL）_49802466.md`
- 原始手册：`evidence/UDG/20.15.2/查询IPv6扩展头选项安全配置（LST-IPV6EXTHSECALL）_00866237.md`
- 原始手册：`evidence/UDG/20.15.2/添加IPv6扩展头选项安全配置（ADD-IPV6EXTHSECALL）_50121558.md`
