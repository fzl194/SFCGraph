# 调测基于HSS的P-CSCF故障恢复（适用于IMS PDN 重建）

- [操作场景](#ZH-CN_OPI_0000001143988078__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001143988078__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001143988078__1.3.3)

## [操作场景](#ZH-CN_OPI_0000001143988078)

调测基于HSS的P-CSCF故障恢复特性，以恢复VoLTE被叫场景为例进行调测。

## [必备事项](#ZH-CN_OPI_0000001143988078)

前提条件

- 请仔细阅读[WSFD-201205 基于HSS的P-CSCF故障恢复（IMS PDN 重建）特性概述](特性概述（适用于IMS PDN 重建）_89987789.md)。
- 完成[激活基于HSS的P-CSCF故障恢复（适用于IMS PDN 重建）](激活基于HSS的P-CSCF故障恢复（适用于IMS PDN 重建）_90107949.md)。

数据

无。

## [操作步骤](#ZH-CN_OPI_0000001143988078)

在相关网元均完成本特性的配置后，可以采用以下步骤检查特性工作是否正常：

![](调测基于HSS的P-CSCF故障恢复（适用于IMS PDN 重建）_43988078.assets/notice_3.0-zh-cn_2.png)

如下验证方法需要在P-CSCF故障时进行，建议在测试环境中进行，避免对现网业务造成影响。

1. 建立用户跟踪。
2. 用户A附着到LTE网络，并建立数据和IMS PDN连接。
3. P-CSCF故障。
4. 用户B呼叫用户A，并观测跟踪消息。
  **预期结果：** 呼叫用户A成功。同时跟踪消息可以看到：

  a. MME收到HSS发送的Insert Subscription Data Request (IDR-Flags bit8 = 1)消息。
    b. MME向终端发送Deactivate EPS Bearer Context Request，携带PCO（Protocol Configuration Options ）信元。
      > **说明**
      > Deactivate EPS Bearer Context Request消息携带的原因值可通过DWORD_EX12 BIT30进行设置。
    c. 用户A发起IMS PDN连接重建。
