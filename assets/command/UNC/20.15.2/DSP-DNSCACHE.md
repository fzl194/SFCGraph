---
id: UNC@20.15.2@MMLCommand@DSP DNSCACHE
type: MMLCommand
name: DSP DNSCACHE（显示DNS Cache）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DNSCACHE
command_category: 查询类
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
- DNS Cache管理
status: active
---

# DSP DNSCACHE（显示DNS Cache）

## 功能

**适用网元：SGSN、MME**

该命令用于查看DNS在各个进程上的Cache信息，以及HOSTFILE信息。DNS Cache是使用DNS服务器解析时查找到的域名和IP地址信息在系统中的缓存，用于快速解析域名。DNS Cache分为一级Cache和二级Cache。一级Cache保存在SPP进程上，二级Cache保存在添加了DNSLE（参见 [**ADD DNSLE**](../DNS本端实体管理/增加DNS实体绑定DNS Client IP(ADD DNSLE)_72225567.md) ）的SPU上对应的1号SGP进程上。HOSTFILE信息是通过 [**ADD IPV4DNSH**](../DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md) 、 [**ADD IPV6DNSH**](../DNS Hostfile管理/增加IPV6 DNS Hostfile记录(ADD IPV6DNSH)_26145886.md) 或 [**ADD DNSN**](../DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md) 配置的数据。

## 注意事项

- 该命令执行后立即生效。
- 该命令只用于查询SPP或1号SGP进程。
- 该命令执行模糊查询时，执行的是分段查询。即从“起始输出索引”开始，向后查找“最大查找索引个数”。
- 该命令执行时，如缓存类型为L1CACHE，会查询到HOSTFILE信息。
- 该命令执行模糊查询时，如果查找到的结果较多，会导致OMP进程的CPU占用率短暂冲高，不建议频繁进行此类查询。
- 对于查询S-GW网元域名的结果信息，在一级Cache中只保存S4、S11接口信息；对于查询非APN域名的结果信息，在一级Cache中不保存GGSN、P-GW网元信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

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

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNSCACHE]] · DNS Cache（DNSCACHE）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示DNS-Cache(DSP-DNSCACHE)_72225561.md`
