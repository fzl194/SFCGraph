---
id: UNC@20.15.2@License@LKV2NOIP01
type: License
name: Non-IP数据传输
nf: UNC
version: 20.15.2
license_code: LKV2NOIP01
control_item_id: '82207383'
applicable_nf:
- MME
status: active
---

# Non-IP数据传输

`LKV2NOIP01` · 控制项 82207383 ·  · 域 

## 归属/适用NF（原文）

MME

## 功能描述

本特性支持NB-IoT（Narrow Band Internet of Things）制式UE通过NB-IoT RAN接入MME后，建立Non-IP的PDN上下文，并采用Non-IP Data Over NAS进行数据传输，从而减小传送数据包大小，提高传输效率和空口容量。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

在大多数物联网行业应用中，终端发送数据报文频率较低且字节较小（一般在20到200个字节之间），但仅数据报文头（UDP/IP传输层协议栈）所占用字节数有时就会超过数据，导致数据报文在传输过程中的有效字节数较低。在这种场景下，可以使用本特性来大幅度提升无线网络数据传输效率。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-215103 Non-IP数据传输

## 控制的能力

- [WSFD-215103](feature/UNC/20.15.2/WSFD-215103.md)  — 控制项 82207383

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
