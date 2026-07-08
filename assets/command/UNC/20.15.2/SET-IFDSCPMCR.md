---
id: UNC@20.15.2@MMLCommand@SET IFDSCPMCR
type: MMLCommand
name: SET IFDSCPMCR（设置接口DSCP配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IFDSCPMCR
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- 接口DSCP管理
- 接口DSCP参数管理
status: active
---

# SET IFDSCPMCR（设置接口DSCP配置）

## 功能

**适用网元：MME**

此命令用于设置MCR对外网元接口发送IP包时的DSCP值。

有关DSCP的内容请参见RFC2474。DSCP总共分成了4类：Class Selector(CS)、Expedited Forwarding(EF)、Assured Forwarding(AF)和Best Effort(BE)。CS（类选择器）的DSCP值后三位为0，EF（加速转发）的DSCP值为101110(46)，AF（确保转发）的DSCP值最后一位为0，BE（默认）的DSCP值为000000(0)。常用的DSCP用法见 [表1](#ZH-CN_MMLREF_0000001171850995__tab1)

相关命令： [**MOD DSCPPRIMCR**](../DSCP优先级映射管理/修改DSCP映射优先级配置表(MOD DSCPPRIMCR)_71731089.md) 。

## 注意事项

- 此命令执行后，当“数据DSCP使用策略”设置为“MODIFY(修改DSCP值)”时，除“SNDCP转GTP数据的DSCP值”立即生效外，其他数据消息的DSCP配置只对新激活的用户生效；信令消息相关的DSCP配置立即生效。
- Iu接口信令面的SCCP层对应的DPC必须与M3UA层（M3LNK）对应的DPC相同，否则会判断为“M3UA_PROTOCOL”参数的DSCP值。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用命令[**DSP LICENSE**](../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTFTP_SHOW | 接口类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于选择信令报文修改DSCP值的接口类型。<br>数据来源：整网规划<br>取值范围：<br>- “DEFAULT(未指定接口)”<br>- “Sdup(Sdup)”<br>系统初始设置值：请参考<br>[表2](#ZH-CN_MMLREF_0000001171850995__tab2)<br>说明：- “Sdup”为“WSFD-201201 MME链式备份”特性新增的MME之间的私有接口，用于实现MME之间用户信息备份，以及MME故障后业务的恢复。 |
| MSGTP | 消息类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于选择使用GTP协议的信令报文的消息类型。<br>前提条件：该参数在<br>“接口类型”<br>为<br>“GTP_PROTOCOL_SIGNALING(使用GTP协议的接口的信令消息)”<br>时配置。<br>数据来源：整网规划<br>取值范围：<br>- “G-PDU_TRIGGERED_GTPU_SIGNALING(GTP数据报文触发的GTPU信令消息)”：是指“Error Indication”和“Supported Extension Headers Notification”消息。该类消息是由数据报文触发的，建议其DSCP值设置为小于“OTHERS(其他消息)”的DSCP值，否则可能会大量挤占信令队列的资源，造成“OTHERS(其他消息)”得不到及时处理，出现链路故障。<br>- “OTHERS(其他消息)”：是指除了“G-PDU_TRIGGERED_GTPU_SIGNALING(GTP数据报文触发的GTPU信令消息)”以外的GTP信令消息。<br>系统初始设置值：请参考<br>[表2](#ZH-CN_MMLREF_0000001171850995__tab2)<br>说明：当参数设置为<br>“OTHERS(其他消息)”<br>时，“逻辑接口DSCP配置”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-111501，license项：LKV2LIDC01）。 |
| DSCPV | DSCP值 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置信令报文的DSCP值。<br>数据来源：整网规划<br>取值范围：0～63<br>系统初始设置值：请参考<br>[表2](#ZH-CN_MMLREF_0000001171850995__tab2) |
| SNDCP2GTP_DATA_DSCP | SNDCP转GTP数据的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置2G数据上行报文（SNDCP转为GTP之前）使用的DSCP值。<br>前提条件：仅在<br>“数据DSCP使用策略”<br>为<br>“TRANSFER(透传DSCP值)”<br>时，2G数据上行报文在Gn/Gp接口填写的DSCP等于本参数的设置。<br>数据来源：整网规划<br>取值范围：0～63<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001171850995__tab3) |
| DATAPOLICY | 数据DSCP使用策略 | 可选必选说明：可选参数<br>参数含义：该参数用于设置数据报文的DSCP值填写策略。<br>数据来源：整网规划<br>取值范围：<br>- “TRANSFER(透传DSCP值)”<br>- “MODIFY(修改DSCP值)”<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001171850995__tab3) |
| CCDSCP | 会话类数据的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置会话类用户的发送数据报文对应的DSCP值。<br>前提条件：该参数在<br>“数据DSCP使用策略”<br>为<br>“MODIFY(修改DSCP值)”<br>时配置。<br>数据来源：整网规划<br>取值范围：<br>- “NC(网络控制)”<br>- “EF(快速转发)”<br>- “AF43(确保转发43)”<br>- “AF42(确保转发42)”<br>- “AF41(确保转发41)”<br>- “AF33(确保转发33)”<br>- “AF32(确保转发32)”<br>- “AF31(确保转发31)”<br>- “AF23(确保转发23)”<br>- “AF22(确保转发22)”<br>- “AF21(确保转发21)”<br>- “AF13(确保转发13)”<br>- “AF12(确保转发12)”<br>- “AF11(确保转发11)”<br>- “BE(尽力转发)”<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001171850995__tab3) |
| SCDSCP | 流类数据的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置流类用户的发送数据报文对应的DSCP值。<br>前提条件：该参数在<br>“数据DSCP使用策略”<br>为<br>“MODIFY(修改DSCP值)”<br>时配置。<br>数据来源：整网规划<br>取值范围：<br>- “NC(网络控制)”<br>- “EF(快速转发)”<br>- “AF43(确保转发43)”<br>- “AF42(确保转发42)”<br>- “AF41(确保转发41)”<br>- “AF33(确保转发33)”<br>- “AF32(确保转发32)”<br>- “AF31(确保转发31)”<br>- “AF23(确保转发23)”<br>- “AF22(确保转发22)”<br>- “AF21(确保转发21)”<br>- “AF13(确保转发13)”<br>- “AF12(确保转发12)”<br>- “AF11(确保转发11)”<br>- “BE(尽力转发)”<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001171850995__tab3) |
| ICTHP1DSCP | 交互类优先级1的数据的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置交互类优先级1的用户的发送数据报文对应的DSCP值。<br>前提条件：该参数在<br>“数据DSCP使用策略”<br>为<br>“MODIFY(修改DSCP值)”<br>时配置。<br>数据来源：整网规划<br>取值范围：<br>- “NC(网络控制)”<br>- “EF(快速转发)”<br>- “AF43(确保转发43)”<br>- “AF42(确保转发42)”<br>- “AF41(确保转发41)”<br>- “AF33(确保转发33)”<br>- “AF32(确保转发32)”<br>- “AF31(确保转发31)”<br>- “AF23(确保转发23)”<br>- “AF22(确保转发22)”<br>- “AF21(确保转发21)”<br>- “AF13(确保转发13)”<br>- “AF12(确保转发12)”<br>- “AF11(确保转发11)”<br>- “BE(尽力转发)”<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001171850995__tab3) |
| ICTHP2DSCP | 交互类优先级2的数据的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置交互类优先级2的用户的发送数据报文对应的DSCP值。<br>前提条件：该参数在<br>“数据DSCP使用策略”<br>为<br>“MODIFY(修改DSCP值)”<br>时配置。<br>数据来源：整网规划<br>取值范围：<br>- “NC(网络控制)”<br>- “EF(快速转发)”<br>- “AF43(确保转发43)”<br>- “AF42(确保转发42)”<br>- “AF41(确保转发41)”<br>- “AF33(确保转发33)”<br>- “AF32(确保转发32)”<br>- “AF31(确保转发31)”<br>- “AF23(确保转发23)”<br>- “AF22(确保转发22)”<br>- “AF21(确保转发21)”<br>- “AF13(确保转发13)”<br>- “AF12(确保转发12)”<br>- “AF11(确保转发11)”<br>- “BE(尽力转发)”<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001171850995__tab3) |
| ICTHP3DSCP | 交互类优先级3的数据的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置交互类优先级3的用户的发送数据报文对应的DSCP值。<br>前提条件：该参数在<br>“数据DSCP使用策略”<br>为<br>“MODIFY(修改DSCP值)”<br>时配置。<br>数据来源：整网规划<br>取值范围：<br>- “NC(网络控制)”<br>- “EF(快速转发)”<br>- “AF43(确保转发43)”<br>- “AF42(确保转发42)”<br>- “AF41(确保转发41)”<br>- “AF33(确保转发33)”<br>- “AF32(确保转发32)”<br>- “AF31(确保转发31)”<br>- “AF23(确保转发23)”<br>- “AF22(确保转发22)”<br>- “AF21(确保转发21)”<br>- “AF13(确保转发13)”<br>- “AF12(确保转发12)”<br>- “AF11(确保转发11)”<br>- “BE(尽力转发)”<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001171850995__tab3) |
| BCDSCP | 背景类数据的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置背景类用户的发送数据报文对应的DSCP值。<br>前提条件：该参数在<br>“数据DSCP使用策略”<br>为<br>“MODIFY(修改DSCP值)”<br>时配置。<br>数据来源：整网规划<br>取值范围：<br>- “NC(网络控制)”<br>- “EF(快速转发)”<br>- “AF43(确保转发43)”<br>- “AF42(确保转发42)”<br>- “AF41(确保转发41)”<br>- “AF33(确保转发33)”<br>- “AF32(确保转发32)”<br>- “AF31(确保转发31)”<br>- “AF23(确保转发23)”<br>- “AF22(确保转发22)”<br>- “AF21(确保转发21)”<br>- “AF13(确保转发13)”<br>- “AF12(确保转发12)”<br>- “AF11(确保转发11)”<br>- “BE(尽力转发)”<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001171850995__tab3) |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IFDSCPMCR]] · 接口DSCP配置（IFDSCPMCR）

## 使用实例

设置 “接口类型” 为 “Sdup(Sdup)” ， “DSCP值” 为 “46” ：

SET IFDSCPMCR: INTFTP_SHOW=Sdup, MSGTP=OTHERS, DSCPV=46;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-IFDSCPMCR.md`
