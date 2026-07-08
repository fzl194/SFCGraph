---
id: UNC@20.15.2@MMLCommand@ADD AREADNS
type: MMLCommand
name: ADD AREADNS（增加位置区域DNS域名）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: AREADNS
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 2048
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-SGSN_S10_S16_S3接口管理
- 位置域名管理
status: active
---

# ADD AREADNS（增加位置区域DNS域名）

## 功能

**适用网元：SGSN、MME**

该命令用于增加位置区域DNS域名，从而可以简化 UNC 上 [**ADD IPV4DNSH**](../../DNS/DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md) 和 [**ADD DNSN**](../../DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md) 的配置信息。

- 在2G/3G用户Inter-SGSN流程中，会涉及到对端网元SGSN的选择，并解析出网元的地址信息。以前采用的是域名到网元地址的一一映射机制，为了简化[**ADD IPV4DNSH**](../../DNS/DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md)的配置信息，提出了位置域名管理，可以将多个位置区域名映射到一个网元地址上。
  场景举例：
  如果 “0x0001” 位置区下0x01～0x05路由区的用户，需要配置对应SGSN的域名解析:
    - 当无此配置时，则需要配置如下五条IPv4地址信息，才可以满足在该位置区下各个不同路由区的用户查询DNS的功能正常：
      ADD IPV4DNSH: HSINDEX=1, HOSTNAME="RAC0001.LAC0001.RAC.EPC.MNC123.MCC456.3GPPNETWORK.ORG", ADDRSECTION=SECTION1,IPV4ADDR1="10.141.149.100";
      ADD IPV4DNSH: HSINDEX=2, HOSTNAME="RAC0002.LAC0001.RAC.EPC.MNC123.MCC456.3GPPNETWORK.ORG", ADDRSECTION=SECTION1,IPV4ADDR1="10.141.149.100";
      ADD IPV4DNSH: HSINDEX=3, HOSTNAME="RAC0003.LAC0001.RAC.EPC.MNC123.MCC456.3GPPNETWORK.ORG", ADDRSECTION=SECTION1,IPV4ADDR1="10.141.149.100";
      ADD IPV4DNSH: HSINDEX=4, HOSTNAME="RAC0004.LAC0001.RAC.EPC.MNC123.MCC456.3GPPNETWORK.ORG", ADDRSECTION=SECTION1,IPV4ADDR1="10.141.149.100";
      ADD IPV4DNSH: HSINDEX=5, HOSTNAME="RAC0005.LAC0001.RAC.EPC.MNC123.MCC456.3GPPNETWORK.ORG", ADDRSECTION=SECTION1,IPV4ADDR1="10.141.149.100";
    - 当有如下配置存在时：
      ADD AREADNS: DNTYPE=SGSN_RAI, LAC="0001", RAC="01", RACRANGE="05";
      则只需要配置如下一条IPv4地址信息来代替上面五条，就可以满足在该位置区下各个不同路由区的用户查询DNS的功能正常：
      ADD IPV4DNSH: HSINDEX=1, HOSTNAME="RAC0001.LAC0001.RAC.EPC.MNC123.MCC456.3GPPNETWORK.ORG",ADDRSECTION=SECTION1,IPV4ADDR1=" 10.141.149.100 ";
