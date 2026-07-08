# 调测支持NG-RAN和WLAN互操作

- [操作场景](#ZH-CN_OPI_0000002157554189__1.3.1)
- [必备事项](#ZH-CN_OPI_0000002157554189__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000002157554189__1.3.3)

## [操作场景](#ZH-CN_OPI_0000002157554189)

当系统支持用户可以在3GPP 5G网络和非3GPP WLAN间进行切换，而无需中断业务，需要对本功能进行调测，确保功能可以正常使用。

> **说明**
> 适用于PGW-C、SMF。

## [必备事项](#ZH-CN_OPI_0000002157554189)

前提条件

- 请仔细阅读[WSFD-201303 支持NG-RAN和WLAN互操作特性概述](特性概述_55783949.md)和[实现原理](实现原理_05264252.md)。
- PGW-C/SMF上完成S2b接口配置。
- 已完成特性License“82200FNQ LKV2VOWFNRSM01 VoWifi和VoNR互操作-USM”加载，可以通过**[DSP LICENSE](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)**命令查询确认，如果本特性的License在查询列表中可见，即可认为本特性License已加载成功。

数据

该操作无需准备数据。

工具

- 终端
- OM Portal跟踪

## [操作步骤](#ZH-CN_OPI_0000002157554189)

Active UE从WLAN网络到5G网络的切换

1. 在PGW-C/SMF的OM Portal上创建用户跟踪任务。
2. UE从WLAN网络接入。
  ![](调测支持NG-RAN和WLAN互操作_57554189.assets/zh-cn_image_0000002122316236_2.png)
3. UE切换到5G网络，进行初始注册、PDU会话建立流程，PDU Session Establishment Request消息中Request Type为“Existing PDU Session”，指示将当前会话从Non-3GPP网络切换到3GPP网络。
  ![](调测支持NG-RAN和WLAN互操作_57554189.assets/zh-cn_image_0000002122166428_2.png)
4. 完成到5G网络的切换后，向ePDG发送Delete Bearer Request，指示原因为“access changed from Non-3GPP to 3GPP”。
  ![](调测支持NG-RAN和WLAN互操作_57554189.assets/zh-cn_image_0000002157690217_2.png)

Active UE从5G网络到WLAN网络的切换

1. 在PGW-C/SMF的OM Portal上创建用户跟踪任务。
2. UE从5G网络接入。
  ![](调测支持NG-RAN和WLAN互操作_57554189.assets/zh-cn_image_0000002157701097_2.png)
3. UE切换到WLAN网络，ePDG向PGW-C发送Create Session Request消息，建立PDN连接，indication flags中“hi”指示位为1。
  ![](调测支持NG-RAN和WLAN互操作_57554189.assets/zh-cn_image_0000002157633553_2.png)
4. PGW-C/SMF通过5G网络接入发起网络请求的PDU Session Resource Release Command，释放5GC和NG-RAN资源。SMF向AMF发送Nsmf_PDUSession_SmContextsNotify Request指示PDU会话释放完成，原因为“PDU Session Handover”。
  ![](调测支持NG-RAN和WLAN互操作_57554189.assets/zh-cn_image_0000002122531790_2.png)
