# 显示IKE安全联盟（DSP IKESA）

- [命令功能](#ZH-CN_MMLREF_0000001225912245__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001225912245__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001225912245__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001225912245__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001225912245__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001225912245)

该命令用于显示IKE安全联盟。

> **说明**
> - 该命令执行后立即生效。
> - 该命令在有大量智家随行业务的家庭网关在线时，如果查询全量的IKE安全联盟，可能存在链路过多查询失败的风险。
> - 由于用户级IPSEC链路只支持被动响应协商，查询结果中用户级链路的“剩余SA长度”字段为0。

#### [操作用户权限](#ZH-CN_MMLREF_0000001225912245)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001225912245)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REMOTEADDRESS | 远端地址 | 可选必选说明：可选参数<br>参数含义：IPsec策略远端地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| REMOTEADDRESS6 | 远端地址IPV6 | 可选必选说明：可选参数<br>参数含义：IPsec策略IPV6远端地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001225912245)

显示IKE安全联盟：

```
DSP IKESA:;
RETCODE = 0  操作成功

结果如下
--------
         地址类型  =  IPv4地址
         远端地址  =  10.1.1.2
     远端地址IPV6  =  ::
          POD名称  =  ipsecexec-pod-0192-168-1-1
           连接ID  =  46
           SA标记  =  RD|ST
           实例ID  =  46
             阶段  =  1
         本端地址  =  10.1.1.1
     本端地址IPV6  =  ::
     触发端Cookie  =  e3a8e1bb615e3e8c
     回应端Cookie  =  ba946bbfc7e3af8c
         接口名称  =  Tunnel37
         认证方法  =  预共享
         认证算法  =  sha2-256算法
         加密算法  =  256位AES算法
       完整性算法  =  sha2-256算法
             DH组  =  DH组14
       剩余SA长度  =  48267
       是否已备份  =  否
       SA建立时间  =  2021-12-22 09:08:45
    IKE对等体名称  =  env37_peer
          IKE版本  =  版本2
    流VPN实例名称  =  _public_
对等体VPN实例名称  =  _public_
              Ext  =  NULL
     发送消息计数  =  0
     接收消息计数  =  0
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001225912245)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 地址类型 | 用于表示地址类型。<br>取值说明：<br>- “AllIPv4（IPv4地址）”：IPv4地址<br>- “AllIPv6（IPv6地址）”：IPv6地址 |
| 远端地址 | IPsec策略远端地址。 |
| 远端地址IPV6 | IPsec策略IPV6远端地址。 |
| POD名称 | POD名称。 |
| 连接ID | IKE安全联盟的连接ID。 |
| SA标记 | 安全联盟标记字符串。<br>RD（READY）：表示此SA已建立成功。<br>ST（STAYALIVE）：表示此端是通道协商发起方。<br>RL（REPLACED）：标识此通道已经被新的通道代替，一段时间后将被删除。<br>FD（FADING）：表示此通道已发生过一次软超时，目前还在使用，如果发生硬超时则会删除此通道。<br>TO（TIMEOUT）：表示此SA在上次keepalive超时发生后还没有收到keepalive报文，如果在下次keepalive超时发生时仍没有收到keepalive报文，此SA将被删除。<br>NOSTATE：表示此SA初始建立但是尚未成功，一段时间还未建立成功将会被删除。 |
| 实例ID | 实例ID。 |
| 阶段 | 阶段。 |
| 本端地址 | IPsec策略本地地址。 |
| 本端地址IPV6 | IPsec策略IPV6本地地址。 |
| 触发端Cookie | 发起者的Cookie。 |
| 回应端Cookie | 响应者的Cookie。 |
| 接口名称 | 配置接口名。 |
| 认证方法 | 认证方法。<br>取值说明：<br>- “Pre_share（预共享）”：预共享密钥方式<br>- “Rsa_signature（RSA数字签名）”：RSA数字签名<br>- “Cert_signature（数字证书签名）”：数字证书签名<br>- “Digital_envelope（数字信封）”：数字信封 |
| 认证算法 | 认证算法。<br>取值说明：<br>- “Md5（Md5算法）”：Md5算法<br>- “Sha1（Sha1算法）”：Sha1算法<br>- “Sha2_256（Sha2-256算法）”：Sha2-256算法<br>- “Sha2_384（Sha2-384算法）”：Sha2-384算法<br>- “Sha2_512（Sha2-512算法）”：Sha2-512算法 |
| 加密算法 | 加密算法。<br>取值说明：<br>- “Des_cbc（DES算法）”：DES算法<br>- “Aes_cbc_128（128位AES算法）”：128位AES算法<br>- “Aes_cbc_192（192位AES算法）”：192位AES算法<br>- “Aes_cbc_256（256位AES算法）”：256位AES算法<br>- “Alg_3Des_cbc（3DES算法）”：3DES算法<br>- “Aes_gcm_128（128位AES-GCM算法）”：128位AES-GCM算法<br>- “Aes_gcm_256（256位AES-GCM算法）”：256位AES-GCM算法<br>- “Sm4（SM4算法）”：SM4算法 |
| 完整性算法 | 完整性算法。<br>取值说明：<br>- “Hmac_md5_96（Md5算法）”：Md5算法<br>- “Hmac_sha1_96（Sha1算法）”：Sha1算法<br>- “Hmac_sha2_256（Sha2-256算法）”：Sha2-256算法<br>- “Hmac_sha2_384（Sha2-384算法）”：Sha2-384算法<br>- “Aes_xcbc_96（Aes-xcbc-96算法）”：Aes-xcbc-96算法<br>- “Sm3（Sm3算法）”：Sm3算法<br>- “Hmac_sha2_512（Sha2-512算法）”：Sha2-512算法 |
| DH组 | DH组。<br>取值说明：<br>- None（无）<br>- “Dh_group1（DH组1）”：DH组1，不安全的DH组<br>- “Dh_group2（DH组2）”：DH组2，不安全的DH组<br>- “Dh_group5（DH组5）”：DH组5，不安全的DH组<br>- “Dh_group14（DH组14）”：DH组14，不安全的DH组<br>- “Dh_group19（DH组19）”：DH组19，推荐的安全DH组<br>- “Dh_group20（DH组20）”：DH组20，推荐的安全DH组<br>- “Dh_group31（DH组31）”：DH组31，推荐的安全DH组 |
| 剩余SA长度 | 剩余的安全联盟的有效时间。 |
| 是否已备份 | 是否备份的标记。<br>取值说明：<br>- TRUE(TRUE)<br>- FALSE(FALSE) |
| SA建立时间 | 安全联盟的建立时间。 |
| IKE对等体名称 | IKE对端名字。 |
| IKE版本 | IKE版本号。<br>取值说明：<br>- “V1（版本1）”：版本1<br>- “V2（版本2）”：版本2<br>- “V1V2（版本1、2）”：版本1、2 |
| 流VPN实例名称 | 流VPN。 |
| 对等体VPN实例名称 | 对端VPN。 |
| Ext | 扩展字段。 |
| 发送消息计数 | 发送消息个数。 |
| 接收消息计数 | 接收消息个数。 |
| 非对称加密算法 | 非对称加密算法。<br>取值说明：<br>- “NULL（空）”：空<br>- “Sm2（Sm2算法）”：Sm2算法 |
