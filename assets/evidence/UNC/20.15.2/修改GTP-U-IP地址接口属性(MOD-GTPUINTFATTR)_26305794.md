# 修改GTP-U IP地址接口属性(MOD GTPUINTFATTR)

- [命令功能](#ZH-CN_MMLREF_0000001126305794__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305794__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305794__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305794__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305794__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305794__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305794)

**适用网元：SGSN、MME**

该命令用于修改已存在记录的名称等维护信息。

#### [注意事项](#ZH-CN_MMLREF_0000001126305794)

- 该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305794)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305794)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305794)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MODTYPE | 修改条件 | 可选必选说明：必选参数<br>参数含义：该参数用于指定修改操作的类型。<br>数据来源：本端规划<br>取值范围：<br>- “BYINDEX(根据记录索引)”<br>- “BYINTFSUB(根据接口类型和用户范围)”<br>默认值：无 |
| INDEX | 记录索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定已存在记录的索引。<br>前提条件：该参数在<br>“修改条件”<br>参数配置为<br>“BYINDEX(根据记录索引)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0~4294967295<br>默认值：无<br>说明：使用<br>[**LST GTPUINTFATTR**](查询GTP-U IP地址接口属性(LST GTPUINTFATTR)_72345585.md)<br>查询记录的名称。 |
| SUBRANGE | 用户范围 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GTPU IP地址适用的用户范围。<br>前提条件：该参数在<br>“修改条件”<br>参数配置为<br>“YINTFSUB(根据接口类型和用户范围)”<br>B后生效。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”<br>- “SPECIAL_NOID(指定运营商)”<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户归属的运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“SPECIAL_NOID(指定运营商)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，请先在[**ADD MNO**](../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的IMSI前缀。使用时按照IMSI最长匹配进行查询。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>后生效。<br>数据来源：全网规划<br>取值范围：1~15位十进制数<br>默认值：无 |
| INTFTP1 | 接口类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GTPU IP地址适用的接口类型。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“ALL_USER(所有用户)”<br>后生效。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_INTERFACE(所有接口)”<br>- “GN-GGSN/GP(Gn-GGSN/Gp)”<br>- “GN-SGSN/S16(Gn-SGSN/S16)”<br>- “Iu(IU)”<br>- “S11(S11)”<br>- “S4(S4)”<br>默认值：无<br>说明：“GN-SGSN(Gn-SGSN)”<br>包含GnGp SGSN之间的接口以及GnGp SGSN与MME之间的接口。 |
| INTFTP2 | 接口类型2 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GTPU IP地址适用的接口类型。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“SPECIAL_NOID(指定运营商)”<br>/<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>后生效。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_INTERFACE(所有接口)”<br>- “GN-GGSN/GP(Gn-GGSN/Gp)”<br>- “S11(S11)”<br>- “S4(S4)”<br>默认值：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定描述信息。<br>数据来源：本端规划<br>取值范围：0~31位字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305794)

将修改类型为BYINDEX、INDEX为1的记录的DESC修改为"HUAWEI"。

MOD GTPUINTFATTR: MODTYPE=BYINDEX, INDEX=0, DESC="HUAWEI";
