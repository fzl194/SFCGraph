---
id: UNC@20.15.2@License@LKV3WPHOLW11
type: License
name: E-UTRAN和WLAN互操作
nf: UNC
version: 20.15.2
license_code: LKV3WPHOLW11
control_item_id: '82209418'
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# E-UTRAN和WLAN互操作

`LKV3WPHOLW11` · 控制项 82209418 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

LTE与WIFI间的非优化切换功能指用户可以在3GPP E-UTRAN网络和Non-3GPP WLAN网络间进行切换，而无需中断业务。

## 实现描述

License中LTE与WIFI间的非优化切换功能项为允许时，支持LTE与WIFI间的非优化切换功能生效；否则不生效。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

支持LTE和WIFI用户同时接入，为切换用户提供平滑的服务。对于实时性要求不高的数据业务，如浏览、消息业务、文件下载、流媒体等，LTE和WIFI的非优化切换即可支持该类业务的连续性。

## 相关控制项（原文，未解释为边）

无。

## 对应特性（原文）

WSFD-201301 E-UTRAN和WLAN互操作

## 控制的能力

- [WSFD-201301](feature/UNC/20.15.2/WSFD-201301.md)  — 控制项 82209418

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63767897.md`
