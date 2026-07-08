---
id: UNC@20.15.2@MMLCommand@LST N2DTLSPARA
type: MMLCommand
name: LST N2DTLSPARA（查询N2接口的DTLS参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N2DTLSPARA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- N2接口DTLS安全管理
status: active
---

# LST N2DTLSPARA（查询N2接口的DTLS参数）

## 功能

**适用NF：AMF**

开启N2接口的DTLS连接时，需要配置详细的DTLS上下文参数，该命令用于查询N2接口DTLS连接参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| N2DTLSSWITCH | 是否开启N2DTLS | 可选必选说明：必选参数<br>参数含义：该参数用于指定N2接口DTLS是否开启。开启DTLS以后，新的gNodeB连接请求将会按照DTLS配置策略进行接入，已有连接不受影响。<br>数据来源：全网规划<br>取值范围：<br>- Yes<br>- No<br>默认值：No<br>配置原则： 无 |
| PEERCAPMATCH | 对端DTLS能力匹配策略 | 可选必选说明：必选参数<br>参数含义：该参数主要针对可能存在部分gNodeB不支持DTLS的情况。<br>数据来源：全网规划<br>取值范围：<br>- 安全优先：选择安全优先会直接拒绝不支持DTLS的gNodeB的连接请求。<br>- 业务优先：选择业务优先会进行兼容处理，对不支持DTLS的gNodeB允许接入，报文不进行DTLS安全加密传输，无法保证传输安全性；对于支持DTLS的gNodeB，按照DTLS的方式连接。建议根据全网gNodeB能力进行规划。<br>默认值：安全优先<br>配置原则： 无 |
| VERIFY | 是否验证对端证书 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否验证对端证书。<br>数据来源：全网规划<br>取值范围：<br>- Yes<br>- No<br>默认值：Yes<br>配置原则： 无 |
| VDEPTH | 校验深度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定校验深度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：10<br>配置原则： 无 |
| CIPHER | 加密套件集合 | 可选必选说明：可选参数<br>参数含义：该参数用于指定加密套件集合。<br>数据来源：全网规划<br>取值范围：位域类型，取值范围如下：<br>- 0x00_0x9E(TLS_DHE_RSA_WITH_AES_128_GCM_SHA256)<br>- 0x00_0x9F(TLS_DHE_RSA_WITH_AES_256_GCM_SHA384)<br>- 0x00_0xA2(TLS_DHE_DSS_WITH_AES_128_GCM_SHA256)<br>- 0x00_0xA3(TLS_DHE_DSS_WITH_AES_256_GCM_SHA384)<br>- 0xC0_0x2B(TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)<br>- 0xC0_0x2C(TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)<br>- 0xC0_0x2F(TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)<br>- 0xC0_0x30(TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)<br>- 0xC0_0x9E(TLS_DHE_RSA_WITH_AES_128_CCM)<br>- 0xC0_0x9F(TLS_DHE_RSA_WITH_AES_256_CCM)<br>- 0xC0_0xA2(TLS_DHE_RSA_WITH_AES_128_CCM_8)<br>- 0xC0_0xA3(TLS_DHE_RSA_WITH_AES_256_CCM_8)<br>- 0xC0_0xAC(TLS_ECDHE_ECDSA_WITH_AES_128_CCM)<br>- 0xC0_0xAD(TLS_ECDHE_ECDSA_WITH_AES_256_CCM)<br>- 0xC0_0xAE(TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8)<br>- 0xC0_0xAF(TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8)<br>默认值：全选中<br>配置原则： 无 |
| PROTOCAL | 协议版本 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定协议版本。<br>数据来源：全网规划<br>取值范围：位域类型，取值范围是Protocolver。<br>默认值：DTLS1_2<br>配置原则： 无 |
| AUTHTHUNKTYPE | SCTP数据块校验类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于DTLS启用时，指定SCTP数据块校验类型。<br>**若设置AUTHTHUNKTYPE中的COOKIE ECHO、COOKIE ACK、ECNE、CWR这四项必须要确保全网gNodeB均配置了该校验类型。**<br>若配置不一致，会导致与gNodeB链路连接失败，请谨慎操作。<br>数据来源：全网规划<br>取值范围：位域类型<br>- DATA<br>- SACK<br>- HEARTBEAT<br>- HEARTBEAT ACK<br>- ABORT<br>- SHUTDOWN<br>- SHUTDOWN ACK<br>- ERROR<br>- COOKIE ECHO<br>- COOKIE ACK<br>- ECNE<br>- CWR<br>默认值：除COOKIE ECHO、COOKIE ACK、ECNE、CWR这四项默认不校验，其余项默认校验<br>配置原则：无 |
| NESCENE | 设备证书使用场景名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定设备证书使用场景的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则： 无 |
| CASCENE | CA证书使用场景名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CA证书使用场景的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则： 无 |
| CRLFLAG | CRL是否开启 | 可选必选说明：必选参数<br>参数含义：该参数用于表示是否启用CRL。<br>数据来源：本端规划<br>取值范围：<br>- CRL_OFF（CRL不开启）<br>- CRL_ON（CRL开启）<br>默认值：CRL_OFF<br>配置原则： 无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定N2接口DTLS上下文描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则： 无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@N2DTLSPARA]] · N2接口的DTLS参数（N2DTLSPARA）

## 使用实例

若运营商要查询N2接口DTLS连接的相关配置信息，可以用如下命令：

```
%%LST N2DTLSPARA:;%%
RETCODE = 0  操作成功

操作结果如下
------------------------ 
                      是否开启N2DTLS  =  是
                对端DTLS能力匹配策略  =  安全优先
                    是否验证对端证书  =  是
                            校验深度  =  10
                        加密套件集合  =  DTLS_DHE_RSA_WITH_AES_128_GCM_SHA256
                            协议版本  =  传输层安全性协议版本v1.2
                  SCTP数据块校验类型  =  Abort&Payload Data&Operation Error&Heartbeat Request&Heartbeat Acknowledgement&Selective Acknowledgement&Shutdown&Shutdown Acknowledgement
                设备证书使用场景名称  =  NESCENE
                  CA证书使用场景名称  =  CASCENE
                         CRL是否开启  =  CRL不开启
                                描述  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-N2DTLSPARA.md`
