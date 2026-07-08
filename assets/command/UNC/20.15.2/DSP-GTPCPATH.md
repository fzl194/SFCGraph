---
id: UNC@20.15.2@MMLCommand@DSP GTPCPATH
type: MMLCommand
name: DSP GTPCPATH（显示GTP-C路径）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GTPCPATH
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
- GTP-C协议管理
- GTP-C路径管理
status: active
---

# DSP GTPCPATH（显示GTP-C路径）

## 功能

**适用网元：SGSN、MME**

该命令用于查询GTP-C路径状态，如果输入路径在系统中已经存在则输出这条路径的状态。

## 注意事项

- 该命令执行后立即生效。
- 该命令可用于SPP进程/UPP进程。
- 当“进程类型”未输入时，默认查询UPP进程上的路径状态信息。
- 当查询尚未确定版本类型的路径时，输入参数“GTP版本”需要选择“GTPv1”。
- 该命令查询出的路径是最近使用的路径，当路径上长时间没有信令消息时，路径会老化删除并不再显示，直到路径上重新有信令传输才会重新创建显示。路径的老化删除时间可以参考[**SET UGTP**](../GTP-C路径扫描参数/设置GTP-C路径扫描参数(SET UGTP)_26145916.md)命令。
- 当GTP-C路径数较多时，命令执行时长可能会持续几分钟。建议通过“本端IPv4地址”/“本端IPv6地址”、“对端IPv4地址”/“对端IPv6地址”、“对端IPv4地址掩码”、“路径状态筛选”、“网元间接口类型筛选”参数的组合来进行分类查询，减少一次查询的GTP-C路径数，提高每次查询的效率。（GTP-C路径数可通过[**DSP GTPCPATHNUM**](显示GTP-C路径个数(DSP GTPCPATHNUM)_26305720.md)命令查询获得）。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称。该参数可以通过<br>[**DSP RU**](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：1~63位字符串<br>默认值：无 |
| PROCTP | 进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程的进程类型。<br>取值范围：<br>- “SPP(SPP)”<br>- “UPP(UPP)”<br>默认值：无 |
| PROCNO | 进程号 | 可选必选说明：可选参数<br>可选必选说明：条件可选参数<br>参数含义：该参数用于指定进程的序号。<br>取值范围：0~20<br>默认值：0 |
| QRYTP | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询类型。<br>取值范围：<br>- “MEMORY(内存)”<br>- “DDB(数据库)”<br>默认值：<br>“MEMORY(内存)”<br>说明：普通查询可以选择系统默认值。 |
| GTPVER | GTP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C路径的协议版本。<br>取值范围：<br>- “GTPv0(GTPv0)”<br>- “GTPv1(GTPv1)”<br>- “GTPv2(GTPv2)”<br>默认值：无 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端GSN的IP地址类型。<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| LOCIPV4ADDR | 本端IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定本端GSN IPv4地址。<br>前提条件：当<br>“IP类型”<br>设置为<br>“IPV4(IPV4)”<br>时此参数有效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>说明：若本参数没有输入，则不以本参数作为筛选条件来查询所有的GTP-C路径。若本参数输入，则以输入的值作为筛选条件来查询所有的GTP-C路径。<br>GTP-C路径的本端IPv4地址可以使用<br>[**LST GTPCLE**](../../Gtpc本端实体管理/查询GTP-C本地实体(LST GTPCLE)_72345567.md)<br>查询 |
| PEERIPV4ADDR | 对端IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定对端GSN IPv4地址。<br>前提条件：当<br>“IP类型”<br>设置为<br>“IPV4(IPV4)”<br>时此参数有效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>说明：若本参数没有输入，则不以本参数作为筛选条件来查询所有的GTP-C路径。若本参数输入，则以输入的值与<br>“对端IPv4地址掩码”<br>组成的网段作为筛选条件来查询所有的GTP-C路径。 |
| PEERIPV4MASK | 对端IPv4地址掩码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GTP-C路径的对端IPv4地址的掩码，与<br>“对端IPv4地址”<br>参数一起指定查询GTP-C路径的对端IPv4地址的网段。<br>数据来源：整网规划<br>前提条件：当<br>“IP类型”<br>设置为<br>“IPV4(IPv4)”<br>时此参数有效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：255.255.255.255 |
| LOCIPV6ADDR | 本端IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定本端GSN IPv6地址。<br>前提条件：当<br>“IP类型”<br>设置为<br>“IPV6(IPV6)”<br>时此参数有效。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| PEERIPV6ADDR | 对端IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定对端GSN IPv6地址。<br>前提条件：当<br>“IP类型”<br>设置为<br>“IPV6(IPV6)”<br>时此参数有效。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>说明：在输入对端IP地址参数时，请确认此IP为对端GSN信令面（GTP-C路径）的IP地址，如果存在与{本端IP地址、对端IP地址、GTP版本}标识对应的路径，将显示此路径的详细信息。 |
| MAXDSPNUM | 最大显示路径数目 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询结果最大显示的路径数目。若实际匹配的查询路径数大于指定的最大显示路径条目，多出的路径数不会显示。<br>数据来源：整网规划<br>取值范围：1~65536<br>默认值：5000<br>说明：当GTP-C路径数较多时，本参数的取值越大，命令执行的时长越长。建议保持系统默认值不变。 |
| PATHST | 路径状态筛选 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询GTP-C路径的状态。<br>数据来源：整网规划<br>取值范围：<br>- “NORMAL（正常）”<br>- “ERROR（故障）”<br>- “ALL（所有）”<br>默认值：<br>“ERROR(故障)”<br>说明：若本参数没有输入，系统缺省查询<br>“ERROR（故障）”<br>状态的GTP-C路径。 |
| PEERINTF | 网元间接口类型筛选 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询GTP-C路径的网元间接口类型。<br>数据来源：整网规划<br>取值范围：Gn（Gn），Gp（Gp），S3（S3），S4（S4），S10（S10），S11（S11），S16（S16），Sv（Sv）<br>默认值：无<br>说明：若本参数没有输入，系统缺省查询所有网元间接口类型的GTP-C路径。若GTP-C路径同时存在多个网元间接口类型时，输出结果为包含指定输入的网元间接口类型的GTP-C路径。<br>举例：GTP-C路径上同时存在“S11”、“S4”接口类型，输入“S11”筛选条件可以查询，输入“S4”筛选条件也可以查询。 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：此参数用于指定待查询的服务名称，可以通过<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>配置原则：<br>- 如果要查询SPP进程上的GTPC路径，则SERVICETYPE需要填写USN的VNFC类型名称。<br>- 如果要查询UPP进程上的GTPC路径，则SERVICETYPE需要填写LINK的VNFC类型名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCPATH]] · GTP-C路径（GTPCPATH）

