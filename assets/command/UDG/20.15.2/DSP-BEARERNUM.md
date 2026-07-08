---
id: UDG@20.15.2@MMLCommand@DSP BEARERNUM
type: MMLCommand
name: DSP BEARERNUM（显示承载数）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: BEARERNUM
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 承载数目查询
status: active
---

# DSP BEARERNUM（显示承载数）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查看当前在线承载个数。如果不输入参数表示显示整机的所有承载个数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DISPLAYMODE | 显示方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定显示方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- APN：查询使用该APN激活的当前在线上下文数。<br>- APN_RELATE：APN别名或真实APN，查询使用该别名APN激活的当前在线上下文数。该别名APN所对应的真实APN必须在系统上已经配置。如果输入真实APN，则显示与真实APN相关联的所有别名APN上的当前在线上下文数。<br>- ONLINE：查询当前使用在线计费以及在线计费转离线计费的上下文数。在线计费上下文是指N4接口下发online-urrid-switch信元值为enable或者N4接口下发在线计费类型URR（Create-URR携带volume-quota/time-quota/event-quota信元）的上下文。<br>- OFFLINE：查询当前使用离线计费的上下文数。离线计费上下文是指下发offline-urrid-switch信元为enable或者不下发offline-urrid-switch信元的上下文。<br>- RAT：查询不同无线接入类型的上下文数目。<br>- NODEID：查询使用该NODEID激活的当前在线上下文数。<br>- NON_IP：查询激活的Non-IP用户上下文数。<br>- NSA：查询当前NSA各网元的上下文数。<br>- BWM：查询当前BWM用户的上下文数。<br>- N4U_TUNNEL：查询当前N4U隧道的上下文数。<br>- QOS_MONT：查询时延监测的承载总数。<br>- COLOCATED_ULCL：查询本地分流的上下文数。<br>- NGLAN：查询当前5G LAN用户的上下文数。<br>- TRUNK：查询宽带集群用户承载数。<br>- MBS：查询组播/广播业务用户承载数。<br>- MBMS：查询MBMS用户承载数。<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“APN”时为必选参数。<br>参数含义：该参数用于指定APN实例名。表示查询使用该APN激活的当前在线承载数，该APN必须在系统上已经配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| RELATEAPN | APN别名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“APN_RELATE”时为必选参数。<br>参数含义：该参数用于指定APN别名。表示查询使用该别名APN激活的当前在线承载数，该别名APN所对应的真实APN必须在系统上已经配置。如果输入真实APN，则显示与真实APN相关联的所有别名APN上的当前在线承载数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| RATTYPE | 无线接入类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“RAT”时为必选参数。<br>参数含义：该参数用来指定无线接入类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- UTRAN：通用陆地无线接入网。<br>- GERAN：GSM/EDGE无线接入网。<br>- WLAN：无线局域网。<br>- GAN：通用访问网络。<br>- HSPA：高速分组接入。<br>- EUTRAN：演进型通用陆地无线接入网。<br>- EUTRAN_NB_IOT：窄带物联网。<br>- LTE_M：低功耗窄带物联网。<br>- NR：5G用户。<br>- REDCAP：RedCap NR的5G用户。<br>默认值：无<br>配置原则：无 |
| CPNODEIDTYPE | Node ID类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“NODEID”时为必选参数。<br>参数含义：该参数用来指定Node ID 类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPv4：表示Node ID类型为IPv4地址。<br>- IPv6：表示Node ID类型为IPv6地址。<br>- FQDN：表示Node ID类型为FQDN。<br>默认值：无<br>配置原则：无 |
| CPNODEIDIPV4 | Node ID中的IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于指定，在根据Node ID查询CP信息时，Node ID中的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CPNODEIDIPV6 | Node ID中的IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于指定，在根据Node ID查询CP信息时，Node ID中的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| CPNODEFQDN | Node ID的FQDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“FQDN”时为必选参数。<br>参数含义：该参数用于指定，在根据NODE ID查询CP信息时，Node ID中的FQDN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～255。不支持空格，必须是可见ASCII码，不区分大小写。<br>默认值：无<br>配置原则：无 |
| VNINSTANCE | 5G LAN 组名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“NGLAN”时为可选参数。<br>参数含义：表示用户的5G LAN组名称信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BEARERNUM]] · 承载数（BEARERNUM）

## 使用实例

显示承载数：

```
DSP BEARERNUM:;
```

```

RETCODE = 0  操作成功

承载数信息:
-----------
result  =  

                                         Pod Name = ssgpod-0
                            GGSN Bearer Number(s) = 0
                             SGW Bearer Number(s) = 0
                             PGW Bearer Number(s) = 0
                            SPGW Bearer Number(s) = 0
                             UPF Bearer Number(s) = 0
                            N4-U Bearer Number(s) = 0
                           Trunk Bearer Number(s) = 0
                             MBS Bearer Number(s) = 0

                        ALL GGSN Bearer Number(s) = 0
                         ALL SGW Bearer Number(s) = 0
                         ALL PGW Bearer Number(s) = 0
                        ALL SPGW Bearer Number(s) = 0
                         ALL UPF Bearer Number(s) = 0
                        ALL N4-U Bearer Number(s) = 0
                       ALL Trunk Bearer Number(s) = 0
                         ALL MBS Bearer Number(s) = 0

                             ALL Bearer Number(s) = 0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-BEARERNUM.md`
