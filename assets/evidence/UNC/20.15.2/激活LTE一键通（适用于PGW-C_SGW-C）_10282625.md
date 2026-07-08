# 激活 LTE一键通 （适用于PGW-C/SGW-C）

- [操作场景](#ZH-CN_OPI_0310282625__1.3.1)
- [必备事项](#ZH-CN_OPI_0310282625__1.3.2)
- [操作步骤](#ZH-CN_OPI_0310282625__1.3.3)
- [任务示例](#ZH-CN_OPI_0310282625__1.3.4)

## [操作场景](#ZH-CN_OPI_0310282625)

本操作指导介绍在运行网络中激活 LTE一键通 特性的操作过程。

> **说明**
> 适用于SGW-C、PGW-C。

**图1** 操作过程

<br>

![](激活LTE一键通（适用于PGW-C_SGW-C）_10282625.assets/zh-cn_image_0311554973_2.png "点击放大")

## [必备事项](#ZH-CN_OPI_0310282625)

前提条件

- 请仔细阅读[WSFD-102601 LTE一键通基础功能（适用于PGW-C/SGW-C）](../WSFD-102601 LTE一键通基础功能（适用于PGW-C_SGW-C）/特性概述_10980736.md)和[WSFD-102602 LTE一键通特性概述（适用于PGW-C/SGW-C）](特性概述_10282604.md)。

- 已完成加载License。

数据

*表1 基于全局的一键通配置*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD STDQOSID**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/扩展QCI功能/标准QoS ID配置/增加标准QoS ID配置（ADD STDQOSID）_06399909.md) | QOSIDTYPE（QoS ID类型） | QCI | 本端规划 | 用于增加标准QoS ID配置。<br>根据3GPP协议规定，最初的标准QCI/5QI只有1~9，后续协议演进增加了其他的数值作为标准QoS ID，当需要支持其他的数值作为标准QoS ID时可以通过本命令增加。<br>说明：标准QoS ID需要整网规划，通过本命令配置新增的标准QCI/5QI以后，这些标准QCI/5QI就可能通过各个接口发送给对端的不同设备，因此需要同时确认对端设备已支持相应的数值，否则可能会造成业务对接失败。 |
| [**ADD STDQOSID**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/扩展QCI功能/标准QoS ID配置/增加标准QoS ID配置（ADD STDQOSID）_06399909.md) | QOSIDSV（QoS ID起始值） | 65 | 全网规划 | 用于增加标准QoS ID配置。<br>根据3GPP协议规定，最初的标准QCI/5QI只有1~9，后续协议演进增加了其他的数值作为标准QoS ID，当需要支持其他的数值作为标准QoS ID时可以通过本命令增加。<br>说明：标准QoS ID需要整网规划，通过本命令配置新增的标准QCI/5QI以后，这些标准QCI/5QI就可能通过各个接口发送给对端的不同设备，因此需要同时确认对端设备已支持相应的数值，否则可能会造成业务对接失败。 |
| [**ADD STDQOSID**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/扩展QCI功能/标准QoS ID配置/增加标准QoS ID配置（ADD STDQOSID）_06399909.md) | QOSIDEV（QoS ID结束值） | 67 | 全网规划 | 用于增加标准QoS ID配置。<br>根据3GPP协议规定，最初的标准QCI/5QI只有1~9，后续协议演进增加了其他的数值作为标准QoS ID，当需要支持其他的数值作为标准QoS ID时可以通过本命令增加。<br>说明：标准QoS ID需要整网规划，通过本命令配置新增的标准QCI/5QI以后，这些标准QCI/5QI就可能通过各个接口发送给对端的不同设备，因此需要同时确认对端设备已支持相应的数值，否则可能会造成业务对接失败。 |
| [**ADD STDQOSID**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/扩展QCI功能/标准QoS ID配置/增加标准QoS ID配置（ADD STDQOSID）_06399909.md) | RESOURCETYPE（标准QoS ID的资源类型） | GBR | 全网规划 | 用于增加标准QoS ID配置。<br>根据3GPP协议规定，最初的标准QCI/5QI只有1~9，后续协议演进增加了其他的数值作为标准QoS ID，当需要支持其他的数值作为标准QoS ID时可以通过本命令增加。<br>说明：标准QoS ID需要整网规划，通过本命令配置新增的标准QCI/5QI以后，这些标准QCI/5QI就可能通过各个接口发送给对端的不同设备，因此需要同时确认对端设备已支持相应的数值，否则可能会造成业务对接失败。 |
| [**LST STDQOSID**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/扩展QCI功能/标准QoS ID配置/查询标准QoS ID配置（LST STDQOSID）_06399918.md) | QOSIDTYPE（QoS ID类型） | QCI | 本端规划 | 用于查询标准QoS ID配置。 |
| [**SET PTTFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/一键通/全局一键通配置/设置一键通配置（SET PTTFUNC）_06399931.md) | LTEPTTSWITCH（<br>LTE一键通<br>功能开关） | ENABLE | 本端规划 | 基于全局的PTT业务配置开关。 |
| [**SET EPSQCI2PRER8**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/EPS QCI映射到PreR8/设置EPS QCI到Pre-R8 QoS映射规则（SET EPSQCI2PRER8）_09651491.md) | QCI（QCI值） | 65<br>66<br>69<br>70 | 全网规划 | PTT QCI到Pre-R8 QoS参数traffic class的映射关系。<br>说明：用户通过GnGp SGSN接入<br>UNC<br>，由于GnGp SGSN和<br>UNC<br>之间交互的是GTPv0和GTPv1信令，故<br>UNC<br>需将R8 QoS中的QCI信息映射至Pre Rel-8 QoS参数，保证系统正常运行。 |
| [**SET EPSQCI2PRER8**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/EPS QCI映射到PreR8/设置EPS QCI到Pre-R8 QoS映射规则（SET EPSQCI2PRER8）_09651491.md) | TRAFFICCLASS（业务类型） | CONVERSATIONAL | 全网规划 | PTT QCI到Pre-R8 QoS参数traffic class的映射关系。<br>说明：用户通过GnGp SGSN接入<br>UNC<br>，由于GnGp SGSN和<br>UNC<br>之间交互的是GTPv0和GTPv1信令，故<br>UNC<br>需将R8 QoS中的QCI信息映射至Pre Rel-8 QoS参数，保证系统正常运行。 |
| [**SET EPSQCI2PRER8**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/EPS QCI映射到PreR8/设置EPS QCI到Pre-R8 QoS映射规则（SET EPSQCI2PRER8）_09651491.md) | THP（通信处理优先级） | HIGH | 全网规划 | PTT QCI到Pre-R8 QoS参数traffic class的映射关系。<br>说明：用户通过GnGp SGSN接入<br>UNC<br>，由于GnGp SGSN和<br>UNC<br>之间交互的是GTPv0和GTPv1信令，故<br>UNC<br>需将R8 QoS中的QCI信息映射至Pre Rel-8 QoS参数，保证系统正常运行。 |
| [**SET EPSQCI2PRER8**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/EPS QCI映射到PreR8/设置EPS QCI到Pre-R8 QoS映射规则（SET EPSQCI2PRER8）_09651491.md) | SIGNALIND（信令传输优化） | OPTIMIZE | 全网规划 | PTT QCI到Pre-R8 QoS参数traffic class的映射关系。<br>说明：用户通过GnGp SGSN接入<br>UNC<br>，由于GnGp SGSN和<br>UNC<br>之间交互的是GTPv0和GTPv1信令，故<br>UNC<br>需将R8 QoS中的QCI信息映射至Pre Rel-8 QoS参数，保证系统正常运行。 |
| [**SET EPSQCI2PRER8**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/EPS QCI映射到PreR8/设置EPS QCI到Pre-R8 QoS映射规则（SET EPSQCI2PRER8）_09651491.md) | SRCSTATDESC（源统计描述） | SPEECH | 全网规划 | PTT QCI到Pre-R8 QoS参数traffic class的映射关系。<br>说明：用户通过GnGp SGSN接入<br>UNC<br>，由于GnGp SGSN和<br>UNC<br>之间交互的是GTPv0和GTPv1信令，故<br>UNC<br>需将R8 QoS中的QCI信息映射至Pre Rel-8 QoS参数，保证系统正常运行。 |
| [**SET QCI2ARP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QCI到ARP映射/设置标准QCI到ARP的映射规则（SET QCI2ARP）_09652269.md) | QCI（标准QCI） | 65<br>66<br>69<br>70 | 本端规划 | PTT QCI和ARP之间的映射关系，从而通过标准QCI来映射出相应的承载ARP取值。 |
| [**SET QCI2ARP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QCI到ARP映射/设置标准QCI到ARP的映射规则（SET QCI2ARP）_09652269.md) | ARPPL（ARP的优先级别） | 7 | 本端规划 | PTT QCI和ARP之间的映射关系，从而通过标准QCI来映射出相应的承载ARP取值。 |
| [**SET QCI2ARP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QCI到ARP映射/设置标准QCI到ARP的映射规则（SET QCI2ARP）_09652269.md) | ARPPVI（QCI的被抢占能力） | 0 | 本端规划 | PTT QCI和ARP之间的映射关系，从而通过标准QCI来映射出相应的承载ARP取值。 |
| [**ADD EPSREMARK**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md) | QOSPROFILENAME（QoS Profile名称） | qos1 | 全网规划 | 增加EPS QoS到TOS/DSCP的映射规则。 |
| [**ADD EPSREMARK**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md) | QCI（QCI） | 65<br>66<br>69<br>70 | 全网规划 | 增加EPS QoS到TOS/DSCP的映射规则。 |
| [**ADD EPSREMARK**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md) | ARPPL（ARP的优先级别） | 2 | 全网规划 | 增加EPS QoS到TOS/DSCP的映射规则。 |
| [**ADD EPSREMARK**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md) | REMARKTYPE（标记类型） | DSCP | 全网规划 | 增加EPS QoS到TOS/DSCP的映射规则。 |
| [**ADD EPSREMARK**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md) | DSCP（DSCP） | EF | 全网规划 | 增加EPS QoS到TOS/DSCP的映射规则。 |
| [**SET DEFEPSQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | QOSCLASSID（QCI值） | 69 | 本端规划 | 配置EPS本地QoS策略下缺省QoS参数，PGW-C根据协议检查用户携带的QoS参数的合法性，如果参数非法，则根据该命令配置的缺省QoS参数进行纠错和替换。 |
| [**SET DEFEPSQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | ARPVALUE（ARP值） | 1 | 本端规划 | 配置EPS本地QoS策略下缺省QoS参数，PGW-C根据协议检查用户携带的QoS参数的合法性，如果参数非法，则根据该命令配置的缺省QoS参数进行纠错和替换。 |
| [**SET DEFEPSQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | GBRDL（下行保证带宽） | 200bit/s | 本端规划 | 配置EPS本地QoS策略下缺省QoS参数，PGW-C根据协议检查用户携带的QoS参数的合法性，如果参数非法，则根据该命令配置的缺省QoS参数进行纠错和替换。 |
| [**SET DEFEPSQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | GBRUL（上行保证带宽） | 230bit/s | 本端规划 | 配置EPS本地QoS策略下缺省QoS参数，PGW-C根据协议检查用户携带的QoS参数的合法性，如果参数非法，则根据该命令配置的缺省QoS参数进行纠错和替换。 |
| [**SET DEFEPSQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | MBRDL（下行最大带宽） | 300bit/s | 本端规划 | 配置EPS本地QoS策略下缺省QoS参数，PGW-C根据协议检查用户携带的QoS参数的合法性，如果参数非法，则根据该命令配置的缺省QoS参数进行纠错和替换。 |
| [**SET DEFEPSQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | MBRUL（上行最大带宽） | 300bit/s | 本端规划 | 配置EPS本地QoS策略下缺省QoS参数，PGW-C根据协议检查用户携带的QoS参数的合法性，如果参数非法，则根据该命令配置的缺省QoS参数进行纠错和替换。 |
| [**SET DEFEPSQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | APNAMBRDL（下行APN AMBR） | 1000bit/s | 本端规划 | 配置EPS本地QoS策略下缺省QoS参数，PGW-C根据协议检查用户携带的QoS参数的合法性，如果参数非法，则根据该命令配置的缺省QoS参数进行纠错和替换。 |
| [**SET DEFEPSQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md) | APNAMBRUL（上行APN AMBR） | 1000bit/s | 本端规划 | 配置EPS本地QoS策略下缺省QoS参数，PGW-C根据协议检查用户携带的QoS参数的合法性，如果参数非法，则根据该命令配置的缺省QoS参数进行纠错和替换。 |
| [**ADD EPSSUBQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md) | SUBQOSINDEX（用户QOS索引） | 1 | 本端规划 | 配置用户的签约QoS属性支持PTT QCI。 |
| [**ADD EPSSUBQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md) | QCI（QCI） | 65<br>66<br>69<br>70 | 本端规划 | 配置用户的签约QoS属性支持PTT QCI。 |
| [**ADD EPSSUBQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md) | ARPPL（ARP的优先级别） | 7 | 本端规划 | 配置用户的签约QoS属性支持PTT QCI。 |
| [**ADD EPSSUBQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md) | AMBRDL（下行APN AMBRR） | 22 | 本端规划 | 配置用户的签约QoS属性支持PTT QCI。 |
| [**ADD EPSSUBQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md) | AMBRUL（上行APN AMBRR） | 33 | 本端规划 | 配置用户的签约QoS属性支持PTT QCI。 |
| [**ADD QOSPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md) | QOSPROFILENAME（QoS Profile名） | qos1 | 本端规划 | QosProfile的配置信息。 |
| [**ADD QOSPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md) | 绑定EPS用户QoS（BINDEPSSUBQOS） | ENABLE（使能） | 本端规划 | QosProfile的配置信息。 |
| [**ADD QOSPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md) | EPS用户QoS索引（EPSSUBQOS） | 200 | 本端规划 | QosProfile的配置信息。 |
| [**SET QOSGLOBAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置全局QoS配置（SET QOSGLOBAL）_09652976.md) | QOSPROFILENAME（QoS Profile名） | qos2 | 本端规划 | 配置全局的QoS信息。 |
| [**SET QOSGLOBAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置全局QoS配置（SET QOSGLOBAL）_09652976.md) | 绑定EPS用户QoS（BINDEPSSUBQOS） | ENABLE（使能） | 本端规划 | 配置全局的QoS信息。 |
| [**SET QOSGLOBAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置全局QoS配置（SET QOSGLOBAL）_09652976.md) | EPS用户QoS索引（EPSSUBQOS） | 200 | 本端规划 | 配置全局的QoS信息。 |
| [**ADD QOSPROP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QOSPROPNAME（QoS属性名称） | qos3 | 本端规划 | 配置PCC预定义规则的QoS参数。 |
| [**ADD QOSPROP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QCIVALUE（QoS等级标识） | 65<br>66<br>69<br>70 | 本端规划 | 配置PCC预定义规则的QoS参数。 |
| [**ADD QOSPROP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | QOSTYPE（QoS属性类型） | QOS_BEARER_PARA | 本端规划 | 配置PCC预定义规则的QoS参数。 |
| [**ADD QOSPROP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md) | EMPCAP（QoS抢占能力） | ENABLE | 本端规划 | 配置PCC预定义规则的QoS参数。 |

*表2 基于APN的一键通配置*

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD STDQOSID**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/扩展QCI功能/标准QoS ID配置/增加标准QoS ID配置（ADD STDQOSID）_06399909.md) | QOSIDTYPE（QoS ID类型） | QCI | 本端规划 | 用于增加标准QoS ID配置。<br>根据3GPP协议规定，最初的标准QCI/5QI只有1~9，后续协议演进增加了其他的数值作为标准QoS ID，当需要支持其他的数值作为标准QoS ID时可以通过本命令增加。<br>说明：标准QoS ID需要整网规划，通过本命令配置新增的标准QCI/5QI以后，这些标准QCI/5QI就可能通过各个接口发送给对端的不同设备，因此需要同时确认对端设备已支持相应的数值，否则可能会造成业务对接失败。 |
| [**ADD STDQOSID**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/扩展QCI功能/标准QoS ID配置/增加标准QoS ID配置（ADD STDQOSID）_06399909.md) | QOSIDSV（QoS ID起始值） | 65 | 全网规划 | 用于增加标准QoS ID配置。<br>根据3GPP协议规定，最初的标准QCI/5QI只有1~9，后续协议演进增加了其他的数值作为标准QoS ID，当需要支持其他的数值作为标准QoS ID时可以通过本命令增加。<br>说明：标准QoS ID需要整网规划，通过本命令配置新增的标准QCI/5QI以后，这些标准QCI/5QI就可能通过各个接口发送给对端的不同设备，因此需要同时确认对端设备已支持相应的数值，否则可能会造成业务对接失败。 |
| [**ADD STDQOSID**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/扩展QCI功能/标准QoS ID配置/增加标准QoS ID配置（ADD STDQOSID）_06399909.md) | QOSIDEV（QoS ID结束值） | 67 | 全网规划 | 用于增加标准QoS ID配置。<br>根据3GPP协议规定，最初的标准QCI/5QI只有1~9，后续协议演进增加了其他的数值作为标准QoS ID，当需要支持其他的数值作为标准QoS ID时可以通过本命令增加。<br>说明：标准QoS ID需要整网规划，通过本命令配置新增的标准QCI/5QI以后，这些标准QCI/5QI就可能通过各个接口发送给对端的不同设备，因此需要同时确认对端设备已支持相应的数值，否则可能会造成业务对接失败。 |
| [**ADD STDQOSID**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/扩展QCI功能/标准QoS ID配置/增加标准QoS ID配置（ADD STDQOSID）_06399909.md) | RESOURCETYPE（标准QoS ID的资源类型） | GBR | 全网规划 | 用于增加标准QoS ID配置。<br>根据3GPP协议规定，最初的标准QCI/5QI只有1~9，后续协议演进增加了其他的数值作为标准QoS ID，当需要支持其他的数值作为标准QoS ID时可以通过本命令增加。<br>说明：标准QoS ID需要整网规划，通过本命令配置新增的标准QCI/5QI以后，这些标准QCI/5QI就可能通过各个接口发送给对端的不同设备，因此需要同时确认对端设备已支持相应的数值，否则可能会造成业务对接失败。 |
| [**LST STDQOSID**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/扩展QCI功能/标准QoS ID配置/查询标准QoS ID配置（LST STDQOSID）_06399918.md) | QOSIDTYPE（QoS ID类型） | QCI | 本端规划 | 用于查询标准QoS ID配置。 |
| [**ADD APNPTTFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/一键通/APN的一键通配置/增加基于APN的一键通功能配置（ADD APNPTTFUNC）_06399904.md) | APN(APN名称) | apn1 | 本端规划 | 基于APN的PTT业务配置开关。<br>APN名称必须已经通过命令<br>[**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>配置。 |
| [**ADD APNPTTFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/一键通/APN的一键通配置/增加基于APN的一键通功能配置（ADD APNPTTFUNC）_06399904.md) | LTEPTTSWITCH（<br>LTE一键通<br>功能开关） | ENABLE | 本端规划 | 基于APN的PTT业务配置开关。<br>APN名称必须已经通过命令<br>[**ADD APN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>配置。 |
| [**ADD EPSSUBQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md) | SUBQOSINDEX（用户QOS索引） | 1 | 本端规划 | 配置用户的签约QoS属性支持PTT QCI。 |
| [**ADD EPSSUBQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md) | QCI（QCI） | 65<br>66<br>69<br>70 | 本端规划 | 配置用户的签约QoS属性支持PTT QCI。 |
| [**ADD EPSSUBQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md) | ARPPL（ARP的优先级别） | 7 | 本端规划 | 配置用户的签约QoS属性支持PTT QCI。 |
| [**ADD EPSSUBQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md) | AMBRDL（下行APN AMBRR） | 22 | 本端规划 | 配置用户的签约QoS属性支持PTT QCI。 |
| [**ADD EPSSUBQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md) | AMBRUL（上行APN AMBRR） | 33 | 本端规划 | 配置用户的签约QoS属性支持PTT QCI。 |
| [**ADD QOSPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md) | QOSPROFILENAME（QoS Profile名） | qos1 | 本端规划 | QosProfile的配置信息。 |
| [**ADD QOSPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md) | 绑定EPS用户QoS（BINDEPSSUBQOS） | ENABLE（使能） | 本端规划 | QosProfile的配置信息。 |
| [**ADD QOSPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md) | EPS用户QoS索引（EPSSUBQOS） | 200 | 本端规划 | QosProfile的配置信息。 |
| [**SET APNQOSATTR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md) | APN（APN名称） | apn1 | 本端规划 | 为APN实例绑定QosProfile。 |
| [**SET APNQOSATTR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md) | HASQOSPROFILE（是否配置QosProfile） | ENABLE | 本端规划 | 为APN实例绑定QosProfile。 |
| [**SET APNQOSATTR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md) | QOSPROFILENAME（QoS Profile名） | qos1 | 本端规划 | 为APN实例绑定QosProfile。 |

## [操作步骤](#ZH-CN_OPI_0310282625)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开 LTE一键通 功能特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 基于全局的一键通业务配置：
    a. 查询PTT业务QCI是否已经配置为标准QCI。
      [**LST STDQOSID**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/扩展QCI功能/标准QoS ID配置/查询标准QoS ID配置（LST STDQOSID）_06399918.md)
    b. 开启基于全局的PTT业务配置开关。
      [**SET PTTFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/一键通/全局一键通配置/设置一键通配置（SET PTTFUNC）_06399931.md)
    c. （可选）增加PTT业务QoS参数到Pre-R8 QoS参数映射规则。
      [**SET EPSQCI2PRER8**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/PreR8 QoS配置/EPS QCI映射到PreR8/设置EPS QCI到Pre-R8 QoS映射规则（SET EPSQCI2PRER8）_09651491.md)
    d. （可选）配置PTT QCI和ARP的映射规则。
      [**SET QCI2ARP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QCI到ARP映射/设置标准QCI到ARP的映射规则（SET QCI2ARP）_09652269.md)
    e. （可选）配置PTT QCI到TOS/DSCP的映射规则。
      [**ADD EPSREMARK**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/EPS Qos映射ToS_DSCP/增加EPS QoS到TOS_DSCP的映射规则（ADD EPSREMARK）_09652275.md)
    f. （可选）配置EPS本地QoS策略下缺省QoS参数，用于纠错。
      [**SET DEFEPSQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/全局EPS QoS纠错/设置EPS缺省QoS参数（SET DEFEPSQOS）_09653732.md)
    g. （可选）配置用户的签约QoS属性支持PTT QCI。
      [**ADD EPSSUBQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md)
    h. （可选）配置QosProfile信息。
      [**ADD QOSPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md)
    i. （可选）配置PCC预定义规则的QoS参数。
      [**ADD QOSPROP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/业务质量属性/增加QoS属性（ADD QOSPROP）_09897163.md)
4. 基于APN的一键通业务配置：
    a. 查询PTT业务QCI是否已经配置为标准QCI。
      [**LST STDQOSID**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/扩展QCI功能/标准QoS ID配置/查询标准QoS ID配置（LST STDQOSID）_06399918.md)
    b. 开启基于APN的PTT业务配置开关。
      [**ADD APNPTTFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/一键通/APN的一键通配置/增加基于APN的一键通功能配置（ADD APNPTTFUNC）_06399904.md)
    c. （可选）配置用户的签约QoS属性支持PTT QCI。
      [**ADD EPSSUBQOS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/EPS QoS配置/本地EPS QoS/增加EPS签约QoS配置（ADD EPSSUBQOS）_09653648.md)
    d. （可选）配置QosProfile信息。
      [**ADD QOSPROFILE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md)
    e. （可选）为APN实例绑定QosProfile。
      [**SET APNQOSATTR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)

## [任务示例](#ZH-CN_OPI_0310282625)

任务描述

配置APN为“apn1”，基于此APN激活 LTE一键通 功能特性。

脚本

// 进入 “MML命令行-UNC” 窗口。

//打开 LTE一键通 功能特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2QPPT02", SWITCH=ENABLE;
```

//查询PTT业务QCI是否已经配置为标准QCI。

```
LST STDQOSID: QOSIDTYPE=QCI;
```

//配置APN为“apn1”。

```
ADD APN: APN="apn1";
```

//开启基于APN的PTT业务配置开关。

```
ADD APNPTTFUNC: APN="apn1", LTEPTTSWITCH=ENABLE;
```
