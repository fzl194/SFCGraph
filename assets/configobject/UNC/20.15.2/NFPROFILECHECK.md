---
id: UNC@20.15.2@ConfigObject@NFPROFILECHECK
type: ConfigObject
name: NFPROFILECHECK（测试NF和NRF上的网元信息是否一致）
nf: UNC
version: 20.15.2
object_name: NFPROFILECHECK
object_kind: action
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
status: active
---

# NFPROFILECHECK（测试NF和NRF上的网元信息是否一致）

## 说明

**适用NF：AMF、SMF、NRF、NSSF、SMSF**

该命令用来手动触发NF本地配置的NFProfile信息和NRF上存储的该NF的NFProfile信息校验，如果两者不一致NF会自动触发一次注册，保证NRF上存储的NFProfile信息和本地配置的保持一致。

## 操作本对象的命令

- [[command/UNC/20.15.2/TST-NFPROFILECHECK]] · TST NFPROFILECHECK

## 证据

- 原始手册：`evidence/UNC/20.15.2/测试NF和NRF上的网元信息是否一致（TST-NFPROFILECHECK）_35803156.md`
