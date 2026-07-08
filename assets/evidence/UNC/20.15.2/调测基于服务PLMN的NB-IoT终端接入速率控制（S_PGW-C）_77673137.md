# 调测基于服务PLMN的NB-IoT终端接入速率控制（S/PGW-C）

- [操作场景](#ZH-CN_OPI_0277673137__1.3.1)
- [必备事项](#ZH-CN_OPI_0277673137__1.3.2)
- [操作步骤](#ZH-CN_OPI_0277673137__1.3.3)

## [操作场景](#ZH-CN_OPI_0277673137)

当运营商部署基于服务PLMN的NB-IoT终端接入速率控制业务时，需对该功能进行调测。

> **说明**
> SGW-C、PGW-C

## [必备事项](#ZH-CN_OPI_0277673137)

前提条件

- 请仔细阅读[WSFD-215205 基于服务PLMN的NB-IoT终端接入速率控制特性概述（S/PGW-C）](特性概述_77673135.md)。
- 完成[激活基于服务PLMN的NB-IoT终端接入速率控制（S/PGW-C）](激活基于服务PLMN的NB-IoT终端接入速率控制（S_PGW-C）_77673136.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息查询 | IMSI | 123000123456789 | 测试终端自带 | - |
| 测试终端使用的APN | APN（APN） | apn-op | 已配置数据中获取 | 取自<br>[激活基于服务PLMN的NB-IoT终端接入速率控制（S/PGW-C）](激活基于服务PLMN的NB-IoT终端接入速率控制（S_PGW-C）_77673136.md)<br>配置的APN实例名。 |

工具

- 测试终端
- OM Portal跟踪工具

## [操作步骤](#ZH-CN_OPI_0277673137)

1. 进入 “MML命令行-UNC” 窗口。
2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查看回显中是否允许使用基于服务PLMN的NB-IoT终端接入速率控制功能。
    - 如果“ 开关”为“使能”，请执行[3](#ZH-CN_OPI_0277673137__cmd722063597184706)。
    - 如果“ 开关”为“不使能”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
3. 执行 [**LST APNPLMNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/PLMN速率控制/APN Serving PLMN速率控制/查询APN Serving PLMN速率控制配置（LST APNPLMNRATECTRL）_64343876.md) 命令查看基于APN的Serving PLMN速率控制功能是否开启。
  ```
  LST APNPLMNRATECTRL:APN="apn-op";
  ```
  ```
  ......
  ---------------------------------------
                     APN = apn-op
  Serving PLMN速率控制开关 = 使能
  (结果个数 = 1)
  ---    END
  ```
    - 如果已配置APN的“ Serving PLMN速率控制开关”为“继承”，则执行[4](#ZH-CN_OPI_0277673137__cmd125419694184706)。
    - 如果已配置APN的“ Serving PLMN速率控制开关”为“使能”，请执行[5](#ZH-CN_OPI_0277673137__cmd637368458184706)。
    - 如果已配置APN的“ Serving PLMN速率控制开关”为“不使能”，请参考[激活基于服务PLMN的NB-IoT终端接入速率控制（S/PGW-C）](激活基于服务PLMN的NB-IoT终端接入速率控制（S_PGW-C）_77673136.md)重新配置后再次执行[3](#ZH-CN_OPI_0277673137__cmd722063597184706)。
4. **可选：**执行 [**LST PLMNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/PLMN速率控制/Serving PLMN速率控制配置/查询Serving PLMN速率控制配置（LST PLMNRATECTRL）_64343890.md) 命令查看基于全局的Serving PLMN速率控制功能是否开启。
  ```
  LST PLMNRATECTRL:;
  ```
  ```
  ......
  ---------------------------------------
              Serving PLMN速率控制开关 = 使能
  (结果个数 = 1)
  ---    END
  ```
    - 如果“ Serving PLMN速率控制开关”为“使能”，请执行[5](#ZH-CN_OPI_0277673137__cmd637368458184706)。
    - 如果“ Serving PLMN速率控制开关”为“不使能”，请参考[激活基于服务PLMN的NB-IoT终端接入速率控制（S/PGW-C）](激活基于服务PLMN的NB-IoT终端接入速率控制（S_PGW-C）_77673136.md)重新配置后再次执行[4](#ZH-CN_OPI_0277673137__cmd125419694184706)。
5. **可选：**执行 [**LST DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/查询DCC模板（LST DCCTEMPLATE）_09896933.md) 命令查看配置 “ Serving PLMN速率控制” 改变时是否发送CCR消息。
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
    - 如果“ 服务PLMN控制速率改变触发重授权开关”为“使能”，请执行[6](#ZH-CN_OPI_0277673137__cmd690869232184706)。
    - 如果“ 服务PLMN控制速率改变触发重授权开关”为“不使能”，请参考[激活基于服务PLMN的NB-IoT终端接入速率控制（S/PGW-C）](激活基于服务PLMN的NB-IoT终端接入速率控制（S_PGW-C）_77673136.md)重新配置后再次执行[5](#ZH-CN_OPI_0277673137__cmd637368458184706)。
6. **可选：**执行 [**LST CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/查询话单字段模板（LST CDRFIELDTEMP）_09896893.md) 命令查看CDR话单中携带Serving PLMN Rate Control字段的功能是否开启。
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
                          ......
  (结果个数 = 1)
  ```
    - 如果“ serving-plmn-rate-control”为“携带该字段”，请执行[7](#ZH-CN_OPI_0277673137__cmd802559881184706)。
    - 如果“ serving-plmn-rate-control”为“不携带该字段”，请参考[激活基于服务PLMN的NB-IoT终端接入速率控制（S/PGW-C）](激活基于服务PLMN的NB-IoT终端接入速率控制（S_PGW-C）_77673136.md)重新配置后再次执行[6](#ZH-CN_OPI_0277673137__cmd690869232184706)。
7. **可选：**执行 [**LST OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/显示离线计费话单参数（LST OFCCDRPARA）_09896906.md) 命令查看PGW-CDR或SGW-CDR中携带Serving PLMN Rate Control字段的功能是否开启。
  ```
  LST OFCCDRPARA;
  ```
  ```
  --------------------------------------------------------------
                                                        ......
             PGW-CDR话单LoSD携带Serving PLMN Rate Control  =  使能
                                                        ......
    (结果个数 = 1)
  ---    END
  ```
    - 如果“ PGW-CDR话单LoSD携带Serving PLMN Rate Control”或“话单List of Traffic Volume携带Serving PLMN Rate Control”为“使能”，请执行[8](#ZH-CN_OPI_0277673137__cmd1544965702184706)。
    - 如果“ PGW-CDR话单LoSD携带Serving PLMN Rate Control”或“话单List of Traffic Volume携带Serving PLMN Rate Control”为“不使能”，请参考[激活基于服务PLMN的NB-IoT终端接入速率控制（S/PGW-C）](激活基于服务PLMN的NB-IoT终端接入速率控制（S_PGW-C）_77673136.md)重新配置后再次执行[7](#ZH-CN_OPI_0277673137__cmd802559881184706)。
8. 在OM Portal上 [创建用户跟踪任务](../../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md) ，在“参数配置”栏输入用户IMSI，在“消息类型”栏选择GTPC、UP、DOWN消息类型。
9. 激活用户，并跟踪该用户消息。
10. 查看接口跟踪消息，打开MME发送给SGW-C/PGW-C的Create Session Request消息，查看indication-flags信元中携带的“cpopci”是否为1，如 [图1](#ZH-CN_OPI_0277673137__fig1) 所示。
  **图1** CPOPCI信元

  <br>

  ![](调测基于服务PLMN的NB-IoT终端接入速率控制（S_PGW-C）_77673137.assets/zh-cn_image_0000002119173885_2.png)
    - 如果是，则执行 [11](#ZH-CN_OPI_0277673137__cmd107059268184706) 。
    - 如果否，请执行 [12](#ZH-CN_OPI_0277673137__step12) 。
11. 查看接口跟踪消息，打开MME发送给SGW-C/PGW-C的Create Session Request消息，查看是否携带“Serving PLMN Rate Control”信元，如 [图2](#ZH-CN_OPI_0277673137__fig2) 所示。
  **图2** Serving Plmn Rate Control信元

  <br>

  ![](调测基于服务PLMN的NB-IoT终端接入速率控制（S_PGW-C）_77673137.assets/zh-cn_image_0000002119242145_2.png)

  - 如果是，调测完成。
    - 如果否，请执行 [12](#ZH-CN_OPI_0277673137__step12) 。
12. 收集信息并寻求技术支持。
    a. 执行 **[EXP MML](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md)** 命令将当前配置数据导出为MML脚本文件并保存。
    b. 收集归纳所有信息并联系华为技术支持解决。
