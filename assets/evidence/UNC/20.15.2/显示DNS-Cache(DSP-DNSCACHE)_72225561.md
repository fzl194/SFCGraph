# 显示DNS Cache(DSP DNSCACHE)

- [命令功能](#ZH-CN_MMLREF_0000001172225561__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225561__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225561__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225561__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225561__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225561__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172225561__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225561)

**适用网元：SGSN、MME**

该命令用于查看DNS在各个进程上的Cache信息，以及HOSTFILE信息。DNS Cache是使用DNS服务器解析时查找到的域名和IP地址信息在系统中的缓存，用于快速解析域名。DNS Cache分为一级Cache和二级Cache。一级Cache保存在SPP进程上，二级Cache保存在添加了DNSLE（参见 [**ADD DNSLE**](../DNS本端实体管理/增加DNS实体绑定DNS Client IP(ADD DNSLE)_72225567.md) ）的SPU上对应的1号SGP进程上。HOSTFILE信息是通过 [**ADD IPV4DNSH**](../DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md) 、 [**ADD IPV6DNSH**](../DNS Hostfile管理/增加IPV6 DNS Hostfile记录(ADD IPV6DNSH)_26145886.md) 或 [**ADD DNSN**](../DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md) 配置的数据。

#### [注意事项](#ZH-CN_MMLREF_0000001172225561)

- 该命令执行后立即生效。
- 该命令只用于查询SPP或1号SGP进程。
- 该命令执行模糊查询时，执行的是分段查询。即从“起始输出索引”开始，向后查找“最大查找索引个数”。
- 该命令执行时，如缓存类型为L1CACHE，会查询到HOSTFILE信息。
- 该命令执行模糊查询时，如果查找到的结果较多，会导致OMP进程的CPU占用率短暂冲高，不建议频繁进行此类查询。
- 对于查询S-GW网元域名的结果信息，在一级Cache中只保存S4、S11接口信息；对于查询非APN域名的结果信息，在一级Cache中不保存GGSN、P-GW网元信息。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225561)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225561)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225561)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定<br>SPU<br>资源单元名。<br>数据来源：整网规划<br>取值范围：1~63 位字符串，通过<br>[**DSP RU**](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令获取。<br>默认值：无 |
| PROCESSNO | 进程号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指示查询的目的进程号，当<br>“Cache类型”<br>为<br>“L1CACHE(一级Cache)”<br>时，指对应的SPP进程号。<br>数据来源：整网规划<br>取值范围：0~20，通过<br>[**DSP PROCESSUSN**](../../../../../../平台服务管理/操作维护/VNFC公共功能管理/操作维护/系统调测/进程管理/查询USN进程信息(DSP PROCESSUSN)_11295773.md)<br>或者<br>[**DSP PROCESSLINK**](../../../../../../平台服务管理/操作维护/VNFC公共功能管理/操作维护/系统调测/进程管理/查询LINK进程信息(DSP PROCESSLINK)_11295772.md)<br>获取。<br>默认值：无 |
| CACHETYPE | Cache类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要查询的DNS Cache类型。<br>数据来源：整网规划<br>取值范围：<br>- “L1CACHE(一级Cache)”<br>- “L2CACHE(二级Cache)”<br>默认值：无 |
| DNSQUERYMODE | DNS查询方式 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指示DNS查询的类型。<br>前提条件：当<br>“Cache类型”<br>为<br>“L1CACHE(一级Cache)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- “AAAA/A(AAAA/A)”<br>- “NAPTR(NAPTR)”<br>默认值：无 |
| MATCHTYPE | DNS匹配方式 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指示DNS查询的匹配类型。<br>前提条件：当<br>“Cache类型”<br>为<br>“L1CACHE(一级Cache)”<br>时，此参数为必选参数。<br>数据来源：整网规划<br>取值范围：<br>- “EXACT_SEARCH（精确查找）”<br>- “FUZZY_SEARCH(模糊查找)”<br>默认值：EXACT_SEARCH（精确查找） |
| STRINDEX | 起始输出索引 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示起始查询的域名地址索引。<br>前提条件：当<br>“Cache类型”<br>为<br>“L1CACHE(一级Cache)”<br>并且<br>“DNS匹配方式”<br>为<br>“FUZZY_SEARCH(模糊查找)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：0~19999<br>默认值：0<br>说明：- 当“DNS查询方式”为“AAAA/A(AAAA/A)”时，最大的有效值为8191。<br>- 当“DNS查询方式”为“NAPTR(NAPTR)”时，最大的有效值为19999。 |
| MAXDSPNUM | 最大查询索引个数 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示基于起始查询索引的最大查找范围。<br>前提条件：当<br>“Cache类型”<br>为<br>“L1CACHE(一级Cache)”<br>并且<br>“DNS匹配方式”<br>为<br>“FUZZY_SEARCH(模糊查找)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：1~200<br>默认值：20 |
| DNSUF | 域名后缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示待查询的域名后缀。<br>前提条件：当<br>“Cache类型”<br>为<br>“L1CACHE(一级Cache)”<br>并且<br>“DNS匹配方式”<br>为<br>“FUZZY_SEARCH(模糊查找)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：1~255个字符<br>默认值：无 |
| DOMAINNAME | DOMAINNAME域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指示要查询的域名<br>数据来源：整网规划<br>取值范围：1~255个字符<br>默认值：无<br>配置原则：<br>- 按照协议RFC1035规定，域名最大有效字符数为253，并且每个Label最大长度为63个字节。<br>- 当“Cache类型”为“L1CACHE(一级Cache)”并且“DNS匹配方式”为“EXACT_SEARCH（精确查找）”或者“Cache类型”为“L2CACHE(二级Cache)”时，可选参数“DOMAINNAME域名”必须填写，否则查询失败。 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：此参数用于指定待查询的服务名称，可以通过<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>配置原则：DNS Cache分为一级Cache和二级Cache，一个Cache保存在SPP进程上，对应的VNFC为USN，二级Cache保存在1号SGP进程上，对应的VNFC为LINK。<br>- 如果要查询一类Cache，则SERVICETYPE需要填写USN的VNFC类型名称；<br>- 如果要查询二类Cache，则SERVICETYPE需要填写LINK的VNFC类型名称。 |
| ITERATIVEQUERY | 是否进行迭代查询 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制是否对待查询域名进行迭代查询以获取完整查询记录。<br>前提条件：当“Cache类型”为“L2CACHE(二级Cache)”时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：“NO（否）”<br>配置原则：如果查询NAPTR记录时，需要获取此NAPTR记录的完整查询树结果，请将本参数设置为“YES（是）”。<br>说明：- 迭代查询仅支持查询NAPTR记录，如果待查询域名为其他类型，则回退到非迭代查询方案。<br>- 在一次迭代查询全部完成之前，重复下发迭代查询命令会失败。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225561)

