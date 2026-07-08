---
id: UNC@20.15.2@License@LKV2SSCM02
type: License
name: 支持SSC Mode2
nf: UNC
version: 20.15.2
license_code: LKV2SSCM02
control_item_id: '82209920'
applicable_nf:
- SMF
status: active
---

# 支持SSC Mode2

`LKV2SSCM02` · 控制项 82209920 ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

5G系统支持会话和业务的连续性SSC（Session and Service Continuity）。为了满足不同业务对连续性的不同要求，5G系统支持不同的SSC Mode，一个PDU会话的SSC Mode在该会话的生命周期里保持不变。SSC Mode2不提供IP连续性，在一个PDU会话中SMF请求UE释放原会话之后，重新建立一个新的到相同DN的PDU会话。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

适用于网页浏览等对于业务连续性要求不高，允许业务出现短暂中断的应用。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-107016 支持SSC Mode2

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_63967929.md`
