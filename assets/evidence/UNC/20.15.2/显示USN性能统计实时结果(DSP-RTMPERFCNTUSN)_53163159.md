# 显示USN性能统计实时结果(DSP RTMPERFCNTUSN)

- [命令功能](#ZH-CN_CONCEPT_0253163159__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0253163159__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0253163159__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0253163159__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0253163159__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0253163159__1.3.6.1)
- [参考信息](#ZH-CN_CONCEPT_0253163159__1.3.7.1)

#### [命令功能](#ZH-CN_CONCEPT_0253163159)

**适用网元：MME**

该命令用于实时查看USN_VNFC当前性能统计的情况，即查询某一对象实例的某一单元下所有指标的当前性能统计值。

#### [注意事项](#ZH-CN_CONCEPT_0253163159)

- 系统最多支持5个用户并发执行该命令。
- 由于各进程、各类型指标的采样点不能完全统一，因此指标结果存在一定的误差，统计误差最大不超过该指标在10s内的统计变化值。
- 测量周期前10s执行该命令查看性能统计，“查询结果”会返回“Result is UnReliable”，如果出现了此现象，可等待10s再查询。
- 使用该命令查询之前需要先在U2020/MAE上创建基于该测量对象实例的话统统计任务，等待5min后再执行相应查询命令。基于SGSN对象的话统指标不需要创建统计任务，该对象的测量单元可直接查询。
- 此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。

#### [本地用户权限](#ZH-CN_CONCEPT_0253163159)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0253163159)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0253163159)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOC | 测量对象 | 可选必选说明：必选参数。<br>参数含义：测量对象类ID。<br>数据来源：本端规划。<br>取值范围：<br>- “RNCID(RNC ID)”<br>- “CG_IP(CG IP)”<br>- “GB_RAI(Gb模式路由区号)”<br>- “IU_RAI(Iu模式路由区号)”<br>- “GNGPIP(GnGp IP)”<br>- “APN(APN)”<br>- “SGSN(USN function)”<br>- “GGSNIP(GGSN IP地址)”<br>- “VLR(VLR)”<br>- “PLMN(PLMN)”<br>- “PAGING_RULE(寻呼规则)”<br>- “PRA(PRA)”<br>- “BSSID(Gb接口BSSID)”<br>- “CELL(小区号)”<br>- “IMSI(IMSI号码)”<br>- “MVNO(MVNO)”<br>- “UE_TYPE(UE类型)”<br>- “TAI_GROUP(TAI组)”<br>- “ENODEB(eNodeB)”<br>- “S11U_IP(S11U IP)”<br>- “VM_USN(虚拟机)”<br>- “RU(资源单元)”<br>- “ScaleGroup(ScaleGroup)”<br>- “HSS_HOSTNAME(HSS主机名)”<br>默认值：无 |
| MOI | 实例名称 | 可选必选说明：必选参数。<br>参数含义：测量对象实例。<br>数据来源：本端规划。<br>前提条件：该测量实例已经在U2020/MAE上话统测量管理（通过“性能->测量管理”菜单打开）中下发，SGSN对象类实例除外。<br>取值范围：1~63位字符串<br>默认值：无 |
| MUID | 测量单元 | 可选必选说明：必选参数。<br>参数含义：测量对象对应的测量单元。<br>数据来源：本端规划。<br>取值范围：<br>该参数在<br>“MOC”<br>参数设置为<br>“RNCID(RNC ID)”<br>时：<br>- “PERF_TYPE_RELOCATION(指定RNC重定位)”<br>- “PERF_TYPE_RNCID_PACKETS_USR_PLANE(指定RNC的用户面流量)”<br>- “PERF_TYPE_RESOURCE_RNC(指定RNC无线资源)”<br>- “PERF_TYPE_3G_SM_RESOURCE_INRNC(指定RNC会话资源)”<br>该参数在<br>“MOC”<br>参数设置为<br>“CG_IP(CG IP)”<br>时：<br>- “PERF_TYPE_CDR_GTP_TO_CG(Ga接口)”<br>该参数在<br>“MOC”<br>参数设置为<br>“GB_RAI(Gb模式路由区号)”<br>时：<br>- “PERF_TYPE_2G_ATTACH(指定路由区Gb模式附着流程)”<br>- “PERF_TYPE_2G_DETACH(指定路由区Gb模式分离流程测量)”<br>- “PERF_TYPE_2G_INSIDE_SGSN_RAU(指定路由区Gb模式SGSN内路由更新)”<br>- “PERF_TYPE_2G_AMONG_SGSN_RAU(指定路由区Gb模式SGSN间路由更新)”<br>- “PERF_TYPE_2G_PS_RRM(指定路由区Gb模式分组寻呼)”<br>- “PERF_TYPE_2G_USER_PER_RA(指定路由区Gb模式无线资源)”<br>- “PERF_TYPE_2G_SM_RESOURCE_INRAI(指定路由区Gb模式会话资源)”<br>- “PERF_TYPE_2G_SM_COURSE_RAI(路由区2G会话业务测量)”<br>- “PERF_TYPE_GBMOCN(Gb MOCN模式下基本流程测量)”<br>该参数在<br>“MOC”<br>参数设置为<br>“IU_RAI(Iu模式路由区号)”<br>时：<br>- “PERF_TYPE_3G_ATTACH(指定路由区Iu模式附着流程测量)”<br>- “PERF_TYPE_3G_DETACH(指定路由区Iu模式分离流程测量)”<br>- “PERF_TYPE_3G_INSIDE_SGSN_RAU(指定路由区Iu模式SGSN内路由更新)”<br>- “PERF_TYPE_3G_AMONG_SGSN_RAU(指定路由区Iu模式SGSN间路由更新)”<br>- “PERF_TYPE_3G_SERVICE_REQUEST(指定路由区Iu模式服务请求性能)”<br>- “PERF_TYPE_SYS_SWITCH(指定路由区Iu模式系统间切换)”<br>- “PERF_TYPE_3G_PS_RRM(指定路由区Iu模式分组寻呼)”<br>- “PERF_TYPE_3G_USER_PER_RA(指定路由区Iu模式无线资源)”<br>- “PERF_TYPE_3G_SM_RESOURCE_INRAI(指定路由区Iu模式会话资源)”<br>- “PERF_TYPE_3G_SM_COURSE_RAI(路由区3G会话业务测量)”<br>- “PERF_TYPE_IUMOCN(Iu MOCN模式下基本流程测量)”<br>- “PERF_TYPE_3G_SM_RAB_WITHIN_RAI(指定路由区Iu模式RAB)”<br>该参数在<br>“MOC”<br>参数设置为<br>“GNGPIP(GnGp IP)”<br>时：<br>- “PERF_TYPE_GTPU_IP(指定Gn IP流量)”<br>- “PERF_TYPE_GTP_MESSAGE_WITH_IP(指定IP地址的GTP报文)”<br>该参数在<br>“MOC”<br>参数设置为<br>“APN(APN)”<br>时：<br>- “PERF_TYPE_APN_GB_MODE_ACTIVE(指定APN Gb模式会话激活)”<br>- “PERF_TYPE_APN_IU_MODE_ACTIVE(指定APN Iu模式会话激活)”<br>- “PERF_TYPE_APN_GB_MODE_SM_RESOURCE(特定APN的Gb模式会话资源)”<br>- “PERF_TYPE_APN_IU_MODE_SM_RESOURCE(特定APN的Iu模式会话资源)”<br>- “PERF_TYPE_APN_UHPU_USER_PLANE(特定APN的数据包)”<br>- “PERF_TYPE_APN_S1_MODE_PDN_CONNECTIVITY(指定APN S1模式PDN连接)”<br>- “PERF_TYPE_APN_SIG_CONGESTION_CONTROL(指定APN信令拥塞控制)”<br>- “PERF_TYPE_APN_NBS1_DATA_OVER_NAS(基于APN的NB-S1模式Data over NAS)”<br>- “PERF_TYPE_APN_S1_BEARER_ACTIVATION(指定APN的S1模式承载统计)”<br>该参数在<br>“MOC”<br>参数设置为<br>“SGSN(USN function)”<br>时：<br>- “PERF_TYPE_SGSN_CDR(SGSN计费话单)”<br>- “PERF_TYPE_GTP_CP(GTP消息处理)”<br>- “PERF_TYPE_GTP_DNS(SGSN的DNS请求)”<br>- “PERF_TYPE_UHPU_GN(用户面Gn接口)”<br>- “PERF_TYPE_UHPU_GP(用户面Gp接口)”<br>- “PERF_TYPE_UHPU_UNKNOWN_IF(用户面未配置类型)”<br>- “PERF_TYPE_UHPU(GTP-U承载)”<br>- “PERF_TYPE_UHPU_UP(GTP-U数据包转发)”<br>- “PERF_TYPE_UHPU_CP(GTP-U消息处理)”<br>- “PERF_TYPE_UHPU_QOS(GTP-U数据包各QoS级别转发)”<br>- “PERF_TYPE_UHPU_BANDWIDTH(转发带宽测量)”<br>- “PERF_TYPE_2G_MM(Gb模式MM L3信令)”<br>- “PERF_TYPE_2G_GLOBAL_ATTACH(Gb模式附着流程)”<br>- “PERF_TYPE_2G_GLOBAL_DETACH(Gb模式分离流程)”<br>- “PERF_TYPE_2G_GLOBAL_INSIDE_SGSN_RAU(Gb模式SGSN内路由更新)”<br>- “PERF_TYPE_2G_GLOBAL_AMONG_SGSN_RAU(Gb模式SGSN间路由更新)”<br>- “PERF_TYPE_2G_AUTH(Gb模式安全性)”<br>- “PERF_TYPE_GB_MM_RESOURCE(Gb模式无线资源)”<br>- “PERF_TYPE_GB_MM_RRM(Gb模式寻呼)”<br>- “PERF_TYPE_3G_MM(Iu模式 MM L3信令)”<br>- “PERF_TYPE_3G_GLOBAL_ATTACH(Iu模式附着)”<br>- “PERF_TYPE_3G_GLOBAL_DETACH(Iu模式分离)”<br>- “PERF_TYPE_3G_GLOBAL_INSIDE_SGSN_RAU(Iu模式SGSN内路由更新)”<br>- “PERF_TYPE_3G_GLOBAL_AMONG_SGSN_RAU(Iu模式SGSN间路由更新)”<br>- “PERF_TYPE_3G_AUTH(Iu模式安全性)”<br>- “PERF_TYPE_IU_MM_RRM(Iu模式寻呼)”<br>- “PERF_TYPE_IU_MM_RESOURCE(Iu模式无线资源)”<br>- “PERF_TYPE_3G_GLOBAL_SERVICE_REQUEST(Iu模式服务请求)”<br>- “PERF_TYPE_GLOBAL_SYS_SWITCH(系统间切换)”<br>- “PERF_TYPE_GLOBAL_RELOCATION(SGSN重定位)”<br>- “PERF_TYPE_2G_SM_COURSE(Gb模式会话激活)”<br>- “PERF_TYPE_2G_SM_DEACTIVE(Gb模式会话去激活)”<br>- “PERF_TYPE_2G_SM_MODIFY(Gb模式会话修改)”<br>- “PERF_TYPE_2G_L3(Gb模式层3)”<br>- “PERF_TYPE_2G_SM_RESOURCE(Gb模式会话资源)”<br>- “PERF_TYPE_3G_SM_COURSE(Iu模式会话激活)”<br>- “PERF_TYPE_3G_SM_DEACTIVE(Iu模式会话去激活)”<br>- “PERF_TYPE_3G_SM_MODIFY(Iu模式会话修改)”<br>- “PERF_TYPE_3G_L3(Iu模式层3)”<br>- “PERF_TYPE_3G_SM_KEEP(Iu模式会话保留)”<br>- “PERF_TYPE_3G_SM_RAB(Iu模式RAB)”<br>- “PERF_TYPE_3G_SM_RESOURCE(Iu模式会话资源)”<br>- “PERF_TYPE_BSSAPPLUS(BSSAP+基本业务)”<br>- “PERF_TYPE_BSSAPPLUS_ERROR(BSSAP+信令规程错误与超时)”<br>- “PERF_TYPE_MAP(MAP基本业务)”<br>- “PERF_TYPE_MAP_ERROR(MAP信令规程错误与超时)”<br>- “PERF_TYPE_MAP_PUBLIC_ERROR(MAP公共业务规程错误)”<br>- “PERF_TYPE_MAP_GC(MAP的Gc接口消息转发业务量)”<br>- “PERF_TYPE_SS(补充业务)”<br>- “PERF_TYPE_MAP_SMS(短消息)”<br>- “PERF_TYPE_GB_SRVHANDOVER(Gb模式业务切换次数统计)”<br>- “PERF_TYPE_IU_SRVHANDOVER(Iu模式业务切换次数统计)”<br>- “PERF_TYPE_GB_DIFFSRV_USER_ACCESS_REJECT(Gb模式用户接入拒绝次数统计)”<br>- “PERF_TYPE_IU_DIFFSRV_USER_ACCESS_REJECT(Iu模式用户接入拒绝次数统计)”<br>- “PERF_TYPE_GB_DIFFSRV_PDP_ACCESS_REJECT(Gb模式PDP接入拒绝次数统计)”<br>- “PERF_TYPE_IU_DIFFSRV_PDP_ACCESS_REJECT(Iu模式PDP接入拒绝次数统计)”<br>- “PERF_TYPE_2G_EDGE_ATTACH(EDGE用户的Gb模式附着流程)”<br>- “PERF_TYPE_2G_EDGE_SM_COURSE(EDGE用户的Gb模式会话激活流程)”<br>- “PERF_TYPE_2G_APN_CORRECTION(Gb模式APN纠错)”<br>- “PERF_TYPE_3G_APN_CORRECTION(Iu模式APN纠错)”<br>- “PERF_TYPE_3G_SM_TUNNEL(Iu模式隧道相关)”<br>- “PERF_TYPE_2G_PDP_DEACT(2G PDP上下文去激活统计)”<br>- “PERF_TYPE_3G_PDP_DEACT(3G PDP上下文去激活统计)”<br>- “PERF_TYPE_SPECIFIC_ABNORMAL_GTP(GTP异常报文)”<br>- “PERF_TYPE_S1AP(S1接口统计)”<br>- “PERF_TYPE_S6A(S6a接口统计)”<br>- “PERF_TYPE_S1_ATTACH(S1模式附着)”<br>- “PERF_TYPE_S1_DETACH(S1模式分离)”<br>- “PERF_TYPE_S1_INTRA_MME_TAU(S1模式MME内跟踪区更新)”<br>- “PERF_TYPE_S1_INTER_MME_TAU(S1模式MME间跟踪区更新)”<br>- “PERF_TYPE_S1_INTRA_MME_HANDOVER(S1模式MME内Handover)”<br>- “PERF_TYPE_S1_INTER_MME_HANDOVER(S1模式MME间Handover)”<br>- “PERF_TYPE_S1_SECURITY(S1模式安全性)”<br>- “PERF_TYPE_S1_PAGING(S1模式寻呼)”<br>- “PERF_TYPE_S1_SERVICE_REQUEST(S1模式服务请求)”<br>- “PERF_TYPE_S1_USER_RESOURCE(S1模式用户资源)”<br>- “PERF_TYPE_S1_MME_S1_RELEASE(S1模式MME发起的RELAESE)”<br>- “PERF_TYPE_S1_INTRA_ENB_CONFIG_TRANSFER(S1模式intra MME eNB配置传输)”<br>- “PERF_TYPE_S1_INTER_ENB_CONFIG_TRANSFER(S1模式inter MME eNB配置传输)”<br>- “PERF_TYPE_INTER_CN(LTE和UTRAN及GERAN互通)”<br>- “PERF_TYPE_S1_SRVCC(S1模式SRVCC)”<br>- “PERF_TYPE_INTRA_CN(Intra USN LTE和GSM及UMTS互通)”<br>- “PERF_TYPE_S1_BEARER_ACTIVATION(S1模式承载激活)”<br>- “PERF_TYPE_S1_BEARER_DEACTIVATION(S1模式承载去激活)”<br>- “PERF_TYPE_S1_BEARER_MODIFICATION(S1模式承载修改)”<br>- “PERF_TYPE_S1_PDN_CONNECTIVITY(S1模式PDN连接)”<br>- “PERF_TYPE_S1_PDN_DISCONNECTION(S1模式PDN断连)”<br>- “PERF_TYPE_S1_BEARER_RESOURCE(S1模式承载资源)”<br>- “PERF_TYPE_S1_BEARER_ALLOCATION(S1模式承载分配)”<br>- “PERF_TYPE_SIG_REDUCE(异常信令抑制)”<br>- “PERF_TYPE_4G_APN_CORRECTION(S1模式APN纠错)”<br>- “PERF_TYPE_SGS(SGs接口统计)”<br>- “PERF_TYPE_SYS_OVERLOAD_CTRL_WHOLE_SYSTEM(整系统因流控而丢弃的消息统计)”<br>- “PERF_TYPE_UHPU_S4(用户面S4接口)”<br>- “PERF_TYPE_PGW_RESELECT(本地P-GW的PDN重建)”<br>- “PERF_TYPE_INTER_USN(Inter USN LTE和GSM及UMTS互通)”<br>- “PERF_TYPE_SGW_PGW_RESTORATION(S-GW或P-GW故障业务恢复)”<br>- “PERF_TYPE_SV(Sv接口统计)”<br>- “PERF_TYPE_VOLTE(VOLTE)”<br>- “PERF_TYPE_CHR(CHR业务)”<br>- “PERF_TYPE_PRA(PRA业务)”<br>- “PERF_TYPE_UE_CAP_INFO_IND(S1模式UE能力信息指示)”<br>- “PERF_TYPE_UHPU_S11_U(用户面S11-U接口)”<br>- “PERF_TYPE_NBS1_ATTACH(NB-S1模式附着)”<br>- “PERF_TYPE_NBS1_DETACH(NB-S1模式分离)”<br>- “PERF_TYPE_NBS1_INTRA_MME_TAU(NB-S1模式MME内跟踪区更新)”<br>- “PERF_TYPE_NBS1_INTER_MME_TAU(NB-S1模式MME间跟踪区更新)”<br>- “PERF_TYPE_NBS1_PAGING(NB-S1模式寻呼)”<br>- “PERF_TYPE_NBS1_SERVICE_REQUEST(NB-S1模式服务请求)”<br>- “PERF_TYPE_NBS1_USER_RESOURCE(NB-S1模式用户资源)”<br>- “PERF_TYPE_NBS1_DATA_OVER_NAS(NB-S1模式Data over NAS)”<br>- “PERF_TYPE_NBS1_BEARER_RESOURCE(NB-S1模式承载资源)”<br>- “PERF_TYPE_IP_PACKETS(转发面报文统计)”<br>- “PERF_TYPE_S13(S13接口统计)”<br>- “PERF_TYPE_SIG_STORM_SHAPING_PROCESS(信令风暴平滑处理统计)”<br>- “PERF_TYPE_REDUNDANCY(设备级容灾业务)”<br>- “PERF_TYPE_NBS1_MME_S1_RELEASE(NB-S1模式MME发起的S1连接释放)”<br>- “PERF_TYPE_NBS1_BEARER_DEACTIVATION(NB-S1模式承载去激活)”<br>- “PERF_TYPE_NBS1_BEARER_MODIFICATION(NB-S1模式承载修改)”<br>- “PERF_TYPE_NBS1_PDN_CONNECTIVITY(NB-S1模式PDN连接)”<br>- “PERF_TYPE_NBS1_PDN_DISCONNECTION(NB-S1模式PDN断连)”<br>- “PERF_TYPE_NBS1_APN_CORRECTION(NB-S1模式APN纠错)”<br>- “PERF_TYPE_NBS1_SIG_MM_REDUCE(NB-S1模式移动管理异常信令节省)”<br>- “PERF_TYPE_NBS1_SIG_SM_REDUCE(NB-S1模式会话管理异常信令节省)”<br>- “PERF_TYPE_NBS1_SECURITY(NB-S1模式安全性)”<br>- “PERF_TYPE_IP_PACKETS(转发面报文统计)”<br>该参数在<br>“MOC”<br>参数设置为<br>“GGSNIP(GGSN IP地址)”<br>时：<br>- “PERF_TYPE_GGSNIP_GB_MODE_CREATE(指定GGSNIP GB模式会话激活)”<br>- “PERF_TYPE_GGSNIP_IU_MODE_CREATE(指定GGSNIP IU模式会话激活)”<br>该参数在<br>“MOC”<br>参数设置为<br>“VLR(VLR)”<br>时：<br>- “PERF_TYPE_BSSAPPLUS_PER_VLR(指定VLR的BSSAP+基本业务)”<br>- “PERF_TYPE_SGS_WITH_SPECIFIC_VLR(指定VLR的SGs基本业务)”<br>该参数在<br>“MOC”<br>参数设置为<br>“PLMN(PLMN)”<br>时：<br>- “PERF_TYPE_2G_PLMN_ATTACH(指定PLMN的GB模式附着用户数)”<br>- “PERF_TYPE_3G_PLMN_ATTACH(指定PLMN的Iu模式附着用户数)”<br>- “PERF_TYPE_3G_PLMN_ATTACH_COURSE(指定PLMN的Iu模式附着流程测量)”<br>- “PERF_TYPE_2G_PLMN_ATTACH_COURSE(指定PLMN的Gb模式附着流程测量)”<br>- “PERF_TYPE_3G_PLMN_SM_COURSE(指定PLMN的Iu模式会话激活)”<br>- “PERF_TYPE_2G_PLMN_SM_COURSE(指定PLMN的Gb模式会话激活)”<br>- “PERF_TYPE_3G_PLMN_SM_RESOURCE(指定PLMN的Iu模式会话资源)”<br>- “PERF_TYPE_2G_PLMN_SM_RESOURCE(指定PLMN的Gb模式会话资源)”<br>- “PERF_TYPE_2G_INTRA_RAU_WITHIN_PLMN(指定PLMN内Gb模式SGSN内路由更新)”<br>- “PERF_TYPE_3G_INTRA_RAU_WITHIN_PLMN(指定PLMN内Iu模式SGSN内路由更新)”<br>- “PERF_TYPE_S1_PLMN_MM_EMG(指定PLMN的紧急呼叫移动管理)”<br>- “PERF_TYPE_S1_PLMN_SM_EMG(指定PLMN的紧急呼叫会话管理)”<br>- “PERF_TYPE_S1_INTRA_MME_TAU_WITHIN_PLMN(指定PLMN的S1模式MME内跟踪区更新)”<br>- “PERF_TYPE_S1_INTER_MME_TAU_WITHIN_PLMN(指定PLMN的S1模式MME间跟踪区更新)”<br>- “PERF_TYPE_S1_SECURITY_WITHIN_PLMN(指定PLMN的S1模式安全性)”<br>- “PERF_TYPE_S1_ATTACH_WITHIN_PLMN(指定PLMN的S1模式附着)”<br>- “PERF_TYPE_S1_DETACH_WITHIN_PLMN(指定PLMN的S1模式分离)”<br>- “PERF_TYPE_S1_USER_RESOURCE_WITHIN_PLMN(指定PLMN的S1模式用户资源)”<br>- “PERF_TYPE_S1_PDN_CONNECTIVITY_WITHIN_PLMN(指定PLMN的S1模式PDN连接)”<br>- “PERF_TYPE_S1_BEARER_ACTIVATION_WITHIN_PLMN(指定PLMN的S1模式承载激活)”<br>- “PERF_TYPE_S1_BEARER_DEACTIVATION_WITHIN_PLMN(指定PLMN的S1模式承载去激活)”<br>- “PERF_TYPE_S1_BEARER_MODIFICATION_WITHIN_PLMN(指定PLMN的S1模式承载修改)”<br>- “PERF_TYPE_S1_BEARER_RESOURCE_WITHIN_PLMN(指定PLMN的S1模式承载资源)”<br>- “PERF_TYPE_S6A_WITHIN_PLMN(指定PLMN的S6a接口统计)”<br>- “PERF_TYPE_PLMN_TRAFFIC(指定PLMN的用户面流量)”<br>- “PERF_TYPE_PLMN_NBS1_DATA_OVER_NAS(基于PLMN的NB-S1模式Data over NAS)”<br>- “PERF_TYPE_PLMN_IMEI_CHECK(指定PLMN的IMEI Check)”<br>- “PERF_TYPE_PLMN_LCS(指定PLMN的位置业务)”<br>该参数在<br>“MOC”<br>参数设置为<br>“PAGING_RULE(寻呼规则)”<br>时：<br>- “PERF_TYPE_S1_PAGING_RULE(指定寻呼规则的S1模式寻呼)”<br>该参数在<br>“MOC”<br>参数设置为<br>“PRA(PRA)”<br>时：<br>- “PERF_TYPE_SPECIFIC_PRA(指定PRA的统计)”<br>该参数在<br>“MOC”<br>参数设置为<br>“ENODEB(eNodeB)”<br>时：<br>- “PERF_TYPE_S1_ENB_ATTACHED_USER_NUM(指定eNodeB S1模式附着用户数)”<br>该参数在<br>“MOC”<br>参数设置为<br>“S11U_IP(S11U IP)”<br>时：<br>- “PERF_TYPE_S11U_GTPU_IP(指定IP的S11-U口流量统计)”<br>该参数在<br>“MOC”<br>参数设置为<br>“VM_USN(虚拟机)”<br>时：<br>- “PERF_TYPE_VM_USN(虚拟机资源_USN)”<br>- “PERF_TYPE_USRPLANE_VM_MSG_SPECS (虚拟机级用户面消息处理统计)”<br>该参数在<br>“MOC”<br>参数设置为<br>“RU(资源单元)”<br>时：<br>- “PERF_TYPE_RU_CPU_RESOURCE(资源单元CPU资源_USN)”<br>该参数在<br>“MOC”<br>参数设置为<br>“ScalGroup(ScalGroup)”<br>时:<br>- “PERF_TYPE_SCALEGROUP_WORKLOAD(ScalGroup负载_USN)”<br>该参数在<br>“MOC”<br>参数设置为<br>“HSS_HOSTNAME(HSS主机名)”<br>时:<br>- “PERF_TYPE_S1_USER_RESOURCE_WITHIN_HSS(基于HSS的S1模式用户资源)”<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0253163159)

查询“SGSN”对象的“S1接口统计”单元下的所有指标的当前实时统计值：

DSP RTMPERFCNTUSN:MOC=SGSN,MOI="0",MUID=PERF_TYPE_S1AP;

```
%%DSP RTMPERFCNTUSN: MOC=SGSN,MOI="0",MUID=PERF_TYPE_S1AP;%%
RETCODE = 0  操作成功

操作结果如下
----------
                                             测量结果 = Result is Reliable!
                               S1连接建立请求次数(次) = 0
                               S1连接建立成功次数(次) = 0
                     eNodeB发起的S1 Reset请求次数(次) = 0
                     eNodeB发起的S1 Reset成功次数(次) = 0
                              SAE承载建立请求次数(次) = 0
                              SAE承载建立成功次数(次) = 0
                              SAE承载修改请求次数(次) = 0
                              SAE承载修改成功次数(次) = 0
                     MME发起的SAE承载释放请求次数(次) = 0
                     MME发起的SAE承载释放成功次数(次) = 0
                  eNodeB发起的SAE承载释放请求次数(次) = 0
                           S1接口收到上行消息包数(包) = 0
                           S1接口发送下行消息包数(包) = 0
                           S1接口收到上行流量(KBytes) = 0
                           S1接口发送下行流量(KBytes) = 0
           eNodeB触发S1释放请求次数（用户非活动）(次) = 0
             eNodeB触发S1释放请求次数（其他原因）(次) = 0
        MME发送Location Reporting Control消息次数(次) = 0
                   MME接收Location Report消息次数(次) = 0
MME接收Location Report Failure Indication消息次数(次) = 0
                                 整系统eNodeB个数(个) = 0
                   S1接口SCTP链路发送数据流量(KBytes) = 0
                   S1接口SCTP链路接收数据流量(KBytes) = 0
                       S1接口SCTP链路发送SCTP包数(个) = 0
                       S1接口SCTP链路接收SCTP包数(个) = 0
                       S1接口SCTP链路发送数据块数(个) = 0
                       S1接口SCTP链路接收数据块数(个) = 0
                       S1接口SCTP链路数据块重发数(个) = 0
(结果个数 = 1)
---    END
```

#### [参考信息](#ZH-CN_CONCEPT_0253163159)

*表1 对象实例输入格式*

| 测量对象类 | 对象实例数据获取参考 | 对象实例输入格式 | 输入格式示例 |
| --- | --- | --- | --- |
| RNCID：RNC ID | **[LST RNC](../../../Iu接口管理/Iu接口RNC信息/查询Iu接口RNC信息(LST RNC)_72345641.md)** | MCC：MNC：RNC标识 | "123:03:1191" |
| CG_IP：CG IP | **[LST CHGCG](../../../../计费管理/计费控制/查询CG配置参数(LST CHGCG)_26145376.md)** | CG的IP地址：协议类型：端口 | "192.168.1.145:0:4006" |
| GB_RAI：Gb模式路由区号 | **[LST PERFGBPAGING](../性能对象管理/查询Gb接口寻呼数据(LST PERFGBPAGING)_26146192.md)** | LAI：RAC | "123031901:01" |
| IU_RAI：Iu模式路由区号 | **[LST IUPAGING](../../../Iu接口管理/Iu接口寻呼数据/查询Iu接口寻呼数据(LST IUPAGING)_26146036.md)** | LAI：RAC | "123031901:01" |
| GNGPIP：GnGp IP | 对端GGSN/S-GW GTPC地址 | GnGp接口IP地址 | "192.168.41.11" |
| APN：APN | **[LST PERFOBJ](../性能对象管理/查询性能对象信息(LST PERFOBJ)_26306000.md)** | APN名称 | "HUAWEI119" |
| SGSN：USN function | 0 | "0" | "0" |
| GGSNIP：GGSN IP地址 | GGSN控制面ipv4地址 | 指定GGSN的IP地址 | "192.168.41.11" |
| VLR：VLR | [LST VLR](../../../电路域联合业务/VLR管理/查询VLR配置信息(LST VLR)_72225125.md) | VLR号 | "86139019201" |
| PLMN：PLMN | **[LST HPLMN](../../../网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/查询本地PLMN(LST HPLMN)_72345675.md)**<br>和<br>**[LST CONNECTPLMN](../../../网络管理/互联PLMN管理/查询互联PLMN(LST CONNECTPLMN)_72225723.md)** | MCC：MNC | "123:03" |
| PAGING_RULE：寻呼规则 | **[LST S1PAGINGRULE](../../../S1接口管理/S1寻呼规则管理/查询S1寻呼规则(LST S1PAGINGRULE)_72225927.md)** | 规则索引 | "1" |
| DSP S1APLNK | **[DSP S1APLNK](../../../S1接口管理/S1AP链路/显示S1AP连接状态(DSP S1APLNK)_26146252.md)** | eNodeB标识 | "233489" |
| PRA：PRA | **[LST PRAID](../../../移动性管理/PRA区域管理/PRA区域标识管理/查询PRA标识(LST PRAID)_26145596.md)** | PRA标识 | "800001" |
| BSSID：Gb接口BSSID | **[LST NSE](../../../Gb接口管理/信令实体管理/查询信令实体（LST NSE）_72345629.md)** | BSS编号 | "133" |
| CELL：小区号 | **[LST CELL](../../../Gb接口管理/小区管理/查询小区(LST CELL)_26145990.md)** | 小区号 | "123054804041026(123-05-18436-4-4134)" |
| IMSI：IMSI号码 | IMSI号码 | IMSI号码 | "123031600000002" |
| MVNO：MVNO | **[LST MVNO](../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/查询MVNO配置信息(LST MVNO)_26146070.md)** | MVNO标识 | "1" |
| UE_TYPE：UE类型 | 终端类型 | 终端类型 | "0"<br>说明：- "0":"Android"<br>- "1":"Black Berry"<br>- "2":"iOS"<br>- "3":"Windows"<br>- "4":"自定义类型1"<br>- "5":"自定义类型2"<br>- "6":"自定义类型3"<br>- "7":"自定义类型4"<br>- "8":"自定义类型5"<br>- "9":"自定义类型6"<br>- "10":"自定义类型7"<br>- "11":"自定义类型8"<br>- "12":"自定义类型9"<br>- "13":"自定义类型10"<br>- "14":"自定义类型11"<br>- "15":"自定义类型12" |
| TAI_GROUP：TAI组 | **[LST PERFOBJ](../性能对象管理/查询性能对象信息(LST PERFOBJ)_26306000.md)** | TAI组名 | "huawei" |
| S11U_IP：S11U IP | 对端S-GW GTPU地址 | S11U接口IP地址 | "192.168.41.11" |
| VM_USN：虚拟机<br>说明：此对象在Full-Stack裸机及三方CaaS场景下不生效。 | **[DSP NODE](../../../../../../平台服务管理/设备管理/节点管理/节点查询（DSP NODE）_71678755.md)** | 虚拟机名称 | "SPU_B_0066" |
| RU: 资源单元 | **[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)** | 资源单元名称 | "USN_SP_RU_0064" |
| ScalGroup:ScalGroup 名字 | **[DSP WORKLOAD](../../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/VM负载管理/查询系统负载(DSP WORKLOAD)_29626911.md)** | ScaleGroup的名字 | "SG1_USN" |
| HSS_HOSTNAME：HSS主机名 | **[LST PERFOBJ](../性能对象管理/查询性能对象信息(LST PERFOBJ)_26306000.md)** | HSS对象名称 | "LOCAL" |
