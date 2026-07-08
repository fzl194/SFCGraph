---
id: UNC@20.15.2@License@LKV2VPFBSM01
type: License
name: 语音PCF故障bypass
nf: UNC
version: 20.15.2
license_code: LKV2VPFBSM01
control_item_id: 82200HME
applicable_nf:
- PGW-C
- SMF
status: active
---

# 语音PCF故障bypass

`LKV2VPFBSM01` · 控制项 82200HME ·  · 域 

## 归属/适用NF（原文）

PGW-C、SMF

## 功能描述

语音PCF故障bypass是在语音域PCF全部故障时，SMF/PGW-C支持将语音业务会话转换为本地PCC会话，不再向PCF获取动态PCC策略，使用本地配置的PCC策略，保证语音业务可以惯性运行，避免影响用户业务。

## 实现描述

在建立语音会话，语音会话回滚的时候，该License总数加1；在删除bypass的语音会话的时候，该License总数减1；

## 取值范围

0～16000000 Session

## 默认值

10

## 应用场景

为避免在语音域PCF全部故障时语音业务不可用，可以开启本特性，提升语音业务可靠性。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-201207 语音PCF/PCRF故障Bypass

## 控制的能力

- [WSFD-201207](feature/UNC/20.15.2/WSFD-201207.md)  — 控制项 82200HME

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_63767897.md`
