# 增加DNS NAPTR记录(ADD DNSN)

- [命令功能](#ZH-CN_MMLREF_0000001172225569__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225569__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225569__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225569__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225569__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225569__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225569)

**适用网元：SGSN、MME**

该命令用于配置 “FQDN” （全称标准规范域名）与网元接口的对应关系。

在Attach、建立PDN连接、TAU、Handover等流程中，都会涉及到 “S-GW” 、 “P-GW” 、 “MME” 等网元的选择，并解析出网元的地址信息。以前采用的是域名到网元地址的一对一映射机制，为了提高组网运作性能，减少信令的传输延时，提出了智能网关选择的策略。比如按照组网方式，在Attach流程中尽量选择 “S-GW” 和 “P-GW” 合一的节点，可以减少信令的传输时延。

该命令可以配置域名（FQDN）与网元节点间多对多的对应关系。当LICENSE支持激活智能网元选择功能且功能开关打开时，由于同一 “FQDN” 可以与多个 “HSINDEX” 配置对应关系，因此在查询过程中，同一 “FQDN” 对应的查询 “HSINDEX” 结果可能存在多个（ “ENTITY” 、 “INTERFACETYPE” 配置相同），这就需要利用智能网元选择策略（选择合一/选择拓扑关系最近）选择出最优的网元节点，而网元节点与IP地址的对应关系是在命令 [**ADD IPV4DNSH**](../DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md) 、 [**ADD IPV6DNSH**](../DNS Hostfile管理/增加IPV6 DNS Hostfile记录(ADD IPV6DNSH)_26145886.md) 中配置。当智能网元选择功能关闭或LICENSE不支持时，查询出的多个结果直接按照优先级/权重返回。

#### [注意事项](#ZH-CN_MMLREF_0000001172225569)

- 本表最大记录数为8192。
- 该命令执行后立即生效。
- “网元类型”、“接口类型”、“UE USAGE TYPE策略”、“支持DCNR”和“融合PGW-C/SMF”都相同的“FQDN”，可配置的主机名最大记录数是64。
- 参数“主机名索引”对应的主机名可以配置2条不同的索引，一条索引关联IPV4DNSH记录，另一条索引关联IPV6DNSH记录，这2条索引配置到DNSN记录中时，当“FQDN”、“网元类型”、“接口类型”、“UE USAGE TYPE策略”、“支持DCNR”和“融合PGW-C/SMF”字段相同时，则除去“描述”参数外，其他参数值必须保持一致。
- 当参数“网元类型”配置为“SGSN(SGSN)”、“MSC(MSC)”，或“IWS(IWS)”时，参数“支持DCNR”不能配置为“YES（是）”。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225569)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225569)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225569)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FQDN | FQDN | 可选必选说明：必选参数<br>参数含义：该参数用于标识由RAI、TAI、APN、MME等构建的域名，用来进行网元查询。<br>数据来源：整网规划<br>取值范围：1~255位字符串<br>默认值：无<br>配置原则：利用构建的FQDN可以查询SGSN、MME、S-GW、P-GW、IWS等网元。其中构建域名的信元组成如下：<br>- S-GW(TAI)：TAC-LB<TAC-LOW-BYTE>.TAC-HB<TAC-HIGH-BYTE>.TAC.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG。例如：TAC-LB01.TAC-HB71.TAC.EPC.MNC123.MCC123.3GPPNETWORK.ORG。<br>- MME(GUMMEI): MMEC<MMEC>.MMEGI<MMEGI>.MME.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG。例如：MMEC12.MMEGI8001.MME.EPC.MNC123.MCC123.3GPPNETWORK.ORG。<br>- P-GW(APN): <APNNI>.APN.EPC.MNC<MNC>.MCC<MCC>.3GPPNETWORK.ORG。例如：HUAWEI1.COM.APN.EPC.MNC123.MCC123.3GPPNETWORK.ORG。<br>说明：- 该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。<br>- <TAC-LOW-BYTE>，<TAC-HIGH-BYTE>，<MMEC>为2位十六进制数， <MMEGI>为4位十六进制数，<MSC ID>为6位十六进制数。<br>- <MNC>，<MCC>为3位十进制数 ，<CELL ID>为4位十进制数。<br>- 如果<>（除了<APNNI>）中的内容不足相应的位数，前面以“0”补齐。<br>- FQDN不能以“.”开始，也不能以“.”结束。 |
| HSINDEX | 主机名索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定FQDN对应网元的索引。<br>前提条件：该参数必须先由<br>[**ADD IPV4DNSH**](../DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md)<br>、<br>[**ADD IPV6DNSH**](../DNS Hostfile管理/增加IPV6 DNS Hostfile记录(ADD IPV6DNSH)_26145886.md)<br>命令定义，才能在此处引用。<br>数据来源：整网规划<br>取值范围：1~2048<br>默认值：无 |
| ENTITY | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口网元的类型。<br>数据来源：整网规划<br>取值范围：<br>- “SGSN(SGSN)”<br>- “GGSN(GGSN)”<br>- “MME(MME)”<br>- “SGW(SGW)”<br>- “PGW(PGW)”<br>- “MSC(MSC)”<br>- “IWS(IWS)”<br>- “AMF(AMF)”<br>默认值：无<br>说明：只有AMF，MME， SGW， PGW网元支持IPv6地址相关的业务。 |
| INTYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定接口对应的类型。<br>数据来源：整网规划<br>取值范围：<br>- “Gn(Gn)”<br>- “Gp(Gp)”<br>- “S3(S3)”<br>- “S4(S4)”<br>- “S5(S5)”<br>- “S8(S8)”<br>- “S10(S10)”<br>- “S11(S11)”<br>- “S16(S16)”<br>- “Sv(Sv)”<br>- “S102(S102)”<br>- “Sdup(Sdup)”<br>- “N26(N26)”<br>默认值：无<br>配置原则：网元类型和接口类型间存在配置约束关系如下，具体配置哪种接口需要依据组网情况而定：<br>- “SGSN”：“Gn”、“S3”、“S4”、“S16”、“Gp”。<br>- “GGSN”：“Gn”、“Gp”。<br>- “MME”：“Gn”、“S3”、“S10”、“S11”、“Sdup”。<br>- “SGW”：“S4”、“S5”、“S8”、“S11”。<br>- “PGW”：“S5”、“S8”、“Gn”、“Gp”。<br>- “MSC”：“Sv”。<br>- “IWS”：“S102”。<br>- “AMF”：“N26”。<br>说明：当该配置数据用于链式备份网元寻址时，需要选Sdup枚举，Sdup接口华为私有接口，是MME和MME之间的接口，用于实现MME间的数据备份。 |
| S5PROTOCOL | S5接口协议类型 | 可选必选说明：可选参数<br>参数含义：该参数用来配置网元SGW/PGW的S5接口协议。<br>前提条件：该参数在<br>“ENTITY”<br>参数配置为<br>“SGW”<br>或<br>“PGW”<br>后为有效值。<br>数据来源：整网规划<br>取值范围：<br>- “GTP(GTP)”<br>- “PMIP(PMIP)”<br>- “GTP_PMIP(GTP_PMIP)”<br>默认值：<br>“GTP(GTP)” |
| S8PROTOCOL | S8接口协议类型 | 可选必选说明：可选参数<br>参数含义：该参数用来配置网元SGW/PGW的S8接口协议。<br>前提条件：该参数在<br>“ENTITY”<br>参数配置为<br>“SGW”<br>或<br>“PGW”<br>后为有效值。<br>数据来源：整网规划<br>取值范围：<br>- “GTP(GTP)”<br>- “PMIP(PMIP)”<br>- “GTP_PMIP(GTP_PMIP)”<br>默认值：<br>“GTP(GTP)” |
| UEUSGTYPEPLCY | UE USAGE TYPE策略 | 可选必选说明：可选参数<br>参数含义：该参数用来指定在专用核心网选择期间，MME查询对应网关时是否需要携带UE USAGE TYPE。<br>数据来源：全网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO（否）”<br>配置原则：当DECOR功能开启，需要通过UE USAGE TYPE进行DNS查询时，需要增加此参数配置为<br>“YES（是）”<br>的DNS NAPTR记录。当前特性支持使用UE USAGE TYPE查询的网元包括MME，SGW和PGW。使用DECOR功能需要开启DECOR基础功能特性（特性编号：WSFD-<br>208001<br>，license部件编码：LKV2DECOR00）和DECOR特性（特性编号：WSFD-<br>208002<br>，license部件编码：LKV2DECOR01）。当接口类型为<br>“Sdup(Sdup)”<br>，配置网元为MME时，需要将此参数配置为<br>“NO(否)”<br>。 |
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：条件必选参数<br>前提条件：该参数在<br>“UE USAGE TYPE策略”<br>“YES(是)”<br>后生效。<br>参数含义：该参数用来指定UE USAGE TYPE群组标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~1023。<br>默认值：无 |
| DCNR | 支持DCNR | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否支持DCNR接入。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“NO（否）”<br>配置原则：当配置为<br>“YES（是）”<br>时，不支持SGSN，MSC和IWS网元。当接口类型为<br>“Sdup(Sdup)”<br>，配置网元为MME时，需要将此参数配置为<br>“NO(否)”<br>。 |
| SMF | 融合PGW-C/SMF | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否支持融合的PGW-C/SMF。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“NO（否）”<br>配置原则：该参数仅在<br>“网元类型”<br>配置为<br>“PGW”<br>时，才能配置为<br>“YES”<br>。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用来指定接口网元对应的优先级。<br>数据来源：整网规划<br>取值范围：0~65535<br>默认值：0<br>配置原则：<br>- 优先级数值配置越小，代表优先级越高。<br>- 优先级越高，则顺序越靠前。 |
| WEIGHT | 权重 | 可选必选说明：可选参数<br>参数含义：该参数用来指定接口网元对应的权重。<br>数据来源：整网规划<br>取值范围：0~65535<br>默认值：100<br>配置原则：<br>- 权重数值配置越大，代表权重越大。<br>- 对于同优先级的网元接口，进行随机选择，权重越大，被选中的概率就越大。<br>- DNS Server返回的Preference需要转换才是权重，转换方法为65535–Preference。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述该命令的文字说明，目的是在配置的时候可以将对象属性、配置原因、背景等进行描述，以便在查询时能够在大量配置数据中清晰的掌握配置的原因。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225569)

