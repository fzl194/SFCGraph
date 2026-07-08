---
id: UDG@20.15.2@ConfigObject@HTTPOAUTHKEY
type: ConfigObject
name: HTTPOAUTHKEY（HTTPOauth密钥）
nf: UDG
version: 20.15.2
object_name: HTTPOAUTHKEY
object_kind: entity
status: active
---

# HTTPOAUTHKEY（HTTPOauth密钥）

## 说明

该命令用于增加NF认证所需的公钥。5G核心网NF间基于OAuth2.0框架使用token进行认证，NRF通过私钥对token进行数字签名，NF服务提供者通过对应的公钥校验token的数字签名是否合法。

> **说明**
> - 该命令执行后立即生效。
>
> - 如果NF服务消费者发送的OAuth令牌中携带了公钥标识，但NF服务提供者没有配置该公钥标识的公钥，而配置了无公钥标识的公钥，则使用无公钥标识的公钥进行校验。
> - HTTPOAUTHKEY 命令和SBINRFKEY命令存在相同功能，且HTTPOAUTHKEY命令和SBINRFKEY命令不能配置相同的记录，更推荐使用HTTPOAUTHKEY命令。
>
> - 最多可输入128条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-HTTPOAUTHKEY]] · ADD HTTPOAUTHKEY
- [[command/UDG/20.15.2/LST-HTTPOAUTHKEY]] · LST HTTPOAUTHKEY
- [[command/UDG/20.15.2/RMV-HTTPOAUTHKEY]] · RMV HTTPOAUTHKEY

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除HTTPOauth密钥（RMV-HTTPOAUTHKEY）_96728956.md`
- 原始手册：`evidence/UDG/20.15.2/增加HTTPOauth密钥（ADD-HTTPOAUTHKEY）_44728569.md`
- 原始手册：`evidence/UDG/20.15.2/查询HTTPOauth密钥（LST-HTTPOAUTHKEY）_44648417.md`
