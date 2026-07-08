---
id: UDG@20.15.2@MMLCommand@MOD RELAYURLAUTH
type: MMLCommand
name: MOD RELAYURLAUTH（修改媒体中继URL鉴权配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: RELAYURLAUTH
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继URL鉴权
status: active
---

# MOD RELAYURLAUTH（修改媒体中继URL鉴权配置）

## 功能

**适用NF：UPF、PGW-U**

![](修改媒体中继URL鉴权配置（MOD RELAYURLAUTH）_94871971.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，执行该命令后，会影响媒体中继防盗链校验功能。

该命令用于修改媒体中继URL鉴权配置。

## 注意事项

- 该命令执行后立即生效。
- 当URLAUTHMETHOD为TYPED时，ALGORITHM仅支持配置为HMAC_SHA1。HMAC_SHA1也仅支持URLAUTHMETHOD为TYPED时配置。
- 鉴权算法MD5、HMAC_SHA1属于不安全算法，建议优先使用SHA256算法。出于业务对接需要，必须使用MD5或HMAC_SHA1算法进行URL鉴权时，需要告知客户或服务厂商存在的安全风险并达成一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYURLAUTHNM | 媒体中继URL鉴权名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定媒体中继URL鉴权名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| RELAYAUTHKEYNM | 媒体中继鉴权密钥名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定媒体中继认证密钥名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD RELAYAUTHKEY命令配置生成。<br>- 该取值必须和ADD RELAYAUTHKEY中配置的"RELAYAUTHKEYNM"参数取值相同。 |
| URLAUTHMETHOD | URL鉴权方法 | 可选必选说明：可选参数<br>参数含义：该参数用于指定URL鉴权方法。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TYPEA：鉴权方式A。<br>- TYPEB：鉴权方式B。<br>- TYPEC1：鉴权方式C1。<br>- TYPEC2：鉴权方式C2。<br>- TYPED：鉴权方式D。<br>默认值：无<br>配置原则：无 |
| ALGORITHM | 加密算法 | 可选必选说明：可选参数<br>参数含义：该参数用于指定算法类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MD5：表示加密类型为MD5，有安全风险，不建议使用。<br>- SHA256：表示加密类型为SHA256。<br>- HMAC_SHA1：表示加密类型为HMAC_SHA1，有安全风险，不建议使用。<br>默认值：无<br>配置原则：鉴权算法MD5、HMAC_SHA1属于不安全算法，建议优先使用SHA256算法。 |
| VALIDTIME | 有效时间 | 可选必选说明：可选参数<br>参数含义：该参数用于指定有效时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是为1～144000，单位是分钟。<br>默认值：无<br>配置原则：无 |
| TIMESTAMPFMT | 时间戳格式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定时间戳格式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DECSEC：十进制。<br>- HEXSEC：十六进制。<br>- TIMESTAMP：日期。<br>- DEFAULT：不同鉴权方式的时间戳默认格式。<br>默认值：无<br>配置原则：当时间戳格式配置为Default时，自动配置为URL鉴权方法对应的默认时间戳格式。其中，TYPEA为十进制，TYPEB为日期，TYPEC1为十六进制，TYPEC2为十六进制，TYPED为十进制。 |
| AUTHFAILACT | 鉴权失败动作 | 可选必选说明：可选参数<br>参数含义：该参数用于指定鉴权失败动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FORBIDDEN：禁止访问（403）。<br>- REDIRECT：重定向。<br>默认值：无<br>配置原则：无 |
| AUTHFIELDNAME | 鉴权字段名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“URLAUTHMETHOD”配置为“TYPEA”、“TYPEC2” 或 “TYPED”时为可选参数。<br>参数含义：该参数用于指定鉴权字段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| TIMESTAMPNAME | 时间戳字段名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“URLAUTHMETHOD”配置为“TYPEC2” 或 “TYPED”时为可选参数。<br>参数含义：该参数用于指定时间戳字段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DASHAUTHEXTSW | Dash扩展鉴权开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置Dash扩展鉴权开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [媒体中继URL鉴权配置（RELAYURLAUTH）](configobject/UDG/20.15.2/RELAYURLAUTH.md)

## 使用实例

修改媒体中继URL鉴权配置：

```
MOD RELAYURLAUTH: RELAYURLAUTHNM="urlauth", RELAYAUTHKEYNM="auth1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改媒体中继URL鉴权配置（MOD-RELAYURLAUTH）_94871971.md`
