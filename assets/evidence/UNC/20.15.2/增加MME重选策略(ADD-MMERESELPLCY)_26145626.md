# 增加MME重选策略(ADD MMERESELPLCY)

- [命令功能](#ZH-CN_MMLREF_0000001126145626__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145626__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145626__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145626__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145626__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145626__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145626)

**适用网元：MME**

该命令用于增加MME重选策略参数，即为不同范围的用户，配置进行MME重选的条件，满足重选条件用户将被重选至指定MME。

#### [注意事项](#ZH-CN_MMLREF_0000001126145626)

- 该命令执行后立即生效。
- 最大配置记录数是1024条。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145626)

manage-ug；system-ug；

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145626)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145626)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待进行网元重选的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- ALL_USER（所有用户）：表示用户范围为系统内所有用户。<br>- HOME_USER（本网用户）：表示用户范围为本网用户。<br>- FOREIGN_USER（外网用户）：表示用户范围为外网用户。<br>- IMSI_PREFIX（指定IMSI前缀）：表示用户范围通过IMSI前缀指定。<br>默认值：无<br>配置原则：MME重选策略优先级高到低为：“IMSIPRE(IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”， “ALL_USER(所有用户)”。 系统优先查找高优先级的配置记录，如果查找不到，再查找低优先级的配置记录。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“HOME_USER(本网用户)”<br>或<br>“FOREIGN_USER(外网用户)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在"用户范围"参数配置为"指定IMSI前缀"后生效。<br>数据来源：整网规划<br>取值范围：5~15十进制数字字符串<br>默认值：无 |
| RESELSW | 重选开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否开启选择功能。<br>数据来源：整网规划<br>取值范围：<br>- OFF：关闭<br>- ON：开启<br>默认值：无 |
| RESELPLCY | 重选策略 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定进行MME网元重选的方式。<br>前提条件：该参数在<br>“重选开关”<br>参数配置为<br>“ON(开启)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- REROUTE_NAS：使用“REROUTE_NAS”Request方式。<br>配置原则：<br>- 当需要通过Reroute NAS Request消息将用户新接入的Attach Request或TAU Request消息重选到目标MME时，将此参数设置为“REROUTE_NAS”。<br>默认值：无 |
| RESELCOND | 重选条件 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定进行MME网元重选时需要满足的条件。<br>前提条件：该参数在<br>“重选策略”<br>参数配置为<br>“使用Reroute NAS Request方式”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- DCNR：根据UE网络能力中的DCNR字段制定匹配条件。如果用户的UE网络能力中支持DCNR，则用户符合重选条件。<br>- DCNR_UUT_INCLUDE：根据UE网络能力中的DCNR字段和UE USAGE TYPE属于UE USAGE TYPE群组制定匹配条件。如果用户的UE网络能力中支持DCNR，并且用户的UE USAGE TYPE在所配置的UE USAGE TYPE群组范围内，则用户符合重选条件。<br>- DCNR_UUT_NOT_INCLUDE：根据UE网络能力中的DCNR字段和UE USAGE TYPE不属于UE USAGE TYPE群组制定匹配条件。如果用户的UE网络能力中不支持DCNR，或者用户的UE USAGE TYPE不在所配置的UE USAGE TYPE群组范围内，则用户符合重选条件。<br>默认值：无 |
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定UE USAGE TYPE群组标识。<br>前提条件：<br>- 该参数在“重选条件”参数配置为“DCNR_UUT_INCLUDE”后生效。<br>- 该参数在“重选条件”参数配置为“DCNR_UUT_NOT_INCLUDE”后生效。<br>数据来源：整网规划<br>取值范围：0~1023的整数类型。<br>默认值：无<br>配置原则：此参数已通过<br>[**ADD UEUSGTYPEGP**](../../../业务安全管理/DCN管理/UE USAGE TYPE群组管理/增加UE USAGE TYPE群组(ADD UEUSGTYPEGP)_72225499.md)<br>配置。 |
| TMMEGPIDX | 目标MME组索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定进行MME网元选择时的目标MME群组的标识。<br>前提条件：该参数在<br>“重选策略”<br>参数配置为<br>“使用Reroute NAS Request方式”<br>后生效。<br>数据来源：整网规划<br>取值范围：0~63的整数类型。<br>默认值：无<br>配置原则：该参数必须已经在<br>[**ADD MMEGP**](../../MME群组管理/MME群组配置/增加MME群组(ADD MMEGP)_72225301.md)<br>配置。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145626)

1. 增加一条：用户范围为“所有用户”，重选开关为“ON（开启）”，重选策略为“REROUTE_NAS(使用Reroute NAS Request方式)”，重选条件为“DCNR(根据网络能力重选NSA用户)”，目标MME组索引为“0”的记录
  ADD MMERESELPLCY: SUBRANGE=ALL_USER, RESELSW=ON, RESELPLCY=REROUTE_NAS, RESELCOND=DCNR, TMMEGPIDX=0;
