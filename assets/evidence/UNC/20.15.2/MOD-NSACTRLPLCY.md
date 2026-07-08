# 修改NSA控制策略(MOD NSACTRLPLCY)

- [命令功能](#ZH-CN_MMLREF_0000001126305940__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305940__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305940__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305940__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305940__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305940__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305940)

**适用网元：MME**

该命令用于在NSA组网时，修改用户的NSA控制策略。

#### [注意事项](#ZH-CN_MMLREF_0000001126305940)

- 该命令执行后只对新接入用户生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305940)

manage-ug；system-ug；

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305940)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305940)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用以指定配置NSA控制策略的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- ALL_USER（所有用户）：表示用户范围为系统内所有用户。<br>- HOME_USER（本网用户）：表示用户范围为本网用户。<br>- FOREIGN_USER（外网用户）：表示用户范围为外网用户。<br>- IMSI_PREFIX（指定IMSI前缀）：表示用户范围通过IMSI前缀指定。<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“HOME_USER(本网用户)”<br>或<br>“FOREIGN_USER(外网用户)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用以指定待配置NSA控制策略用户的IMSI前缀。<br>前提条件：该参数在"用户范围"参数配置为"指定IMSI前缀"后生效。<br>数据来源：整网规划<br>取值范围：5~15位十进制数字字符串<br>默认值：无 |
| ISDCNR | 是否支持DC-NR接入 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否允许用户DC-NR接入。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无 |
| ISSECRATRPTSGW | 是否在使用数据报告中置位IRSGW标志 | 可选必选说明：条件可选参数<br>参数含义：该参数用以指定向网关上报的用户使用数据报告中IRSGW标志是否置位。使用数据报告（Secondary RAT Usage Data Report）中包含了用户在NR接入方式下的使用流量统计及IRSGW、IRPGW标志，其中IRSGW标志用以标识S-GW接收到使用数据报告后是否需要处理。<br>前提条件：该参数在<br>“是否支持DC-NR接入”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无 |
| ISSECRATRPT | 是否在使用数据报告中置位IRPGW标志 | 可选必选说明：条件可选参数<br>参数含义：该参数用以指定向网关上报的用户使用数据报告中IRPGW标志是否置位。使用数据报告（Secondary RAT Usage Data Report）中包含了用户在NR接入方式下的使用流量统计及IRSGW、IRPGW标志，其中IRPGW标志用以标识P-GW接收到使用数据报告后是否需要处理。<br>前提条件：该参数在<br>“是否支持DC-NR接入”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无 |
| ISGUUPSEL | 是否支持GU接入选择用户面 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否为NSA用户在GU接入时选择高速网关。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无<br>说明：“NSA用户业务连续性保障”特性的相关License授权并开启后，此参数配置才生效（特性编号：WSFD-<br>104602<br>，License部件编码：LKV2UNCUP02）。 |
| RPTPSCELLID | 是否指示eNodeB上报PS Cell ID信息 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制NSA用户是否在Location Reporting Control消息中携带Additional Location Information信元。<br>前提条件：该参数在“是否支持DC-NR接入”参数配置为“YES(是)”后生效。<br>数据来源：全网规划<br>取值范围：<br>- "NO（否）"<br>- "YES（是）"<br>默认值："NO（否）"<br>配置原则：<br>如果希望eNodeB在Location Reporting流程上报PS Cell ID信息时，设置本参数为“YES（是）”；否则设置本参数为“NO（否）”。<br>说明：该参数打开后，如果下发给eNodeB的指示为“Change of service cell”，则PSCell ID变化也会触发Location report消息，会增加S1-MME接口、S11接口上信令数目，降低系统性能，并且频繁的位置更新上报也可能会大量增加Gx接口的信令负载，因此不能对所有用户同时开启该特性，应该区分用户进行开启。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于对配置记录的描述。<br>数据来源：整网规划<br>取值范围：0~32位字符串类型。<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305940)

1. 修改用户范围为“ALL_USER(所有用户)”是否支持DCNR接入为“NO”，是否支持GU接入选择用户面为“NO”的记录。
  MOD NSACTRLPLCY: SUBRANGE=ALL_USER, ISDCNR=NO, ISGUUPSEL=NO;
