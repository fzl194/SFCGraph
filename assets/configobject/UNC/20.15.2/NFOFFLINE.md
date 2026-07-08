---
id: UNC@20.15.2@ConfigObject@NFOFFLINE
type: ConfigObject
name: NFOFFLINE（NF下线）
nf: UNC
version: 20.15.2
object_name: NFOFFLINE
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

# NFOFFLINE（NF下线）

## 说明

![](激活NF下线（ACT NFOFFLINE）_09652524.assets/notice_3.0-zh-cn_2.png)

该命令用于激活NF下线，该命令执行以后，服务端场景下会触发NF向NRF的去注册处理，删除在NRF的注册，造成服务消费者无法发现该NF服务，导致该NF无法向外提供服务，请谨慎操作。

**适用NF：AMF、SMF、NRF、NSSF、NCG、SMSF**

该命令用来激活NF向NRF去注册。在NF进行升级、重装或重大网络调整等情况下，如果希望暂时不被其他NF发现，可以通过本命令触发NF到NRF的去注册。去注册会导致其他NF无法发现该NF，可能导致业务异常，请谨慎操作。

## 操作本对象的命令

- [[command/UNC/20.15.2/ACT-NFOFFLINE]] · ACT NFOFFLINE

## 证据

- 原始手册：`evidence/UNC/20.15.2/NFOFFLINE.md`