按照如下的方式增加配置，则对给定的域名 “TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG” 进行查询时，可以得到两个结果，即 “topon.Eth-0.gw32.abcd.west.example.com” 和 “topon.Eth-0.gw32.abcd.east.example.com” 。假设需要选择与 “gw32.abcd.west.example.com” 合一的网元节点，则最终会根据智能网元选择策略，优先选出节点 “topon.Eth-0.gw32.abcd.west.example.com” ，所得地址为 “192.168.10.10” 。

1. 增加主机名及接口IP地址的对应关系配置：
    - ADD IPV4DNSH: HSINDEX=1, HOSTNAME="topon.Eth-0.gw32.abcd.west.example.com", ADDRSECTION=SECTION1, IPV4ADDR1="192.168.10.10";
    - ADD IPV4DNSH: HSINDEX=2, HOSTNAME="topon.Eth-0.gw32.abcd.east.example.com", ADDRSECTION=SECTION1, IPV4ADDR1="192.168.10.20";
    - ADD IPV4DNSH: HSINDEX=3, HOSTNAME="topoff.Eth-0.gw32.florida.east.example.com", ADDRSECTION=SECTION1, IPV4ADDR1="192.168.10.30";
2. 增加一个网元，“网元类型”类型是“SGW”，“接口类型”是“S11”，“UE USAGE TYPE策略”为“是”，“UEUSGTYPEGPID”为“1”，“支持DCNR”为“NO”，“融合PGW-C/SMF”为“NO”，“优先级”为“0”，“权重”是“100”，“FQDN”为“TAC-LB01.TAC-HB71.TAC.EPC.MNC123.MCC123.3GPPNETWORK.ORG”，“描述”是“To huawei SGW01”：
    - ADD DNSN: FQDN="TAC-LB01.TAC-HB71.TAC.EPC.MNC123.MCC123.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=SGW, INTYPE=S11, S5PROTOCOL=GTP, S8PROTOCOL=GTP, UEUSGTYPEPLCY=YES, UEUSGTYPEGPID=1, DCNR=NO, SMF=NO, PRIORITY=0, WEIGHT=100, DESC="To huawei SGW01";
    - ADD DNSN: FQDN="TAC-LB01.TAC-HB71.TAC.EPC.MNC123.MCC123.3GPPNETWORK.ORG", HSINDEX=2, ENTITY=SGW, INTYPE=S11, S5PROTOCOL=GTP, S8PROTOCOL=GTP, UEUSGTYPEPLCY=YES, UEUSGTYPEGPID=1, DCNR=NO, SMF=NO, PRIORITY=0, WEIGHT=100, DESC="To huawei SGW01";
    - ADD DNSN: FQDN="TAC-LB01.TAC-HB71.TAC.EPC.MNC123.MCC123.3GPPNETWORK.ORG", HSINDEX=3, ENTITY=SGW, INTYPE=S11, S5PROTOCOL=PMIP, S8PROTOCOL=PMIP, UEUSGTYPEPLCY=YES, UEUSGTYPEGPID=1, DCNR=NO, SMF=NO, PRIORITY=0, WEIGHT=100, DESC="To huawei SGW01";
