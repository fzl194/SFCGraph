---
id: UNC@20.15.2@MMLCommand@MOD IPSECPROPOSAL
type: MMLCommand
name: MOD IPSECPROPOSAL（修改IPsec提议）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IPSECPROPOSAL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- IPsec
- IPsec提议
status: active
---

# MOD IPSECPROPOSAL（修改IPsec提议）

## 功能

该命令用于修改IP安全提议。

## 注意事项

- 该命令执行后立即生效。
- 该命令中的一些配置可能是不安全的。
- 认证算法中md5和sha1都是不安全的，建议使用sha2_256算法。
- 加密算法中3des和des都是不安全的，建议使用aes_256算法。
- 当认证算法选择null或unconfigure时，存在安全风险。
- AH认证算法不能为空，当选择unconfigure时，下发默认值。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROPOSALNAME | Proposal名称 | 可选必选说明：必选参数<br>参数含义：Proposal名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。不区分大小写。<br>默认值：无 |
| IPSECPROTOCOL | IPsec安全协议 | 可选必选说明：可选参数<br>参数含义：IPsec协议：AH / ESP。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- ah：AH协议。<br>- esp：ESP协议。<br>默认值：无 |
| ESPAUTHALGO | ESP认证算法 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPSECPROTOCOL”配置为“esp”时为可选参数。<br>参数含义：ESP认证算法：MD5 / SHA1 / SHA2-256 / SHA2-384 / SHA2-512 / NULL。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- md5：md5算法。<br>- sha1：sha1算法。<br>- sha2_256：sha2-256算法。<br>- sha2_384：sha2-384算法。<br>- sha2_512：sha2-512算法。<br>- null：空。<br>- unconfigure：未配置。<br>默认值：无 |
| ESPENCRYPTALGO | ESP加密算法 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPSECPROTOCOL”配置为“esp”时为可选参数。<br>参数含义：加密算法：DES / 3DES / AES-128 / AES-192 / AES-256。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- 3des：3DES算法。<br>- des：DES算法。<br>- aes_128：128位AES算法。<br>- aes_192：192位AES算法。<br>- aes_256：256位AES算法。<br>- null：空。<br>- unconfigure：未配置。<br>默认值：无 |
| AHAUTHALGO | AH认证算法 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPSECPROTOCOL”配置为“ah”时为可选参数。<br>参数含义：认证算法：MD5 / SHA1 / SHA2-256 / SHA2-384 / SHA2-512。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- md5：md5算法。<br>- sha1：sha1算法。<br>- sha2_256：sha2-256算法。<br>- sha2_384：sha2-384算法。<br>- sha2_512：sha2-512算法。<br>- unconfigure：未配置。<br>默认值：无 |
| ENCAPMODE | 封装模式 | 可选必选说明：可选参数<br>参数含义：封装模式。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- transport：传输模式。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPSECPROPOSAL]] · IPsec提议（IPSECPROPOSAL）

## 使用实例

修改名称为“asdf2”的IP安全提议：

```
MOD IPSECPROPOSAL:PROPOSALNAME="asdf2",IPSECPROTOCOL=ah,AHAUTHALGO=sha2_256,ENCAPMODE=transport;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-IPSECPROPOSAL.md`
