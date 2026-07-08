# 设置接口DSCP配置(SET IFDSCP)

- [命令功能](#ZH-CN_MMLREF_0000001126306022__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126306022__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126306022__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126306022__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126306022__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126306022__1.3.6.1)
- [参考信息](#ZH-CN_MMLREF_0000001126306022__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126306022)

**适用网元：SGSN、MME**

此命令用于设置 UNC 对外网元接口发送IP包时的DSCP值。

有关DSCP的内容请参见RFC2474。DSCP总共分成了4类：Class Selector(CS)、Expedited Forwarding(EF)、Assured Forwarding(AF)和Best Effort(BE)。CS（类选择器）的DSCP值后三位为0，EF（加速转发）的DSCP值为101110(46)，AF（确保转发）的DSCP值最后一位为0，BE（默认）的DSCP值为000000(0)。常用的DSCP用法见 [表1](#ZH-CN_MMLREF_0000001126306022__tab1)

相关命令： [**MOD DSCPPRI**](../DSCP优先级映射管理/修改DSCP映射优先级配置表(MOD DSCPPRI)_26146208.md) 。

#### [注意事项](#ZH-CN_MMLREF_0000001126306022)

- 系统初次运行时，会执行系统初始设置值。
- 此命令执行后，当“数据DSCP使用策略”设置为“MODIFY(修改DSCP值)”时，除“SNDCP转GTP数据的DSCP值”立即生效外，其他数据消息的DSCP配置只对新激活的用户生效；信令消息相关的DSCP配置立即生效。
- Iu接口信令面的SCCP层对应的DPC必须与M3UA层（M3LNK）对应的DPC相同，否则会判断为“M3UA_PROTOCOL”参数的DSCP值。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126306022)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126306022)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126306022)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGCLS | 消息类别 | 可选必选说明：可选参数<br>参数含义：该参数用于选择修改DSCP值的报文类型。<br>数据来源：整网规划<br>取值范围：<br>- “SIGNALLING(信令消息)”<br>- “DATA(数据消息)”<br>系统初始设置值：请参考<br>[表2](#ZH-CN_MMLREF_0000001126306022__tab2)<br>和<br>[表3](#ZH-CN_MMLREF_0000001126306022__tab3) |
| INTFTP_SHOW | 接口类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于选择信令报文修改DSCP值的接口类型。<br>前提条件：该参数在<br>“消息类别”<br>为<br>“SIGNALLING(信令消息)”<br>时配置。<br>数据来源：整网规划<br>取值范围：<br>- “DEFAULT(未指定接口)”<br>- “S1_MME(S1_MME接口)”<br>- “M3UA_PROTOCOL(使用M3UA协议的接口)”<br>- “GTP_PROTOCOL_SIGNALING(使用GTP协议的接口的信令消息)”<br>- “Diameter_PROTOCOL(使用Diameter协议的接口)”<br>- “Gb_SIGNALING(Gb接口)”<br>- “Ga(Ga接口)”<br>- “Iu_SIGNALING(Iu接口的信令消息)”<br>- “DNS(DNS接口)”<br>- “SLs(SLs接口)”<br>- “SGs(SGs接口)”<br>- “SBc(SBc接口)”<br>- “S102(S102接口)”<br>- “Tm(Tm接口)”<br>系统初始设置值：请参考<br>[表2](#ZH-CN_MMLREF_0000001126306022__tab2)<br>说明：- “M3UA_PROTOCOL(使用M3UA协议的接口)”包含的接口为“Gr/Gf/Gd/Gs/Ge/Lg接口”<br>- “GTP_PROTOCOL_SIGNALING(使用GTP协议的接口的信令消息)”包含的接口为“Gn/Gp/S11/S10/S3/S4/S16/Sm/Sv接口”<br>- “Diameter_PROTOCOL(使用Diameter协议的接口)”包含的接口为“S6a/S6d/S13/SLg接口”<br>- 当参数设置为“Diameter_PROTOCOL(使用Diameter协议的接口)”，“Ga(Ga接口)”，“Iu_SIGNALING(Iu接口的信令消息)”，“DNS(DNS接口)”，“SLs(SLs接口)”，“SGs(SGs接口)”，“SBc(SBc接口)”或“S102(S102接口)”时，或者当参数设置为“GTP_PROTOCOL_SIGNALING(使用GTP协议的接口的信令消息)”且“消息类型”设置为“OTHERS(其他消息)”时，“逻辑接口DSCP配置”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-105004，license部件编码：LKV2LIDC01）。 |
| MSGTP | 消息类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于选择使用GTP协议的信令报文的消息类型。<br>前提条件：该参数在<br>“接口类型”<br>为<br>“GTP_PROTOCOL_SIGNALING(使用GTP协议的接口的信令消息)”<br>时配置。<br>数据来源：整网规划<br>取值范围：<br>- “G-PDU_TRIGGERED_GTPU_SIGNALING(GTP数据报文触发的GTPU信令消息)”：是指“Error Indication”和“Supported Extension Headers Notification”消息。该类消息是由数据报文触发的，建议其DSCP值设置为小于“OTHERS(其他消息)”的DSCP值，否则可能会大量挤占信令队列的资源，造成“OTHERS(其他消息)”得不到及时处理，出现链路故障。<br>- “OTHERS(其他消息)”：是指除了“G-PDU_TRIGGERED_GTPU_SIGNALING(GTP数据报文触发的GTPU信令消息)”以外的GTP信令消息。<br>系统初始设置值：请参考<br>[表2](#ZH-CN_MMLREF_0000001126306022__tab2)<br>说明：当参数设置为<br>“OTHERS(其他消息)”<br>时，“逻辑接口DSCP配置”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-<br>105004<br>，license部件编码：LKV2LIDC01）。 |
| DSCPV | DSCP值 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置信令报文的DSCP值。<br>前提条件：该参数在<br>“消息类别”<br>为<br>“SIGNALLING(信令消息)”<br>时配置。<br>数据来源：整网规划<br>取值范围：0～63<br>系统初始设置值：请参考<br>[表2](#ZH-CN_MMLREF_0000001126306022__tab2) |
| SNDCP2GTP_DATA_DSCP | SNDCP转GTP数据的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置2G数据上行报文（SNDCP转为GTP之前）使用的DSCP值。<br>前提条件：仅在<br>“数据DSCP使用策略”<br>为<br>“TRANSFER(透传DSCP值)”<br>时，2G数据上行报文在Gn/Gp接口填写的DSCP等于本参数的设置。<br>数据来源：整网规划<br>取值范围：0～63<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001126306022__tab3) |
| DATAPOLICY | 数据DSCP使用策略 | 可选必选说明：可选参数<br>参数含义：该参数用于设置数据报文的DSCP值填写策略。<br>数据来源：整网规划<br>取值范围：<br>- “TRANSFER(透传DSCP值)”<br>- “MODIFY(修改DSCP值)”<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001126306022__tab3) |
| CCDSCP | 会话类数据的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置会话类用户的发送数据报文对应的DSCP值。<br>前提条件：该参数在<br>“数据DSCP使用策略”<br>为<br>“MODIFY(修改DSCP值)”<br>时配置。<br>数据来源：整网规划<br>取值范围：<br>- “NC(网络控制)”<br>- “EF(快速转发)”<br>- “AF43(确保转发43)”<br>- “AF42(确保转发42)”<br>- “AF41(确保转发41)”<br>- “AF33(确保转发33)”<br>- “AF32(确保转发32)”<br>- “AF31(确保转发31)”<br>- “AF23(确保转发23)”<br>- “AF22(确保转发22)”<br>- “AF21(确保转发21)”<br>- “AF13(确保转发13)”<br>- “AF12(确保转发12)”<br>- “AF11(确保转发11)”<br>- “BE(尽力转发)”<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001126306022__tab3) |
| SCDSCP | 流类数据的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置流类用户的发送数据报文对应的DSCP值。<br>前提条件：该参数在<br>“数据DSCP使用策略”<br>为<br>“MODIFY(修改DSCP值)”<br>时配置。<br>数据来源：整网规划<br>取值范围：<br>- “NC(网络控制)”<br>- “EF(快速转发)”<br>- “AF43(确保转发43)”<br>- “AF42(确保转发42)”<br>- “AF41(确保转发41)”<br>- “AF33(确保转发33)”<br>- “AF32(确保转发32)”<br>- “AF31(确保转发31)”<br>- “AF23(确保转发23)”<br>- “AF22(确保转发22)”<br>- “AF21(确保转发21)”<br>- “AF13(确保转发13)”<br>- “AF12(确保转发12)”<br>- “AF11(确保转发11)”<br>- “BE(尽力转发)”<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001126306022__tab3) |
| ICTHP1DSCP | 交互类优先级1的数据的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置交互类优先级1的用户的发送数据报文对应的DSCP值。<br>前提条件：该参数在<br>“数据DSCP使用策略”<br>为<br>“MODIFY(修改DSCP值)”<br>时配置。<br>数据来源：整网规划<br>取值范围：<br>- “NC(网络控制)”<br>- “EF(快速转发)”<br>- “AF43(确保转发43)”<br>- “AF42(确保转发42)”<br>- “AF41(确保转发41)”<br>- “AF33(确保转发33)”<br>- “AF32(确保转发32)”<br>- “AF31(确保转发31)”<br>- “AF23(确保转发23)”<br>- “AF22(确保转发22)”<br>- “AF21(确保转发21)”<br>- “AF13(确保转发13)”<br>- “AF12(确保转发12)”<br>- “AF11(确保转发11)”<br>- “BE(尽力转发)”<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001126306022__tab3) |
| ICTHP2DSCP | 交互类优先级2的数据的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置交互类优先级2的用户的发送数据报文对应的DSCP值。<br>前提条件：该参数在<br>“数据DSCP使用策略”<br>为<br>“MODIFY(修改DSCP值)”<br>时配置。<br>数据来源：整网规划<br>取值范围：<br>- “NC(网络控制)”<br>- “EF(快速转发)”<br>- “AF43(确保转发43)”<br>- “AF42(确保转发42)”<br>- “AF41(确保转发41)”<br>- “AF33(确保转发33)”<br>- “AF32(确保转发32)”<br>- “AF31(确保转发31)”<br>- “AF23(确保转发23)”<br>- “AF22(确保转发22)”<br>- “AF21(确保转发21)”<br>- “AF13(确保转发13)”<br>- “AF12(确保转发12)”<br>- “AF11(确保转发11)”<br>- “BE(尽力转发)”<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001126306022__tab3) |
| ICTHP3DSCP | 交互类优先级3的数据的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置交互类优先级3的用户的发送数据报文对应的DSCP值。<br>前提条件：该参数在<br>“数据DSCP使用策略”<br>为<br>“MODIFY(修改DSCP值)”<br>时配置。<br>数据来源：整网规划<br>取值范围：<br>- “NC(网络控制)”<br>- “EF(快速转发)”<br>- “AF43(确保转发43)”<br>- “AF42(确保转发42)”<br>- “AF41(确保转发41)”<br>- “AF33(确保转发33)”<br>- “AF32(确保转发32)”<br>- “AF31(确保转发31)”<br>- “AF23(确保转发23)”<br>- “AF22(确保转发22)”<br>- “AF21(确保转发21)”<br>- “AF13(确保转发13)”<br>- “AF12(确保转发12)”<br>- “AF11(确保转发11)”<br>- “BE(尽力转发)”<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001126306022__tab3) |
| BCDSCP | 背景类数据的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置背景类用户的发送数据报文对应的DSCP值。<br>前提条件：该参数在<br>“数据DSCP使用策略”<br>为<br>“MODIFY(修改DSCP值)”<br>时配置。<br>数据来源：整网规划<br>取值范围：<br>- “NC(网络控制)”<br>- “EF(快速转发)”<br>- “AF43(确保转发43)”<br>- “AF42(确保转发42)”<br>- “AF41(确保转发41)”<br>- “AF33(确保转发33)”<br>- “AF32(确保转发32)”<br>- “AF31(确保转发31)”<br>- “AF23(确保转发23)”<br>- “AF22(确保转发22)”<br>- “AF21(确保转发21)”<br>- “AF13(确保转发13)”<br>- “AF12(确保转发12)”<br>- “AF11(确保转发11)”<br>- “BE(尽力转发)”<br>系统初始设置值：请参考<br>[表3](#ZH-CN_MMLREF_0000001126306022__tab3) |

#### [使用实例](#ZH-CN_MMLREF_0000001126306022)

设置 “消息类别” 为 “SIGNALING(信令消息)” ， “接口类型” 为 “S1_MME(S1_MME接口)” ， “DSCP值” 为 “46” ：

SET IFDSCP: MSGCLS=SIGNALLING, INTFTP_SHOW=S1_MME, DSCPV=46;

#### [参考信息](#ZH-CN_MMLREF_0000001126306022)

*表1 常用的DSCP用法列表*

| 对应的服务 | IPv4优先级/EXP/802.1P | DSCP(二进制) | DSCP[十进制][十六进制] | TOS[十进制][十六进制] | 应用 | 丢包率 |
| --- | --- | --- | --- | --- | --- | --- |
| BE | 0 | 000 000 | 0 | 0 | Internet | - |
| AF1 | Green 1 | 001 010 | 10[0x0a] | 40[0x28] | Leased Line | L |
| AF1 | Green 1 | 001 100 | 12[0x0c] | 48[0x30] | Leased Line | M |
| AF1 | Green 1 | 001 110 | 14[0x0e] | 56[0x38] | Leased Line | H |
| AF2 | Green 2 | 010 010 | 18[0x12] | 72[0x48] | IPTV VOD | L |
| AF2 | Green 2 | 010 100 | 20[0x14] | 80[0x50] | IPTV VOD | M |
| AF2 | Green 2 | 010 110 | 22[0x16] | 88[0x58] | IPTV VOD | H |
| AF3 | Green 3 | 011 010 | 26[0x1a] | 104[0x68] | IPTV Broadcast | L |
| AF3 | Green 3 | 011 100 | 28[0x1c] | 112[0x70] | IPTV Broadcast | M |
| AF3 | Green 3 | 011 110 | 30[0x1e] | 120[0x78] | IPTV Broadcast | H |
| AF4 | Green 4 | 100 010 | 34[0x22] | 136[0x88] | NGN/3G Signaling | L |
| AF4 | Green 4 | 100 100 | 36[0x24] | 144[0x90] | NGN/3G Signaling | M |
| AF4 | Green 4 | 100 110 | 38[0x26] | 152[0x98] | NGN/3G Signaling | H |
| EF | 5 | 101 110 | 46[0x2E] | 184[0xB8] | NGN/3G voice | - |
| CS6(INC) | 6 | 110 000 | 48[0x30] | 192[0xC0] | Protocol | - |
| CS7(NC) | 7 | 111 000 | 56[0x38] | 224[0xE0] | Protocol | - |

NC、EF、AF4、AF3、AF2、AF1、BE等都是RFC2474协议中定义的差异化服务类等级。NC是最高优先级服务，依次递减，BE为最低优先级服务类。CS6和CS7默认用于协议报文，因为如果这些报文无法接收的话会引起协议中断，所以应该优先保障；EF用于承载语音的流量，因为语音要求低延迟、低抖动、低丢包率，是仅次于协议报文的最重要的报文；AF4可以用来承载语音的信令流量；AF3可以用来承载IPTV的直播流量，直播的实时性很强，需要连续性和大吞吐量的保证；AF2可以用来承载VOD的流量；AF1可以用来承载专线业务；BE可以用来承载INTERNET业务。

> **说明**
> 通常使用AF服务类等级加丢包率表示AF类的DSCP值。例如，AF43表示服务类等级为AF4，丢包率为H；AF42表示服务类等级为AF4，丢包率为M；AF41表示服务类等级为AF4，丢包率为L。

*表2 信令消息DSCP系统初始设置值*

| 消息类别 | 接口类型 | 消息类型 | DSCP值 |
| --- | --- | --- | --- |
| 信令消息 | 未指定接口 | 其他消息 | 56 |
| 信令消息 | S1_MME接口 | 其他消息 | 46 |
| 信令消息 | 使用M3UA协议的接口 | 其他消息 | 56 |
| 信令消息 | 使用GTP协议的接口的信令消息 | 其他消息 | 56 |
| 信令消息 | 使用GTP协议的接口的信令消息 | GTP数据报文触发的GTPU信令消息 | 10 |
| 信令消息 | 使用Diameter协议的接口 | 其他消息 | 56 |
| 信令消息 | Gb接口的信令消息 | 其他消息 | 56 |
| 信令消息 | Ga接口 | 其他消息 | 56 |
| 信令消息 | Iu接口的信令消息 | 其他消息 | 56 |
| 信令消息 | DNS接口 | 其他消息 | 56 |
| 信令消息 | SLs接口 | 其他消息 | 56 |
| 信令消息 | SGs接口 | 其他消息 | 56 |
| 信令消息 | SBc接口 | 其他消息 | 56 |
| 信令消息 | S102接口 | 其他消息 | 56 |
| 信令消息 | Tm接口 | 其他消息 | 56 |

*表3 数据消息DSCP系统初始设置值*

| 消息类别 | SNDCP转GTP数据的DSCP值 | 数据DSCP使用策略 | 会话类数据的DSCP值 | 流类数据的DSCP值 | 交互类优先级1的数据的DSCP值 | 交互类优先级2的数据的DSCP值 | 交互类优先级3的数据的DSCP值 | 背景类数据的DSCP值 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 数据消息 | 46 | 透传DSCP值 | 快速转发 | 确保转发41 | 确保转发31 | 确保转发21 | 确保转发11 | 尽力转发 |
