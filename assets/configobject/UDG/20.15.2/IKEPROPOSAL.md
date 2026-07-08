---
id: UDG@20.15.2@ConfigObject@IKEPROPOSAL
type: ConfigObject
name: IKEPROPOSAL（IKE提议）
nf: UDG
version: 20.15.2
object_name: IKEPROPOSAL
object_kind: entity
status: active
---

# IKEPROPOSAL（IKE提议）

## 说明

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

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-IKEPROPOSAL]] · ADD IKEPROPOSAL
- [[command/UDG/20.15.2/LST-IKEPROPOSAL]] · LST IKEPROPOSAL
- [[command/UDG/20.15.2/MOD-IKEPROPOSAL]] · MOD IKEPROPOSAL
- [[command/UDG/20.15.2/RMV-IKEPROPOSAL]] · RMV IKEPROPOSAL

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IKE提议（MOD-IKEPROPOSAL）_80592508.md`
- 原始手册：`evidence/UDG/20.15.2/删除IKE提议（RMV-IKEPROPOSAL）_25912255.md`
- 原始手册：`evidence/UDG/20.15.2/增加IKE提议（ADD-IKEPROPOSAL）_26032189.md`
- 原始手册：`evidence/UDG/20.15.2/查询IKE提议（LST-IKEPROPOSAL）_25830693.md`
