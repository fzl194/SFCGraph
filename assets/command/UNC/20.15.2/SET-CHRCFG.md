---
id: UNC@20.15.2@MMLCommand@SET CHRCFG
type: MMLCommand
name: SET CHRCFG（设置CHR配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CHRCFG
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- CHR管理
- CHR配置
status: active
---

# SET CHRCFG（设置CHR配置）

## 功能

**适用网元：SGSN、MME**

该命令用于系统在上报CHR单据时，配置单据采集及订阅的流程。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 本命令执行后立即生效。
- CHR冲突流程处理目前只对4G用户生效。
- 当软参BYTE_EX_B53 BIT2设置为“1”时，NSA协商失败的流程都会上报CHR，上报流程不受该命令控制。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GERANSUCC | Gb模式流程成功时上报选项 | 可选必选说明：可选参数<br>参数含义：用于控制在Gb模式流程成功时，勾选流程上报CHR单据。<br>数据来源：本端规划<br>取值范围：<br>- “ATTACH(Attach)”：表示附着流程成功后需要上报CHR单据。<br>- “DETACH(Detach)”：表示分离流程成功后需要上报CHR单据。<br>- “RAU(Routing Area Update)”：表示路由区更新流程成功后需要上报CHR单据。<br>- “SYSCHG(Inter System Change)”：表示系统切换流程成功后需要上报CHR单据。<br>- “ACTPDP(PDP Context Activation)”：表示激活流程成功后需要上报CHR单据。<br>- “DEACTPDP(PDP Context Deactivation)”：表示去激活流程成功后需要上报CHR单据。<br>- “MODPDP(PDP Context Modification)”：表示PDP修改流程成功后需要上报CHR单据。<br>- “PAGING(Paging)”：表示寻呼流程成功后需要上报CHR单据。<br>- “SUSPEND(Suspend)”：表示挂起流程成功后需要上报CHR单据。<br>- “CANCELLOC(Cancel Location)”：表示位置取消流程成功后需要上报CHR单据。<br>- “OTHER(Other Procedure)”：表示其它流程成功后需要上报CHR单据。<br>- “RESERVED1(RESERVED1)”<br>- “RESERVED2(RESERVED2)”<br>- “RESERVED3(RESERVED3)”<br>- “RESERVED4(RESERVED4)”<br>- “RESERVED5(RESERVED5)”<br>- “RESERVED6(RESERVED6)”<br>- “RESERVED7(RESERVED7)”<br>- “RESERVED8(RESERVED8)”<br>- “RESERVED9(RESERVED9)”<br>- “RESERVED10(RESERVED10)”<br>- “RESERVED11(RESERVED11)”<br>- “RESERVED12(RESERVED12)”<br>- “RESERVED13(RESERVED13)”<br>- “RESERVED14(RESERVED14)”<br>- “RESERVED15(RESERVED15)”<br>系统初始设置值：<br>“全部清空”<br>。<br>配置原则：勾选的流程成功后将上报CHR单据，未勾选的流程成功后将不上报CHR单据。<br>说明：“RESERVED1(RESERVED1)”<br>～<br>“RESERVED15(RESERVED15)”<br>是保留取值，暂不使用。 |
| GERANFAIL | Gb模式流程失败时上报选项 | 可选必选说明：可选参数<br>参数含义：用于控制在Gb模式流程失败时，勾选流程上报CHR单据。<br>数据来源：本端规划<br>取值范围：<br>- “ATTACH(Attach)”：表示附着流程失败后需要上报CHR单据。<br>- “DETACH(Detach)”：表示分离流程失败后需要上报CHR单据。<br>- “RAU(Routing Area Update)”：表示路由区更新流程失败后需要上报CHR单据。<br>- “SYSCHG(Inter System Change)”：表示系统切换流程失败后需要上报CHR单据。<br>- “ACTPDP(PDP Context Activation)”：表示激活流程失败后需要上报CHR单据。<br>- “DEACTPDP(PDP Context Deactivation)”：表示去激活流程失败后需要上报CHR单据。<br>- “MODPDP(PDP Context Modification)”：表示PDP修改流程失败后需要上报CHR单据。<br>- “PAGING(Paging)”：表示寻呼流程失败后需要上报CHR单据。<br>- “SUSPEND(Suspend)”：表示挂起流程失败后需要上报CHR单据。<br>- “CANCELLOC(Cancel Location)”：表示位置取消流程失败后需要上报CHR单据。<br>- “OTHER(Other Procedure)”：表示其它流程失败后需要上报CHR单据。<br>- “RESERVED1(RESERVED1)”<br>- “RESERVED2(RESERVED2)”<br>- “RESERVED3(RESERVED3)”<br>- “RESERVED4(RESERVED4)”<br>- “RESERVED5(RESERVED5)”<br>- “RESERVED6(RESERVED6)”<br>- “RESERVED7(RESERVED7)”<br>- “RESERVED8(RESERVED8)”<br>- “RESERVED9(RESERVED9)”<br>- “RESERVED10(RESERVED10)”<br>- “RESERVED11(RESERVED11)”<br>- “RESERVED12(RESERVED12)”<br>- “RESERVED13(RESERVED13)”<br>- “RESERVED14(RESERVED14)”<br>- “RESERVED15(RESERVED15)”<br>系统初始设置值：<br>“全部选中”<br>。<br>配置原则：勾选的流程失败后将上报CHR单据，未勾选的流程失败后将不上报CHR单据。 |
| UTRANSUCC | Iu模式流程成功时上报选项 | 可选必选说明：可选参数<br>参数含义：用于控制在Iu模式流程成功时，勾选流程上报CHR单据。<br>数据来源：本端规划<br>取值范围：<br>- “ATTACH(Attach)”：表示附着流程成功后需要上报CHR单据。<br>- “DETACH(Detach)”：表示分离流程成功后需要上报CHR单据。<br>- “RAU(Routing Area Update)”：表示路由区更新流程成功后需要上报CHR单据。<br>- “RELOC(SRNS Relocation)”：表示重定位流程成功后需要上报CHR单据。<br>- “SYSCHG(Inter System Change)”：表示系统切换流程成功后需要上报CHR单据。<br>- “IURLS(IU Release)”：表示在IU连接释放流程成功后需要上报CHR单据。<br>- “SVR(Service Request)”：表示在服务请求流程成功后需要上报CHR单据。<br>- “ACTPDP(PDP Context Activation)”：表示激活流程成功后需要上报CHR单据。<br>- “DEACTPDP(PDP Context Deactivation)”：表示去激活流程成功后需要上报CHR单据。<br>- “MODPDP(PDP Context Modification)”：表示PDP修改流程成功后需要上报CHR单据。<br>- “PAGING(Paging)”：表示寻呼流程成功后需要上报CHR单据。<br>- “RAB_ASSIGN(RAB Assignment in Service Request)”：表示“Service Request”中的RAB指派流程成功后需要上报CHR单据。<br>- “SUSPEND(Suspend)”：表示挂起流程成功后需要上报CHR单据。<br>- “LOCREPORT(Location Report)”：表示位置上报流程成功后需要上报CHR单据。<br>- “CANCELLOC(Cancel Location)”：表示位置取消流程成功后需要上报CHR单据。<br>- “OTHER(Other Procedure)”：表示其它流程成功后需要上报CHR单据。<br>- “RESERVED1(RESERVED1)”<br>- “RESERVED2(RESERVED2)”<br>- “RESERVED3(RESERVED3)”<br>- “RESERVED4(RESERVED4)”<br>- “RESERVED5(RESERVED5)”<br>- “RESERVED6(RESERVED6)”<br>- “RESERVED7(RESERVED7)”<br>- “RESERVED8(RESERVED8)”<br>- “RESERVED9(RESERVED9)”<br>- “RESERVED10(RESERVED10)”<br>- “RESERVED11(RESERVED11)”<br>- “RESERVED12(RESERVED12)”<br>- “RESERVED13(RESERVED13)”<br>- “RESERVED14(RESERVED14)”<br>系统初始设置值：<br>“全部清空”<br>。<br>配置原则：勾选的流程成功后将上报CHR单据，未勾选的流程成功后将不上报CHR单据。 |
| UTRANFAIL | Iu模式流程失败时上报选项 | 可选必选说明：可选参数<br>参数含义：用来控制Iu模式流程失败时，勾选流程上报CHR单据。<br>数据来源：本端规划<br>取值范围：<br>- “ATTACH(Attach)”：表示附着流程失败后需要上报CHR单据。<br>- “DETACH(Detach)”：表示分离流程失败后需要上报CHR单据。<br>- “RAU(Routing Area Update)”：表示路由区更新流程失败后需要上报CHR单据。<br>- “RELOC(SRNS Relocation)”：表示重定位流程失败后需要上报CHR单据。<br>- “SYSCHG(Inter System Change)”：表示系统切换流程失败后需要上报CHR单据。<br>- “IURLS(IU Release)”：表示在IU连接释放流程失败后需要上报CHR单据。<br>- “SVR(Service Request)”：表示在服务请求流程失败后需要上报CHR单据。<br>- “ACTPDP(PDP Context Activation)”：表示激活流程失败后需要上报CHR单据。<br>- “DEACTPDP(PDP Context Deactivation)”：表示去激活流程失败后需要上报CHR单据。<br>- “MODPDP(PDP Context Modification)”：表示PDP修改流程失败后需要上报CHR单据。<br>- “PAGING(Paging)”：表示寻呼流程失败后需要上报CHR单据。<br>- “RAB_ASSIGN(RAB Assignment in Service Request)”：表示“Service Request”中的RAB指派流程失败后需要上报CHR单据。<br>- “SUSPEND(Suspend)”：表示挂起流程失败后需要上报CHR单据。<br>- “LOCREPORT(Location Report)”：表示位置上报流程失败后需要上报CHR单据。<br>- “CANCELLOC(Cancel Location)”：表示位置取消流程失败后需要上报CHR单据。<br>- “OTHER(Other Procedure)”：表示其它流程失败后需要上报CHR单据。<br>- “RESERVED1(RESERVED1)”<br>- “RESERVED2(RESERVED2)”<br>- “RESERVED3(RESERVED3)”<br>- “RESERVED4(RESERVED4)”<br>- “RESERVED5(RESERVED5)”<br>- “RESERVED6(RESERVED6)”<br>- “RESERVED7(RESERVED7)”<br>- “RESERVED8(RESERVED8)”<br>- “RESERVED9(RESERVED9)”<br>- “RESERVED10(RESERVED10)”<br>- “RESERVED11(RESERVED11)”<br>- “RESERVED12(RESERVED12)”<br>- “RESERVED13(RESERVED13)”<br>- “RESERVED14(RESERVED14)”<br>系统初始设置值：<br>“全部选中”<br>。<br>配置原则：勾选的流程失败后将上报CHR单据，未勾选的流程失败后将不上报CHR单据。 |
| EPSSUCC | S1模式流程成功时上报选项 | 可选必选说明：可选参数<br>参数含义：用于控制在S1模式流程成功时，勾选流程上报CHR单据。<br>数据来源：本端规划<br>取值范围：<br>- “OTHER(Other Procedure)”：表示其它流程成功后需要上报CHR单据。<br>- “ATTACH(Attach)”：表示附着流程成功后需要上报CHR单据。<br>- “DETACH(Detach)”：表示分离流程成功后需要上报CHR单据。<br>- “TAU(Tracking Area Update)”：表示跟踪区域更新流程成功后需要上报CHR单据。<br>- “SYSCHG(Inter System Change)”：表示系统切换流程成功后需要上报CHR单据。<br>- “S1HO（S1 Handover）”：表示基于S1口的Handover流程成功后需要上报CHR单据。<br>- “X2HO（X2 Handover）”：表示基于X2口的Handover流程成功后需要上报CHR单据。<br>- “SVR(Service Request)”：表示在服务请求流程成功后需要上报CHR单据。<br>- “PAGING（Paging）”：表示寻呼流程成功后需要上报CHR单据。<br>- “S1RLS（S1 Release）”：表示S1口连接释放流程成功后需要上报CHR单据。<br>- “PDNCON(UE Requested PDN Connectivity)”：表示UE发起的PDN连接流程成功后需要上报CHR单据。<br>- “PDNDISCON(UE or MME Requested PDN Disconnection)”：表示UE或MME发起的PDN断开流程成功后需要上报CHR单据。<br>- “CRTBR(Dedicated Bearer Activation)”：表示承载激活流程成功后需要上报CHR单据。<br>- “MODBR(Bearer Modification)”：表示承载修改流程成功后需要上报CHR单据。<br>- “DELBR(Dedicated Bearer Deactivation)”：表示承载去激活流程成功后需要上报CHR单据。<br>- “SGSPAGING(SGS Paging)”：表示SGs Paging流程成功后需要上报CHR单据。<br>- “SRVCC(SRVCC)”：表示SRVCC流程成功后需要上报CHR单据。<br>- “LOCREPORT(Location Report)”：表示位置上报流程成功后需要上报CHR单据。<br>- “CPSVR(Control Plane Service Request)”：表示Control Plane Service Request流程成功后需要上报CHR单据。<br>- “PGWPDNDISCON(P-GW-initiated PDN Disconnect)”：表示P-GW发起的PDN断连流程成功后需要上报CHR单据。<br>- “CONSUSPEND(Connection Suspend)”：表示Connection Suspend流程成功后需要上报CHR单据。<br>- “CONRESUME(Connection Resume)”：表示Connection Resume流程成功后需要上报CHR单据。<br>- “REROUTENAS(Reroute NAS)”：表示Reroute NAS流程成功后需要上报CHR单据。<br>- “ERABMODIND(E-RAB Modification Indication)”：表示E-RAB Modification Indication流程成功后需要上报CHR单据。<br>- “CANCELLOC(Cancel Location)”：表示位置取消流程成功后需要上报CHR单据。<br>- “RESERVED1(RESERVED1)”：表示CP Relocation流程成功后需要上报CHR单据。<br>- “RESERVED2(RESERVED2)”<br>- “RESERVED3(RESERVED3)”<br>- “RESERVED4(RESERVED4)”<br>- “RESERVED5(RESERVED5)”<br>- “RESERVED6(RESERVED6)”<br>系统初始设置值：<br>“全部清空”<br>。<br>配置原则：勾选的流程成功后将上报CHR单据，未勾选的流程成功后将不上报CHR单据。 |
| EPSFAIL | S1模式流程失败时上报选项 | 可选必选说明：可选参数<br>参数含义：用于控制在S1模式流程失败时，勾选流程上报CHR单据。<br>数据来源：本端规划<br>取值范围：<br>- “OTHER(Other Procedure)”：表示其它流程失败后需要上报CHR单据。<br>- “ATTACH(Attach)”：表示附着流程失败后需要上报CHR单据。<br>- “DETACH(Detach)”：表示分离流程失败后需要上报CHR单据。<br>- “TAU(Tracking Area Update)”：表示跟踪区域更新流程失败后需要上报CHR单据。<br>- “SYSCHG(Inter System Change)”：表示系统切换流程失败后需要上报CHR单据。<br>- “S1HO（S1 Handover）”：表示基于S1口的Handover流程失败后需要上报CHR单据。<br>- “X2HO（X2 Handover）”：表示基于X2口的Handover流程失败后需要上报CHR单据。<br>- “SVR(Service Request)”：表示在服务请求流程失败后需要上报CHR单据。<br>- “PAGING（Paging）”：表示寻呼流程失败后需要上报CHR单据。<br>- “S1RLS（S1 Release）”：表示S1口连接释放流程失败后需要上报CHR单据。<br>- “PDNCON(UE Requested PDN Connectivity)”：表示UE发起的PDN连接流程失败后需要上报CHR单据。<br>- “PDNDISCON(UE or MME Requested PDN Disconnection)”：表示UE或MME发起的PDN断开流程失败后需要上报CHR单据。<br>- “CRTBR(Dedicated Bearer Activation)”：表示承载激活流程失败后需要上报CHR单据。<br>- “MODBR(Bearer Modification)”：表示承载修改流程失败后需要上报CHR单据。<br>- “DELBR(Dedicated Bearer Deactivation)”：表示承载去激活流程失败后需要上报CHR单据。<br>- “SGSPAGING(SGS Paging)”：表示SGs Paging流程失败后需要上报CHR单据。<br>- “SRVCC(SRVCC)”：表示SRVCC流程失败后需要上报CHR单据。<br>- “LOCREPORT(Location Report)”：表示位置上报流程失败后需要上报CHR单据。<br>- “CPSVR(Control Plane Service Request)”：表示Control Plane Service Request流程失败后需要上报CHR单据。<br>- “PGWPDNDISCON(P-GW-initiated PDN Disconnect)”：表示P-GW发起的PDN断连流程失败后需要上报CHR单据。<br>- “VOLTEABNORMAL(VoLTE Bearer Deleted Unexpectedly)”：表示IMS域语音承载或视频承载被异常删除后需要上报CHR单据。<br>- “CONSUSPEND(Connection Suspend)”：表示Connection Suspend流程失败后需要上报CHR单据。<br>- “CONRESUME(Connection Resume)”：表示Connection Resume流程失败后需要上报CHR单据。<br>- “REROUTENAS(Reroute NAS)”：表示Reroute NAS流程失败后需要上报CHR单据。<br>- “ERABMODIND(E-RAB Modification Indication)”：表示E-RAB Modification Indication流程失败后需要上报CHR单据。<br>- “CANCELLOC(Cancel Location)”：表示位置取消流程失败后需要上报CHR单据。<br>- “RESERVED1(RESERVED1)”：表示CP Relocation流程失败后需要上报CHR单据。<br>- “RESERVED2(RESERVED2)”<br>- “RESERVED3(RESERVED3)”<br>- “RESERVED4(RESERVED4)”<br>- “RESERVED5(RESERVED5)”<br>- “RESERVED6(RESERVED6)”<br>系统初始设置值：<br>“全部选中”<br>。<br>配置原则：勾选的流程失败后将上报CHR单据，未勾选的流程失败后将不上报CHR单据。 |
| COLLISION | 冲突流程时上报选项 | 可选必选说明：可选参数<br>参数含义：用于控制用户流程发生冲突时，哪些用户需要上报CHR单据。勾选的用户发生流程冲突后将上报CHR单据，未勾选的用户发生流程冲突后将不上报CHR单据<br>数据来源：全网规划<br>取值范围：<br>- “ACCESSTYPE_LTE(LTE(4G)接入用户)”:表示LTE(4G)接入用户的冲突流程需要上报CHR单据。<br>- “ACCESSTYPE_NBIOT(NBIOT接入用户)”：表示NB-IoT接入用户的冲突流程需要上报CHR单据。<br>- “RESERVED1(RESERVED1)”<br>- “RESERVED2(RESERVED2)”<br>- “RESERVED3(RESERVED3)”<br>- “RESERVED4(RESERVED4)”<br>- “RESERVED5(RESERVED5)”<br>- “RESERVED6(RESERVED6)”<br>系统初始设置值：<br>“全部清空”<br>配置原则：不上报用户冲突流程CHR单据时，建议所有选项均不选择。 |
| ADDITION | 附加流程上报选项 | 可选必选说明：可选参数<br>参数含义：用于控制用户发生勾选的附加流程时，上报CHR单据。<br>数据来源：全网规划<br>取值范围：<br>- “UERADIOCAP(UE无线能力)”:表示LTE(4G)接入用户在UE CAPABILITY INFO INDICATION消息中携带UE Radio Capability时需要上报CHR单据。<br>- “RESERVED1(RESERVED1)”<br>- “RESERVED2(RESERVED2)”<br>- “RESERVED3(RESERVED3)”<br>- “RESERVED4(RESERVED4)”<br>- “RESERVED5(RESERVED5)”<br>- “RESERVED6(RESERVED6)”<br>- “RESERVED7(RESERVED7)”<br>系统初始设置值：<br>“全部清空”<br>说明：- 若UNC为25.1.0.25及之后的版本，确保软参BYTE_EX_B152 BIT5设置为“0”，“UERADIOCAP(UE无线能力)”的CHR上报内容长度最长512字节。或者确保不使用本参数。<br>- 若UNC为25.1.0.25之前的版本，请确保不使用本参数。 |
| RPTDEVNO | CHR单据设备号填充方式 | 可选必选说明：可选参数<br>参数含义：用于设置CHR单据的设备号字段的填充方式。<br>数据来源：本端规划<br>取值范围：<br>- “SGSN_NUMBER（SGSN号）”<br>- “MMEID（MMEID）”<br>系统初始设置值：<br>“SGSN_NUMBER（SGSN号）”<br>。<br>配置原则：<br>- UNC作为独立SGSN网元时，该参数应配置为“SGSN_NUMBER（SGSN号）”，此时UNC使用通过[**ADD SCCPOPC**](../../../信令传输管理/SCCP管理/SCCP本局信令点/增加SCCP本局信令点(ADD SCCPOPC)_72226009.md)命令配置的“本局SGSN号”作为网元设备号码来填充CHR单据。<br>- UNC作为独立MME网元时，参数应配置为“MMEID（MMEID）”，此时UNC使用通过**[ADD MMEID](../../../网络管理/MME POOL区管理/MMEID管理/增加MMEID配置(ADD MMEID)_26146088.md)**命令配置的MMEID作为网元设备号码来填充CHR单据。<br>- UNC作为融合（SGSN+MME）的场景中，参数与CloudUDN侧的配置保持一致即可。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHRCFG]] · CHR配置（CHRCFG）

