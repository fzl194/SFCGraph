---
id: UDG@20.15.2@ConfigObject@IPSECPROPOSALIPSEC
type: ConfigObject
name: IPSECPROPOSALIPSEC（IPsec提议）
nf: UDG
version: 20.15.2
object_name: IPSECPROPOSALIPSEC
object_kind: entity
status: active
---

# IPSECPROPOSALIPSEC（IPsec提议）

## 说明

![](增加IPsec提议（ADD IPSECPROPOSALIPSEC）_80432524.assets/notice_3.0-zh-cn.png)

该配置中的部分参数可能含有不安全算法，影响加解密安全性。

该命令用于增加IPsec安全提议。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令中的一些配置可能是不安全的。
> - 提议名称格式为“proposal”+“数字”的IPSEC提议（数字区间为80~91，例如proposal80）可以通过软参配置不安全算法MD5、DES、3DES，具体配置方法请参考产品文档相应软参文档。
> - 认证算法中Md5、Sha1是不安全的，建议使用Sha2_256算法。
> - AH认证算法不能为空，当选择Unconfigure时，下发Sha2_256算法。
> - 加密算法中DES、3DES、Aes_128、Aes_192、Aes_256是不安全的，建议使用Aes_gcm_128算法。
> - 当ESP加密算法配置AES_GCM或AES_GMAC时，ESP认证算法必须为空。
> - 当ESP加密算法不配置AES_GCM或AES_GMAC时，认证算法必须不为空。
> - 当ESP加密算法配置AES_GCM或AES_GMAC时，不能用软参配置算法。
> - 国密算法Sm3、Sm4需要设置软参开关才能使用，打开国密算法软参开关命令："SET FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=1401, DWORDVALUE=1;"，关闭国密算法软参开关命令："SET FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=1401, DWORDVALUE=0;"。
> - 老旧V3单板不支持开启国密算法加速功能。
> - 以下算法不支持IKEv1：ESP加密算法: 128位AES-GCM算法、256位AES-GCM算法、128位AES-GMAC算法、NULL。
> - IKEv1国密的IPSEC提议仅支持一种配置：IPsec安全协议为ESP，ESP认证算法为SM3，ESP加密算法为SM4，封装模式为隧道模式。
>
> - 最多可输入100条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-IPSECPROPOSALIPSEC]] · ADD IPSECPROPOSALIPSEC
- [[command/UDG/20.15.2/LST-IPSECPROPOSALIPSEC]] · LST IPSECPROPOSALIPSEC
- [[command/UDG/20.15.2/MOD-IPSECPROPOSALIPSEC]] · MOD IPSECPROPOSALIPSEC
- [[command/UDG/20.15.2/RMV-IPSECPROPOSALIPSEC]] · RMV IPSECPROPOSALIPSEC

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IPsec提议（MOD-IPSECPROPOSALIPSEC）_25912253.md`
- 原始手册：`evidence/UDG/20.15.2/删除IPsec提议（RMV-IPSECPROPOSALIPSEC）_26150763.md`
- 原始手册：`evidence/UDG/20.15.2/增加IPsec提议（ADD-IPSECPROPOSALIPSEC）_80432524.md`
- 原始手册：`evidence/UDG/20.15.2/查询IPsec提议（LST-IPSECPROPOSALIPSEC）_80910992.md`
