# 修改BGP VPN地址族（MOD BGPVRFAF）

- [命令功能](#ZH-CN_CONCEPT_0000001549961310__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001549961310__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001549961310__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001549961310__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001549961310__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001549961310)

该命令用于修改BGP VPN地址族。

#### [注意事项](#ZH-CN_CONCEPT_0000001549961310)

- 该命令执行后立即生效。
- BGP路由负载分担可区分BGP邻居类型，只在同BGP邻居类型间进行。MAXLOADEBGPNUM用来配置EBGP路由负载分担数。MAXLOADIBGPNUM用来配置IBGP路由负载分担数。若EBGP和IBGP负载分担数一致，可用MAXIMUMLOADBALANCE配置，此配置在IBGP和EBGP中均生效。若不需要区分BGP邻居类型，需要在EBGP和IBGP路由进行混合负载分担（比如CE双归场景），则需要配置EIBGPLOADBALANCE参数为非0。因此，MAXLOADEBGPNUM和MAXIMUMLOADBALANCE、EIBGPLOADBALANCE互斥，MAXLOADIBGPNUM和MAXIMUMLOADBALANCE、EIBGPLOADBALANCE互斥。此处互斥是指参数不能同时配置，若配置了其中一个，要配置另一参数，需要执行MOD BGPVRFAF命令将前一个参数配置为默认值，后再配置另一个参数，否则会报错。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001549961310)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001549961310)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST BGPVRFAF命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BGP VPN实例下的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| ASPATHIGNORE | 忽略AS路径 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定在选择最优路由时是否忽略AS_PATH属性。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：与LOADASPATHIGNORE互斥。 |
| MEDNONEASMAXIMUM | MED使用最大值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定在选择最优路由时，如没有MED属性，则把MED按最大值来处理。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| ALWAYSCOMPAREMED | 总是比较MED | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于允许比较来自不同自治系统中邻居路由的MED值。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| DEFAULTLOCALPREF | 缺省本地优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv6vpn”、“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定该地址族下的缺省本地优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| DEFAULTMED | 缺省MED | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv6vpn”、“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定BGP路由的缺省MED值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| DEFAULTRTIMPORTENABLE | 缺省路由引入使能 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否允许将缺省路由引入到BGP路由表中。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| MAXIMUMLOADBALANCE | 最大等价路由数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定在负载分担方式下的等价路由的最大数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～128。<br>默认值：无<br>配置原则：和EIBGPLOADBALANCE互斥； 和MAXLOADEBGPNUM、MAXLOADIBGPNUM互斥。 |
| PREFERENCEEXTERNAL | 外部路由协议优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定EBGP路由的协议优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：和PREFERENCEPOLICYNAME互斥。 |
| PREFERENCEINTERNAL | 内部路由协议优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定IBGP路由的协议优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：和PREFERENCEPOLICYNAME互斥。 |
| PREFERENCELOCAL | 本地路由协议优先级 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定本地路由的协议优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：和PREFERENCEPOLICYNAME互斥。 |
| REFLECTBETWEENCLIENT | 客户机路由反射 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv6vpn”、“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否使能客户机之间的路由反射。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| REFLECTORCLUSTERID | 路由反射器集群ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv6vpn”、“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定反射器的集群ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：集群ID不能和客户机的Router ID相同，当配置成0时，当前配置被删除。 |
| REFLECTORCLUSTERIPV4 | 路由反射器集群ID(IPv4) | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv6vpn”、“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定IPv4地址类型的反射器集群ID。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：集群ID不能和客户机的Router ID相同。当配置成0.0.0.0时，当前配置被删除。 |
| AUTOMATICSUMMARY | 自动聚合 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni”时为可选参数。<br>参数含义：该参数用于使能对本地引入的路由进行自动聚合。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：AUTOMATICSUMMARY属性对network命令引入的路由无效。 |
| ROUTERIDNEGLECT | 忽略路由器ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定BGP在选择最优路由时是否忽略路由ID。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| IGPMETRICIGNORE | 忽略IGP Metric | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv6vpn”、“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定BGP在选择最优路由时忽略IGP Metric的比较。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| PREFERENCEPOLICYNAME | 协议优先级策略名 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定路由策略，可以为满足匹配条件的从对等体收到的路由配置优先级。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 和PREFERENCEEXTERNAL、PREFERENCEINTERNAL、PREFERENCELOCAL字段互斥。路由策略必须已经存在。使用ADD ROUTEPOLICY命令可配置路由策略。使用LST ROUTEPOLICY命令查看可用路由策略。 |
| DETERMINMED | 使能Deterministic-MED | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否开启BGP deterministic-med功能，使能后在对从多个不同AS收到的相同前缀的路由进行选路时，首先会按路由的AS_Path最左边的AS号进行分组。在组内进行比较后，再用组中的优选路由和其他组中的优选路由进行比较，消除了选路的结果和路由接收顺序的相关性，不使能则会按照路由接收的顺序依次进行比较，最终选路的结果和路由的接收顺序是相关的。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| EIBGPLOADBALANCE | EBGP/IBGP负载分担数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定EBGP和IBGP路由负载分担的最大条数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无<br>配置原则：主要用于VPN里CE双归属的场景。当一台CE双归属两台PE，CE和其中一台PE处于相同的AS，和另外一台PE处于不同的AS，这时可以配置EBGP和IBGP路由负载分担的条数，使路由的类型（EBGP/IBGP）不再作为判断条件，从而实现私网流量在EBGP和IBGP路由之间负载分担； 和MAXIMUMLOADBALANCE、MAXLOADEBGPNUM、MAXLOADIBGPNUM互斥；当配置成0时，当前配置被删除。 |
| EBGPIFSENSITIVE | EBGP接口快速感知 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：使能后，当某个接口状态变为Down时，立即清除建立在该接口上的直连EBGP邻居的BGP会话。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| IBGPIFSENSITIVE | IBGP接口快速感知 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：使能后，当某个接口状态变为Down时，立即清除建立在该接口上的直连IBGP邻居的BGP会话。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| MAXLOADEBGPNUM | EBGP负载分担数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定EBGP路由参与BGP负载分担最大条数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～128。<br>默认值：无<br>配置原则：和MAXIMUMLOADBALANCE 、EIBGPLOADBALANCE互斥。 |
| MAXLOADIBGPNUM | IBGP负载分担数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定IBGP路由参与BGP负载分担最大条数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～128。<br>默认值：无<br>配置原则：和MAXIMUMLOADBALANCE 、EIBGPLOADBALANCE互斥。 |
| NHPRELAYROUTEPOLICYNAME | 下一跳迭代路由策略名 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv6vpn”、“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定下一跳迭代使用的路由策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 路由策略必须已经存在。使用ADD ROUTEPOLICY命令可配置路由策略。使用LST ROUTEPOLICY命令查看可用路由策略。 |
| ECMPNEXTHOPCHANGED | 负载分担改下一跳 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否允许BGP只在发布形成负载分担的路由时才修改下一跳为自己，而在发布没有形成负载分担的路由时，不对下一跳作特殊处理。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：需要先配置MAXIMUMLOADBALANCE。 |
| EIBGPEXTHOPCHANGED | EBGP/IBGP负载分担改下一跳 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否允许EBGP路由和IBGP路由只在形成负载分担的路由时才修改下一跳为自己，而在发布没有形成负载分担的路由时，不对下一跳作特殊处理。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：主要用于VPN里CE双归属的场景。 |
| EBGPECMPNEXTHOPCHANGED | EBGP负载分担改下一跳 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否允许EBGP路由在形成负载分担的路由时才修改下一跳为自己，而在发布没有形成负载分担的EBGP路由时，不对下一跳作特殊处理。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：需要先配置MAXLOADEBGPNUM。 |
| IBGPECMPNEXTHOPCHANGED | IBGP负载分担改下一跳 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否允许IBGP路由只在形成负载分担的路由时才修改下一跳为自己，而在发布没有形成负载分担的IBGP路由时，不对下一跳作特殊处理。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：需要先配置MAXLOADIBGPNUM。 |
| REFLECTCHGPATH | 反射器应用出口策略 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv6vpn”、“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否使能路由反射器通过出口策略修改BGP路由的路径属性。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| ACTIVEROUTEADVERTISE | 活跃路由通告 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定BGP仅发布在IP路由表中被优选的路由。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| POLICYEXTCOMMENABLE | 修改扩展团体属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否使能修改扩展团体属性。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| SUPERNETUNIADV | 发布超网单播路由 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否使能向BGP对等体发布BGP超网单播路由，BGP超网路由是指路由目的地址与下一跳地址相同或者路由目的地址更精确。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| ROUTERID | 路由器标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定BGP VPN实例地址族下的路由器ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。取值为一个IPv4地址，不支持0.0.0.0或255.255.255.255。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- ROUTERID和VRFRIDAUTOSEL的配置相互覆盖，且二者不可同时配置。只支持在私网下配置。<br>- BGP VPN实例地址族没有配置Router ID时，若BGP VPN实例下已配置，则直接使用实例下Router ID。 |
| VRFRIDAUTOSEL | 私网BGP实例自动选择路由器ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否设置VPN实例自动选择Router ID。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：VRFRIDAUTOSEL只对私网起作用，公网下配置不起作用，ROUTERID和VRFRIDAUTOSEL的配置相互覆盖，且二者不可同时配置。 |
| POLICYVPNTARGET | 是否需要过VpnTarget的策略 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定是否需要过VpnTarget的策略。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| NEXTHOPSELDEPENDTYPE | 下一跳迭代方式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定下一跳迭代方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- default：缺省类型。<br>- dependTunnel：选路依赖隧道迭代。<br>- dependIp：选路依赖IP迭代。<br>默认值：无<br>配置原则：如果AFTYPE为VPNv4或VPNv6，该参数只能配置为dependTunnel或者dependIp。 |
| TNLSELECTORNAME | 隧道选择器名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv6vpn” 或 “ipv4uni”时为可选参数。<br>参数含义：该参数用于指定隧道选择器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～40。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| TUNNELSELECTORALL | 应用隧道选择器到标签路由，引入路由和网段路由 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否应用隧道选择器到标签路由，引入路由和网段路由。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| BESTEXTERNAL | 是否发布bestExternal路由 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv6vpn”、“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否发布bestExternal路由。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| ROUTESELECTDELAY | 路由选路延迟时间 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv6vpn”、“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定路由选路延迟时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～3600。<br>默认值：无 |
| ADDPATHSELNUM | 选择add-path路由的数量 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv6vpn”、“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定选择add-path路由的数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0，2～64。<br>默认值：无 |
| APPLYLABELMODE | 标签分配方式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定标签分配方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- perRoute：每路由每标签。<br>- perNexthop：每下一跳每标签。<br>默认值：无<br>配置原则：为了节省标签资源，必须配置为perNexthop。 |
| ORIGINATORPRIOR | 选择最佳路由时，Router ID优先于CLUSTER_LIST | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv6vpn”、“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定选择最佳路由时，Router ID是否优先于CLUSTER_LIST。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| RELAYDELAYENABLE | 迭代延迟使能 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv6vpn”、“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否使能迭代延迟。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| RRFILTERNUMBER | 路由反射器组支持的扩展团体属性过滤器号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于给定路由反射器组支持的扩展团体属性过滤器号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～51。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| LOADASPATHIGNORE | 负载均衡忽略AS Path | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定路由在形成负载分担时是否不比较路由的AS-Path属性。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：与ASPATHIGNORE互斥。 |
| MEDCONFED | 联盟内部比较MED | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否仅在联盟内比较MED值的大小。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| AUTOFRRENABLE | 自动FRR使能 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定是否允许自动FRR使能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001549961310)

修改BGP VPN中IPv4单播地址族的参数：

```
MOD BGPVRFAF:VRFNAME="vpna",AFTYPE=ipv4uni,DEFAULTLOCALPREF=100;
```
