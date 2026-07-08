---
id: UNC@20.15.2@ConfigObject@NFONLINE
type: ConfigObject
name: NFONLINE（NF上线）
nf: UNC
version: 20.15.2
object_name: NFONLINE
object_kind: action
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
- SMSF
status: active
---

# NFONLINE（NF上线）

## 说明

**适用NF：AMF、SMF、NRF、NSSF、NCG、SMSF**

该命令用来激活NF向NRF注册。在完成NF相关基础数据配置后，可以通过本命令手动触发NF到NRF的注册。也可以在NF注册、或者配置数据更新异常的情况下，通过本命令重新手动触发NF到NRF的重新上线注册。

## 操作本对象的命令

- [[command/UNC/20.15.2/ACT-NFONLINE]] · ACT NFONLINE

## 证据

- 原始手册：`evidence/UNC/20.15.2/NFONLINE.md`
