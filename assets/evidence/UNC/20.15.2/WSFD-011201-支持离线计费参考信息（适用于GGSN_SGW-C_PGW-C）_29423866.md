# WSFD-011201 支持离线计费参考信息（适用于GGSN/SGW-C/PGW-C）

- [命令](#ZH-CN_TOPIC_0229423866__1.3.1.1)
- [告警](#ZH-CN_TOPIC_0229423866__1.3.2.1)
- [软参](#ZH-CN_TOPIC_0229423866__1.3.3.1)
- [测量指标](#ZH-CN_TOPIC_0229423866__1.3.5.1)

#### [命令](#ZH-CN_TOPIC_0229423866)

本特性相关的MML命令如下：

- **[ADD CHARGECHAR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
- [**SET USRPROFCHARGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md)
- [**SET APNCHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md)
- [**SET GLBCHARGECHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
- [**SET CHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)
- [**ADD CHARGEMETHOD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)
- [**SET SGWCHARGECFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW计费基础参数/SGW计费配置（SET SGWCHARGECFG）_09896989.md)
- [**SET SGWAPNCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW APN计费方式/设置SGW APN计费方式（SET SGWAPNCHGMETH）_09896992.md)
- [**SET SGWCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/计费属性控制/设置SGW Charge Method（SET SGWCHGMETH）_09896985.md)
- [**ADD OFCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/增加离线计费模板（ADD OFCTEMPLATE）_09896908.md)
- [**SET OFCTHRESHOLD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)
- [**SET CDRTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费话单产生开关（SET CDRTRIGGER）_09896911.md)
- [**SET CONTAINERTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费容器产生开关（SET CONTAINERTRIGGER）_09896912.md)
- [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
- [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
- [**ADD SUBSCRIBERIDSEGGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN IMEISV号段组/增加IMSI_MSISDN_IMEISV号段组（ADD SUBSCRIBERIDSEGGRP）_65997002.md)
- [**ADD CGGRPBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG组绑定/增加CG组绑定关系（ADD CGGRPBINDING）_09896884.md)
- [**ADD SGWSEGGCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW IMSI_MSISDN号段组计费方式/增加SGW IMSI_MSISDN Group Charge Method（ADD SGWSEGGCHGMETH）_09896995.md)
- [**ADD GLBOFCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/全局离线计费模板/增加全局离线计费模板（ADD GLBOFCTEMPLATE）_09896916.md)
- [**ADD FESTIVAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/节假日/增加计费节假日表（ADD FESTIVAL）_09896827.md)
- [**ADD WEEKDAY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/工作日/配置计费星期表（ADD WEEKDAY）_09896831.md)
- [**ADD TARIFFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/费率切换组/配置费率切换组（ADD TARIFFGROUP）_09896836.md)
- [**SET GLBTARIFFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)
- [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
- [**SET GLBCDRFLDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/全局话单字段模板/设置全局话单模板（SET GLBCDRFLDTEMP）_09896895.md)
- [**FOC GENERATECDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费维护/强制生成话单/强制生成话单（FOC GENERATECDR）_09897016.md)
- [**SET OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
- [**SET CDRSTRGSTATUS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费缓存/缓存目录/设置话单缓存目录状态（SET CDRSTRGSTATUS）_09897006.md)
- [**SET CDRSTORAGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费缓存/缓存控制/设置话单存储控制参数（SET CDRSTORAGECTRL）_09897001.md)
- [**SET ZEROCHGSKIPSW**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置零流量计费事件忽略开关（SET ZEROCHGSKIPSW）_09896806.md)
- [**ADD CG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG管理/配置CG（ADD CG）_09896845.md)
- [**ADD CGGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG组/添加CG组（ADD CGGROUP）_09896879.md)
- [**ADD CGBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG绑定/增加CG绑定关系（ADD CGBINDING）_09896874.md)
- [**SET SGWCHARGECFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW计费基础参数/SGW计费配置（SET SGWCHARGECFG）_09896989.md)
- [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
- [**ADD CPCGGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/抄送CG组/增加抄送CG组（ADD CPCGGRP）_09896864.md)
- [**ADD CPCGBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/抄送CG绑定/增加抄送CG绑定（ADD CPCGBINDING）_09896869.md)
- **[DSP SMPDPNUM](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文数/查询会话管理的PDP上下文数（DSP SMPDPNUM）_09653799.md)**

#### [告警](#ZH-CN_TOPIC_0229423866)

本特性相关的告警如下：

- [ALM-81021 CG无响应](../../../../../../网络运维/故障处理/UNC告警处理/业务告警/SMF&GW-C&GGSN/ALM-81021 CG无响应_14905555.md)
- [ALM-81059 超期话单缓存](../../../../../../网络运维/故障处理/UNC告警处理/业务告警/SMF&GW-C&GGSN/ALM-81059 超期话单缓存_28571624.md)
- [ALM-81005 话单池空间不足](../../../../../../网络运维/故障处理/UNC告警处理/业务告警/SMF&GW-C&GGSN/ALM-81005 话单池空间不足_28573364.md)
- [ALM-81033 配置与业务冲突](../../../../../../网络运维/故障处理/UNC告警处理/业务告警/SMF&GW-C&GGSN/ALM-81033 配置与业务冲突_15325585.md)

#### [软参](#ZH-CN_TOPIC_0229423866)

本特性相关的软参如下：

- [BYTE77 控制运营商定制需求](../../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/在线计费管理/BYTE77 控制运营商定制需求_98644169.md)
- [BIT836 控制是否携带华为CG的5G定制字段。](../../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/离线计费管理/BIT836 控制是否携带华为CG的5G定制字段。_11353184.md)
- [BYTE72 控制CG锁定时长和话单优先发送到CG发送的重定向消息中指定CG的时长](../../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/离线计费管理/BYTE72 控制CG锁定时长和话单优先发送到CG发送的重定向消息中指定CG的时长_98644153.md)
- [BIT160 控制话单中业务容器的Duration为0但有流量时，业务容器的时间填充原则](../../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/离线计费管理/BIT160 控制话单中业务容器的Duration为0但有流量时，业务容器的时间填充原则_11113630.md)
- [BIT1105 控制当PCRF下发非法CG IP和端口时是否去激活用户](../../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/离线计费管理/BIT1105 控制当PCRF下发非法CG IP和端口时是否去激活用户_10873924.md)
- [BIT1211 控制话单中流量容器的QoS-Info是否携带APN-AMBR字段](../../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/离线计费管理/BIT1211 控制话单中流量容器的QoS-Info是否携带APN-AMBR字段_98644149.md)

#### [测量指标](#ZH-CN_TOPIC_0229423866)

本特性无相关测量指标。