查询VM_USN_SPU_1上的DNS服务器的一级缓存信息：

DSP DNSCACHE: RUNAME="USN_SP_RU_0064", CACHETYPE=L1CACHE, PROCESSNO=0, DNSQUERYMODE=NAPTR, MATCHTYPE=EXACT_SEARCH, DOMAINNAME="HUAWEI1.COM.APN.EPC.MNC003.MCC460.3GPPNETWORK.ORG", SERVICETYPE="USN_VNFC";

```
%%DSP DNSCACHE: RUNAME="USN_SP_RU_0064", CACHETYPE=L1CACHE, PROCESSNO=0, DNSQUERYMODE=NAPTR, MATCHTYPE=EXACT_SEARCH, DOMAINNAME="HUAWEI1.COM.APN.EPC.MNC003.MCC460.3GPPNETWORK.ORG", 
SERVICETYPE="USN_VNFC"
;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
                          FQDN  =  HUAWEI1.COM.APN.EPC.MNC003.MCC460.3GPPNETWORK.ORG
                 Host Name索引  =  252
                  域名信息来源  =  DNS 服务器
                      网元类型  =  SGW
                      接口类型  =  S11
                S5接口协议类型  =  GTP_PMIP
                S8接口协议类型  =  GTP
                    UE使用类型  =  UUT_GroupID:1
                      网络能力  =  支持NR（New Radio）接入
                           TTL  =  NULL
          本地调整后的TTL（s）  =  0
                   PDP负荷 (%)  =  NULL
                   CPU负荷 (%)  =  NULL
                        优先级  =  65535
                      配置权重  =  65535
                  调整后的权重  =  NULL
                        优先级  =  0
                      配置权重  =  100
                  调整后的权重  =  100
                        优先级  =  65535
                      配置权重  =  65535
                  调整后的权重  =  NULL
                        优先级  =  65535
                      配置权重  =  65535
                  调整后的权重  =  NULL
                        优先级  =  65535
                      配置权重  =  65535
                  调整后的权重  =  NULL
                        主机名  =  TOPON.SGW.SGW1.NODES.EPC.ENVID00.MNC03.MCC460.3GPPNETWORK.ORG
                     主机名TTL  =  NULL
    本地调整后的主机名TTL（s）  =  0
                    IP地址类型  =  IPV4
                    地址区间号  =  SECTION1
                     Ipv4地址1  =  10.10.10.10
                       优先级1  =  127
                     配置权重1  =  127
                 调整后的权重1  =  127
                  PDP负荷1 (%)  =  NULL
                  CPU负荷1 (%)  =  NULL
                     Ipv4地址2  =  0.0.0.0
                       优先级2  =  0
                     配置权重2  =  0
                 调整后的权重2  =  0
                  PDP负荷2 (%)  =  0
                  CPU负荷2 (%)  =  0
                     Ipv4地址3  =  0.0.0.0
                       优先级3  =  0
                     配置权重3  =  0
                 调整后的权重3  =  0
                  PDP负荷3 (%)  =  0
                  CPU负荷3 (%)  =  0
                     Ipv4地址4  =  0.0.0.0
                       优先级4  =  0
                     配置权重4  =  0
                 调整后的权重4  =  0
                  PDP负荷4 (%)  =  0
                  CPU负荷4 (%)  =  0
                     Ipv4地址5  =  0.0.0.0
                       优先级5  =  0
                     配置权重5  =  0
                 调整后的权重5  =  0
                  PDP负荷5 (%)  =  0
                  CPU负荷5 (%)  =  0
                     Ipv4地址6  =  0.0.0.0
                       优先级6  =  0
                     配置权重6  =  0
                 调整后的权重6  =  0
                  PDP负荷6 (%)  =  0
                  CPU负荷6 (%)  =  0
                     Ipv4地址7  =  0.0.0.0
                       优先级7  =  0
                     配置权重7  =  0
                 调整后的权重7  =  0
                  PDP负荷7 (%)  =  0
                  CPU负荷7 (%)  =  0
                     Ipv4地址8  =  0.0.0.0
                       优先级8  =  0
                     配置权重8  =  0
                 调整后的权重8  =  0
                  PDP负荷8 (%)  =  0
                  CPU负荷8 (%)  =  0
(Number of results = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001172225561)

| 输出项名称 | 输出项解释 |
| --- | --- |
| FQDN | 标识由RAI、TAI、APN、MME等构建的域名，用来进行网元查询。 |
| Host Name索引 | 标识FQDN对应网元的索引。 |
| 网元类型 | 标识指定网元的类型。 |
| 接口类型 | 标识指定接口对应的类型。 |
| S5接口协议类型 | 用于配置网元S-GW/P-GW的S5接口协议。 |
| S8接口协议类型 | 用于配置网元S-GW/P-GW的S8接口协议。 |
| UE使用类型 | UE使用类型（UE Usage Type，简称UUT）是专用核心网（Dedicated Core Network，DCN）引入的一个概念，通过签约不同的UUT值可以区分不同的终端用户。同时，在DNS记录的“Service Parameters”字段中加上"+ue-<ue-usage-type>"，用以对核心网网元进行专网的划分。 如果一条DNS记录中指定了多个UUT，那么在本命令查询结果中，多个UUT之间用“.”间隔，形如“10.141.149.100”。如果DNS Cache的来源是本地配置，那么本字段输出格式为“UUT_GroupID:x”，x即本地配置的UUT的组ID，具体UUT成员可以通过LST UEUSGTYPEGPMEM进行查询。 |
| 网络能力 | 该参数用以区分网元是否具备特殊的网络能力，其DNS记录的“Service Parameters”字段中会加上“+nc-<network capability>”。<br>当前支持如下：<br>- 支持NR高带宽的网关，network capability含有nr，以表明网关具备NR高带宽能力。<br>- 支持PGW-C/SMF融合网关，network capability含有smf，以表明网关具备PGW-C/SMF融合能力。 |
| TTL | 标识该条CACHE记录的老化时间（s）。 |
| 本地调整后的TTL（s） | 标识该条CACHE记录本地调整后的老化时间（s）。 |
| 主机名TTL | 标识该条主机名CACHE记录的老化时间（s）。 |
| 本地调整后的主机名TTL（s） | 标识该条主机名CACHE记录本地调整后的老化时间（s）。 |
| 优先级 | 标识网元对应的优先级。优先级数值配置越小，代表优先级越高。 |
| 配置权重 | 标识DNS HOSTFILE里配置的网关权重或者查询DNS服务器时获得的网关权重。<br>配置权重在组网规划时确定。对于同优先级的网关IP地址，配置权重越高，网关被选择的几率越大。 |
| 调整后的权重 | 标识<br>UNC<br>根据网关的实时负荷信息以及配置权重，重新计算得出的权重。 |
| 主机名 | 标识主机名。 |
| IP地址类型 | 标识IP地址类型。 |
| 地址区间号 | 用于划分IP地址区间。 |
| IPV4地址 | 标识主机对应的IPv4地址。 |
| IPV6地址 | 标识主机对应的IPv6地址。 |
| PDP负荷(%) | 网关对应的PDP负荷(%)。 |
| CPU负荷(%) | 网关对应的CPU负荷(%)。 |
| 域名索引 | 标识查询的域名字符串对应的索引。 |
| 域名 | 标识查询的域名字符串 |
| DNS服务器组号 | 标识向DNS服务器查询使用的服务器组。 |
| 查询类型 | 标识向DNS服务器查询的类型。 |
| 最近一次被访问时间有效性 | 标识二级Cache根节点最近一次被访问的时间是否有效。 |
| 最近一次被访问时间 | 标识二级Cache根节点最近一次被访问的时间。 |
| 最近一次更新时间有效性 | 标识二级Cache根节点最近一次从DNS服务器更新的时间是否有效。 |
| 最近一次更新时间 | 标识二级Cache根节点最近一次从DNS服务器更新的时间。 |
| 第一次查询失败的时间有效性 | 标识二级Cache根节点最近一次向DNS服务器查询失败的时间是否有效。 |
| 第一次查询失败的时间 | 标识二级Cache根节点最近一次向DNS服务器查询失败的时间。 |
| 暂停查询开始时间有效性 | 标识二级Cache根节点暂时停止向DNS服务器查询的开始时间是否有效。 |
| 暂停查询开始时间 | 标识二级Cache根节点暂时停止向DNS服务器查询的开始时间。 |
| 根节点状态 | 标识二级Cache根节点的状态。 |
| RR节点类型 | 标识二级Cache根节点的RR节点的类型。 |
| 下一次查询的域名的索引 | 标识二级Cache NAPTR或SRV类型RR节点下一次要查询的域名的索引。 |
| 下一次查询的域名 | 标识二级Cache NAPTR或SRV类型RR节点下一次要查询的域名。 |
| 下一次查询的类型 | 标识二级Cache NAPTR类型RR节点下一次要查询的类型。 |
| 接口个数 | 标识二级Cache NAPTR类型RR节点的接口个数。 |
| IP地址索引 | 标识IP地址的索引。 |
| CNAME索引 | 标识CNAME字符串的索引。 |
| CNAME | 标识CNAME字符串。 |

查询LINK_SP_RU_0064上的DNS服务器的二级缓存信息：

DSP DNSCACHE: RUNAME="LINK_SP_RU_0064", CACHETYPE=L2CACHE, DOMAINNAME="HUAWEI23.COM.APN.EPC.MNC003.MCC460.3GPPNETWORK.ORG", ITERATIVEQUERY=YES, SERVICETYPE="LINK_VNFC";

```
操作结果如下
------------
                       TTL  =  420
      本地调整后的TTL（s）  =  0
                  域名索引  =  20
                      域名  =  HUAWEI23.COM.APN.EPC.MNC003.MCC460.3GPPNETWORK.ORG
             DNS服务器组号  =  21
                  查询类型  =  NAPTR类型查询
  最近一次被访问时间有效性  =  有效
        最近一次被访问时间  =  2023-09-06 11:03:02
    最近一次更新时间有效性  =  有效
          最近一次更新时间  =  2023-09-06 11:03:02
