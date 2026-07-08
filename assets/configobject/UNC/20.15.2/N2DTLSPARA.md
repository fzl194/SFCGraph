---
id: UNC@20.15.2@ConfigObject@N2DTLSPARA
type: ConfigObject
name: N2DTLSPARA（N2接口的DTLS参数）
nf: UNC
version: 20.15.2
object_name: N2DTLSPARA
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# N2DTLSPARA（N2接口的DTLS参数）

## 说明

![](设置N2接口的DTLS参数(SET N2DTLSPARA)_54302474.assets/notice_3.0-zh-cn_2.png)

若设置AUTHTHUNKTYPE中的COOKIE ECHO、COOKIE ACK、ECNE、CWR这四项必须要确保全网gNodeB均配置了该校验类型，若配置不一致，会导致链路连接失败，请谨慎操作。

**适用NF：AMF**

开启N2接口的DTLS连接时，需要配置详细的DTLS上下文参数，该命令用于设置N2接口DTLS连接参数。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-N2DTLSPARA]] · LST N2DTLSPARA
- [[command/UNC/20.15.2/SET-N2DTLSPARA]] · SET N2DTLSPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询N2接口的DTLS参数(LST-N2DTLSPARA)_54302475.md`
- 原始手册：`evidence/UNC/20.15.2/设置N2接口的DTLS参数(SET-N2DTLSPARA)_54302474.md`
