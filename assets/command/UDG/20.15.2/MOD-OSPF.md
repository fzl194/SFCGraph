---
id: UDG@20.15.2@MMLCommand@MOD OSPF
type: MMLCommand
name: MOD OSPF（修改OSPF进程配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: OSPF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF进程配置
status: active
---

# MOD OSPF（修改OSPF进程配置）

## 功能

该命令用于修改OSPF特性的进程的相关配置。

![](修改OSPF进程配置（MOD OSPF）_50121158.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，如果指定修改OSPF路由器标识会导致OSPF邻接关系中断，且以前的信息将无法恢复；如果指定去使能OSPF共网段虚拟系统功能，会关闭此进程所有OSPF共网段接口。

## 注意事项

- 该命令执行后立即生效。
- 修改参数SCHEMAROUID会导致OSPF进程复位，去使能参数VIRTUALSYSFLAG会关闭此进程所有OSPF共网段接口，导致路由器之间的OSPF邻接关系中断。
- 设备的一个接口只能属于某一个OSPF进程。
- 如果指定了VPN实例，OSPF进程属于此实例，否则属于全局实例。进程实例不可更改，只能在第一次使能该进程时指定。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| SCHEMAROUID | 路由器标识 | 可选必选说明：可选参数<br>参数含义：路由器标识。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：<br>- 路由器的ID可以手工配置，如果没有通过命令指定ID号，系统会从当前接口的IP地址中自动选取一个作为路由器的ID号。其选择顺序是：优先从Loopback地址中选择最大的IP地址作为路由器的ID号，如果没有配置Loopback接口，则在接口地址中选取最大的IP地址作为路由器的ID号。 以下两种情况会进行Router ID的重新选取：（1）通过MOD OSPF命令重新配置OSPF的Router ID，并且重新启动OSPF进程。（2）原来被选举为系统的Router ID的IP地址被删除并且重新启动OSPF进程。<br>- 路由器的ID只能修改不能删除。<br>- 修改路由器的ID会导致OSPF进程复位。 |
| SILENTALLFLAG | 抑制接口收发OSPF报文 | 可选必选说明：可选参数<br>参数含义：禁止OSPF进程下所有接口收发OSPF报文标志。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| BFDALLINTFFLG | 使能BFD | 可选必选说明：可选参数<br>参数含义：配置OSPF进程下使能BFD特性。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| BFDRXCFGFLAG | 是否配置BFD最小接收报文间隔 | 可选必选说明：可选参数<br>参数含义：是否配置BFD最小接收报文间隔。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| BFDMINRXINTV | 接收BFD包的最小时间间隔（ms） | 可选必选说明：条件必选参数<br>前提条件：该参数在“BFDRXCFGFLAG”配置为“TRUE”时为必选参数。<br>参数含义：期望从对端接收BFD报文的最小接收间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000，单位是毫秒。<br>默认值：无 |
| BFDTXCFGFLAG | 是否配置BFD最小发送报文间隔 | 可选必选说明：可选参数<br>参数含义：是否配置BFD最小发送报文间隔。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| BFDMINTXINTV | 发送BFD包的最小时间间隔（ms） | 可选必选说明：条件必选参数<br>前提条件：该参数在“BFDTXCFGFLAG”配置为“TRUE”时为必选参数。<br>参数含义：向对端发送BFD报文的最小发送间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000，单位是毫秒。<br>默认值：无 |
| SCHEMABFDDETMUL | BFD检测乘数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定会话检测倍数，如果BFD会话在设置的检测周期内没有收到对端发来的BFD报文，则认为链路发生了故障，BFD会话的状态将会置为Down。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～50。<br>默认值：无 |
| FRRBINDINGFLAG | BFD会话与接口链路状态绑定标志 | 可选必选说明：可选参数<br>参数含义：是否将BFD会话状态与接口的链路状态进行绑定。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：配置此参数后，BFD会话状态与OSPF Auto FRR进行绑定。BFD检测到接口链路故障后，BFD会话状态会变为Down并触发系统进行快速重路由，将流量从故障链路切换到备份链路上，从而达到流量保护的目的。 |
| RFC1583COMPFLG | 兼容RFC1583 | 可选必选说明：可选参数<br>参数含义：使能兼容RFC1583的路由选择优先规则。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| ROUTAGFLAG | 配置VPN引入路由的tag值 | 可选必选说明：可选参数<br>参数含义：配置VPN引入路由的tag值。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| ROUTAG | VPN引入路由的tag值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ROUTAGFLAG”配置为“TRUE”时为必选参数。<br>参数含义：标识VPN引入路由的tag值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：缺省情况下，tag值的前面两个字节为固定的0xD000，后面的两个字节为本端BGP的AS号，例如，如果本端BGP的AS号为100，VPN引入路由的tag值默认为3489661028；如果BGP AS号大于65535默认tag值为0，需要手动配置tag值。 |
| BANDWIDTHREF | 计算链路开销参考值（Mbps） | 可选必选说明：可选参数<br>参数含义：计算链路开销时所依据的参考值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～2147483648，单位是兆比特每秒。<br>默认值：无 |
| RXMTLIMITENABLE | 使能最大重传数 | 可选必选说明：可选参数<br>参数含义：标志是否使能最大重传限制数。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| RETRANSLIMIT | 最大重传限制 | 可选必选说明：条件可选参数<br>前提条件：该参数在“RXMTLIMITENABLE”配置为“TRUE”时为可选参数。<br>参数含义：最大重传限制数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2～255。<br>默认值：无 |
| OPAQCAPFLG | Opaque LSA能力 | 可选必选说明：可选参数<br>参数含义：使能Opaque-LSA能力，从而OSPF进程可以生成Opaque LSA，并能从邻居设备接收Opaque LSA。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| DESCRIPTIONTEXT | 描述信息 | 可选必选说明：可选参数<br>参数含义：OSPF进程的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～80。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| LSAARRINTVFLAG | 取消使用智能定时器配置LSA接收的间隔时间 | 可选必选说明：可选参数<br>参数含义：取消使用智能定时器配置LSA接收的间隔时间。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| LSAARRINTV | 接收时间间隔（ms） | 可选必选说明：条件必选参数<br>前提条件：该参数在“LSAARRINTVFLAG”配置为“TRUE”时为必选参数。<br>参数含义：LSA被接收的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～10000，单位是毫秒。<br>默认值：无 |
| LSAARRMAXINTV | 接收最长间隔时间（ms） | 可选必选说明：条件必选参数<br>前提条件：该参数在“LSAARRINTVFLAG”配置为“FALSE”时为必选参数。<br>参数含义：接收OSPF LSA的最长间隔时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10000，单位是毫秒。<br>默认值：无 |
| LSAARRSTARINTV | 接收初始间隔时间（ms） | 可选必选说明：条件必选参数<br>前提条件：该参数在“LSAARRINTVFLAG”配置为“FALSE”时为必选参数。<br>参数含义：接收OSPF LSA的初始间隔时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1000，单位是毫秒。<br>默认值：无 |
| LSAARRHLDINTV | 接收基数间隔时间（ms） | 可选必选说明：条件必选参数<br>前提条件：该参数在“LSAARRINTVFLAG”配置为“FALSE”时为必选参数。<br>参数含义：接收OSPF LSA的基数间隔时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～5000，单位是毫秒。<br>默认值：无 |
| LSAORIGINSTFLAG | 是否指定LSA更新的时间间隔为0 | 可选必选说明：可选参数<br>参数含义：是否指定LSA更新的时间间隔为0，即取消LSA的5秒的更新时间间隔。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| LSAORIGINTV | 更新时间间隔（s） | 可选必选说明：条件可选参数<br>前提条件：该参数在“LSAORIGINSTFLAG”配置为“FALSE”时为可选参数。<br>参数含义：指定设置除OSPF Router LSA和Network LSA外LSA的更新间隔时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～10，单位是秒。<br>默认值：无 |
| LSAORIGMAXINTV | 更新最长间隔时间（ms） | 可选必选说明：条件可选参数<br>前提条件：该参数在“LSAORIGINSTFLAG”配置为“FALSE”时为可选参数。<br>参数含义：更新Router LSA和Network LSA的最长间隔时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10000，单位是毫秒。<br>默认值：无 |
| LSAORIGSTARINTV | 更新初始间隔时间（ms） | 可选必选说明：条件可选参数<br>前提条件：该参数在“LSAORIGINSTFLAG”配置为“FALSE”时为可选参数。<br>参数含义：更新Router LSA和Network LSA的初始间隔时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1000，单位是毫秒。<br>默认值：无 |
| LSAORIGHLDINTV | 更新基数间隔时间（ms） | 可选必选说明：条件可选参数<br>前提条件：该参数在“LSAORIGINSTFLAG”配置为“FALSE”时为可选参数。<br>参数含义：更新Router LSA和Network LSA的基数间隔时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～5000，单位是毫秒。<br>默认值：无 |
| VPNINSCAPSIMFLG | 去使能VPN路由环路检测 | 可选必选说明：可选参数<br>参数含义：禁止路由环路检测，直接进行路由计算。当在MCE（Multi-VPN-Instance CE）路由器上支持VPN多实例时，需要取消环路检查。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：TRUE：禁止路由环路检测。 FALSE：允许路由环路检测。 |
| STUBROUFLG | Stub路由器 | 可选必选说明：可选参数<br>参数含义：配置Stub路由器。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NoConfig：不配置。<br>- StubOnHand：配置Stub路由器。<br>- StubOnBoot：路由器在发生主备倒换过程中一段时间内保持为Stub路由器。<br>默认值：无<br>配置原则：<br>- Stub路由器通过增大该路由器所生成的LSA中的链路的度量值（65535），告知其它OSPF路由器不要使用这个Stub路由器来转发数据。<br>- 但由于度量值不是无穷大，因此仍然可以拥有一个到Stub路由器的路由。<br>- Stub路由器生成的Router LSA中，所有链路的度量值都设置为比较大。 |
| STUBROUSTUPINTV | On-Startup时间间隔（s） | 可选必选说明：条件可选参数<br>前提条件：该参数在“STUBROUFLG”配置为“StubOnBoot”时为可选参数。<br>参数含义：路由器在发生主备倒换过程中保持为Stub路由器的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～65535，单位是秒。<br>默认值：无 |
| STUBROUINCSTUB | 是否为Stub链路发布最大开销值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“STUBROUFLG”配置为“StubOnBoot” 或 “StubOnHand”时为可选参数。<br>参数含义：指定设备为Router LSA中的stub链路设置最大开销65535。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| SAFESYNCFLG | 安全同步 | 可选必选说明：可选参数<br>参数含义：配置安全同步。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| SPFINTVSEC | SPF计算间隔时间（s） | 可选必选说明：可选参数<br>参数含义：OSPF的SPF（最短路径优先）计算间隔时间。通过调节SPF的计算间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10，单位是秒。<br>默认值：无 |
| SPFINTVMILLISEC | SPF计算间隔时间（ms） | 可选必选说明：可选参数<br>参数含义：OSPF的SPF计算间隔时间。通过调节SPF的计算间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10000，单位是毫秒。<br>默认值：无 |
| SPFMAXINTERVAL | SPF计算最长间隔时间（ms） | 可选必选说明：可选参数<br>参数含义：通过智能定时器设置OSPF SPF计算的最长间隔时间。通过调节SPF的计算间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20000，单位是毫秒。<br>默认值：无 |
| SPFSTARTINTV | SPF计算初始间隔时间（ms） | 可选必选说明：可选参数<br>参数含义：指定通过智能定时器设置OSPF SPF计算的初始间隔时间。通过调节SPF的计算间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1000，单位是毫秒。<br>默认值：无 |
| SPFHOLDINTERVAL | SPF计算基数间隔时间（ms） | 可选必选说明：可选参数<br>参数含义：指定通过智能定时器设置OSPF SPF计算的基数间隔时间。通过调节SPF的计算间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～5000，单位是毫秒。<br>默认值：无 |
| RTTAGDISFLAG | 禁止使用tag检测环路 | 可选必选说明：可选参数<br>参数含义：禁止使用tag检测环路。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：TRUE：禁止标签环路检测。 FALSE：允许标签环路检测。 |
| ECAROUTEFLAG | 使能ECA路由类型 | 可选必选说明：可选参数<br>参数含义：为VPN使能的ECA路由类型。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| DOMAINNULLFLAG | 配置Domain ID为空 | 可选必选说明：可选参数<br>参数含义：设置该标志删除所有Domain ID配置。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| SUPPREACH | 使能可达性抑制 | 可选必选说明：可选参数<br>参数含义：使能可达性抑制。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| SPFCONSERVFLAG | SPF正常模式标志 | 可选必选说明：可选参数<br>参数含义：SPF正常模式标志。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| SHAMHELLOFLAG | 使能Sham-hello | 可选必选说明：可选参数<br>参数含义：OSPF特有特性，使能Sham-hello后，节点收到任何有效的OSPF报文，都保持活动状态。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| MPLSLDPAUTOCFG | 是否自动使能MPLS LDP功能 | 可选必选说明：可选参数<br>参数含义：是否使能指定OSPF进程下所有可建立OSPF邻居的接口自动使能MPLS LDP的功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- None：去使能。<br>- Enable：使能。<br>默认值：无 |
| VIRTUALSYSFLAG | OSPF共网段虚拟系统使能标志 | 可选必选说明：可选参数<br>参数含义：OSPF共网段虚拟系统使能标志。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：<br>- 进程下VIRTUALSYSFLAG和接口下VIRTUALSYSFLAG同时配置，共网段才能生效。<br>- 共网段生效后，DRPRI生效值自动变为0；网络中需要有至少一个非共网段接口。<br>- 进程下VIRTUALSYSFLAG默认使能。<br>- 去使能OSPF共网段虚拟系统功能，会关闭此进程所有OSPF共网段接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPF]] · OSPF进程配置（OSPF）

## 使用实例

修改OSPF进程1的Router id为10.1.1.1：

```
MOD OSPF: PROCID=1, SCHEMAROUID="10.1.1.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-OSPF.md`
