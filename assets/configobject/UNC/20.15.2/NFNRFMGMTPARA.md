---
id: UNC@20.15.2@ConfigObject@NFNRFMGMTPARA
type: ConfigObject
name: NFNRFMGMTPARA（NF与NRF间的全局管理参数）
nf: UNC
version: 20.15.2
object_name: NFNRFMGMTPARA
object_kind: global_setting
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- NCG
- SMSF
- CBCF
status: active
---

# NFNRFMGMTPARA（NF与NRF间的全局管理参数）

## 说明

![](设置NF与NRF间的全局管理参数（SET NFNRFMGMTPARA）_32041712.assets/notice_3.0-zh-cn_2.png)

执行本命令将NTFUPDCACHESW开关打开时，当NRF订阅通知消息量较大时，可能会对通信造成压力。

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF、CBCF**

该命令用于配置NF与NRF间的管理参数。NF向NRF注册、订阅/通知、发现时，需要配置一些参数控制不同功能。例如NRF主备组网情况下，当主用NRF故障恢复后，NF可以配置自动从备用NRF切换到主用NRF；针对缓存的NF，可以控制本端网元是否使用NRF发送的订阅通知中的NfProfile信息更新其缓存信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NFNRFMGMTPARA]] · LST NFNRFMGMTPARA
- [[command/UNC/20.15.2/SET-NFNRFMGMTPARA]] · SET NFNRFMGMTPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/NFNRFMGMTPARA.md`
- 原始手册：`evidence/UNC/20.15.2/NFNRFMGMTPARA.md`
