---
id: UNC@20.15.2@MMLCommand@ADD CHGCG
type: MMLCommand
name: ADD CHGCG（增加CG配置参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CHGCG
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 16
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 计费控制
status: active
---

# ADD CHGCG（增加CG配置参数）

## 功能

**适用网元：SGSN**

该命令用于配置与本端SGSN对接的CG需满足的相关参数。

SGSN与CG对接时，需要配置该命令。

## 注意事项

- 该命令执行后立即生效。
- 此表最大记录数为16。
- “GTP承载协议（PRO）”、“CG的IP地址（IP）”和“CG接收端口号（SPN）”唯一确定一条记录。
- 只有在本命令中配置的CG，才能在[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)、[**ADD CHGBEHA**](../计费行为参数配置/增加计费行为参数(ADD CHGBEHA)_26145366.md)和[**ADD CHGPLMNCG**](../PLMN CG 配置/增加PLMN-CG配置参数（ADD CHGPLMNCG）_72225067.md)中生效。
- 不同命令配置的CG优先级从高到低的次序是：[**ADD CHGPLMNCG**](../PLMN CG 配置/增加PLMN-CG配置参数（ADD CHGPLMNCG）_72225067.md)，[**ADD CHGBEHA**](../计费行为参数配置/增加计费行为参数(ADD CHGBEHA)_26145366.md)，[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)，[**ADD CHGCG**](增加CG配置参数（ADD CHGCG）_72225055.md)。
- 当[**SET CHGCDR**](设置计费CDR参数（SET CHGCDR）_26145372.md)中配置“PLMNCG范围扩展（EXTRANGE）”为“NO”时，[**ADD CHGPLMNCG**](../PLMN CG 配置/增加PLMN-CG配置参数（ADD CHGPLMNCG）_72225067.md)中配置的CGIP，其在本命令中的“缺省CG（DEFAULTCG）”必须为“NO”。
- CG上支持接入的GA链路条数有规格限制，不能超过“CG上2G类型的AP数量 * 300”，配置GA链路前，需要联系华为工程师提前规划GA链路总数。CG上2G类型的AP数量可以通过**[**LST MODULE**](../../../NCG业务及策略管理/计费管理/业务配置管理/业务模块/查询业务模块（LST MODULE）_51174292.md)**命令查询。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于标识与本端SGSN连接的CG的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4(IPV4地址)”<br>- “IPV6(IPV6地址)”<br>默认值：“IPV4(IPV4地址)” |
| IP | CG的IPV4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于标识与本端SGSN连接的CG的IPV4地址。<br>前提条件：该参数在<br>“IPT(IP地址类型)”<br>配置为<br>“IPV4(IPV4地址)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 有效的IPV4地址不能为环回地址（127.x.y.z）。<br>- 有效的IPV4地址必须是A、B或者C类地址。 |
| IPV6 | CG的IPV6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于标识与本端SGSN连接的CG的IPV6地址。<br>前提条件：该参数在<br>“IPT(IP地址类型)”<br>配置为<br>“IPV6(IPV6地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPV6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| GRD | 优先级 | 可选必选说明：条件可选参数<br>参数含义：该参数用于标识CG的优先级。SGSN首先向高优先级的CG发送话单，高优先级的CG不可达后，选择次高优先级的CG发送。对于优先级别相同的CG，同一个用户的话单每次都发往相同的CG，不同用户的话单发送时则会轮选CG。<br>前提条件：该参数在<br>“DEFAULTCG”<br>设置为<br>“YES（是）”<br>时生效。<br>数据来源：整网规划<br>取值范围：0~11<br>默认值：0<br>配置原则：0为最高等级，11为最低等级。 |
| PRO | GTP承载协议 | 可选必选说明：必选参数<br>参数含义：该参数用于标识CG支持的GTP'承载协议。<br>数据来源：整网规划<br>取值范围：<br>- “UDP(UDP)”：表示SGSN和CG之间通过UDP/IP进行通讯。<br>- “TCP(TCP)”：表示SGSN和CG之间通过TCP/IP进行通讯。<br>默认值：无<br>说明：本版本暂不支持将<br>“GTP承载协议（PRO）”<br>设置为<br>“TCP(TCP)”<br>。 |
| CGR | CG协议版本 | 可选必选说明：必选参数<br>参数含义：该参数用于标识CG支持的协议版本。<br>数据来源：整网规划<br>取值范围：<br>- “R98(R98)”：表示CG支持的协议版本为R98。<br>- “R99(R99)”：表示CG支持的协议版本为R99。<br>- “R4(R4)”：表示CG支持的协议版本为R4。<br>- “R5(R5)”：表示CG支持的协议版本为R5。<br>- “R6(R6)”：表示CG支持的协议版本为R6。<br>- “R7(R7)”：表示CG支持的协议版本为R7。<br>- “R9(R9)”：表示CG支持的协议版本为R9。<br>默认值：无<br>配置原则：<br>- 对于GPRS，可以使用R98、R99、R4、R5、R6、R7和R9协议版本的CG。<br>- 对于WCDMA，可以使用R99、R4、R5、R6、R7和R9协议版本的CG。 |
| SPN | CG接收端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于标识UDP类型CG的SGSN消息所要发往的端口号（亦即UDP类型CG的接收端口号）或TCP类型CG的侦听端口号。<br>数据来源：整网规划<br>取值范围：1024~65535<br>默认值：3386<br>配置原则：<br>- 与对端CG网元的设置保持一致。<br>- 具有相同IP地址的UDP CG之间的“CG接收端口号”不能相同。<br>- 具有相同IP地址的TCP CG之间的“CG接收端口号”不能相同。<br>- 具有相同IP地址的UDP CG和TCP CG之间的“CG接收端口号”不能相同。 |
| DEFAULTCG | 缺省CG | 可选必选说明：可选参数<br>参数含义：该参数用于控制当PLMN CG（<br>[**ADD CHGPLMNCG**](../PLMN CG 配置/增加PLMN-CG配置参数（ADD CHGPLMNCG）_72225067.md)<br>），计费行为CG（<br>[**ADD CHGBEHA**](../计费行为参数配置/增加计费行为参数(ADD CHGBEHA)_26145366.md)<br>），计费属性CG（<br>[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)<br>）推荐CG都不可用的情况下，是否选择缺省CG。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“YES（是）”<br>配置原则：<br>- 当[**SET CHGCDR**](设置计费CDR参数（SET CHGCDR）_26145372.md)中配置“PLMNCG范围扩展（EXTRANGE）”为“NO”时，[**ADD CHGPLMNCG**](../PLMN CG 配置/增加PLMN-CG配置参数（ADD CHGPLMNCG）_72225067.md)中配置的CGIP，其在本命令中的“缺省CG（DEFAULTCG）”必须为“NO”。<br>- 当PLMN CG（[**ADD CHGPLMNCG**](../PLMN CG 配置/增加PLMN-CG配置参数（ADD CHGPLMNCG）_72225067.md)），计费行为CG（[**ADD CHGBEHA**](../计费行为参数配置/增加计费行为参数(ADD CHGBEHA)_26145366.md)），计费属性CG（[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)）和推荐CG都不可用的情况下，该参数需配置为“YES”，否则话单将存储在硬盘。 |
| CGN | CG名 | 可选必选说明：可选参数<br>参数含义：该参数用于标识CG的名称。<br>数据来源：整网规划<br>取值范围：1~32位字符串<br>默认值：noname |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGCG]] · CG配置参数（CHGCG）

## 关联任务

- [[UNC@20.15.2@Task@0-00017]]

## 使用实例

1. 增加一个CG的配置，IP地址类型为IPV4，CG的IPV4地址为172.22.5.50，优先级为0，GTP承载协议为UDP，CG协议版本为R98，CG接收端口号为3386，CG名为 “xx” ：
  ADD CHGCG: IPT=IPV4, IP="172.22.5.50", PRO=UDP, CGR=R98, SPN=3386, DEFAULTCG=YES, GRD=0, CGN="xx";
2. 增加一个CG的配置，IP地址类型为IPV4，CG的IPV4地址为172.22.5.42，优先级为1，GTP承载协议为UDP，CG协议版本为R4，CG接收端口号为3386，CG名为 “yy” ：
  ADD CHGCG: IPT=IPV4, IP="172.22.5.42", PRO=UDP, CGR=R4, SPN=3386, DEFAULTCG=YES, GRD=1, CGN="yy";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加CG配置参数（ADD-CHGCG）_72225055.md`
