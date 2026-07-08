---
id: UNC@20.15.2@MMLCommand@ADD SBCAPLE
type: MMLCommand
name: ADD SBCAPLE（增加SBCAP本地实体）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SBCAPLE
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
- SBCAP本地实体
status: active
---

# ADD SBCAPLE（增加SBCAP本地实体）

## 功能

**适用网元：MME**

此命令用于增加SBc链路本地实体，配置SBc链路本地实体名称，本端点的IP地址类型等信息。涉及小区广播服务特性。

此命令在配置MME作为服务器端的SBc链路时使用。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为128。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LLEINDEX | 本端实体号 | 可选必选说明：必选参数<br>参数含义：该参数用于在系统范围内部唯一标识一条SBc链路本地实体号。<br>数据来源：本端规划<br>取值范围：0～127<br>默认值：无 |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SBCAP本端端点的IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：<br>“IPV4(IPv4)”<br>配置原则：系统目前仅支持IPV4地址。 |
| LOCALIPV4_1 | 本地IPv4地址1 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定MME侧SBCAP本端端点的第一个IP地址。<br>前提条件：<br>- 在UNCMML窗口上执行命令[**ADD SERVICEIP**](../../业务IP管理/业务IP/增加业务IP(ADD SERVICEIP)_26306178.md)设置此参数。<br>- “IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>- 对于多归属（即一个端点可能有多个IP地址）配置，需要配置“本地IPv4地址1”、“本地IPv4地址2”共两个IP地址。当“本地IPv4地址1”通信正常时，系统使用第一个IP地址；当“本地IPv4地址1”通信故障时，系统会自动切换到“本地IPv4地址2”通信。<br>- 若不采用多归属配置，不需要配置“本地IPv4地址2”。 |
| LOCALIPV4_2 | 本地IPv4地址2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME侧SBCAP本端端点的第二个IP地址。当<br>“本地IPv4地址1”<br>通信故障时，系统会自动切换到本参数指定的IP地址来与对端通信。<br>前提条件：<br>- 在UNC MML窗口上执行命令[**ADD SERVICEIP**](../../业务IP管理/业务IP/增加业务IP(ADD SERVICEIP)_26306178.md)设置此参数。<br>- “IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无 |
| LOCALIPV6_1 | 本地IPv6地址1 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定MME侧SBCAP本端端点的第一个IP地址。<br>前提条件：<br>- 在UNC MML窗口上执行命令[**ADD SERVICEIP**](../../业务IP管理/业务IP/增加业务IP(ADD SERVICEIP)_26306178.md)设置此参数。<br>- “IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- 对于多归属配置，需要配置“本地IPv6地址1”、“本地IPv6地址2”共两个IP地址。当“本地IPv6地址1”1通信正常时，系统使用第一个IP地址；当“本地IPv6地址1”通信故障时，系统会自动切换到“本地IPv6地址2”通信。<br>- 若不采用多归属配置，不需要配置“本地IPv6地址2”。 |
| LOCALIPV6_2 | 本地IPv6地址2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME侧SBCAP本端端点的第二个IP地址。当<br>“本地IPv6地址1”<br>通信故障时，系统会自动切换到本参数指定的IP地址来与对端通信。<br>前提条件：<br>- 在UNC MML窗口上执行命令[**ADD SERVICEIP**](../../业务IP管理/业务IP/增加业务IP(ADD SERVICEIP)_26306178.md)设置此参数。<br>- “IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| LOCALPORT | 本地端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端所使用的SCTP端口号<br>数据来源：整网规划<br>取值范围：1024~65534<br>默认值：29168<br>配置原则：该参数需要与对端网元配置的对端端口号保持一致。 |
| CROSSIPFLAG | 交叉路径是否可用 | 可选必选说明：可选参数<br>参数含义：该参数用于表明交叉路径是否可用。交叉路径是指本端第一个IP地址到对端第二个IP地址和本端第二个IP地址到对端第一个IP地址所组成的路径。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>配置原则：<br>- 交叉路径会增加组网的复杂度，建议配置为交叉路径不可用。<br>- SCTP双归属下配置交叉路径不可用时，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址1”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址2”两条路径可用，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址2”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址1”两条路径不可用。<br>- SCTP双归属下配置交叉路径可用时，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址1”，“本端IPv4(IPv6)地址1”与“对端IPv4(IPv6)地址2”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址1”，“本端IPv4(IPv6)地址2”与“对端IPv4(IPv6)地址2”四条路径均可用。 |
| SCTPINDX | SCTP协议参数索引 | 可选必选说明：必选参数<br>参数含义：该参数为SCTPPARA表的索引号，用于指定本SBc链路使用的SCTP协议栈参数。<br>前提条件：在UNC MML窗口上执行命令<br>[**ADD SCTPPARA**](../../信令传输管理/SCTP管理/增加SCTP协议参数(ADD SCTPPARA)_26306150.md)<br>设置此参数。<br>数据来源：整网规划<br>取值范围：0~65534<br>默认值：无 |
| LLENAM | 本端实体名称 | 可选必选说明：可选参数<br>参数含义：该参数用于链路本地实体名称，标识SBc链路。<br>数据来源：整网规划<br>取值范围：1～32位字符串<br>默认值：noname<br>配置原则：建议取有实际意义的名称，以方便识别。例如<br>“To-CBC0”<br>。 |
| VPNNAME | vpn名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN的名称。<br>数据来源：整网规划<br>前提条件：该参数取值必须与<br>[**ADD SERVICEIP**](../../业务IP管理/业务IP/增加业务IP(ADD SERVICEIP)_26306178.md)<br>的<br>“VPN实例名称”<br>参数取值保持一致。<br>说明：当<br>[**ADD SERVICEIP**](../../业务IP管理/业务IP/增加业务IP(ADD SERVICEIP)_26306178.md)<br>的<br>“VPN实例名称”<br>参数未配置时，该参数无需配置。<br>当<br>[**ADD SERVICEIP**](../../业务IP管理/业务IP/增加业务IP(ADD SERVICEIP)_26306178.md)<br>的<br>“VPN实例名称”<br>参数配置了有效值时，该参数必须配置。<br>取值范围：1～31位字符串<br>默认值：无<br>配置原则：建议取有实际意义的名称，以方便识别。例如<br>“To-CBC0”<br>。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SBCAPLE]] · SBCAP本地实体（SBCAPLE）

## 使用实例

1. 增加一个SBCAP本端实体，本端有一个IPv4地址：本端实体索引号为0，IP地址类型为IPv4，本地IP1为10.1.1.1，SCTP协议参数索引为0，本端实体名为toCBC0。
  ADD SBCAPLE:LLEINDEX=0, IPTYPE=IPV4, LOCALIPV4_1="10.1.1.1", SCTPINDX=0, LLENAM="toCBC0";
2. 增加一个SBCAP本端实体，本端有两个IPv4地址：本端实体索引号为1，IP地址类型为IPv4，本地IP1为10.1.1.2，本地IP2为10.1.1.3，SCTP协议参数索引为0，本端实体名为toCBC1。
  ADD SBCAPLE:LLEINDEX=1, IPTYPE=IPV4, LOCALIPV4_1="10.1.1.2", LOCALIPV4_2="10.1.1.3", SCTPINDX=0, LLENAM="toCBC1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SBCAPLE.md`
