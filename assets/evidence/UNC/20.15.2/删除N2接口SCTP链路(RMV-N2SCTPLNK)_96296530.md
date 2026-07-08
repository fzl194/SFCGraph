# 删除N2接口SCTP链路(RMV N2SCTPLNK)

- [命令功能](#ZH-CN_CONCEPT_0296296530__1.4.1.1)
- [注意事项](#ZH-CN_CONCEPT_0296296530__1.4.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0296296530__1.4.3.1)
- [参数说明](#ZH-CN_CONCEPT_0296296530__1.4.4.1)
- [使用实例](#ZH-CN_CONCEPT_0296296530__1.4.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0296296530)

**适用NF：AMF**

此命令用于删除N2接口SCTP链路。当希望触发重建N2接口SCTP链路时可以执行此命令。

#### [注意事项](#ZH-CN_CONCEPT_0296296530)

- 该命令执行后立即生效。
- 该命令在版本升级过程中禁止执行。
- 删除链路可能影响正在进行的业务。
- 当参数“N2 SCTP链路删除策略”选择“IPANDPORT(指定IP和PORT)”，且参数“本端IPv4地址1”、“本端IPv4地址2”、“对端IPv6地址1”、“对端IPv6地址2”、“本端端口号”均不输入时，标识所有到指定对端的链路均会被删除。

#### [操作用户权限](#ZH-CN_CONCEPT_0296296530)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0296296530)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待删除链路所在的RU名称。该参数可以通过<br>[DSP RU](../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：1~63位字符串<br>默认值 ：无<br>配置原则：RU名称、进程类型、进程号必须同时输入或同时不输入。 |
| PROCTYPE | 进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定N2接口SCTP链路的进程类型。<br>取值范围：<br>- “SGP(SGP)”<br>默认值：无<br>配置原则：RU名称、进程类型、进程号必须同时输入或同时不输入。 |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：待删除链路所在SGP的进程号。<br>取值范围： 0~11<br>默认值 ：无<br>配置原则：RU名称、进程类型、进程号必须同时输入或同时不输入。 |
| PLCYRMV | N2 SCTP链路删除策略 | 可选必选说明：必选参数<br>参数含义：指定删除链路的方式。<br>取值范围：<br>- CSDBINDIDX(指定N2 SCTP CSDB间接索引)：通过指定N2 SCTP CSDB间接索引删除链路。<br>- IPANDPORT(指定IP和PORT)：通过指定IP与端口号删除链路。<br>默认值 ：无<br>配置原则：如果想删除某一条链路时，两种删除方式均可以使用；如果希望删除到指定对端IP和端口号的所有链路时可以选择“IPANDPORT(指定IP和PORT)”，同时不输入本端的信息进行删除。 |
| CSDBINDIDX | N2 SCTP CSDB间接索引 | 可选必选说明：条件必选参数<br>参数含义：待删除链路的N2 SCTP CSDB间接索引。<br>前提条件：“N2 SCTP链路删除策略”参数需要设置为“CSDBINDIDX(指定N2 SCTP CSDB间接索引)”，参见“N2 SCTP链路删除策略”。<br>取值范围：0~268435455<br>默认值 ：无 |
| IPTYPE | IP类型 | 可选必选说明：条件必选参数<br>参数含义：待删除链路的IP地址类型<br>前提条件：“N2 SCTP链路删除策略”参数需要设置为“IPANDPORT(指定IP和PORT)”，参见“N2 SCTP链路删除策略”。<br>取值范围：<br>- IPV4(IPv4)<br>- IPV6(IPv6)<br>默认值 ：无 |
| PEERIPV4ADDR1 | 对端IPv4地址1 | 可选必选说明：条件必选参数<br>参数含义：待删除链路中gNodeB的第一个IP地址。<br>前提条件：“IP类型”参数需要设置为“IPV4(IPv4)”，参见“IP类型”。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值 ：无 |
| PEERIPV4ADDR2 | 对端IPv4地址2 | 可选必选说明：可选参数<br>参数含义：待删除链路中gNodeB的第二个IP地址。<br>前提条件：“IP类型”参数需要设置为“IPV4(IPv4)”，参见“IP类型”。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值 ：无<br>说明：当NGAPLNK为多归属时，必须配置此参数，否则此命令无法生效。 |
| PEERIPV6ADDR1 | 对端IPv6地址1 | 可选必选说明：条件必选参数<br>参数含义：待删除链路中gNodeB的第一个IP地址。<br>前提条件：“IP类型”参数需要设置为“IPV6(IPv6)”，参见“IP类型”。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值 ：无 |
| PEERIPV6ADDR2 | 对端IPv6地址2 | 可选必选说明：可选参数<br>参数含义：待删除链路中gNodeB的第二个IP地址。<br>前提条件：“IP类型”参数需要设置为“IPV6(IPv6)”，参见“IP类型”。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值 ：无<br>说明：当NGAPLNK为多归属时，必须配置此参数，否则此命令无法生效。 |
| PEERPORT | 对端端口号 | 可选必选说明：条件必选参数<br>参数含义：待删除链路中gNodeB的端口号。<br>前提条件：“N2 SCTP链路删除策略”参数需要设置为“IPANDPORT(指定IP和PORT)”，参见“N2 SCTP链路删除策略”。<br>取值范围：0~65534<br>默认值 ：无 |
| LOCALIPV4ADDR1 | 本端IPv4地址1 | 可选必选说明：可选参数<br>参数含义：待删除链路中AMF侧SCTP本端端点的第一个IP地址。<br>前提条件：“IP类型”参数需要设置为“IPV4(IPv4)”，参见“IP类型”。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值 ：无 |
| LOCALIPV4ADDR2 | 本端IPv4地址2 | 可选必选说明：可选参数<br>参数含义：待删除链路中AMF侧SCTP本端端点的第二个IP地址。<br>前提条件：“IP类型”参数需要设置为“IPV4(IPv4)”，参见“IP类型”。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值 ：无<br>说明：当NGAPLNK为多归属时，必须配置此参数，否则此命令无法生效。 |
| LOCALIPV6ADDR1 | 本端IPv6地址1 | 可选必选说明：可选参数<br>参数含义：待删除链路中AMF侧SCTP本端端点的第一个IP地址。<br>前提条件：“IP类型”参数需要设置为“IPV6(IPv6)”，参见“IP类型”。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值 ：无 |
| LOCALIPV6ADDR2 | 本端IPv6地址2 | 可选必选说明：可选参数<br>参数含义：待删除链路中AMF侧SCTP本端端点的第二个IP地址。<br>前提条件：“IP类型”参数需要设置为“IPV6(IPv6)”，参见“IP类型”。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值 ：无<br>说明：当NGAPLNK为多归属时，必须配置此参数，否则此命令无法生效。 |
| LOCALPORT | 本端端口号 | 可选必选说明：可选参数<br>参数含义：待删除链路中AMF侧SCTP本端端点的端口号。<br>前提条件：“N2 SCTP链路删除策略”参数需要设置为“IPANDPORT(指定IP和PORT)”，参见“N2 SCTP链路删除策略”。<br>取值范围：1024~65534<br>默认值 ：无 |

#### [使用实例](#ZH-CN_CONCEPT_0296296530)

删除N2 SCTP CSDB间接索引为2的N2 SCTP链路，可以用如下命令：

```
RMV N2SCTPLNK: PLCYRMV=CSDBINDIDX, CSDBINDIDX=2;
```
