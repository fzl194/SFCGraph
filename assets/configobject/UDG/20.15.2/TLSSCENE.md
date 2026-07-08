---
id: UDG@20.15.2@ConfigObject@TLSSCENE
type: ConfigObject
name: TLSSCENE（TLS证书场景）
nf: UDG
version: 20.15.2
object_name: TLSSCENE
object_kind: entity
status: active
---

# TLSSCENE（TLS证书场景）

## 说明

该命令用于添加TLS证书使用场景。

> **说明**
> - 该命令执行后立即生效。
>
> - 若TLSSCENE场景关联的TLSPARA “MODE”为服务端模式，当参数“VERIFYLOCALCERT”设置为“No”时，不校验本端证书，存在安全风险。
> - 当[**ADD TLSPARA**](../HTTP TLS安全管理/增加TLS参数（ADD TLSPARA）_84132096.md)命令中参数“HTTP模式”配置为Server时参数“VERIFYLOCALIP”生效，若配置为Client则参数“VERIFYLOCALIP”无实际效果。
>
> - 最多可输入254条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-TLSSCENE]] · ADD TLSSCENE
- [[command/UDG/20.15.2/LST-TLSSCENE]] · LST TLSSCENE
- [[command/UDG/20.15.2/MOD-TLSSCENE]] · MOD TLSSCENE
- [[command/UDG/20.15.2/RMV-TLSSCENE]] · RMV TLSSCENE

## 证据

- 原始手册：`evidence/UDG/20.15.2/TLSSCENE.md`
- 原始手册：`evidence/UDG/20.15.2/TLSSCENE.md`
- 原始手册：`evidence/UDG/20.15.2/TLSSCENE.md`
- 原始手册：`evidence/UDG/20.15.2/TLSSCENE.md`
