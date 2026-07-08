# 查询N2接口SCTP链路状态(DSP N2SCTPLNK)

- [命令功能](#ZH-CN_CONCEPT_0000001107993874__1.4.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001107993874__1.4.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001107993874__1.4.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001107993874__1.4.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001107993874__1.4.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001107993874__1.4.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001107993874)

**适用NF：AMF**

此命令用于查询N2接口SCTP链路状态。

#### [注意事项](#ZH-CN_CONCEPT_0000001107993874)

此命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001107993874)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001107993874)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OUTPUTTYPE | 输出类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定输出类型。<br>取值范围：<br>- “SUMMARY（统计信息）”：统计信息<br>- “SCREEN（报告输出）”：报告输出，最多显示30000条记录。<br>默认值：“SUMMARY（统计信息）” |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询N2接口SCTP链路所在的RU名称。该参数可以通过<br>[DSP RU](../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：1~63位字符串<br>默认值 ：无 |
| PROCTYPE | 进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定N2接口SCTP链路的进程类型。<br>取值范围：<br>- “SGP(SGP)”<br>默认值：无 |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：待查询链路所在SGP的进程号。<br>取值范围： 0~11<br>默认值 ：无 |
| SCTPLEINDEX | SCTP本端实体标识 | 可选必选说明：可选参数<br>参数含义：待查询链路的本端实体标识。<br>取值范围： 0~1023<br>默认值 ：无<br>配置原则：无 |
| PLCYDSP | N2 SCTP链路查询策略 | 可选必选说明：可选参数<br>参数含义：指定查询链路的方式。<br>取值范围：<br>- CSDBINDIDX(指定N2 SCTP CSDB间接索引)：通过指定N2 SCTP CSDB间接索引查询链路。<br>- IPANDPORT(指定IP和PORT)：通过指定IP与端口号查询链路。<br>默认值 ：无<br>配置原则：如果想查询某一条链路时，两种查询方式均可以使用；如果希望查询到指定对端IP和端口号的所有链路时可以选择“IPANDPORT(指定IP和PORT)”，同时不输入本端的信息进行查询。 |
| CSDBINDIDX | N2 SCTP CSDB间接索引 | 可选必选说明：条件必选参数<br>参数含义：待查询链路的N2 SCTP CSDB间接索引。<br>前提条件：“N2 SCTP链路查询策略”参数设置为“CSDBINDIDX(指定N2 SCTP CSDB间接索引)”时，该参数有效。<br>取值范围：0~268435455<br>默认值 ：无 |
| IPTYPE | IP类型 | 可选必选说明：条件必选参数<br>参数含义：待查询链路的IP地址类型<br>前提条件：“N2 SCTP链路查询策略”参数设置为“IPANDPORT(指定IP和PORT)”时，该参数有效。<br>取值范围：<br>- IPV4(IPv4)<br>- IPV6(IPv6)<br>默认值 ：无 |
| PEERIPV4ADDR1 | 对端IPv4地址1 | 可选必选说明：条件必选参数<br>参数含义：待查询链路中gNodeB的第一个IP地址。<br>前提条件：“IP类型”参数设置为“IPV4(IPv4)”时，该参数有效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值 ：无 |
| PEERIPV4ADDR2 | 对端IPv4地址2 | 可选必选说明：可选参数<br>参数含义：待查询链路中gNodeB的第二个IP地址。<br>前提条件：“IP类型”参数设置为“IPV4(IPv4)”时，该参数有效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值 ：无<br>说明：当NGAPLNK为多归属时，必须配置此参数，否则此命令无法生效。 |
| PEERIPV6ADDR1 | 对端IPv6地址1 | 可选必选说明：条件必选参数<br>参数含义：待查询链路中gNodeB的第一个IP地址。<br>前提条件：“IP类型”参数设置为“IPV6(IPv6)”时，该参数有效。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值 ：无 |
| PEERIPV6ADDR2 | 对端IPv6地址2 | 可选必选说明：可选参数<br>参数含义：待查询链路中gNodeB的第二个IP地址。<br>前提条件：“IP类型”参数设置为“IPV6(IPv6)”时，该参数有效。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值 ：无<br>说明：当NGAPLNK为多归属时，必须配置此参数，否则此命令无法生效。 |
| PEERPORT | 对端端口号 | 可选必选说明：条件必选参数<br>参数含义：待查询链路中gNodeB的端口号。<br>前提条件：“N2 SCTP链路查询策略”参数设置为“IPANDPORT(指定IP和PORT)”时，该参数有效。<br>取值范围：0~65534<br>默认值 ：无 |
| LOCALIPV4ADDR1 | 本端IPv4地址1 | 可选必选说明：可选参数<br>参数含义：待查询链路中AMF侧SCTP本端端点的第一个IP地址。<br>前提条件：“IP类型”参数设置为“IPV4(IPv4)”时，该参数有效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值 ：无 |
| LOCALIPV4ADDR2 | 本端IPv4地址2 | 可选必选说明：可选参数<br>参数含义：待查询链路中AMF侧SCTP本端端点的第二个IP地址。<br>前提条件：“IP类型”参数设置为“IPV4(IPv4)”时，该参数有效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值 ：无<br>说明：当NGAPLNK为多归属时，必须配置此参数，否则此命令无法生效。 |
| LOCALIPV6ADDR1 | 本端IPv6地址1 | 可选必选说明：可选参数<br>参数含义：待查询链路中AMF侧SCTP本端端点的第一个IP地址。<br>前提条件：“IP类型”参数设置为“IPV6(IPv6)”时，该参数有效。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值 ：无 |
| LOCALIPV6ADDR2 | 本端IPv6地址2 | 可选必选说明：可选参数<br>参数含义：待查询链路中AMF侧SCTP本端端点的第二个IP地址。<br>前提条件：“IP类型”参数设置为“IPV6(IPv6)”时，该参数有效。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值 ：无<br>说明：当NGAPLNK为多归属时，必须配置此参数，否则此命令无法生效。 |
| LOCALPORT | 本端端口号 | 可选必选说明：可选参数<br>参数含义：待查询链路中AMF侧SCTP本端端点的端口号。<br>前提条件：“N2 SCTP链路查询策略”参数设置为“IPANDPORT(指定IP和PORT)”时，该参数有效。<br>取值范围：1024~65534<br>默认值 ：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001107993874)

