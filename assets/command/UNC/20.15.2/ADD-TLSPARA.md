---
id: UNC@20.15.2@MMLCommand@ADD TLSPARA
type: MMLCommand
name: ADD TLSPARA（增加TLS参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TLSPARA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP TLS安全管理
status: active
---

# ADD TLSPARA（增加TLS参数）

## 功能

![](增加TLS参数（ADD TLSPARA）_84132096.assets/notice_3.0-zh-cn_2.png)

该命令中CIPHER参数用于选择安全算法，DHE相关的算法性能较差，在大量建链场景下会导致本端CPU占用过高以及长时间无法建链的问题，请谨慎使用，建议选择ECDHE算法。

开启服务化接口的TLS协议时，需要配置详细的TLS上下文参数，该命令用于增加一组TLS参数。

## 注意事项

- 该命令执行后立即生效。

- 增加TLS参数前，如果采用证书的认证方式，需要先通过[**ADD TLSSCENE**](../HTTP TLS证书场景管理/增加TLS证书场景（ADD TLSSCENE）_29213279.md)增加证书使用场景；如果采用预共享密钥的认证方式，需要先通过命令[**ADD TLSPSKGRP**](../HTTP TLS预共享密钥组管理/增加TLS预共享密钥组（ADD TLSPSKGRP）_07789673.md)增加使用的预共享密钥组，再通过[**ADD TLSPSK**](../HTTP TLS预共享密钥管理/增加预共享密钥（ADD TLSPSK）_07669721.md)命令增加使用的预共享密钥信息。
- 如果选择了TLS1.2版本，则TLS1.2加密套件中需要选择至少一个，否则此命令会执行失败。TLS1.2加密套件包括：TLS_DHE_RSA_WITH_AES_128_GCM_SHA256、TLS_DHE_RSA_WITH_AES_256_GCM_SHA384、TLS_DHE_DSS_WITH_AES_128_GCM_SHA256、TLS_DHE_DSS_WITH_AES_256_GCM_SHA384、TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256、TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384、TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256、TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384、TLS_DHE_RSA_WITH_AES_128_CCM、TLS_DHE_RSA_WITH_AES_256_CCM、TLS_DHE_RSA_WITH_AES_128_CCM_8、TLS_DHE_RSA_WITH_AES_256_CCM_8、TLS_ECDHE_ECDSA_WITH_AES_128_CCM、TLS_ECDHE_ECDSA_WITH_AES_256_CCM、TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8、TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8。
- 如果选择了TLS1.3版本，则TLS_AES_128_GCM_SHA256、TLS_AES_256_GCM_SHA384、TLS_CHACHA20_POLY1305_SHA256三个加密套件需要同时选择或者不选。如果需要单独勾选，需要执行MML命令[**SET FWSOFTPARABITS**](../../../../操作维护/软参配置管理/设置软件参数比特位（SET FWSOFTPARABITS）_37580503.md)，将软参DWORD1612 BIT2设置为1。
- 如果选择了TLS1.3版本，且预期是不使用TLS_AES_128_CCM_SHA256和TLS_AES_128_CCM_8_SHA256算法套，则不勾选这两个算法套的同时，需要执行MML命令[**SET FWSOFTPARABITS**](../../../../操作维护/软参配置管理/设置软件参数比特位（SET FWSOFTPARABITS）_37580503.md)，将软件参数DWORD1612 BIT1设置为0。
- 如果选择了TLS1.3版本，但未选择任何TLS1.3版本的加密套件，则建链时会将三个默认的加密套件（TLS_AES_128_GCM_SHA256、TLS_AES_256_GCM_SHA384、TLS_CHACHA20_POLY1305_SHA256）加入到加密套件集合进行TLS握手。
- 增加TLS参数后开始业务前，如果采用证书的认证方式，需要确认TLS参数使用的证书场景已经关联了对应的CA证书和设备证书。若没有关联，会导致TLS链路建立失败。

