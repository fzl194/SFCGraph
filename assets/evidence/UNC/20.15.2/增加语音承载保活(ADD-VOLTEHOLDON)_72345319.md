# 增加语音承载保活(ADD VOLTEHOLDON)

- [命令功能](#ZH-CN_MMLREF_0000001172345319__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345319__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345319__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345319__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345319__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345319__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345319)

**适用网元：SGSN、MME**

该命令用于增加语音承载保活策略。

#### [注意事项](#ZH-CN_MMLREF_0000001172345319)

- 此命令执行后立即生效。
- 此命令最大记录数为1024条。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345319)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345319)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345319)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- ALL_USER（所有用户）：表示用户范围为系统内所有用户。<br>- HOME_USER（本网用户）：表示用户范围为本网用户。<br>- FOREIGN_USER（外网用户）：表示用户范围为外网用户。<br>- IMSI_PREFIX（指定IMSI前缀）：表示用户范围通过IMSI前缀指定。<br>默认值：无<br>配置原则：<br>- 策略匹配优先级高到低为：“IMSI_PREFIX（指定IMSI前缀）”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”， “ALL_USER(所有用户)”。<br>- 系统优先查找高优先级的配置记录，如果查找不到，再查找低优先级的配置记录。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“HOME_USER(本网用户)”<br>或<br>“FOREIGN_USER(外网用户)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在**ADD MVNO**中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在"用户范围"参数配置为"指定IMSI前缀"后生效。<br>数据来源：整网规划<br>取值范围：5～15位十进制字符串<br>默认值：无<br>配置原则：无<br>说明：- 按照IMSI最长匹配进行查询，相同IMSI前缀只能配置一条记录。<br>- IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |
| S1RELCAUSE | S1释放原因值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置语音承载保活的原因值。<br>数据来源：整网规划<br>取值范围：<br>- TX2RELOCOVERALL-EXPIRY(TX2RELOCOVERALL-EXPIRY)<br>- EUTRAN-GENERATED-REASON(RELEASE-DUE-TO-EUTRAN-GENERATED-REASON)<br>- TS1RELOCOVERALL-EXPIRY(TS1RELOCOVERALL-EXPIRY)<br>- UE-LOST(RADIO-CONNECTION-WITH-UE-LOST)<br>- UE-NOT-AVAILABLE(UE-NOT-AVAILABLE-FOR-PS-SERVICE)<br>- FAIL-IN-RADIO-INTERFACE(FAILURE-IN-RADIO-INTERFACE-PROCEDURE)<br>- TS1RELOCPREP-EXPIRY(TS1RELOCPREP-EXPIRY)<br>- CELL-NOT-AVAILABLE(CELL-NOT-AVAILABLE)<br>- INTERACT-WITH-OTHER-PROC(INTERACTION-WITH-OTHER-PROCEDURE)<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345319)

增加一条语音承载保活配置， “用户范围” 为 “HOME_USER” ， “运营商标识” 为 “1” ：

ADD VOLTEHOLDON: SUBRANGE=HOME_USER, NOID=1;
