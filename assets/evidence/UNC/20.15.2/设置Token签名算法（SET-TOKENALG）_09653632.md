# 设置Token签名算法（SET TOKENALG）

- [命令功能](#ZH-CN_MMLREF_0209653632__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653632__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653632__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653632__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209653632)

**适用NF：NRF**

NF服务消费者获取到Token后，携带Token访问NF服务提供方的服务。NF服务提供方会对NF服务消费者进行认证，校验Token是否正确，校验过程中NF会使用到公钥和NRF侧配置的Token签名算法。

此命令用于设置NRF上Token的签名算法。

## [注意事项](#ZH-CN_MMLREF_0209653632)

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ALGNAME |
| --- |
| RS256 |

#### [操作用户权限](#ZH-CN_MMLREF_0209653632)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653632)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALGNAME | 算法 | 可选必选说明：必选参数<br>参数含义：该参数用于表示Token的签名算法。<br>数据来源：全网规划<br>取值范围：<br>- “RS256（RS256）”：RSASSA-PKCS1-v1_5 using SHA-256<br>- “RS384（RS384）”：RSASSA-PKCS1-v1_5 using SHA-384<br>- “RS512（RS512）”：RSASSA-PKCS1-v1_5 using SHA-512<br>- “ES256（ES256）”：ECDSA using P-256 and SHA-256<br>- “ES384（ES384）”：ECDSA using P-384 and SHA-384<br>- “ES512（ES512）”：ECDSA using P-512 and SHA-512<br>- “PS256（PS256）”：RSASSA-PSS using SHA-256 and MGFI with SHA-256<br>- “PS384（PS384）”：RSASSA-PSS using SHA-384 and MGFI with SHA-384<br>- “PS512（PS512）”：RSASSA-PSS using SHA-512 and MGFI with SHA-512<br>默认值：无。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653632)

设置NRF上的Token签名算法为RS384：

```
SET TOKENALG:ALGNAME=RS384;
```
