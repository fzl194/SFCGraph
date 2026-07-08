---
id: UDG@20.15.2@ConfigObject@IKEPEER6
type: ConfigObject
name: IKEPEER6（IPv6 IKE对等体）
nf: UDG
version: 20.15.2
object_name: IKEPEER6
object_kind: entity
status: active
---

# IKEPEER6（IPv6 IKE对等体）

## 说明

该命令用于增加IKE对等体。

> **说明**
> - 该命令执行后立即生效。
>
> - 参数IKEMSGSYNC、IPSECMSGSYNC只有在参数VERSION2为TRUE时才生效。
> - 参数LOCALIDTYPE配置为Fqdn_ipv6（Fqdn_Ipv6）或User_fqdn_ipv6（User_fqdn_ipv6）时，参数REMOTEID必须进行配置。
> - IKEV1是不安全的协议，建议使用IKEV2。
> - IKEv1国密IPSEC仅支持主模式。
> - IKEv1国密IPSEC不支持NAT穿越。
> - IKEv1国密IPSEC不支持主备隧道。
> - IKEv1仅支持国密数字信封，不支持除此之外的认证方式。
> - IP-disable仅支持IKEv1。
> - 证书字段和场景字段不能同时配置。
>
> - 最多可输入4000条记录。

## 操作本对象的命令

- [ADD IKEPEER6](command/UDG/20.15.2/ADD-IKEPEER6.md)
- [LST IKEPEER6](command/UDG/20.15.2/LST-IKEPEER6.md)
- [MOD IKEPEER6](command/UDG/20.15.2/MOD-IKEPEER6.md)
- [RMV IKEPEER6](command/UDG/20.15.2/RMV-IKEPEER6.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IPv6-IKE对等体（MOD-IKEPEER6）_21521242.md`
- 原始手册：`evidence/UDG/20.15.2/删除IPv6-IKE对等体（RMV-IKEPEER6）_21521252.md`
- 原始手册：`evidence/UDG/20.15.2/增加IPv6-IKE对等体（ADD-IKEPEER6）_21361306.md`
- 原始手册：`evidence/UDG/20.15.2/查询IPv6-IKE对等体（LST-IKEPEER6）_21521230.md`
