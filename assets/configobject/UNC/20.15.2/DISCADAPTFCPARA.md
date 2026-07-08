---
id: UNC@20.15.2@ConfigObject@DISCADAPTFCPARA
type: ConfigObject
name: DISCADAPTFCPARA（服务发现自适应流控全局配置）
nf: UNC
version: 20.15.2
object_name: DISCADAPTFCPARA
object_kind: global_setting
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
status: active
---

# DISCADAPTFCPARA（服务发现自适应流控全局配置）

## 说明

![](设置服务发现自适应流控全局配置（SET DISCADAPTFCPARA）_10690450.assets/notice_3.0-zh-cn_2.png)

如果CODES被设置为非流控返回码，可能会发生误流控导致服务发现速率被限制。

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于设置服务发现自适应流控全局配置。系统会根据这些配置和当前状态来判断是否要进行流控。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-DISCADAPTFCPARA]] · LST DISCADAPTFCPARA
- [[command/UNC/20.15.2/SET-DISCADAPTFCPARA]] · SET DISCADAPTFCPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/DISCADAPTFCPARA.md`
- 原始手册：`evidence/UNC/20.15.2/DISCADAPTFCPARA.md`