- 在4G用户Attach、建立PDN连接、TAU、Handover、SRVCC等流程中，都会涉及到S-GW、P-GW、MME、MSC等网元的选择，并解析出网元的地址信息。以前采用的是域名到网元地址的一一映射机制，为了提高组网运作性能，减少信令的传输延时，提出了智能网关选择的策略。而为了简化智能网关选择命令[**ADD DNSN**](../../DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md)的配置信息，提出了位置域名管理，可以将多个位置区域名映射到一个网关上。
  场景举例：
  如果0x0001～0x0005跟踪区下的用户对应如下S-GW的IPv4地址信息配置：
  ADD IPV4DNSH: HSINDEX=1, HOSTNAME="TOPON.SGW.SGW1.NODES.EPC.MNC123.MCC456.3GPPNETWORK.ORG", ADDRSECTION=SECTION1, IPV4ADDR1=" 10.141.149.100 ";
    - 当无此配置时，则需要配置如下五条FQDN与S11口的对应关系，才可以满足各个不同跟踪区下的用户查询DNS的功能正常：
      ADD DNSN: FQDN="TAC-LB01.TAC-HB00.TAC.EPC.MNC123.MCC456.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=SGW, INTYPE=S11;
      ADD DNSN: FQDN="TAC-LB02.TAC-HB00.TAC.EPC.MNC123.MCC456.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=SGW, INTYPE=S11;
      ADD DNSN: FQDN="TAC-LB03.TAC-HB00.TAC.EPC.MNC123.MCC456.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=SGW, INTYPE=S11;
      ADD DNSN: FQDN="TAC-LB04.TAC-HB00.TAC.EPC.MNC123.MCC456.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=SGW, INTYPE=S11;
      ADD DNSN: FQDN="TAC-LB05.TAC-HB00.TAC.EPC.MNC123.MCC456.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=SGW, INTYPE=S11;
    - 当有如下配置存在时：
      ADD AREADNS: DNTYPE=SGW_TAI, TAC="0x0001", TACRANGE="0x0005";
      则只需要配置如下一条FQDN与S11口的对应关系来代替上面五条，就可以满足在该位置区下各个不同跟踪区的用户查询DNS的功能正常：
      ADD DNSN: FQDN="TAC-LB01.TAC-HB00.TAC.EPC.MNC123.MCC456.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=SGW, INTYPE=S11;
