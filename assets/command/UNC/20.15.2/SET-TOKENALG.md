---
id: UNC@20.15.2@MMLCommand@SET TOKENALG
type: MMLCommand
name: SET TOKENALG（设置Token签名算法）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: TOKENALG
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 授权管理
- Token管理
- Token算法管理
status: active
---

# SET TOKENALG（设置Token签名算法）

## 功能

**适用NF：NRF**

NF服务消费者获取到Token后，携带Token访问NF服务提供方的服务。NF服务提供方会对NF服务消费者进行认证，校验Token是否正确，校验过程中NF会使用到公钥和NRF侧配置的Token签名算法。

此命令用于设置NRF上Token的签名算法。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ALGNAME |
| --- |
| RS256 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALGNAME | 算法 | 可选必选说明：必选参数<br>参数含义：该参数用于表示Token的签名算法。<br>数据来源：全网规划<br>取值范围：<br>- “RS256（RS256）”：RSASSA-PKCS1-v1_5 using SHA-256<br>- “RS384（RS384）”：RSASSA-PKCS1-v1_5 using SHA-384<br>- “RS512（RS512）”：RSASSA-PKCS1-v1_5 using SHA-512<br>- “ES256（ES256）”：ECDSA using P-256 and SHA-256<br>- “ES384（ES384）”：ECDSA using P-384 and SHA-384<br>- “ES512（ES512）”：ECDSA using P-512 and SHA-512<br>- “PS256（PS256）”：RSASSA-PSS using SHA-256 and MGFI with SHA-256<br>- “PS384（PS384）”：RSASSA-PSS using SHA-384 and MGFI with SHA-384<br>- “PS512（PS512）”：RSASSA-PSS using SHA-512 and MGFI with SHA-512<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TOKENALG]] · Token签名算法（TOKENALG）

## 使用实例

设置NRF上的Token签名算法为RS384：

```
SET TOKENALG:ALGNAME=RS384;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置Token签名算法（SET-TOKENALG）_09653632.md`
