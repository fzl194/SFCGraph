---
id: UNC@20.15.2@MMLCommand@DSP COMGTPCPATHINFO
type: MMLCommand
name: DSP COMGTPCPATHINFO（显示UAM GTPC路径信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: COMGTPCPATHINFO
command_category: 查询类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C路径维护
status: active
---

# DSP COMGTPCPATHINFO（显示UAM GTPC路径信息）

## 功能

**适用NF：SGSN、MME、AMF**

该命令用于显示UAM GTP-C路径信息。

## 注意事项

- 如需要进行MME/SGSN单进程的查询，则需要通过DSP GTPCPATH命令查询。
- 当"RU名称"未输入时，默认只向AMF查询。
- 查询的GTP-C路径数目，最大可显示MME/SGSN以及AMF共5000条，大于5000条需要独立查询原子表。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C路径的IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：无 |
| LOCALIPV4 | 本端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于指定GTP-C路径的本端IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| LOCALIPV6 | 本端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于指定GTP-C路径的本端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| GTPVERIN | GTP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C路径的GTP版本号。<br>数据来源：本端规划<br>取值范围：GTPV0只适用于MME/SGSN。<br>- GTPV0（GTP V0）<br>- GTPV1（GTP V1）<br>- GTPV2（GTP V2）<br>默认值：无<br>配置原则：无 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| QRYTP | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：本端规划<br>取值范围：<br>- MEMORY（内存）<br>- DDB（数据库）<br>默认值：MEMORY<br>配置原则：无 |
| INTFTYPEIN | 接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GTP-C路径的接口类型。<br>数据来源：本端规划<br>取值范围：AMF只支持选择一种接口类型，包括unknown，Gn，Gp，S11，S5，S8，N26，S4，All；MME/SGSN不支持选择S5，S8，N26。<br>- UNKNOWN（unknown）<br>- Gn（Gn）<br>- Gp（Gp）<br>- S3（S3）<br>- S4（S4）<br>- S10（S10）<br>- S11（S11）<br>- S16（S16）<br>- Sm（Sm）<br>- Sv（Sv）<br>- S101（S101）<br>- Sn（Sn）<br>- N26（N26）<br>- S5（S5）<br>- S8（S8）<br>- ALL（All）<br>默认值：ALL-1<br>配置原则：无 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。该参数只适用于MME/SGSN，该参数可以通过DSP RU命令查询；AMF默认显示为NULL。<br>默认值：无<br>配置原则：无 |
| PATHSTATUSIN | 路径状态 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GTP-C路径的路径状态。<br>数据来源：本端规划<br>取值范围：<br>- ERROR（故障）<br>- NORMAL（正常）<br>- ALL（所有）<br>默认值：ERROR<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/COMGTPCPATHINFO]] · UAM GTPC路径信息（COMGTPCPATHINFO）

## 使用实例

DSP COMGTPCPATHINFO: IPTYPE=IPV4, GTPVERIN=GTPV2, QRYTP=MEMORY, INTFTYPEIN=UNKNOWN-0&Gn-0&Gp-0&S3-0&S4-0&S10-0&S11-0&S16-0&Sm-0&Sv-0&S101-0&Sn-0&N26-0&S5-0&S8-0&ALL-1, PATHSTATUSIN=ALL;

```
%%DSP COMGTPCPATHINFO: IPTYPE=IPV4, GTPVERIN=GTPV2, QRYTP=MEMORY, INTFTYPEIN=UNKNOWN-0&Gn-0&Gp-0&S3-0&S4-0&S10-0&S11-0&S16-0&Sm-0&Sv-0&S101-0&Sn-0&N26-0&S5-0&S8-0&ALL-1, PATHSTATUSIN=ALL;%%
RETCODE = 0  操作成功

结果如下
------------------------
                    IP地址类型  =  IPV4
                    本端IP地址  =  192.168.138.2
                    对端IP地址  =  10.70.240.1
                      进程类型  =  NULL
                        进程号  =  0
                 GTP-C路径数目  =  0
             GTP-C路径网络类型  =  5G Core Network
           发送Echo Request开关  =  ON
                      接口类型  =  S11
               路径断去激活会话时间  =  00:00:00
对端Recovery变化去激活会话时间  =  00:00:00
                       对端Recovery值  =  0
                       Prn标志  =  Disable
                       Ntsr标志  =  Disable
                       RU名称  =  NULL
                     路径状态  =  NORMAL
                    GTP版本  =  GTP V2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示UAM-GTPC路径信息（DSP-COMGTPCPATHINFO）_71516425.md`