- 当域名类型为“GGSN/PGW_RAI（根据路由区（RAI）查找GGSN/PGW）”，“GGSN/PGW_RAI（根据路由区（RAI）查找GGSN/PGW）”或“PGW_TAI（根据跟踪区（TAI）查找PGW）”时，开启了WSFD-205003基于位置区域选择网关特性，支持对RAC/LAC/TAC进行分组，例如RAC_1~RAC_3组成一个集合或者LAC_1~LAC_3组成一个集合，此集合映射为归一化标识（ZNAME），当位于RAC_1~RAC_3或者LAC_1~LAC_3的用户请求以APN1激活时，将APN1添加归一化标识(如APNNI.ZNAME.APNOI)。这种方法可以大大减少配置DNS解析记录的数量。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数2048。
- 区域名称的构成字符对大小写字母敏感。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNTYPE | 域名类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定域名类型。<br>数据来源：全网规划<br>取值范围：<br>- “SGW_RAI（根据路由区（RAI）查找SGW）”<br>- “SGW_TAI（根据跟踪区（TAI）查找SGW）”<br>- “SGSN_RAI（根据路由区（RAI）查找SGSN）”<br>- “MME_TAI（根据跟踪区（TAI）查找MME）”<br>- “GGSN/PGW_RAI（根据路由区（RAI）查找GGSN/PGW）”<br>- “PGW_TAI（根据跟踪区（TAI）查找PGW）”<br>- “MSC_RAI（根据路由区（RAI）查找MSC）”<br>- “MSC_LAI（根据位置区（LAI）查找MSC）”<br>- “GGSN/PGW_LAI（根据位置区（LAI）查找GGSN/PGW）”<br>- “SGW_LAI（根据位置区（LAI）查找SGW）”<br>- “SGSN_LAI（根据位置区（LAI）查找SGSN）”<br>- “MME_TAI_UUT（根据跟踪区（TAI）和UE USAGE TYPE查找MME）”<br>- “SGW_TAI_UUT（根据跟踪区（TAI）和UE USAGE TYPE查找SGW）”<br>- “MMEGI_TAI_UUT（根据跟踪区（TAI）和UE USAGE TYPE查找MMEGI）”<br>默认值：无<br>配置原则：<br>- “SGW_RAI（根据路由区（RAI）查找SGW）”：该参数用于指定域名类型为根据路由区（RAI）查找SGW。<br>- “SGW_TAI（根据跟踪区（TAI）查找SGW）”：该参数用于指定域名类型为根据跟踪区（TAI）查找SGW。<br>- “SGSN_RAI（根据路由区（RAI）查找SGSN）”：该参数用于指定域名类型为根据路由区（RAI）查找SGSN。<br>- “MME_TAI（根据跟踪区（TAI）查找MME）”：该参数用于指定域名类型为根据跟踪区（TAI）查找MME。<br>- “GGSN/PGW_RAI（根据路由区（RAI）查找GGSN/PGW）”：该参数用于指定域名类型为根据路由区（RAI）查找GGSN/PGW。<br>- “PGW_TAI（根据跟踪区（TAI）查找PGW）”：该参数用于指定域名类型为根据跟踪区（TAI）查找PGW。<br>- “MSC_RAI（根据路由区（RAI）查找MSC）”：该参数用于指定域名类型为根据跟踪区（RAI）查找MSC。[**SET MSCSELPLCY**](../../Sv接口管理/MSC选择策略/设置MSC选择策略(SET MSCSELPLCY)_26305786.md)的“Sv接口域名解析策略”参数配置为“RAI（RAI）”时有效。当运营商仅部署SRVCC特性，而不部署基于SRVCC的数据语音双切换特性的情况下，无需使用本域名配置简化功能（因为eNodeB在“Handover Required”中携带的“RAC”为“FF”）。<br>- “MSC_LAI（根据位置区（LAI）查找MSC）”：该参数用于指定域名类型为根据跟踪区（LAI）查找MSC。[**SET MSCSELPLCY**](../../Sv接口管理/MSC选择策略/设置MSC选择策略(SET MSCSELPLCY)_26305786.md)的“Sv接口域名解析策略”参数配置为“LAI（LAI）”时有效。<br>- “GGSN/PGW_LAI（根据位置区（LAI）查找GGSN/PGW）”：该参数用于指定域名类型为根据位置区（LAI）查找GGSN/PGW。<br>- “SGW_LAI（根据位置区（LAI）查找SGW）”：该参数用于指定域名类型为根据位置区（LAI）查找SGW。<br>- “SGSN_LAI（根据位置区（LAI）查找SGSN）”：该参数用于指定域名类型为根据位置区（LAI）查找SGSN。<br>- “根据跟踪区（TAI）和UE USAGE TYPE查找MME”：该参数用于指定域名类型为根据跟踪区（TAI）和UE USAGE TYPE查找MME，其在DECOR特性开启时生效，使用DECOR特性需要开启DECOR基础功能特性（特性编号：WSFD-208001，license部件编码：81202740）和DECOR特性（特性编号：WSFD-208002，license部件编码：82207914）。<br>- “根据跟踪区（TAI）和UE USAGE TYPE查找MMEGI”：该参数用于指定域名类型为根据跟踪区（TAI）和UE USAGE TYPE查找MMEGI，其在DECOR特性开启时生效，使用DECOR特性需要开启DECOR基础功能特性（特性编号：WSFD-208001，license部件编码：81202740）和DECOR特性（特性编号：WSFD-208002，license部件编码：82207914）。<br>- “根据跟踪区（TAI）和UE USAGE TYPE查找SGW”：该参数用于指定域名类型为根据跟踪区（TAI）和UE USAGE TYPE查找SGW，其在DECOR特性开启时生效，使用DECOR特性需要开启DECOR基础功能特性（特性编号：WSFD-208001，license部件编码：81202740）和DECOR特性（特性编号：WSFD-208002，license部件编码：82207914）。说明：- 当同时匹配到“GGSN/PGW_RAI（根据路由区（RAI）查找GGSN/PGW）”和“GGSN/PGW_LAI（根据位置区（LAI）查找GGSN/PGW）”时，以前者为准。<br>- 当同时匹配到“SGW_RAI（根据路由区（RAI）查找SGW）”和“SGW_LAI（根据位置区（LAI）查找SGW）”时，以前者为准。<br>- 当同时匹配到“SGSN_RAI（根据路由区（RAI）查找SGSN）”和“SGSN_LAI（根据位置区（LAI）查找SGSN）”时，以前者为准。 |
| LAC | 位置区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定位置区域码。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“SGW_RAI（根据路由区（RAI）查找SGW）”<br>或<br>“SGSN_RAI（根据路由区（RAI）查找SGSN）”<br>或<br>“GGSN/PGW_RAI（根据路由区（RAI）查找GGSN/PGW）”<br>或<br>“MSC_RAI（根据路由区（RAI）查找MSC）”<br>或<br>“MSC_LAI（根据位置区（LAI）查找MSC）”<br>或<br>“SGW_LAI（根据位置区（LAI）查找SGW）”<br>或<br>“SGSN_LAI（根据位置区（LAI）查找SGSN）”<br>或<br>“GGSN/PGW_LAI（根据位置区（LAI）查找GGSN/PGW）”<br>后显示。<br>数据来源：全网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>说明：用户在输入值的时候，可以加上<br>“0x”<br>前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| LACRANGE | 位置区域码范围 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定位置区域码范围。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“MSC_LAI（根据位置区（LAI）查找MSC）”<br>或<br>“SGW_LAI（根据位置区（LAI）查找SGW）”<br>或<br>“SGSN_LAI（根据位置区（LAI）查找SGSN）”<br>或<br>“GGSN/PGW_LAI（根据位置区（LAI）查找GGSN/PGW）”<br>后显示。<br>数据来源：全网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>配置原则：<br>- 该参数的值必须大于等于“位置区域码”的值。<br>- 新添加的位置区域码范围不能与原有的位置区域码范围出现重叠。<br>- 如果该参数不输入，表示配置单个LAC。<br>说明：用户在输入值的时候，可以加上<br>“0x”<br>前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| RAC | 路由区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定路由区域码。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“SGW_RAI（根据路由区（RAI）查找SGW）”<br>或<br>“SGSN_RAI（根据路由区（RAI）查找SGSN）”<br>或<br>“GGSN/PGW_RAI（根据路由区（RAI）查找GGSN/PGW）”<br>或<br>“MSC_RAI（根据路由区（RAI）查找MSC）”<br>后显示。<br>数据来源：全网规划<br>取值范围：0x00～0xFF<br>默认值：无<br>说明：用户在输入值的时候，可以加上<br>“0x”<br>前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| RACRANGE | 路由区域码范围 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定路由区域码范围。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“SGW_RAI（根据路由区（RAI）查找SGW）”<br>或<br>“SGSN_RAI（根据路由区（RAI）查找SGSN）”<br>或<br>“GGSN/PGW_RAI（根据路由区（RAI）查找GGSN/PGW）”<br>或<br>“MSC_RAI（根据路由区（RAI）查找MSC）”<br>后显示。<br>数据来源：全网规划<br>取值范围：0x00～0xFF<br>默认值：无<br>配置原则：<br>- 该参数的值必须大于等于“路由区域码”的值。<br>- 同一位置区下新添加的路由区域码范围不能与原有路由区域码范围出现重叠。<br>- 如果该参数不输入，表示配置单个RAC。<br>说明：用户在输入值的时候，可以加上<br>“0x”<br>前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| TAC | 跟踪区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定跟踪区域码。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“SGW_TAI（根据跟踪区（TAI）查找SGW）”<br>或<br>“MME_TAI（根据跟踪区（TAI）查找MME）”<br>或<br>“PGW_TAI（根据跟踪区（TAI）查找PGW）”<br>后显示。<br>数据来源：全网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>说明：用户在输入值的时候，可以加上<br>“0x”<br>前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| TACRANGE | 跟踪区域码范围 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定跟踪区域码范围。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“SGW_TAI（根据跟踪区（TAI）查找SGW）”<br>或<br>“MME_TAI（根据跟踪区（TAI）查找MME）”<br>或<br>“PGW_TAI（根据跟踪区（TAI）查找PGW）”<br>后显示。<br>数据来源：全网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>配置原则：<br>- 该参数的值必须大于等于“跟踪区域码”的值。<br>- 新添加的跟踪区域码范围不能与原有跟踪区域码范围出现重叠。<br>- 如果该参数不输入，表示配置单个TAC。<br>说明：用户在输入值的时候，可以加上<br>“0x”<br>前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| UUT | UE USAGE TYPE | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定UE USAGE TYPE。<br>前提条件：<br>- 该参数在<br>“域名类型”<br>参数配置为<br>“根据跟踪区（TAI）和UE USAGE TYPE查找MME”<br>后生效。<br>- 该参数在<br>“域名类型”<br>参数配置为<br>“根据跟踪区（TAI）和UE USAGE TYPE查找SGW”<br>后生效。<br>- 该参数在<br>“域名类型”<br>参数配置为<br>“根据跟踪区（TAI）和UE USAGE TYPE查找MMEGI”<br>后生效。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0~255<br>默认值：无<br>配置原则：<br>UE USAGE TYPE为用户的特征属性。请参见3GPP TS 29.272 |
| ZONESW | 定制区域标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制是否为位置区域定制标识。<br>数据来源：全网规划<br>取值范围：“NO（否）”“YES（是）”<br>默认值：“NO（否）”<br>配置原则：<br>- NO:将集合内的RAI/LAI/TAI映射到归一的RAI/LAI/TAI（即起始RAI/LAI/TAI），再根据通过归一的RAI/LAI/TAI来定制DNS域名。例如：位于RAI_1~RAI_10的用户请求以APN1激活时，统一将APN1定制为RAI_1+APN1进行DNS解析。<br>- YES:将集合内的RAI/LAI/TAI映射到区域名称(ZONENAME)，再根据区域名称来定制DNS域名。例如：位于RAI_1~RAI_10的用户请求以APN1激活时，统一将APN1定制为APN1.ZONE1.APNOI进行DNS解析。 |
| ZONENAME | 区域名称 | 可选必选说明：条件必选参数<br>参数含义：该参数标识位置区域，用于定制DNS域名，简化DNS Server或Hostfile的数据配置。<br>前提条件：该参数在<br>“定制区域标识”<br>参数配置为<br>“YES（是）”<br>后显示。<br>数据来源：全网规划<br>取值范围：1~32位字符串<br>默认值：无<br>配置原则：<br>区域名称的构成字符只能是字母A～Z或a～z、数字0～9、符号“-”和“.”，并且“-”和“.”不能是区域名称的开头和结尾，大小写不敏感。 |
| ZONELOC | 区域名称位置 | 可选必选说明：条件可选参数<br>参数含义：该参数用于标识区域名称在DNS域名中的位置。<br>前提条件：该参数在<br>“定制区域标识”<br>参数配置为<br>“YES（是）”<br>后显示。<br>数据来源：全网规划<br>取值范围：<br>- “APNNI_ZONE_APNOI（APNNI_ZONE_APNOI）”<br>- “ZONE_APNNI_APNOI（ZONE_APNNI_APNOI）”<br>默认值：<br>“APNNI_ZONE_APNOI（APNNI_ZONE_APNOI）”<br>配置原则：<br>- APNNI_ZONE_APNOI：区域名称位于DNS域名的中间位置。定制后的域名格式为：APNNI.ZONE.APNOI。<br>- ZONE_APNNI_APNOI：区域名称位于DNS域名的开始位置。定制后的域名格式为：ZONE.APNNI.APNOI。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AREADNS]] · 位置区域DNS域名（AREADNS）