- 最多可输入128条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TLS参数索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：<br>与<br>[**ADD HTTPLE**](../../HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)<br>中配置的TLS参数索引保持一致。 |
| MODE | HTTP模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定开启服务化接口的TLS协议时的HTTP模式，HTTP模式指客户端模式或服务端模式的区分。<br>数据来源：全网规划<br>取值范围：<br>- “Client（客户端模式）”：Client指的是客户端模式<br>- “Server（服务端模式）”：Server指的是服务端模式<br>默认值：无<br>配置原则：无 |
| AUTHMODE | 认证模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定身份认证方式。<br>数据来源：全网规划<br>取值范围：<br>- “CERT（证书认证）”：采用证书方式进行认证<br>- “PSK（预共享密钥）”：采用预共享密钥方式进行认证<br>默认值：CERT<br>配置原则：无 |
| VERIFY | 是否验证对端证书 | 可选必选说明：该参数在"AUTHMODE"配置为"CERT"时为条件必选参数。<br>参数含义：该参数用于指定是否验证对端证书。<br>数据来源：全网规划<br>取值范围：<br>- “Yes（开启校验对端证书）”：开启校验对端证书<br>- “No（关闭校验对端证书）”：关闭校验对端证书<br>默认值：无<br>配置原则：<br>客户端模式，当参数设置为“No”时，不校验服务端证书，存在安全风险，请谨慎设置。 |
| VERIFYCN | 域名校验开关 | 可选必选说明：该参数在"VERIFY"配置为"Yes"时为条件可选参数。<br>参数含义：该参数用于指定在证书校验阶段是否校验对端域名。开启域名校验时，将校验对端证书中的域名与实际域名是否一致，如果不一致则HTTPS建链失败。<br>数据来源：全网规划<br>取值范围：<br>- “Yes（开启校验对端证书）”：开启校验对端证书<br>- “No（关闭校验对端证书）”：关闭校验对端证书<br>默认值：无<br>配置原则：<br>证书中的域名应当与网络规划的域名保持一致，否则TLS握手会失败。为提升证书认证的安全性，可以开启域名校验功能，以防仿冒攻击。仅当参数“HTTP模式”配置为Client时生效，若配置为Server则无实际效果。 |
| VERIFYIP | IP校验开关 | 可选必选说明：该参数在"VERIFY"配置为"Yes"时为条件可选参数。<br>参数含义：该参数用于指定在证书校验阶段是否校验对端IP地址。开启IP校验后，将校验对端证书中的IP地址与实际IP地址是否一致，如果不一致则HTTPS建链失败。<br>数据来源：全网规划<br>取值范围：<br>- “Yes（开启校验对端证书）”：开启校验对端证书<br>- “No（关闭校验对端证书）”：关闭校验对端证书<br>默认值：无<br>配置原则：<br>证书中的IP地址应当与网络规划的IP地址保持一致，否则TLS握手会失败。为提升证书认证的安全性，可以开启IP地址校验功能，以防仿冒攻击。仅当参数“HTTP模式”配置为Client时生效，若配置为Server则无实际效果。 |
| VERIFYSNI | SNI校验开关 | 可选必选说明：该参数在"VERIFY"配置为"Yes"时为条件可选参数。<br>参数含义：该参数用于控制是否使用SNI验证证书中的域名。如果开启了该功能，当使用SNI匹配证书的域名失败后，建链失败。<br>数据来源：全网规划<br>取值范围：<br>- “Yes（开启SNI校验）”：开启校验SNI<br>- “No（关闭SNI校验）”：关闭校验SNI<br>默认值：无<br>配置原则：<br>证书中的域名应当与client-hello中的SNI保持一致。为提升证书认证的安全性，可以开启SNI校验功能，以防仿冒攻击。仅当参数“HTTP模式”配置为Server时生效，若配置为Client则无实际效果。如果服务端期望使用此参数，则需要客户端TLS握手消息携带SNI才有效，否则服务端会随机选择一个证书进行TLS握手。 |
| VDEPTH | 校验深度 | 可选必选说明：该参数在"AUTHMODE"配置为"CERT"时为条件可选参数。<br>参数含义：该参数用于指定校验深度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| CIPHER | 加密套件集合 | 可选必选说明：必选参数<br>参数含义：该参数用于指定加密套件集合。<br>数据来源：全网规划<br>取值范围：取值为枚举值<br>- “TLS_DHE_RSA_WITH_AES_128_GCM_SHA256（TLS_DHE_RSA_WITH_AES_128_GCM_SHA256）”：使用TLS_DHE_RSA_WITH_AES_128_GCM_SHA256加密算法的加密套件<br>- “TLS_DHE_RSA_WITH_AES_256_GCM_SHA384（TLS_DHE_RSA_WITH_AES_256_GCM_SHA384）”：使用TLS_DHE_RSA_WITH_AES_256_GCM_SHA384加密算法的加密套件<br>- “TLS_DHE_DSS_WITH_AES_128_GCM_SHA256（TLS_DHE_DSS_WITH_AES_128_GCM_SHA256）”：使用TLS_DHE_DSS_WITH_AES_128_GCM_SHA256加密算法的加密套件<br>- “TLS_DHE_DSS_WITH_AES_256_GCM_SHA384（TLS_DHE_DSS_WITH_AES_256_GCM_SHA384）”：使用TLS_DHE_DSS_WITH_AES_256_GCM_SHA384加密算法的加密套件<br>- “TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256（TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256）”：使用TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256机密算法的加密套件<br>- “TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384（TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384）”：使用TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384加密算法的加密套件<br>- “TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256（TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256）”：使用TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256加密算法的加密套件<br>- “TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384（TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384）”：使用TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384加密算法的加密套件<br>- “TLS_DHE_RSA_WITH_AES_128_CCM（TLS_DHE_RSA_WITH_AES_128_CCM）”：使用TLS_DHE_RSA_WITH_AES_128_CCM加密算法的加密套件<br>- “TLS_DHE_RSA_WITH_AES_256_CCM（TLS_DHE_RSA_WITH_AES_256_CCM）”：使用TLS_DHE_RSA_WITH_AES_256_CCM加密算法的加密套件<br>- “TLS_DHE_RSA_WITH_AES_128_CCM_8（TLS_DHE_RSA_WITH_AES_128_CCM_8）”：使用TLS_DHE_RSA_WITH_AES_128_CCM_8加密算法的加密套件（不安全算法）<br>- “TLS_DHE_RSA_WITH_AES_256_CCM_8（TLS_DHE_RSA_WITH_AES_256_CCM_8）”：使用TLS_DHE_RSA_WITH_AES_256_CCM_8加密算法的加密套件（不安全算法）<br>- “TLS_ECDHE_ECDSA_WITH_AES_128_CCM（TLS_ECDHE_ECDSA_WITH_AES_128_CCM）”：使用TLS_ECDHE_ECDSA_WITH_AES_128_CCM加密算法的加密套件<br>- “TLS_ECDHE_ECDSA_WITH_AES_256_CCM（TLS_ECDHE_ECDSA_WITH_AES_256_CCM）”：使用TLS_ECDHE_ECDSA_WITH_AES_256_CCM加密算法的加密套件<br>- “TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8（TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8）”：使用TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8加密算法的加密套件（不安全算法）<br>- “TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8（TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8）”：使用TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8加密算法的加密套件（不安全算法）<br>- “TLS_AES_128_GCM_SHA256（TLS_AES_128_GCM_SHA256）”：使用TLS_AES_128_GCM_SHA256加密算法的加密套件<br>- “TLS_AES_256_GCM_SHA384（TLS_AES_256_GCM_SHA384）”：使用TLS_AES_256_GCM_SHA384加密算法的加密套件<br>- “TLS_CHACHA20_POLY1305_SHA256（TLS_CHACHA20_POLY1305_SHA256）”：使用TLS_CHACHA20_POLY1305_SHA256加密算法的加密套件<br>- “TLS_AES_128_CCM_SHA256（TLS_AES_128_CCM_SHA256）”：使用TLS_AES_128_CCM_SHA256加密算法的加密套件<br>- “TLS_AES_128_CCM_8_SHA256（TLS_AES_128_CCM_8_SHA256）”：使用TLS_AES_128_CCM_8_SHA256加密算法的加密套件（不安全算法）<br>- “TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256（TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256）”：使用TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256加密算法的加密套件<br>- “TLS_DHE_PSK_WITH_AES_128_GCM_SHA256（TLS_DHE_PSK_WITH_AES_128_GCM_SHA256）”：使用TLS_DHE_PSK_WITH_AES_128_GCM_SHA256加密算法的加密套件<br>- “TLS_DHE_PSK_WITH_AES_256_GCM_SHA384（TLS_DHE_PSK_WITH_AES_256_GCM_SHA384）”：使用TLS_DHE_PSK_WITH_AES_256_GCM_SHA384加密算法的加密套件<br>- “TLS_DHE_PSK_WITH_CHACHA20_POLY1305_SHA256（TLS_DHE_PSK_WITH_CHACHA20_POLY1305_SHA256）”：使用TLS_DHE_PSK_WITH_CHACHA20_POLY1305_SHA256加密算法的加密套件<br>- “TLS_DHE_PSK_WITH_AES_128_CCM（TLS_DHE_PSK_WITH_AES_128_CCM）”：使用TLS_DHE_PSK_WITH_AES_128_CCM加密算法的加密套件<br>- “TLS_DHE_PSK_WITH_AES_256_CCM（TLS_DHE_PSK_WITH_AES_256_CCM）”：使用TLS_DHE_PSK_WITH_AES_256_CCM加密算法的加密套件<br>- “TLS_PSK_WITH_AES_256_GCM_SHA384（TLS_PSK_WITH_AES_256_GCM_SHA384）”：使用TLS_PSK_WITH_AES_256_GCM_SHA384加密算法的加密套件<br>- “TLS_PSK_WITH_AES_256_CCM（TLS_PSK_WITH_AES_256_CCM）”：使用TLS_PSK_WITH_AES_256_CCM加密算法的加密套件<br>默认值：无<br>配置原则：无 |
| PROTOCAL | 协议版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定协议版本。<br>数据来源：全网规划<br>取值范围：<br>- “TLS1_2（传输层安全性协议版本v1.2）”：TLS1_2表示使用传输层安全性协议版本v1.2<br>- “TLS1_3（传输层安全性协议版本v1.3）”：TLS1_3表示使用传输层安全性协议版本v1.3<br>默认值：无<br>配置原则：无 |
| NESCENE | 设备证书场景 | 可选必选说明：该参数在"AUTHMODE"配置为"CERT"时为条件必选参数。<br>参数含义：该参数用于设备证书场景。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~254。<br>默认值：无<br>配置原则：<br>与<br>[**ADD TLSSCENE**](../HTTP TLS证书场景管理/增加TLS证书场景（ADD TLSSCENE）_29213279.md)<br>中配置的设备证书场景的索引保持一致，255为无效值。 |
| CASCENE | CA证书场景 | 可选必选说明：该参数在"AUTHMODE"配置为"CERT"时为条件必选参数。<br>参数含义：该参数用于CA证书场景。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~254。<br>默认值：无<br>配置原则：<br>与<br>[**ADD TLSSCENE**](../HTTP TLS证书场景管理/增加TLS证书场景（ADD TLSSCENE）_29213279.md)<br>中配置的CA证书场景的索引保持一致。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TLS上下文描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| CRLFLAG | CRL是否开启 | 可选必选说明：该参数在"AUTHMODE"配置为"CERT"时为条件必选参数。<br>参数含义：该参数用于指定开启服务化接口的TLS协议时是否开启吊销证书列表。<br>数据来源：本端规划<br>取值范围：<br>- “CRL_OFF（关闭吊销证书列表）”：关闭吊销证书列表<br>- “CRL_ON（开启吊销证书列表）”：开启吊销证书列表<br>默认值：无<br>配置原则：<br>若启用CRL，即吊销证书列表，则需上传CRL文件。 |
| PSKGRPIDX | 预共享密钥组索引 | 可选必选说明：该参数在"AUTHMODE"配置为"PSK"时为条件必选参数。<br>参数含义：在身份认证模式为预共享密钥时，该参数用于指定关联的预共享密钥组索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：<br>与<br>[**ADD TLSPSKGRP**](../HTTP TLS预共享密钥组管理/增加TLS预共享密钥组（ADD TLSPSKGRP）_07789673.md)<br>中配置的预共享密钥组索引保持一致。 |
| VERIFYCNFULL | 域名校验全匹配 | 可选必选说明：该参数在"VERIFYCN"配置为"Yes"时为条件可选参数。<br>参数含义：该参数用于指定检验证书域名时是否全匹配。<br>数据来源：本端规划<br>取值范围：<br>- “YES（开启域名校验全匹配）”：开启对端证书域名检验全匹配<br>- “NO（关闭域名检验全匹配）”：关闭对端证书域名检验全匹配<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TLSPARA]] · TLS参数（TLSPARA）