第一次查询失败的时间有效性  =  无效
      第一次查询失败的时间  =  NULL
    暂停查询开始时间有效性  =  无效
          暂停查询开始时间  =  NULL
                根节点状态  =  查询成功
                  网元类型  =  PGW
                       TTL  =  420
                    优先级  =  1
                  配置权重  =  65533
    下一次查询的域名的索引  =  22
          下一次查询的域名  =  PGWLIST1.PGW.HUAWEI23.COM.APN.EPC.MNC003.MCC460.3GPPNETWORK.ORG
          下一次查询的类型  =  SRV查询
                  接口个数  =  1
                  接口信息  =  (1)S5 GTP NULL
                       TTL  =  86400
      本地调整后的TTL（s）  =  0
                  域名索引  =  22
                      域名  =  PGWLIST1.PGW.HUAWEI23.COM.APN.EPC.MNC003.MCC460.3GPPNETWORK.ORG
             DNS服务器组号  =  21
                  查询类型  =  SRV查询
  最近一次被访问时间有效性  =  有效
        最近一次被访问时间  =  2023-09-06 11:03:02
    最近一次更新时间有效性  =  有效
          最近一次更新时间  =  2023-09-06 11:03:02
第一次查询失败的时间有效性  =  无效
      第一次查询失败的时间  =  NULL
    暂停查询开始时间有效性  =  无效
          暂停查询开始时间  =  NULL
                根节点状态  =  查询成功
                       TTL  =  86400
                    优先级  =  10
                  配置权重  =  10
    下一次查询的域名的索引  =  23
          下一次查询的域名  =  TOPON.A0.PGW.HUAWEI23.COM.APN.EPC.MNC003.MCC460.3GPPNETWORK.ORG
                       TTL  =  420
      本地调整后的TTL（s）  =  0
                  域名索引  =  23
                      域名  =  TOPON.A0.PGW.HUAWEI23.COM.APN.EPC.MNC003.MCC460.3GPPNETWORK.ORG
             DNS服务器组号  =  21
                  查询类型  =  A类型查询
  最近一次被访问时间有效性  =  有效
        最近一次被访问时间  =  2023-09-06 11:03:02
    最近一次更新时间有效性  =  有效
          最近一次更新时间  =  2023-09-06 11:03:02
第一次查询失败的时间有效性  =  无效
      第一次查询失败的时间  =  NULL
    暂停查询开始时间有效性  =  无效
          暂停查询开始时间  =  NULL
                根节点状态  =  查询成功
                       TTL  =  420
                 Ipv4地址1  =  10.1.3.1
                IP地址索引  =  8
(结果个数 = 1)

---    END
```
