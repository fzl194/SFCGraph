# 调测 支持Category NB2接入 （S/PGW-C）

- [操作场景](#ZH-CN_OPI_0277673143__1.3.1)
- [必备事项](#ZH-CN_OPI_0277673143__1.3.2)
- [操作步骤](#ZH-CN_OPI_0277673143__1.3.3)

## [操作场景](#ZH-CN_OPI_0277673143)

本操作指导介绍在运行网络中调测 支持Category NB2接入 的操作过程。

> **说明**
> SGW-C、PGW-C

## [必备事项](#ZH-CN_OPI_0277673143)

前提条件

- 请仔细阅读[WSFD-215501 支持Category NB2接入特性概述（S/PGW-C）](特性概述_77673141.md)。
- 完成[激活支持Category NB2接入（S/PGW-C）](激活支持Category NB2接入（S_PGW-C）_77673142.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| APN名称 | APN（APN名称） | apn-test | 本端规划 | [**LST APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/查询APN配置（LST APN）_09652599.md) |
| 用户信息查询 | IMSI | 123000123456789 | 测试终端自带 | - |

工具

- NB-IoT测试终端
- 接入侧/PDN侧镜像接口已安装第三方抓包工具
- OM Portal跟踪工具

## [操作步骤](#ZH-CN_OPI_0277673143)

1. 进入 “MML命令行-UNC” 窗口。
2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询license中是否允许使用Category NB2 接入功能。
    - 如果 “SWITCH” 为 “ENABLE” ，请执行 [3](#ZH-CN_OPI_0277673143__cmd901522578184706) 。
    - 如果 “SWITCH” 为 “DISABLE” ，则执行 [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
3. 打开接入侧/PDN侧镜像接口上的抓包工具，准备抓取 测试终端 的出入报文。
4. 测试终端 使用“apn-test”APN接入网络，并开始使用NB-IoT业务。
    - 如果测试终端可以使用NB-IoT业务，请执行[5](#ZH-CN_OPI_0277673143__cmd861663247184706)。
    - 如果测试终端无法使用NB-IoT业务，请调测UNC的NB-IoT终端接入业务。之后，重新执行此步骤。
5. 在OM Portal上 [创建用户跟踪任务](../../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) ，在 “参数配置” 栏输入用户IMSI，查看用户跟踪消息中SGW-C收到的Create Session Request消息中的下行APN-AMBR数值，检查用户请求的 “apn-ambr-for-uplink” / “apn-ambr-for-downlink” 是否大于164Kbit/s/140Kbit/s。如 [图1](#ZH-CN_OPI_0277673143__fig_lic4) 所示。
  **图1** Create Session Request消息

  <br>

  ![](调测支持Category NB2接入（S_PGW-C）_77673143.assets/zh-cn_image_0000001381661364_2.png)
    - 如果“apn-ambr-for-uplink”/“apn-ambr-for-downlink”不高于164Kbit/s/140Kbit/s，则需要确保用户请求的上下行APN-AMBR值分别高于164Kbit/s/140Kbit/s，重新执行此步骤。
    - 如果“apn-ambr-for-uplink”/“apn-ambr-for-downlink”大于164Kbit/s/140Kbit/s，请执行[6](#ZH-CN_OPI_0277673143__cmd1763411983184706)。
6. 查看用户跟踪消息中MME收到的Create Session Response消息中的上、下行APN-AMNR数值，检查SGW-C返回的 “apn-ambr-for-uplink” / “apn-ambr-for-downlink” 是否为164Kbit/s/140Kbit/s。
    - 如果“apn-ambr-for-uplink”/“apn-ambr-for-downlink”低于164Kbit/s/140Kbit/s，请执行[8](#ZH-CN_OPI_0277673143__cmd858326600184706)。
    - 如果“apn-ambr-for-uplink”/“apn-ambr-for-downlink”为164Kbit/s/140Kbit/s，请执行[7](#ZH-CN_OPI_0277673143__cmd1263743190184706)。
7. 通过抓包工具查看 测试终端 镜像接口报文。
    - 如果上下行流量数值最高分别可到164Kbit/s/140Kbit/s，则调测结束。
    - 否则，请执行[8](#ZH-CN_OPI_0277673143__cmd858326600184706)。
8. 收集信息并寻求技术支持。
    a. 在镜像接口或服务器上开启抓包工具，执行 [7](#ZH-CN_OPI_0277673143__cmd1263743190184706) 并保存报文。
    b. 执行 **[EXP MML](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md)** 命令将当前配置数据导出为MML脚本文件并保存。
    c. 查看并收集对端设备配置及接口状态信息。
    d. 收集归纳所有信息并联系华为技术支持解决。
