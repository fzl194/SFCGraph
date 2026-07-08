---
id: UNC@20.15.2@License@LKV3WNBNIP11
type: License
name: Non-IP数据传输
nf: UNC
version: 20.15.2
license_code: LKV3WNBNIP11
control_item_id: '82209407'
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# Non-IP数据传输

`LKV3WNBNIP11` · 控制项 82209407 ·  · 域 

## 归属/适用NF（原文）

SGW-C、PGW-C

## 功能描述

此license用来控制是否支持用户进行Non-IP数据传输。

## 实现描述

系统中每激活一个支持Non-IP数据传输上下文，支持Non-IP数据传输上下文数加一；每去激活一个支持Non-IP数据传输上下文，支持Non-IP数据传输上下文数减一。<br>如果系统中已接入的支持Non-IP数据传输上下文达到License中“Non-IP数据传输”数值，新的支持Non-IP数据传输上下文将无法接入到系统。

## 取值范围

0~16000000 Bearer

## 默认值

10

## 应用场景

用户进行Non-IP数据传输。

## 相关控制项（原文，未解释为边）

基于信令面的数据传输。

## 对应特性（原文）

WSFD-215103 Non-IP数据传输

## 控制的能力

- [WSFD-215103](feature/UNC/20.15.2/WSFD-215103.md)  — 控制项 82209407

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63767897.md`
