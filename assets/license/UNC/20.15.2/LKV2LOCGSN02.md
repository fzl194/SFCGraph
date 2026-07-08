---
id: UNC@20.15.2@License@LKV2LOCGSN02
type: License
name: 基于位置区域选择网关
nf: UNC
version: 20.15.2
license_code: LKV2LOCGSN02
control_item_id: '82206561'
applicable_nf:
- SGSN
- MME
status: active
---

# 基于位置区域选择网关

`LKV2LOCGSN02` · 控制项 82206561 ·  · 域 

## 归属/适用NF（原文）

SGSN/MME

## 功能描述

基于<br>位置区域<br>选择<br>网关<br>，是指<br>UNC<br>在使用<br>APN<br>(Access Point Name)进行<br>DNS<br>(Domain Name Service)解析获取网关的IP地址前，首先通过域名定制方法在原APN中加入用户位置信息(LAI/RAI/TAI)，然后向DNS服务器发送定制域名，获取GGSN/P-GW-C的IP地址，实现基于用户位置信息的网关选择。<br>UNC<br>可以根据UE的位置信息选择离RAC/eNodeB最近的GGSN/PGW-C，以缩短用户数据的传输路径。

## 实现描述

只有获得了License许可后才能获得该特性的服务。

## 取值范围

0～12000000 SAU

## 默认值

10

## 应用场景

- 在Direct Tunnel应用场景中，RNC需要和网关之间直接建立用户面隧道，为了降低RNC和网关之间的数据传输路径，部署分布式网关后，UNC可以根据用户的位置信息选择离RAN最近的网关。<br>- 若MME/SGSN集中部署，网关（GGSN/PGW-C）设备下沉，无线接入设备分布在多个局点，可通过配置本特性选择离eNodeB/RNC侧更近的网关，缩短用户面传输路径。<br>- 若运营商希望对某些特定区域的用户指定特定的GGSN/PGW-C，在用户进行接入时，可通过配置本特性将其指定到特定的GGSN/PGW-C上。<br>上述场景中，当用户接入时，<br>UNC<br>首先对用户APN进行扩展，在其APN中增加位置信息，然后再将定制域名（即扩展后的APN）送到DNS解析，DNS根据用户的位置信息，返回与用户距离最近的GGSN/PGW-C的IP地址，<br>UNC<br>通过该地址为用户建立连接。

## 相关控制项（原文，未解释为边）

请求信息纠正功能

## 对应特性（原文）

WSFD-205003 基于位置区域选择网关

## 控制的能力

- [WSFD-205003](feature/UNC/20.15.2/WSFD-205003.md)  — 控制项 82206561

## 证据

- 原始手册：`evidence/UNC/20.15.2/可选项_15088206.md`
