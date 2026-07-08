# 增加BGP对等体组地址族（ADD BGPPEERGROUPAF）

- [命令功能](#ZH-CN_CONCEPT_0000001600840805__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600840805__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600840805__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600840805__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600840805__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600840805)

该命令用于添加BGP对等体组的地址族。

#### [注意事项](#ZH-CN_CONCEPT_0000001600840805)

- 该命令执行后立即生效。
- 该命令最大记录数为32768。
- ADD BGPPEERGROUP会默认添加对等体组到IPv4地址族。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600840805)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600840805)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于给定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| GROUPNAME | 对等体组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定相应的对等体组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：使用LST BGPPEERGROUP命令查看可用对等体组名。 |
| GROUPTYPE | 对等体组类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定该对等体组的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ebgp：EBGP。<br>- ibgp：IBGP。<br>默认值：ibgp<br>配置原则：GROUPTYPE为ebgp时，不支持的参数有REFLECTCLIENT、ADVADDPATHNUM、ADDPATHMODE、SUBSTITUTEASENABLE、ADVBESTEXTERNAL。 |
| ADVERTISECOMMUNITY | 团体属性发布 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于选择是否将团体属性发布给对等体组。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| ADVERTISEEXTCOMMUNITY | 扩展团体属性发布 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于选择是否将扩展团体属性发布给对等体组。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| DISCARDEXTCOMMUNITY | 扩展团体属性丢弃 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于选择是否丢弃接收到的路由中的扩展团体属性。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| ALLOWASLOOPENABLE | 允许AS号重复 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于选择该对等体组是否允许对等体发送的路由AS-PATH中含有本地AS号的路由。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| ALLOWASLOOPLIMIT | 允许AS号重复数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定允许的AS号最大重复个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10。<br>默认值：无<br>配置原则：<br>- 只有在ALLOWASLOOPENABLE被使能后，该参数才能配置。<br>- 如果不输入该参数，则不允许收到路由的AS号与本地AS号重复。 |
| DEFAULTRTADVENABLE | 允许缺省路由通告 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于选择是否向对等体组发布缺省路由。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| DEFAULTRTADVPOLICY | 缺省路由通告策略 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定配置路由的发布策略。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：在此之前应使用ADD ROUTEPOLICY命令配置对应策略。使用LST ROUTEPOLICY命令查看可用路由策略。 |
| DEFAULTRTMATCHMODE | 带条件匹配缺省路由发布 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定缺省路由的匹配模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- null：不指定匹配模式。<br>- matchall：全部匹配。<br>- matchany：部分匹配。<br>默认值：null |
| KEEPALLROUTES | 路由更新保存 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定是否保存自BGP连接建立之后的所有来自对等体（组）的BGP路由更新信息，即使这些路由没有通过已配置的入口策略。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| NEXTHOPCONFIGURE | 下一跳处理模式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定向IBGP对等体发送路由时是否将下一跳改为本地接口地址。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- null：不指定下一跳处理模式。<br>- local：本地。<br>- invariable：下一跳属性不变化。<br>默认值：无<br>配置原则：当地址族类型为ipv6uni时，不支持配置该字段为invariable。 |
| PREFERREDVALUE | 路由首选值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于设定BGP路由的首选值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：0 |
| PUBLICASONLY | 仅携带公有AS号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定该对等体组发送BGP更新报文时AS_Path属性不携带私有AS号，仅携带公有AS号。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| ROUTELIMIT | 路由超限阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定从BGP对等体收到的最大路由数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：<br>- 如果不输入该参数，则不限制从BGP对等体组收到的最大路由数量。<br>- 当配置成0时，当前配置被删除。 |
| ROUTELIMITPERCENT | 路由超限百分比 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定路由器开始生成告警消息时的路由数量的百分比，当数量超过（number×alert-percent）/100时，开始发出警告信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：75<br>配置原则：只有在ROUTELIMIT被配置后，该参数才能配置。 |
| ROUTELIMITTYPE | 路由超限告警类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定路由器接收路由数超出允许接收的最大路由数时的动作类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- noparameter：缺省值。<br>- alertOnly：对路由超限仅限于产生告警，不再接收超限后的路由。<br>- idleForever：路由超限断连后，不自动重新建立连接。<br>- idleTimeout：路由超限断连后，在超时定时器规定的时间内自动重新建立连接。<br>默认值：noparameter |
| ROUTELIMITIDLETIMEOUT | 超时定时器（min） | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定当路由超限断开连接后，设置自动重新建立连接超时定时器的时间，在定时器超时前，不自动重新建立连接。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1200，单位是分钟。<br>默认值：无<br>配置原则：<br>- 当ROUTELIMITTYPE为idleTimeout，才可配置该字段。否则该字段配置被删除。<br>- 如果不输入该参数，则路由超限后产生告警并记入日志，邻居中断连接，30秒后自动重新尝试建立邻居关系。 |
| RTUPDTINTERVAL | 路由更新时间（s） | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。<br>参数含义：该参数用于指定向指定对等体/对等体组发送相同路由前缀更新报文的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～600，单位是秒。<br>默认值：无<br>配置原则：如果不配置该参数，IBGP对等体组的路由更新时间间隔为15秒，EBGP对等体组的路由更新时间间隔为30秒。 |
| REFLECTCLIENT | 路由反射器客户 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定本对等体组作为路由反射器。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE<br>配置原则：该参数和ADVBESTEXTERNAL互斥。反射器客户仅可配置在IBGP邻居。 |
| SUBSTITUTEASENABLE | 替换AS Path属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于使能是否替换AS_PATH中指定对等体的AS号。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE<br>配置原则：当VRFNAME为_public_时，该参数只能配置为FALSE。替换AS_Path属性里的对等体AS号仅可配置在IBGP邻居。 |
| IMPORTRTPOLICYNAME | 引入路由策略 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定对等体组的路由入口策略。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：路由策略必须已经存在。使用ADD ROUTEPOLICY命令可配置路由策略。使用LST ROUTEPOLICY命令查看可用路由策略。 |
| EXPORTRTPOLICYNAME | 发布路由策略 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定对等体组的路由出口策略。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：路由策略必须已经存在。使用ADD ROUTEPOLICY命令可配置路由策略。使用LST ROUTEPOLICY命令查看可用路由策略。 |
| IMPORTPREFFILTNAME | 引入前缀过滤策略 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn” 或 “ipv4uni”时为可选参数。<br>参数含义：该参数用于指定IPv4地址族的入口Prefix过滤策略 数据来源：本端规划 。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无<br>配置原则：前缀过滤策略必须已经存在。使用ADD PREFIXFILTERNODE命令可配置前缀过滤策略。使用LST PREFIXFILTERNODE命令查看可用前缀过滤策略。 |
| EXPORTPREFFILTNAME | 发布前缀过滤策略 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn” 或 “ipv4uni”时为可选参数。<br>参数含义：该参数用于指定IPv4地址族的出口Prefix过滤策略。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无<br>配置原则：前缀过滤策略必须已经存在。使用ADD PREFIXFILTERNODE命令可配置前缀过滤策略。使用LST PREFIXFILTERNODE命令查看可用前缀过滤策略。 |
| IMPORTASPATHFILTER | 接收路由AS Path过滤 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定本地的入口AS_PATH过滤策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～51。<br>默认值：无<br>配置原则：as-path过滤策略必须已经存在。使用ADD ASPATHFILTERNODE命令可配置as-path过滤策略。使用LST ASPATHFILTERNODE命令查看可用as-path过滤策略。 |
| EXPORTASPATHFILTER | 发布路由AS Path过滤 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni”、“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定本地的出口AS_PATH过滤策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～51。<br>默认值：无<br>配置原则：as-path过滤策略必须已经存在。使用ADD ASPATHFILTERNODE命令可配置as-path过滤策略。使用LST ASPATHFILTERNODE命令查看可用as-path过滤策略。 |
| IMPORTACLNAMEORNUM | 接收路由ACL规则标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn” 或 “ipv4uni”时为可选参数。<br>参数含义：该参数用于指定路由器入口方向上的IPv4地址族访问控制列表（ACL）名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。只支持ACL number取值范围为2000-2999的基本ACL策略。<br>默认值：无<br>配置原则：被引用的ACL策略中只会生效ACL number为2000-2999的基本ACL策略。基本ACL策略必须已经存在。使用ADD ACLGROUP命令可配置基本ACL策略。使用LST ACLGROUP命令查看可用基本ACL策略。 |
| EXPORTACLNAMEORNUM | 发布路由ACL规则标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn” 或 “ipv4uni”时为可选参数。<br>参数含义：该参数用于指定路由器出口方向上IPv4地址族的访问控制列表（ACL）名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。只支持ACL number取值范围为2000-2999的基本ACL策略。<br>默认值：无<br>配置原则：被引用的ACL策略中只会生效ACL number为2000-2999的基本ACL策略。基本ACL策略必须已经存在。使用ADD ACLGROUP命令可配置基本ACL策略。使用LST ACLGROUP命令查看可用基本ACL策略。 |
| ADVBESTEXTERNAL | 是否发布bestExternal路由 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定是否发布bestExternal路由。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE<br>配置原则：与ADVADDPATHNUM互斥，路由发布命令仅可配置在IBGP邻居。当VRFNAME为_public_时，才支持配置该参数。 |
| ADVADDPATHNUM | 向邻居发布多少条add-path路由 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定向邻居发布多少条add-path路由。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0，2～64。<br>默认值：无<br>配置原则：<br>- 与ADVBESTEXTERNAL互斥，路由发布命令仅可配置在IBGP邻居。当VRFNAME为_public_时，才支持配置该参数。<br>- 如果不输入该参数，则BGP设备只向对等体发送一条最优路由。 |
| ADDPATHMODE | add-path模式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定add-path模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- null：不指定Add-Path处理模式。<br>- receive：接收。<br>- send：发送。<br>- both：收发。<br>默认值：null<br>配置原则：当VRFNAME为_public_时，才支持配置该参数。 |
| PUBLICASONLYFORCE | 强制删除私有AS号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定是否强制删除私有as号。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE<br>配置原则：只有在PUBLICASONLY使能的情况下，该参数才能为TRUE，并且与PUBLICASONLYLIMITED互斥。 |
| PUBLICASONLYLIMITED | 删除左边的私有AS号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定是否删除左边的私有AS号。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE<br>配置原则：只有在PUBLICASONLY使能的情况下，该参数才能为TRUE，并且与PUBLICASONLYFORCE互斥。 |
| PUBLICASONLYREPLACE | 用本地AS号替换所有的私有AS号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定是否用本地AS号替换所有的私有AS号。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE<br>配置原则：只有在PUBLICASONLYFORCE或者PUBLICASONLYLIMITED使能的情况下，该参数才能为TRUE。 |
| INCLUDEPEERAS | 不忽略BGP邻居的AS号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv4vpn”、“ipv4uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定是否忽略BGP邻居的AS号。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE<br>配置原则：只有在PUBLICASONLYFORCE或者PUBLICASONLYLIMITED使能的情况下，该参数才能为TRUE。 |
| IMPORTPREF6FILTNAME | 引入IPv6前缀过滤策略 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定IPv6地址族的入口前缀过滤策略。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无 |
| EXPORTPREF6FILTNAME | 发布IPv6前缀过滤策略 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定IPv6地址族的出口前缀过滤策略。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无 |
| IMPORTACL6NAMEORNUM | 接收路由ACL6规则标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定路由器入口方向上的IPv6地址族访问控制列表（ACL）编号或者名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：被引用的ACL策略中只会生效ACL number为2000-2999的基本ACL策略。 |
| EXPORTACL6NAMEORNUM | 发布路由ACL6规则标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“ipv6uni” 或 “ipv6vpn”时为可选参数。<br>参数含义：该参数用于指定路由器出口方向上IPv6地址族的访问控制列表（ACL）编号或者名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：被引用的ACL策略中只会生效ACL number为2000-2999的基本ACL策略。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600840805)

- 为对等体组"asdf"添加VPNv4地址族：
  ```
  SET BGP:ASNUM="100",BGPENABLE=TRUE;
  ADD BGPPEERGROUP:VRFNAME="_public_",AFTYPE=public,GROUPNAME="asdf";
  ADD BGPPEERGROUPAF:VRFNAME="_public_",AFTYPE=ipv4vpn,GROUPNAME="asdf";
  ```
- 为对等体组"asdf"添加IPv6地址族：
  ```
  SET BGP:ASNUM="100",BGPENABLE=TRUE;
  ADD BGPPEERGROUP:VRFNAME="_public_",AFTYPE=public,GROUPNAME="asdf";
  ADD BGPPEERGROUPAF:VRFNAME="_public_",AFTYPE=ipv6uni,GROUPNAME="asdf";
  ```
