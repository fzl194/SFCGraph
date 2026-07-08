# 调测NB-IoT eDRX模式（MME）

- [操作场景](#ZH-CN_OPI_0277194594__1.3.1)
- [必备事项](#ZH-CN_OPI_0277194594__1.3.2)
- [操作步骤](#ZH-CN_OPI_0277194594__1.3.3)

## [操作场景](#ZH-CN_OPI_0277194594)

本操作指导介绍在运行网络中调测NB-IoT eDRX模式的操作过程。

## [必备事项](#ZH-CN_OPI_0277194594)

前提条件

- 请仔细阅读[WSFD-215002 NB-IoT eDRX模式特性概述（MME）](特性概述_75829027.md)。
- 完成[激活NB-IoT eDRX模式（MME）](激活NB-IoT eDRX模式（MME）_76015636.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息查询 | 查询方式（QUERYOPT） | BYIMSI | 本端规划 | - |
| 用户信息查询 | IMSI（IMSI） | 123034801000001 | 测试终端自带 | - |

工具

OM Portal跟踪

## [操作步骤](#ZH-CN_OPI_0277194594)

- **验证附着流程中支持eDRX特性。**
  在相关网元均完成本特性的配置后，可以采用以下步骤检查特性工作是否正常：
    1. 进入 “MML命令行-UNC” 窗口。
    2. 在 UNC 上创建用户跟踪。
    3. 终端开机、附着到网络，UE在附着消息中携带了Extended DRX parameters信元，如 [图1](#ZH-CN_OPI_0277194594__fig01) 所示。
      **图1** Attach Request消息中携带Extended DRX parameters信元

      <br>

      ![](调测NB-IoT eDRX模式（MME）_77194594.assets/zh-cn_image_0000002129027484_2.png "点击放大")
      NB-IoT（窄带）制式下查询MM上下文相关状态：
      [**DSP COMMMCTX**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/融合接入业务管理/融合用户数据库管理/显示移动性管理上下文的相关信息（DSP COMMMCTX）_58365337.md) : QUERYOPT=BYIMSI, IMSI="123034801000001";
      预期结果：

      - 报文中包含“UE请求的寻呼周期(秒)”，且该参数值为20.48。
          - 报文中包含“UE请求的寻呼时间窗口时长(秒)”，且该参数取值为10.24。

      > **说明**
      > Extended DRX parameters包含两个部分：寻呼时间窗口（Paging Time Window）和寻呼周期（eDRX value），具体的信元值的含义可参考3GPP 24.008 v10.15.0。
      在Attach Accept消息下发Extended DRX parameters信元给终端。如 [图2](#ZH-CN_OPI_0277194594__fig02) 所示。
      **图2** Attach Accept携带Extended DRX parameters信元

      <br>

      ![](调测NB-IoT eDRX模式（MME）_77194594.assets/zh-cn_image_0000002164228917_2.png "点击放大")
