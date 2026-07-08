---
id: UNC@20.15.2@ConfigObject@NRFKEY
type: ConfigObject
name: NRFKEY（NRF密钥）
nf: UNC
version: 20.15.2
object_name: NRFKEY
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFKEY（NRF密钥）

## 说明

![](增加NRF密钥（ADD NRFKEY）_09651563.assets/notice_3.0-zh-cn_2.png)

请注意TOKEN签名算法时私钥的长度设置，以确保密钥的安全性。当TOKEN签名算法为RSA类型时，建议原始私钥长度不小于3072bit；当TOKEN签名算法配置为ECC类型时，建议原始私钥长度不小于256bit。若配置的密钥算法对应的长度不满足要求，则密钥算法可能会被攻击破解，导致私钥泄露。

**适用NF：NRF**

NF服务消费者获取到Token后，携带Token访问NF服务提供方的服务。NF服务提供方会对NF服务消费者进行认证，校验Token是否正确，校验过程中NF会使用到NRF侧配置的Token签名算法和公钥（校验对应NRF上的私钥）。

该命令用于配置NRF上的私钥信息，其对应的公钥信息在NF上通过ADD SBINRFKEY命令配置。NRF上配置的私钥信息生成时需给定密钥口令，用于保护私钥安全。

## 操作本对象的命令

- [[command/UNC/20.15.2/ACT-NRFKEY]] · ACT NRFKEY
- [[command/UNC/20.15.2/ADD-NRFKEY]] · ADD NRFKEY
- [[command/UNC/20.15.2/DEA-NRFKEY]] · DEA NRFKEY
- [[command/UNC/20.15.2/LST-NRFKEY]] · LST NRFKEY
- [[command/UNC/20.15.2/RMV-NRFKEY]] · RMV NRFKEY

## 证据

- 原始手册：`evidence/UNC/20.15.2/NRFKEY.md`
- 原始手册：`evidence/UNC/20.15.2/NRFKEY.md`
- 原始手册：`evidence/UNC/20.15.2/NRFKEY.md`
- 原始手册：`evidence/UNC/20.15.2/NRFKEY.md`
- 原始手册：`evidence/UNC/20.15.2/NRFKEY.md`
