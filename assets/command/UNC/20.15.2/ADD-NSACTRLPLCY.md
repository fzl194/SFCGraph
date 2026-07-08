---
id: UNC@20.15.2@MMLCommand@ADD NSACTRLPLCY
type: MMLCommand
name: ADD NSACTRLPLCY（增加NSA控制策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NSACTRLPLCY
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- NSA组网管理
- NSA控制策略
status: active
---

# ADD NSACTRLPLCY（增加NSA控制策略）

## 功能

**适用网元：MME**

该命令用于在NSA组网时，为不同的用户配置NSA控制策略。

## 注意事项

- 该命令执行后只对新接入用户生效。
- 最大配置记录数是1024条。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

## 权限

manage-ug；system-ug；
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置NSA控制策略的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- ALL_USER（所有用户）：表示用户范围为系统内所有用户。<br>- HOME_USER（本网用户）：表示用户范围为本网用户。<br>- FOREIGN_USER（外网用户）：表示用户范围为外网用户。<br>- IMSI_PREFIX（指定IMSI前缀）：表示用户范围通过IMSI前缀指定。<br>默认值：无<br>配置原则：<br>- NSA控制策略优先级高到低为：“IMSIPRE(IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”， “ALL_USER(所有用户)”。<br>- 系统优先查找高优先级的配置记录，如果查找不到，再查找低优先级的配置记录。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“HOME_USER(本网用户)”<br>或<br>“FOREIGN_USER(外网用户)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用以指定待配置NSA控制策略用户的IMSI前缀。<br>前提条件：该参数在"用户范围"参数配置为"指定IMSI前缀"后生效。<br>数据来源：整网规划<br>取值范围：5~15十进制数字字符串<br>默认值：无 |
| ISDCNR | 是否支持DC-NR接入 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否允许具备DCNR能力的终端接入。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无 |
| ISSECRATRPTSGW | 是否在使用数据报告中置位IRSGW标志 | 可选必选说明：条件可选参数<br>参数含义：该参数用以指定向网关上报的用户使用数据报告中IRSGW标志是否置位。使用数据报告（Secondary RAT Usage Data Report）中包含了用户在NR接入方式下的使用流量统计及IRSGW、IRPGW标志，其中IRSGW标志用以标识S-GW接收到使用数据报告后是否需要处理。<br>前提条件：该参数在<br>“是否支持DC-NR接入”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“YES（是）”<br>配置原则：如果运营商希望S-GW只针对指定PLMN的用户接收或者不接收使用流量报告，以控制话单生成或其它用途，可以通过本开关进行设置。<br>说明：需要将命令<br>[**SET NSACTRL**](../NSA控制参数/设置NSA控制参数(SET NSACTRL)_26305942.md)<br>的参数<br>“NR流量上报”<br>设置为<br>“YES（是）”<br>后，该参数才能生效。 |
| ISSECRATRPT | 是否在使用数据报告中置位IRPGW标志 | 可选必选说明：条件可选参数<br>参数含义：该参数用以指定向网关上报的用户使用数据报告中IRPGW标志是否置位。使用数据报告（Secondary RAT Usage Data Report）中包含了用户在NR接入方式下的使用流量统计及IRSGW、IRPGW标志，其中IRPGW标志用以标识P-GW接收到使用数据报告后是否需要处理。<br>前提条件：该参数在<br>“是否支持DC-NR接入”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“YES（是）”<br>配置原则：如果运营商希望P-GW只针对指定PLMN的用户接收或者不接收使用流量报告，以控制话单生成或其它用途，可以通过本开关进行设置。<br>说明：需要将命令<br>[**SET NSACTRL**](../NSA控制参数/设置NSA控制参数(SET NSACTRL)_26305942.md)<br>的参数<br>“NR流量上报”<br>设置为<br>“YES（是）”<br>后，该参数才能生效。 |
| ISGUUPSEL | 是否支持GU接入选择用户面 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否为NSA用户在GU接入时选择高速网关。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“YES（是）”<br>说明：“NSA用户业务连续性保障”特性的相关License授权并开启后，此参数配置才生效（特性编号：WSFD-<br>104602<br>，License部件编码：LKV2UNCUP02）。 |
| RPTPSCELLID | 是否指示eNodeB上报PS Cell ID信息 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制NSA用户是否在Location Reporting Control消息中携带Additional Location Information信元。<br>前提条件：该参数在“是否支持DC-NR接入”参数配置为“YES(是)”后生效。<br>数据来源：全网规划<br>取值范围：<br>- "NO（否）"<br>- "YES（是）"<br>默认值："NO（否）"<br>配置原则：<br>如果希望eNodeB在Location Reporting流程上报PS Cell ID信息时，设置本参数为“YES（是）”；否则设置本参数为“NO（否）”。<br>说明：该参数打开后，如果下发给eNodeB的指示为“Change of service cell”，则PSCell ID变化也会触发Location report消息，会增加S1-MME接口、S11接口上信令数目，降低系统性能，并且频繁的位置更新上报也可能会大量增加Gx接口的信令负载，因此不能对所有用户同时开启该特性，应该区分用户进行开启。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于对配置记录的描述。<br>数据来源：整网规划<br>取值范围：0~32位字符串。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NSACTRLPLCY]] · NSA控制策略（NSACTRLPLCY）

## 使用实例

1. 增加一条：用户范围为“所有用户”，是否支持DCNR接入为“YES”，是否支持使用数据报告上报为“YES”，是否支持GU接入选择用户面为“YES”的记录
  ADD NSACTRLPLCY: SUBRANGE=ALL_USER, ISDCNR=YES, ISSECRATRPT=YES, ISGUUPSEL=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NSACTRLPLCY.md`
