# 调测基于HeNB GW的HeNB接入

- [操作场景](#ZH-CN_OPI_0166313833__1.3.1)
- [必备事项](#ZH-CN_OPI_0166313833__1.3.2)
- [操作步骤](#ZH-CN_OPI_0166313833__1.3.3)

## [操作场景](#ZH-CN_OPI_0166313833)

当运营商部署基于HeNB GW的HeNB接入时，需对UNC的基于HeNB GW的HeNB接入功能进行调测，确保本功能可以正常使用。

验证UE从Macro eNodeB（源侧）移动至HeNB（目标侧）触发S1-based Handover流程，系统查找目标HeNB GW。

> **说明**
> 适用于MME。

## [必备事项](#ZH-CN_OPI_0166313833)

前提条件

- 请仔细阅读[WSFD-205009 基于HeNB GW的HeNB接入特性概述](特性概述_66292247.md)。
- 完成[激活基于HeNB GW的HeNB接入](激活基于HeNB GW的HeNB接入_66313832.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息查询 | IMSI | 460000123456789 | 测试终端自带 | - |

工具

测试终端

## [操作步骤](#ZH-CN_OPI_0166313833)

1. 进入 “MML命令行-UNC” 窗口。
2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License配置开关是否已打开。
    - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0166313833__step811720172748)。
    - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
3. 创建指定IMSI UE的用户跟踪。
4. UE开机附着到eNodeB的小区，且除缺省承载外，未建立其他专用承载。
5. 移动UE至HeNB的小区下，触发S1-based Handover流程。
  预期结果：S1-based handover流程成功，如 [图1](#ZH-CN_OPI_0166313833__fig114041248115419) 所示。

  - Macro eNodeB向MME发送Handover Required，消息中Target ID为Home eNB ID。
    - MME向HeNB GW发送Handover Request消息且收到HeNB GW发送的Handover Request Acknowledge消息。
    - UE收到Handover Command消息，流程成功。

  **图1** S1-based Handover流程用户跟踪（样例）

  <br>

  ![](调测基于HeNB GW的HeNB接入_66313833.assets/zh-cn_image_0171539023_2.png "点击放大")

  <br>
