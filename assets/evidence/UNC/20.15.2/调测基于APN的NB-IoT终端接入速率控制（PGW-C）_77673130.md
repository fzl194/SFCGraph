# 调测基于APN的NB-IoT终端接入速率控制（PGW-C）

- [操作场景](#ZH-CN_OPI_0277673130__1.3.1)
- [必备事项](#ZH-CN_OPI_0277673130__1.3.2)
- [操作步骤](#ZH-CN_OPI_0277673130__1.3.3)

## [操作场景](#ZH-CN_OPI_0277673130)

当运营商部署APN速率控制业务时，需对该功能进行调测。

> **说明**
> 适用于PGW-C。

## [必备事项](#ZH-CN_OPI_0277673130)

前提条件

- 请仔细阅读[WSFD-215204 基于APN的NB-IoT终端接入速率控制特性概述（PGW-C）](特性概述_77673128.md)。
- 完成[激活基于APN的NB-IoT终端接入速率控制（PGW-C）](激活基于APN的NB-IoT终端接入速率控制（PGW-C）_77673129.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息查询 | IMSI | 123000123456789 | 测试终端自带 | - |
| 测试终端使用的APN | APN（APN） | apn-op | 已配置数据中获取 | 取自<br>[激活基于APN的NB-IoT终端接入速率控制（PGW-C）](激活基于APN的NB-IoT终端接入速率控制（PGW-C）_77673129.md)<br>配置的APN实例名。 |

工具

- 测试终端
- OM Portal跟踪工具

## [操作步骤](#ZH-CN_OPI_0277673130)

1. 进入 “MML命令行-UNC” 窗口。
2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查看回显中是否允许使用APN速率控制功能。
    - 如果“ 开关”为“使能”，请执行[3](#ZH-CN_OPI_0277673130__cmd610952254184706)。
    - 如果“ 开关”为“不使能”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
3. 执行 [**LST APNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/查询APN速率控制配置（LST APNRATECTRL）_64343877.md) 命令查看基于APN的NB-IoT速率控制功能是否开启。
  ```
  LST APNRATECTRL:APN="apn-op";
  ```
  ```
  ......
  -------------------------
            APN  =  apn-op
     下行时间单位  =  小时
     上行时间单位  =  小时
     最大下行速率  =  100
     最大上行速率  =  50
     APN速率控制开关  =  使能
  (结果个数 = 1)
  ---    END
  ```
    - 如果已配置APN的“APN速率控制开关”为“使能”，请执行[4](#ZH-CN_OPI_0277673130__cmd1564752774184706)。
    - 如果已配置APN的“APN速率控制开关”为“不使能”，请参考[激活基于APN的NB-IoT终端接入速率控制（PGW-C）](激活基于APN的NB-IoT终端接入速率控制（PGW-C）_77673129.md)重新配置后再次执行[3](#ZH-CN_OPI_0277673130__cmd610952254184706)。
4. **可选：**执行 [**LST DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/查询DCC模板（LST DCCTEMPLATE）_09896933.md) 命令查看配置APN Rate Control改变时是否发送CCR消息。
  ```
  LST DCCTEMPLATE:DCCTMPLTNAME="dcctemplate";
  ```
  ```
  ......
  ---------------------------------------
                                        ......
             服务PLMN控制速率改变触发重授权开关  =  使能
                 APN控制速率改变触发重授权开关  =  使能
  (结果个数 = 1)
  ---    END
  ```
    - 如果“APN控制速率改变触发重授权开关”为“使能”，请执行[5](#ZH-CN_OPI_0277673130__cmd339617831184706)。
    - 如果“APN控制速率改变触发重授权开关”为“不使能”，请参考[激活基于APN的NB-IoT终端接入速率控制（PGW-C）](激活基于APN的NB-IoT终端接入速率控制（PGW-C）_77673129.md)重新配置后再次执行[4](#ZH-CN_OPI_0277673130__cmd1564752774184706)。
5. **可选：**执行 [**LST CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/查询话单字段模板（LST CDRFIELDTEMP）_09896893.md) 命令查看CDR话单中携带APN Rate Control字段的功能是否开启。
  ```
  LST CDRFIELDTEMP:TEMPLATENAME="cdrfieldtemp";
  ```
  ```
  ......
  -------------------------
                           ......
           apn-rate-control  =  不携带该字段
  sgi-ptp-tunnelling-method  =  不携带该字段
  serving-plmn-rate-control  =  不携带该字段
  (结果个数 = 1)
  ```
    - 如果“apn-rate-control”为“携带该字段”，请执行[6](#ZH-CN_OPI_0277673130__cmd961390220184706)。
    - 如果“apn-rate-control”为“不携带该字段”，请参考[激活基于APN的NB-IoT终端接入速率控制（PGW-C）](激活基于APN的NB-IoT终端接入速率控制（PGW-C）_77673129.md)重新配置后再次执行[5](#ZH-CN_OPI_0277673130__cmd339617831184706)。
6. **可选：**执行 [**LST OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/显示离线计费话单参数（LST OFCCDRPARA）_09896906.md) 命令查看PGW-CDR中携带APN Rate Control字段的功能是否开启。
  ```
  LST OFCCDRPARA:;
  ```
  ```
  ......
  --------------------------------------------------------------
                                                    ......
             PGW-CDR话单LoSD携带Serving PLMN Rate Control  =  不使能
                    PGW-CDR话单的LoSD携带APN Rate Control  =  使能
                                                    ......
  ---    END
  ```
    - 如果“PGW-CDR话单的LoSD携带APN Rate Control”为“使能”，请执行[7](#ZH-CN_OPI_0277673130__cmd1967962205184706)。
    - 如果“PGW-CDR话单的LoSD携带APN Rate Control”为“不使能”，请参考[激活基于APN的NB-IoT终端接入速率控制（PGW-C）](激活基于APN的NB-IoT终端接入速率控制（PGW-C）_77673129.md)重新配置后再次执行[6](#ZH-CN_OPI_0277673130__cmd961390220184706)。
7. 在OM Portal上 [创建用户跟踪任务](../../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) ，在“参数配置”栏输入用户IMSI，在“消息类型”栏选择GTPC、UP、DOWN消息类型。
8. 激活用户，并跟踪该用户消息。
9. 查看接口跟踪消息，打开MME发送给PGW-C的Create Session Request消息，查看消息的PCO信元是否携带“apn-rate-control-support-indicator”，如 [图1](#ZH-CN_OPI_0277673130__fig1) 所示。
  **图1** Create Session Request消息

  <br>

  ![](调测基于APN的NB-IoT终端接入速率控制（PGW-C）_77673130.assets/zh-cn_image_0000002119179077_2.png)
    - 如果是，请执行 [10](#ZH-CN_OPI_0277673130__cmd1015798349184706) 。
    - 如果否，请执行 [11](#ZH-CN_OPI_0277673130__step14716341931) 。
10. 查看接口跟踪消息，打开PGW-C发送给MME的Create Session Response消息，查看消息的PCO信元是否携带“apn-rate-control-parameters”，如 [图2](#ZH-CN_OPI_0277673130__fig2) 所示。
  **图2** Create Session Response消息

  <br>

  ![](调测基于APN的NB-IoT终端接入速率控制（PGW-C）_77673130.assets/zh-cn_image_0000002083779230_2.png)
    - 如果是，调测完成。
    - 如果否，请执行 [11](#ZH-CN_OPI_0277673130__step14716341931) 。
11. 收集信息并寻求技术支持。
    a. 执行 **[EXP MML](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md)** 命令将当前配置数据导出为MML脚本文件并保存。
    b. 收集归纳所有信息并联系华为技术支持解决。
