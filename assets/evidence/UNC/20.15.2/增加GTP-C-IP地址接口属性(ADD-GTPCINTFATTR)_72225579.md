# 增加GTP-C IP地址接口属性(ADD GTPCINTFATTR)

- [命令功能](#ZH-CN_MMLREF_0000001172225579__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225579__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225579__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225579__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225579__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225579__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225579)

**适用网元：SGSN、MME、AMF**

该命令用于指定GTPC IP地址在指定的接口使用，或者在指定的用户范围内使用，满足不同的组网部署要求。

本命令需和 [**ADD GTPCLE**](../Gtpc本端实体管理/增加GTP-C本地实体(ADD GTPCLE)_26145966.md) 命令配合，通过 [**ADD GTPCLE**](../Gtpc本端实体管理/增加GTP-C本地实体(ADD GTPCLE)_26145966.md) 命令的组号与本命令的{接口类型+用户范围}关联起来，满足各种组网规划的应用。

应用场景举例1：Sv接口是PS域网元与CS域网元的接口，从网络安全角度考虑，组网上Sv接口划分独立的VPN，避免PS域的其他接口与CS域互通。这就要求Sv接口上使用的GTPC IP地址能够独立指定，与其他接口的GTPC IP地址分开。数据规划时，将Sv接口的GTPC IP地址规划为1号组，其他接口的GTPC IP地址规划为0号组，通过本命令指定Sv接口与1号组关联，其他接口缺省与0号组关联。

应用场景举例2：MME和SGSN融合部署时，组网上将MME的Sx接口与SGSN的GnGp接口隔离，通常划分独立的VPN，这就要求GnGp接口上使用的GTPC IP地址能够独立指定，与Sx接口的GTPC IP地址分开。数据规划时，将GnGp接口的GTPC IP地址规划为2号组，其他接口的GTPC IP地址规划为0号组，通过本命令指定GnGp接口与2号组关联，其他接口缺省与0号组关联。

#### [注意事项](#ZH-CN_MMLREF_0000001172225579)

- 该命令执行后立即生效。
- 指定IMSI前缀的记录最大支持1024。
- 指定运营商标识的记录最大支持128。
- 用户范围参数选择为所有用户时的记录数最大支持8。
- {接口类型+用户范围}唯一标识一条记录。
- 不同的{接口类型+用户范围}允许指定相同的组号。
- {“所有接口”+“所有用户”}为系统初始记录，指定ADD GTPCLE配置的0号组，不允许指定为其他组号。
- “IMSI前缀”长度不相等时，使用“IMSI前缀”最长匹配的记录。
- GTPC IP地址使用的优先级从高到低为：
- 指定接口类型+“SPECIAL_IMSIPRE（指定IMSI前缀）”。
- “ALL_INTERFACE（所有接口类型）”+“SPECIAL_IMSIPRE（指定IMSI前缀）”。
- 指定接口类型+“SPECIAL_NOID（指定运营商）”。
- “ALL_INTERFACE（所有接口类型）”+“SPECIAL_NOID（指定运营商）”。
- 指定接口类型+“ALL_USER（所有用户）”。
- “ALL_INTERFACE（所有接口类型）”+“ALL_USER（所有用户）”。
- 当AMF的N26接口部署模式为融合部署模式时，该命令适用于AMF。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225579)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225579)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225579)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTPC IP地址适用的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”<br>- “SPECIAL_NOID(指定运营商)”<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户归属的运营商标识。<br>前提条件：该参数在"用户范围"参数配置为"SPECIAL_NOID(指定运营商)"后生效。<br>数据来源：全网规划<br>取值范围：0~64,128~254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，请先在[**ADD MNO**](../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的IMSI前缀。使用时按照IMSI最长匹配进行查询。<br>前提条件：该参数在"用户范围"参数配置为"SPECIAL_IMSIPRE(指定IMSI前缀)"后生效。<br>数据来源：全网规划<br>取值范围：1~15位十进制数<br>默认值：无 |
| INTFTP | 接口类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GTPC IP地址适用的接口类型。<br>前提条件：该参数在"用户范围"参数配置为"ALL_USER(所有用户)"后生效。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_INTERFACE(所有接口)”<br>- “GN-GGSN/GP(Gn-GGSN/Gp)”<br>- “GN-SGSN/S16(Gn-SGSN/S16)”<br>- “S10(S10)”<br>- “S11(S11)”<br>- “S3(S3)”<br>- “S4(S4)”<br>- “SV(Sv)”<br>默认值：无<br>说明：“GN-SGSN(Gn-SGSN)”<br>包含GnGp SGSN之间的接口以及GnGp SGSN与MME之间的接口。 |
| INTFTP2 | 接口类型2 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GTPC IP地址适用的接口类型。<br>前提条件：<br>- 该参数在"用户范围"参数配置为"SPECIAL_NOID(指定运营商)"后生效。<br>- 该参数在"用户范围"参数配置为"SPECIAL_IMSIPRE(指定IMSI前缀)"后生效。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_INTERFACE(所有接口)”<br>- “GN-GGSN/GP(Gn-GGSN/Gp)”<br>- “S11(S11)”<br>- “S4(S4)”<br>默认值：无 |
| GRPID | 组号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTPC IP所属的组。<br>数据来源：本端规划<br>取值范围：1~32<br>默认值：无<br>配置原则：请先在<br>[**ADD GTPCLE**](../Gtpc本端实体管理/增加GTP-C本地实体(ADD GTPCLE)_26145966.md)<br>中配置取值相同的“组号”参数。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定描述信息。<br>数据来源：本端规划<br>取值范围：0~31位字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225579)

增加记录，配置SUBRANGE为ALL_USER、INTFTP为SV、GRPID为1、DESC为"huawei"的记录：

ADD GTPCINTFATTR: SUBRANGE=ALL_USER,INTFTP=SV,GRPID=1,DESC="huawei";
