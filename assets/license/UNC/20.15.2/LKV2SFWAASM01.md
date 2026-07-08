---
id: UNC@20.15.2@License@LKV2SFWAASM01
type: License
name: 支持FWA接入 - USM
nf: UNC
version: 20.15.2
license_code: LKV2SFWAASM01
control_item_id: 82200HWG
applicable_nf:
- SMF
status: active
---

# 支持FWA接入 - USM

`LKV2SFWAASM01` · 控制项 82200HWG ·  · 域 

## 归属/适用NF（原文）

SMF

## 功能描述

FWA（Fixed Wireless Access）是一种固定宽带的接入技术，指家庭或企业的各种终端设备通过CPE（Customer-Premises Equipment ）直接接入无线网络，提供用户宽带接入功能。根据接入方式可以将固定宽带的接入方式分为有线接入技术和无线接入技术两种，有线接入技术主要包括混合光纤同轴电缆（HFC）接入、铜线（xDSL）接入和光纤（FTTx）接入；无线接入技术主要就是固定无线接入（FWA）。

## 实现描述

SMF系统中每激活一个使用FWA业务的会话，该License总数加1；每去激活一个使用FWA业务的会话，总数减1。

## 取值范围

0~16000000 Session

## 默认值

10

## 应用场景

FWA主要针对以下两大场景：<br>- 家庭宽带：- 拓宽基础连接。<br>- 替代xDSL接入。<br>- 类光纤服务。<br>- 中小型企业场景：- 一些中小型企业往往处于郊区或者农村，无法连接固定网络。FWA帮助运营商满足这些用户的需求，并且提供相对低廉的价格。<br>- 临时或者半移动的场所，例如建筑工地，码头堆场，或者公交汽车等，会需要使用监控设备，但是由于其场景的特殊性无法使用固网，FWA可以给他们提供更灵活的解决方案。<br>- 针对金融，邮政等对实时性，数据要求高的行业，除了部署固定网络以外，FWA作为5G 业务增强，可以进一步保证网络的速率和稳定。

## 相关控制项（原文，未解释为边）

无

## 对应特性（原文）

WSFD-010112 支持FWA接入

## 控制的能力

- [WSFD-010112](feature/UNC/20.15.2/WSFD-010112.md)  — 控制项 82200HWG

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15248022.md`
