---
id: UNC@20.15.2@MMLCommand@ADD PROCLMTPLCY
type: MMLCommand
name: ADD PROCLMTPLCY（增加流程限制策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PROCLMTPLCY
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 2048
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 流程限制管理
status: active
---

# ADD PROCLMTPLCY（增加流程限制策略）

## 功能

**适用网元：SGSN、MME**

该命令用于增加流程限制策略。为特定用户设置流程限制策略后，系统将会拒绝此类用户执行对应流程。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为2048条。
- 执行该命令后，设置的相关业务流程会被限制而失败，同时影响对应流程的性能指标统计。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- ALL_USER（所有用户）：表示用户范围为系统内所有用户。<br>- HOME_USER（本网用户）：表示用户范围为本网用户。<br>- FOREIGN_USER（外网用户）：表示用户范围为外网用户。<br>- IMSI_PREFIX（指定IMSI前缀）：表示用户范围通过IMSI前缀指定。<br>默认值：无<br>配置原则：<br>- 策略匹配优先级高到低为：“IMSI_PREFIX（指定IMSI前缀）”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”， “ALL_USER(所有用户)”。<br>- 系统优先查找高优先级的配置记录，如果查找不到，再查找低优先级的配置记录。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“HOME_USER(本网用户)”<br>或<br>“FOREIGN_USER(外网用户)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在"用户范围"参数配置为"指定IMSI前缀"后生效。<br>数据来源：整网规划<br>取值范围：5～15位十进制字符串<br>默认值：无<br>说明：- 按照IMSI最长匹配进行查询，相同IMSI前缀只能配置一条记录。<br>- IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |
| SRVCC | 限制SRVCC流程 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否限制SRVCC流程。<br>数据来源：整网规划<br>取值范围：<br>- NO(否)<br>- YES(是)<br>默认值：NO(否)<br>配置原则：当期望指定用户的SRVCC流程需要被限制时，将该参数设置为<br>“YES(是)”<br>。 |
| EMGCSRVCC | 限制紧急SRVCC流程 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定是否限制紧急SRVCC流程。<br>前提条件：该参数在<br>“限制SRVCC流程”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- NO(否)<br>- YES(是)<br>默认值：NO(否)<br>配置原则：当期望指定用户的紧急SRVCC流程也需要被限制时，将该参数设置为<br>“YES(是)”<br>。 |
| SRVCCCAUSE | SRVCC失败原因值 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定拒绝SRVCC流程时，MME向eNodeB发送Handover Preparation Failure消息中携带的原因值。<br>前提条件：该参数在<br>“限制SRVCC流程”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- CUSTOMER_DEFINED(自定义)<br>- HO_TARGET_NOT_ALLOWED(Handover Target not allowed)<br>默认值：HO_TARGET_NOT_ALLOWED(Handover Target not allowed)<br>说明：SRVCC流程失败的原因值，请参考3GPP TS 36.413进行输入。 |
| CDCAUSE | 自定义原因值 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定拒绝SRVCC流程时，MME向eNodeB发送Handover Preparation Failure消息中携带的自定义原因值。<br>前提条件：该参数在<br>“SRVCC失败原因值”<br>参数配置为<br>“ CUSTOMER_DEFINED(自定义)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～99<br>默认值：无<br>说明：当原因值为自定义时，SRVCC流程失败的原因值请参考3GPP TS 36.413进行输入。如果此参数设置的不是协议中定义的原因值，Handover Preparation Failure消息中的原因值将会被设置成Unspecified。<br>3GPP TS 36.413中定义的无线网络层原因如下：<br>- Unspecified（0）<br>- TX2RELOCOverallExpiry（1）<br>- Successful Handover（2）<br>- Release due to E-UTRAN Generated Reason（3）<br>- Handover Cancelled（4）<br>- Partial Handover（5）<br>- Handover Failure In Target EPC/eNB Or Target System（6）<br>- Handover Target not allowed（7）<br>- TS1RELOCoverallExpiry（8）<br>- TS1RELOCprepExpiry（9）<br>- Cell not available（10）<br>- Unknown Target ID（11）<br>- No Radio Resources Available in Target Cell（12）<br>- Unknown or already allocated MME UE S1AP ID（13）<br>- Unknown or already allocated eNB UE S1AP ID（14）<br>- Unknown or inconsistent pair of UE S1AP ID（15）<br>- Handover desirable for radio reasons（16）<br>- Time critical handover（17）<br>- Resource optimisation handover（18）<br>- Reduce load in serving cell（19）<br>- User inactivity（20）<br>- Radio Connection With UE Lost（21）<br>- Load Balancing TAU Required（22）<br>- CS Fallback Triggered（23）<br>- UE Not Available For PS Service（24）<br>- Radio resources not available（25）<br>- Failure in the Radio Interface Procedure（26）<br>- Invalid QoS combination（27）<br>- Inter-RAT redirection（28）<br>- Interaction with other procedure（29）<br>- Unknown E-RAB ID（30）<br>- Multiple E-RAB ID instances（31）<br>- Encryption and/or integrity protection algorithms not supported（32）<br>- S1 intra system Handover triggered（33）<br>- S1 inter system Handover triggered（34）<br>- X2 Handover triggered（35）<br>- Redirection towards 1xRTT（36）<br>- Not supported QCI value（37）<br>- invalid CSG Id（38） |
| CS | 限制CS域业务 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否限制CS域业务。<br>数据来源：整网规划<br>取值范围：<br>- NO(否)<br>- YES(是)<br>默认值：NO(否)<br>配置原则：当期望指定用户在联合附着或者联合TAU流程中限制向MSC进行注册时，将该参数设置为<br>“YES(是)”<br>。<br>说明：限制CS域业务后，MME在联合附着或者联合TAU流程中不会向MSC发送Location Update Request消息。 |
| CSCAUSE | CS域失败原因值 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定限制CS域业务时EMM CAUSE中的失败原因值。<br>前提条件：该参数在<br>“限制CS域业务”<br>参数配置为<br>“ YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- MSC_TEMPORARILY_NOT_REACHABLE(#16 MSC temporarily not reachable)<br>- CS_DOMAIN_NOT_AVAILABLE(#18 CS domain not available)<br>默认值：CS_DOMAIN_NOT_AVAILABLE(#18 CS domain not available)<br>说明：EMM CAUSE中的失败原因值，请参考3GPP TS 24.301进行输入。 |

## 操作的配置对象

- [流程限制策略（PROCLMTPLCY）](configobject/UNC/20.15.2/PROCLMTPLCY.md)

## 使用实例

增加一条流程限制策略配置， “用户范围” 为 “HOME_USER” ， “运营商标识” 为 “1” ， “限制SRVCC流程” 为 “YES(是)” ， “限制CS域业务” 为 “YES(是)” ：

ADD PROCLMTPLCY: SUBRANGE=HOME_USER, NOID=1, SRVCC=YES, CS=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加流程限制策略(ADD-PROCLMTPLCY)_72225309.md`
