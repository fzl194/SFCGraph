# 调测EPS Fallback

- [操作场景](#ZH-CN_OPI_0182220358__1.3.1)
- [必备事项](#ZH-CN_OPI_0182220358__1.3.2)
- [操作步骤](#ZH-CN_OPI_0182220358__1.3.3)

## [操作场景](#ZH-CN_OPI_0182220358)

EPS Fallback（Evolved Packet System Fallback）是指在无线网络没有部署VoNR（Voice over NR，NR网络语音业务）的情况下，当UE从5G网络接入时，允许其在IMS域注册，但是当UE要进行通话时，会通过切换或者重定向的方式回落到4G网络通过VoLTE进行通话。它是VoLTE向VoNR演进的过渡语音方案。

> **说明**
> 适用于AMF、SMF。

## [必备事项](#ZH-CN_OPI_0182220358)

前提条件

- 请仔细阅读[WSFD-102702 EPS Fallback特性概述](特性概述_60374917.md)。
- 已完成[激活EPS Fallback](激活EPS Fallback_76175590.md)。

数据

该操作无需准备数据。

工具

- 测试终端
- OM Portal

## [操作步骤](#ZH-CN_OPI_0182220358)

1. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 查询WSFD-102702 EPS Fallback功能对应的License配置开关是否打开。
    - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0182220358__cmd1098161310282)。
    - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
2. 验证UE语音EPS Fallback可实现。
    a. 在MME、AMF的OM Portal上创建用户跟踪任务。5G用户开机注册。
    b. 查询用户上下文的用户状态信息。
      进入 “MML命令行-UNC” 窗口。 执行命令 **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** 查询用户在5G网络下的PDU会话。如果为IMS的PDU会话，则 “APN或者DNN” 为 “ ims” 。
      预期结果：用户在5G网络有数据PDU会话和IMS的PDU会话。
    c. 查看AMF上用户跟踪。
      预期结果：
          - 用户附着到网络，AMF向UE返回Registration Accept消息中携带5GS network feature support信元，并对IMS voice PS session over 3GPP access indicator置位。
            ![](调测EPS Fallback_82220358.assets/zh-cn_image_0000001089078936_2.png)
          - UE发起会话建立。PDU Session Establishment Accept消息中的Extended protocol configuration options信元包含P-CSCF地址或者地址列表。
            ![](调测EPS Fallback_82220358.assets/zh-cn_image_0000001136149873_2.png)
          - 在5GC触发5QI=1的IMS语音数据流。AMF向NG RAN发送PDU Session Resource Modify Request消息。
            fiveQI：指示业务质量的索引，5QI对应4G的QCI，此处取值为1。
            ![](调测EPS Fallback_82220358.assets/zh-cn_image_0000001089432082_2.png)
          - NG RAN基站拒绝语音QoS Flow，向AMF发送PDU Session Resource Modify Response消息，并携带IMS Voice EPS Fallback or RAT Fallback Triggered原因值。
            ![](调测EPS Fallback_82220358.assets/zh-cn_image_0000001136770755_2.png)
          - NG RAN基站触发5GC->EPC切换流程。切换流程调测参见[调测5G SA到LTE网络间切换](../../../../业务专题/5G Core 4_5G互操作解决方案/调测指导/调测5G SA到LTE网络间切换_01_10043.md)。
    d. 查看MME上用户跟踪。
      预期结果：
          - 完成切换后UE触发TAU位置更新流程，SMF+PGW-C触发PDN连接修改流程，向eNodeB请求建立QCI=1专有承载，MME向E-UTRAN发送Bearer Setup Request。
    e. EPC网络QCI=1承载建立后，IMS流程执行完毕。
      预期结果：被叫响铃，接通被叫。
    f. 语音业务执行成功。
      进入 “MML命令行-UNC” 窗口。 执行命令 **[DSP PDUSESSION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)** （参数DSPINFOTYPE为DETAILED，WLNETWKTYPE为NW2G3G4G），查询用户在4G网络下的PDN连接。
      预期结果：用户在4G网络有VoLTE语音专载。
    g. 如果 [2.b](#ZH-CN_OPI_0182220358__substep4123184655110) ~ [2.f](#ZH-CN_OPI_0182220358__substep71255433249) 查看非预期结果，先参考 [激活EPS Fallback](激活EPS Fallback_76175590.md) 排查配置是否正确，若配置正确则执行 [3](#ZH-CN_OPI_0182220358__step2091112885113) 。
3. 收集信息并寻求技术支持。
    a. 进入 “MML命令行-UNC” 窗口。 执行命令 [**EXP MML**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md) 将当前配置数据导出为MML脚本文件并保存。
    b. 收集并保存上述所有查询信息。
    c. 收集归纳所有信息并联系华为技术支持解决。
