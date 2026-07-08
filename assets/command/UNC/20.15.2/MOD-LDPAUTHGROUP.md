---
id: UNC@20.15.2@MMLCommand@MOD LDPAUTHGROUP
type: MMLCommand
name: MOD LDPAUTHGROUP（修改LDP认证组）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: LDPAUTHGROUP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP认证组管理
status: active
---

# MOD LDPAUTHGROUP（修改LDP认证组）

## 功能

该命令用于修改LDP认证组。

## 注意事项

- 该命令执行后立即生效。
- 如果修改认证与邻居配置不同，可能会使建立成功的LDP会话中断。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| AUTHPEERGROUPNAME | 认证组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定认证组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无 |
| AUTHENTYPE | LDP认证类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定LDP认证类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MD5：MD5认证类型。MD5验证是在TCP发出去之前进行的：LDP消息在经TCP发出前，会在TCP头后面填充一个唯一的信息摘要再发出。<br>- KEYCHAIN：Keychain认证类型。Keychain类似于MD5，针对同一段信息计算出对应的信息摘要，实现LDP报文防篡改校验。Keychain允许用户定义一组密码，形成一个密码串，并且分别为每个密码指定加解密算法及密码使用的有效时间。<br>默认值：无<br>配置原则：在使用中需要注意，MD5属于不安全的加密算法，建议使用Keychain认证。 |
| MD5PASSWORD | 认证组MD5密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AUTHENTYPE”配置为“MD5”时为必选参数。<br>参数含义：该参数用于指定认证组MD5密码。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：配置的密码建议至少包含大写、小写、数字、特殊字符中的2种，并且长度不能小于6。 |
| KEYCHAINNAME | 认证组KeyChain名字 | 可选必选说明：条件必选参数<br>前提条件：该参数在“AUTHENTYPE”配置为“KEYCHAIN”时为必选参数。<br>参数含义：该参数用于指定认证组KeyChain名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：所用的KeyChain名字需提前配好。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LDPAUTHGROUP]] · LDP认证组（LDPAUTHGROUP）

## 使用实例

修改LDP认证组：

```
MOD LDPAUTHGROUP:VRFNAME="_public_",AUTHPEERGROUPNAME="bb",AUTHENTYPE=KEYCHAIN,KEYCHAINNAME="key2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-LDPAUTHGROUP.md`
