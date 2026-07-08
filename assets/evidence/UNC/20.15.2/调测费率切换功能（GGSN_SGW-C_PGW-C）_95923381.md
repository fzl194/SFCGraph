# 调测费率切换功能（GGSN/SGW-C/PGW-C）

- [操作场景](#ZH-CN_OPI_0295923381__1.3.1)
- [必备事项](#ZH-CN_OPI_0295923381__1.3.2)
- [操作流程](#ZH-CN_OPI_0295923381__1.3.3)
- [操作步骤](#ZH-CN_OPI_0295923381__1.3.4)

## [操作场景](#ZH-CN_OPI_0295923381)

当运营商部署了离线计费业务，需要调测GGSN/SGW-C/PGW-C的费率切换功能。

> **说明**
> 适用于SGW-C、PGW-C 、GGSN 。

## [必备事项](#ZH-CN_OPI_0295923381)

前提条件

- 请仔细阅读[Ga/Gy接口离线/在线计费](../../../../../业务专题/5G Core 计费解决方案/计费解决方案概述/计费原理/Ga_Gy接口离线_在线计费_87165686.md)。
- 完成[配置到CG的数据（GGSN/SGW-C/PGW-C）](../激活离线计费/配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md)。
- 完成[配置离线计费费率切换（GGSN/SGW-C/PGW-C）](../激活离线计费/配置离线计费费率切换（GGSN_SGW-C_PGW-C）_95923434.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD CHARGECHAR** | 计费属性名称（CCNAME） | testchgcha | 已配置数据中获取 | 该参数已在<br>[配置计费属性CC（GGSN/SGW-C/PGW-C）](../激活离线计费/配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md)<br>中通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |
| **ADD CHARGECHAR** | 本地用户计费属性（HOME） | 0x0800 | 已配置数据中获取 | 该参数已在<br>[配置计费属性CC（GGSN/SGW-C/PGW-C）](../激活离线计费/配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md)<br>中通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |
| **ADD CHARGECHAR** | 漫游用户计费属性（ROAM） | 0x0800 | 已配置数据中获取 | 该参数已在<br>[配置计费属性CC（GGSN/SGW-C/PGW-C）](../激活离线计费/配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md)<br>中通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |
| **ADD CHARGECHAR** | 拜访用户计费属性（VISIT） | 0x0800 | 已配置数据中获取 | 该参数已在<br>[配置计费属性CC（GGSN/SGW-C/PGW-C）](../激活离线计费/配置计费属性CC（GGSN_SGW-C_PGW-C）_95923501.md)<br>中通过命令<br>**ADD CHARGECHAR**<br>配置，可以使用命令<br>**LST CHARGECHAR**<br>进行查询。 |
| **ADD FESTIVAL** | 全局配置（GLOBALFLG） | CHARGE_CHARACT | 本端规划 | 配置指定日期的费率类型为节假日。 |
| **ADD FESTIVAL** | 计费属性值（CCVALUE） | 0x0800 | 本端规划 | 配置指定日期的费率类型为节假日。 |
| **ADD FESTIVAL** | 节假日月份（MONTH） | 8 | 本端规划 | 配置指定日期的费率类型为节假日。 |
| **ADD FESTIVAL** | 节假日日期（DAY） | 1 | 本端规划 | 配置指定日期的费率类型为节假日。 |
| **ADD WEEKDAY** | 全局配置（GLOBALFLG） | CHARGE_CHARACT | 本端规划 | 配置指定周日期的费率类型为工作日或周末。 |
| **ADD WEEKDAY** | 计费属性值（CCVALUE） | 0x0800 | 本端规划 | 配置指定周日期的费率类型为工作日或周末。 |
| **ADD WEEKDAY** | 周日期（DAYOFWEEK） | MONDAY<br>TUESDAY<br>WEDNESDAY<br>THURSDAY<br>FRIDAY<br>SATURDAY<br>SUNDAY | 全网规划 | 配置指定周日期的费率类型为工作日或周末。 |
| **ADD WEEKDAY** | 费率类型（TARIFFTYPE） | WORKDAY<br>WEEKEND | 全网规划 | 配置指定周日期的费率类型为工作日或周末。 |
| **ADD TARIFFGROUP** | 费率切换组名（TARIFFGRPNAME） | testtariff | 本端规划 | 配置费率切换点 |
| **ADD TARIFFGROUP** | 全局配置（GLOBALFLG） | CHARGE_CHARACT | 本端规划 | 配置费率切换点 |
| **ADD TARIFFGROUP** | Charge Characteristic值（CCVALUE） | 0x0800 | 本端规划 | 配置费率切换点 |
| **ADD TARIFFGROUP** | 费率类型（TARIFFTYPE） | FESTIVAL<br>WEEKEND<br>WORKDAY | 全网规划 | 配置费率切换点 |
| **ADD TARIFFGROUP** | 费率切换起始时间（STARTTIME） | 6:00 | 全网规划 | 配置费率切换点 |
| **ADD TARIFFGROUP** | 费率切换终止时间（ENDTIME） | 17:00 | 全网规划 | 配置费率切换点 |
| **SET GLBTARIFFGROUP** | 费率切换组名（GLBTARIFFGRP） | testtariff | 本端规划 | 绑定全局费率切换组 |
| **ADD APN** | APN名称（APN） | apn-test | 全网规划 | 配置APN。 |
| **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 每个APN只能绑定一个费率切换组。 |
| **SET APNCHARGECTRL** | 费率切换组名（TARIFFGRPNAME） | testtariff | 已配置数据中获取 | 每个APN只能绑定一个费率切换组。 |

工具

- 测试终端
- 维护终端OM Portal
- CG客户端工具

## [操作流程](#ZH-CN_OPI_0295923381)

1. 在所配置的费率切换点前激活用户。
2. 在经过费率切换点后去激活用户。
3. 检查话单中是否含有费率切换生成的话单流量容器。

## [操作步骤](#ZH-CN_OPI_0295923381)

1. 进入 “MML命令行-UNC” 窗口。 设置合适的话单时长阈值，本调测设置话单的时长阈值是15分钟。
  **SET OFCTHRESHOLD**
2. 在配置的费率切换点前激活用户，该用户计费属性是normal， 测试终端 使用“apn-test”APN接入网络，访问业务。本调测任务是在05:40激活用户。
    - 如果测试终端成功接入网络，请执行[步骤 3](#ZH-CN_OPI_0295923381__step30-1)。
    - 如果测试终端无法接入网络，请调测UNC的接入功能。
3. 用户访问业务，生成话单，06:10停止业务，去激活用户。
4. 登录CG客户端，查询此用户刚生成的话单（06:10左右）。如 [图1](#ZH-CN_OPI_0295923381__fig1) 所示，查看所生成话单中的List of Traffic Volumes字段，流量容器的关闭的原因是否是费率切换。
  **图1** CG客户端查询

  <br>

  ![](调测费率切换功能（GGSN_SGW-C_PGW-C）_95923381.assets/zh-cn_image_0295923600_2.png)

  <br>
    - 如果是，表明费率切换功能正常，本调测任务结束。
    - 如果否，则继续执行[步骤 5](#ZH-CN_OPI_0295923381__stp4)。
5. 执行 **LST APNCHARGECTRL** 命令，查看此APN下是否绑定了费率组TARIFFGROUP。
  ```
  LST APNCHARGECTRL:APN="apn-test";
  ```
  ```
  RETCODE = 0  操作成功 
 
  APN计费配置 
  -----------
                                    APN名称  =  apn-test
                                          ......
                          PGW离线计费模板名  =  offlinecharge-test
                          SGW离线计费模板名  =  offlinecharge-test
                         GGSN离线计费模板名  =  offlinecharge-test
                                           ......
                               费率切换组名  =  testtariff
                                           ......
  (结果个数 = 1)
  ---    END
  ```
    - 如果是，表示配置成功，继续执行[步骤 6](#ZH-CN_OPI_0295923381__stp5)。
    - 如果否，则参考[配置离线计费费率切换（GGSN/SGW-C/PGW-C）](../激活离线计费/配置离线计费费率切换（GGSN_SGW-C_PGW-C）_95923434.md)重新配置费率组绑定到APN上，之后再重新执行[步骤 1](#ZH-CN_OPI_0295923381__stp1)。
6. 执行 **LST TARIFFGROUP** 命令，查看费率组TariffGroup中时间、计费类型和日期类型的信息配置是否正确，主要查看06:00是否是配置的费率切换点。
  ```
  LST TARIFFGROUP:TARIFFGRPNAME="testtariff";
  ```
  ```
  ......

  -------------------------
  费率切换组名  全局配置     Charge Characteristic值    费率类型    费率切换起始时间    费率切换终止时间   Charge Characteristic掩码     Charge Characteristic 优先级 
  testtariff    计费属性         0x0800                Workday        06:00               18:00             0xFFFF                  0                      
  testtariff    计费属性         0x0800                Weekend        06:00               18:00             0xFFFF                  0                      
  testtariff    计费属性         0x0800                Festival       06:00               18:00             0xFFFF                  0            
  (结果个数 = 3)
  ---    END
  ```
    - 如果是，执行[步骤 7](#ZH-CN_OPI_0295923381__stp6)。
    - 如果否，则参考[配置离线计费费率切换（GGSN/SGW-C/PGW-C）](../激活离线计费/配置离线计费费率切换（GGSN_SGW-C_PGW-C）_95923434.md)重新配置费率组，之后再重新执行[步骤 1](#ZH-CN_OPI_0295923381__stp1)。
7. 执行 **LST WEEKDAY** 命令，查看星期表的计费类型和日期数据配置是否符合数据规划。
  > **说明**
  > 对于本调测任务实例，该步不是必须的，本调测任务实例主要关注费率切换点，对于设置了星期费率切换的任务，需要关注该步。
  ```
  LST WEEKDAY:GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800";
  ```
  ```
  ......

  -------------------------
  全局配置   计费属性值     计费属性掩码    计费属性优先级    周日期     费率类型 
  计费属性     0x0800         0xFFFF              0          Sunday       Weekend 
  计费属性     0x0800         0xFFFF              0          Monday       Workday 
  计费属性     0x0800         0xFFFF              0          Tuesday      Workday 
  计费属性     0x0800         0xFFFF              0         Wednesday     Workday 
  计费属性     0x0800         0xFFFF              0          Thursday     Workday 
  计费属性     0x0800         0xFFFF              0           Friday      Workday 
  计费属性     0x0800         0xFFFF              0          Saturday     Weekend 
  (结果个数 = 7)
  ---    END
  ```
    - 如果是，执行[步骤 8](#ZH-CN_OPI_0295923381__stp7)。
    - 如果否，则参考[配置离线计费费率切换（GGSN/SGW-C/PGW-C）](../激活离线计费/配置离线计费费率切换（GGSN_SGW-C_PGW-C）_95923434.md)重新配置星期表数据，之后再执行[步骤 1](#ZH-CN_OPI_0295923381__stp1)。
8. 执行 **LST FESTIVAL** 命令，查看节假日的计费类型和日期配置是否符合数据规划。
  > **说明**
  > 对于本调测任务实例，该步不是必须的，本调测任务实例主要关注费率切换点，对于设置了节假日费率切换的任务，需要关注该步。
  ```
  LST FESTIVAL:GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0800";
  ```
  ```
  ......

  -------------------------
                            全局配置  =  计费属性
             Charge Characteristic值  =  0x0800
            Charge Characteristic掩码 =  0xFFFF
         Charge Characteristic 优先级 =  0
                          节假日年份  =  0
                          节假日月份  =  8
                          节假日日期  =  1
  (结果个数 = 1)
  ---    END
  ```
    - 如果是，执行[步骤 9](#ZH-CN_OPI_0295923381__stp8)。
    - 如果否，则参考[配置离线计费费率切换（GGSN/SGW-C/PGW-C）](../激活离线计费/配置离线计费费率切换（GGSN_SGW-C_PGW-C）_95923434.md)重新配置节假日数据，之后再执行[步骤 1](#ZH-CN_OPI_0295923381__stp1)。
9. 执行 **LST OFCTEMPLATE** 命令，查看该APN实例绑定的OFCTemplate模板中的容器产生开关是否打开。
  ```
  LST OFCTEMPLATE:OFCTEMPLATENAME="offlinecharge-test";
  ```
  ```
  RETCODE = 0  操作成功。
  
  离线计费模板配置 
  ----------------
                           离线计费模板名  =  offlinecharge-test
                                         ......                    
                        Container RAT更新  =  ENABLE
                                  QoS更新  =  ENABLE
                         Serving Node更新  =  ENABLE
                              CGI/SAI更新  =  ENABLE
                                 ECGI更新  =  ENABLE
                                  TAI更新  =  ENABLE
                                  ULI更新  =  ENABLE
      Container Serving Node PLMN标识更新  =  ENABLE
                                   RAI更新 =  ENABLE
                                  费率切换 =  ENABLE
                                         ......         
  (结果个数 = 1)
  ---    END
  ```
    - 如果是，请执行[步骤 10](#ZH-CN_OPI_0295923381__step1829245425110)。
    - 如果否，则参考[配置离线计费费率切换（GGSN/SGW-C/PGW-C）](../激活离线计费/配置离线计费费率切换（GGSN_SGW-C_PGW-C）_95923434.md)重新配置数据，使能费率切换生成容器，之后执行[步骤 1](#ZH-CN_OPI_0295923381__stp1)。
10. 收集信息并寻求技术支持。
    a. 执行 **EXP MML** 命令将当前配置数据导出为MML脚本文件并保存。
    b. 收集并保存上述所有查询信息。
    c. 收集归纳所有信息并联系华为技术支持解决。
