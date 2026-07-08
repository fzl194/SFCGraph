# 激活语音PCF/PCRF故障Bypass（Gx接口）

- [操作场景](#ZH-CN_OPI_0000002160552093__1.3.1)
- [必备事项](#ZH-CN_OPI_0000002160552093__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000002160552093__1.3.3)
- [任务示例](#ZH-CN_OPI_0000002160552093__1.3.4)

## [操作场景](#ZH-CN_OPI_0000002160552093)

本操作指导在运行网络中激活语音PCF/PCRF故障Bypass特性的过程。

## [必备事项](#ZH-CN_OPI_0000002160552093)

前提条件

- 请仔细阅读[WSFD-201207 语音PCF/PCRF故障Bypass特性概述](WSFD-201207 语音PCF_PCRF故障Bypass特性概述_31784105.md)和[实现原理（Gx接口）](实现原理（Gx接口）_18551772.md)。
- 依赖的特性已完成配置，相关特性参见[与其他特性的交互](WSFD-201207 语音PCF_PCRF故障Bypass特性概述_31784105.md#ZH-CN_TOPIC_0000001931784105__Dependency)。
- PGW-C和PCRF直连场景，对于支持Failover的PCRF已参考[Gx Failover功能](../../智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/激活PCC基本功能/Gx Failover功能_31422950.md)配置PCRF支持Failover功能。
- 已完成License加载，对应License项见[License支持](WSFD-201207 语音PCF_PCRF故障Bypass特性概述_31784105.md#ZH-CN_TOPIC_0000001931784105__p1554908070180641)。

数据

> **说明**
> - 下面数据表格中的URRID、USAGERPTMODE、PCCPOLICYGRPNM、 RULENAME、POLICYTYPE、POLICYNAME、USERPROFILENAME要与UPF保持一致。
> - 语音承载的静态PCC规则中的RG与PCRF下发的动态规则中的RG相同。
> - PCRF下发的用于创建语音专有承载的规则的优先级高于本地配置的用于创建语音专有承载的规则；本地配置的用于创建语音专有承载的规则优先级高于PCRF下发的any to any的动态规则和本地配置的any to any的预定义规则。

*表1 语音缺省承载静态PCC策略数据*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 使用量上报规则名称（URRNAME） | urr_signaling_offline<br>urr_signaling_online | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | URR标识（URRID） | 2005<br>2015 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 使用量上报模式（USAGERPTMODE） | OFFLINE<br>ONLINE | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费标识组成类型（OFFCOMPOUNDTYPE） | ONLYRG | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费组（RG） | 20 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费统计类型（OFFMETERINGTYPE） | VOLUME | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费标识组成类型（ONLCOMPOUNDTYPE） | ONLYRG | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费组（ONLINERG） | 25 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费统计类型（ONLMETERINGTYPE） | VOLUME | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 使用量上报规则组名称（URRGROUPNAME） | urrg_signaling_01 | 本端规划 | 增加使用量上报规则组。 |
| **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 上行发起URR名称1（UPURRNAME1） | urr_signaling_offline | 本端规划 | 增加使用量上报规则组。 |
| **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 下行发起URR名称1（DOWNURRNAME1） | urr_signaling_offline | 本端规划 | 增加使用量上报规则组。 |
| **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 上行发起URR名称2（UPURRNAME2） | urr_signaling_online | 本端规划 | 增加使用量上报规则组。 |
| **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 下行发起URR名称2（DOWNURRNAME2） | urr_signaling_online | 本端规划 | 增加使用量上报规则组。 |
| [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | PCC策略组名称（PCCPOLICYGRPNM） | pccpolicygrp_signaling | 本端规划 | 配置PCC策略组。存在多条记录时，PCC策略组名称不能重复。 |
| [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | 使用量上报规则组名称（URRGROUPNAME） | urrg_signaling_01 | 已配置数据中获取 | 使用<br>**[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**<br>定义的使用量上报规则组。 |
| [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | rule_ims_signaling | 本端规划 | 配置业务策略规则。存在多条数据时，规则名称+策略类型不能完全相同。 |
| [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCRF下发的用于创建语音专有承载的规则的优先级高于本地配置的用于创建语音专有承载的规则；本地配置的用于创建语音/专有承载的规则优先级高于PCRF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
| [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 全局优先级（PRIORITY） | 65535 | 与对端协商 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCRF下发的用于创建语音专有承载的规则的优先级高于本地配置的用于创建语音专有承载的规则；本地配置的用于创建语音/专有承载的规则优先级高于PCRF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
| [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略名称（POLICYNAME） | pccpolicygrp_signaling | 已配置数据中获取 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCRF下发的用于创建语音专有承载的规则的优先级高于本地配置的用于创建语音专有承载的规则；本地配置的用于创建语音/专有承载的规则优先级高于PCRF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
| **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)** | 用户模板名称（USERPROFILENAME） | up_ims | 全网规划 | （可选）配置用户模板。 |
| [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 用户模板名称(USERPROFILENAME) | up_ims | 已配置数据中获取 | 增加用户模板与规则的绑定关系，将本地rule/预定义规则rule绑定到UserProfile上。 |
| [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 规则名称(RULENAME) | rule_ims_signaling | 已配置数据中获取 | 增加用户模板与规则的绑定关系，将本地rule/预定义规则rule绑定到UserProfile上。 |
| [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | 如果不指定策略类型，则把规则名称相同的所有策略类型的规则绑定到用户模板上。 |
| **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）配置用户模板组。 |
| **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）将用户模板绑定到用户模板组中。 |
| **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板绑定类型（UPBINDTYPE） | SPECIFIC | 全网规划 | （可选）将用户模板绑定到用户模板组中。 |
| **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 优先级（PRIORITY） | 15 | 本端规划 | （可选）将用户模板绑定到用户模板组中。 |
| **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板名称（USERPROFILENAME） | up_ims | 本端规划 | （可选）将用户模板绑定到用户模板组中。 |
| **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)** | APN（APN） | ims | 全网规划 | （可选）为APN绑定用户模板组。 |
| **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）为APN绑定用户模板组。 |

*表2 语音专有承载静态PCC策略数据*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 使用量上报规则名称（URRNAME） | urr_voice_offline<br>urr_voice_online<br>urr_qos_01 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | URR标识（URRID） | 1005<br>1015<br>1006 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 使用量上报模式（USAGERPTMODE） | OFFLINE<br>ONLINE<br>QOS | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费标识组成类型（OFFCOMPOUNDTYPE） | ONLYRG | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费组（RG） | 10 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 离线计费统计类型（OFFMETERINGTYPE） | VOLUME | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费标识组成类型（ONLCOMPOUNDTYPE） | ONLYRG | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费组（ONLINERG） | 15 | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md) | 在线计费统计类型（ONLMETERINGTYPE） | VOLUME | 本端规划 | 增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。<br>“URRID”<br>在所有URR内唯一。<br>此处取值为举例，请根据业务规划进行配置。 |
| **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 使用量上报规则组名称（URRGROUPNAME） | urrg_voice_01 | 本端规划 | 增加使用量上报规则组。 |
| **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 上行发起URR名称1（UPURRNAME1） | urr_voice_offline | 本端规划 | 增加使用量上报规则组。 |
| **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 下行发起URR名称1（DOWNURRNAME1） | urr_voice_offline | 本端规划 | 增加使用量上报规则组。 |
| **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 上行发起URR名称2（UPURRNAME2） | urr_voice_online | 本端规划 | 增加使用量上报规则组。 |
| **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)** | 下行发起URR名称2（DOWNURRNAME2） | urr_voice_online | 本端规划 | 增加使用量上报规则组。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS属性名称（QOSPROPNAME） | qosprop_voice | 本端规划 | 配置静态PCC策略的QoS参数。存在多条记录时，QoS属性名称不能重复。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS抢占能力（EMPCAP） | ENABLE | 本端规划 | 该业务可以抢占已经分配给其他低优先级业务流的资源时，设置为ENABLE。此处以抢占为例。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS被抢占设置（EMPVUL） | DISABLE | 本端规划 | 其他高优先级业务不能抢占本业务流的资源时，设置为DISABLE。此处以不被抢占为例。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 保证的上行比特率（GBRUPLKVALUE） | 64 | 固定取值 | PCRF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCRF Bypass期间，创建专有承载时，使用PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 保证的下行比特率（GBRDNLKVALUE） | 64 | 固定取值 | PCRF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCRF Bypass期间，创建专有承载时，使用PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 最大上行比特率（MBRUPLKVALUE） | 64 | 固定取值 | PCRF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCRF Bypass期间，创建专有承载时，使用PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 最大下行比特率（MBRDNLKVALUE） | 64 | 固定取值 | PCRF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCRF Bypass期间，创建专有承载时，使用PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS属性类型（QOSTYPE） | QOS_BEARER_PARA | 本端规划 | 5G用户使用QOS_FLOW_PARA，2/3/4G用户使用QOS_BEARER_PARA。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS等级标识（QCIVALUE） | 1 | 本端规划 | “QOSTYPE”<br>为<br>“QOS_BEARER_PARA”<br>时需要规划。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS使用量上报规则名称（QOSURRNAME） | urr_qos_01 | 已配置数据中获取 | 使用<br>[**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)<br>定义的URRNAME。 |
| [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | PCC策略组名称（PCCPOLICYGRPNM） | pccpolicygrp_voice | 本端规划 | 配置PCC策略组。存在多条记录时，PCC策略组名称不能重复。 |
| [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | 使用量上报规则组名称（URRGROUPNAME） | urrg_voice_01 | 已配置数据中获取 | 使用<br>**[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**<br>定义的使用量上报规则组。 |
| [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md) | Qos属性名称（QOSPROPNAME） | qosprop_voice | 已配置数据中获取 | 使用<br>[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)<br>定义的QOSPROPNAME。 |
| [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 规则名称（RULENAME） | rule_ims_voice | 本端规划 | 配置业务策略规则。存在多条数据时，规则名称+策略类型不能完全相同。 |
| [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
| [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 全局优先级（PRIORITY） | 65535 | 与对端协商 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
| [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略名称（POLICYNAME） | pccpolicygrp_voice | 已配置数据中获取 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
| **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)** | 用户模板名称（USERPROFILENAME） | up_ims | 全网规划 | （可选）配置用户模板。 |
| [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 用户模板名称(USERPROFILENAME) | up_ims | 已配置数据中获取 | 增加用户模板与规则的绑定关系，将本地rule/预定义规则rule绑定到UserProfile上。 |
| [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 规则名称(RULENAME) | rule_ims_voice | 已配置数据中获取 | 增加用户模板与规则的绑定关系，将本地rule/预定义规则rule绑定到UserProfile上。 |
| [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | 如果不指定策略类型，则把规则名称相同的所有策略类型的规则绑定到用户模板上。 |
| **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）配置用户模板组。 |
| **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）将用户模板绑定到用户模板组中。 |
| **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板绑定类型（UPBINDTYPE） | SPECIFIC | 全网规划 | （可选）将用户模板绑定到用户模板组中。 |
| **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 优先级（PRIORITY） | 15 | 本端规划 | （可选）将用户模板绑定到用户模板组中。 |
| **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)** | 用户模板名称（USERPROFILENAME） | up_ims | 本端规划 | （可选）将用户模板绑定到用户模板组中。 |
| **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)** | APN（APN） | ims | 全网规划 | （可选）为APN绑定用户模板组。 |
| **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)** | 用户模板组名称（USERPROFGNAME） | upg_ims | 全网规划 | （可选）为APN绑定用户模板组。 |

*表3 PCRF Bypass条件数据*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | 选择PCRF/PCF失败动作（SELPEERFAILACT） | ROLLBACK | 本端规划 | 配置PCRF故障处理动作。 |
| **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | Initial流程故障处理动作（INITIALFAILACT） | ROLLBACK | 本端规划 | 配置PCRF故障处理动作。 |
| **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | Update流程故障处理动作（UPDATEFAILACT） | ROLLBACK | 本端规划 | 配置PCRF故障处理动作。 |
| **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | Update流程故障回滚为Local PCC用户类型（UPDFAILLOCPCC） | INHERIT_PCC | 本端规划 | 配置PCRF故障处理动作。 |
| **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** | 用户回滚后在线保持时长（分钟）（HOLDINGTIME） | 30 | 本端规划 | 配置全局Holding Time和Fast Holding Time。 |
| **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** | 随机延迟范围（分钟）（ADJUSTRANGE） | 10 | 本端规划 | 配置全局Holding Time和Fast Holding Time。 |
| **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** | 用户快速回滚后在线保持时长（分钟）（FASTHOLDINGTIME） | 10 | 全网规划 | 配置全局Holding Time和Fast Holding Time。 |
| **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** | 快速随机延迟范围（分钟）（FASTADJUSTRANGE） | 5 | 全网规划 | 配置全局Holding Time和Fast Holding Time。 |
| [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | PCC模板名称（PCCTEMPNAME） | pcctemplate | 本端规划 | 配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
| [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | 选择PCRF/PCF失败动作（SELPEERFAILACT） | ROLLBACK | 本端规划 | 配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
| [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | Initial流程故障处理动作（INITIALFAILACT） | ROLLBACK | 本端规划 | 配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
| [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | Update流程故障处理动作（UPDATEFAILACT） | ROLLBACK | 本端规划 | 配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
| [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | Update流程故障回滚为Local PCC用户类型（UPDFAILLOCPCC） | INHERIT_PCC | 本端规划 | 配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
| [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | 用户回滚后在线保持时长（分钟）（HOLDINGTIME） | 30 | 本端规划 | 配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
| [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | 随机延迟范围（分钟）（ADJUSTRANGE） | 10 | 本端规划 | 配置PCC模板中PCRF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | PCC模板名称（PCCTEMPLATE） | pcctemplate | 已配置数据中获取 | 配置对端回复指定结果码后PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“GXRESULTCODEVAL”<br>需要与对端PCRF/DRA确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 接口类型（INTFTYPE） | INTFTYPE_GX | 与对端协商 | 配置对端回复指定结果码后PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“GXRESULTCODEVAL”<br>需要与对端PCRF/DRA确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 设备提供商标识（VENDORID） | 0 | 全网规划 | 配置对端回复指定结果码后PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“GXRESULTCODEVAL”<br>需要与对端PCRF/DRA确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | Gx返回码（GXRESULTCODEVAL） | 3004<br>3002<br>5012 | 与对端协商 | 配置对端回复指定结果码后PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“GXRESULTCODEVAL”<br>需要与对端PCRF/DRA确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 直连对端Initial流程处理动作（DIRECTINITACT） | FAILOVER | 本端规划 | 配置对端回复指定结果码后PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“GXRESULTCODEVAL”<br>需要与对端PCRF/DRA确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 直连对端Update流程处理动作（DIRECTUPDACT） | FAILOVER | 本端规划 | 配置对端回复指定结果码后PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“GXRESULTCODEVAL”<br>需要与对端PCRF/DRA确认，此处取值仅为举例。 |
| **[ADD RESULTCODEDRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加DRA返回码控制（ADD RESULTCODEDRA）_67382653.md)** | PCC模板名称（PCCTEMPLATE） | pcctemplate | 已配置数据中获取 | 配置PGW-C与PCRF非直连场景，DRA返回异常返回码的处理动作。 |
| **[ADD RESULTCODEDRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加DRA返回码控制（ADD RESULTCODEDRA）_67382653.md)** | 设备提供商标识（VENDORID） | 0 | 全网规划 | 配置PGW-C与PCRF非直连场景，DRA返回异常返回码的处理动作。 |
| **[ADD RESULTCODEDRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加DRA返回码控制（ADD RESULTCODEDRA）_67382653.md)** | 返回码（RESULTCODEVAL） | 3004<br>3002<br>5012 | 与对端协商 | 配置PGW-C与PCRF非直连场景，DRA返回异常返回码的处理动作。 |
| **[ADD RESULTCODEDRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加DRA返回码控制（ADD RESULTCODEDRA）_67382653.md)** | Initial流程处理动作（INITACTION） | FAILOVER<br>LOCALPCC | 本端规划 | 配置PGW-C与PCRF非直连场景，DRA返回异常返回码的处理动作。 |
| **[ADD RESULTCODEDRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加DRA返回码控制（ADD RESULTCODEDRA）_67382653.md)** | Initial流程回滚后使能Holding-Time（INITHOLDTMSW） | ENABLE | 本端规划 | 配置PGW-C与PCRF非直连场景，DRA返回异常返回码的处理动作。 |
| **[ADD RESULTCODEDRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加DRA返回码控制（ADD RESULTCODEDRA）_67382653.md)** | Update流程处理动作（UPDATEACTION） | FAILOVER<br>INHERIT_PCC | 本端规划 | 配置PGW-C与PCRF非直连场景，DRA返回异常返回码的处理动作。 |
| **[ADD RESULTCODEDRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加DRA返回码控制（ADD RESULTCODEDRA）_67382653.md)** | Update流程回滚后使能Holding-Time（UPDHOLDTMSW） | ENABLE | 本端规划 | 配置PGW-C与PCRF非直连场景，DRA返回异常返回码的处理动作。 |
| **[ADD PCCBYPASSCODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加PCC故障场景维持BYPASS状态码配置（ADD PCCBYPASSCODE）_83249518.md)** | PCC模板名称（PCCTEMPLATE） | pcctemplate | 本端规划 | 配置在非直连组网场景，会话退出PCRF Bypass状态时PGW-C发送探测消息后，收到对端网元返回特定状态码会话继续保持Bypass状态。 |
| **[ADD PCCBYPASSCODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加PCC故障场景维持BYPASS状态码配置（ADD PCCBYPASSCODE）_83249518.md)** | 接口类型（INTFTYPE） | INTFTYPE_GX | 与对端协商 | 配置在非直连组网场景，会话退出PCRF Bypass状态时PGW-C发送探测消息后，收到对端网元返回特定状态码会话继续保持Bypass状态。 |
| **[ADD PCCBYPASSCODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加PCC故障场景维持BYPASS状态码配置（ADD PCCBYPASSCODE）_83249518.md)** | Gx返回码（GXRESULTCODEVAL） | 3xxx | 与对端协商 | 配置在非直连组网场景，会话退出PCRF Bypass状态时PGW-C发送探测消息后，收到对端网元返回特定状态码会话继续保持Bypass状态。 |
| **[SET IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/设置语音PCF_PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）_49496669.md)** | 无语音专载时的故障非预期Bypass场景的异常处理动作（ACTNODEDBEARER） | TERMINATE | 本端规划 | 配置更新流程Gx接口不支持Failover场景、PGW-C和PCRF直连场景Failover后收到备PCRF返回异常码场景和PGW-C和PCRF非直连场景Failover后收到DRA返回非5012/3002异常码场景，分别在有、无语音专有承载时的处理动作，以及在PGW-C和PCRF非直连场景没有语音专有承载时，会话退出PCRF Bypass状态是否发送探测消息。<br>说明：此处取值仅为举例，请根据局点实际业务需要进行配置。 |
| **[SET IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/设置语音PCF_PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）_49496669.md)** | 存在语音专载时的更新流程故障非预期Bypass场景的异常处理动作（ACTWITDEDBEARER） | FASTROLLBACK | 本端规划 | 配置更新流程Gx接口不支持Failover场景、PGW-C和PCRF直连场景Failover后收到备PCRF返回异常码场景和PGW-C和PCRF非直连场景Failover后收到DRA返回非5012/3002异常码场景，分别在有、无语音专有承载时的处理动作，以及在PGW-C和PCRF非直连场景没有语音专有承载时，会话退出PCRF Bypass状态是否发送探测消息。<br>说明：此处取值仅为举例，请根据局点实际业务需要进行配置。 |
| **[SET IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/设置语音PCF_PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）_49496669.md)** | 存在语音专载时更新流程故障回滚为Local PCC用户类型（FAILLOCPCC） | INHERIT_PCC | 全网规划 | 配置更新流程Gx接口不支持Failover场景、PGW-C和PCRF直连场景Failover后收到备PCRF返回异常码场景和PGW-C和PCRF非直连场景Failover后收到DRA返回非5012/3002异常码场景，分别在有、无语音专有承载时的处理动作，以及在PGW-C和PCRF非直连场景没有语音专有承载时，会话退出PCRF Bypass状态是否发送探测消息。<br>说明：此处取值仅为举例，请根据局点实际业务需要进行配置。 |
| **[SET IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/设置语音PCF_PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）_49496669.md)** | 非直连场景下退出Bypass发送探测消息开关（TSTUPDATEREQSW） | ENABLE | 本端规划 | 配置更新流程Gx接口不支持Failover场景、PGW-C和PCRF直连场景Failover后收到备PCRF返回异常码场景和PGW-C和PCRF非直连场景Failover后收到DRA返回非5012/3002异常码场景，分别在有、无语音专有承载时的处理动作，以及在PGW-C和PCRF非直连场景没有语音专有承载时，会话退出PCRF Bypass状态是否发送探测消息。<br>说明：此处取值仅为举例，请根据局点实际业务需要进行配置。 |
| **[MOD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/修改Diameter路由域名信息（MOD DIAMRTREALM）_09897304.md)** | Diameter域名名称（REALMNAME） | pcrf.huawei.com | 本端规划 | 配置DRA支持Failover功能。 |
| **[MOD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/修改Diameter路由域名信息（MOD DIAMRTREALM）_09897304.md)** | Diameter应用（APPLICATION） | Gx | 本端规划 | 配置DRA支持Failover功能。 |
| **[MOD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/修改Diameter路由域名信息（MOD DIAMRTREALM）_09897304.md)** | Failover开关（FAILOVERSW） | ENABLE | 本端规划 | 配置DRA支持Failover功能。 |
| [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | APN名称（APN） | ims | 全网规划 | （可选）针对指定的DNN绑定PCC模板。 |
| [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | PCC模板名称（PCCTEMPLATE） | pcctemplate | 本端规划 | （可选）针对指定的DNN绑定PCC模板。 |
| [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | APN名称（APN） | ims | 已配置数据中获取 | 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除承载，删除承载后还需要重新创建承载。<br>此处以5分钟为例，请以局点规划数据为准。 |
| [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 继承默认开关（INHERIT） | NO | 本端规划 | 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除承载，删除承载后还需要重新创建承载。<br>此处以5分钟为例，请以局点规划数据为准。 |
| [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | PGW-C和SGW-C/PGW-C空闲上下文检查开关(PCTXCHKSW) | ENABLE | 本端规划 | 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除承载，删除承载后还需要重新创建承载。<br>此处以5分钟为例，请以局点规划数据为准。 |
| [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | GUL承载级别参数（GULTIMERLEVEL） | BEARER | 本端规划 | 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除承载，删除承载后还需要重新创建承载。<br>此处以5分钟为例，请以局点规划数据为准。 |
| [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 缺省承载和默认GBR的定时器（DFTBEARPOLICY） | OFF | 本端规划 | 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除承载，删除承载后还需要重新创建承载。<br>此处以5分钟为例，请以局点规划数据为准。 |
| [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 承载定时器(min)（BEARERTIMER） | 5 | 本端规划 | 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除承载，删除承载后还需要重新创建承载。<br>此处以5分钟为例，请以局点规划数据为准。 |

*表4 相关软参数据*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 数据类型（DT） | Dw | 本端规划 | 配置在HoldingTime超时时，用户会话中有语音专有承载时不去活会话，重启HoldingTime定时器；没有语音专有承载时去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | Dword索引（DWORDNUM） | 519 | 本端规划 | 配置在HoldingTime超时时，用户会话中有语音专有承载时不去活会话，重启HoldingTime定时器；没有语音专有承载时去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 软参记录值（VALUE） | 1 | 本端规划 | 配置在HoldingTime超时时，用户会话中有语音专有承载时不去活会话，重启HoldingTime定时器；没有语音专有承载时去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 比特位（POSITION） | 5 | 本端规划 | 配置在HoldingTime超时时，用户会话中有语音专有承载时不去活会话，重启HoldingTime定时器；没有语音专有承载时去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 数据类型（DT） | Dw | 本端规划 | 配置PGW-C在激活流程查询PCRF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活用户）生效。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | Dword索引（DWORDNUM） | 519 | 本端规划 | 配置PGW-C在激活流程查询PCRF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活用户）生效。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 软参记录值（VALUE） | 1 | 本端规划 | 配置PGW-C在激活流程查询PCRF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活用户）生效。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 比特位（POSITION） | 9 | 本端规划 | 配置PGW-C在激活流程查询PCRF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活用户）生效。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 数据类型（DT） | Dw | 本端规划 | 配置语音PCRF进入Bypass后，HoldingTime定时器启动三次后不强制去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | Dword索引（DWORDNUM） | 544 | 本端规划 | 配置语音PCRF进入Bypass后，HoldingTime定时器启动三次后不强制去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 软参记录值（VALUE） | 1 | 本端规划 | 配置语音PCRF进入Bypass后，HoldingTime定时器启动三次后不强制去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 比特位（POSITION） | 17 | 本端规划 | 配置语音PCRF进入Bypass后，HoldingTime定时器启动三次后不强制去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 数据类型（DT） | Dw | 本端规划 | 配置PGW-C对接语音PCRF时将业务触发专载的双向流进行拆分处理。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | Dword索引（DWORDNUM） | 545 | 本端规划 | 配置PGW-C对接语音PCRF时将业务触发专载的双向流进行拆分处理。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 软参记录值（VALUE） | 1 | 本端规划 | 配置PGW-C对接语音PCRF时将业务触发专载的双向流进行拆分处理。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 比特位（POSITION） | 18 | 本端规划 | 配置PGW-C对接语音PCRF时将业务触发专载的双向流进行拆分处理。 |

## [操作步骤](#ZH-CN_OPI_0000002160552093)

全部展开

1. **可选：**
  配置语音缺省承载静态PCC策略。

  > **说明**
  > 仅当局点未配置语音缺省承载静态PCC策略时，执行本步骤。否则，跳过本步骤。

  a. 增加使用量上报规则信息。
      [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    b. 增加使用量上报规则组。
      **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**
    c. 配置PCC策略组。
      [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    d. 配置业务策略规则。
      [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    e. **可选：**配置用户模板。
      > **说明**
      > 如果已配置了APN ims使用的用户模板，则跳过本步骤。
      **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)**
    f. 增加用户模板与规则的绑定关系。
      [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    g. **可选：**配置用户模板组。
      > **说明**
      > 如果已配置了APN ims使用的用户模板组，则跳过本步骤。
      **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**
    h. **可选：**将用户模板绑定到用户模板组中。
      > **说明**
      > 如果已配置了APN ims使用的用户模板与模板组的绑定关系，则跳过本步骤。
      **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)**
    i. **可选：**为APN绑定用户模板组。
      > **说明**
      > 如果APN ims已绑定了用户模板组，则跳过本步骤。
      **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)**
2.
  配置语音缺省承载静态PCC策略。

  a. 增加使用量上报规则信息。
      [**ADD URR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/内容计费标识/增加URR（ADD URR）_09897158.md)
    b. 增加使用量上报规则组。
      **[ADD URRGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/使用量上报规则组/增加URR组（ADD URRGROUP）_09897193.md)**
    c. 配置静态PCC策略的QoS参数。
      [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
    d. 配置PCC策略组。
      [**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)
    e. 配置业务策略规则。
      [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    f. **可选：**配置用户模板。
      > **说明**
      > 如果已配置了APN ims使用的用户模板，则跳过本步骤。
      **[ADD USERPROFILE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)**
    g. 增加用户模板与规则的绑定关系。
      [**ADD RULEBINDING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    h. **可选：**配置用户模板组。
      > **说明**
      > 如果已配置了APN ims使用的用户模板组，则跳过本步骤。
      **[ADD USRPROFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板组/增加用户模板组（ADD USRPROFGROUP）_09897220.md)**
    i. **可选：**将用户模板绑定到用户模板组中。
      > **说明**
      > 如果已配置了APN ims使用的用户模板与模板组的绑定关系，则跳过本步骤。
      **[ADD UPBINDUPG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板绑定/增加用户模板组和用户模板的绑定关系（ADD UPBINDUPG）_09897229.md)**
    j. **可选：**为APN绑定用户模板组。
      > **说明**
      > 如果APN ims已绑定了用户模板组，则跳过本步骤。
      **[ADD APNUSRPROFG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)**
3.
  配置PCRF Bypass条件。

  a. 配置全局PCRF故障处理动作。
      **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)**
    b. 配置全局Holding Time。
      **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**
    c. 基于PCC模板配置故障处理动作、failover开关和Holding Time。
      > **说明**
      > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。
      [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) / **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**
    d. 配置对端PCRF/DRA回复指定结果码后PGW-C的处理操作。
      > **说明**
      > 具体结果码需要与对端PCRF/DRA确认。
      **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)** / **[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)**
      **[ADD RESULTCODEDRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加DRA返回码控制（ADD RESULTCODEDRA）_67382653.md)**
    e. 增加PCC故障场景维持BYPASS状态码配置。
      **[ADD PCCBYPASSCODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加PCC故障场景维持BYPASS状态码配置（ADD PCCBYPASSCODE）_83249518.md)**
    f. 配置更新流程Gx接口不支持Failover场景、PGW-C和PCRF直连场景Failover后收到备PCRF返回异常码场景和PGW-C和PCRF非直连场景Failover后收到DRA返回非5012/3002异常码场景，分别在有、无语音专有承载时的处理动作，以及在PGW-C和PCRF非直连场景没有语音专有承载时，会话退出PCRF Bypass状态是否发送探测消息。
      **[SET IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/设置语音PCF_PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）_49496669.md)**
    g. Gx接口PGW-C和PCRF非直连场景，对于支持Failover的DRA配置支持Failover功能。
      > **说明**
      > 如果DRA不支持Failover则跳过本步骤。
      **[MOD DIAMRTREALM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由管理/Diameter路由/修改Diameter路由域名信息（MOD DIAMRTREALM）_09897304.md)**
    h. **可选：**为DNN绑定PCC模板，如果已经绑定过，则不需要执行该步骤。
      [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    i. 设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。
      [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
4.
  配置相关软参。

  a. 通过软参 [DWORD519 Bit5](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/PCC策略控制管理/DWORD519 BIT5 控制HoldingTime超时时是否去活有语音专载的会话_98344879.md) 配置在HoldingTime超时时，用户会话中有语音专有承载时不去活会话，重启HoldingTime定时器；没有语音专有承载时去活会话。
      **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)**
    b. 通过软参 [DWORD519 Bit9](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/PCC策略控制管理/DWORD519 Bit9控制激活流程查询PCF失败发生回滚时，HoldingTime功能是否生效_97903713.md) 配置在PGW-C激活流程查询PCRF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活会话）生效。
      **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)**
    c. **可选：**通过软参 [DWORD544 BIT17](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/PCC策略控制管理/DWORD544 BIT17 控制语音PCF_PCRF进入Bypass后，HoldingTime启动三次后是否强制去活_42799282.md) 配置语音PCRF进入Bypass后，HoldingTime定时器启动三次后是否强制去活会话。
      **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)**
    d. 通过软参 [DWORD545 BIT18](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/PCC策略控制管理/DWORD545 BIT18 控制UNC对接语音PCRF_PCF时是否将业务触发专载的双向流进行拆分处理_95599886.md) 配置PGW-C对接语音PCRF时将业务触发专载的双向流进行拆分处理。
      **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)**

## [任务示例](#ZH-CN_OPI_0000002160552093)

任务描述

任务一：PGW-C上没有配置语音缺省承载静态PCC策略，在PGW-C上激活语音PCF/PCRF故障Bypass功能。

任务二：PGW-C上已配置语音缺省承载静态PCC策略，APN ims绑定了User Profile组upg_ims，User Profile组中绑定了User Profile upg_ims，在当前配置基础上激活语音PCF/PCRF故障Bypass功能。

脚本

- **任务一：PGW-C上没有配置语音缺省承载静态PCC策略，在PGW-C上激活语音PCF/PCRF故障Bypass功能。**
    1. 配置语音缺省承载静态PCC策略。
      //增加使用量上报规则信息。

      ```
      ADD URR:URRNAME="urr_signaling_offline", URRID=2005, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=20, OFFMETERINGTYPE=VOLUME;
      ADD URR:URRNAME="urr_signaling_online", URRID=2015, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=25, ONLMETERINGTYPE=VOLUME;
      ```
      //增加使用量上报规则组。

      ```
      ADD URRGROUP:URRGROUPNAME="urrg_signaling_01", UPURRNAME1="urr_signaling_offline", DOWNURRNAME1="urr_signaling_offline", UPURRNAME2="urr_signaling_online", DOWNURRNAME2="urr_signaling_online";
      ```
      //配置PCC策略组。

      ```
      ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_signaling", URRGROUPNAME="urrg_signaling_01";
      ```
      //配置业务策略规则。

      ```
      ADD RULE:RULENAME="rule_ims_signaling", POLICYTYPE=PCC, PRIORITY=65535, POLICYNAME="pccpolicygrp_signaling";
      ```
      //配置用户模板。

      ```
      ADD USERPROFILE:USERPROFILENAME="up_ims";
      ```
      //增加用户模板与规则的绑定关系。

      ```
      ADD RULEBINDING:USERPROFILENAME="up_ims", RULENAME="rule_ims_signaling", POLICYTYPE=PCC;
      ```
      //配置用户模板组。

      ```
      ADD USRPROFGROUP:USERPROFGNAME="upg_ims";
      ```
      //把用户模板绑定到用户模板组中。

      ```
      ADD UPBINDUPG:USERPROFGNAME="upg_ims", UPBINDTYPE=SPECIFIC, PRIORITY=15, USERPROFILENAME="up_ims";
      ```
      //为APN绑定用户模板组。

      ```
      ADD APNUSRPROFG:APN="ims", USERPROFGNAME="upg_ims";
      ```
    2. 配置语音专有承载静态PCC策略。
      //增加使用量上报规则信息。

      ```
      ADD URR:URRNAME="urr_qos_01", URRID=1006, USAGERPTMODE=QOS;
      ADD URR:URRNAME="urr_voice_offline", URRID=1005, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=10, OFFMETERINGTYPE=VOLUME;
      ADD URR:URRNAME="urr_voice_online", URRID=1015, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=15, ONLMETERINGTYPE=VOLUME;
      ```
      //增加使用量上报规则组。

      ```
      ADD URRGROUP:URRGROUPNAME="urrg_voice_01", UPURRNAME1="urr_voice_offline", DOWNURRNAME1="urr_voice_offline", UPURRNAME2="urr_voice_online", DOWNURRNAME2="urr_voice_online";
      ```
      //配置语音专有承载的QoS参数。

      ```
      ADD QOSPROP:QOSPROPNAME="qosprop_voice", EMPCAP=ENABLE, EMPVUL=DISABLE, GBRUPLKVALUE=64, GBRDNLKVALUE=64, MBRUPLKVALUE=64, MBRDNLKVALUE=64, QOSTYPE=QOS_BEARER_PARA, QCIVALUE=1, QOSURRNAME="urr_qos_01";
      ```
      //配置PCC策略组。

      ```
      ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_voice", URRGROUPNAME="urrg_voice_01", QOSPROPNAME="qosprop_voice";
      ```
      //配置业务策略规则。

      ```
      ADD RULE:RULENAME="rule_ims_voice", POLICYTYPE=PCC, PRIORITY=65535, POLICYNAME="pccpolicygrp_voice";
      ```
      //增加用户模板与规则的绑定关系。

      ```
      ADD RULEBINDING:USERPROFILENAME="up_ims", RULENAME="rule_ims_voice", POLICYTYPE=PCC;
      ```
    3. 配置PCRF Bypass条件。
      //配置全局PCRF故障处理动作。

      ```
      SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC;
      ```
      //配置全局Holding Time。

      ```
      SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10, FASTHOLDINGTIME=10, FASTADJUSTRANGE=5;
      ```
      //基于存在的PCC模板配置故障处理动作、failover开关和Holding Time。

      > **说明**
      > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。

      ```
      MOD PCCTEMPLATE:PCCTEMPNAME="pcctemplate", SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, HOLDINGTIME=30, ADJUSTRANGE=10;
      ```
      //配置对端PCRF/DRA回复指定结果码后PGW-C的处理操作。

      > **说明**
      > 具体结果码需要与对端PCF/SCP确认。
          - 策略接口为Gx接口，直连组网
            ```
            ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="3004";
            ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="3002";
            ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="5012";
            ```
          - 策略接口为Gx接口，非直连组网
            ```
            ADD RESULTCODEDRA:VENDORID=0, PCCTEMPLATE="pcctemplate", INITACTION=FAILOVER, UPDATEACTION=FAILOVER, RESULTCODEVAL="3004";
            ADD RESULTCODEDRA:VENDORID=0, PCCTEMPLATE="pcctemplate", INITACTION=FAILOVER, UPDATEACTION=FAILOVER, RESULTCODEVAL="3002";
            ADD RESULTCODEDRA:VENDORID=0, PCCTEMPLATE="pcctemplate", INITACTION=LOCALPCC, INITHOLDTMSW=ENABLE, UPDATEACTION=INHERIT_PCC, UPDHOLDTMSW=ENABLE, RESULTCODEVAL="5012";
            ```
      //增加Gx接口非直连场景，PCC故障场景维持BYPASS状态码配置。此处理取值仅为举例。

      ```
      ADD PCCBYPASSCODE:PCCTEMPLATE="pcctemplate", INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="3xxx";
      ```
      //配置更新流程Gx接口不支持Failover场景、PGW-C和PCRF直连场景Failover后收到备PCRF返回异常码场景和PGW-C和PCRF非直连场景Failover后收到DRA返回非5012/3002异常码场景，分别在有、无语音专有承载时的处理动作，以及在PGW-C和PCRF非直连场景没有语音专有承载时，会话退出PCRF Bypass状态发送探测消息。
      ```
      SET IMSBYPASSFUNC: ACTNODEDBEARER=TERMINATE, ACTWITDEDBEARER=FASTROLLBACK, FAILLOCPCC=INHERIT_PCC, TSTUPDATEREQSW=ENABLE;
      ```
      //Gx接口PGW-C和PCRF非直连场景，对于支持Failover的DRA配置支持Failover功能。

      ```
      MOD DIAMRTREALM: REALMNAME="pcrf.huawei.com", APPLICATION=GX, FAILOVERSW=ENABLE;
      ```
      //（可选）为DNN绑定PCC模板，如果已经绑定过，则不需要执行该步骤。

      ```
      SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";
      ```
      //设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。

      ```
      SET APNIDLETIME: APN="ims", INHERIT=NO, PCTXCHKSW=ENABLE, GULTIMERLEVEL=BEARER, DFTBEARPOLICY=OFF, BEARERTIMER=5;
      ```
    4. 配置相关软参。
      //配置在HoldingTime超时时，用户会话中有语音专有承载时不去活会话，重启HoldingTime定时器；没有语音专有承载时去活会话。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=519, VALUE=VALUE_1, POSITION=5;
      ```
      //配置PGW-C在激活流程查询PCRF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活会话）生效。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=519, VALUE=VALUE_1, POSITION=9;
      ```
      //（可选）配置语音PCRF进入Bypass后，HoldingTime定时器启动三次后不强制去活会话。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=544, VALUE=VALUE_1, POSITION=17;
      ```
      //配置PGW-C对接语音PCRF时将业务触发专载的双向流进行拆分处理。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=545, VALUE=VALUE_1, POSITION=18;
      ```
- **任务二：PGW-C上已配置语音缺省承载静态PCC策略，APN ims绑定了User Profile组upg_ims，User Profile组中绑定了User Profile upg_ims，在当前配置基础上激活语音PCF/PCRF故障Bypass功能。**
    1. 配置语音专有承载静态PCC策略。
      //增加使用量上报规则信息。

      ```
      ADD URR:URRNAME="urr_qos_01", URRID=1006, USAGERPTMODE=QOS;
      ADD URR:URRNAME="urr_voice_offline", URRID=1005, USAGERPTMODE=OFFLINE, OFFCOMPOUNDTYPE=ONLYRG, RG=10, OFFMETERINGTYPE=VOLUME;
      ADD URR:URRNAME="urr_voice_online", URRID=1015, USAGERPTMODE=ONLINE, ONLCOMPOUNDTYPE=ONLYRG, ONLINERG=15, ONLMETERINGTYPE=VOLUME;
      ```
      //增加使用量上报规则组。

      ```
      ADD URRGROUP:URRGROUPNAME="urrg_voice_01", UPURRNAME1="urr_voice_offline", DOWNURRNAME1="urr_voice_offline", UPURRNAME2="urr_voice_online", DOWNURRNAME2="urr_voice_online";
      ```
      //配置语音专有承载的QoS参数。

      ```
      ADD QOSPROP:QOSPROPNAME="qosprop_voice", EMPCAP=ENABLE, EMPVUL=DISABLE, GBRUPLKVALUE=64, GBRDNLKVALUE=64, MBRUPLKVALUE=64, MBRDNLKVALUE=64, QOSTYPE=QOS_BEARER_PARA, QCIVALUE=1, QOSURRNAME="urr_qos_01";
      ```
      //配置PCC策略组。

      ```
      ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_voice", URRGROUPNAME="urrg_voice_01", QOSPROPNAME="qosprop_voice";
      ```
      //配置业务策略规则。

      ```
      ADD RULE:RULENAME="rule_ims_voice", POLICYTYPE=PCC, PRIORITY=65535, POLICYNAME="pccpolicygrp_voice";
      ```
      //增加用户模板与规则的绑定关系。

      ```
      ADD RULEBINDING:USERPROFILENAME="up_ims", RULENAME="rule_ims_voice", POLICYTYPE=PCC;
      ```
    2. 配置PCRF Bypass条件。
      //配置全局PCRF故障处理动作。

      ```
      SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC;
      ```
      //配置全局Holding Time。

      ```
      SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10, FASTHOLDINGTIME=10, FASTADJUSTRANGE=5;
      ```
      //基于存在的PCC模板配置故障处理动作、failover开关和Holding Time。

      > **说明**
      > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。

      ```
      MOD PCCTEMPLATE:PCCTEMPNAME="pcctemplate", SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, HOLDINGTIME=30, ADJUSTRANGE=10;
      ```
      //配置对端PCRF/DRA回复指定结果码后PGW-C的处理操作。

      > **说明**
      > 具体结果码需要与对端PCF/SCP确认。
          - 策略接口为Gx接口，直连组网
            ```
            ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="3004";
            ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="3002";
            ADD RESULTCODECTRL:VENDORID=0, PCCTEMPLATE="pcctemplate", DIRECTINITACT=FAILOVER, DIRECTUPDACT=FAILOVER, INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="5012";
            ```
          - 策略接口为Gx接口，非直连组网
            ```
            ADD RESULTCODEDRA:VENDORID=0, PCCTEMPLATE="pcctemplate", INITACTION=FAILOVER, UPDATEACTION=FAILOVER, RESULTCODEVAL="3004";
            ADD RESULTCODEDRA:VENDORID=0, PCCTEMPLATE="pcctemplate", INITACTION=FAILOVER, UPDATEACTION=FAILOVER, RESULTCODEVAL="3002";
            ADD RESULTCODEDRA:VENDORID=0, PCCTEMPLATE="pcctemplate", INITACTION=LOCALPCC, INITHOLDTMSW=ENABLE, UPDATEACTION=INHERIT_PCC, UPDHOLDTMSW=ENABLE, RESULTCODEVAL="5012";
            ```
      //增加Gx接口非直连场景，PCC故障场景维持BYPASS状态码配置。此处理取值仅为举例。

      ```
      ADD PCCBYPASSCODE:PCCTEMPLATE="pcctemplate", INTFTYPE=INTFTYPE_GX, GXRESULTCODEVAL="3xxx";
      ```
      //配置更新流程Gx接口不支持Failover场景、PGW-C和PCRF直连场景Failover后收到备PCRF返回异常码场景和PGW-C和PCRF非直连场景Failover后收到DRA返回非5012/3002异常码场景，分别在有、无语音专有承载时的处理动作，以及在PGW-C和PCRF非直连场景没有语音专有承载时，会话退出PCRF Bypass状态发送探测消息。
      ```
      SET IMSBYPASSFUNC: ACTNODEDBEARER=TERMINATE, ACTWITDEDBEARER=FASTROLLBACK, FAILLOCPCC=INHERIT_PCC, TSTUPDATEREQSW=ENABLE;
      ```
      //Gx接口PGW-C和PCRF非直连场景，对于支持Failover的DRA配置支持Failover功能。

      ```
      MOD DIAMRTREALM: REALMNAME="pcrf.huawei.com", APPLICATION=GX, FAILOVERSW=ENABLE;
      ```
      //（可选）为DNN绑定PCC模板，如果已经绑定过，则不需要执行该步骤。

      ```
      SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";
      ```
      //设置承载空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除承载。

      ```
      SET APNIDLETIME: APN="ims", INHERIT=NO, PCTXCHKSW=ENABLE, GULTIMERLEVEL=BEARER, DFTBEARPOLICY=OFF, BEARERTIMER=5;
      ```
    3. 配置相关软参。
      //配置在HoldingTime超时时，用户会话中有语音专有承载时不去活会话，重启HoldingTime定时器；没有语音专有承载时去活会话。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=519, VALUE=VALUE_1, POSITION=5;
      ```
      //配置PGW-C在激活流程查询PCRF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活会话）生效。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=519, VALUE=VALUE_1, POSITION=9;
      ```
      //（可选）配置语音PCRF进入Bypass后，HoldingTime定时器启动三次后不强制去活会话。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=544, VALUE=VALUE_1, POSITION=17;
      ```
      //配置PGW-C对接语音PCRF时将业务触发专载的双向流进行拆分处理。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=545, VALUE=VALUE_1, POSITION=18;
      ```
