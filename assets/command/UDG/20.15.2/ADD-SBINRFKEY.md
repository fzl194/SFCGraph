---
id: UDG@20.15.2@MMLCommand@ADD SBINRFKEY
type: MMLCommand
name: ADD SBINRFKEY（增加NRF密钥）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SBINRFKEY
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

# ADD SBINRFKEY（增加NRF密钥）

## 功能

该命令用于增加NF认证所需的公钥。5G核心网NF间基于OAuth2.0框架使用token进行认证，NRF通过私钥对token进行数字签名，NF服务提供者通过对应的公钥校验token的数字签名是否合法。

> **说明**
> - 该命令执行后立即生效。
>
> - HTTPOAUTHKEY 命令和SBINRFKEY命令存在相同功能，且HTTPOAUTHKEY命令和SBINRFKEY命令不能配置相同的记录，更推荐使用HTTPOAUTHKEY命令。
>
> - 最多可输入128条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRFID | NRF实例ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置的NRF实例ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| NRFKEY | NRF密钥 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置的NRF密钥。<br>数据来源：本端规划<br>取值范围：任意类型，取值范围是0~1024。<br>默认值：无<br>配置原则：无 |
| KEYNAME | 密钥名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置的密钥名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SBINRFKEY]] · NRF密钥（SBINRFKEY）

## 使用实例

假设运营商需要为NRF实例bf33a517-7789-4637-b675-b3591b0d706b配置公钥，公钥名称为key1，可以用如下命令：

```
ADD SBINRFKEY: NRFID="bf33a517-7789-4637-b675-b3591b0d706b", NRFKEY="-----BEGIN PUBLIC KEY----- MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQA/axE26pXWXesAjcTP/2Tfe4EcF4A 3LuqgpIFzrftiztViq0+5deUvfcxuPIFk+ANVinlAOzgZWpFS0kheI7KJAYA3fOH n5ZTU08AAjau0CoZe9GSPUC4cnSy1nqetiKBW0YpBvhaY5FXnngvfHUHdmkFSVLC S6N+LXoi/dm0Fbo6snE= -----END PUBLIC KEY-----", KEYNAME="key1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-SBINRFKEY.md`
