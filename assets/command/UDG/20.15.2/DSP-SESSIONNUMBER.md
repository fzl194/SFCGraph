---
id: UDG@20.15.2@MMLCommand@DSP SESSIONNUMBER
type: MMLCommand
name: DSP SESSIONNUMBER（显示会话数）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SESSIONNUMBER
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
- 会话数目查询
status: active
---

# DSP SESSIONNUMBER（显示会话数）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询当前在线会话数。如果不输入参数表示显示整机的所有会话数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DISPLAYMODE | 显示方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定显示方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- APN：查询使用该APN激活的当前在线会话数。<br>- APN_RELATE：查询使用该别名APN激活的当前在线会话数。<br>- ONLINE：查询当前使用在线计费的会话数。在线计费会话是指N4接口下发online-urrid-switch信元值为enable或者N4接口下发在线计费类型URR（Create-URR携带volume-quota/time-quota/event-quota信元）的会话。<br>- OFFLINE：查询当前使用离线计费的会话数。离线计费会话是指下发offline-urrid-switch信元为enable或者不下发offline-urrid-switch信元的会话。<br>- NON_IP：查询激活的Non-IP用户会话数。<br>- NODEID：根据NODEID查询当前在线会话数。<br>- NSA：查询当前非独立组网激活的会话数。<br>- USERPROFILE：查询当前user profile激活的会话数。<br>- ANTIFRAUD：查询防欺诈的会话数。<br>- PODNAME：根据PODNAME查询当前在线会话数。<br>- L2TP：查询当前L2TP会话数。<br>- CU_CONFIGURATION_INCONSISTENCY：查询受CP和UP关键配置不一致影响的在线用户会话数。<br>- BWM：查询当前BWM会话数。<br>- UPLINKBWLEV：查询上行带宽级别的会话数。<br>- N4U_TUNNEL：查询基于N4建立GTPU隧道的设备级会话数。<br>- ROAMING：查询当前在线漫游用户数和拜访数。<br>- NGLAN：表示查询当前在线的5G LAN组会话和UE会话数。<br>- QOS_MONT：查询当前整机内的时延监测实时会话数。<br>- RAT：按照接入类型查询会话数。<br>- TRUNK：查询宽带集群用户会话数。<br>- DNAI：按照DNAI查询会话数。<br>- MultiDNN：按照MultiDNN类型查询会话数。<br>- HIGHSPEED：查询当前在线的高速用户会话数。<br>- MBS：表示查询当前在线的MBS会话数。<br>- IPSUIT：按照IPSuit查询会话数。<br>- RtsDNN：按照RtsDnn类型查询会话数。<br>- DEDICATEDLBO：查询专网UPF分流的独立ULCL会话数。<br>- MBMS：表示查询当前在线的MBMS会话数。<br>- NETWORKINSTANCE：表示查询当前在线的NETWORKINSTANCE会话数。<br>- IMS_BYPASS：查询UPF上IMS惯性运行会话数。<br>- QOS_ANA：查询当前提供服务质量分析的会话数。<br>- QOS_EXP：查询当前提供服务体验上报的会话数。<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“APN”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“UPLINKBWLEV”、“RAT”、“MultiDNN”、“RtsDNN” 或 “DEDICATEDLBO”时为可选参数。<br>参数含义：该参数用于指定APN实例名。表示查询使用该APN激活的当前在线会话数，该APN必须在系统上已经配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及部分特殊字符。可以支持的特殊字符有“.”和“-”，“.”不可以是第一个字符且不可以连续出现。<br>默认值：无<br>配置原则：无 |
| RELATEAPN | APN别名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“APN_RELATE”时为必选参数。<br>参数含义：该参数用于指定APN别名。表示查询使用该别名APN激活的当前在线会话数，该别名APN所对应的真实APN必须在系统上已经配置。如果输入真实APN，则显示与真实APN相关联的所有别名APN上的当前在线会话数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及部分特殊字符。可以支持的特殊字符有“.”和“-”，“.”不可以是第一个字符且不可以连续出现。<br>默认值：无<br>配置原则：无 |
| CPNODEIDSW | Node ID开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“NGLAN”时为可选参数。<br>参数含义：该参数用于指定是否使用Node ID查询会话数。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| CPNODEIDTYPE | Node ID类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“NODEID”时为必选参数。<br>可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDSW”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用来指定Node ID 类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPv4：表示Node ID类型为IPv4地址。<br>- IPv6：表示Node ID类型为IPv6地址。<br>- FQDN：表示Node ID类型为FQDN。<br>默认值：无<br>配置原则：无 |
| CPNODEIDIPV4 | Node ID中的IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于指定，在根据Node ID查询CP信息时，Node ID中的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CPNODEIDIPV6 | Node ID中的IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于指定，在根据Node ID查询CP信息时，Node ID中的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| CPNODEFQDN | Node ID的FQDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“FQDN”时为必选参数。<br>参数含义：该参数用于指定，在根据NODE ID查询CP信息时，Node ID中的FQDN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～255。不支持空格，必须是可见ASCII码，不区分大小写。<br>默认值：无<br>配置原则：无 |
| USERPROFILE | 用户模板名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“USERPROFILE”时为必选参数。<br>参数含义：用户的userprofile名。该userprofile必须在系统上已经配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USERPROFILE命令配置生成。 |
| PODNAME | Pod名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“PODNAME”时为必选参数。<br>参数含义：该参数用于指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1~63，不支持空格，区分大小写。<br>默认值：无<br>配置原则：无 |
| MNC | 移动设备码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“ROAMING”时为可选参数。<br>参数含义：该参数用于指定MNC移动网络码。表示查询使用该MNC激活的当前在线会话数。<br>数据来源：本端规划<br>取值范围：字符串类型，为3位数字，000～999。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“ROAMING”时为可选参数。<br>参数含义：该参数用于指定MCC移动国家码。表示查询使用该MCC激活的当前在线会话数。<br>数据来源：本端规划<br>取值范围：字符串类型，为3位数字，000～999。<br>默认值：无<br>配置原则：无 |
| VNINSTANCE | 5G LAN 组名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“NGLAN”时为可选参数。<br>参数含义：表示用户的VNINSTANCE信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：无 |
| RATTYPE | RAT类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“RAT”时为必选参数。<br>参数含义：该参数用来指定无线接入类型。表示查询该接入类型当前在线会话数。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- UTRAN：通用陆地无线接入网。<br>- GERAN：GSM/EDGE无线接入网。<br>- WLAN：无线局域网。<br>- GAN：通用访问网络。<br>- HSPA：高速分组接入。<br>- EUTRAN：演进型通用陆地无线接入网。<br>- EUTRAN_NB_IOT：窄带物联网。<br>- LTE_M：低功耗窄带物联网。<br>- NR：5G用户。<br>- REDCAP：RedCap NR的5G用户。<br>默认值：无<br>配置原则：无 |
| DNAI | DNAI 名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“DNAI”时为必选参数。<br>参数含义：该参数用于指定DNAI实例名。表示查询使用该DNAI激活的当前在线会话数，该DNAI必须在系统上已经配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| IPSUITNAME | IPSuit 名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“IPSUIT”时为必选参数。<br>参数含义：IP Suit的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。此名称系统自动生成，取值为1~64。<br>默认值：无<br>配置原则：无 |
| USERPROFILETYPE | UserProfile类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“USERPROFILE”时为必选参数。<br>参数含义：UserProfile类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- COMMONPOLICY：COMMONPOLICY类型。<br>- PREDEFINEDRULE：预定义Rule类型。<br>- ALL：COMMONPOLICY和PREDEFINEDRULE类型。<br>默认值：无<br>配置原则：无 |
| CONFLICTMODE | 冲突会话类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DISPLAYMODE”配置为“MultiDNN” 或 “RtsDNN”时为可选参数。<br>参数含义：表示查询当前在线的冲突会话数。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPCONFLICT：用户IP地址和ServerIP冲突会话。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SESSIONNUMBER]] · 会话数（SESSIONNUMBER）

