---
id: UNC@20.15.2@MMLCommand@ADD NRFKEY
type: MMLCommand
name: ADD NRFKEY（增加NRF密钥）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFKEY
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 授权管理
- 密钥管理
status: active
---

# ADD NRFKEY（增加NRF密钥）

## 功能

![](增加NRF密钥（ADD NRFKEY）_09651563.assets/notice_3.0-zh-cn_2.png)

请注意TOKEN签名算法时私钥的长度设置，以确保密钥的安全性。当TOKEN签名算法为RSA类型时，建议原始私钥长度不小于3072bit；当TOKEN签名算法配置为ECC类型时，建议原始私钥长度不小于256bit。若配置的密钥算法对应的长度不满足要求，则密钥算法可能会被攻击破解，导致私钥泄露。

**适用NF：NRF**

NF服务消费者获取到Token后，携带Token访问NF服务提供方的服务。NF服务提供方会对NF服务消费者进行认证，校验Token是否正确，校验过程中NF会使用到NRF侧配置的Token签名算法和公钥（校验对应NRF上的私钥）。

该命令用于配置NRF上的私钥信息，其对应的公钥信息在NF上通过ADD SBINRFKEY命令配置。NRF上配置的私钥信息生成时需给定密钥口令，用于保护私钥安全。

## 注意事项

- 该命令执行后立即生效。

- 系统只使用其中一条记录。
- 私钥生成算法要求和TOKEN签名算法保持一致。
- 当TOKEN签名算法为RSA（RS256，RS384，RS512，PS256，PS384，PS512）时，建议原始私钥长度大于等于3072bit；当TOKEN签名算法配置为ECC（ES256，ES384，ES512）时，建议原始私钥长度大于等于256bit。
- 私钥加密算法采用CBC模式的AES算法（密钥长度大于等于128bit）。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。
- NRFKEY不支持MOD命令，如需修改NRFKEY中NRFKEYID，请参考5G Core NRF解决方案中NRF解决方案安全配置实例（NRF容灾+NF访问授权&NF认证）章节的相关说明

- 最多可输入5条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYNAME | 密钥名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示在NRF上配置的密钥名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |
| KEYINFO | 密钥密文 | 可选必选说明：必选参数<br>参数含义：为保证安全，NRF上提供的密钥是加密的。该参数用于表示在NRF上配置的密钥密文，即密钥信息加密后的密文。<br>数据来源：全网规划<br>取值范围：Pwd，取值范围是0~4096。<br>默认值：无<br>配置原则：无 |
| AUTHPWD | 密钥口令 | 可选必选说明：必选参数<br>参数含义：该参数表示NRF上配置的密钥密文的解密口令，用于解密加密后的密文信息。运营商需依据加密协议生成密钥密文，生成时需要指定密钥口令，用于保护私钥，防止未经授权时访问私钥。<br>数据来源：本端规划<br>取值范围：Pwd，取值范围是8~16。<br>默认值：无<br>配置原则：<br>私钥的加密口令建议满足如下复杂度要求：至少包含一个小写字母、一个大写字母、一个数字和一个特殊字符。 |
| NRFKEYIDSW | NRF密钥ID开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制Token申请响应报文中生成的accessToken是否包含NRFKEYID。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无<br>配置原则：无 |
| NRFKEYID | NRF密钥ID | 可选必选说明：该参数在"NRFKEYIDSW"配置为"FUNC_ON"时为条件必选参数。<br>参数含义：该参数表示NRF上配置的密钥ID，用于标识同一NRF分配的不同Token。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：<br>NRFKEYID不能重复。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFKEY]] · NRF密钥（NRFKEY）

## 使用实例

新增NRF密钥：

```
ADD NRFKEY: KEYNAME="keyname001", KEYINFO="*****", AUTHPWD="*****",NRFKEYIDSW=FUNC_ON,NRFKEYID="nrfkid1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NRFKEY.md`
