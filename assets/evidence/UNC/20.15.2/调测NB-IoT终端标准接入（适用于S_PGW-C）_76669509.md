# 调测 NB-IoT终端标准接入 （适用于S/PGW-C）

- [操作场景](#ZH-CN_OPI_0276669509__1.3.1)
- [必备事项](#ZH-CN_OPI_0276669509__1.3.2)
- [操作步骤](#ZH-CN_OPI_0276669509__1.3.3)

## [操作场景](#ZH-CN_OPI_0276669509)

当运营商部署NB-IoT终端接入功能时，需对 UNC 的NB-IoT终端接入功能进行调测，确保该特性正常生效。

## [必备事项](#ZH-CN_OPI_0276669509)

前提条件

- 请仔细阅读[WSFD-011601 NB-IoT终端标准接入特性概述（适用于S/PGW-C）](特性概述_76669507.md)。
- 完成[激活基于信令面的数据传输（SGW-C）](../../WSFD-215101 基于信令面的数据传输/WSFD-215101 基于信令面的数据传输（SGW-C）/激活基于信令面的数据传输（SGW-C）_77260996.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息查询 | IMSI | 123000123456789 | 测试终端自带 | - |
| 测试终端使用的APN | APN | test | 已配置数据中获取 | 已通过<br>[**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>配置，可通过<br>[**LST APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md)<br>查询。 |

工具

- 测试终端
- OM Portal跟踪

## [操作步骤](#ZH-CN_OPI_0276669509)

1. 在OM Portal操作界面上 [创建用户跟踪任务](../../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) ，在“参数配置”栏输入用户IMSI，在“消息类型”栏选择GTPC、UP DATA和DOWN DATA消息类型。
2. 激活用户，并跟踪该用户消息。
3. 查看用户跟踪消息，检查MME发送给S-GW的、以及S-GW发送给P-GW的Create Session Request消息携带的“rat-type-value”值是否为“eutran-nb-iot(8)”，如 [图1](#ZH-CN_OPI_0276669509__fig1) 所示。
  **图1** RAT type信元

  <br>

  ![](调测NB-IoT终端标准接入（适用于S_PGW-C）_76669509.assets/zh-cn_image_0000002083871510_2.png)
    - 如果携带的“rat-type-value”值为“eutran-nb-iot(8)”，请执行 [步骤 4](#ZH-CN_OPI_0276669509__step4_new) 。
    - 如果携带的“rat-type-value”值不为“eutran-nb-iot(8)”，请执行 [步骤 5](#ZH-CN_OPI_0276669509__step5) 。
4. 查看P-GW发送给S-GW、S-GW发给MME的Create Session Response消息是否携带“request-accepted”字段，如 [图2](#ZH-CN_OPI_0276669509__fig2) 所示。
  **图2** Create Session Response消息

  <br>

  ![](调测NB-IoT终端标准接入（适用于S_PGW-C）_76669509.assets/zh-cn_image_0000002119391341_2.png)
    - 如果携带“request-accepted”字段，则调测完成。
    - 如果未携带“request-accepted”字段，请执行 [步骤 5](#ZH-CN_OPI_0276669509__step5) 。
5. 收集信息并寻求技术支持。
    a. 在OM Portal上创建用户跟踪任务 ，执行 [步骤 2](#ZH-CN_OPI_0276669509__step3) 并保存报文。
    b. 执行 [**EXP MML**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md) 命令将当前配置数据导出为MML脚本文件并保存。
    c. 查看并收集对端设备配置及接口状态信息。
    d. 收集归纳所有信息并联系华为技术支持解决。
