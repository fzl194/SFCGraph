# 增加NSE属性模板(ADD GBNSECFGPARA)

- [命令功能](#ZH-CN_MMLREF_0000001126146004__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126146004__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126146004__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126146004__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126146004__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126146004__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126146004)

**适用网元：SGSN**

某些局点可能不同NSE的属性也不相同，此命令用于增加NSE属性模板，以制定NSE的属性。只适用于Gb over IP自动配置的场景。

NSE属性匹配规则：一般是通过 [**ADD GBNSEGRP**](../NSE属性管理/增加NSE和属性模板的关联(ADD GBNSEGRP)_72345601.md) 命令进行NSE与属性模版的关联。对于没有关联配置的NSE，使用默认配置。系统默认模板，其“模板索引”值为“0”，其余属性参见下面参数的默认值。自动上报的NSE匹配不到其他属性时，使用该默认模板。

#### [注意事项](#ZH-CN_MMLREF_0000001126146004)

- 此命令执行后，参数“信令权重”和“数据权重”要在BSC重新发起动态建链流程后才能对自动配置的NSE生效，其他参数立即生效。
- 此命令最大记录数为100。
- 新增的NSE属性模板优先级高于默认属性模板。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126146004)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126146004)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126146004)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARAINDEX | 模板索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待增加的NSE属性模板的索引。<br>数据来源：整网规划<br>取值范围： 0～65535<br>默认值：无<br>说明：当取值为0时，表示修改系统默认添加的NSE属性模板。 |
| FLUSTHT | FLUSH监控定时器（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定待增加的NSE属性模板的FLUSH监控定时器时长，即为SGSN发送FLUSH LL后等待FLUSH LL ACK的超时时长。<br>数据来源：整网规划<br>取值范围：50ms～2000ms<br>默认值：50ms |
| PFC | 是否支持PFC | 可选必选说明：可选参数<br>参数含义：该参数用于指定本网络服务实体是否支持PFC流程（Packet Flow Context procedure）。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“YES(是)” |
| CBL | 是否支持CBL | 可选必选说明：可选参数<br>参数含义：该参数用于指定本网络服务实体是否支持CBL功能（Current Bucket Level） 。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“YES(是)” |
| INR | 是否支持INR | 可选必选说明：可选参数<br>参数含义：该参数用于指定本网络服务实体是否支持INR功能（Inter-NSE re-routing）。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“YES(是)” |
| LCS | 是否支持LCS | 可选必选说明：可选参数<br>参数含义：该参数用于指定本网络服务实体是否支持LCS功能（Location Services）。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)” |
| RIM | 是否支持RIM | 可选必选说明：可选参数<br>参数含义：该参数用于指定本网络服务实体是否支持RIM功能（RAN Information Management）。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)” |
| ARP | 是否携带ARP信元 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否在CREATE-BSS-PFC消息中携带ARP（Allocation/Retention Priority）信元。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)” |
| RACAP | 是否携带RA Capability信元 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否在CREATE-BSS-PFC消息中携带RACAP（RA Capability）信元。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)” |
| GB_FLEX | 是否支持Gb-Flex | 可选必选说明：可选参数<br>参数含义：该参数用于指定本网络服务实体是否支持Gb-Flex功能。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)” |
| SPECSRV | 是否支持特殊业务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本网络服务实体是否支持特殊业务类型。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)” |
| BSSQOSVERSION | BSS支持的Qos版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BSS支持的Qos版本。<br>数据来源：整网规划<br>取值范围：<br>- “R99(R99)”<br>- “R5(R5)”<br>默认值：<br>“R99(R99)” |
| EPNUM | 本端端点个数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端端点个数，用户对NSE下的端点个数有具体要求时使用。<br>数据来源：整网规划<br>取值范围：<br>- “NUMBER_OF_GB_IP_IN_SYSTEM(系统内业务IP个数)”<br>- “ONE(1)”<br>- “TWO(2)”<br>- “THREE(3)”<br>- “FOUR(4)”<br>- “FIVE(5)”<br>- “SIX(6)”<br>默认值：<br>“NUMBER_OF_GB_IP_IN_SYSTEM(系统内业务IP个数)”<br>配置原则：<br>- 当无线侧不同厂商的设备，对核心网侧的端点个数有要求时，根据NSE范围进行配置和关联。<br>- 建议使用默认值。<br>说明：该参数描述自动上报的NSE下本端端点的个数。在选择“NUMBER_OF_GB_IP_IN_SYSTEM(系统内业务IP个数)”的时候，不会超过每个NSE的本端端点最大规格10，同时<br>UNC<br>会根据BSS的SIZE消息中的“Maximum Number of NS-VCs”和“Number of IP4 Endpoints”来限制本端端点的个数，因此规则是MIN(10，“本端端点个数”，“Maximum Number of NS-VCs”/“Number of IP4 Endpoints”)。 |
| SW | 信令权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定自动配置的NSE下本端端点的信令权重，通过SNS CONFIG流程通知到BSC侧。在Pool组网下，某些BSC使用这个端点权重在Pool内的各个SGSN之间进行负荷分担。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：255 |
| DW | 数据权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定自动配置的NSE下本端端点的数据权重，通过SNS CONFIG流程通知到BSC侧。在Pool组网下，某些BSC使用这个端点权重在Pool内的各个SGSN之间进行负荷分担。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：255 |
| MOCN | 是否支持MOCN | 可选必选说明：可选参数<br>参数含义：该参数用于标识自动配置NSE是否支持MOCN功能。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>说明：- 当参数设置为“YES(是)”时，“网络共享(MOCN)”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-207001，License项：LKV2MOCN02）。<br>- 只有BSC、SGSN同时支持MOCN功能时，该功能才会生效。 |
| SPID | 是否支持SPID | 可选必选说明：可选参数<br>参数含义：该参数用于指定向BSS发送的消息中是否携带SPID。<br>数据来源：与对端网元协商<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>说明：- SPID信元，是在3GPP TS R8 48.018协议引入的，由于无线侧设备可能是低协议版本的设备，提供此功能开关避免启用SPID功能时对无线侧设备产生接口兼容性影响。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126146004)

增加一个NSE属性模板， “模板索引 ” 为 “1” ， “FLUSH监控定时器（ms）” 为 “50” ：

ADD GBNSECFGPARA: PARAINDEX=1, FLUSTHT=50;
