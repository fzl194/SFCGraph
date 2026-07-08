---
id: UDG@20.15.2@ConfigObject@TLSPARA
type: ConfigObject
name: TLSPARA（TLS参数）
nf: UDG
version: 20.15.2
object_name: TLSPARA
object_kind: entity
status: active
---

# TLSPARA（TLS参数）

## 说明

![](增加TLS参数（ADD TLSPARA）_84132096.assets/notice_3.0-zh-cn.png)

该命令中CIPHER参数用于选择安全算法，DHE相关的算法性能较差，在大量建链场景下会导致本端CPU占用过高以及长时间无法建链的问题，请谨慎使用，建议选择ECDHE算法。

开启服务化接口的TLS协议时，需要配置详细的TLS上下文参数，该命令用于增加一组TLS参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 增加TLS参数前，如果采用证书的认证方式，需要先通过[**ADD TLSSCENE**](../HTTP TLS证书场景管理/增加TLS证书场景（ADD TLSSCENE）_29213279.md)增加证书使用场景；如果采用预共享密钥的认证方式，需要先通过命令[**ADD TLSPSKGRP**](../HTTP TLS预共享密钥组管理/增加TLS预共享密钥组（ADD TLSPSKGRP）_07789673.md)增加使用的预共享密钥组，再通过[**ADD TLSPSK**](../HTTP TLS预共享密钥管理/增加预共享密钥（ADD TLSPSK）_07669721.md)命令增加使用的预共享密钥信息。
> - 如果选择了TLS1.2版本，则TLS1.2加密套件中需要选择至少一个，否则此命令会执行失败。TLS1.2加密套件包括：TLS_DHE_RSA_WITH_AES_128_GCM_SHA256、TLS_DHE_RSA_WITH_AES_256_GCM_SHA384、TLS_DHE_DSS_WITH_AES_128_GCM_SHA256、TLS_DHE_DSS_WITH_AES_256_GCM_SHA384、TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256、TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384、TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256、TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384、TLS_DHE_RSA_WITH_AES_128_CCM、TLS_DHE_RSA_WITH_AES_256_CCM、TLS_DHE_RSA_WITH_AES_128_CCM_8、TLS_DHE_RSA_WITH_AES_256_CCM_8、TLS_ECDHE_ECDSA_WITH_AES_128_CCM、TLS_ECDHE_ECDSA_WITH_AES_256_CCM、TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8、TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8。
> - 如果选择了TLS1.3版本，则TLS_AES_128_GCM_SHA256、TLS_AES_256_GCM_SHA384、TLS_CHACHA20_POLY1305_SHA256三个加密套件需要同时选择或者不选。如果需要单独勾选，需要执行MML命令[**SET FWSOFTPARABITS**](../../../../操作维护/软参配置管理/设置软件参数比特位（SET FWSOFTPARABITS）_37580503.md)，将软参DWORD1612 BIT2设置为1。
> - 如果选择了TLS1.3版本，且预期是不使用TLS_AES_128_CCM_SHA256和TLS_AES_128_CCM_8_SHA256算法套，则不勾选这两个算法套的同时，需要执行MML命令[**SET FWSOFTPARABITS**](../../../../操作维护/软参配置管理/设置软件参数比特位（SET FWSOFTPARABITS）_37580503.md)，将软件参数DWORD1612 BIT1设置为0。
> - 如果选择了TLS1.3版本，但未选择任何TLS1.3版本的加密套件，则建链时会将三个默认的加密套件（TLS_AES_128_GCM_SHA256、TLS_AES_256_GCM_SHA384、TLS_CHACHA20_POLY1305_SHA256）加入到加密套件集合进行TLS握手。
> - 增加TLS参数后开始业务前，如果采用证书的认证方式，需要确认TLS参数使用的证书场景已经关联了对应的CA证书和设备证书。若没有关联，会导致TLS链路建立失败。
>
> - 最多可输入128条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-TLSPARA]] · ADD TLSPARA
- [[command/UDG/20.15.2/LST-TLSPARA]] · LST TLSPARA
- [[command/UDG/20.15.2/MOD-TLSPARA]] · MOD TLSPARA
- [[command/UDG/20.15.2/RMV-TLSPARA]] · RMV TLSPARA

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改TLS参数（MOD-TLSPARA）_83972192.md`
- 原始手册：`evidence/UDG/20.15.2/删除TLS参数（RMV-TLSPARA）_28971849.md`
- 原始手册：`evidence/UDG/20.15.2/增加TLS参数（ADD-TLSPARA）_84132096.md`
- 原始手册：`evidence/UDG/20.15.2/查询TLS参数（LST-TLSPARA）_84132104.md`
