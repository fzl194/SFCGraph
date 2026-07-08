# 调测NB-IoT eDRX模式（SGW-C）

- [操作场景](#ZH-CN_OPI_0277194598__1.3.1)
- [必备事项](#ZH-CN_OPI_0277194598__1.3.2)
- [操作步骤](#ZH-CN_OPI_0277194598__1.3.3)

## [操作场景](#ZH-CN_OPI_0277194598)

当运营商部署 NB-IoT eDRX模式 功能时，需对该功能进行调测，确保该功能正常生效。

> **说明**
> 适用于SGW-C。

## [必备事项](#ZH-CN_OPI_0277194598)

前提条件

- 请仔细阅读[WSFD-215002 NB-IoT eDRX模式特性概述（SGW-C）](特性概述_77194596.md)。
- 完成[激活NB-IoT eDRX模式（SGW-C）](激活NB-IoT eDRX模式（SGW-C）_77194597.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息查询 | IMSI | 123000123456789 | 测试终端自带 | - |
| 测试终端使用的APN | APN | test | 已配置数据中获取 | 取自<br>[激活NB-IoT eDRX模式](激活NB-IoT eDRX模式（SGW-C）_77194597.md)<br>中配置的APN实例名。 |

工具

- 测试终端
- OM Portal跟踪

## [操作步骤](#ZH-CN_OPI_0277194598)

1. 进入 “MML命令行-UNC” 窗口。
2. 查询License中是否允许使用 NB-IoT eDRX模式 功能。
  [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) : LICITEM="LKV3WNBDRX11";
    - 如果“ 开关”为“使能”，请执行[3](#ZH-CN_OPI_0277194598__cmd1126127540184705)。
    - 如果“ 开关”为“不使能”，则执行 [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
3. 在OM Portal上 [创建用户跟踪任务](../../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) ，在“参数配置”栏输入用户IMSI，在“消息类型”栏选择GTPC、UP DATA和DOWN DATA消息类型。 [4](#ZH-CN_OPI_0277194598__step3)
4. 测试终端使用“test”APN接入网络，并进行下行数据业务。激活用户，并跟踪该用户消息。
5. 查看用户跟踪消息，可以跟踪到MME发送给S-GW的Downlink Data Notification Acknowledgement消息携带DL Buffering Duration信元，S-GW按信元携带的时间缓存下行数据包。如 [图1](#ZH-CN_OPI_0277194598__fig1) 所示。
  **图1** DL Buffering Duration信元

  <br>

  ![](调测NB-IoT eDRX模式（SGW-C）_77194598.assets/zh-cn_image_0277204121_2.png)
6. 等待终端寻呼成功，可以跟踪到Modify Bearer Request和Modify Bearer Response消息。检查S-GW缓存的数据包是否转发给MME。
    - 如果S-GW缓存的数据包正常转发给MME，则该功能调测完成。
    - 如果S-GW缓存的数据包未能正常转发给MME，请执行[7](#ZH-CN_OPI_0277194598__cmd1590441288184705)。
7. 执行 [**DSP ACTALM**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/单体服务公共功能管理/操作维护/告警管理/活动告警/显示活动告警（DSP ACTALM）_59104140.md) 命令，查看是否存在 [ALM-81027 内部资源不足](../../../../../../网络运维/故障处理/UNC告警处理/业务告警/SMF&GW-C&GGSN/ALM-81027 内部资源不足_36590880.md) 告警，且告警提示信息为“eDRX Buffering Resource Alarm”。
    - 如果产生告警，请参考[ALM-81027 内部资源不足](../../../../../../网络运维/故障处理/UNC告警处理/业务告警/SMF&GW-C&GGSN/ALM-81027 内部资源不足_36590880.md)处理步骤解决。
    - 如果没有产生告警，请执行[8](#ZH-CN_OPI_0277194598__cmd165620017184705)。
8. 收集信息并寻求技术支持。
    a. 在OM Portal上创建用户跟踪任务 ，执行 [4](#ZH-CN_OPI_0277194598__step3) 并保存报文。
    b. 执行 **[EXP MML](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md)** 命令将当前配置数据导出为MML脚本文件并保存。
    c. 查看并收集对端设备配置及接口状态信息。
    d. 收集归纳所有信息并联系华为技术支持解决。
