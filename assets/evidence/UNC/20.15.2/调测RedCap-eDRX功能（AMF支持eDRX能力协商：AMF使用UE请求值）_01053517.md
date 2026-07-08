# 调测RedCap eDRX功能（AMF支持eDRX能力协商：AMF使用UE请求值）

- [操作场景](#ZH-CN_OPI_0000001601053517__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001601053517__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001601053517__1.3.3)

## [操作场景](#ZH-CN_OPI_0000001601053517)

当已经部署eDRX使用UE请求值功能时，需要对本功能进行调测，确保功能可以正常使用。

> **说明**
> 适用于AMF。

## [必备事项](#ZH-CN_OPI_0000001601053517)

前提条件

- 请仔细阅读[WSFD-990005 支持5G eDRX功能特性概述](WSFD-990005 支持RedCap eDRX功能特性概述_50693596.md)。
- 完成激活5G eDRX功能。

数据

该操作无需准备数据。

工具

OM Portal跟踪

## [操作步骤](#ZH-CN_OPI_0000001601053517)

1. 进入 “MML命令行-UNC” 窗口。
2. 在 UNC 上创建用户跟踪。
3. UE开机并向核心网发起注册，UE在Registration Request消息中携带了“requested-extended-DRX-parameters“信元，如下 [图1 Registration Request中携带requested-extended-DRX-parameters信元](#ZH-CN_OPI_0000001601053517__fig7629357715) 所示。
  **图1** Registration Request中携带requested-extended-DRX-parameters信元

  <br>

  ![](调测RedCap eDRX功能（AMF支持eDRX能力协商：AMF使用UE请求值）_01053517.assets/zh-cn_image_0000001601173345_2.png "点击放大")
4. AMF根据本地配置协商以后，给UE回复Registration Accept消息，携带“negotiated-extended-DRX-parameters“信元，下发协商以后的结果，如下 [图2 Registration Accept中携带negotiated-extended-DRX-parameters信元](#ZH-CN_OPI_0000001601053517__fig162881025132516) 所示。
  **图2** Registration Accept中携带negotiated-extended-DRX-parameters信元

  <br>

  ![](调测RedCap eDRX功能（AMF支持eDRX能力协商：AMF使用UE请求值）_01053517.assets/zh-cn_image_0000001550693640_2.png "点击放大")
  NR模式接入5G核心网场景下，PTW的值以“extended-paging-time-window“为准。如上图所示，UE请求的eDRX周期与下发的相同，但是PTW值“31“协商后变为“14“。这是因为UE请求的PTW值大于eDRX周期。因此在AMF上参数校正开关开启的情况下，会将PTW矫正至不大于eDRX周期的值：可通过命令 [**LST NGM2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/M2M控制参数/查询5G M2M控制参数（LST NGM2MCTRL）_34572336.md) 的参数 **UEEDRXCOSW** 检查。
5. 若步骤 [3](#ZH-CN_OPI_0000001601053517__cmd1249366922) 中未携带信元requested-extended-DRX-parameters，则代表UE不支持或者不使能eDRX能力。请检查：UE自身情况。
6. 若步骤 [4](#ZH-CN_OPI_0000001601053517__cmd22673298412) 中未携带信元negotiated-extended-DRX-parameters，则代表AMF协商结果不支持eDRX。请检查：
    - AMF上的eDRX开关是否开启：[**LST NGM2MPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/5G M2M策略参数配置/查询5G M2M策略参数（LST NGM2MPLCY）_34412860.md)。
    - UE请求值中的PTW是否大于eDRX Cycle。若大于，AMF上需要开启参数校正，将PTW矫正至不大于eDRX周期的值，否则AMF无法给用户下发eDRX周期和PTW。可通过命令[**LST NGM2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/M2M控制参数/查询5G M2M控制参数（LST NGM2MCTRL）_34572336.md)查看，配置[**SET NGM2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/M2M控制参数/设置5G M2M控制参数（SET NGM2MCTRL）_84932189.md)的参数**UEEDRXCOSW**为打开。
7. 收集信息并寻求技术支持。
    a. 在OM Portal上创建用户跟踪任务 ，执行 [步骤 3](#ZH-CN_OPI_0000001601053517__step1493161028) 并保存报文。
    b. 执行 **[EXP MML](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md)** 命令将当前配置数据导出为MML脚本文件并保存。
    c. 查看并收集对端设备配置及接口状态信息。
    d. 收集归纳所有信息并联系华为技术支持解决。
