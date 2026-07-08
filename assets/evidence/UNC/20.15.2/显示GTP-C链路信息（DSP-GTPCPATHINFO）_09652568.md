# 显示GTP-C链路信息（DSP GTPCPATHINFO）

- [命令功能](#ZH-CN_MMLREF_0209652568__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652568__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652568__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652568__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209652568__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209652568)

**适用NF：AMF、PGW-C、SGW-C、GGSN**

该命令用于查询GTP-C路径信息。

## [注意事项](#ZH-CN_MMLREF_0209652568)

- 当“接口类型”未输入时，默认查询所有接口类型的路径状态信息。
- 当“查询类型”未输入时，默认查询内存(MEMORY)中的路径状态信息。
- 当“查询类型”为“内存(MEMORY)”时，不显示“对端Recovery值”、“路径断去激活会话时间”、“对端Recovery变化去激活会话时间”信息。
- 当“路径状态筛选”未输入时，默认查询路径状态为故障(Error)的路径状态信息。
- 当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效，请使用命令DSP GTPCPATH查询。

#### [操作用户权限](#ZH-CN_MMLREF_0209652568)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652568)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTPVER | GTP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C路径的GTP版本号。<br>数据来源：全网规划<br>取值范围：<br>- GTPv1（GTPv1）<br>- GTPv2（GTPv2）<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C路径的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPTypeV4（IPv4类型）”：IPTypeV4<br>- “IPTypeV6（IPv6类型）”：IPTypeV6<br>默认值：无<br>配置原则：无 |
| LOCALIPV4 | 本端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV4"时为条件可选参数。<br>参数含义：该参数用于指定GTP-C路径的本端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>业务地址必须是A、B或者C类地址。 |
| LOCALIPV6 | 本端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV6"时为条件可选参数。<br>参数含义：该参数用于指定GTP-C路径的本端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV4"时为条件可选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>业务地址必须是A、B或者C类地址。 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV6"时为条件可选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| PATHST | 路径状态筛选 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询GTP-C路径的状态。<br>数据来源：本端规划<br>取值范围：<br>- ERROR（故障）<br>- NORMAL（正常）<br>- ALL（所有）<br>默认值：ERROR<br>配置原则：无 |
| QRYTP | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：本端规划<br>取值范围：<br>- MEMORY（内存）<br>- DDB（数据库）<br>默认值：MEMORY<br>配置原则：无 |
| INTERFACETYPEIN | 接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GTP-C路径的接口类型。<br>数据来源：本端规划<br>取值范围：<br>- Unknow（未知接口）<br>- Gn（Gn接口）<br>- Gp（Gp接口）<br>- S5（S5接口）<br>- S8（S8接口）<br>- S11（S11接口）<br>- N26（N26接口）<br>- S4（S4接口）<br>- All（All）<br>- Proxy（Proxy接口）<br>默认值：All<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652568)

查询本端IP地址为10.1.12.3，对端IP地址为10.2.20.1，GTP版本号为GTPv2的GTP-C路径信息：DSP GTPCPATHINFO: GTPVER=GTPv2, IPTYPE=IPTypeV4, LOCALIPV4="10.1.12.3", PEERIPV4="10.2.20.1", PATHST=ALL;

```
%%DSP GTPCPATHINFO: GTPVER=GTPv2, IPTYPE=IPTypeV4, LOCALIPV4="10.1.12.3", PEERIPV4="10.2.20.1", PATHST=ALL;%%
RETCODE = 0  操作成功

结果如下
------------------------
   IP地址类型  =  IPTypeV4
 本端IPv4地址  =  10.1.12.3
 对端IPv4地址  =  10.2.20.1
      GTP版本  =  GTPv2
     路径状态  =  Normal
     接口类型  =  S5接口
      POD名称  =  uncpod-0
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209652568)

| 输出项名称 | 输出项解释 |
| --- | --- |
| IP地址类型 | 该参数用于指定GTP-C路径的IP地址类型。<br>取值说明：<br>- “IPTypeV4（IPv4类型）”：IPTypeV4<br>- “IPTypeV6（IPv6类型）”：IPTypeV6 |
| 本端IPv6地址 | 该参数用于指定GTP-C路径的本端IPv6地址。 |
| 对端IPv6地址 | 该参数用于指定GTP-C路径的对端IPv6地址。 |
| GTP版本 | 该参数用于指定GTP-C路径的GTP版本号。<br>取值说明：<br>- GTPv1（GTPv1）<br>- GTPv2（GTPv2） |
| 路径状态 | 该参数用于指定GTP-C路径的路径状态。<br>取值说明：<br>- Normal（Normal）<br>- Error（Error）<br>- Idle（Idle） |
| 接口类型 | 该参数用于指定GTP-C路径的接口类型。<br>取值说明：<br>- Unknow（未知接口）<br>- Gn（Gn接口）<br>- Gp（Gp接口）<br>- S5（S5接口）<br>- S8（S8接口）<br>- S11（S11接口）<br>- N26（N26接口）<br>- S4（S4接口）<br>- All（All）<br>- Proxy（Proxy接口） |
| 路径断去激活会话时间 | 该参数用于指定当GTP-C路径持续故障后，使用该GTP-C路径在该时间之前接入的会话会被去激活。 |
| 对端Recovery变化去激活会话时间 | 该参数用于指定当对端Recovery变化后，在该时间之前和对端创建的会话会被去激活。 |
| 对端Recovery值 | 该参数用于指定该GTP-C路径指示的对端网元的Recovery值。 |
| Prn标志 | 该参数用于指定该GTP-C路径指示的对端网元是否支持PRN功能。<br>取值说明：<br>- Enable（Enable）<br>- Disable（Disable） |
| Ntsr标志 | 该参数用于指定该GTP-C路径指示的对端网元是否支持NTSR功能。<br>取值说明：<br>- Enable（Enable）<br>- Disable（Disable） |
| 本端IPv4地址 | 该参数用于指定GTP-C路径的本端IPv4地址。 |
| 对端IPv4地址 | 该参数用于指定GTP-C路径的对端IPv4地址。 |
| ASN查询状态 | 该参数用于指定查询ASN的状态。<br>取值说明：<br>- STATE_NULL（初始状态）<br>- STATE_NORMAL（成功获取ASN）<br>- STATE_SENDING（正在获取ASN）<br>- STATE_NOT_RESPOND（获取ASN响应超时）<br>- STATE_INVALID（获取到的ASN无效） |
| ASN值 | 该参数用于表示该路径使用的ASN值。 |
| POD名称 | 该参数用于显示POD名称。 |