## 使用实例

1. 当“0x0001”到“0x0022”跟踪区对应同一个SGW时，可以使用该命令来简化[**ADD DNSN**](../../DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md)配置。
  ADD AREADNS: DNTYPE=SGW_TAI, TAC="0x0001", TACRANGE="0x0022";
  ADD IPV4DNSH: HSINDEX=100, HOSTNAME="TOPON.SGW.SGW1.NODES.EPC.MNC003.MCC460.3GPPNETWORK.ORG", ADDRSECTION=SECTION1, IPV4ADDR1="192.168.49.205";
  ADD DNSN: FQDN="TAC-LB01.TAC-HB00.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG", HSINDEX=100, ENTITY=SGW, INTYPE=S11;
2. 当“0x0001”到“0x0022”位置区对应同一个MSC时，可以使用该命令来简化[**ADD DNSN**](../../DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md)配置。
  ADD AREADNS: DNTYPE=MSC_LAI, LAC="0x0001", LACRANGE="0x0022";
  ADD IPV4DNSH: HSINDEX=101, HOSTNAME="TOPON.MSC.MSC1.NODES.EPC.MNC003.MCC460.3GPPNETWORK.ORG", ADDRSECTION=SECTION1, IPV4ADDR1="192.168.48.205";
  ADD DNSN: FQDN="LAC0001.LAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG", HSINDEX=101, ENTITY=MSC, INTYPE=Sv;
