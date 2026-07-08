# 调测语音PCF/PCRF故障Bypass（Gx接口）

- [操作场景](#ZH-CN_OPI_0000001994763290__1.3.1)
- [对系统的影响](#ZH-CN_OPI_0000001994763290__1.3.2)
- [必备事项](#ZH-CN_OPI_0000001994763290__1.3.3)
- [操作步骤](#ZH-CN_OPI_0000001994763290__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001994763290)

本操作指导以策略接口使用Gx接口，用户激活时PCRF全部故障为例调测语音PCF/PCRF全故障Bypass功能。

## [对系统的影响](#ZH-CN_OPI_0000001994763290)

调测过程需要构建PCRF全故障场景可能会影响语音业务，请在测试床进行调测。

## [必备事项](#ZH-CN_OPI_0000001994763290)

前提条件

- 已仔细阅读[WSFD-201207 语音PCF/PCRF故障Bypass特性概述](WSFD-201207 语音PCF_PCRF故障Bypass特性概述_31784105.md)和[实现原理（N7接口）](实现原理（N7接口）_85304236.md)。
- 已按照[激活语音PCF/PCRF故障Bypass（N7接口）](激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md)完成特性激活。
- IMS域和PGW-U已完成PCRF Bypass相关配置。

数据

该操作无需准备数据。

工具

OM Portal

## [操作步骤](#ZH-CN_OPI_0000001994763290)

1. 确认是否已经按照规划配置了语音PCF/PCRF故障Bypass相关配置。
  | 检查项 | MML命令 | 期望结果 |
  | --- | --- | --- |
  | 是否按规划配置了语音专有QoS Flow/专有承载静态PCC策略 | **[LST URR](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/查询URR（LST URR）_09897161.md)**<br>**[LST QOSPROP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/查询QoS属性（LST QOSPROP）_09897166.md)**<br>**[LST PCCPOLICYGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/查询PCC策略组（LST PCCPOLICYGRP）_09897176.md)**<br>**[LST RULE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/查询规则（LST RULE）_09897204.md)**<br>**[LST RULEBINDING](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/查询用户模板和规则的绑定关系（LST RULEBINDING）_09897218.md)**<br>**[LST USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/查询用户模板（LST USERPROFILE）_09897214.md)**<br>**[LST USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/查询用户模板组（LST USRPROFGROUP）_09897222.md)**<br>**[LST UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/查询用户模板组和用户模板的绑定关系（LST UPBINDUPG）_09897232.md)**<br>**[LST APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/查询APN用户模板组绑定关系（LST APNUSRPROFG）_09897227.md)** | 已按规划配置。 |
  | 是否按规划配置了PCRF Bypass相关条件 | **[LST PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/查询PCC功能（LST PCCFUNC）_21559291.md)**<br>**[LST PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/查询PCC故障处理（LST PCCFAILACTION）_33684768.md)**<br>**[LST PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/查询PCC定时器（LST PCCTIMER）_96782686.md)**<br>**[LST PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/查询PCC模板（LST PCCTEMPLATE）_09897067.md)**<br>**[LST RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/查询返回码控制（LST RESULTCODECTRL）_09897087.md)**<br>**[LST RESULTCODEDRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/查询DRA返回码控制（LST RESULTCODEDRA）_67261101.md)**<br>**[LST PCCBYPASSCODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/查询PCC故障场景维持BYPASS状态码配置（LST PCCBYPASSCODE）_83409210.md)**<br>**[LST IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/查询语音PCF_PCRF故障Bypass场景功能（LST IMSBYPASSFUNC）_13938054.md)**<br>**[LST APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/查询APN PCC功能（LST APNPCCFUNC）_09897035.md)**<br>**[LST APNIDLETIME](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/查询APN空闲上下文定时器配置（LST APNIDLETIME）_09653829.md)**<br>**[LST APNDEACTQFPLCY](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/查询基于APN去活用户面专有QoS Flow策略（LST APNDEACTQFPLCY）_38890149.md)** | 已按规划配置。 |
  | 是否按规划配置软参DWORD519 bit5 | **[LST SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/查询SMF软件参数比特位（LST SMFSOFTPARAOFBIT）_09653189.md)** | 已按规划配置。 |
  | 是否按规划配置软参DWORD519 bit9 | **[LST SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/查询SMF软件参数比特位（LST SMFSOFTPARAOFBIT）_09653189.md)** | 已按规划配置。 |
  | 是否按规划配置软参DWORD544 bit17 | **[LST SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/查询SMF软件参数比特位（LST SMFSOFTPARAOFBIT）_09653189.md)** | 已按规划配置。 |
  | 是否按规划配置软参DWORD545 bit18 | **[LST SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/查询SMF软件参数比特位（LST SMFSOFTPARAOFBIT）_09653189.md)** | 已按规划配置。 |
    - 是：请执行[2](#ZH-CN_OPI_0000001994763290__step811720172748)。
    - 否：请参考[激活语音PCF/PCRF故障Bypass（N7接口）](激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md)完成配置。
2. 构造语音PCRF全部故障场景。
3. 在PGW-C上创建用户跟踪，开通VoLTE功能的用户A和用户B的4G终端开机注册到网络。
4. 观察用户IMS会话是否激活成功。
  预期结果：用户IMS会话是否激活成功。
    - 是：请执行[5](#ZH-CN_OPI_0000001994763290__step96704528539)。
    - 否：请执行[14](#ZH-CN_OPI_0000001994763290__step8453012171315)。
5. 观察PGW-C是否将本地静态PCC策略传递给PGW-U。
  预期结果：PGW-C通过PFCP Session Modification Request消息（Create PDR中的Activate Predefined Rules信元）把本地静态PCC策略传递给PGW-U。
  ![](调测语音PCF_PCRF故障Bypass（Gx接口）_94763290.assets/zh-cn_image_0000002010117274_2.png)
    - 是：请执行[6](#ZH-CN_OPI_0000001994763290__step82809385453)。
    - 否：请执行[14](#ZH-CN_OPI_0000001994763290__step8453012171315)。
6. 执行 **[DSP IMSBYPASSUSER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/显示进入语音PCF_PCRF故障Bypass状态的用户的IMSI列表（DSP IMSBYPASSUSER）_54762937.md)** 命令观察PGW-C上进入语音PCF/PCRF故障Bypass状态的用户的IMSI列表中是否包含用户A的IMSI。
    - 是：请执行[7](#ZH-CN_OPI_0000001994763290__step13379205812554)。
    - 否：请执行[14](#ZH-CN_OPI_0000001994763290__step8453012171315)。
7. 用户A呼叫用户B。
8. 观察用户呼叫是否成功。
  预期结果：呼叫成功。
    - 是：请执行[9](#ZH-CN_OPI_0000001994763290__step208171736178)。
    - 否：请执行[14](#ZH-CN_OPI_0000001994763290__step8453012171315)。
9. 观察用户跟踪中PGW-U是否触发QCI=1的语音专有承载创建。
  预期结果：PGW-U发送PFCP Session Report Request消息触发QCI=1的语音专有承载创建。
    - 是：请执行[10](#ZH-CN_OPI_0000001994763290__step1862614426817)。
    - 否：请执行[14](#ZH-CN_OPI_0000001994763290__step8453012171315)。
10. 用户激活30-40分钟后，观察用户是否正常在线。
  预期结果：用户正常在线，语音业务正常进行。
    - 是：请执行[11](#ZH-CN_OPI_0000001994763290__step177141531135514)。
    - 否：请执行[14](#ZH-CN_OPI_0000001994763290__step8453012171315)。
11. 修复PCRF故障，使其恢复正常。
12. 用户A和用户B结束语音呼叫。
13. 会话激活60-80分钟后，观察会话是否还存在。
  预期结果：会话被去激活。
    - 是：调测结束。
    - 否：请执行[14](#ZH-CN_OPI_0000001994763290__step8453012171315)。
14. 保存跟踪，收集信息并寻求技术支持解决。
