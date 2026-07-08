# 配置话单可选功能（GGSN/SGW-C/PGW-C）

- [操作场景](#ZH-CN_OPI_0295923448__1.3.1)
- [必备事项](#ZH-CN_OPI_0295923448__1.3.2)
- [操作步骤](#ZH-CN_OPI_0295923448__1.3.3)
- [任务示例](#ZH-CN_OPI_0295923448__1.3.4)

## [操作场景](#ZH-CN_OPI_0295923448)

GGSN/SGW-C/PGW-C上的话单可选功能包含：

- 强制产生话单
  在系统测试时，如果GGSN/SGW-C/PGW-C上设置的话单产生条件未到，还不具备自动产生话单时，可采用命令强制产生话单。
- 进行话单缓存
  GGSN/SGW-C/PGW-C支持缓存话单的功能，在与CG组中的CG链路中断的情况下，能够将系统生成的话单暂时缓存在介质上。待CG状态正常后，再将缓存的话单重新发送到CG，从而增强了系统对异常情况的处理，最大限度的降低可能出现的风险。

> **说明**
> 适用于SGW-C、PGW-C 、GGSN 。

## [必备事项](#ZH-CN_OPI_0295923448)

前提条件

- 请仔细阅读[Ga/Gy接口离线/在线计费](../../../../../业务专题/5G Core 计费解决方案/计费解决方案概述/计费原理/Ga_Gy接口离线_在线计费_87165686.md)。
- 完成[配置到CG的数据（GGSN/SGW-C/PGW-C）](配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **FOC GENERATECDR** | 范围（RANGE） | MSISDN | 本端规划 | 强制产生话单 |
| **FOC GENERATECDR** | MSISDN（MSISDN） | **1351234568** | 本端规划 | 强制产生话单 |
| **SET OFCCDRPARA** | CCFH强制产生话单开关（CCFHCDRSW） | ENABLE | 本端规划 | 用户进行在线计费发生CCFH动作处理后，可在话单中增加CCFH标识。 |
| **SET OFCCDRPARA** | CCFH强制产生话单填充的Charging Characteristics值（CCFHCDRCC） | 0x1000 | 本端规划 | 用户进行在线计费发生CCFH动作处理后，可在话单中增加CCFH标识。 |
| **SET CDRSTRGSTATUS** | POD名称（PODNAME） | pod1 | 本端规划 | 对话单缓存目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>中的话单文件进行操作之前，必须锁定目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>。操作完成后，要解锁目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>。 |
| **SET CDRSTRGSTATUS** | 目录状态（STATUS） | LOCK | 本端规划 | 对话单缓存目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>中的话单文件进行操作之前，必须锁定目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>。操作完成后，要解锁目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>。 |
| **SET CDRSTRGSTATUS** | 话单缓存目录（DIRECTORY） | CHARGE1 | 本端规划 | 对话单缓存目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>中的话单文件进行操作之前，必须锁定目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>。操作完成后，要解锁目录<br>**CHARGE1**<br>或者<br>**CHARGE2**<br>。 |
| **SET CDRSTORAGECTRL** | 话单缓存超期天数（CDREXPIREDAY） | 3 | 本端规划 | 配置缓存话单文件的超期时间 |
| **SET CDRSTORAGECTRL** | 话单缓存超期周数（CDREXPIREWEEK） | 3 | 本端规划 | 配置缓存话单文件的超期时间 |
| **ADD OFCTEMPLATE** | 离线计费模板名（OFCTEMPLATENAME） | offlinecharge-test | 已配置数据中获取 | LastActivity计费只有在UTC时间格式下生效。<br>在<br>[配置离线计费参数（GGSN/SGW-C/PGW-C）](配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md)<br>中已通过命令<br>**ADD OFCTEMPLATE**<br>进行配置，可以使用命令<br>**LST OFCTEMPLATE**<br>查询。 |
| **ADD OFCTEMPLATE** | 话单时间格式（CDRTIMEFORMAT） | UTC | 已配置数据中获取 | LastActivity计费只有在UTC时间格式下生效。<br>在<br>[配置离线计费参数（GGSN/SGW-C/PGW-C）](配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md)<br>中已通过命令<br>**ADD OFCTEMPLATE**<br>进行配置，可以使用命令<br>**LST OFCTEMPLATE**<br>查询。 |

## [操作步骤](#ZH-CN_OPI_0295923448)

1. 配置强制产生话单。
    a. 配置强制产生话单（包括G-CDR、eG-CDR、PGW-CDR、SGW-CDR）。
      **FOC GENERATECDR**
      > **说明**
      > 该命令可基于用户（IMSI、MSISDN）强制产生话单。
    b. 配置在线计费CCFH处理时是否强制产生话单，以及强制产生话单时话单中charging characteristic字段的取值、R6版本的eG-CDR是否支持CCFH处理。
      **SET OFCCDRPARA**
2. 配置话单缓存功能。
    a. 配置锁定话单缓存目录。
      **SET CDRSTRGSTATUS**
    b. 配置缓存话单的超期时间。
      **SET CDRSTORAGECTRL**
      > **说明**
      > 当话单缓存的时间超过配置的超期时间时，系统会产生告警 **ALM-81059 超期话单缓存** ，提醒操作维护人员尽快处理话单。话单长期超期得不到处理，会导致用户计费信息丢失。
    c. 配置解锁话单缓存目录。
      **SET CDRSTRGSTATUS**

## [任务示例](#ZH-CN_OPI_0295923448)

任务描述

执行配置实现以下功能：

- 配置用户MSISDN 1351234568强制产生话单。
- 在本实例中，操作员需要在GGSN/SGW-C/PGW-C侧通过数据配置实现对话单缓存主目录 **CHARGE1** 进行手动操作。

脚本

1. 配置强制产生话单功能。
    a. 配置强制产生用户话单。
      ```
      FOC GENERATECDR: RANGE=MSISDN,MSISDN="1351234568";
      ```
    b. 配置在线计费CCFH处理时是否强制产生话单。
      ```
      SET OFCCDRPARA: CCFHCDRSW=ENABLE,CCFHCDRCC="0x1000";
      ```
2. 配置话单缓存功能。
    a. 配置手动操作话单缓存主目录 **CHARGE1** 。
      ```
      SET CDRSTRGSTATUS: PODNAME="pod1",DIRECTORY=CHARGE2,STATUS=UNLOCK;
      ```
      ```
      SET CDRSTRGSTATUS: PODNAME="pod1",DIRECTORY=CHARGE1,STATUS=LOCK;
      ```
      ```
      SET CDRSTRGSTATUS: PODNAME="pod1",DIRECTORY=CHARGE1,STATUS=UNLOCK;
      ```
    b. 手动操作完毕后，配置解锁话单缓存主目录 **CHARGE1** 。
      ```
      SET CDRSTORAGECTRL: CDREXPIREDAY=3,CDREXPIREWEEK=3;
      ```
