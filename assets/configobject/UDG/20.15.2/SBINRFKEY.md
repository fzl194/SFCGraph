---
id: UDG@20.15.2@ConfigObject@SBINRFKEY
type: ConfigObject
name: SBINRFKEY（NRF密钥）
nf: UDG
version: 20.15.2
object_name: SBINRFKEY
object_kind: entity
status: active
---

# SBINRFKEY（NRF密钥）

## 说明

该命令用于增加NF认证所需的公钥。5G核心网NF间基于OAuth2.0框架使用token进行认证，NRF通过私钥对token进行数字签名，NF服务提供者通过对应的公钥校验token的数字签名是否合法。

> **说明**
> - 该命令执行后立即生效。
>
> - HTTPOAUTHKEY 命令和SBINRFKEY命令存在相同功能，且HTTPOAUTHKEY命令和SBINRFKEY命令不能配置相同的记录，更推荐使用HTTPOAUTHKEY命令。
>
> - 最多可输入128条记录。

## 操作本对象的命令

- [ADD SBINRFKEY](command/UDG/20.15.2/ADD-SBINRFKEY.md)
- [LST SBINRFKEY](command/UDG/20.15.2/LST-SBINRFKEY.md)
- [RMV SBINRFKEY](command/UDG/20.15.2/RMV-SBINRFKEY.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除NRF密钥（RMV-SBINRFKEY）_83653666.md`
- 原始手册：`evidence/UDG/20.15.2/增加NRF密钥（ADD-SBINRFKEY）_83972182.md`
- 原始手册：`evidence/UDG/20.15.2/查询NRF密钥（LST-SBINRFKEY）_29053333.md`
