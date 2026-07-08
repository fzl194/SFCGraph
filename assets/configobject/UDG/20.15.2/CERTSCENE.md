---
id: UDG@20.15.2@ConfigObject@CERTSCENE
type: ConfigObject
name: CERTSCENE（证书场景描述）
nf: UDG
version: 20.15.2
object_name: CERTSCENE
object_kind: entity
status: active
---

# CERTSCENE（证书场景描述）

## 说明

该命令用来增加证书场景。

> **说明**
> - 该命令执行后立即生效。
>
> - 不能上传两本使用者字段中的参数完全相同的CA证书。如果上传，必须确保现有的CA证书、设备证书、和即将上传的证书必须都有密钥标识符作区分。
> - 若要使用吊销列表功能，对应的CA证书的密钥用法字段中，必须带有吊销列表标志。
> - 如果证书场景描述没有填，默认使用证书场景名称作为证书场景描述。
>
> - 最多可输入100条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-CERTSCENE]] · ADD CERTSCENE
- [[command/UDG/20.15.2/LST-CERTSCENE]] · LST CERTSCENE
- [[command/UDG/20.15.2/MOD-CERTSCENE]] · MOD CERTSCENE
- [[command/UDG/20.15.2/RMV-CERTSCENE]] · RMV CERTSCENE

## 证据

- 原始手册：`evidence/UDG/20.15.2/CERTSCENE.md`
- 原始手册：`evidence/UDG/20.15.2/CERTSCENE.md`
- 原始手册：`evidence/UDG/20.15.2/CERTSCENE.md`
- 原始手册：`evidence/UDG/20.15.2/CERTSCENE.md`