查询所有N2接口SCTP链路状态，输出类型为统计信息，可以用如下命令：

DSP N2SCTPLNK: OUTPUTTYPE=SUMMARY;

```
%%DSP N2SCTPLNK: OUTPUTTYPE=SUMMARY;%%
RETCODE = 0  操作成功

操作结果如下
------------
        总的N2 SCTP链路数 = 1
     正常的N2 SCTP链路数  = 1
     故障的N2 SCTP链路数  = 1
    接入中的N2 SCTP链路数 = 1
(结果个数 = 1)

---    END 
```

查询N2接口SCTP链路状态，输出类型为报告输出，RU名称为LINK_SP_RU_0064，进程类型为SGP，进程号为0，可以用如下命令：

DSP N2SCTPLNK: OUTPUTTYPE=SCREEN, RUNAME="LINK_SP_RU_0064", PROCTYPE=SGP, PROCID=0;

```
%%DSP N2SCTPLNK: OUTPUTTYPE=SCREEN, RUNAME="LINK_SP_RU_0064", PROCTYPE=SGP, PROCID=0;%%
RETCODE = 0  操作成功

操作结果如下
------------
                 RU名称 = LINK_SP_RU_0064
              进程类型  = SGP
                进程号  = 0
       SCTP本端实体标识 = 9
            IP地址类型1 = IPV4
         gNodeB IP地址1 = 192.168.15.1
            IP地址类型2 = NULL
         gNodeB IP地址2 = NULL
           gNodeB端口号 = 2016
   N2 SCTP CSDB间接索引 = 720384
               链路状态 = CONNECTED
             DO Key类型 = 2549
             DO Key长度 = 4
             DO Key组号 = 4294967295
               DO Key值 = 20481
(结果个数 = 1)

---    END 
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001107993874)

| 输出项名称 | 输出项解释 |
| --- | --- |
| RU名称 | 查询出的SPU资源单元名。<br>取值范围：1~63位字符串 |
| 进程类型 | 查询出的N2 SCTP链路的进程类型。 |
| 进程号 | 查询出的N2 SCTP链路中SGP进程的进程号。 |
| SCTP本端实体标识 | 查询出的N2 SCTP链路的本端实体标识。 |
| IP地址类型1 | 查询出的N2 SCTP链路中gNodeB的IP地址1的类型。 |
| gNodeB IP地址1 | 查询出的N2 SCTP链路中gNodeB的IP地址1。 |
| IP地址类型2 | 查询出的N2 SCTP链路中gNodeB的IP地址2的类型。 |
| gNodeB IP地址2 | 查询出的N2 SCTP链路中gNodeB的IP地址2 |
| gNodeB端口号 | 查询出的N2 SCTP链路中gNodeB的端口号。 |
| N2 SCTP CSDB间接索引 | 查询出的N2 SCTP链路中CSDB的间接索引 |
| 链路状态 | 查询出的N2 SCTP链路的链路状态。<br>取值说明:<br>- “空”：表示该条链路处于空闲态。<br>- “正常”：表示该条链路状态正常。<br>- “接入中”：表示该条链路正在创建，已经建立好了SCTP链路，正在建立NGAP链路。<br>- “故障”：表示该条链路出现故障。 |
| DO Key类型 | 查询出的N2 SCTP链路的DO Key类型。 |
| DO Key长度 | 查询出的N2 SCTP链路的DO Key长度。 |
| DO Key组号 | 查询出的N2 SCTP链路的DO Key组号。 |
| DO Key值 | 查询出的N2 SCTP链路的DO Key值。 |
| 总的N2 SCTP链路数 | 查询出的N2 SCTP链路的总数。 |
| 正常的N2 SCTP链路数 | 查询出的N2 SCTP链路状态正常的链路数。 |
| 故障的N2 SCTP链路数 | 查询出的N2 SCTP链路状态故障的链路数。 |
| 接入中的N2 SCTP链路数 | 查询出的N2 SCTP链路状态接入中的链路数。 |
