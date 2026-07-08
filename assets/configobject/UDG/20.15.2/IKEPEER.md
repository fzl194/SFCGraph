---
id: UDG@20.15.2@ConfigObject@IKEPEER
type: ConfigObject
name: IKEPEER（IKE对等体）
nf: UDG
version: 20.15.2
object_name: IKEPEER
object_kind: entity
status: active
---

# IKEPEER（IKE对等体）

## 说明

该命令用于增加IKE对等体。

> **说明**
> - 该命令执行后立即生效。
>
> - 参数IKEMSGSYNC、IPSECMSGSYNC只有在参数VERSION2为TRUE时才生效。
> - IKEv1是不安全的协议，建议使用IKEv2。
> - IKEv1国密IPSEC仅支持主模式。
> - IKEv1国密IPSEC不支持NAT穿越。
> - IKEv1国密IPSEC不支持主备隧道。
> - IKEv1国密仅支持数字信封，不支持除此之外的认证方式。
> - IP-disable仅支持IKEv1。
> - 证书字段和场景字段不能同时配置。
> - 用于策略模板模式时不能配置对端地址。
> - 参数LOCALIDTYPE配置为Fqdn（FQDN）或User_fqdn（User-FQDN）时，参数REMOTEID必须进行配置。
>
> - 最多可输入4000条记录。

## 操作本对象的命令

- [ADD IKEPEER](command/UDG/20.15.2/ADD-IKEPEER.md)
- [LST IKEPEER](command/UDG/20.15.2/LST-IKEPEER.md)
- [MOD IKEPEER](command/UDG/20.15.2/MOD-IKEPEER.md)
- [RMV IKEPEER](command/UDG/20.15.2/RMV-IKEPEER.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IKE对等体（MOD-IKEPEER）_25830697.md`
- 原始手册：`evidence/UDG/20.15.2/删除IKE对等体（RMV-IKEPEER）_80910998.md`
- 原始手册：`evidence/UDG/20.15.2/增加IKE对等体（ADD-IKEPEER）_80592498.md`
- 原始手册：`evidence/UDG/20.15.2/查询IKE对等体（LST-IKEPEER）_80432528.md`
