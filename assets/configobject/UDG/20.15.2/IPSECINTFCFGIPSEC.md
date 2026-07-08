---
id: UDG@20.15.2@ConfigObject@IPSECINTFCFGIPSEC
type: ConfigObject
name: IPSECINTFCFGIPSEC（IPsec隧道接口）
nf: UDG
version: 20.15.2
object_name: IPSECINTFCFGIPSEC
object_kind: entity
status: active
---

# IPSECINTFCFGIPSEC（IPsec隧道接口）

## 说明

该命令用于增加IPsec隧道。

> **说明**
> - 该命令执行后立即生效。
>
> - 此配置会将安全策略与接口进行绑定，若配置了空的安全策略，则不会进行记录，只有配置真实有效的安全策略才会生成IPsec隧道接口。
>
> - 最多可输入512条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-IPSECINTFCFGIPSEC]] · ADD IPSECINTFCFGIPSEC
- [[command/UDG/20.15.2/LST-IPSECINTFCFGIPSEC]] · LST IPSECINTFCFGIPSEC
- [[command/UDG/20.15.2/MOD-IPSECINTFCFGIPSEC]] · MOD IPSECINTFCFGIPSEC
- [[command/UDG/20.15.2/RMV-IPSECINTFCFGIPSEC]] · RMV IPSECINTFCFGIPSEC

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IPsec隧道接口（MOD-IPSECINTFCFGIPSEC）_80751070.md`
- 原始手册：`evidence/UDG/20.15.2/删除IPsec隧道接口（RMV-IPSECINTFCFGIPSEC）_80592512.md`
- 原始手册：`evidence/UDG/20.15.2/增加IPsec隧道接口（ADD-IPSECINTFCFGIPSEC）_80910986.md`
- 原始手册：`evidence/UDG/20.15.2/查询IPsec隧道接口（LST-IPSECINTFCFGIPSEC）_26150755.md`
