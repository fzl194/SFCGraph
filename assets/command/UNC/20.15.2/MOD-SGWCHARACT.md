---
id: UNC@20.15.2@MMLCommand@MOD SGWCHARACT
type: MMLCommand
name: MOD SGWCHARACT（修改S-GW特性对接配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SGWCHARACT
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
- S11接口管理
- S-GW属性
status: active
---

# MOD SGWCHARACT（修改S-GW特性对接配置）

## 功能

**适用网元：SGSN、MME**

该命令用于修改MME与S-GW支持特性的能力交互配置策略。

## 注意事项

- 该命令执行后立即生效。
- “对端设备范围”、“IP地址类型”、“IPv4地址”、“IPV4地址掩码”、“IPv6地址”、“IPV4地址掩码”这几个参数不能通过该命令修改。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 对端设备范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要特性能力相互通知的对端设备S-GW范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL(所有S-GW)”<br>- “SPECIFIED(指定S-GW)”<br>默认值：无<br>配置原则：<br>- “ALL(所有S-GW)”为系统的缺省记录，不允许增加，也不允许删除，但可以修改。<br>- 配置记录的优先级关系：“SPECIFIED(指定S-GW)”高于“ALL(所有S-GW)”。 |
| IPT | IP地址类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定S-GW信令面IP地址类型。<br>前提条件：该参数在<br>“对端设备范围”<br>参数配置为<br>“SPECIFIED(指定S-GW)”<br>后生效。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定S-GW信令面IPv4地址，系统中可以配置多条<br>“SPECIFIED(指定S-GW)”<br>的记录，但是IP网段区间不能相同，允许包含关系。当存在包含关系的IP网段记录时，以目标IP地址落入的最小IP网段记录为准。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“IPV4(IPV4)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.1~255.255.255.254<br>默认值：无<br>配置原则：<br>- 有效的IPv4地址不能为环回地址(127.x.y.z)。<br>- 有效的IPv4地址必须是A、B或者C类地址。 |
| IPV4MSK | IPV4地址掩码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端S-GW的信令面IPv4地址的掩码。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“IPV4(IPV4)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.1~255.255.255.255<br>默认值：无<br>配置原则：<br>- 输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定S-GW信令面IPv6地址，系统中可以配置多条<br>“SPECIFIED(指定S-GW)”<br>的记录，但是IP网段区间不能相同，允许包含关系。当存在包含关系的IP网段记录时，以目标IP地址落入的最小IP网段记录为准。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“IPV6(IPV6)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| IPV6MSK | IPV6地址前缀长度 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IPv6地址的子网前缀的长度。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“IPV6(IPV6)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0~128<br>默认值：无<br>配置原则：0是无效掩码。 |
| NTSR | S-GW支持NTSR功能 | 可选必选说明：可选参数<br>参数含义：该参数用于设置S-GW是否支持NTSR功能。<br>数据来源：对端协商<br>取值范围：<br>- "YES(支持)"<br>- "NO(不支持)"<br>默认值：无<br>配置原则：<br>- “MME链式备份”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-201201，license部件编码：LKV2MCR01）<br>- 参数设置为“支持”时，发送给对应S-GW的Echo Request/Echo Respone消息的“Node Feature”信元中“NTSR”比特设置为1。<br>- 参数设置为“不支持”时，发送给对应S-GW的Echo Request/Echo Respone消息的“Node Feature”信元中“NTSR”比特设置为0。<br>- 当“Node Feature”信元所有bit为0，Echo Request/Echo Respone消息将不携带该信元。 |
| PRN | S-GW支持PRN功能 | 可选必选说明：可选参数<br>参数含义：该参数用于设置S-GW是否支持PRN功能。<br>数据来源：对端协商<br>取值范围：<br>- "YES(支持)"<br>- "NO(不支持)"<br>默认值：无<br>配置原则：<br>- “S-GW/P-GW故障下的业务恢复”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-201203，license部件编码：LKV2SRGF01）<br>- 参数设置为“支持”时，发送给对应S-GW的Echo Request/Echo Respone消息的“Node Feature”信元中“PRN”比特设置为1。<br>- 参数设置为“不支持”时，发送给对应S-GW的Echo Request/Echo Respone消息的“Node Feature”信元中“PRN”比特设置为0。<br>- 当“Node Feature”信元所有bit为0，Echo Request/Echo Respone消息将不携带该信元。 |
| MMEID | S-GW支持MME ID | 可选必选说明：可选参数<br>参数含义：该参数用于设置S-GW是否支持MME ID信元。<br>数据来源：对端协商<br>取值范围：<br>- "YES(支持)"<br>- "NO(不支持)"<br>默认值：无<br>配置原则：<br>- “S-GW/P-GW故障下的业务恢复”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-201203，license部件编码：LKV2SRGF01）<br>- 参数设置为“支持”，发送给对应S-GW的Create Session Request/Modify Bearer Request消息携带“MME ID”信元。<br>- 参数设置为“不支持”，发送给对应S-GW的Create Session Request/ModifyBearer Request消息不携带“MME ID”信元。 |
| SECRATRPT | S-GW支持Secondary RAT Usage Data Report | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否在MME发送给对应S-GW的Modify Bearer Request、Delete Session Request、Delete Bearer Response、Delete Bearer Command、Release Access Bearers Request、Change Notification Request等消息中携带“Secondary RAT Usage Data Report”信元。<br>数据来源：全网规划<br>取值范围：<br>- "NO（不支持）"<br>- "YES（支持）"<br>默认值：无 |
| GTPUIPPLCY | GTPU IP类型选择策略 | 可选必选说明：可选参数<br>参数含义：该参数用于在MME用户面同时支持IPv4与IPv6地址的场景下，指定与SGW之间的用户面IP地址类型选择策略。<br>数据来源：对端协商<br>取值范围：<br>- IPV4PRE(与SGW之间的用户面IP地址类型优先选择IPv4地址类型)<br>- IPV6PRE(与SGW之间的用户面IP地址类型优先选择IPv6地址类型)<br>- GTPCPRE(与SGW之间的用户面IP地址类型优先选择与控制面地址类型相同)<br>默认值：无<br>配置原则：<br>- S-GW的S11U地址仅支持IPv4地址，则IP地址类型优先选择IPv4地址类型。<br>- S-GW的S11U地址仅支持IPv6地址，则IP地址类型优先选择IPv6地址类型。<br>- S-GW的S11U地址支持IPv4和IPv6地址，则IP地址类型优先选择与控制面地址类型相同的IP。<br>说明：该参数仅在<br>[**SET SMFUNC**](../../../业务安全管理/会话管理/SM扩展功能管理/设置会话管理扩展功能(SET SMFUNC)_26145684.md)<br>中<br>“LTEUSERPLCYSW”<br>配置为<br>“YES”<br>时生效。 |
| ULIFORSGW | S-GW支持User Location Information For S-GW | 可选必选说明：可选参数<br>参数含义：该参数用于设置S-GW是否支持User Location Information For S-GW信元。<br>数据来源：对端协商<br>取值范围：<br>- "NO（不支持）"<br>- "YES（支持）"<br>默认值："NO（不支持）"<br>配置原则：<br>- 参数设置为“YES(支持)”，发送给对应S-GW的Create Session Request/Modify Bearer Request消息携带该信元。<br>- 参数设置为“NO(不支持)”，发送给对应S-GW的Create Session Request/Modify Bearer Request消息不携带该信元。 |
| PSCELLIDCSR | S-GW支持CSR消息携带PSCell ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定在MME给对端S-GW发送的Create Session Request消息中是否支持携带“PSCell ID”信元。<br>数据来源：全网规划<br>取值范围：<br>- "NO（不支持）"<br>- "YES（支持）"<br>默认值："NO（不支持）"<br>配置原则：NSA用户在本地有PSCell Information信息，且有双连接时，希望对端SGW支持Create Session Request消息中携带PSCell ID信元，设置本参数为“YES（支持）”；否则设置本参数为“NO（不支持）”。<br>说明：23401协议中有描述需要携带给SGW，但是29274(i00)协议未在Create Session Request消息中添加该信元，因此在协议未更新前属于私有实现，只有对接华为的SGW才允许打开。 |
| PSCELLID | S-GW支持PSCell ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否在MME发送给对端S-GW的Create Bearer Response、Bearer Resource Command、Modify Bearer Request、Delete Session Request、Delete Bearer Response、Update Bearer Response、Delete Bearer Command、Release Access Bearers Request、Change Notification Request消息中支持携带“PSCell ID”信元。<br>数据来源：全网规划<br>取值范围：<br>- "NO（不支持）"<br>- "YES（支持）"<br>默认值："NO（不支持）"<br>配置原则：如果对端SGW支持PSCell ID信元，设置本参数为“YES（支持）”；否则设置本参数为“NO（不支持）”。 |
| PGWRNSI | S-GW支持PGWRNSI | 可选必选说明：可选参数<br>参数含义：该参数用于设置S-GW是否支持PGWRNSI(PGW Redirection due to mismatch with Network Slice subscribed by UE Support Indication)功能<br>数据来源：全网规划<br>取值范围：<br>- "NO（不支持）"<br>- "YES（支持）"<br>默认值："NO（不支持）"<br>配置原则：<br>- 如果对端SGW支持PGWRNSI功能，设置本参数为“YES（支持）”；否则设置本参数为“NO（不支持）”。<br>- 参数设置为“支持”时，发送给对应S-GW的Create Session Request消息的“Indication Flags”信元中“PGWRNSI”比特设置为1。说明：启用PGW重定向功能后，无法保证P-GW和S-GW拓扑合一。 |
| PCSCFRESTOIND | S-GW支持P-CSCF Restoration Indication | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否在MME发送给对端S-GW的Modify Bearer Request消息中支持indication Flags信元内的“P-CSCF Restoration Indication”标志位。<br>数据来源：全网规划<br>取值范围：<br>- "NO（不支持）"<br>- "YES（支持）"<br>默认值："NO（不支持）"<br>配置原则：<br>- “ 基于HSS的P-CSCF故障恢复”特性的相关License授权并开启后，此参数配置才生效（特性编号：WSFD-201205，License部件编码：LKV2FRPH02）<br>- 如果对端S-GW支持“P-CSCF Restoration Indication”标志位，才设置本参数为“YES（支持）”；否则设置本参数为“NO（不支持）”。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述信息。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [S-GW特性对接配置（SGWCHARACT）](configobject/UNC/20.15.2/SGWCHARACT.md)

## 使用实例

该命令用于修改MME与S-GW支持特性的能力交互配置策略，执行此命令：

MOD SGWCHARACT: RANGE=SPECIFIED, IPT=IPV4, IPV4="10.95.69.96", IPV4MSK="255.255.255.0", NTSR=YES, PRN=NO, MMEID=YES, SECRATRPT=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改S-GW特性对接配置(MOD-SGWCHARACT)_26145970.md`
