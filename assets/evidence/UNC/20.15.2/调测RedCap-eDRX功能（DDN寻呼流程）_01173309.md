# 调测RedCap eDRX功能（DDN寻呼流程）

- [操作场景](#ZH-CN_OPI_0000001601173309__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001601173309__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001601173309__1.3.3)
- [任务示例](#ZH-CN_OPI_0000001601173309__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001601173309)

当已经部署eDRX功能时，需要对本功能进行调测，确保功能可以正常使用。

> **说明**
> 适用于SMF。

## [必备事项](#ZH-CN_OPI_0000001601173309)

前提条件

- 请仔细阅读[WSFD-990005 支持5G eDRX功能特性概述](WSFD-990005 支持RedCap eDRX功能特性概述_50693596.md)。
- 完成[激活RedCap eDRX功能](激活RedCap eDRX功能（DDN寻呼流程）_00958549.md)。

数据

该操作无需准备数据。

工具

OM Portal跟踪

## [操作步骤](#ZH-CN_OPI_0000001601173309)

1. 进入 “MML命令行-UNC” 窗口。
2. 查询License中是否允许使用 NB-IoT eDRX模式 功能。
  [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) : LICITEM="LKV2RCEDRXSM01";
    - 如果“ 开关”为“使能”，请执行[步骤 3](#ZH-CN_OPI_0000001601173309__step16421957519)。
    - 如果“ 开关”为“不使能”，则执行 [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) 命令打开本特性对应的License配置开关。
3. 在 UNC 上创建用户跟踪。
4. 测试终端接入网络，并进行下行数据业务。激活用户，并跟踪该用户消息。
5. UPF向SMF发送消息PFCP Session Report Request上报下行数据。
  **图1** UPF向SMF发送消息PFCP Session Report Request

  <br>

  ![](调测RedCap eDRX功能（DDN寻呼流程）_01173309.assets/zh-cn_image_0000001550853624_2.png "点击放大")
6. SMF向AMF发送Namf_Communication_N1N2MessageTransfer Request消息。
    - 若携带信元extBufSupport取值True，代表SMF支持eDRX功能
  **图2** Namf_Communication_N1N2MessageTransfer Request消息中携带的extBufSupport信元

  <br>

  ![](调测RedCap eDRX功能（DDN寻呼流程）_01173309.assets/zh-cn_image_0000001550374448_2.png)
    - 若信元取值为False，请检查：SMF上基于APN粒度的eDRX开关是否配置：[**LST APNEDRXATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/eDRX模式管理/查询APN的终端接入eDRX模式属性（LST APNEDRXATTR）_32221484.md)。若配置为“INHERIT“，则检查全局粒度的配置：[**LST GLBEDRXATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/PFCP接口兼容性/设置PFCP接口兼容性参数（SET PFCPCMPT）_96243192.md)。
    - 若未携带extBufSupport信元，请检查：License是否开启：[**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)。
7. AMF向SMF发送Namf_Communication_N1N2MessageTransfer Response消息，请检查：
    - 若此消息中携带错误码504，且携带信元maxWaitingTime，则说明此时UE不在PTW，并且距离下一个PTW的差值为20。
      **图3** Namf_Communication_N1N2MessageTransfer Response返回错误码

      <br>

      ![](调测RedCap eDRX功能（DDN寻呼流程）_01173309.assets/zh-cn_image_0000001601293313_2.png)
    - 若此消息中状态码为200，说明UE刚好在寻呼窗口，不携带信元maxWaitingTime，AMF直接发起寻呼。
8. SMF向UPF发送消息PFCP Session Modification Request。
    - 此消息中应携带信元DL Buffering Duration和信元DL Buffering Packet Count，且DL Buffering Duration的时长大于等于maxWaitingTime与SMF本地下行包缓存额外时长之和。如下[图4 信元DL Buffering Duration的值](#ZH-CN_OPI_0000001601173309__fig68720283505)所示，点1处为time unit，2 seconds。点2处为时间值，20。DL Buffering Duration的取值为点1乘点2，即40，大于等于maxWaitingTime（20s）与SMF本地下行包缓存额外时长（20s）之和。
      **图4** 信元DL Buffering Duration的值

      ![](调测RedCap eDRX功能（DDN寻呼流程）_01173309.assets/zh-cn_image_0000001582251224_2.png "点击放大")
    - SMF本地下行包缓存额外时长可以通过命令[**LST APNEDRXATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/eDRX模式管理/查询APN的终端接入eDRX模式属性（LST APNEDRXATTR）_32221484.md)或者[**LST GLBEDRXATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/PFCP接口兼容性/设置PFCP接口兼容性参数（SET PFCPCMPT）_96243192.md)查询。
    - 若此消息中不携带上述信元，请检查PFCP接口兼容性参数是否配置为支持：[**LST PFCPCMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/PFCP接口兼容性/查询PFCP接口兼容性参数（LST PFCPCMPT）_96242371.md)。检查参数**BAR**若不是请配置为“SUPPORT“。
9. 等待终端寻呼成功，可以跟踪到Nsmf_PDUSession_UpdateSmContext Request和Nsmf_PDUSession_UpdateSmContext Response消息。检查SMF缓存的数据包是否转发给AMF。
    - 如果SMF缓存的数据包正常转发给AMF，则该功能调测完成。
    - 如果SMF缓存的数据包未能正常转发给AMF，请执行[步骤 10](#ZH-CN_OPI_0000001601173309__step5_new)。
10. 执行 [**DSP ACTALM**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/单体服务公共功能管理/操作维护/告警管理/活动告警/显示活动告警（DSP ACTALM）_59104140.md) 命令，查看是否存在 [ALM-81027 内部资源不足](../../../../../网络运维/故障处理/UNC告警处理/业务告警/SMF&GW-C&GGSN/ALM-81027 内部资源不足_36590880.md) 告警，且告警提示信息为“eDRX Buffering Resource Alarm”。
    - 如果产生告警，请参考[ALM-81027 内部资源不足](../../../../../网络运维/故障处理/UNC告警处理/业务告警/SMF&GW-C&GGSN/ALM-81027 内部资源不足_36590880.md)处理步骤解决。
    - 如果没有产生告警，请执行[步骤 11](#ZH-CN_OPI_0000001601173309__step6)。
11. 收集信息并寻求技术支持。
    a. 在OM Portal上创建用户跟踪任务 ，执行 [步骤 4](#ZH-CN_OPI_0000001601173309__step3) 并保存报文。
    b. 执行 **[EXP MML](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md)** 命令将当前配置数据导出为MML脚本文件并保存。
    c. 查看并收集对端设备配置及接口状态信息。
    d. 收集归纳所有信息并联系华为技术支持解决。

## [任务示例](#ZH-CN_OPI_0000001601173309)

任务描述

本操作指导用于调测在5G eDRX模式，UE不在寻呼窗口时的DDN寻呼流程。

脚本

//查询SMF上全局终端接入eDRX模式属性。

```
LST GLBEDRXATTR;
```

//查询SMF上PFCP兼容性。

```
LST PFCPCMCT;
```

//查询SMF上License是否开启。

```
LST LICENSESWITCH;
```
