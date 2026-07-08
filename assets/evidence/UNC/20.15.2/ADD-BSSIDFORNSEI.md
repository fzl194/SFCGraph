# 增加NSEI和BSSID值的对应关系(ADD BSSIDFORNSEI)

- [命令功能](#ZH-CN_MMLREF_0000001172345595__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345595__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345595__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345595__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345595__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345595__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345595)

**适用网元：SGSN**

此命令用于增加一个或一组NSEI和BSSID值的对应关系来指定BSSID的值。只适用于Gb over IP自动配置的场景。

如果自动上报的NSE在本命令中NSE的范围内不能查找到，该NSE对应BSSID的值则参照 [**LST BSSGP**](../../BSSGP参数/查询BSSGP参数(LST BSSGP)_26145988.md) 命令中的 “BSSID与NSEI的对应关系” 来指定。

#### [注意事项](#ZH-CN_MMLREF_0000001172345595)

- 此命令执行后立即生效。
- 此命令最大记录数为8192。
- 此命令仅影响小部分话统，影响5个性能测量对象对应的性能测试指标，分别是“指定BSS附着”、“指定BSS SGSN内路由更新”、“指定BSS SGSN间路由更新”、“指定BSS无线资源”、“指定BSS GB接口流量”。
- 若参数BSSIDRULE为空则填充默认值（NSEI）。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345595)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345595)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345595)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSEI | 起始NSE标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待增加NSEI和BSSID值对应关系的网络服务实体起始标识。<br>数据来源：整网规划<br>取值范围：0～65535<br>默认值：无 |
| NSEIEND | 结束NSE标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待增加NSEI和BSSID值对应关系的网络服务实体结束标识。<br>“结束NSE标识”<br>必须大于等于<br>“起始NSE标识”<br>。<br>数据来源：整网规划<br>取值范围：0～65535<br>默认值：无<br>说明：本参数可选。如果只配置了“起始NSE标识”或“起始NSE标识”与“结束NSE标识”相等，则本记录只针对单个NSE生效。 |
| BSSIDRULE | BSSID与NSEI的对应关系 | 可选必选说明：可选参数<br>参数含义：该参数用于指定自动上报NSE的BSSID与NSEI的对应关系。<br>数据来源：整网规划<br>取值范围：<br>- “NSEI(NSEI)”：BSSID值与NSEI值相同。<br>- “NSEI_EXCLUDE_LAST_DIGIT(NSEI去掉最后1位)”：BSSID值为NSEI值去掉最后1位。<br>- “NSEI_EXCLUDE_LAST_2_DIGITS(NSEI去掉最后2位)”：BSSID值为NSEI值去掉最后2位。<br>- “NSEI_EXCLUDE_LAST_3_DIGITS(NSEI去掉最后3位)”：BSSID值为NSEI值去掉最后3位。<br>- “NSEI_EXCLUDE_FIRST_DIGIT(NSEI去掉前1位)”：BSSID值为NSEI值去掉前1位。<br>- “NSEI_EXCLUDE_FIRST_2_DIGITS(NSEI去掉前2位)”：BSSID值为NSEI值去掉前2位。<br>- “NSEI_EXCLUDE_FIRST_3_DIGITS(NSEI去掉前3位)”：BSSID值为NSEI值去掉前3位。<br>- “NSEI_MAP_SPECIFIC_BSSID(指定BSSID)”：BSSID值由“BSS标识”指定。<br>默认值：<br>NSEI<br>配置原则：<br>- 当无线侧不同厂商的设备，对核心网侧的BSSID值有要求时，根据NSE范围进行配置和关联。<br>- 建议使用默认值。<br>说明：当配置“起始NSE标识”为65535，“BSSID与NSEI的对应关系”为“NSEI(NSEI)”时，由于“BSS标识”的取值范围为0～65534，BSSID值为65534。 |
| BSSID | BSS标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待增加NSEI和BSSID值对应关系的BSS标识。<br>前提条件：该参数在<br>“BSSID与NSEI的对应关系”<br>为<br>“NSEI_MAP_SPECIFIC_BSSID(指定BSSID)”<br>时配置<br>数据来源：整网规划<br>取值范围：0～65534<br>默认值：无<br>说明：一个BSS标识可以对应多个NSE标识。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345595)

增加一组NSEI和BSSID值的对应关系， “起始NSE标识 ” 为 “0” ， “结束NSE标识 ” 为 “5” ， “BSSID与NSEI的对应关系 ” 为 “NSEI_MAP_SPECIFIC_BSSID(指定BSSID)” ， “BSS标识” 为 “1” ：

ADD BSSIDFORNSEI: NSEI=0, NSEIEND=5, BSSIDRULE=NSEI_MAP_SPECIFIC_BSSID, BSSID=1;
