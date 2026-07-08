---
id: UNC@20.15.2@MMLCommand@LST TLSPARA
type: MMLCommand
name: LST TLSPARA（查询TLS参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TLSPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP TLS安全管理
status: active
---

# LST TLSPARA（查询TLS参数）

## 功能

开启服务化接口的TLS协议时，需要配置详细的TLS上下文参数，该命令用于查询一组TLS参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TLS参数索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：<br>与<br>[**ADD HTTPLE**](../../HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)<br>中配置的TLS参数索引保持一致。 |

## 操作的配置对象

- [TLS参数（TLSPARA）](configobject/UNC/20.15.2/TLSPARA.md)

## 使用实例

- 若运营商想查询索引为1的TLS参数配置信息，可以用如下命令；
  ```
  %%LST TLSPARA: INDEX=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
              索引  =  1
          HTTP模式  =  服务端模式
  是否验证对端证书  =  开启校验对端证书
          校验深度  =  0
          协议版本  =  传输层安全性协议版本v1.2&传输层安全性协议版本v1.3
      加密套件集合  =  TLS_DHE_RSA_WITH_AES_128_GCM_SHA256&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_RSA_WITH_AES_128_CCM&TLS_DHE_RSA_WITH_AES_256_CCM&TLS_DHE_RSA_WITH_AES_128_CCM_8&TLS_DHE_RSA_WITH_AES_256_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_128_CCM&TLS_ECDHE_ECDSA_WITH_AES_256_CCM&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8&TLS_AES_128_GCM_SHA256&TLS_AES_256_GCM_SHA384&TLS_CHACHA20_POLY1305_SHA256
        CA证书场景  =  2
      设备证书场景  =  1
       CRL是否开启  =  开启吊销证书列表
              描述  =  NULL
      域名校验开关  =  关闭校验对端证书
        IP校验开关  =  关闭校验对端证书
       SNI校验开关  =  关闭SNI校验
          认证模式  =  证书认证
  预共享密钥组索引  =  0
    域名校验全匹配  =  关闭域名检验全匹配
  (结果个数 = 1)

  ---    END
  ```
- 若运营商想查询所有的TLS参数配置信息，可以用如下命令；
  ```
  %%LST TLSPARA:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  索引  HTTP模式    是否验证对端证书  校验深度  协议版本                                           加密套件集合                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            CA证书场景  设备证书场景  CRL是否开启       描述  域名校验开关      IP校验开关        SNI校验开关  认证模式  预共享密钥组索引  域名校验全匹配      

  1     服务端模式  开启校验对端证书  0         传输层安全性协议版本v1.2&传输层安全性协议版本v1.3  TLS_DHE_RSA_WITH_AES_128_GCM_SHA256&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_RSA_WITH_AES_128_CCM&TLS_DHE_RSA_WITH_AES_256_CCM&TLS_DHE_RSA_WITH_AES_128_CCM_8&TLS_DHE_RSA_WITH_AES_256_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_128_CCM&TLS_ECDHE_ECDSA_WITH_AES_256_CCM&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8&TLS_AES_128_GCM_SHA256&TLS_AES_256_GCM_SHA384&TLS_CHACHA20_POLY1305_SHA256  2           1             开启吊销证书列表  NULL  关闭校验对端证书  关闭校验对端证书  关闭SNI校验  证书认证  0                 关闭域名检验全匹配  
  2     客户端模式  开启校验对端证书  0         传输层安全性协议版本v1.2&传输层安全性协议版本v1.3  TLS_DHE_RSA_WITH_AES_128_GCM_SHA256&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_RSA_WITH_AES_128_CCM&TLS_DHE_RSA_WITH_AES_256_CCM&TLS_DHE_RSA_WITH_AES_128_CCM_8&TLS_DHE_RSA_WITH_AES_256_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_128_CCM&TLS_ECDHE_ECDSA_WITH_AES_256_CCM&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8&TLS_AES_128_GCM_SHA256&TLS_AES_256_GCM_SHA384&TLS_CHACHA20_POLY1305_SHA256  2           1             开启吊销证书列表  NULL  关闭校验对端证书  关闭校验对端证书  关闭SNI校验  证书认证  0                 关闭域名检验全匹配  
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询TLS参数（LST-TLSPARA）_84132104.md`
