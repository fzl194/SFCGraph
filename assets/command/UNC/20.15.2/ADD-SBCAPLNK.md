---
id: UNC@20.15.2@MMLCommand@ADD SBCAPLNK
type: MMLCommand
name: ADD SBCAPLNK（增加SBc链路）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SBCAPLNK
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 128
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- SBc接口管理
- SBc链路
status: active
---

# ADD SBCAPLNK（增加SBc链路）

## 功能

**适用网元：MME**

该命令用于增加一条SBc链路。SBc链路是MME网元与CBC网元间的链路，涉及CBS特性。

该命令在配置MME作为客户端的SBc链路时使用。

## 注意事项

- 该命令执行后立即生效。
- 该表最大记录数为128。
- 链路配置在SGP进程上。
- 一个SGP进程最多支持8个SBc链路。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNKINDEX | 链路索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待添加的SBc链路的索引。<br>数据来源：本端规划<br>取值范围：0~127<br>默认值：无<br>配置原则：<br>- 此链路索引在系统范围内唯一。<br>- 建议从“0”开始顺序取值。 |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CBC IP和本地IP的地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：<br>“IPV4(IPv4)”<br>配置原则：系统目前仅支持IPV4地址。 |
| LOCALIPV4_1 | 本地IPv4地址1 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本地第一个IPv4类型的IP地址。<br>前提条件：<br>- 在UNCMML窗口上执行命令[**ADD SERVICEIP**](../../业务IP管理/业务IP/增加业务IP(ADD SERVICEIP)_26306178.md)设置此参数。<br>- “IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 采用多归属配置时，需要配置“本地IPv4地址1”、“本地IPv4地址2”、“对端IPv4地址1”和“对端IPv4地址2”共四个IP地址。当“本地IPv4地址1”与“对端IPv4地址1”通信正常时，系统使用第一个IP地址。当“本地IPv4地址1”与“对端IPv4地址1”通信故障时，系统会自动切换到“本地IPv4地址2”与“对端IPv4地址2”通信。<br>- 不采用多归属配置时，不需要配置“本地IPv4地址2”和“对端IPv4地址2”。 |
| LOCALIPV4_2 | 本地IPv4地址2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定本地第二个IPv4类型的IP地址。<br>前提条件：<br>- 在UNCMML窗口上执行命令[**ADD SERVICEIP**](../../业务IP管理/业务IP/增加业务IP(ADD SERVICEIP)_26306178.md)设置此参数。<br>- “IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| LOCALIPV6_1 | 本地IPv6地址1 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本地第一个IPv6类型的IP地址。<br>前提条件：<br>- 在UNCMML窗口上执行命令[**ADD SERVICEIP**](../../业务IP管理/业务IP/增加业务IP(ADD SERVICEIP)_26306178.md)设置此参数。<br>- “IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- 采用多归属配置时，需要配置“本地IPv6地址1”、“本地IPv6地址2”、“对端IPv6地址1”和“对端IPv6地址2”共四个IP地址。当“本地IPv6地址1”与“对端IPv6地址1”通信正常时，系统使用第一个IP地址。当“本地IPv6地址1”与“对端IPv6地址1”通信故障时，系统会自动切换到“本地IPv6地址2”与“对端IPv6地址2”通信。<br>- 不采用多归属配置时，不需要配置“本地IPv6地址2”和“对端IPv6地址2”。 |
| LOCALIPV6_2 | 本地IPv6地址2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定本地第二个IPv6类型的IP地址。<br>前提条件：<br>- 在UNCMML窗口上执行命令[**ADD SERVICEIP**](../../业务IP管理/业务IP/增加业务IP(ADD SERVICEIP)_26306178.md)设置此参数。<br>- “IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| LOCALPORT | 本地端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端所使用的SCTP端口号。数据来源：整网规划<br>取值范围：1024~65534<br>默认值：29168<br>配置原则：该参数需要与对端网元配置的对端端口号保持一致。 |
| PEERIPV4_1 | 对端IPv4地址1 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端第一个IPv4类型的IP地址。<br>前提条件：<br>- 在UNCMML窗口上执行命令[**ADD CBC**](../CBC配置/增加CBC(ADD CBC)_72226049.md)设置此参数。<br>- “IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：该地址必须与对端网元的<br>“本端IPv4地址1”<br>保持一致。 |
| PEERIPV4_2 | 对端IPv4地址2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定对端第二个IPv4类型的IP地址。<br>前提条件：<br>- 在UNCMML窗口上执行命令[**ADD CBC**](../CBC配置/增加CBC(ADD CBC)_72226049.md)设置此参数。<br>- “IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 该地址必须与对端网元的“本端IPv4地址2”保持一致。 |
| PEERIPV6_1 | 对端IPv6地址1 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端第一个IPv6类型的IP地址。<br>前提条件：<br>- 在UNCMML窗口上执行命令[**ADD CBC**](../CBC配置/增加CBC(ADD CBC)_72226049.md)设置此参数。<br>- “IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：该地址必须与对端网元的<br>“本端IPv6地址1”<br>保持一致。 |
| PEERIPV6_2 | 对端IPv6地址2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定对端第二个IPv6类型的IP地址。<br>前提条件：<br>- 在UNCMML窗口上执行命令[**ADD CBC**](../CBC配置/增加CBC(ADD CBC)_72226049.md)设置此参数。<br>- “IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- 该地址必须与对端网元的“本端IPv6地址2”保持一致。 |
| PEERPORT | 对端端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端所使用的SCTP端口号。数据来源：整网规划<br>取值范围：1024~65534<br>默认值：29168<br>配置原则：该参数需要与对端网元配置的本端端口号保持一致。 |
| SCTPINDX | SCTP协议参数索引 | 可选必选说明：必选参数<br>参数含义：该参数为SCTPPARA表的索引号，用于指定本SBc链路使用的SCTP协议栈参数。<br>前提条件：在<br>UNC<br>MML窗口上执行命令<br>[**ADD SCTPPARA**](../../信令传输管理/SCTP管理/增加SCTP协议参数(ADD SCTPPARA)_26306150.md)<br>此参数。<br>数据来源：整网规划<br>取值范围：0~65534<br>默认值：无 |
| CROSSIPFLAG | 交叉路径是否可用 | 可选必选说明：可选参数<br>参数含义：该参数用于表明交叉路径是否可用。交叉路径是指本端第一个IP地址到对端第二个IP地址和本端第二个IP地址到对端第一个IP地址所组成的路径。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>配置原则：<br>- 交叉路径会增加组网的复杂度，建议配置为交叉路径不可用。<br>- SCTP双归属下配置交叉路径不可用时，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址1”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址2”两条路径可用，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址2”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址1”两条路径不可用。<br>- SCTP双归属下配置交叉路径可用时，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址1”，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址2”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址1”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址2”四条路径均可用。 |
| LINKNAM | 链路名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SBc链路名称。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：noname<br>配置原则：建议取有实际意义的名称，以方便识别。例如<br>“To-CBC”<br>。 |
| VPNNAME | vpn名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN的名称。<br>前提条件：<br>- 在UNCMML窗口上执行命令[**ADD SERVICEIP**](../../业务IP管理/业务IP/增加业务IP(ADD SERVICEIP)_26306178.md)设置此参数。<br>数据来源：本端规划<br>取值范围：1~31位字符串<br>默认值：无 |

