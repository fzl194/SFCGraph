---
id: UNC@20.15.2@ConfigObject@HTTPOAUTHKEY
type: ConfigObject
name: HTTPOAUTHKEY（HTTPOauth密钥）
nf: UNC
version: 20.15.2
object_name: HTTPOAUTHKEY
object_kind: entity
status: active
---

# HTTPOAUTHKEY（HTTPOauth密钥）

## 说明

该命令用于增加NF认证所需的公钥。5G核心网NF间基于OAuth2.0框架使用token进行认证，NRF通过私钥对token进行数字签名，NF服务提供者通过对应的公钥校验token的数字签名是否合法。

## 操作本对象的命令

- [ADD HTTPOAUTHKEY](command/UNC/20.15.2/ADD-HTTPOAUTHKEY.md)
- [LST HTTPOAUTHKEY](command/UNC/20.15.2/LST-HTTPOAUTHKEY.md)
- [RMV HTTPOAUTHKEY](command/UNC/20.15.2/RMV-HTTPOAUTHKEY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除HTTPOauth密钥（RMV-HTTPOAUTHKEY）_96728956.md`
- 原始手册：`evidence/UNC/20.15.2/增加HTTPOauth密钥（ADD-HTTPOAUTHKEY）_44728569.md`
- 原始手册：`evidence/UNC/20.15.2/查询HTTPOauth密钥（LST-HTTPOAUTHKEY）_44648417.md`