## 使用实例

查询资源单元为USN_SP_RU_0066上的V1版本GTP-C PATH信息：

DSP GTPCPATH: RUNAME="USN_SP_RU_0066", PROCNO=0, QRYTP=MEMORY, GTPVER=GTPv1, IPTYPE=IPV4, SERVICETYPE="USN_VNFC";

```
%%DSP GTPCPATH: RUNAME="USN_SP_RU_0066", PROCNO=0, QRYTP=MEMORY, GTPVER=GTPv1, IPTYPE=IPV4, 
SERVICETYPE="USN_VNFC"
;%%
RETCODE = 0  操作成功。

操作结果如下
------------
       RU名称 = USN_SP_RU_0066
     进程类型 = UPP
       进程号 = 0
仍有后续报告输出
---    END

%%DSP GTPCPATH: RUNAME="USN_SP_RU_0066", PROCNO=0, QRYTP=MEMORY, GTPVER=GTPv1, IPTYPE=IPV4, 
SERVICETYPE="USN_VNFC"
;%%
RETCODE = 0  操作成功。

操作结果如下
------------
GTP路径数目  =  1
仍有后续报告输出
---    END

%%DSP GTPCPATH: RUNAME="USN_SP_RU_0066", PROCNO=0, QRYTP=MEMORY, GTPVER=GTPv1, IPTYPE=IPV4, 
SERVICETYPE="USN_VNFC"
;%%
RETCODE = 0  操作成功。

操作结果如下
------------
                GTP版本 = GTPv2
             本端IP地址 = 192.168.14.20
             对端IP地址 = 192.168.9.20
        GTP路径接口类型 = 2G或3G网络
       PLMN网元间的接口 = Gn接口
            GTP路径状态 = 故障
            GTP路径属性 = 路径管理
        对端Recovery值  = 10
   是否发送Echo Request = 是
(结果个数 = 3)
共有3个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示GTP-C路径(DSP-GTPCPATH)_72225591.md`
