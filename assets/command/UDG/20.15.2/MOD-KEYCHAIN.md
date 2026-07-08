---
id: UDG@20.15.2@MMLCommand@MOD KEYCHAIN
type: MMLCommand
name: MOD KEYCHAIN（修改Keychain的配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: KEYCHAIN
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- Keychain
- Keychain配置
status: active
---

# MOD KEYCHAIN（修改Keychain的配置）

## 功能

该命令用于修改Keychain的全局属性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYCHAINNAME | Keychain名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Keychain名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。不含问号或空格，大小写不敏感。<br>默认值：无 |
| TIMEMODE | 时间模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定时间类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LMT：Keychain的时间模式为LMT。<br>- UTC：Keychain的时间模式为UTC。<br>默认值：无 |
| RECVTOLTYPE | 接收容错时长类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接收容错时长类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DURATION：接收容错时长持续某段时间。<br>- INFINITE：接收容错时长持续永远，直到被删除。<br>默认值：无 |
| RECVTOLVALUE | 接收容错时长（min） | 可选必选说明：条件必选参数<br>前提条件：该参数在“RECVTOLTYPE”配置为“DURATION”时为必选参数。<br>参数含义：该参数用于指定发送端和接收端的Key ID不一致的容错时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～14400，单位是分钟。<br>默认值：无 |
| TCPKIND | TCP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于使用Keychain的TCP应用指定TCP类型。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为28～255。<br>默认值：无 |
| HMACMD5 | HMAC-MD5算法ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定HMAC-MD5算法标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～63。密钥长度为16bytes。<br>默认值：无<br>配置原则：为了保证更好的安全性，建议不要使用HMAC-MD5算法。 |
| HMACSHA112 | HMAC-SHA1-12算法ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定HMAC-SHA1-12算法标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～63。密钥长度为12bytes。<br>默认值：无<br>配置原则：为了保证更好的安全性，建议不要使用HMAC-SHA1-12算法。 |
| HMACSHA120 | HMAC-SHA1-20算法ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定HMAC-SHA1-20算法标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～63。密钥长度为20bytes。<br>默认值：无<br>配置原则：为了保证更好的安全性，建议不要使用HMAC-SHA1-20算法。 |
| MD5 | MD5算法ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定MD5算法标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～63。密钥长度为16bytes。<br>默认值：无<br>配置原则：为了保证更好的安全性，建议不要使用MD5算法。 |
| SHA1 | SHA-1算法ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定SHA-1算法标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～63。密钥长度为20bytes。<br>默认值：无<br>配置原则：为了保证更好的安全性，建议不要使用SHA-1算法。 |
| HMACSHA256 | HMAC-SHA-256算法ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定HMAC-SHA-256算法标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～63。密钥长度为32bytes。<br>默认值：无<br>配置原则：HMAC-SHA-256验证比其他验证方式安全性高。为了保证更好的安全性，建议使用HMAC-SHA-256验证方式。 |
| SHA256 | SHA-256算法ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定SHA-256算法标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～63。密钥长度为32bytes。<br>默认值：无<br>配置原则：SHA-256验证比其他验证方式安全性高。为了保证更好的安全性，建议使用SHA-256验证方式。 |

## 操作的配置对象

- [Keychain的配置（KEYCHAIN）](configobject/UDG/20.15.2/KEYCHAIN.md)

## 使用实例

修改Keychain ospf的接收容错时长为无限，时间模式UTC：

```
MOD KEYCHAIN:KEYCHAINNAME="ospf",TIMEMODE=UTC,RECVTOLTYPE=INFINITE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改Keychain的配置（MOD-KEYCHAIN）_50281074.md`