## 操作的配置对象

- [SBc链路（SBCAPLNK）](configobject/UNC/20.15.2/SBCAPLNK.md)

## 使用实例

1. 增加一条SBc链路，本端与对端均只有一个IPv4地址：地址类型为IPv4，本地IP1为10.10.10.10，对端IP1为10.10.10.11，本地端口号为29168，对端端口号为29168，SCTP协议参数索引为0，交叉路径是否可用选择NO。
  ADD SBCAPLNK:LNKINDEX=0, IPTYPE=IPV4, LOCALIPV4_1="10.10.10.10", LOCALPORT=29168, PEERIPV4_1="10.10.10.11", PEERPORT=29168, SCTPINDX=0, CROSSIPFLAG=NO;
2. 增加一条SBc链路，本端与对端均有两个IPv4地址：地址类型为IPv4，本地IP1为10.10.10.10，本地IP2为10.10.10.12，对端IP1为10.10.10.13，对端IP2为10.10.10.14，本地端口号为29168，对端端口号为29168，SCTP协议参数索引为0，交叉路径是否可用选择NO。
  ADD SBCAPLNK:LNKINDEX=1, IPTYPE=IPV4, LOCALIPV4_1="10.10.10.10", LOCALIPV4_2="10.10.10.12", LOCALPORT=29168, PEERIPV4_1="10.10.10.13", PEERIPV4_2="10.10.10.14", PEERPORT=29168, SCTPINDX=0, CROSSIPFLAG=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加SBc链路(ADD-SBCAPLNK)_72345973.md`
