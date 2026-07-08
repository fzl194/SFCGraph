---
id: UDG@20.15.2@MMLCommand@MOD OSPFAREAAUTH
type: MMLCommand
name: MOD OSPFAREAAUTH（修改OSPF区域认证配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: OSPFAREAAUTH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF区域认证配置
status: active
---

# MOD OSPFAREAAUTH（修改OSPF区域认证配置）

## 功能

该命令用于修改OSPF区域认证配置。

![](修改OSPF区域认证配置（MOD OSPFAREAAUTH）_00600321.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，如果OSPF区域认证与邻居配置不同，可能会使此区域的OSPF邻接关系中断，造成业务影响。推荐使用HMAC-SHA256认证算法，并且配置满足复杂度的密码，否则有安全隐患。

## 注意事项

- 该命令执行后立即生效。
- 修改OSPF区域认证，请确保和邻居认证配置相同，否则会导致邻接关系中断，影响业务。
- 只有配置了OSPF进程和OSPF区域后才能使用此命令。
- 使用区域验证时，一个区域中所有设备的接口上所配置的认证模式和口令必须一致。
- 区域验证方式的优先级低于接口验证方式的优先级。
- 当前支持配置的认证算法及密码长度均符合IETF标准规定。
- 如果配置的认证算法是Simple，MD5或者HMAC-MD5，则有安全隐患，推荐使用HMAC-SHA256算法。
- 配置的密码至少包含大写、小写、数字、特殊字符中的2种，并且长度不能小于8。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| AREAID | 区域号 | 可选必选说明：必选参数<br>参数含义：区域号。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：OSPF区域必须已经存在。请使用LST OSPFAREA命令查看可用的OSPF区域。 |
| AUTHENMODE | 认证模式 | 可选必选说明：必选参数<br>参数含义：认证模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- keychain：Keychain认证模式。<br>- hmac-sha256：HMAC-SHA256密文验证模式。<br>- simple：简单验证模式。<br>- md5：MD5密文验证模式。<br>- hmac-md5：HMAC-MD5密文验证模式。<br>默认值：无<br>配置原则：Simple、MD5或HMAC-MD5为不安全认证算法，推荐使用HMAC-SHA256。 |
| AUTHTEXTTYPE | 密文口令类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AUTHENMODE”配置为“hmac-sha256”、“simple”、“md5” 或 “hmac-md5”时为可选参数。<br>参数含义：认证密码类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- cipher：密文类型。<br>默认值：无<br>配置原则：cipher类型可以键入简单口令或密文口令，但在查看配置文件时均以密文方式显示口令。 |
| AUTHTEXTMD5 | MD5/HMAC-MD5/HMAC-SHA256 密码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AUTHENMODE”配置为“hmac-sha256”、“md5” 或 “hmac-md5”时为可选参数。<br>参数含义：MD5/HMAC-MD5/HMAC-SHA256密码。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：<br>- 字符不允许包括“？”和空格。<br>- 配置密码时，使用明文格式，长度范围为1~255。<br>- 配置的密码建议至少包含大写、小写、数字、特殊字符中的2种，并且长度不能小于8。 |
| AUTHTEXTSIMPLE | 简单认证密码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AUTHENMODE”配置为“simple”时为可选参数。<br>参数含义：简单认证密码。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为1～8。<br>默认值：无<br>配置原则：<br>- 字符不允许包括“？”和空格。<br>- 配置密码时，使用明文格式，长度范围为1~8。<br>- 配置的密码建议至少包含大写、小写、数字、特殊字符中的2种，并且长度不能小于8。 |
| KEYID | 密文验证字标识符 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AUTHENMODE”配置为“hmac-sha256”、“md5” 或 “hmac-md5”时为可选参数。<br>参数含义：密文验证字标识符。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：<br>- 密文验证字标识符和加密认证密码必须同时配置。<br>- KeyID需要跟对端保持一致。 |
| KEYCHAINNAME | KeyChain名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AUTHENMODE”配置为“keychain”时为必选参数。<br>参数含义：KeyChain名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：<br>- 不区分大小写，并且字符不允许包括“？”和空格。<br>- Keychain需要在Keychain模块已经配置。<br>- Keychain可以使用的安全认证算法有sha-256及hmac-sha-256。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFAREAAUTH]] · OSPF区域认证配置（OSPFAREAAUTH）

## 使用实例

修改OSPF进程1区域0.0.0.0下的认证keychain名称：

```
MOD OSPFAREAAUTH:PROCID=1,AREAID="0.0.0.0",AUTHENMODE=keychain,KEYCHAINNAME="KcName2";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改OSPF区域认证配置（MOD-OSPFAREAAUTH）_00600321.md`
