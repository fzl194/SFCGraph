# 激活SmartPhone控制基础功能

- [操作场景](#ZH-CN_OPI_0185152746__1.3.1)
- [必备事项](#ZH-CN_OPI_0185152746__1.3.2)
- [操作步骤](#ZH-CN_OPI_0185152746__1.3.3)
- [任务示例](#ZH-CN_OPI_0185152746__1.3.4)

## [操作场景](#ZH-CN_OPI_0185152746)

本操作指导介绍在运行网络中激活Smartphone控制基础功能的操作过程。

Smartphone控制基础功能包括基于信令行为控制、基于终端类型控制和SmartPaging三个部分：

- 基于信令行为的Smartphone控制功能
  通过分析信令识别Smartphone，系统利用禁止使用Direct Tunnel和禁止启用去激活空闲PDP功能的机制来节省信令资源。
- 基于终端类型的Smartphone控制功能
  通过识别Smartphone终端类型，系统针对不同的智能终端实行差异化策略，利用禁止某一类智能终端使用Direct Tunnel功能的机制来节省信令资源。
- SmartPaging功能
  SGSN解析下行消息中的DSCP(Differentiated Services Code Point)字段，并根据下行数据包的优先级以及设备本身的拥塞情况决定是否下发Paging消息，根据实际情况丢弃低优先级的下行包，确保高优先级的业务正常处理。

> **说明**
> 适用于 SGSN 。

## [必备事项](#ZH-CN_OPI_0185152746)

前提条件

- 请仔细阅读[WSFD-206005 Smartphone控制基础功能特性概述](特性概述_85628479.md)。
- 完成协议版本为R4的配置。
- 对端网元已开启协议版本R4或可以携带PDP Status信元的开关。
- 完成加载License。

数据

| 类别 | **参数名称** | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET SMARTCFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/Smartphone控制基础功能/设置智能用户功能（SET SMARTCFG）_26145750.md) | 是否启用SMART用户识别功能（SMARTSW） | YES | 本端规划 | 开启SmartPhone用户识别功能。 |
| [**SET SMARTCFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/Smartphone控制基础功能/设置智能用户功能（SET SMARTCFG）_26145750.md) | 识别SMART用户的SERVICE REQUEST门限（times/h）（SERVREQTHRESHOLD） | 10 | 本端规划 | 开启SmartPhone用户识别功能。 |
| [**SET SMARTCFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/Smartphone控制基础功能/设置智能用户功能（SET SMARTCFG）_26145750.md) | SMART用户是否禁止启用DT功能（DTSW） | YES | 本端规划 | 开启SmartPhone用户识别功能。 |
| [**SET SMARTCFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/Smartphone控制基础功能/设置智能用户功能（SET SMARTCFG）_26145750.md) | SMART用户是否禁止启用去活非活动PDP功能（DEAPDPSW） | YES | 本端规划 | 开启SmartPhone用户识别功能。 |
| [**ADD IMEILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md) | 设备型号核准号码（IMEITAC） | 46001111 | 本端规划 | 配置IMEI库。 |
| [**ADD IMEILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md) | 终端类型（UETYPE） | BLACKBERRY | 本端规划 | 配置IMEI库。 |
| [**ADD SMARTDT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/基于终端类型的DT限制/增加基于终端类型的DT限制(ADD SMARTDT)_26145738.md) | 终端类型（UETYPE） | BLACKBERRY | 本端规划 | 禁止指定终端类型的Smartphone使用Direct Tunnel功能。 |
| [**ADD SMARTDT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/基于终端类型的DT限制/增加基于终端类型的DT限制(ADD SMARTDT)_26145738.md) | DT限制开关（DTLIMIT） | ON | 本端规划 | 禁止指定终端类型的Smartphone使用Direct Tunnel功能。 |
| [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2SPCB02 | 全网规划 | 打开Smartphone控制功能的License开关。 |
| [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 全网规划 | 打开Smartphone控制功能的License开关。 |
| [**ADD LOWPRIDSCP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/低优先级DSCP/增加低优先级业务DSCP(ADD LOWPRIDSCP)_26145510.md) | DSCP起始值（BEGINDSCP） | 0 | 全网规划 | 开启低优先级业务识别功能。 |
| [**ADD LOWPRIDSCP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/低优先级DSCP/增加低优先级业务DSCP(ADD LOWPRIDSCP)_26145510.md) | DSCP结束值（ENDDSCP） | 10 | 全网规划 | 开启低优先级业务识别功能。 |
| [**ADD GGSNCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN属性/增加GGSN属性配置信息(ADD GGSNCHARACT)_72225613.md) | 对端设备范围（RANGE） | SPECIAL_GGSN | 本端规划 | 配置GGSN支持SmartPaging功能。 |
| [**ADD GGSNCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN属性/增加GGSN属性配置信息(ADD GGSNCHARACT)_72225613.md) | IP地址类型（IPT） | IPV4 | 全网规划 | 配置GGSN支持SmartPaging功能。 |
| [**ADD GGSNCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN属性/增加GGSN属性配置信息(ADD GGSNCHARACT)_72225613.md) | GGSN的信令面IP地址（GGSNIPV4） | 10.2.3.12 | 全网规划 | 配置GGSN支持SmartPaging功能。 |
| [**ADD GGSNCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN属性/增加GGSN属性配置信息(ADD GGSNCHARACT)_72225613.md) | 掩码（MASKV4） | 255.255.255.255 | 全网规划 | 配置GGSN支持SmartPaging功能。 |
| [**ADD GGSNCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN属性/增加GGSN属性配置信息(ADD GGSNCHARACT)_72225613.md) | GGSN是否支持Smart Paging（SMARTPAGING） | YES | 与对端协商 | 配置GGSN支持SmartPaging功能。 |

## [操作步骤](#ZH-CN_OPI_0185152746)

- 激活基于信令行为的Smartphone控制功能。
    1. 进入 “MML命令行-UNC” 窗口。
    2. 开启SmartPhone用户识别功能。
      [**SET SMARTCFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/Smartphone控制基础功能/设置智能用户功能（SET SMARTCFG）_26145750.md)
      > **说明**
      > - 如果不配置参数“SERVREQTHRESHOLD”（识别SMART用户的SERVICE REQUEST门限），则该参数自动取上一次执行命令时配置的参数值。例如，上一次执行该命令时，参数“SERVREQTHRESHOLD”配置为11次/小时，如果此次执行该命令时，不配置参数“SERVREQTHRESHOLD”，则该参数自动取值为11次/小时。另外，参数“SERVREQTHRESHOLD”的系统默认值为10次/小时。
      > - 参数“SMARTSW”（是否启用SMART用户识别功能）固定选择“YES”。
    3. 打开基于信令行为的SmartPhone控制功能的License开关。
      [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
- 激活基于终端类型的Smartphone控制功能。
    1. 进入 “MML命令行-UNC” 窗口。
    2. 配置识别终端类型的数据库。
          - 可选：配置IMEI库。
            [**ADD IMEILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md)
          - 可选：配置APN NI库。
            [**ADD APNNILIB**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/终端类型识别/APNNI库管理/增加APNNI库记录（ADD APNNILIB）_26145736.md)
      > **说明**
      > IMEI库和APN NI库两者可以同时配置，优先级从高到低依次为：签约APN，IMEI，请求APN。
    3. 禁止指定终端类型的Smartphone使用Direct Tunnel功能。
      [**ADD SMARTDT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/基于终端类型的DT限制/增加基于终端类型的DT限制(ADD SMARTDT)_26145738.md)
      > **说明**
      > 参数 “DTLIMIT” （DT限制开关）固定选择 “ON” 。
    4. 打开基于终端类型的Smartphone控制功能的License开关。
      [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
- 激活SmartPaging功能。
    1. 进入 “MML命令行-UNC” 窗口。
    2. 开启低优先级业务识别功能。
      [**ADD LOWPRIDSCP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/低优先级DSCP/增加低优先级业务DSCP(ADD LOWPRIDSCP)_26145510.md)
    3. 配置GGSN支持SmartPaging功能。
      [**ADD GGSNCHARACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN属性/增加GGSN属性配置信息(ADD GGSNCHARACT)_72225613.md)
      > **说明**
      > - 参数“IPT”（IP地址类型）选择“IPV4”。
      > - 参数“SMARTPAGING”（GGSN是否支持Smart Paging）选择“YES”（是）。
    4. 打开SmartPaging功能的License开关。
      [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0185152746)

任务描述

- 任务1：激活基于信令行为的Smartphone控制功能。禁止黑莓手机使用Direct Tunnel功能，并且禁止所有智能手机去激活非活动PDP。

- 任务2：激活基于终端类型的Smartphone控制功能。禁止黑莓手机使用Direct Tunnel功能，并且禁止所有智能手机去激活非活动PDP。
- 任务3：激活地址为“10.2.3.12”的GGSN支持SmartPaging功能，并开启低级别业务识别功能。

> **说明**
> 以下脚本中设置IMEI号码为46001111的手机为黑莓手机，此设置仅为举例，现场配置时请根据实际情况选择参数值配置。

脚本

- 脚本1：
  //开启Smartphone用户识别功能。

  ```
  SET SMARTCFG: SMARTSW=YES, SERVREQTHRESHOLD=10, DTSW=YES, DEAPDPSW=YES;
  ```
- 脚本2：
  //配置IMEI库。

  ```
  ADD IMEILIB: IMEITAC="46001111", UETYPE=BLACKBERRY;
  ```
  //禁止指定终端类型的Smartphone使用Direct Tunnel功能。

  ```
  ADD SMARTDT: UETYPE=BLACKBERRY, DTLIMIT=ON;
  ```
  //打开License配置开关。

  ```
  SET LICENSESWITCH: LICITEM="LKV2SPCB02", SWITCH=ENABLE;
  ```
- 脚本3：
  //开启低级别业务识别功能。

  ```
  ADD LOWPRIDSCP: BEGINDSCP=0, ENDDSCP=10;
  ```
  //配置GGSN支持SmartPaging功能。

  ```
  ADD GGSNCHARACT: RANGE=SPECIAL_GGSN, IPT=IPV4, GGSNIPV4="10.2.3.12", MASKV4="255.255.255.255", SMARTPAGING=YES;
  ```
  //打开License配置开关。

  ```
  SET LICENSESWITCH: LICITEM="LKV2SPCB02", SWITCH=ENABLE;
  ```
