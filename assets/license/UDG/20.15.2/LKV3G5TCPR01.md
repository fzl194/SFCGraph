---
id: UDG@20.15.2@License@LKV3G5TCPR01
type: License
name: TCP重传识别
nf: UDG
version: 20.15.2
license_code: LKV3G5TCPR01
control_item_id: 82200DER
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# TCP重传识别

`LKV3G5TCPR01` · 控制项 82200DER · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

TCP重传识别是指<br>UDG<br>支持识别TCP重传报文，根据配置对重传报文流量实施灵活的计费策略。

## 实现描述

重传报文是否识别并且灵活计费受该License控制。<br>License不开启时，重传报文不会识别并且灵活计费。<br>License开启时，重传报文会识别并且灵活计费。

## 取值范围

10~16000000

## 默认值

10

## 应用场景

用户进行业务访问，<br>UDG<br>对报文进行解析，如果识别出是重传报文，则根据本地配置实施灵活的计费策略。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

GWFD-020307 TCP重传识别

## 控制的能力

- [GWFD-020307](feature/UDG/20.15.2/GWFD-020307.md)  — 控制项 82200DER

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
