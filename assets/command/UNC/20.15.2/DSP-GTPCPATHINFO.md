---
id: UNC@20.15.2@MMLCommand@DSP GTPCPATHINFO
type: MMLCommand
name: DSP GTPCPATHINFO（显示GTP-C链路信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GTPCPATHINFO
command_category: 查询类
applicable_nf:
- AMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C路径维护
status: active
---

# DSP GTPCPATHINFO（显示GTP-C链路信息）

## 功能

**适用NF：AMF、PGW-C、SGW-C、GGSN**

该命令用于查询GTP-C路径信息。

## 注意事项

- 当“接口类型”未输入时，默认查询所有接口类型的路径状态信息。
- 当“查询类型”未输入时，默认查询内存(MEMORY)中的路径状态信息。
- 当“查询类型”为“内存(MEMORY)”时，不显示“对端Recovery值”、“路径断去激活会话时间”、“对端Recovery变化去激活会话时间”信息。
- 当“路径状态筛选”未输入时，默认查询路径状态为故障(Error)的路径状态信息。
- 当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效，请使用命令DSP GTPCPATH查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTPVER | GTP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C路径的GTP版本号。<br>数据来源：全网规划<br>取值范围：<br>- GTPv1（GTPv1）<br>- GTPv2（GTPv2）<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C路径的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPTypeV4（IPv4类型）”：IPTypeV4<br>- “IPTypeV6（IPv6类型）”：IPTypeV6<br>默认值：无<br>配置原则：无 |
| LOCALIPV4 | 本端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV4"时为条件可选参数。<br>参数含义：该参数用于指定GTP-C路径的本端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>业务地址必须是A、B或者C类地址。 |
| LOCALIPV6 | 本端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV6"时为条件可选参数。<br>参数含义：该参数用于指定GTP-C路径的本端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV4"时为条件可选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>业务地址必须是A、B或者C类地址。 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV6"时为条件可选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| PATHST | 路径状态筛选 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询GTP-C路径的状态。<br>数据来源：本端规划<br>取值范围：<br>- ERROR（故障）<br>- NORMAL（正常）<br>- ALL（所有）<br>默认值：ERROR<br>配置原则：无 |
| QRYTP | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：本端规划<br>取值范围：<br>- MEMORY（内存）<br>- DDB（数据库）<br>默认值：MEMORY<br>配置原则：无 |
| INTERFACETYPEIN | 接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GTP-C路径的接口类型。<br>数据来源：本端规划<br>取值范围：<br>- Unknow（未知接口）<br>- Gn（Gn接口）<br>- Gp（Gp接口）<br>- S5（S5接口）<br>- S8（S8接口）<br>- S11（S11接口）<br>- N26（N26接口）<br>- S4（S4接口）<br>- All（All）<br>- Proxy（Proxy接口）<br>默认值：All<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GTPCPATHINFO]] · GTP-C路径（GTPCPATHINFO）

## 使用实例

查询本端IP地址为10.1.12.3，对端IP地址为10.2.20.1，GTP版本号为GTPv2的GTP-C路径信息：DSP GTPCPATHINFO: GTPVER=GTPv2, IPTYPE=IPTypeV4, LOCALIPV4="10.1.12.3", PEERIPV4="10.2.20.1", PATHST=ALL;

```
%%DSP GTPCPATHINFO: GTPVER=GTPv2, IPTYPE=IPTypeV4, LOCALIPV4="10.1.12.3", PEERIPV4="10.2.20.1", PATHST=ALL;%%
RETCODE = 0  操作成功

结果如下
------------------------
   IP地址类型  =  IPTypeV4
 本端IPv4地址  =  10.1.12.3
 对端IPv4地址  =  10.2.20.1
      GTP版本  =  GTPv2
     路径状态  =  Normal
     接口类型  =  S5接口
      POD名称  =  uncpod-0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-GTPCPATHINFO.md`
