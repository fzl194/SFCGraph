---
id: UDG@20.15.2@MMLCommand@RMV HTTPOAUTHKEY
type: MMLCommand
name: RMV HTTPOAUTHKEY（删除HTTPOauth密钥）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: HTTPOAUTHKEY
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP OAuth安全管理
status: active
---

# RMV HTTPOAUTHKEY（删除HTTPOauth密钥）

## 功能

该命令用于删除NF认证所需的公钥。5G核心网NF间基于OAuth2.0框架使用token进行认证，NRF通过私钥对token进行数字签名，NF服务提供者通过对应的公钥校验token的数字签名是否合法。当NRF更新私钥时，需要删除老的公钥，并配置新的私钥所对应的公钥。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定表项索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [HTTPOauth密钥（HTTPOAUTHKEY）](configobject/UDG/20.15.2/HTTPOAUTHKEY.md)

## 使用实例

若运营商想删除索引为1的配置公钥，可以用如下命令：

```
RMV HTTPOAUTHKEY: INDEX=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除HTTPOauth密钥（RMV-HTTPOAUTHKEY）_96728956.md`
