---
id: UNC@20.15.2@ConfigObject@NRFPARA
type: ConfigObject
name: NRFPARA（NRF协议参数）
nf: UNC
version: 20.15.2
object_name: NRFPARA
object_kind: entity
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
- CBCF
status: active
---

# NRFPARA（NRF协议参数）

## 说明

![](增加NRF协议参数（ADD NRFPARA）_09652551.assets/notice_3.0-zh-cn_2.png)

OAUTH2SWITCH配置为ON时，如果端到端不支持OAUTHTOKEN功能，可能会导致业务呼损，建议配置为OFF。

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、CBCF**

该命令用于增加NRF协议相关的配置信息。与NRF对接的时候使用，可用于设置等待时长和最大重传次数等参数。

## 操作本对象的命令

- [ADD NRFPARA](command/UNC/20.15.2/ADD-NRFPARA.md)
- [LST NRFPARA](command/UNC/20.15.2/LST-NRFPARA.md)
- [MOD NRFPARA](command/UNC/20.15.2/MOD-NRFPARA.md)
- [RMV NRFPARA](command/UNC/20.15.2/RMV-NRFPARA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改NRF协议参数（MOD-NRFPARA）_09652973.md`
- 原始手册：`evidence/UNC/20.15.2/删除NRF协议参数（RMV-NRFPARA）_09651539.md`
- 原始手册：`evidence/UNC/20.15.2/增加NRF协议参数（ADD-NRFPARA）_09652551.md`
- 原始手册：`evidence/UNC/20.15.2/查询NRF协议参数（LST-NRFPARA）_09653029.md`