## 使用实例

- 若运营商想配置一条TLS上下文参数，索引是1，模式是服务端，不验证对端证书等其他属性，可以用如下命令：
  ```
  ADD TLSPARA: INDEX=1, MODE=Server, AUTHMODE=CERT, VERIFY=No, CIPHER=TLS_DHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256-1&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_RSA_WITH_AES_128_CCM-1&TLS_DHE_RSA_WITH_AES_256_CCM-1&TLS_DHE_RSA_WITH_AES_128_CCM_8-1&TLS_DHE_RSA_WITH_AES_256_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8-1&TLS_AES_128_GCM_SHA256-1&TLS_AES_256_GCM_SHA384-1&TLS_CHACHA20_POLY1305_SHA256-1&TLS_AES_128_CCM_SHA256-1&TLS_AES_128_CCM_8_SHA256-1&TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256-1&TLS_DHE_PSK_WITH_AES_128_GCM_SHA256-1&TLS_DHE_PSK_WITH_AES_256_GCM_SHA384-1&TLS_DHE_PSK_WITH_CHACHA20_POLY1305_SHA256-1&TLS_DHE_PSK_WITH_AES_128_CCM-1&TLS_DHE_PSK_WITH_AES_256_CCM-1, PROTOCAL=TLS1_2-1&TLS1_3-1, NESCENE=2, CASCENE=1, CRLFLAG=CRL_OFF;
  ```
- 若运营商向配置一条TLS上下文参数，索引是2，模式是服务端，使用预共享密钥认证方式，可以使用如下命令：
  ```
  ADD TLSPARA: INDEX=2, MODE=Server, AUTHMODE=PSK, CIPHER=TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256-1&TLS_DHE_PSK_WITH_AES_128_GCM_SHA256-1&TLS_DHE_PSK_WITH_AES_256_GCM_SHA384-1&TLS_DHE_PSK_WITH_CHACHA20_POLY1305_SHA256-1&TLS_DHE_PSK_WITH_AES_128_CCM-1&TLS_DHE_PSK_WITH_AES_256_CCM-1, PROTOCAL=TLS1_2-1, PSKGRPIDX=1;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-TLSPARA.md`
