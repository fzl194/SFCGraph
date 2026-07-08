# 增加S11接口子网配置 (ADD S11INTFSUBNET)

- [命令功能](#ZH-CN_CONCEPT_0319330999__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0319330999__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0319330999__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0319330999__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0319330999__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0319330999__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0319330999)

**适用网元：MME**

此命令用于新增S11或S11-U接口的子网配置。

#### [注意事项](#ZH-CN_CONCEPT_0319330999)

- 该命令执行后立即生效。
- 本表最大记录数为65534条。
- 该命令在版本升级过程中禁止执行。
- “S11接口类型”参数选为“INTFTYPE_S11(S11接口)”时，“本端IPV4地址”或“本端IPV6地址”通过执行**[LST GTPCLE](../../Gtpc本端实体管理/查询GTP-C本地实体(LST GTPCLE)_72345567.md)**命令查询获取。
- “S11接口类型”参数选为“INTFTYPE_S11-U(S11-U接口)”时，“本端IPV4地址”或“本端IPV6地址”通过执行**[LST GTPULE](../../../GTP-U接口管理/Gtpu本端实体管理/查询GTP-U本地实体(LST GTPULE)_26305792.md)**命令查询获取。

#### [本地用户权限](#ZH-CN_CONCEPT_0319330999)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0319330999)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0319330999)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNKIDX | 链路关联索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本对端IP地址关联索引。<br>取值范围：0~65534<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | 远端实例ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端局向NF实例号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40<br>默认值：无<br>配置原则：无 |
| INTFTYPE | S11接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定S11接口类型。<br>取值范围：<br>- “INTFTYPE_S11 (S11接口)”<br>- “INTFTYPE_S11-U (S11-U接口)”<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：指定关联的IP地址类型<br>取值范围：<br>- “IPV4 (IPV4)”<br>- “IPV6 (IPV6)”<br>默认值：IPV4<br>配置原则：无 |
| LOCALIPV4 | 本端IPV4地址 | 可选必选说明：条件必选参数<br>参数含义：本端IPV4地址<br>前提条件：“IP地址类型”参数需要设置为“IPV4”。<br>取值范围：IPv4地址类型，0.0.0.0~255.255.255.255。<br>默认值：无<br>配置原则：<br>- “S11接口类型”参数选为“INTFTYPE_S11(S11接口)”时，通过执行**[LST GTPCLE](../../Gtpc本端实体管理/查询GTP-C本地实体(LST GTPCLE)_72345567.md)**命令查询获取。<br>- “S11接口类型”参数选为“INTFTYPE_S11-U(S11-U接口)”时，通过执行**[LST GTPULE](../../../GTP-U接口管理/Gtpu本端实体管理/查询GTP-U本地实体(LST GTPULE)_26305792.md)**命令查询获取。 |
| PEERIPV4 | 对端IPV4地址 | 可选必选说明：条件必选参数<br>参数含义：S-GW地址。<br>数据来源：全网规划<br>前提条件：“IP地址类型”参数需要设置为“IPV4”。<br>取值范围：IPv4地址类型。0.0.0.0~255.255.255.255。<br>默认值：无<br>配置原则：<br>- “S11接口类型”参数选为“INTFTYPE_S11(S11接口)”时，表示DNS中配置的S-GW地址。<br>- “S11接口类型”参数选为“INTFTYPE_S11-U(S11-U接口)”时，表示S-GW分配的S11-U地址。 |
| IPV4MASK | IPV4掩码 | 可选必选说明：条件必选参数<br>参数含义：IPV4掩码<br>前提条件：“IP地址类型”参数需要设置为“IPV4”。<br>取值范围：IPv4地址类型。0.0.0.0~255.255.255.255<br>默认值：无 |
| LOCALIPV6 | 本端IPV6地址 | 可选必选说明：条件必选参数<br>参数含义：本端IPV6地址<br>前提条件：“IP地址类型”参数需要设置为“IPV6”。<br>取值范围：IPv6地址类型，::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：<br>- “S11接口类型”参数选为“INTFTYPE_S11(S11接口)”时，通过执行**[LST GTPCLE](../../Gtpc本端实体管理/查询GTP-C本地实体(LST GTPCLE)_72345567.md)**命令查询获取。<br>- “S11接口类型”参数选为“INTFTYPE_S11-U(S11-U接口)”时，通过执行**[LST GTPULE](../../../GTP-U接口管理/Gtpu本端实体管理/查询GTP-U本地实体(LST GTPULE)_26305792.md)**命令查询获取。 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：S-GW地址。<br>数据来源：全网规划<br>前提条件：“IP地址类型”参数需要设置为“IPV6”。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- “S11接口类型”参数选为“INTFTYPE_S11(S11接口)”时，表示DNS中配置的S-GW地址。<br>- “S11接口类型”参数选为“INTFTYPE_S11-U(S11-U接口)”时，表示S-GW分配的S11-U地址。 |
| IPV6MASK | IPV6掩码 | 可选必选说明：条件必选参数<br>参数含义：IPV6掩码<br>前提条件：“IP地址类型”参数需要设置为“IPV6”。<br>取值范围：整数类型，取值范围0~128。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0319330999)

1. 添加S11接口子网配置，可以用如下命令：
  ```
  ADD S11INTFSUBNET: LNKIDX=0, NFINSTANCEID="huawei", INTFTYPE=INTFTYPE_S11, IPTYPE=IPV4, LOCALIPV4="192.168.52.1", PEERIPV4="192.168.52.2", IPV4MASK="255.255.255.255";
  ```
