# 激活语音PCF/PCRF故障Bypass（N7接口）

- [操作场景](#ZH-CN_OPI_0000001932852169__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001932852169__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001932852169__1.3.3)
- [任务示例](#ZH-CN_OPI_0000001932852169__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001932852169)

本操作指导在运行网络中激活语音PCF/PCRF故障Bypass特性的过程。

## [必备事项](#ZH-CN_OPI_0000001932852169)

前提条件

- 请仔细阅读[WSFD-201207 语音PCF/PCRF故障Bypass特性概述](WSFD-201207 语音PCF_PCRF故障Bypass特性概述_31784105.md)和[实现原理（N7接口）](实现原理（N7接口）_85304236.md)。
- 依赖的特性已完成配置，相关特性参见[与其他特性的交互](WSFD-201207 语音PCF_PCRF故障Bypass特性概述_31784105.md#ZH-CN_TOPIC_0000001931784105__Dependency)。
- 已完成License加载，对应License项见[License支持](WSFD-201207 语音PCF_PCRF故障Bypass特性概述_31784105.md#ZH-CN_TOPIC_0000001931784105__p1554908070180641)。

数据

> **说明**
> - 下面数据表格中的URRID、USAGERPTMODE、PCCPOLICYGRPNM、 RULENAME、POLICYTYPE、POLICYNAME、USERPROFILENAME要与UPF保持一致。
> - 语音承载的静态PCC规则中的RG与PCF下发的动态规则中的RG相同。
> - PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。

*表1 语音缺省QoS Flow/缺省承载静态PCC策略数据*

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
| [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略类型（POLICYTYPE） | PCC | 本端规划 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
| [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 全局优先级（PRIORITY） | 65535 | 与对端协商 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
| [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md) | 策略名称（POLICYNAME） | pccpolicygrp_signaling | 已配置数据中获取 | - “POLICYTYPE”设置为“PCC”时，“POLICYNAME”使用[**ADD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/增加PCC策略组（ADD PCCPOLICYGRP）_09897173.md)定义的PCCPOLICYGRPNM。<br>- “POLICYTYPE”设置为“QOS”时，“POLICYNAME”使用[**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)定义的QOSPROPNAME。<br>- 配置“PRIORITY”时需要注意：PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 |
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

*表2 语音专有QoS Flow/专有承载静态PCC策略数据*

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
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 保证的上行比特率（GBRUPLKVALUE） | 64 | 固定取值 | PCF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCF Bypass期间，创建专有QoSFlow/专有承载时，使用SMF/PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 保证的下行比特率（GBRDNLKVALUE） | 64 | 固定取值 | PCF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCF Bypass期间，创建专有QoSFlow/专有承载时，使用SMF/PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 最大上行比特率（MBRUPLKVALUE） | 64 | 固定取值 | PCF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCF Bypass期间，创建专有QoSFlow/专有承载时，使用SMF/PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 最大下行比特率（MBRDNLKVALUE） | 64 | 固定取值 | PCF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。<br>PCF Bypass期间，创建专有QoSFlow/专有承载时，使用SMF/PGW-C上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QoS属性类型（QOSTYPE） | QOS_FLOW_PARA | 本端规划 | 5G用户使用QOS_FLOW_PARA，2/3/4G用户使用QOS_BEARER_PARA。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 分配保留优先级（ARPVALUE） | 2 | 本端规划 | 值越小优先级越高。 |
| [**ADD QOSPROP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | 5G QoS标识（FQI） | 1 | 本端规划 | “QOSTYPE”<br>为<br>“QOS_FLOW_PARA”<br>时需要规划。 |
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

*表3 PCF Bypass条件数据*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) | N7 Failover功能开关（N7FAILOVERSW） | ENABLE | 与对端协商 | 策略接口使用N7接口且PCF采用主备容灾组网时，使能N7接口failover功能。 |
| **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | 选择PCRF/PCF失败动作（SELPEERFAILACT） | ROLLBACK | 本端规划 | 配置PCF故障处理动作。<br>当SMF和PCF采用Model C/D通信模式时，需要通过<br>“SCPFAILOVERSW”<br>参数配置SCP故障时，SMF进行SCP重选。 |
| **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | Initial流程故障处理动作（INITIALFAILACT） | ROLLBACK | 本端规划 | 配置PCF故障处理动作。<br>当SMF和PCF采用Model C/D通信模式时，需要通过<br>“SCPFAILOVERSW”<br>参数配置SCP故障时，SMF进行SCP重选。 |
| **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | Update流程故障处理动作（UPDATEFAILACT） | ROLLBACK | 本端规划 | 配置PCF故障处理动作。<br>当SMF和PCF采用Model C/D通信模式时，需要通过<br>“SCPFAILOVERSW”<br>参数配置SCP故障时，SMF进行SCP重选。 |
| **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | Update流程故障回滚为Local PCC用户类型（UPDFAILLOCPCC） | INHERIT_PCC | 本端规划 | 配置PCF故障处理动作。<br>当SMF和PCF采用Model C/D通信模式时，需要通过<br>“SCPFAILOVERSW”<br>参数配置SCP故障时，SMF进行SCP重选。 |
| **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)** | SCP故障重选开关（SCPFAILOVERSW） | SCP_FAILOVER | 全网规划 | 配置PCF故障处理动作。<br>当SMF和PCF采用Model C/D通信模式时，需要通过<br>“SCPFAILOVERSW”<br>参数配置SCP故障时，SMF进行SCP重选。 |
| **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** | 用户回滚后在线保持时长（分钟）（HOLDINGTIME） | 30 | 本端规划 | 配置全局Holding Time。 |
| **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** | 随机延迟范围（分钟）（ADJUSTRANGE） | 10 | 本端规划 | 配置全局Holding Time。 |
| [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | PCC模板名称（PCCTEMPNAME） | pcctemplate | 本端规划 | 配置PCC模板中PCF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
| [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | 选择PCRF/PCF失败动作（SELPEERFAILACT） | ROLLBACK | 本端规划 | 配置PCC模板中PCF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
| [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | Initial流程故障处理动作（INITIALFAILACT） | ROLLBACK | 本端规划 | 配置PCC模板中PCF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
| [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | Update流程故障处理动作（UPDATEFAILACT） | ROLLBACK | 本端规划 | 配置PCC模板中PCF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
| [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | Update流程故障回滚为Local PCC用户类型（UPDFAILLOCPCC） | INHERIT_PCC | 本端规划 | 配置PCC模板中PCF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
| [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | 用户回滚后在线保持时长（分钟）（HOLDINGTIME） | 30 | 本端规划 | 配置PCC模板中PCF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
| [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | 随机延迟范围（分钟）（ADJUSTRANGE） | 10 | 本端规划 | 配置PCC模板中PCF故障处理动作、Failover开关和Holding Time。<br>说明：建议IMS语音业务单独使用一个PCC模板。新建模板使用<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>命令；修改已有模板使用<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**<br>命令。 |
| [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>**[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** | N7 Failover功能开关（N7FAILOVERSW） | ENABLE | 与对端协商 | 策略接口使用N7接口且PCF采用主备容灾组网时，设置为<br>“ENABLE”<br>。<br>该开关支持APN粒度（<br>[**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)<br>）和全局粒度（<br>[**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)<br>），请根据实际PCF能力规划。 |
| **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | APN名称（APN） | ims | 全网规划 | 为语音业务绑定PCC模板，配置PCF状态过滤参数。 |
| **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | PCC模板名称（PCCTEMPLATE） | pcctemplate | 本端规划 | 为语音业务绑定PCC模板，配置PCF状态过滤参数。 |
| **[SET APNPCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)** | PCF状态过滤参数（DISCCUSTOM） | MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT | 本端规划 | 为语音业务绑定PCC模板，配置PCF状态过滤参数。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | PCC模板名称（PCCTEMPLATE） | pcctemplate | 已配置数据中获取 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 接口类型（INTFTYPE） | INTFTYPE_N7 | 与对端协商 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | N7返回码（N7RESULTCODEVAL） | 500<br>400<br>504 | 与对端协商 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 设备提供商标识（VENDORID） | 0 | 全网规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | Initial流程处理动作（INITACTION） | FAILOVER<br>LOCALPCC | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | Initial流程回滚后使能Holding-Time（INITHOLDTMSW） | ENABLE | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | Update流程处理动作（UPDATEACTION） | FAILOVER<br>INHERIT_PCC | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | Update流程回滚后使能Holding-Time（UPDHOLDTMSW） | ENABLE | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 直连对端Initial流程处理动作（DIRECTINITACT） | FAILOVER | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 直连对端Update流程处理动作（DIRECTUPDACT） | FAILOVER | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 直连对端Initial流程回滚后使能Holding-Time（DIRECTINITHTSW） | ENABLE | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 直连对端Update流程回滚后使能Holding-Time（DIRECTUPDHTSW） | ENABLE | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
| **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**<br>**[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)** | 直连对端Update流程回滚后使能Holding-Time（DIRECTUPDHTSW） | ENABLE | 本端规划 | 配置对端回复指定结果码后SMF/PGW-C的处理操作。<br>“INTFTYPE”<br>需要根据现网语音业务使用的策略接口进行配置。<br>“N7RESULTCODEVAL”<br>需要与对端PCF/SCP确认，此处取值仅为举例。 |
| **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)** | PCC模板名称（PCCTEMPLATE） | pcctemplate | 本端规划 | 配置在MODELC/D组网场景下，对端回复指定结果码和错误信息后，SMF/PGW-C的处理动作。 |
| **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)** | 组网场景（MODELTYPE） | MODELC<br>MODELD | 本端规划 | 配置在MODELC/D组网场景下，对端回复指定结果码和错误信息后，SMF/PGW-C的处理动作。 |
| **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)** | N7返回码（N7RESULTCODEVAL） | 500<br>502<br>504<br>5XX | 与对端协商 | 配置在MODELC/D组网场景下，对端回复指定结果码和错误信息后，SMF/PGW-C的处理动作。 |
| **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)** | 故障码对应的Protocol or application Error信息（ERRINFO） | NF_SERVICE_FAILOVER<br>NF_DISCOVERY_ERROR\|MAX_SCP_HOPS_REACHED<br>TARGET_NF_NOT_REACHABLE<br>* | 全网规划 | 配置在MODELC/D组网场景下，对端回复指定结果码和错误信息后，SMF/PGW-C的处理动作。 |
| **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)** | Initial流程处理动作（INITACTION） | LOCALPCC<br>FAILOVER | 本端规划 | 配置在MODELC/D组网场景下，对端回复指定结果码和错误信息后，SMF/PGW-C的处理动作。 |
| **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)** | Initial流程回滚后使能Holding-Time（INITHOLDTMSW） | ENABLE | 本端规划 | 配置在MODELC/D组网场景下，对端回复指定结果码和错误信息后，SMF/PGW-C的处理动作。 |
| **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)** | Update流程处理动作（UPDATEACTION） | INHERIT_PCC<br>FAILOVER | 本端规划 | 配置在MODELC/D组网场景下，对端回复指定结果码和错误信息后，SMF/PGW-C的处理动作。 |
| **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)** | Update流程回滚后使能Holding-Time（UPDHOLDTMSW） | ENABLE | 本端规划 | 配置在MODELC/D组网场景下，对端回复指定结果码和错误信息后，SMF/PGW-C的处理动作。 |
| **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)** | Terminate流程处理动作（TERMINACTION） | - | 本端规划 | 配置在MODELC/D组网场景下，对端回复指定结果码和错误信息后，SMF/PGW-C的处理动作。 |
| **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)** | 重新激活请求（REACTREQ） | - | 本端规划 | 配置在MODELC/D组网场景下，对端回复指定结果码和错误信息后，SMF/PGW-C的处理动作。 |
| **[ADD PCCBYPASSCODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加PCC故障场景维持BYPASS状态码配置（ADD PCCBYPASSCODE）_83249518.md)** | PCC模板名称（PCCTEMPLATE） | pcctemplate | 本端规划 | 配置在MODEL C/D组网场景，会话退出PCF Bypass状态时SMF/PGW-C发送探测消息后，收到对端网元返回特定状态码会话继续保持Bypass状态。 |
| **[ADD PCCBYPASSCODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加PCC故障场景维持BYPASS状态码配置（ADD PCCBYPASSCODE）_83249518.md)** | 接口类型（INTFTYPE） | INTFTYPE_N7 | 与对端协商 | 配置在MODEL C/D组网场景，会话退出PCF Bypass状态时SMF/PGW-C发送探测消息后，收到对端网元返回特定状态码会话继续保持Bypass状态。 |
| **[ADD PCCBYPASSCODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加PCC故障场景维持BYPASS状态码配置（ADD PCCBYPASSCODE）_83249518.md)** | N7返回码（N7RESULTCODEVAL） | 5xx | 与对端协商 | 配置在MODEL C/D组网场景，会话退出PCF Bypass状态时SMF/PGW-C发送探测消息后，收到对端网元返回特定状态码会话继续保持Bypass状态。 |
| **[ADD PCCBYPASSCODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加PCC故障场景维持BYPASS状态码配置（ADD PCCBYPASSCODE）_83249518.md)** | 错误信息（ERRINFO） | - | 全网规划 | 配置在MODEL C/D组网场景，会话退出PCF Bypass状态时SMF/PGW-C发送探测消息后，收到对端网元返回特定状态码会话继续保持Bypass状态。 |
| **[SET IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/设置语音PCF_PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）_49496669.md)** | 无语音专载时的故障非预期Bypass场景的异常处理动作（ACTNODEDBEARER） | TERMINATE | 本端规划 | 配置SMF分别在有、无语音专有承载时的处理动作，以及在SMF和PCF非直连场景没有语音专有承载时，会话退出PCF Bypass状态发送探测消息。 |
| **[SET IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/设置语音PCF_PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）_49496669.md)** | 存在语音专载时的更新流程故障非预期Bypass场景的异常处理动作（ACTWITDEDBEARER） | FASTROLLBACK | 本端规划 | 配置SMF分别在有、无语音专有承载时的处理动作，以及在SMF和PCF非直连场景没有语音专有承载时，会话退出PCF Bypass状态发送探测消息。 |
| **[SET IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/设置语音PCF_PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）_49496669.md)** | 存在语音专载时更新流程故障回滚为Local PCC用户类型（FAILLOCPCC） | INHERIT_PCC | 全网规划 | 配置SMF分别在有、无语音专有承载时的处理动作，以及在SMF和PCF非直连场景没有语音专有承载时，会话退出PCF Bypass状态发送探测消息。 |
| **[SET IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/设置语音PCF_PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）_49496669.md)** | 非直连场景下退出Bypass发送探测消息开关（TSTUPDATEREQSW） | ENABLE | 本端规划 | 配置SMF分别在有、无语音专有承载时的处理动作，以及在SMF和PCF非直连场景没有语音专有承载时，会话退出PCF Bypass状态发送探测消息。 |
| [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | APN名称（APN） | ims | 全网规划 | （可选）针对指定的DNN绑定PCC模板。 |
| [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | PCC模板名称（PCCTEMPLATE） | pcctemplate | 本端规划 | （可选）针对指定的DNN绑定PCC模板。 |
| [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | APN名称（APN） | ims | 已配置数据中获取 | 设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除QoS Flow，删除QoS Flow后还需要重新创建QoS Flow。<br>此处以5分钟为例，请以局点规划数据为准。 |
| [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 继承默认开关（INHERIT） | NO | 本端规划 | 设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除QoS Flow，删除QoS Flow后还需要重新创建QoS Flow。<br>此处以5分钟为例，请以局点规划数据为准。 |
| [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | H-SMF空闲上下文核查级别（HSMFTIMERLEVEL） | QOSFLOW | 固定取值 | 设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除QoS Flow，删除QoS Flow后还需要重新创建QoS Flow。<br>此处以5分钟为例，请以局点规划数据为准。 |
| [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 专有QoS Flow空闲定时器时长(min)（DEDQFIDLETIMER） | 5 | 本端规划 | 设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。<br>说明：根据业务模型进行设置。设置过大，会长时间占用上下文资源；设置过小，会强制删除QoS Flow，删除QoS Flow后还需要重新创建QoS Flow。<br>此处以5分钟为例，请以局点规划数据为准。 |
| [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) | APN名称（APN） | ims | 已配置数据中获取 | 配置专有GBR类型QoS Flow的延迟释放时长。在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），SMF立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。 |
| [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) | NgApCause组（NGAPCAUSEGROUP） | RADIO_NETWORK | 固定取值 | 配置专有GBR类型QoS Flow的延迟释放时长。在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），SMF立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。 |
| [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) | NgApCause值（NGAPCAUSEVALUE） | 21 | 固定取值 | 配置专有GBR类型QoS Flow的延迟释放时长。在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），SMF立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。 |
| [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) | 专有GBR类型QoS Flow处理策略（QFPLCY） | DELAY_RELEASE | 固定取值 | 配置专有GBR类型QoS Flow的延迟释放时长。在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），SMF立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。 |
| [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md) | 延迟释放专有GBR类型QoS Flow时长(秒)（DELAYTIMER） | 60 | 全网规划 | 配置专有GBR类型QoS Flow的延迟释放时长。在收到UE Context Release（CauseRadioNetwork：radio-connection-with-ue-lost），SMF立即释放专有QoS Flow可能影响进行中的业务（如语音）时，需要设置延迟释放时间。 |

*表4 相关软参数据*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 数据类型（DT） | Dw | 本端规划 | 配置在HoldingTime超时时，用户会话中有语音专有QoS Flow/专有承载时不去活会话，重启HoldingTime定时器；没有语音专有QoS Flow/专有承载时去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | Dword索引（DWORDNUM） | 519 | 本端规划 | 配置在HoldingTime超时时，用户会话中有语音专有QoS Flow/专有承载时不去活会话，重启HoldingTime定时器；没有语音专有QoS Flow/专有承载时去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 软参记录值（VALUE） | 1 | 本端规划 | 配置在HoldingTime超时时，用户会话中有语音专有QoS Flow/专有承载时不去活会话，重启HoldingTime定时器；没有语音专有QoS Flow/专有承载时去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 比特位（POSITION） | 5 | 本端规划 | 配置在HoldingTime超时时，用户会话中有语音专有QoS Flow/专有承载时不去活会话，重启HoldingTime定时器；没有语音专有QoS Flow/专有承载时去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 数据类型（DT） | Dw | 本端规划 | 配置SMF/PGW-C在激活流程查询PCF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活用户）生效。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | Dword索引（DWORDNUM） | 519 | 本端规划 | 配置SMF/PGW-C在激活流程查询PCF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活用户）生效。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 软参记录值（VALUE） | 1 | 本端规划 | 配置SMF/PGW-C在激活流程查询PCF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活用户）生效。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 比特位（POSITION） | 9 | 本端规划 | 配置SMF/PGW-C在激活流程查询PCF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活用户）生效。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 数据类型（DT） | Dw | 本端规划 | 配置语音PCF进入Bypass后，HoldingTime定时器启动三次后不强制去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | Dword索引（DWORDNUM） | 544 | 本端规划 | 配置语音PCF进入Bypass后，HoldingTime定时器启动三次后不强制去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 软参记录值（VALUE） | 1 | 本端规划 | 配置语音PCF进入Bypass后，HoldingTime定时器启动三次后不强制去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 比特位（POSITION） | 17 | 本端规划 | 配置语音PCF进入Bypass后，HoldingTime定时器启动三次后不强制去活会话。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 数据类型（DT） | Dw | 本端规划 | 配置SMF对接语音PCF时将业务触发专载的双向流进行拆分处理。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | Dword索引（DWORDNUM） | 545 | 本端规划 | 配置SMF对接语音PCF时将业务触发专载的双向流进行拆分处理。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 软参记录值（VALUE） | 1 | 本端规划 | 配置SMF对接语音PCF时将业务触发专载的双向流进行拆分处理。 |
| **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)** | 比特位（POSITION） | 18 | 本端规划 | 配置SMF对接语音PCF时将业务触发专载的双向流进行拆分处理。 |
| **[SET COMMONSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置公共软件参数比特位（SET COMMONSOFTPARAOFBIT）_26494601.md)** | 数据类型（DT） | DwCom | 固定取值 | 配置SMF感知除SMF、CHF、AUSF、UDN、NWDAF外其他NF的状态变更。DWORD3 BIT13固定取值为1。 |
| **[SET COMMONSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置公共软件参数比特位（SET COMMONSOFTPARAOFBIT）_26494601.md)** | Common Dword索引（DWORDCOMNUM） | 3 | 固定取值 | 配置SMF感知除SMF、CHF、AUSF、UDN、NWDAF外其他NF的状态变更。DWORD3 BIT13固定取值为1。 |
| **[SET COMMONSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置公共软件参数比特位（SET COMMONSOFTPARAOFBIT）_26494601.md)** | 软参记录值（VALUE） | 1 | 固定取值 | 配置SMF感知除SMF、CHF、AUSF、UDN、NWDAF外其他NF的状态变更。DWORD3 BIT13固定取值为1。 |
| **[SET COMMONSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置公共软件参数比特位（SET COMMONSOFTPARAOFBIT）_26494601.md)** | 比特位（POSITION） | 13 | 固定取值 | 配置SMF感知除SMF、CHF、AUSF、UDN、NWDAF外其他NF的状态变更。DWORD3 BIT13固定取值为1。 |

## [操作步骤](#ZH-CN_OPI_0000001932852169)

全部展开

1. **可选：**
  配置语音缺省QoS Flow/缺省承载静态PCC策略。

  > **说明**
  > 仅当局点未配置语音缺省QoS Flow/缺省承载静态PCC策略时，执行本步骤。否则，跳过本步骤。

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
  配置语音专有QoS Flow/缺省承载静态PCC策略。

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
  配置PCF Bypass条件。

  a. 配置全局Failover开关。
      [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    b. 配置全局PCF故障处理动作。
      **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)**
    c. 配置全局Holding Time。
      **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**
    d. 基于PCC模板配置故障处理动作、failover开关和Holding Time。
      > **说明**
      > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。
      [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) / **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)**
    e. 为语音业务绑定PCC模板，配置PCF状态过滤参数。
      [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    f. 配置对端PCF/SCP回复指定结果码后SMF/PGW-C的处理操作。
      > **说明**
      > 具体结果码需要与对端PCF/SCP确认。
      **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)** / **[MOD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/修改返回码控制（MOD RESULTCODECTRL）_09897085.md)**
    g. **可选：**配置在MODELC/D组网场景下，对端回复指定结果码和错误信息后，SMF/PGW-C的处理动作。
      > **说明**
      > 仅在MODELC/D组网场景需要进行此配置。
      **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)**
    h. **可选：**配置在MODEL C/D组网场景，会话退出PCF Bypass状态时SMF/PGW-C发送探测消息后，收到对端网元返回特定状态码会话继续保持Bypass状态。
      > **说明**
      > 仅在MODELC/D组网场景需要进行此配置。
      **[ADD PCCBYPASSCODE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加PCC故障场景维持BYPASS状态码配置（ADD PCCBYPASSCODE）_83249518.md)**
    i. 配置SMF分别在有、无语音专有承载时的处理动作，以及在SMF和PCF非直连场景没有语音专有承载时，会话退出PCF Bypass状态发送探测消息。
      **[SET IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/设置语音PCF_PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）_49496669.md)**
    j. **可选：**为DNN绑定PCC模板，如果已经绑定过，则不需要执行该步骤。
      [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    k. 设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。
      [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
    l. 配置专有GBR类型QoS Flow的延迟释放时长。
      [**ADD APNDEACTQFPLCY**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话策略管理/5GC QoS Flow管理拓展功能/增加基于APN去活用户面专有QoS Flow策略（ADD APNDEACTQFPLCY）_38692981.md)
4.
  配置相关软参。

  a. 通过软参 [DWORD519 Bit5](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/PCC策略控制管理/DWORD519 BIT5 控制HoldingTime超时时是否去活有语音专载的会话_98344879.md) 配置在HoldingTime超时时，用户会话中有语音专有QoS Flow/专有承载时不去活会话，重启HoldingTime定时器；没有语音专有QoS Flow/专有承载时去活会话。
      **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)**
    b. 通过软参 [DWORD519 Bit9](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/PCC策略控制管理/DWORD519 Bit9控制激活流程查询PCF失败发生回滚时，HoldingTime功能是否生效_97903713.md) 配置在SMF/PGW-C激活流程查询PCF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活会话）生效。
      **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)**
    c. **可选：**通过软参 [DWORD544 BIT17](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/PCC策略控制管理/DWORD544 BIT17 控制语音PCF_PCRF进入Bypass后，HoldingTime启动三次后是否强制去活_42799282.md) 配置语音PCF进入Bypass后，HoldingTime定时器启动三次后是否强制去活会话。
      **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)**
    d. 通过软参 [DWORD545 BIT18](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/PCC策略控制管理/DWORD545 BIT18 控制UNC对接语音PCRF_PCF时是否将业务触发专载的双向流进行拆分处理_95599886.md) 配置SMF对接语音PCF时将业务触发专载的双向流进行拆分处理。
      **[SET SMFSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软件参数比特位（SET SMFSOFTPARAOFBIT）_09652696.md)**
    e. 通过软参 [DWORD3 BIT13](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（5G业务公共）/公共软参/DWORD3 BIT13 控制NF是否感知除SMF、CHF、AUSF、UDN、NWDAF外其他NF的状态变更_11112308.md) 配置SMF感知除SMF、CHF、AUSF、UDN、NWDAF外其他NF的状态变更。
      **[SET COMMONSOFTPARAOFBIT](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置公共软件参数比特位（SET COMMONSOFTPARAOFBIT）_26494601.md)**

## [任务示例](#ZH-CN_OPI_0000001932852169)

任务描述

任务一：SMF/PGW-C上没有配置语音缺省QoS Flow/缺省承载静态PCC策略，在SMF/PGW-C上激活语音PCF/PCRF故障Bypass功能。

任务二：SMF/PGW-C上已配置语音缺省QoS Flow/缺省承载静态PCC策略，APN ims绑定了User Profile组upg_ims，User Profile组中绑定了User Profile upg_ims，在当前配置基础上激活语音PCF/PCRF故障Bypass功能。

脚本

- **任务一：SMF/PGW-C上没有配置语音缺省QoS Flow/缺省承载静态PCC策略，在SMF/PGW-C上激活语音PCF/PCRF故障Bypass功能。**
    1. 配置语音缺省QoS Flow/缺省承载静态PCC策略。
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
    2. 配置语音专有QoS Flow/专有承载静态PCC策略。
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
      //配置语音专有QoS Flow/专有承载的QoS参数。

      ```
      ADD QOSPROP:QOSPROPNAME="qosprop_voice", EMPCAP=ENABLE, EMPVUL=DISABLE, GBRUPLKVALUE=64, GBRDNLKVALUE=64, MBRUPLKVALUE=64, MBRDNLKVALUE=64, QOSTYPE=QOS_FLOW_PARA, FQI=1, ARPVALUE=2, QOSURRNAME="urr_qos_01";
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
    3. 配置PCF Bypass条件。
          - 策略接口为N7接口，直连组网
            //配置全局Failover开关。

            ```
            SET PCCFUNC:N7FAILOVERSW=ENABLE;
            ```
            //配置全局PCF故障处理动作。

            ```
            SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC;
            ```
            //配置全局Holding Time。

            ```
            SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10;
            ```
            //基于存在的PCC模板配置故障处理动作、failover开关和Holding Time。

            > **说明**
            > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。

            ```
            MOD PCCTEMPLATE:PCCTEMPNAME="pcctemplate", SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, HOLDINGTIME=30, ADJUSTRANGE=10, N7FAILOVERSW=ENABLE;
            ```
            //为语音业务绑定PCC模板，配置PCF状态过滤参数。

            ```
            SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate", DISCCUSTOM=MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT;
            ```
            //配置对端PCF回复指定结果码后SMF/PGW-C的处理操作。

            > **说明**
            > 具体结果码需要与对端PCF/SCP确认。

            ```
            ADD RESULTCODECTRL:N7RESULTCODEVAL="504", PCCTEMPLATE="pcctemplate", DIRECTINITACT=LOCALPCC, DIRECTINITHTSW=ENABLE, DIRECTUPDACT=INHERIT_PCC, DIRECTUPDHTSW=ENABLE, INTFTYPE=INTFTYPE_N7;
            ```
            //（可选）为DNN绑定PCC模板，如果已经绑定过，则不需要执行该步骤。

            ```
            SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";
            ```
            //设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。

            ```
            SET APNIDLETIME: APN="ims", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=5;
            ```
            //配置专有GBR类型QoS Flow的延迟释放时长。

            ```
            ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;
            ```
          - 策略接口为N7接口，MODEL C组网
            //配置全局Failover开关。

            ```
            SET PCCFUNC:N7FAILOVERSW=ENABLE;
            ```
            //配置全局PCF故障处理动作。

            ```
            SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, SCPFAILOVERSW=SCP_FAILOVER;
            ```
            //配置全局Holding Time。

            ```
            SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10;
            ```
            //基于存在的PCC模板配置故障处理动作、failover开关和Holding Time。

            > **说明**
            > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。

            ```
            MOD PCCTEMPLATE:PCCTEMPNAME="pcctemplate", SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, HOLDINGTIME=30, ADJUSTRANGE=10, N7FAILOVERSW=ENABLE;
            ```
            //为语音业务绑定PCC模板，配置PCF状态过滤参数。

            ```
            SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate", DISCCUSTOM=MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT;
            ```
            //配置对端PCF回复指定结果码后SMF/PGW-C的处理操作。

            > **说明**
            > 具体结果码需要与对端PCF/SCP确认。

            ```
            ADD RESULTCODECTRL:N7RESULTCODEVAL="504", PCCTEMPLATE="pcctemplate", DIRECTINITACT=LOCALPCC, DIRECTINITHTSW=ENABLE, DIRECTUPDACT=INHERIT_PCC, DIRECTUPDHTSW=ENABLE, INTFTYPE=INTFTYPE_N7;
            ```
            //配置对端SCP回复指定结果码后SMF/PGW-C的处理操作。

            ```
            ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate", MODELTYPE=MODELC, N7RESULTCODEVAL="504", ERRINFO="TARGET_NF_NOT_REACHABLE", INITACTION=LOCALPCC, INITHOLDTMSW=ENABLE, UPDATEACTION=INHERIT_PCC, UPDHOLDTMSW=ENABLE;
            ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate", MODELTYPE=MODELC, N7RESULTCODEVAL="502", ERRINFO="", INITACTION=LOCALPCC, INITHOLDTMSW=ENABLE, UPDATEACTION=INHERIT_PCC, UPDHOLDTMSW=ENABLE;
            ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate", MODELTYPE=MODELC, N7RESULTCODEVAL="5xx", ERRINFO="*", INITACTION=FAILOVER, UPDATEACTION=FAILOVER;
            ```
            //增加PCC故障场景维持BYPASS状态码配置。此处理取值仅为举例。

            ```
            ADD PCCBYPASSCODE:PCCTEMPLATE="pcctemplate", INTFTYPE=INTFTYPE_N7, N7RESULTCODEVAL="5xx";
            ```
            //配置SMF分别在有、无语音专有承载时的处理动作，以及在SMF和PCF非直连场景没有语音专有承载时，会话退出PCRF Bypass状态发送探测消息。

            ```
            SET IMSBYPASSFUNC: ACTNODEDBEARER=TERMINATE, ACTWITDEDBEARER=FASTROLLBACK, FAILLOCPCC=INHERIT_PCC, TSTUPDATEREQSW=ENABLE;
            ```
            //（可选）为DNN绑定PCC模板，如果已经绑定过，则不需要执行该步骤。

            ```
            SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";
            ```
            //设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。

            ```
            SET APNIDLETIME: APN="ims", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=5;
            ```
            //配置专有GBR类型QoS Flow的延迟释放时长。

            ```
            ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;
            ```
          - 策略接口为N7接口，MODEL D组网
            //配置全局Failover开关。

            ```
            SET PCCFUNC:N7FAILOVERSW=ENABLE;
            ```
            //配置全局PCF故障处理动作。

            ```
            SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, SCPFAILOVERSW=SCP_FAILOVER;
            ```
            //配置全局Holding Time。

            ```
            SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10;
            ```
            //基于存在的PCC模板配置故障处理动作、failover开关和Holding Time。

            > **说明**
            > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。

            ```
            MOD PCCTEMPLATE:PCCTEMPNAME="pcctemplate", SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, HOLDINGTIME=30, ADJUSTRANGE=10, N7FAILOVERSW=ENABLE;
            ```
            //为语音业务绑定PCC模板，配置PCF状态过滤参数。

            ```
            SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate", DISCCUSTOM=MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT;
            ```
            //配置对端PCF回复指定结果码后SMF/PGW-C的处理操作。

            > **说明**
            > 具体结果码需要与对端PCF/SCP确认。

            ```
            ADD RESULTCODECTRL:N7RESULTCODEVAL="504", PCCTEMPLATE="pcctemplate", DIRECTINITACT=LOCALPCC, DIRECTINITHTSW=ENABLE, DIRECTUPDACT=INHERIT_PCC, DIRECTUPDHTSW=ENABLE, INTFTYPE=INTFTYPE_N7;
            ```
            //配置对端SCP回复指定结果码后SMF/PGW-C的处理操作。

            ```
            ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate", MODELTYPE=MODELD, N7RESULTCODEVAL="500", ERRINFO="NF_SERVICE_FAILOVER", INITACTION=LOCALPCC, INITHOLDTMSW=ENABLE, UPDATEACTION=INHERIT_PCC, UPDHOLDTMSW=ENABLE;
            ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate", MODELTYPE=MODELD, N7RESULTCODEVAL="504", ERRINFO="TARGET_NF_NOT_REACHABLE", INITACTION=LOCALPCC, INITHOLDTMSW=ENABLE, UPDATEACTION=INHERIT_PCC, UPDHOLDTMSW=ENABLE;
            ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate", MODELTYPE=MODELD, N7RESULTCODEVAL="502", ERRINFO="NF_DISCOVERY_ERROR|MAX_SCP_HOPS_REACHED", INITACTION=LOCALPCC, INITHOLDTMSW=ENABLE, UPDATEACTION=INHERIT_PCC, UPDHOLDTMSW=ENABLE;
            ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate", MODELTYPE=MODELD, N7RESULTCODEVAL="5xx", ERRINFO="*", INITACTION=FAILOVER, UPDATEACTION=FAILOVER;
            ```
            //增加PCC故障场景维持BYPASS状态码配置。此处理取值仅为举例。

            ```
            ADD PCCBYPASSCODE:PCCTEMPLATE="pcctemplate", INTFTYPE=INTFTYPE_N7, N7RESULTCODEVAL="5xx";
            ```
            //配置SMF分别在有、无语音专有承载时的处理动作，以及在SMF和PCF非直连场景没有语音专有承载时，会话退出PCRF Bypass状态发送探测消息。

            ```
            SET IMSBYPASSFUNC: ACTNODEDBEARER=TERMINATE, ACTWITDEDBEARER=FASTROLLBACK, FAILLOCPCC=INHERIT_PCC, TSTUPDATEREQSW=ENABLE;
            ```
            //（可选）为DNN绑定PCC模板，如果已经绑定过，则不需要执行该步骤。

            ```
            SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";
            ```
            //设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。

            ```
            SET APNIDLETIME: APN="ims", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=5;
            ```
            //配置专有GBR类型QoS Flow的延迟释放时长。

            ```
            ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;
            ```
    4. 配置相关软参。
      //配置在HoldingTime超时时，用户会话中有语音专有QoS Flow/专有承载时不去活会话，重启HoldingTime定时器；没有语音专有QoS Flow/专有承载时去活会话。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=519, VALUE=VALUE_1, POSITION=5;
      ```
      //配置SMF/PGW-C在激活流程查询PCF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活会话）生效。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=519, VALUE=VALUE_1, POSITION=9;
      ```
      //（可选）配置语音PCF进入Bypass后，HoldingTime定时器启动三次后不强制去活会话。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=544, VALUE=VALUE_1, POSITION=17;
      ```
      //配置SMF对接语音PCF时将业务触发专载的双向流进行拆分处理。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=545, VALUE=VALUE_1, POSITION=18;
      ```
      //配置SMF感知除SMF、CHF、AUSF、UDN、NWDAF外其他NF的状态变更。

      ```
      SET COMMONSOFTPARAOFBIT: DT=DwCom, DWORDCOMNUM=3, VALUE=VALUE_1, POSITION=13;
      ```
- **任务二：SMF/PGW-C上已配置语音缺省QoS Flow/缺省承载静态PCC策略，APN ims绑定了User Profile组upg_ims，User Profile组中绑定了User Profile upg_ims，在当前配置基础上激活语音PCF/PCRF故障Bypass功能。**
    1. 配置语音专有QoS Flow/专有承载静态PCC策略。
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
      //配置语音专有QoS Flow/专有承载的QoS参数。

      ```
      ADD QOSPROP:QOSPROPNAME="qosprop_voice", EMPCAP=ENABLE, EMPVUL=DISABLE, GBRUPLKVALUE=64, GBRDNLKVALUE=64, MBRUPLKVALUE=64, MBRDNLKVALUE=64, QOSTYPE=QOS_FLOW_PARA, FQI=1, ARPVALUE=2, QOSURRNAME="urr_qos_01";
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
    2. 配置PCF Bypass条件。
          - 策略接口为N7接口，直连组网
            //配置全局Failover开关。

            ```
            SET PCCFUNC:N7FAILOVERSW=ENABLE;
            ```
            //配置全局PCF故障处理动作。

            ```
            SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC;
            ```
            //配置全局Holding Time。

            ```
            SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10;
            ```
            //基于存在的PCC模板配置故障处理动作、failover开关和Holding Time。

            > **说明**
            > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。

            ```
            MOD PCCTEMPLATE:PCCTEMPNAME="pcctemplate", SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, HOLDINGTIME=30, ADJUSTRANGE=10, N7FAILOVERSW=ENABLE;
            ```
            //为语音业务绑定PCC模板，配置PCF状态过滤参数。

            ```
            SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate", DISCCUSTOM=MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT;
            ```
            //配置对端PCF回复指定结果码后SMF/PGW-C的处理操作。

            > **说明**
            > 具体结果码需要与对端PCF/SCP确认。

            ```
            ADD RESULTCODECTRL:N7RESULTCODEVAL="504", PCCTEMPLATE="pcctemplate", DIRECTINITACT=LOCALPCC, DIRECTINITHTSW=ENABLE, DIRECTUPDACT=INHERIT_PCC, DIRECTUPDHTSW=ENABLE, INTFTYPE=INTFTYPE_N7;
            ```
            //（可选）为DNN绑定PCC模板，如果已经绑定过，则不需要执行该步骤。

            ```
            SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";
            ```
            //设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。

            ```
            SET APNIDLETIME: APN="ims", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=5;
            ```
            //配置专有GBR类型QoS Flow的延迟释放时长。

            ```
            ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;
            ```
          - 策略接口为N7接口，MODEL C组网
            //配置全局Failover开关。

            ```
            SET PCCFUNC:N7FAILOVERSW=ENABLE;
            ```
            //配置全局PCF故障处理动作。

            ```
            SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, SCPFAILOVERSW=SCP_FAILOVER;
            ```
            //配置全局Holding Time。

            ```
            SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10;
            ```
            //基于存在的PCC模板配置故障处理动作、failover开关和Holding Time。

            > **说明**
            > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。

            ```
            MOD PCCTEMPLATE:PCCTEMPNAME="pcctemplate", SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, HOLDINGTIME=30, ADJUSTRANGE=10, N7FAILOVERSW=ENABLE;
            ```
            //为语音业务绑定PCC模板，配置PCF状态过滤参数。

            ```
            SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate", DISCCUSTOM=MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT;
            ```
            //配置对端PCF回复指定结果码后SMF/PGW-C的处理操作。

            > **说明**
            > 具体结果码需要与对端PCF/SCP确认。

            ```
            ADD RESULTCODECTRL:N7RESULTCODEVAL="504", PCCTEMPLATE="pcctemplate", DIRECTINITACT=LOCALPCC, DIRECTINITHTSW=ENABLE, DIRECTUPDACT=INHERIT_PCC, DIRECTUPDHTSW=ENABLE, INTFTYPE=INTFTYPE_N7;
            ```
            //配置对端SCP回复指定结果码后SMF/PGW-C的处理操作。

            ```
            ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate", MODELTYPE=MODELC, N7RESULTCODEVAL="504", ERRINFO="TARGET_NF_NOT_REACHABLE", INITACTION=LOCALPCC, INITHOLDTMSW=ENABLE, UPDATEACTION=INHERIT_PCC, UPDHOLDTMSW=ENABLE;
            ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate", MODELTYPE=MODELC, N7RESULTCODEVAL="502", ERRINFO="", INITACTION=LOCALPCC, INITHOLDTMSW=ENABLE, UPDATEACTION=INHERIT_PCC, UPDHOLDTMSW=ENABLE;
            ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate", MODELTYPE=MODELC, N7RESULTCODEVAL="5xx", ERRINFO="*", INITACTION=FAILOVER, UPDATEACTION=FAILOVER;
            ```
            //增加PCC故障场景维持BYPASS状态码配置。此处理取值仅为举例。

            ```
            ADD PCCBYPASSCODE:PCCTEMPLATE="pcctemplate", INTFTYPE=INTFTYPE_N7, N7RESULTCODEVAL="5xx";
            ```
            //配置SMF分别在有、无语音专有承载时的处理动作，以及在SMF和PCF非直连场景没有语音专有承载时，会话退出PCRF Bypass状态发送探测消息。

            ```
            SET IMSBYPASSFUNC: ACTNODEDBEARER=TERMINATE, ACTWITDEDBEARER=FASTROLLBACK, FAILLOCPCC=INHERIT_PCC, TSTUPDATEREQSW=ENABLE;
            ```
            //（可选）为DNN绑定PCC模板，如果已经绑定过，则不需要执行该步骤。

            ```
            SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";
            ```
            //设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。

            ```
            SET APNIDLETIME: APN="ims", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=5;
            ```
            //配置专有GBR类型QoS Flow的延迟释放时长。

            ```
            ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;
            ```
          - 策略接口为N7接口，MODEL D组网
            //配置全局Failover开关。

            ```
            SET PCCFUNC:N7FAILOVERSW=ENABLE;
            ```
            //配置全局PCF故障处理动作。

            ```
            SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, SCPFAILOVERSW=SCP_FAILOVER;
            ```
            //配置全局Holding Time。

            ```
            SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10;
            ```
            //基于存在的PCC模板配置故障处理动作、failover开关和Holding Time。

            > **说明**
            > 建议IMS语音业务单独使用一个PCC模板。新建模板使用 [**ADD PCCTEMPLATE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令；修改已有模板使用 **[MOD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/修改PCC模板（MOD PCCTEMPLATE）_09897065.md)** 命令。

            ```
            MOD PCCTEMPLATE:PCCTEMPNAME="pcctemplate", SELPEERFAILACT=ROLLBACK, INITIALFAILACT=ROLLBACK, UPDATEFAILACT=ROLLBACK, UPDFAILLOCPCC=INHERIT_PCC, HOLDINGTIME=30, ADJUSTRANGE=10, N7FAILOVERSW=ENABLE;
            ```
            //为语音业务绑定PCC模板，配置PCF状态过滤参数。

            ```
            SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate", DISCCUSTOM=MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT;
            ```
            //配置对端PCF回复指定结果码后SMF/PGW-C的处理操作。

            > **说明**
            > 具体结果码需要与对端PCF/SCP确认。

            ```
            ADD RESULTCODECTRL:N7RESULTCODEVAL="504", PCCTEMPLATE="pcctemplate", DIRECTINITACT=LOCALPCC, DIRECTINITHTSW=ENABLE, DIRECTUPDACT=INHERIT_PCC, DIRECTUPDHTSW=ENABLE, INTFTYPE=INTFTYPE_N7;
            ```
            //配置对端SCP回复指定结果码后SMF/PGW-C的处理操作。

            ```
            ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate", MODELTYPE=MODELD, N7RESULTCODEVAL="500", ERRINFO="NF_SERVICE_FAILOVER", INITACTION=LOCALPCC, INITHOLDTMSW=ENABLE, UPDATEACTION=INHERIT_PCC, UPDHOLDTMSW=ENABLE;
            ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate", MODELTYPE=MODELD, N7RESULTCODEVAL="504", ERRINFO="TARGET_NF_NOT_REACHABLE", INITACTION=LOCALPCC, INITHOLDTMSW=ENABLE, UPDATEACTION=INHERIT_PCC, UPDHOLDTMSW=ENABLE;
            ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate", MODELTYPE=MODELD, N7RESULTCODEVAL="502", ERRINFO="NF_DISCOVERY_ERROR|MAX_SCP_HOPS_REACHED", INITACTION=LOCALPCC, INITHOLDTMSW=ENABLE, UPDATEACTION=INHERIT_PCC, UPDHOLDTMSW=ENABLE;
            ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate", MODELTYPE=MODELD, N7RESULTCODEVAL="5xx", ERRINFO="*", INITACTION=FAILOVER, UPDATEACTION=FAILOVER;
            ```
            //增加PCC故障场景维持BYPASS状态码配置。此处理取值仅为举例。

            ```
            ADD PCCBYPASSCODE:PCCTEMPLATE="pcctemplate", INTFTYPE=INTFTYPE_N7, N7RESULTCODEVAL="5xx";
            ```
            //配置SMF分别在有、无语音专有承载时的处理动作，以及在SMF和PCF非直连场景没有语音专有承载时，会话退出PCRF Bypass状态发送探测消息。

            ```
            SET IMSBYPASSFUNC: ACTNODEDBEARER=TERMINATE, ACTWITDEDBEARER=FASTROLLBACK, FAILLOCPCC=INHERIT_PCC, TSTUPDATEREQSW=ENABLE;
            ```
            //（可选）为DNN绑定PCC模板，如果已经绑定过，则不需要执行该步骤。

            ```
            SET APNPCCFUNC:APN="ims", PCCTEMPLATE="pcctemplate";
            ```
            //设置专有QoS Flow空闲定时器时长，在呼叫结束，业务空闲超过该时长后可以删除QoS Flow。

            ```
            SET APNIDLETIME: APN="ims", INHERIT=NO, HSMFTIMERLEVEL=QOSFLOW, DEDQFIDLETIMER=5;
            ```
            //配置专有GBR类型QoS Flow的延迟释放时长。

            ```
            ADD APNDEACTQFPLCY: APN="ims", NGAPCAUSEGROUP=RADIO_NETWORK, NGAPCAUSEVALUE=21, QFPLCY=DELAY_RELEASE, DELAYTIMER=60;
            ```
    3. 配置相关软参。
      //配置在HoldingTime超时时，用户会话中有语音专有QoS Flow/专有承载时不去活会话，重启HoldingTime定时器；没有语音专有QoS Flow/专有承载时去活会话。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=519, VALUE=VALUE_1, POSITION=5;
      ```
      //配置SMF/PGW-C在激活流程查询PCF失败发生回滚时，HoldingTime功能（当HoldingTime超时时，去活会话）生效。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=519, VALUE=VALUE_1, POSITION=9;
      ```
      //（可选）配置语音PCF进入Bypass后，HoldingTime定时器启动三次后不强制去活会话。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=544, VALUE=VALUE_1, POSITION=17;
      ```
      //配置SMF对接语音PCF时将业务触发专载的双向流进行拆分处理。

      ```
      SET SMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=545, VALUE=VALUE_1, POSITION=18;
      ```
      //配置SMF感知除SMF、CHF、AUSF、UDN、NWDAF外其他NF的状态变更。

      ```
      SET COMMONSOFTPARAOFBIT: DT=DwCom, DWORDCOMNUM=3, VALUE=VALUE_1, POSITION=13;
      ```
