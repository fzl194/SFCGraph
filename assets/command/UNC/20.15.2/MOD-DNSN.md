---
id: UNC@20.15.2@MMLCommand@MOD DNSN
type: MMLCommand
name: MOD DNSN（修改DNS NAPTR记录）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DNSN
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- DNS
- DNS NAPTR管理
status: active
---

# MOD DNSN（修改DNS NAPTR记录）

## 功能

![](修改DNS NAPTR记录(MOD DNSN)_72345491.assets/notice_3.0-zh-cn_2.png)

本次修改可能会更新本主机名的其他关联记录。

**适用网元：SGSN、MME**

该命令用于修改 “FQDN” （全称标准规范域名）与网元接口的对应关系。

## 注意事项

- 该命令执行后立即生效。
- 本次修改可能会更新本主机名的其他关联记录。

## 权限

manage-ug
G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FQDN | FQDN | 可选必选说明：必选参数<br>参数含义：该参数用于标识由RAI、TAI、APN、MME等构建的域名，用来进行网元查询。详见命令<br>[**ADD DNSN**](增加DNS NAPTR记录(ADD DNSN)_72225569.md)<br>。<br>数据来源：整网规划<br>取值范围：1~255位字符串<br>默认值：无<br>说明：- 该参数同 “主机名索引”、“网元类型”、“接口类型”、“UE USAGE TYPE策略” 、“支持DCNR”、“融合PGW-C/SMF” 一起唯一确定一条记录，不能修改。<br>- FQDN不能以“.”开始，也不能以“.”结束。 |
| HSINDEX | 主机名索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定FQDN对应网元的索引。<br>数据来源：整网规划<br>取值范围：1~2048<br>默认值：无<br>说明：- 该参数同 “FQDN”、“网元类型”、“接口类型”、“UE USAGE TYPE策略”、“支持DCNR”、“融合PGW-C/SMF” 一起唯一确定一条记录，不能修改。 |
| ENTITY | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定接口网元的类型。<br>数据来源：整网规划<br>取值范围：<br>- “SGSN(SGSN)”<br>- “GGSN(GGSN)”<br>- “MME(MME)”<br>- “SGW(SGW)”<br>- “PGW(PGW)”<br>- “MSC(MSC)”<br>- “IWS(IWS)”<br>- “AMF(AMF)”<br>默认值：无<br>说明：- 该参数同 “FQDN”、“主机名索引”、“接口类型”、“UE USAGE TYPE策略” 、“支持DCNR”、“融合PGW-C/SMF”一起唯一确定一条记录，不能修改。 |
| INTYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定网元对应的接口类型。<br>数据来源：整网规划<br>取值范围：<br>- “Gn(Gn)”<br>- “Gp(Gp)”<br>- “S3(S3)”<br>- “S4(S4)”<br>- “S5(S5)”<br>- “S8(S8)”<br>- “S10(S10)”<br>- “S11(S11)”<br>- “S16(S16)”<br>- “Sv(Sv)”<br>- “S102(S102)”<br>- “Sdup(Sdup)”<br>- “N26(N26)”<br>默认值：无<br>说明：- 该参数同 “FQDN”、“主机名索引”、“网元类型”、“UE USAGE TYPE策略” 、“支持DCNR”、“融合PGW-C/SMF”一起唯一确定一条记录，不能修改。<br>- 当该配置数据用于链式备份网元寻址时，需要选Sdup枚举，Sdup接口华为私有接口，是MME和MME之间的接口，用于实现MME间的数据备份。 |
| S5PROTOCOL | S5接口协议类型 | 可选必选说明：可选参数<br>参数含义：该参数用来配置网元S-GW/P-GW的S5接口协议。<br>前提条件：该参数在<br>“ENTITY”<br>参数配置为<br>“SGW”<br>或<br>“PGW”<br>后为有效。<br>数据来源：整网规划<br>取值范围：<br>- “GTP(GTP)”<br>- “PMIP(PMIP)”<br>- “GTP_PMIP(GTP_PMIP)”<br>默认值：无 |
| S8PROTOCOL | S8接口协议类型 | 可选必选说明：可选参数<br>参数含义：该参数用来配置网元S-GW/P-GW的S8接口协议。<br>前提条件：该参数在<br>“ENTITY”<br>参数配置为<br>“SGW”<br>或<br>“PGW”<br>后为有效。<br>数据来源：整网规划<br>取值范围：<br>- “GTP(GTP)”<br>- “PMIP(PMIP)”<br>- “GTP_PMIP(GTP_PMIP)”<br>默认值：无 |
| UEUSGTYPEPLCY | UE USAGE TYPE策略 | 可选必选说明：必选参数<br>参数含义：该参数用来指定专用核心网选择时，查询对应网关是否需要携带UE USAGE TYPE。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“无”<br>配置原则：当DECOR功能开启，需要通过UE USAGE TYPE进行DNS查询时，将此参数配置为<br>“YES（是）”<br>的DNS NAPTR记录。当前特性支持使用UE USAGE TYPE查询的网元包括MME，SGW和PGW。使用DECOR功能需要开启DECOR基础功能特性（特性编号：WSFD-<br>208001<br>，license部件编码：LKV2DECOR00）和DECOR特性（特性编号：WSFD-<br>208002<br>，license部件编码：LKV2DECOR01）。<br>说明：- 该参数同 “FQDN”、“主机名索引”、“网元类型”、“接口类型” 、“支持DCNR”、“融合PGW-C/SMF”一起唯一确定一条记录，不能修改。 |
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用来指定UE USAGE TYPE群组标识。<br>前提条件：该参数在<br>“UE USAGE TYPE策略”<br>参数配置为<br>“是”<br>后生效。<br>数据来源：本端规划<br>取值范围：0~1023<br>默认值：无<br>配置原则：此参数已经通过<br>[**ADD UEUSGTYPEGP**](../../../业务安全管理/DCN管理/UE USAGE TYPE群组管理/增加UE USAGE TYPE群组(ADD UEUSGTYPEGP)_72225499.md)<br>进行UE Usage Type群组配置。 |
| DCNR | 支持DCNR | 可选必选说明：必选参数<br>参数含义：该参数用于控制是否支持DCNR接入。<br>数据来源：全网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>说明：- 该参数同 “FQDN”、“主机名索引”、“网元类型”、“接口类型”、“UE USAGE TYPE策略”、“融合PGW-C/SMF”一起唯一确定一条记录，不能修改。 |
| SMF | 融合PGW-C/SMF | 可选必选说明：必选参数<br>参数含义：该参数用于控制是否支持融合的PGW-C/SMF。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无<br>配置原则：该参数仅在<br>“网元类型”<br>配置为<br>“PGW”<br>时，才能配置为<br>“YES”<br>。<br>说明：- 该参数同 “FQDN”、“主机名索引”、“网元类型”、“接口类型”、“UE USAGE TYPE策略”、“支持DCNR”一起唯一确定一条记录，不能修改。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用来指定接口网元对应的优先级。<br>数据来源：整网规划<br>取值范围：0~65535<br>默认值：无<br>配置原则：优先级数值配置越小，代表优先级越高。 |
| WEIGHT | 权重 | 可选必选说明：可选参数<br>参数含义：该参数用来指定接口网元对应的权重。<br>数据来源：整网规划<br>取值范围：0~65535<br>默认值：无<br>配置原则：权重数值配置越大，代表权重越大。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述该命令的文字说明，目的是在配置的时候可以将对象属性、配置原因、背景等进行描述，以便在查询时能够在大量配置数据中清晰的掌握配置的原因。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNSN]] · DNS NAPTR记录（DNSN）

## 使用实例

修改FQDN为TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG，HSINDEX为100，网元类型为S-GW，接口类型为S11的一条NAPTR记录，将该记录接口协议类型修改为GTP_PMIP，UE USAGE TYPE群组标识改为2，优先级修改为2，权重修改为50，描述为到华为的SGW01：

MOD DNSN: FQDN="TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG", HSINDEX=100, ENTITY=SGW, INTYPE=S11, S5PROTOCOL=GTP_PMIP, S8PROTOCOL=GTP_PMIP, UEUSGTYPEPLCY=YES, UEUSGTYPEGPID=2, DCNR=NO, SMF=NO, PRIORITY=2, WEIGHT=50, DESC="To huawei SGW01";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-DNSN.md`
