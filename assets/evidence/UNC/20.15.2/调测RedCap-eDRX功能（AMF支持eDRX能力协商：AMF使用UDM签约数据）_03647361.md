# 调测RedCap eDRX功能（AMF支持eDRX能力协商：AMF使用UDM签约数据）

- [操作场景](#ZH-CN_OPI_0000001603647361__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001603647361__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001603647361__1.3.3)

## [操作场景](#ZH-CN_OPI_0000001603647361)

当已经部署eDRX使用UDM签约数据功能时，需要对本功能进行调测，确保功能可以正常使用。

> **说明**
> 适用于AMF。

## [必备事项](#ZH-CN_OPI_0000001603647361)

前提条件

- 请仔细阅读[WSFD-990005 支持5G eDRX功能特性概述](WSFD-990005 支持RedCap eDRX功能特性概述_50693596.md)。
- 完成激活5G eDRX功能。

数据

该操作无需准备数据。

工具

OM Portal跟踪

## [操作步骤](#ZH-CN_OPI_0000001603647361)

1. 进入 “MML命令行-UNC” 窗口。
2. 在 UNC 上创建用户跟踪。
3. UE开机并向核心网发起注册，UE向UDM获取签约数据，UDM通过消息Nudm_SDM_GetMultipleDataSets Response，携带信元edrxParametersList和ptwParametersList，如下 [图1 Registration Request中携带requested-extended-DRX-parameters信元](#ZH-CN_OPI_0000001603647361__fig7629357715) 所示。
  **图1** Nudm_SDM_GetMultipleDataSets Response中携带eDRX周期和PTW

  <br>

  ![](调测RedCap eDRX功能（AMF支持eDRX能力协商：AMF使用UDM签约数据）_03647361.assets/zh-cn_image_0000001554140960_2.png)
4. AMF根据本地配置协商以后，给UE回复Registration Accept消息，携带“negotiated-extended-DRX-parameters“信元，下发协商以后的结果，如下 [图2 Registration Accept中携带negotiated-extended-DRX-parameters信元](#ZH-CN_OPI_0000001603647361__fig162881025132516) 所示。
  **图2** Registration Accept中携带negotiated-extended-DRX-parameters信元

  <br>

  ![](调测RedCap eDRX功能（AMF支持eDRX能力协商：AMF使用UDM签约数据）_03647361.assets/zh-cn_image_0000001553487454_2.png "点击放大")
  NR模式接入5G核心网场景下，PTW的值以 **“Extended Paging Time Window“** 为准。以图示为例，AMF下发的eDRX周期和PTW与步骤 [3](#ZH-CN_OPI_0000001603647361__step1493161028) 中一致。取值换算方式请参考3GPP 协议24.008和38.304。UDM配置签约参数时，需要使eDRX周期大于等于PTW，否则AMF无法使用UDM签约数据。
5. 若步骤 [4](#ZH-CN_OPI_0000001603647361__cmd22673298412) 中未携带信元negotiated-extended-DRX-parameters，则代表AMF协商结果不支持eDRX。请检查：
    - AMF上的eDRX开关是否开启：[**LST NGM2MPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/5G M2M策略参数配置/查询5G M2M策略参数（LST NGM2MPLCY）_34412860.md)。
    - UDM签约数据的PTW是否大于eDRX Cycle。若大于，AMF上需要开启参数校正，将PTW矫正至不大于eDRX周期的值，否则AMF无法给用户下发eDRX周期和PTW。可通过命令[**LST NGM2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/M2M控制参数/查询5G M2M控制参数（LST NGM2MCTRL）_34572336.md)查看，配置[**SET NGM2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G M2M管理/M2M控制参数/设置5G M2M控制参数（SET NGM2MCTRL）_84932189.md)的参数**UEEDRXCOSW**为打开。
6. 若尝试以上问题定位方式仍然无法成功协商，请联系华为技术支持。
