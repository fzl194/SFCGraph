# 激活 本地QOS控制 （适用于SGW-C/PGW-C）

- [操作场景](#ZH-CN_OPI_0228258573__1.3.1)
- [必备事项](#ZH-CN_OPI_0228258573__1.3.2)
- [操作流程](#ZH-CN_OPI_0228258573__1.3.3)
- [操作步骤](#ZH-CN_OPI_0228258573__1.3.4)
- [任务示例](#ZH-CN_OPI_0228258573__1.3.5)

## [操作场景](#ZH-CN_OPI_0228258573)

运营商根据 UNC 本地配置的QoS参数对用户数据进行控制。

> **说明**
> 适用于SGW-C、PGW-C。

## [必备事项](#ZH-CN_OPI_0228258573)

前提条件

- 请仔细阅读 [WSFD-109203 本地QOS控制特性概述](特性概述_28258571.md) 。
- 完成配置普通APN [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) 。
- 完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)<br>[设置License项的开关（SET LICENSESWITCH）](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | LICITEM | LKV3W9LQOS12 | 本端规划 | 配置License配置开关 |
| [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)<br>[设置License项的开关（SET LICENSESWITCH）](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | SWITCH | ENABLE | 本端规划 | 配置License配置开关 |
| [**ADD EPSSUBQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md) | QCI（QCI） | 1 | 本端规划 | 配置4G用户的签约QoS属性。 |
| [**ADD EPSSUBQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md) | ARPPL（ARP的优先级别） | 2 | 本端规划 | 配置4G用户的签约QoS属性。 |
| [**ADD EPSSUBQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md) | AMBRDL（下行APN AMBRR） | 1111 | 本端规划 | 配置4G用户的签约QoS属性。 |
| [**ADD EPSSUBQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md) | AMBRUL（上行APN AMBRR） | 2222 | 本端规划 | 配置4G用户的签约QoS属性。 |
| [**ADD EPSSUBQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md) | SUBQOSINDEX（用户QOS索引） | 200 | 本端规划 | 配置4G用户的签约QoS属性。 |
| [**SET QOSGLOBAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置全局QoS配置（SET QOSGLOBAL）_09652976.md) | QOSPROFILENAME（QoS Profile名） | qos1 | 本端规划 | 配置全局的QoS信息。 |
| [**SET QOSGLOBAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置全局QoS配置（SET QOSGLOBAL）_09652976.md) | 绑定EPS用户QoS（BINDEPSSUBQOS） | ENABLE（使能） | 本端规划 | 配置全局的QoS信息。 |
| [**SET QOSGLOBAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置全局QoS配置（SET QOSGLOBAL）_09652976.md) | EPS用户QoS索引（EPSSUBQOS） | 200 | 本端规划 | 配置全局的QoS信息。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | QOSCLASSID（QCI值） | 1 | 本端规划 | 配置EPS本地缺省QoS参数，用于纠错。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | ARPVALUE（ARP值） | 1 | 本端规划 | 配置EPS本地缺省QoS参数，用于纠错。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | GBRDL（下行保证带宽） | 200bit/s | 本端规划 | 配置EPS本地缺省QoS参数，用于纠错。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | GBRUL（上行保证带宽） | 230bit/s | 本端规划 | 配置EPS本地缺省QoS参数，用于纠错。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | MBRDL（下行最大带宽） | 300bit/s | 本端规划 | 配置EPS本地缺省QoS参数，用于纠错。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | MBRUL（上行最大带宽） | 300bit/s | 本端规划 | 配置EPS本地缺省QoS参数，用于纠错。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | APNAMBRDL（下行APN AMBR） | 1000bit/s | 本端规划 | 配置EPS本地缺省QoS参数，用于纠错。 |
| [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | APNAMBRUL（上行APN AMBR） | 1000bit/s | 本端规划 | 配置EPS本地缺省QoS参数，用于纠错。 |
| [**SET QCI2ARP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QCI到ARP映射/设置标准QCI到ARP的映射规则（SET QCI2ARP）_09652269.md) | QCI（标准QCI） | 1 | 本端规划 | 可选：配置ARP和QCI的对应关系 |
| [**SET QCI2ARP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QCI到ARP映射/设置标准QCI到ARP的映射规则（SET QCI2ARP）_09652269.md) | ARPPCI（ARP的可抢占能力） | 0 | 本端规划 | 可选：配置ARP和QCI的对应关系 |
| [**SET QCI2ARP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QCI到ARP映射/设置标准QCI到ARP的映射规则（SET QCI2ARP）_09652269.md) | ARPPL（ARP的优先级别） | 1 | 本端规划 | 可选：配置ARP和QCI的对应关系 |
| [**SET QCI2ARP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QCI到ARP映射/设置标准QCI到ARP的映射规则（SET QCI2ARP）_09652269.md) | ARPPVI（QCI的被抢占能力） | 0 | 本端规划 | 可选：配置ARP和QCI的对应关系 |
| [**ADD QOSPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md) | QOSPROFILENAME（QoS Profile名） | qos1 | 本端规划 | QosProfile的配置信息。 |
| [**ADD QOSPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md) | 绑定EPS用户QoS（BINDEPSSUBQOS） | ENABLE（使能） | 本端规划 | QosProfile的配置信息。 |
| [**ADD QOSPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md) | EPS用户QoS索引（EPSSUBQOS） | 200 | 本端规划 | QosProfile的配置信息。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | QOSPROFILENAME（QoS Profile名） | qos1 | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | QCI（QCI值） | 1 | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | GBRDL（下行保证带宽） | 256bit/s | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | GBRDLACTION（超过下行保证带宽的处理） | DEGRADE(降级) | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | GBRUL（上行保证带宽） | 128bit/s | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | GBRULACTION（超过上行保证带宽的处理） | DEGRADE(降级) | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | MBRDL（下行最大带宽） | 384bit/s | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | MBRDLACTION<br>（超过下行最大带宽的处理） | DEGRADE(降级) | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | MBRUL（上行最大带宽） | 192bit/s | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) | MBRULACTION<br>（超过上行最大带宽的处理） | DEGRADE(降级) | 本端规划 | 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。 |
| [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN（APN名称） | apn1 | 本端规划 | 指定APN实例。 |
| [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md) | APN（APN名称） | apn1 | 本端规划 | 为APN实例绑定QosProfile。 |
| [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md) | HASQOSPROFILE（是否配置QosProfile） | ENABLE | 本端规划 | 为APN实例绑定QosProfile。 |
| [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md) | QOSPROFILENAME（QoS Profile名） | qos1 | 本端规划 | 为APN实例绑定QosProfile。 |

## [操作流程](#ZH-CN_OPI_0228258573)

如果APN下绑定了Qos-profile，则使用Qos-profile下的规则；否则使用QosGlobal下的规则。

全局和APN绑定Qos-profile控制方式相同，都可绑定本地签约QoS，具体如下：获取绑定的Qos-profile，根据Qos-profile下绑定的 [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md) 配置，根据QCI对应的带宽/THP门限进行比较，如果超过则根据动作进行降级还是拒绝用户接入。

## [操作步骤](#ZH-CN_OPI_0228258573)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
  [设置License项的开关（SET LICENSESWITCH）](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. **可选** ：配置EPC网络中的QoS参数和R99，R98 QoS参数的映射规则。缺省使用默认值
  [**SET EPSQCI2PRER8**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/EPS QCI映射到PreR8/设置EPS QCI到Pre-R8 QoS映射规则（SET EPSQCI2PRER8）_09651491.md)
4. **可选** ：更改缺省的ARP和标准QCI的对应关系
  [**SET QCI2ARP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QCI到ARP映射/设置标准QCI到ARP的映射规则（SET QCI2ARP）_09652269.md)
5. **可选** ：配置本地签约的QoS信息。
  [**ADD EPSSUBQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md)
6. 配置EPS QoS缺省QoS参数（用于纠错）。
  [**SET DEFEPSQOS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md)
7. 设置全局的QoS信息。
  [**SET QOSGLOBAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置全局QoS配置（SET QOSGLOBAL）_09652976.md)
8. 配置基于APN的QoS策略。
    - 配置指定APN实例下的QosProfile名称，并进入QoS实例。
      [**ADD QOSPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md)
    - 配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。
      [**ADD EPSQOSACTION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS QoS控制动作/增加EPS QoS控制动作配置（ADD EPSQOSACTION）_09654382.md)
    - 配置APN实例。
      [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    - 为APN实例绑定QoS profile。
      [**SET APNQOSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)

## [任务示例](#ZH-CN_OPI_0228258573)

任务描述

UNC 对用户携带的QoS进行控制，然后对用户流量进行监管。

脚本

- 打开本特性的License配置开关。
  ```
  SET LICENSESWITCH:LICITEM="LKV3W9LQOS12",SWITCH=ENABLE;
  ```
- **可选**：配置EPC网络中的QoS参数和R99，R98 QoS参数的映射规则。缺省使用默认值。
  ```
  SET EPSQCI2PRER8:QCI=4,TRAFFICCLASS=CONVERSATIONAL,THP=NORMAL,SIGNALIND=OPTIMIZE,SRCSTATDESC=SPEECH;
  ```
- **可选**：更改缺省的ARP和标准QCI的对应关系
  ```
  SET QCI2ARP:QCI=1,ARPPCI=0,ARPPL=1,ARPPVI=0;
  ```
- **可选**：配置本地签约的QoS信息。
  ```
  ADD EPSSUBQOS: SUBQOSINDEX=200, QCI=5, ARPPL=10, AMBRDL=564110, AMBRUL=300000;
  ```
- 配置基于EPS缺省QoS参数（用于纠错）。
  ```
  SET DEFEPSQOS: QOSCLASSID=1, ARPVALUE=1, GBRDL=200, GBRUL=230, MBRDL=300, MBRUL=300, APNAMBRDL=1000, APNAMBRUL=1000;
  ```
- 配置基于全局的EPS QoS信息。
  ```
  SET QOSGLOBAL:QOSPROFILENAME="qos2",BINDEPSSUBQOS=ENABLE,EPSSUBQOS=200;
  ```
- 配置基于APN的QoS。
  //配置指定APN实例下的QosProfile名称，并进入QoS实例。
  ```
  ADD QOSPROFILE:QOSPROFILENAME="qos1",BINDEPSSUBQOS=ENABLE,EPSSUBQOS=200;
  ```
  //配置QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。
  ```
  ADD EPSQOSACTION:QOSPROFILENAME="qos1",QCI=1,GBRDL=256,GBRDLACTION=DEGRADE,GBRUL=128,GBRULACTION=DEGRADE,MBRDL=384,
  MBRDLACTION=DEGRADE,MBRUL=192,MBRULACTION=DEGRADE;
  ```
  //进入指定APN实例。
  ```
  ADD APN:APN="apn1";
  ```
  //为该APN实例绑定QosProfile。
  ```
  SET APNQOSATTR:APN="apn1",HASQOSPROFILE=ENABLE,QOSPROFILENAME="qos1";
  ```
