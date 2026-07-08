# 显示LINK性能统计实时结果(DSP RTMPERFCNTLINK)

- [命令功能](#ZH-CN_CONCEPT_0253163160__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0253163160__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0253163160__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0253163160__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0253163160__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0253163160__1.3.6.1)
- [参考信息](#ZH-CN_CONCEPT_0253163160__1.3.7.1)

#### [命令功能](#ZH-CN_CONCEPT_0253163160)

该命令用于实时查看LINK_VNFC当前性能统计的情况，即查询某一对象实例的某一单元下所有指标的当前性能统计值。

#### [注意事项](#ZH-CN_CONCEPT_0253163160)

- 系统最多支持5个用户并发执行该命令。
- 由于各进程、各类型指标的采样点不能完全统一，因此指标结果存在一定的误差，统计误差最大不超过该指标在10s内的统计变化值。
- 测量周期前10s执行该命令查看性能统计，“查询结果”会返回“Result is UnReliable”，如果出现了此现象，可等待10s再查询。
- 使用该命令查询之前需要先在U2020/MAE上创建基于该测量对象实例的话统统计任务，等待5min后再执行相应查询命令。基于SGSN对象的话统指标不需要创建统计任务，该对象的测量单元可直接查询。

#### [本地用户权限](#ZH-CN_CONCEPT_0253163160)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0253163160)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0253163160)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOC | 测量对象 | 可选必选说明：必选参数。<br>参数含义：测量对象类ID。<br>数据来源：本端规划。<br>取值范围：<br>- “GNGPIP(GnGp IP)”<br>- “SGSN(USN function)”<br>- “M3UA_LNK(M3UA链路)”<br>- “M3UA_LNKSET(M3UA链路集)”<br>- “M3UA_DE(M3UA目的实体)”<br>- “VLR(VLR)”<br>- “DNS_INQUIRY(DNS查询)”<br>- “DIAMETER_LINK(Diameter链路)”<br>- “DIAMETER_LINKSET(Diameter链路集)”<br>- “SCTP_LINK(SCTP链路)”<br>- “VM_USN(虚拟机)”<br>- “M3UA_RT(M3UA信令路由)”<br>- “RU(资源单元)”<br>- “ScalGroup(ScalGroup)”<br>默认值：无 |
| MOI | 实例名称 | 可选必选说明：必选参数。<br>参数含义：测量对象实例。<br>数据来源：本端规划。<br>前提条件：该测量实例已经在U2020/MAE上话统测量管理（通过“性能->测量管理”菜单打开）中下发，SGSN对象类实例除外。<br>取值范围：1~63位字符串<br>默认值：无 |
| MUID | 测量单元 | 可选必选说明：必选参数。<br>参数含义：测量对象对应的测量单元。<br>数据来源：本端规划。<br>取值范围：<br>该参数在<br>“MOC”<br>参数设置为<br>“GNGPIP(GnGp IP)”<br>时：<br>- “PERF_TYPE_GTPU_IP(指定Gn IP流量)”<br>- “PERF_TYPE_GTP_MESSAGE_WITH_IP(指定IP地址的GTP报文)”<br>该参数在<br>“MOC”<br>参数设置为<br>“SGSN(USN function)”<br>时：<br>- “PERF_TYPE_GTP(GTP承载)”<br>- “PERF_TYPE_GTP_CP(GTP消息处理)”<br>- “PERF_TYPE_GTP_DNS(SGSN的DNS请求)”<br>- “PERF_TYPE_RANAP(RANAP)”<br>- “PERF_TYPE_SS7_SCCP_PERFORM(SCCP性能)”<br>- “PERF_TYPE_SS7_SCCP_AVAILABILITY(SCCP可用性)”<br>- “PERF_TYPE_SS7_SCCP_ULTILIZATION(SCCP利用率)”<br>- “PERF_TYPE_SS7_TCAP_ULTILIZATION(TCAP组元利用率)”<br>- “PERF_TYPE_SS7_TCAP_MSG_NUM(TCAP消息)”<br>- “PERF_TYPE_SS7_TCAP_TSL(TCAP TSL)”<br>- “PERF_TYPE_SS7_TCAP_CSL(TCAP CSL)”<br>- “PERF_TYPE_SPECIFIC_ABNORMAL_GTP(GTP异常报文)”<br>- “PERF_TYPE_S1AP(S1接口统计)”<br>- “PERF_TYPE_S6A(S6a接口统计)”<br>- “PERF_TYPE_S1_PAGING(S1模式寻呼)”<br>- “PERF_TYPE_SGS(SGs接口统计)”<br>- “PERF_TYPE_CBS(小区广播业务)”<br>- “PERF_TYPE_SYS_OVERLOAD_CTRL_WHOLE_SYSTEM(整系统因流控而丢弃的消息统计)”<br>- “PERF_TYPE_NBS1_PAGING(NB-S1模式寻呼)”<br>- “PERF_TYPE_IP_PACKETS(转发面报文统计)”<br>- “PERF_TYPE_S13(S13接口统计)”<br>- “PERF_TYPE_IP_PACKETS(转发面报文统计)”<br>该参数在<br>“MOC”<br>参数设置为<br>“M3UA_LNK(M3UA链路)”<br>时：<br>- “PERF_TYPE_SS7_M3UA_LINK(M3UA信令链路)”<br>该参数在<br>“MOC”<br>参数设置为<br>“M3UA_LNKSET(M3UA链路集)”<br>时：<br>- “PERF_TYPE_SS7_M3UA_LINKSET(M3UA信令链路集)”<br>该参数在<br>“MOC”<br>参数设置为<br>“M3UA_DE(M3UA目的实体)”<br>时：<br>- “PERF_TYPE_SS7_M3UA_DE(M3UA目的信令点)”<br>该参数在<br>“MOC”<br>参数设置为<br>“VLR(VLR)”<br>时：<br>- “PERF_TYPE_SGS_WITH_SPECIFIC_VLR(指定VLR的SGs基本业务)”<br>该参数在<br>“MOC”<br>参数设置为<br>“DNS_INQUIRY(DNS查询)”<br>时：<br>- “PERF_TYPE_DNS_INQUIRY(DNS服务器查询)”<br>该参数在<br>“MOC”<br>参数设置为<br>“DIAMETER_LINK(Diameter链路)”<br>时：<br>- “PERF_TYPE_DIAMETER_LINK(Diameter链路)”<br>- “PERF_TYPE_DIAMETER_LINKSET_S1_MODE_LOCATION_UPDATE(指定Diameter链路S1模式位置更新)”<br>- “PERF_TYPE_DIAMETER_LINKSET_S1_MODE_AUTHENTICATION(指定Diameter链路S1模式信息鉴权)”<br>该参数在<br>“MOC”<br>参数设置为<br>“DIAMETER_LINKSET(Diameter链路集)”<br>时：<br>- “PERF_TYPE_DIAMETER_LINKSET(Diameter链路集)”<br>该参数在<br>“MOC”<br>参数设置为<br>“SCTP_LNK(SCTP链路)”<br>时：<br>- “PERF_TYPE_SCTP_LINK_S1_MODE_SCTP_LINK_TRANSFER(指定SCTP链路S1模式SCTP链路转发)”<br>该参数在<br>“MOC”<br>参数设置为<br>“VM_USN(虚拟机)”<br>时：<br>- “PERF_TYPE_VM_LINK(虚拟机资源_LINK)”<br>- “PERF_TYPE_GTPC_VM_MSG_SPECS(虚拟机级信令面消息处理统计)”<br>该参数在<br>“MOC”<br>参数设置为<br>“RU(资源单元)”<br>时：<br>- “PERF_TYPE_RU_CPU_RESOURCE(资源单元CPU资源_LINK)”<br>该参数在<br>“MOC”<br>参数设置为<br>“ScalGroup(ScalGroup)”<br>时:<br>- “PERF_TYPE_SCALEGROUP_WORKLOAD(ScalGroup负载_LINK)”<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0253163160)

查询“虚拟机”对象的“虚拟机资源_LINK”单元下的所有指标的当前实时统计值：

DSP RTMPERFCNTLINK: MOC=VM_USN, MOI="SPU_B_0066", MUID=PERF_TYPE_VM_LINK;

```
%%DSP RTMPERFCNTLINK: MOC=VM_USN, MOI="SPU_B_0066", MUID=PERF_TYPE_VM_LINK;%%
RETCODE = 0  操作成功。

操作结果如下
----------
                                             测量对象 = 虚拟机
                                     测量对象实例名称 = SPU_B_0066
                                             测量单元 = 虚拟机资源_LINK
                                             测量结果 = Result is Reliable!
       基于虚拟机的SGsAP Location Update请求次数(次) = 0
       基于虚拟机的SGsAP Location Update成功次数(次) = 0
                    
(结果个数 = 2)
---    END
```

#### [参考信息](#ZH-CN_CONCEPT_0253163160)

*表1 对象实例输入格式*

| 测量对象类 | 对象实例数据获取参考 | 对象实例输入格式 | 输入格式示例 |
| --- | --- | --- | --- |
| GNGPIP：GnGp IP | 对端GGSN/S-GW GTPC地址 | GnGp接口IP地址 | "192.168.41.11" |
| SGSN：USN function | 0 | "0" | "0" |
| M3UA_LNK：M3UA链路 | **[LST M3LNK](../../../信令传输管理/M3UA管理/M3UA链路/查询M3UA信令链路(LST M3LNK)_26146306.md)** | 链路号 | "1" |
| M3UA_LNKSET：M3UA链路集 | **[LST M3LKS](../../../信令传输管理/M3UA管理/M3UA链路集/查询M3UA信令链路集(LST M3LKS)_26146312.md)** | 链路集索引 | "1" |
| M3UA_DE：M3UA目的实体 | **[LST M3DE](../../../信令传输管理/M3UA管理/M3UA目的实体/查询M3UA目的实体(LST M3DE)_26306114.md)** | 目的实体索引 | "1" |
| VLR：VLR | **[LST VLR](../../../电路域联合业务/VLR管理/查询VLR配置信息(LST VLR)_72225125.md)** | VLR号 | "86139019201" |
| DNS_INQUIRY：DNS查询 | **[LST DNSS](../../../GTP-C接口管理/DNS/DNS服务器管理/查询DNS服务器(LST DNSS)_26305708.md)** | IPV4地址 | "192.168.41.11" |
| DIAMETER_LINK：Diameter链路 | **[LST DMLNK](../../../信令传输管理/Diameter管理/Diameter链路/查询Diameter链路配置(LST DMLNK)_26146276.md)** | 链路号 | "1" |
| DIAMETER_LINKSET：Diameter链路集 | **[LST DMLKS](../../../信令传输管理/Diameter管理/Diameter链路集/查询Diameter链路集配置(LST DMLKS)_26146280.md)** | 链路集索引 | "1" |
| SCTP_LNK：SCTP链路 | **[LST S1APLE](../../../S1接口管理/S1AP本地实体/查询S1AP本地实体(LST S1APLE)_72345855.md)**<br>和<br>**[DSP S1APLNK](../../../S1接口管理/S1AP链路/显示S1AP连接状态(DSP S1APLNK)_26146252.md)** | 本端IP地址：本端端口号：对端IP地址：对端端口号 | "192.168.152.1:31201:192.168.152.20:31201" |
| VM_USN：虚拟机<br>说明：此对象在Full-Stack裸机及三方CaaS场景下不生效。 | **[DSP NODE](../../../../../../平台服务管理/设备管理/节点管理/节点查询（DSP NODE）_71678755.md)** | 虚拟机名称 | "SPU_B_0066" |
| RU: 资源单元 | **[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)** | 资源单元名称 | "LINK_SP_RU_0064" |
| ScalGroup:ScalGroup 名字 | **[DSP WORKLOAD](../../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/VM负载管理/查询系统负载(DSP WORKLOAD)_29626911.md)** | ScaleGroup的名字 | "SG1_LINK" |