## 使用实例

- 显示当前所有会话数：
  ```
  DSP SESSIONNUMBER:;
  ```
  ```

  RETCODE = 0 操作成功。

  会话数信息
  ----------
  Result  =  
                                  Pod Name = ssgpod-0
                           GGSN Session(s) = 0
                            SGW Session(s) = 0
                            PGW Session(s) = 0
                           SPGW Session(s) = 0
                            UPF Session(s) = 0
                    N4-U Tunnel Session(s) = 0
                          Trunk Session(s) = 0
                        UPF MBS Session(s) = 0

                       All GGSN Session(s) = 0
                        All SGW Session(s) = 0
                        All PGW Session(s) = 0
                       All SPGW Session(s) = 0
                        All UPF Session(s) = 0
                All N4-U Tunnel Session(s) = 0
                      All Trunk Session(s) = 0
                    All UPF MBS Session(s) = 0

                    ALL Session context(s) = 0
  (结果个数 = 1)
  ---    END
  ```
- 显示当前离线计费会话数：
  ```
  DSP SESSIONNUMBER: DISPLAYMODE=OFFLINE;
  ```
  ```

  RETCODE = 0 操作成功。

  会话数信息
  ----------
  Result  =  
                              Pod Name = ssgpod-0124-30-0-210
       Offline Charging Session(s) = 1

    All Offline Charging Session(s) = 1
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SESSIONNUMBER.md`
