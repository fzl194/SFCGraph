# 修改用户模板组和用户模板的绑定关系（MOD UPBINDUPG）

- [命令功能](#ZH-CN_CONCEPT_0209897230__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897230__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897230__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897230__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897230__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897230)

**适用NF：PGW-C、SMF**

本命令用于修改用户模板组和用户模板的绑定关系，可以基于特定条件进行绑定，如UserProfile优先级、IMSI/MSISDN号码段名称、IMEISV号码段名称、RAT、Roaming值、ChargeChar值及UsrLocationGrp名称，也可以指定缺省UserProfile。

#### [注意事项](#ZH-CN_CONCEPT_0209897230)

- 该命令执行后立即生效。
- 当UPBINDTYPE指定为SPECIFIC时，ImsiMsSegName、ImeisvSegName、Rat、Roaming、ChargeChar和LocGroupName至少要设置其中任意一个。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897230)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897230)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFGNAME | 用户模板组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD USRPROFGROUP命令配置生成。<br>- 配置的USERPROFGNAME必须是系统已经存在的UsrProfGroup对象名称。 |
| UPBINDTYPE | 用户模板绑定类型 | 可选必选说明：必选参数<br>参数含义：参数用于设置用户模板绑定类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- SPECIFIC：指定被绑定的用户模板。<br>- DEFAULT：指定默认用户模板。<br>- ULCL：指定ULCL用户模板。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：条件必选参数<br>前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为必选参数。<br>参数含义：该参数用于设置UserProfile绑定到UsrProfGroup时的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65534。取值范围为1到65534（65535用于用户绑定类型为默认的优先级）。值越小优先级越高。<br>默认值：无<br>配置原则：无 |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC” 或 “DEFAULT”时为必选参数。<br>参数含义：该参数用于指定UserProfile对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD USERPROFILE命令配置生成。<br>- 配置的USERPROFILENAME必须是系统已经存在的UserProfile对象名称。 |
| RAT | RAT | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为可选参数。<br>参数含义：参数用于设置无线接入技术类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- NONE：不指定无线技术接入类型。<br>- UTRAN：UMTS陆地无线接入网。<br>- GERAN：GSM/EDGE无线接入网。<br>- WLAN：无线局域网。<br>- GAN：通用接入网络。<br>- HSPA：高速分组接入。<br>- EUTRAN：通用陆基无线接入网。<br>- NR：5G无线接入(New Radio)。<br>- NBIOT：窄带物联网。<br>- EMTC：增强型机器类通信。<br>- REDCAP：轻量能力。<br>默认值：无<br>配置原则：无 |
| ROAMING | 漫游属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为可选参数。<br>参数含义：该参数用于设置用户漫游属性。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- NONE：不指定用户归属的属性。<br>- HOME：基于本地用户控制规则。<br>- ROAMING：基于漫游用户控制规则。<br>- VISITING：基于拜访用户控制规则。<br>默认值：无<br>配置原则：无 |
| CCCONFIGMODE | 计费属性配置模式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为可选参数。<br>参数含义：该参数用于设置计费属性配置模式。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- NORMAL：表示计费特征为普通计费。消息中携带的MAPPINGVALUE信元值为2048（0x0800）。<br>- HOTBILLING：表示计费特征为热计费。消息中携带的MAPPINGVALUE信元值为256（0x0100）。<br>- PREPAID：表示计费特征为预付费。消息中携带的MAPPINGVALUE信元值为1024（0x0400）。<br>- FLATBILLING：表示计费特征为统一费率计费。消息中携带的MAPPINGVALUE信元值为512（0x0200）。<br>- SPECIFIC：表示指定配置的其他计费特征。<br>默认值：无<br>配置原则：无 |
| CHARGECHAR | 计费属性 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CCCONFIGMODE”配置为“SPECIFIC”时为必选参数。<br>参数含义：该参数用于设置计费属性。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～6。十六进制，仅支持输入0x/0X、a-f/A-F、0-9，允许不输入0x/0X前缀，字母不区分大小写，取值范围0x0~0xffff。<br>默认值：无<br>配置原则：无 |
| CCMASK | 计费属性掩码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCCONFIGMODE”配置为“SPECIFIC”时为可选参数。<br>参数含义：该参数用于设置计费属性掩码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～6。十六进制，仅支持输入0x/0X、a-f/A-F、0-9，允许不输入0x/0X前缀，字母不区分大小写，取值范围0x1~0xFFFF。<br>默认值：无<br>配置原则：无 |
| IMSIMSSEGNAME | IMSI/MSISDN号段名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为可选参数。<br>参数含义：该参数用于指定IMSI/MSISDN的号码段。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD IMSIMSISDNSEG命令配置生成。<br>- 配置的IMSIMSSEGNAME必须是系统已经存在的ImsiMsisdnSeg对象名称。 |
| IMEISVSEGNAME | IMEISV号段名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为可选参数。<br>参数含义：该参数用于指定IMEISV的号码段。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD IMEISVSEG命令配置生成。<br>- 配置的IMEIVSEGNAME必须是系统已经存在的ImeisvSeg对象名称。 |
| LOCGROUPNAME | 位置组名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为可选参数。<br>参数含义：该参数用于指定位置组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD USRLOCATIONGRP命令配置生成。<br>- 配置的LOCGROUPNAME必须是系统已经存在的UsrLocationGrp对象名称。 |
| SEGGROUPNAME | IMSI/MSISDN/IMEISV 号段组名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为可选参数。<br>参数含义：该参数用于指定IMSI/MSISDN/IMEISV号码段组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD SUBSCRIBERIDSEGGRP命令配置生成。 |
| LOCALPCCSELECT | 本地PCC策略选择模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UNC本地PCC策略选择模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：继承全局配置SET PCCFUNC下的LOCALPCCSELECT参数配置。<br>- LOCAL_PCC_DEACTIVE：本地PCC策略不激活。<br>- LOCAL_PCC_ACTIVE：本地PCC策略激活。<br>- LOCAL_PCC_NO_CRBN_ACT：未下发计费规则组时本地PCC策略激活。<br>- LOCAL_PCC_NO_RULE_ACT：未下发任意计费规则时本地PCC策略激活。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897230)

运营商要修改用户模板组和用户模板的绑定关系，Rat为utran，Roaming为home：

```
MOD UPBINDUPG:USERPROFGNAME="userprofg1",UPBINDTYPE=SPECIFIC,PRIORITY=10,USERPROFILENAME="userprofile1",RAT=UTRAN,ROAMING=HOME;
```
