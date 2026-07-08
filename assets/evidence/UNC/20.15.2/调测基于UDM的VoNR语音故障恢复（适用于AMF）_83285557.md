# 调测基于UDM的VoNR语音故障恢复（适用于AMF）

- [操作场景](#ZH-CN_OPI_0283285557__1.3.1)
- [必备事项](#ZH-CN_OPI_0283285557__1.3.2)
- [操作步骤](#ZH-CN_OPI_0283285557__1.3.3)

## [操作场景](#ZH-CN_OPI_0283285557)

调测基于UDM的VoNR语音故障恢复特性，以恢复VoNR被叫场景为例进行调测。

> **说明**
> 适用于AMF。

## [必备事项](#ZH-CN_OPI_0283285557)

前提条件

- 请仔细阅读[WSFD-221002 基于UDM的VoNR语音故障恢复特性概述](WSFD-221002 基于UDM的VoNR语音故障恢复特性概述_11685434.md)。
- 完成[激活基于UDM的VoNR语音故障恢复（适用于AMF）](激活基于UDM的VoNR语音故障恢复（适用于AMF）_28824215.md)。

数据

无。

## [操作步骤](#ZH-CN_OPI_0283285557)

- 在相关网元均完成本特性的配置后，可以采用以下步骤检查特性工作是否正常：
  ![](调测基于UDM的VoNR语音故障恢复（适用于AMF）_83285557.assets/notice_3.0-zh-cn_2.png)

  如下验证方法需要在P-CSCF故障时进行，建议在测试环境中进行，避免对现网业务造成影响。
    1. 建立用户跟踪。
    2. 用户A注册到5G网络，并建立数据和IMS PDU会话连接。
    3. P-CSCF故障。
    4. A处于连接态，用户B呼叫用户A，并观测跟踪消息。
      **预期结果：** 呼叫用户A成功。同时跟踪消息可以看到：

      a. AMF收到UDM发送的Nudm_UECM_PcscfRestoration3GPPAccessNotify Request消息。
          b. 会话释放，AMF向SMF发送Nsmf_PDUSession_UpdateSMContext，携带Cause为"REL_DUE_TO_REACTIVATION"。
          c. 用户A发起IMS PDU会话连接重建。
