# 增加MVNO网络配置信息(ADD MVNONET)

- [命令功能](#ZH-CN_MMLREF_0000001172345663__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345663__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345663__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345663__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345663__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345663__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345663)

**适用网元：SGSN、MME**

此命令用于增加MVNO的网络配置。 UNC 根据MVNOMCC、MVNOMNC、MATCHIMSI这三个参数及用户的IMSI，判断用户的归属MVNO，为用户提供所属MVNO的服务。

#### [注意事项](#ZH-CN_MMLREF_0000001172345663)

- 此命令最大记录数为2048条。
- 此命令执行后立即生效。
- 若MCC相同，MNC有效长度为2和3位的MNC前两位不允许相同。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345663)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345663)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345663)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MVNOMCC | MVNO移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MVNO用户的IMSI的移动国家代码。<br>数据来源：整网规划<br>取值范围：3位十进制数字<br>默认值：无<br>配置原则：<br>“MVNO移动国家码”<br>+<br>“MVNO移动网号”<br>+<br>“ 匹配IMSI”<br>在CONNECTPLMN和本表唯一，<br>“匹配IMSI”<br>为空时，<br>“MVNO移动国家码”<br>+<br>“MVNO移动网号”<br>在HPLMN、CONNECTPLMN和本表唯一，参见<br>[**ADD HPLMN**](../../MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)<br>和<br>[**ADD CONNECTPLMN**](../../../互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md)<br>。 |
| MVNOMNC | MVNO移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MVNO用户的IMSI的移动网号。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无<br>配置原则：<br>“MVNO移动国家码”<br>+<br>“MVNO移动网号”<br>+<br>“ 匹配IMSI”<br>在CONNECTPLMN和本表唯一，<br>“匹配IMSI”<br>为空时，<br>“MVNO移动国家码”<br>+<br>“MVNO移动网号”<br>在HPLMN、CONNECTPLMN和本表唯一，参见<br>[**ADD HPLMN**](../../MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)<br>和<br>[**ADD CONNECTPLMN**](../../../互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md)<br>。 |
| MATCHIMSI | 匹配IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定MVNO用户除了MCC和MNC外的IMSI的字段。<br>数据来源：整网规划<br>取值范围：长度不超过10的十进制数字<br>默认值：无<br>配置原则：<br>- “MVNO移动国家码” + “MVNO移动网号” + “ 匹配IMSI”在HPLMN、CONNECTPLMN和本表唯一，参见[**ADD HPLMN**](../../MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)和[**ADD CONNECTPLMN**](../../../互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md)。<br>- 由于MCC + MNC + MATCHIMSI组成IMSI号段，因此，它们的长度之和不能大于IMSI的编码长度（15）。 |
| MVNOCC | MVNO 国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MVNO的国家码。<br>数据来源：整网规划<br>取值范围：长度不超过6的十进制数字<br>默认值：无<br>说明：当MVNO用户发起短消息流程时使用。 |
| MVNOID | MVNO标识 | 可选必选说明：必选参数<br>参数含义：该参数用于根据MVNO标识增加这个MVNO的网络配置。<br>前提条件：“MVNO标识”已经增加，参见<br>[**ADD MVNO**](../MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)<br>。<br>数据来源：整网规划<br>取值范围：1～64<br>默认值：无 |
| EMCBS | 是否允许紧急呼叫业务 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否允许使用紧急呼叫业务。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不允许)”<br>- “YES(允许)”<br>默认值：<br>“YES(允许)”<br>配置原则：如果不支持VOLTE紧急呼叫业务，期望在CS域做紧急呼叫时，建议配置为<br>“NO（不允许）” |
| EMGCNUMSW | 紧急号码下发开关 | 可选必选说明：可选参数<br>参数含义：该参数用来控制系统在给指定MVNO用户发送Attach Accept、TAU Accept、RAU Accept消息时，是否将紧急号码携带在消息中发送给UE。<br>数据来源：整网规划<br>取值范围：<br>- “ON(开启)”<br>- “OFF(关闭)”<br>默认值：<br>“ON(开启)”<br>配置原则：当本参数设置为<br>“ON(开启)”<br>时，系统将在Attach Accept、TAU Accept、RAU Accept消息中给指定MVNO用户发送紧急号码列表。其中，紧急号码列表来源于ADD EMGCNUM中的配置，如果ADD EMGCNUM没有配置，则不下发紧急号码。<br>说明：紧急号码下发还受其它配置（SET MMFUNC中EMNUM参数、DWORD_EX6 BIT10、DWORD_EX6 BIT11、DWORD_EX33 BIT13、DWORD_EX33 BIT12）控制，共同决策是否下发紧急号码。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345663)

增加MVNO标识为1的MVNO的网络资源：

ADD MVNONET: MVNOMCC="460", MVNOMNC="00", MATCHIMSI="111", MVNOCC="860", MVNOID=1, EMCBS=YES;
