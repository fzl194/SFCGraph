---
id: UDG@20.15.2@License@LKV3G5RTHE01
type: License
name: RTSP头增强
nf: UDG
version: 20.15.2
license_code: LKV3G5RTHE01
control_item_id: '82209778'
license_domain: UDG
control_item_type: resource
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# RTSP头增强

`LKV3G5RTHE01` · 控制项 82209778 · resource · 域 UDG

## 归属/适用NF（原文）

SGW-U、PGW-U、UPF

## 功能描述

RTSP头增强指对RTSP报文头的内容做增强处理，将用户信息IMSI、Hashed-IMSI、IMSI Password、MSISDN、Hashed-MSISDN、MSISDN Password、SGSN-IP、Hashed-SGSN-IP、SGSN-IP Password、APN、MS IP Address、Zone-id、Billing-type、IMEI、IMEI Type、Charge-Characteristic Name、User Defined Value中的一个或多个添加到RTSP报文头并传递给Server，运营商和服务提供商可基于这些信息灵活开展业务和实施控制，例如业务认证、广告宣传、业务推广和账户管理与查询。

## 实现描述

- 建立TCP连接。TCP连接建立报文的目的IP地址为Server的IP地址。当TCP连接建立报文到达网关后，网关允许其通过，这样就建立起了MS和Server间的TCP连接。<br>- TCP连接建立成功后，MS发起RTSP业务，MS发送的RTSP请求报文到达网关。<br>- 网关首先对报文的协议类型进行识别，协议识别成功后进行报文的SA解析处理，根据SA解析到的报文特征信息进行七层策略匹配，并根据匹配到的结果进行计费或执行动作。当判断出该报文匹配到了RTSP头增强动作，需要进行RTSP头增强处理时，则提取本地预定义的配置和用户的相关信息，以<字段前缀名称: 字段值>格式插入到RTSP 请求报文头中。由于网关对报文新增了数据信息，因此还需要按照协议规定进行TCP层和IP层的某些字段值调整，例如长度与检验字段。<br>- 网关将添加了头增强信息的RTSP请求报文发送给Server。<br>- Server接收到RTSP响应报文后获取当前用户的信息，构造并返回给网关用户个性化的请求响应页面。<br>- 网关对收到的RTSP响应报文进行解析和头增强处理后转发给MS，MS接收并向用户显示RTSP响应报文内容。MS并不感知网关对业务报文的RTSP头增强处理过程。

## 取值范围

0～16000000

## 默认值

10

## 应用场景

由于Server通常部署在数据通信网络中，因此在未开启RTSP头增强特性时，Server无法得知具体用户的相关信息，运营商无法对用户的业务访问进行控制。而当在网元上开启RTSP头增强特性后，用户的相关信息IMSI、Hashed-IMSI、IMSI Password、MSISDN、Hashed-MSISDN、MSISDN Password、SGSN-IP、Hashed-SGSN-IP、SGSN-IP Password、APN、MS IP Address、Zone-id、Billing-type、IMEI、IMEI Type、Charge-Characteristic Name、User Defined Value中的一个或多个就可以由<br>UDG<br>添加到RTSP报文头中传递给Server，从而很好的满足了运营商针对用户做业务访问认证的需求。<br>由于<br>UDG<br>对报文新增或修改了数据信息，因此还需要按照协议规定进行TCP层和IP层的某些字段值调整，例如长度与检验字段等，并对该业务流的后续报文进行RTSP头增强处理，这些处理过程与普通RTSP头增强处理流程一致。

## 相关控制项（原文，未解释为边）

- SA-Basic<br>- SA-Streaming

## 对应特性（原文）

GWFD-110262 RTSP头增强

## 控制的能力

- [GWFD-110262](feature/UDG/20.15.2/GWFD-110262.md)  — 控制项 82209778

## 证据

- 原始手册：`evidence/UDG/20.15.2/资源控制项_69147293.md`
