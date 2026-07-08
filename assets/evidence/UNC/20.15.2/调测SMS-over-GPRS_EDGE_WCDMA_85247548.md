# 调测SMS over GPRS/EDGE/WCDMA

- [操作场景](#ZH-CN_OPI_0185247548__1.3.1)
- [必备事项](#ZH-CN_OPI_0185247548__1.3.2)
- [操作步骤](#ZH-CN_OPI_0185247548__1.3.3)

## [操作场景](#ZH-CN_OPI_0185247548)

本操作指导介绍在运行网络中调测SMS over GPRS/EDGE/WCDMA特性的操作过程。

## [必备事项](#ZH-CN_OPI_0185247548)

前提条件

- 请仔细阅读[WSFD-106202 SMS over GPRS/EDGE/WCDMA特性概述](特性概述_85247546.md)
- 完成[激活SMS over GPRS/EDGE/WCDMA](激活SMS over GPRS_EDGE_WCDMA_84683740.md)。

数据

该操作无需准备数据。

工具

OM Portal跟踪。

## [操作步骤](#ZH-CN_OPI_0185247548)

在完成本特性的配置后，可以采用以下步骤检查特性工作是否正常：

> **说明**
> 在验证操作前做如下准备：
>
> - UNC系统工作正常，且UNC的各个接口工作正常。
> - 短消息中心工作正常。
> - 用户A、B在HLR中已经签约PS短消息业务。
> - 在MSA和MSB上设置通过PS发送短消息，MSA短消息中心设置为8613951702，MSB短消息中心设置为8613951996。
> - UNC与CG的计费版本一致。

1. 进入 “MML命令行-UNC” 窗口。
2. [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) : LICITEM="LKV2SMS02";
  预期结果：可以查看到License开关项为“开启”。
3. 查看PLMN配置信息。
    - [**LST HPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/查询本地PLMN(LST HPLMN)_72345675.md) : MCC=移动国家码 , MNC=移动网号 ;
      预期结果：可以查看到对应的配置信息。
    - [**LST CONNECTPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/查询互联PLMN(LST CONNECTPLMN)_72225723.md) : MCC=移动国家码 , MNC=移动网号 ;
      预期结果：可以查看到对应的配置信息。
4. 查看短消息计费。
    a. 在UNC操作维护台上创建用户跟踪任务。
    b. 用户A、B开机附着到网络上。
    c. 用户A给B发送一条短消息。
      预期结果：用户A短消息发送成功，用户B成功接收短消息。
    d. 在 UNC 操作维护台上查看消息跟踪。
      预期结果： UNC 分别生成S-SMO-CDR和S-SMT-CDR话单，能从CG的话单浏览器中查询到S-SMO-CDR和S-SMT-CDR话单，并且S-SMO-CDR话单中的短消息中心地址为纠正后的短消息中心地址（8613951996）。
