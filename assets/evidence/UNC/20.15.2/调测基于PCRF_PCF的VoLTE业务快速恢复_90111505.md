# 调测 基于PCRF/PCF的VoLTE业务快速恢复

- [操作场景](#ZH-CN_OPI_0000001190111505__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001190111505__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001190111505__1.3.3)

## [操作场景](#ZH-CN_OPI_0000001190111505)

当运营商部署基于PCRF/PCF的VoLTE业务快速恢复功能时，需对 UNC 的基于PCRF/PCF的VoLTE业务快速恢复功能进行调测，确保该特性正常生效。

> **说明**
> 适用于PGW-C。

## [必备事项](#ZH-CN_OPI_0000001190111505)

前提条件

- 请仔细阅读[WSFD-102203 基于PCRF/PCF的VoLTE业务快速恢复特性概述](特性概述_89991353.md)。
- 完成[激活基于PCRF/PCF的VoLTE业务快速恢复](激活基于PCRF_PCF的VoLTE业务快速恢复_43991630.md)。
- 完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息查询 | IMSI | 123000123456789 | 测试终端自带 | - |
| 测试终端使用的APN | APN | ims | 从已配置数据中获取 | 取自<br>[激活P-CSCF故障时IMS业务恢复](../WSFD-102202 P-CSCF故障时IMS业务恢复/激活P-CSCF故障时IMS业务恢复_26216211.md)<br>中配置的APN实例名。 |

工具

- 2台测试终端
- OM Portal跟踪

## [操作步骤](#ZH-CN_OPI_0000001190111505)

1. 在OM Portal启动用户跟踪，准备抓取用户信令报文。
2. 用户A进行IMS业务。
3. 查看RAR消息中PCO信元或Uplink Nas Transport消息中EPCO信元是否包含P-CSCF IPv4 Address Request或P-CSCF IPv6 Address Request及P-CSCF Re-selection support。
    - 是，请执行 [4](#ZH-CN_OPI_0000001190111505__cmd1340758396175814) 。
    - 否，请更换支持P-CSCF重选功能的 测试终端 重新执行本步骤。
4. 查看PCRF下发的RAR消息中Charging-Rule-Definition信元值或PCF下发的Npcf_SMPolicyControl_UpdateNotify Request消息中PccRule信元值。
    - 如果Flow-Information/flowinfos参数的源/目的IP对应的是P-CSCF/UE地址，并且在RAR/Npcf_SMPolicyControl_UpdateNotify Request消息中携带了AfSigProtocol信元，请执行[5](#ZH-CN_OPI_0000001190111505__cmd539313498175814)。
    - 如果Flow-Information参数的源/目的IP对应的是P-CSCF/UE地址，但在RAR/Npcf_SMPolicyControl_UpdateNotify Request消息中没有携带AfSigProtocol信元，请联系PCRF/PCF技术支持，配置正确的规则后返回[2](#ZH-CN_OPI_0000001190111505__cmd1572906276175814)。
    - 如果Flow-Information参数的源/目的IP对应的不是P-CSCF/UE地址，请执行[10](#ZH-CN_OPI_0000001190111505__cmd2030464992175814)。
5. 通知P-CSCF设备的维护人员，构造P-CSCF的故障场景。
6. 呼叫用户A，使用户A处于被叫状态。
7. 查看PCRF/PCF向 UNC 发送的RAR/PccNotifyRequest消息中是否携带PCSCF-Restoration-Indication/pcscfResIndication信元。
    - 是，请执行 [8](#ZH-CN_OPI_0000001190111505__cmd845341089175814) 。
    - 否，请执行 [10](#ZH-CN_OPI_0000001190111505__cmd2030464992175814) 。
8. 查看跟踪中 UNC 是否向UE发送Update Bearer Request消息。
    - 是，请执行 [9](#ZH-CN_OPI_0000001190111505__cmd1434854169175814) 。
    - 否，请执行 [10](#ZH-CN_OPI_0000001190111505__cmd2030464992175814) 。
9. 查看Update Bearer Request消息中，是否携带状态正常的P-CSCF地址列表。
    - 是，调测成功。
    - 否，请执行 [10](#ZH-CN_OPI_0000001190111505__cmd2030464992175814) 。
10. 收集信息并寻求技术支持。