## 使用实例

设置在S1模式下，只上报所有失败流程，不上报成功流程，并且CHR单据设备号字段以SGSN号为填充方式时，可以执行如下命令：

SET CHRCFG: EPSSUCC=ATTACH-0&CANCELLOC-0&CONRESUME-0&CONSUSPEND-0&CPSVR-0&CRTBR-0&DELBR-0&DETACH-0&ERABMODIND-0&LOCREPORT-0&MODBR-0&OTHER-0&PAGING-0&PDNCON-0&PDNDISCON-0&PGWPDNDISCON-0&REROUTENAS-0&RESERVED1-0&RESERVED2-0&RESERVED3-0&RESERVED4-0&RESERVED5-0&RESERVED6-0&S1HO-0&S1RLS-0&SGSPAGING-0&SRVCC-0&SVR-0&SYSCHG-0&TAU-0&X2HO-0, EPSFAIL=ATTACH-1&CANCELLOC-1&CONRESUME-1&CONSUSPEND-1&CPSVR-1&CRTBR-1&DELBR-1&DETACH-1&ERABMODIND-1&LOCREPORT-1&MODBR-1&OTHER-1&PAGING-1&PDNCON-1&PDNDISCON-1&PGWPDNDISCON-1&REROUTENAS-1&RESERVED1-1&RESERVED2-1&RESERVED3-1&RESERVED4-1&RESERVED5-1&RESERVED6-1&S1HO-1&S1RLS-1&SGSPAGING-1&SRVCC-1&SVR-1&SYSCHG-1&TAU-1&VOLTEABNORMAL-1&X2HO-1, RPTDEVNO=SGSN_NUMBER;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CHRCFG.md`
