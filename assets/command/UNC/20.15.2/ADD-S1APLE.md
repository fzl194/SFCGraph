---
id: UNC@20.15.2@MMLCommand@ADD S1APLE
type: MMLCommand
name: ADD S1APLE（增加S1AP本地实体）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: S1APLE
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 64
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1AP本地实体
status: active
---

# ADD S1APLE（增加S1AP本地实体）

## 功能

**适用网元：MME**

此命令用于增加S1AP链路本地实体。

此命令为S1口基本配置，在MME与eNodeB对接的时候必须配置。配置完S1AP本地实体后，需要eNodeB主动发起建链流程才能完成S1链路的建立。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为64。
- IP地址和vpn名称必须在SERVICEIP表中已经配置，可以用[**LST SERVICEIP**](../../业务IP管理/业务IP/查询业务IP(LST SERVICEIP)_72226047.md)查询。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LLEINDEX | 链路本地实体号 | 可选必选说明：必选参数<br>参数含义：该参数用于在系统范围内部唯一标识一条S1AP链路本地实体号。<br>数据来源：本端规划<br>取值范围：0～63<br>默认值：无 |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S1AP链路本端端点的IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “TPTADDR_TYPE_IPV4(IPv4)”<br>- “TPTADDR_TYPE_IPV6(IPv6)”<br>默认值：<br>“TPTADDR_TYPE_IPV4(IPv4)” |
| LOCALIPV4_1 | 本地IPv4地址1 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定MME侧S1AP本端端点的第一个IP地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPv4”<br>时，才有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>- 对于多归属（即一个端点可能有多个IP地址）配置，需要配置“本地IPv4地址1”、“本地IPv4地址2”共两个IP地址。当“本地IPv4地址1”通信正常时，系统使用第一个IP地址；当“本地IPv4地址1”通信故障时，系统会自动切换到“本地IPv4地址2”通信。<br>- 若不采用多归属配置，不需要配置“本地IPv4地址2”。 |
| LOCALIPV4_2 | 本地IPv4地址2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME侧S1AP本端端点的第二个IP地址。当<br>“本地IPv4地址1”<br>通信故障时，系统会自动切换到本参数指定的IP地址来与对端通信。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPv4”<br>时，才有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无 |
| LOCALIPV6_1 | 本地IPv6地址1 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定MME侧S1AP本端端点的第一个IP地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPv6”<br>时，才有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- 对于多归属配置，需要配置“本地IPv6地址1”、“本地IPv6地址2”共两个IP地址。当“本地IPv6地址1”1通信正常时，系统使用第一个IP地址；当“本地IPv6地址1”通信故障时，系统会自动切换到“本地IPv6地址2”通信。<br>- 若不采用多归属配置，不需要配置“本地IPv6地址2”。 |
| LOCALIPV6_2 | 本地IPv6地址2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME侧S1AP本端端点的第二个IP地址。当<br>“本地IPv6地址1”<br>通信故障时，系统会自动切换到本参数指定的IP地址来与对端通信。<br>前提条件：该参数在且<br>“IP地址类型”<br>设置为<br>“IPv6”<br>时，才有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| LOCALPORT | 本地端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME侧S1AP链路所使用的SCTP端口号。<br>数据来源：与对端eNodeB设备协商<br>取值范围：1024～65534<br>默认值：36412 |
| CROSSIPFLAG | 交叉路径是否可用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP双归属的交叉路径（指本端IP地址1和对端IP地址2或本端IP地址2和对端IP地址1组成的路径）是否可用。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>配置原则：<br>- 交叉路径会增加组网的复杂度，建议配置为交叉路径不可用。<br>- 对端eNodeB需配置两个IP地址，才能体现此功能。<br>- SCTP双归属下配置交叉路径不可用时，本端IPv4(IPv6)地址1与对端IPv4(IPv6)地址1、本端IPv4(IPv6)地址2与对端IPv4(IPv6)地址2两条路径可用，本端IPv4(IPv6)地址1与对端IPv4(IPv6)地址2、本端IPv4(IPv6)地址2与对端IPv4(IPv6)地址1两条路径不可用。<br>- SCTP双归属下配置交叉路径可用时，本端IPv4(IPv6)地址1与对端IPv4(IPv6)地址1、本端IPv4(IPv6)地址1与对端IPv4(IPv6)地址2、本端IPv4(IPv6)地址2与对端IPv4(IPv6)地址1、本端IPv4(IPv6)地址2与对端IPv4(IPv6)地址2四条路径均可用。 |
| SCTPINDEX | SCTP协议参数索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定S1AP链路所引用的SCTP协议参数索引。<br>前提条件：该参数已增加，参见<br>[**ADD SCTPPARA**](../../信令传输管理/SCTP管理/增加SCTP协议参数(ADD SCTPPARA)_26306150.md)<br>。<br>数据来源：整网规划<br>取值范围：0～65534<br>默认值：无 |
| LLNAME | 链路本地实体名 | 可选必选说明：可选参数<br>参数含义：该参数用于链路本地实体名称，标识S1AP链路。<br>数据来源：整网规划<br>取值范围：1～32位字符串<br>默认值：无<br>配置原则：建议取有实际意义的名称，以方便识别。例如<br>“To-eNodeB0”<br>。 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN名称。<br>数据来源：整网规划<br>取值范围：1～31位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1APLE]] · S1AP本地实体（S1APLE）

## 使用实例

1. 增加一条S1AP链路，本端有一个IPv4地址：该链路本地实体号为0，地址类型为IPv4，本地IP1为192.168.15.10，本地端口号为36412，SCTP协议参数索引为0，交叉路径是否可用选择NO，链路名为To-eNodeB0，VPN名称为_abc_。
  ADD S1APLE: LLEINDEX=0, IPTYPE=TPTADDR_TYPE_IPV4, LOCALIPV4_1="192.168.15.10", LOCALPORT=36412, CROSSIPFLAG=NO, SCTPINDEX=0, LLNAME="To-eNodeB0",VPNNAME="_abc_";
2. 增加一条S1AP链路，本端有一个IPv4地址：该链路本地实体号为1，地址类型为IPv4，本地IP1为192.168.28.10，本地端口号为36412，SCTP协议参数为0，交叉路径是否可用选择NO，链路名为To-eNodeB1，VPN名称为_abc_。
  ADD S1APLE:LLEINDEX=1, IPTYPE=TPTADDR_TYPE_IPV4, LOCALIPV4_1="192.168.28.10", LOCALPORT=36412, CROSSIPFLAG=NO, SCTPINDEX=0, LLNAME="To-eNodeB1",VPNNAME="_abc_";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加S1AP本地实体(ADD-S1APLE)_26146254.md`
