---
id: UNC@20.15.2@License@LKV3W9EBCS12
type: License
name: 支持事件计费
nf: UNC
version: 20.15.2
license_code: LKV3W9EBCS12
control_item_id: '82209455'
applicable_nf:
- GGSN-C
- PGW-C
- SMF
status: active
---

# 支持事件计费

`LKV3W9EBCS12` · 控制项 82209455 ·  · 域 

## 归属/适用NF（原文）

GGSN-C、PGW-C、SMF

## 功能描述

事件计费是依据用户使用数据业务的次数进行计费的一种计费方式。例如，用户访问HTTP业务，根据用户访问URL的次数进行收费。

## 实现描述

离线计费通过话单将用户计费信息上报给计费系统BS，当GGSN/PGW-C上通过配置<br>**ADD URR**<br>设置业务计费是事件类型后，即在话单中增加事件计费信息。<br>在线计费通过信用控制会话实时扣费，当GGSN/PGW-C上通过配置<br>**ADD URR**<br>设置业务计费是事件类型，且OCS在CCA消息中下发了事件配额即可进行事件计费。

## 取值范围

0～16000000 Bearer

## 默认值

10

## 应用场景

GGSN/PGW-C支持以下协议类型的事件计费：<br>HTTP业务：基于用户对HTTP业务的访问次数进行计费。这里的访问次数，是触发HTTP Get/Post请求的次数，不是用户点击链接的次数。实际上，用户在打开一个主页的过程中，可能会触发多个HTTP Get/Post请求。GGSN/PGW-C会当做多个事件进行计费。<br>RTSP业务：基于用户对流媒体服务的使用次数进行计费，与该数据流访问的时长和流量无关。例如观看一个视频文件，无论是刚开始访问还是访问了半个小时，会按照同样的事件次数计费。<br>WAP业务：基于用户对某种WAP（Wireless Application Protocol）业务的访问次数进行计费。<br>MMS业务：基于用户对MMS（Multimedia Messaging Service）服务的使用次数进行计费。

## 相关控制项（原文，未解释为边）

无。

## 对应特性（原文）

WSFD-109007 支持事件计费

## 控制的能力

- [WSFD-109007](feature/UNC/20.15.2/WSFD-109007.md)  — 控制项 82209455

## 证据

- 原始手册：`evidence/UNC/20.15.2/基本项_15088214.md`