3. 当“0x01”到“0x05”路由区对应同一个GGSN时，可以使用该命令来简化[**ADD IPV4DNSH**](../../DNS/DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md)配置。
  ADD AREADNS: DNTYPE=GGSN/PGW_RAI, LAC="0x02", RAC="0x01", RACRANGE="0x05", ZONESW=YES, ZONENAME="Z001";
  ADD IPV4DNSH:HSINDEX=1020, HOSTNAME="HUaWei158.Z001.MNC003.MCC460.GPRS", ADDRSECTION=SECTION1, IPV4ADDR1="10.10.10.10";
4. 当“0x0001”到“0x0005”位置区对应同一个GGSN时，可以使用该命令来简化[**ADD IPV4DNSH**](../../DNS/DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md)配置。
  ADD AREADNS: DNTYPE=GGSN/PGW_LAI, LAC="0x0001", LACRANGE="0005", ZONESW=YES, ZONENAME="Z001";
  ADD IPV4DNSH:HSINDEX=1020, HOSTNAME="HUaWei158.Z001.MNC003.MCC460.GPRS", ADDRSECTION=SECTION1, IPV4ADDR1="10.10.10.10";
5. 查询“MME组识别码”为“8002”的MME节点时，可以使用该命令来简化[**ADD DNSN**](../../DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md)配置。
  ADD MMEID:MCC="460", MNC="03", MMEGI="8002", MMEC="66";
  ADD IPV4DNSH:HSINDEX=100, HOSTNAME="MMEC66.MMEGI8002.MME.EPC.MNC003.MCC460.3GPPNETWORK.ORG", ADDRSECTION=SECTION1, IPV4ADDR1=" 10.141.149.100 ";
  ADD DNSN:FQDN="MMEC66.MMEGI8002.MME.EPC.MNC003.MCC460.3GPPNETWORK.ORG", HSINDEX=100, ENTITY=MME, INTYPE=S10, PRIORITY=0, WEIGHT=100;
6. 当“0x0001”到“0x0022”的跟踪区和值为"128"的UE USAGE TYPE对应同一个SGW时，可以使用该命令来简化[**ADD DNSN**](../../DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md)配置。
  ADD AREADNS: DNTYPE=SGW_TAI_UUT, TAC="0x0001", TACRANGE="0x0022", UUT=128, ZONESW=NO;
  ADD IPV4DNSH:HSINDEX=100, HOSTNAME="MMEC66.MMEGI8002.MME.EPC.MNC003.MCC460.3GPPNETWORK.ORG", ADDRSECTION=SECTION1, IPV4ADDR1=" 10.141.149.100 ";
  ADD DNSN:FQDN="MMEC66.MMEGI8002.MME.EPC.MNC003.MCC460.3GPPNETWORK.ORG", HSINDEX=100, ENTITY=SGW, INTYPE=S11;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-AREADNS.md`
