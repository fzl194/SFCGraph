---
id: UDG@20.15.2@ConfigObject@IPSECPOLICYTM
type: ConfigObject
name: IPSECPOLICYTM（IPsec策略模板）
nf: UDG
version: 20.15.2
object_name: IPSECPOLICYTM
object_kind: entity
status: active
---

# IPSECPOLICYTM（IPsec策略模板）

## 说明

![](增加IPsec策略模板（ADD IPSECPOLICYTM）_96044554.assets/notice_3.0-zh-cn.png)

增加配置，影响协商及加解密性能。

该命令用于增加IPsec策略模板。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令的策略模板只支持使用FQDN鉴权方式，否则可能导致IKE协商失败。
> - 当配置“SA按时计长”字段值为0时，该字段会采用[**SET IKEGLOBALCONFIG**](../IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md)命令中TIMESADURTN参数的取值。
>
> - 最多可输入2048条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-IPSECPOLICYTM]] · ADD IPSECPOLICYTM
- [[command/UDG/20.15.2/LST-IPSECPOLICYTM]] · LST IPSECPOLICYTM
- [[command/UDG/20.15.2/MOD-IPSECPOLICYTM]] · MOD IPSECPOLICYTM
- [[command/UDG/20.15.2/RMV-IPSECPOLICYTM]] · RMV IPSECPOLICYTM

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IPsec策略模板（MOD-IPSECPOLICYTM）_37044129.md`
- 原始手册：`evidence/UDG/20.15.2/删除IPsec策略模板（RMV-IPSECPOLICYTM）_96044558.md`
- 原始手册：`evidence/UDG/20.15.2/增加IPsec策略模板（ADD-IPSECPOLICYTM）_96044554.md`
- 原始手册：`evidence/UDG/20.15.2/查询IPsec策略模板（LST-IPSECPOLICYTM）_96204446.md`
