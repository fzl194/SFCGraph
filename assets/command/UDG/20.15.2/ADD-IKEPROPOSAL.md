---
id: UDG@20.15.2@MMLCommand@ADD IKEPROPOSAL
type: MMLCommand
name: ADD IKEPROPOSAL（增加IKE提议）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: IKEPROPOSAL
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IKE安全提议
status: active
---

# ADD IKEPROPOSAL（增加IKE提议）

## 功能

![](增加IKE提议（ADD IKEPROPOSAL）_26032189.assets/notice_3.0-zh-cn.png)

该配置中部分参数含有不安全算法，影响加解密安全性。

该命令用于增加IKE安全提议。

> **说明**
> - 该命令执行后立即生效。
>
> - 提议号为80~91的IKE提议可以通过软参配置不安全算法MD5、DES、3DES，具体配置方法请参考产品文档相应软参文档。
> - DH组Dh_group1、Dh_group2、Dh_group5和Dh_group14都是不安全的，建议Dh_group19，但Dh_group19计算较慢。
> - 认证算法Md5、Sha1是不安全的，建议使用Sha2_256算法。
> - 加密算法DES、3DES、Aes_cbc_128、Aes_cbc_192、Aes_cbc_256是不安全的，建议使用Aes_gcm_128算法。
> - 完整性算法Hmac_md5_96、Hmac_sha1_96是不安全的，建议使用Hmac_sha2_256算法。
> - 认证方式使用RSA数字签名存在安全风险，使用证书认证时，推荐使用数字证书认证，并使用Pss填充方式。
> - Pkcs填充方式不安全，建议使用Pss填充方式。
> - 国密算法Sm3、Sm4需要设置软参开关才能使用，打开国密算法软参开关命令："SET FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=1401, DWORDVALUE=1;"，关闭国密算法软参开关命令："SET FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=1401, DWORDVALUE=0;"。
> - 以下算法不支持IKEv1：认证算法: Sha2_384算法、Sha_512算法；加密算法: Aes_gcm_128算法、Aes_gcm_256算法；完整性算法：Sha2-512算法；DH组: Dh_group19、Dh_group20、Dh_group31。
> - IKEv1国密算法标准仅有一个算法套：认证方式是数字信封，对称加密算法是SM4，非对称加密算法是SM2，完整性算法是SM3。
> - IKEv1国密IPSEC不支持预共享密钥。
> - IKEv1国密IPSEC不支持配置DH算法。
> - 从国密数字信封认证方法切换至其他认证方法时，请检查DH组是否配置。
> - 国密数字信封场景下不能用软参方式更改算法。
> - 由于用户级IPSEC链路只支持被动响应协商，“SA持续长度”字段配置不生效。
>
> - 最多可输入1000000条记录。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | PROPOSALNUMBER | AUTHMETHOD | AUTHALGORITHM | ENCRALGORITHM | INTEGALGORITHM | DHGROUP | SADURATION |
> | --- | --- | --- | --- | --- | --- | --- |
> | 101 | Pre_share | Sha2_256 | Aes_cbc_256 | Hmac_sha2_256 | Dh_group14 | 86400 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROPOSALNUMBER | 安全提议号 | 可选必选说明：必选参数<br>参数含义：提议编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967295。101不支持配置，但可以查询。<br>默认值：无<br>配置原则：无 |
| AUTHMETHOD | 认证方法 | 可选必选说明：可选参数<br>参数含义：认证方法。<br>数据来源：对端协商<br>取值范围：<br>- “Pre_share（预共享）”：预共享密钥方式<br>- “Rsa_signature（RSA数字签名）”：RSA数字签名<br>- “Cert_signature（数字证书签名）”：数字证书签名<br>- “Digital_envelope（数字信封）”：数字信封<br>默认值：Pre_share<br>配置原则：无 |
| AUTHALGORITHM | 认证算法 | 可选必选说明：可选参数<br>参数含义：认证算法。<br>数据来源：对端协商<br>取值范围：<br>- “Md5（Md5算法）”：Md5算法<br>- “Sha1（Sha1算法）”：Sha1算法<br>- “Sha2_256（Sha2-256算法）”：Sha2-256算法<br>- “Sha2_384（Sha2-384算法）”：Sha2-384算法<br>- “Sha2_512（Sha2-512算法）”：Sha2-512算法<br>默认值：Sha2_256<br>配置原则：无 |
| ENCRALGORITHM | 加密算法 | 可选必选说明：可选参数<br>参数含义：加密算法。<br>数据来源：对端协商<br>取值范围：<br>- “Des_cbc（DES算法）”：DES算法<br>- “Aes_cbc_128（128位AES算法）”：128位AES算法<br>- “Aes_cbc_192（192位AES算法）”：192位AES算法<br>- “Aes_cbc_256（256位AES算法）”：256位AES算法<br>- “Alg_3Des_cbc（3DES算法）”：3DES算法<br>- “Aes_gcm_128（128位AES-GCM算法）”：128位AES-GCM算法<br>- “Aes_gcm_256（256位AES-GCM算法）”：256位AES-GCM算法<br>- “Sm4（SM4算法）”：SM4算法<br>默认值：Aes_gcm_128<br>配置原则：无 |
| INTEGALGORITHM | 完整性算法 | 可选必选说明：可选参数<br>参数含义：完整性算法。<br>数据来源：对端协商<br>取值范围：<br>- “Hmac_md5_96（Md5算法）”：Md5算法<br>- “Hmac_sha1_96（Sha1算法）”：Sha1算法<br>- “Hmac_sha2_256（Sha2-256算法）”：Sha2-256算法<br>- “Hmac_sha2_384（Sha2-384算法）”：Sha2-384算法<br>- “Aes_xcbc_96（Aes-xcbc-96算法）”：Aes-xcbc-96算法<br>- “Sm3（Sm3算法）”：Sm3算法<br>- “Hmac_sha2_512（Sha2-512算法）”：Sha2-512算法<br>默认值：Hmac_sha2_256<br>配置原则：无 |
| DHGROUP | DH组 | 可选必选说明：可选参数<br>参数含义：DH组。<br>数据来源：对端协商<br>取值范围：<br>- None（无）<br>- “Dh_group1（DH组1）”：DH组1，不安全的DH组<br>- “Dh_group2（DH组2）”：DH组2，不安全的DH组<br>- “Dh_group5（DH组5）”：DH组5，不安全的DH组<br>- “Dh_group14（DH组14）”：DH组14，不安全的DH组<br>- “Dh_group19（DH组19）”：DH组19，推荐的安全DH组<br>- “Dh_group20（DH组20）”：DH组20，推荐的安全DH组<br>- “Dh_group31（DH组31）”：DH组31，推荐的安全DH组<br>默认值：Dh_group19<br>配置原则：无 |
| REAUTHINTERVAL | 重认证间隔 (s) | 可选必选说明：可选参数<br>参数含义：重认证周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是60~604800，单位是秒。<br>默认值：无<br>配置原则：无 |
| SADURATION | SA持续长度 (s) | 可选必选说明：可选参数<br>参数含义：SA生命周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是60~604800，单位是秒。<br>默认值：86400<br>配置原则：无 |
| SIGHASHALGNEGSW | 签名哈希算法协商开关 | 可选必选说明：该参数在"AUTHMETHOD"配置为"Cert_signature"时为条件可选参数。<br>参数含义：签名哈希算法协商开关。<br>数据来源：对端协商<br>取值范围：<br>- “Disable（未使能）”：未使能<br>- “Enable（使能）”：使能<br>默认值：Enable<br>配置原则：无 |
| SIGNPADDING | 签名填充方式 | 可选必选说明：该参数在"SIGHASHALGNEGSW"配置为"Enable"时为条件可选参数。<br>参数含义：签名填充方式。<br>数据来源：对端协商<br>取值范围：<br>- “Pkcs（Pkcs填充）”：Pkcs填充<br>- “Pss（Pss填充）”：Pss填充<br>默认值：Pss<br>配置原则：无 |
| ASYMENCRALG | 非对称加密算法 | 可选必选说明：该参数在"AUTHMETHOD"配置为"Digital_envelope"时为条件必选参数。<br>参数含义：非对称加密算法。<br>数据来源：本端规划<br>取值范围：<br>- “NULL（空）”：空<br>- “Sm2（Sm2算法）”：Sm2算法<br>默认值：Sm2<br>配置原则：无 |

## 操作的配置对象

- [IKE提议（IKEPROPOSAL）](configobject/UDG/20.15.2/IKEPROPOSAL.md)

## 关联任务

- [0-00213](task/UDG/20.15.2/0-00213.md)

## 使用实例

增加IKE安全提议号为1的IKE安全提议：

```
ADD IKEPROPOSAL:PROPOSALNUMBER=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加IKE提议（ADD-IKEPROPOSAL）_26032189.md`
