# 调测NB-IoT eDRX模式

- [操作场景](#ZH-CN_OPI_0267487578__1.3.1)
- [必备事项](#ZH-CN_OPI_0267487578__1.3.2)
- [操作步骤](#ZH-CN_OPI_0267487578__1.3.3)

## [操作场景](#ZH-CN_OPI_0267487578)

当运营商部署NB-IoT eDRX功能时，需对该功能进行调测，确保该功能正常生效。

> **说明**
> 适用于SGW-U。

## [必备事项](#ZH-CN_OPI_0267487578)

前提条件

- 请仔细阅读[GWFD-110601 NB-IoT eDRX模式](../GWFD-110601 NB-IoT eDRX模式_67378801.md)。
- 完成[激活NB-IoT eDRX模式](激活NB-IoT eDRX模式_67487577.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息查询 | IMSI | 460000123456789 | 测试终端自带 | - |
| 测试终端使用的APN | APN | apnnb | 已配置数据中获取 | 取自<br>[激活NB-IoT eDRX模式](激活NB-IoT eDRX模式_67487577.md)<br>中配置的APN实例名。 |

工具

- 测试终端
- OM Portal跟踪工具

## [操作步骤](#ZH-CN_OPI_0267487578)

1. 请确认NB-IoT基本功能已开启（详见 [激活NB-IoT终端标准接入](../GWFD-010296 NB-IoT终端标准接入/激活NB-IoT终端标准接入_74275194.md) ），并使用 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09587900.md) 命令查询是否开启了NB-IoT eDRX功能。
  ```
  LST LICENSESWITCH: LICITEM="LKV3G5NDRX01";
  ```
    - 如果 “Switch” 为 “ENABLE” ，请执行[步骤 2](#ZH-CN_OPI_0267487578__step2)。
    - 如果 “Switch” 为 “DISABLE” ，则执行 [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md) 命令打开本特性对应的License配置开关。
2. 在OM Portal上 [创建UDG用户跟踪任务](../../../../../../网络运维/日常维护/UDG基础运维操作/创建消息跟踪/创建用户跟踪/创建UDG用户跟踪任务_88792206.md) ，在“参数配置”栏输入用户IMSI，在“消息类型”栏选择UP DATA和DOWN DATA消息类型。同时在UNC上开启对GTP-C消息的跟踪任务。
3. 测试终端使用“apnnb”APN接入网络，并进行下行数据业务。激活用户，并跟踪该用户消息。
4. 查看UNC用户跟踪消息，可以跟踪到MME发送给SGW-C的Downlink Data Notification Acknowledgement消息携带DL Buffering Duration信元，SGW-C将缓存时长通知SGW-U，SGW-U按信元携带的时间缓存下行数据包。如 [图1](#ZH-CN_OPI_0267487578__fig1) 所示。
  **图1** DL Buffering Duration信元

  <br>

  ![](调测NB-IoT eDRX模式_67487578.assets/zh-cn_image_0287128740.png)
5. 等待终端寻呼成功，可以跟踪到Modify Bearer Request和Modify Bearer Response消息。检查SGW-U缓存的数据包是否转发给MME。
    - 如果SGW-U缓存的数据包正常转发给MME，则该功能调测完成。
    - 如果SGW-U缓存的数据包未能正常转发给MME，请执行[步骤 6](#ZH-CN_OPI_0267487578__step5_new)。
6. 执行 [**DSP ACTALM**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/单体服务公共功能管理/操作维护/告警管理/活动告警/显示活动告警（DSP ACTALM）_59104140.md) 命令，查看是否存在 [ALM-81002 数据转发类内部资源不足](../../../../../../网络运维/故障处理/用户面告警/ALM-81002 数据转发类内部资源不足_15522308.md) 告警，且告警提示信息为“eDRX Buffering Resource Alarm”。
    - 如果产生告警，请参考[ALM-81002 数据转发类内部资源不足](../../../../../../网络运维/故障处理/用户面告警/ALM-81002 数据转发类内部资源不足_15522308.md)处理步骤解决。
    - 如果没有产生告警，请执行[步骤 7](#ZH-CN_OPI_0267487578__step204091850132213)。
7. 收集问题信息并寻求技术支持。
    a. 在镜像接口或服务器上开启第三方抓包工具，执行 [3](#ZH-CN_OPI_0267487578__step3) 并保存报文。
    b. 在相应窗口下执行 [**EXP MML**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md) 命令将当前配置数据导出为MML脚本文件并保存。
    c. 收集并保存上述所有查询信息。
    d. 归纳所有信息并联系华为技术支持解决。
