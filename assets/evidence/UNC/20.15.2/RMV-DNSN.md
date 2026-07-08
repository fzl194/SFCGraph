# 删除DNS NAPTR记录(RMV DNSN)

- [命令功能](#ZH-CN_MMLREF_0000001126305700__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305700__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305700__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305700__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305700__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305700__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305700)

**适用网元：SGSN、MME**

该命令用于删除 “FQDN” （全称标准规范域名）与网元接口的对应关系。

#### [注意事项](#ZH-CN_MMLREF_0000001126305700)

- 该命令执行后立即生效。
- 删除后将影响DNS对本域名的解析。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305700)

manage-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305700)

G_1，管理员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305700)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FQDN | FQDN | 可选必选说明：必选参数<br>参数含义：该参数用于标识由RAI、TAI、APN、MME等构建的域名，用来进行网元查询。<br>数据来源：整网规划<br>取值范围：1~255位字符串<br>默认值：无<br>说明：- FQDN不能以“.”开始，也不能以“.”结束。 |
| HSINDEX | 主机名索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>“FQDN”<br>对应网元的索引。<br>取值范围：1~2048<br>默认值：无 |
| ENTITY | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定接口网元的类型。<br>数据来源：整网规划<br>取值范围：<br>- “SGSN(SGSN)”<br>- “GGSN(GGSN)”<br>- “MME(MME)”<br>- “SGW(SGW)”<br>- “PGW(PGW)”<br>- “MSC(MSC)”<br>- “IWS(IWS)”<br>- “AMF(AMF)”<br>默认值：无 |
| INTYPE | 接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用来指定接口对应的类型。<br>数据来源：整网规划<br>取值范围：<br>- “Gn(Gn)”<br>- “Gp(Gp)”<br>- “S3(S3)”<br>- “S4(S4)”<br>- “S5(S5)”<br>- “S8(S8)”<br>- “S10(S10)”<br>- “S11(S11)”<br>- “S16(S16)”<br>- “Sv(Sv)”<br>- “S102(S102)”<br>- “Sdup(Sdup)”<br>- “N26(N26)”<br>默认值：无<br>说明：- 当该配置数据用于链式备份网元寻址时，需要选Sdup枚举，Sdup接口华为私有接口，是MME和MME之间的接口，用于实现MME间的数据备份。 |
| UEUSGTYPEPLCY | UE USAGE TYPE策略 | 可选必选说明：必选参数<br>参数含义：该参数用来指定是否携带UE USAGE TYPE。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“NO（否）” |
| DCNR | 支持DCNR | 可选必选说明：必选参数<br>参数含义：该参数用于控制是否支持DCNR接入。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“NO（否）”<br>说明：该参数同<br>“FQDN”<br>、<br>“主机名索引”<br>、<br>“网元类型”<br>、<br>“接口类型”<br>、<br>“UE USAGE TYPE策略”<br>、<br>“融合PGW-C/SMF”<br>一起唯一确定一条记录。 |
| SMF | 融合PGW-C/SMF | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否支持融合的PGW-C/SMF。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“NO（否）”<br>配置原则：该参数仅在<br>“网元类型”<br>配置为<br>“PGW”<br>时，才能配置为<br>“YES”<br>。<br>说明：- 该参数同 “FQDN”、“主机名索引”、“网元类型”、“接口类型”、“UE USAGE TYPE策略”、“支持DCNR”一起唯一确定一条记录，不能修改。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305700)

删除FQDN为TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG，HSINDEX为100，网元类型为S-GW，接口类型是S11，UE USAGE TYPE策略为是的一条NAPTR记录：

RMV DNSN: FQDN="TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG", HSINDEX=100, ENTITY=SGW, INTYPE=S11, UEUSGTYPEPLCY=YES, DCNR=NO, SMF=NO;
