---
id: UNC@20.15.2@MMLCommand@RMV UPBINDUPG
type: MMLCommand
name: RMV UPBINDUPG（删除用户模板组和用户模板的绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UPBINDUPG
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 用户模板绑定
status: active
---

# RMV UPBINDUPG（删除用户模板组和用户模板的绑定关系）

## 功能

**适用NF：PGW-C、SMF**

本命令用于解除UsrProfGroup与所有或某个UserProfile的绑定关系。

## 注意事项

- 该命令执行后立即生效。
- 当用户模板绑定删除类型指定为CONDITION时，必须输入全量精确的绑定条件才能删除对应的配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFGNAME | 用户模板组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的USERPROFGNAME必须是系统已经存在的UsrProfGroup对象名称。 |
| UPREMOVETYPE | 用户模板绑定删除类型 | 可选必选说明：可选参数<br>参数含义：参数用于设置用户模板删除类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- USER_PROFILE_NAME：根据User Profile Name删除。<br>- CONDITION：指定通过条件删除User Profile。<br>默认值：无<br>配置原则：无 |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“UPREMOVETYPE”配置为“USER_PROFILE_NAME”时为必选参数。<br>参数含义：该参数用于指定UserProfile对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的USERPROFILENAME必须是系统已经存在的UserProfile对象名称。 |
| RAT | RAT | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPREMOVETYPE”配置为“CONDITION”时为可选参数。<br>参数含义：参数用于设置无线接入技术类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- NONE：不指定无线技术接入类型。<br>- UTRAN：UMTS陆地无线接入网。<br>- GERAN：GSM/EDGE无线接入网。<br>- WLAN：无线局域网。<br>- GAN：通用接入网络。<br>- HSPA：高速分组接入。<br>- EUTRAN：通用陆基无线接入网。<br>- NR：5G无线接入(New Radio)。<br>- NBIOT：窄带物联网。<br>- EMTC：增强型机器类通信。<br>- REDCAP：轻量能力。<br>默认值：无<br>配置原则：无 |
| ROAMING | 漫游属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPREMOVETYPE”配置为“CONDITION”时为可选参数。<br>参数含义：该参数用于设置用户漫游属性。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- NONE：不指定用户归属的属性。<br>- HOME：基于本地用户控制规则。<br>- ROAMING：基于漫游用户控制规则。<br>- VISITING：基于拜访用户控制规则。<br>默认值：无<br>配置原则：无 |
| CCCONFIGMODE | 计费属性配置模式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPREMOVETYPE”配置为“CONDITION”时为可选参数。<br>参数含义：该参数用于设置计费属性配置模式。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- NORMAL：表示计费特征为普通计费。消息中携带的MAPPINGVALUE信元值为2048（0x0800）。<br>- HOTBILLING：表示计费特征为热计费。消息中携带的MAPPINGVALUE信元值为256（0x0100）。<br>- PREPAID：表示计费特征为预付费。消息中携带的MAPPINGVALUE信元值为1024（0x0400）。<br>- FLATBILLING：表示计费特征为统一费率计费。消息中携带的MAPPINGVALUE信元值为512（0x0200）。<br>- SPECIFIC：表示指定配置的其他计费特征。<br>默认值：无<br>配置原则：无 |
| CHARGECHAR | 计费属性 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CCCONFIGMODE”配置为“SPECIFIC”时为必选参数。<br>参数含义：该参数用于设置计费属性。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～6。十六进制，仅支持输入0x/0X、a-f/A-F、0-9，允许不输入0x/0X前缀，字母不区分大小写，取值范围0x0~0xffff。<br>默认值：无<br>配置原则：无 |
| CCMASK | 计费属性掩码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCCONFIGMODE”配置为“SPECIFIC”时为可选参数。<br>参数含义：该参数用于设置计费属性掩码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～6。十六进制，仅支持输入0x/0X、a-f/A-F、0-9，允许不输入0x/0X前缀，字母不区分大小写，取值范围0x1~0xFFFF。<br>默认值：无<br>配置原则：无 |
| IMSIMSSEGNAME | IMSI/MSISDN号段名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPREMOVETYPE”配置为“CONDITION”时为可选参数。<br>参数含义：该参数用于指定IMSI/MSISDN的号码段。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的IMSIMSSEGNAME必须是系统已经存在的ImsiMsisdnSeg对象名称。 |
| IMEISVSEGNAME | IMEISV号段名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPREMOVETYPE”配置为“CONDITION”时为可选参数。<br>参数含义：该参数用于指定IMEISV的号码段。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的IMEIVSEGNAME必须是系统已经存在的ImeisvSeg对象名称。 |
| LOCGROUPNAME | 位置组名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPREMOVETYPE”配置为“CONDITION”时为可选参数。<br>参数含义：该参数用于指定位置组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的LOCGROUPNAME必须是系统已经存在的UsrLocationGrp对象名称。 |
| SEGGROUPNAME | IMSI/MSISDN/IMEISV 号段组名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPREMOVETYPE”配置为“CONDITION”时为可选参数。<br>参数含义：该参数用于指定IMSI/MSISDN/IMEISV号码段组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [用户模板组和用户模板的绑定关系（UPBINDUPG）](configobject/UNC/20.15.2/UPBINDUPG.md)

## 使用实例

删除UPBindUPG配置，UserProfGName为userprofg1，UserProfileName为userprofile1：

```
RMV UPBINDUPG:USERPROFGNAME="userprofg1",UPREMOVETYPE=USER_PROFILE_NAME,USERPROFILENAME="userprofile1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用户模板组和用户模板的绑定关系（RMV-UPBINDUPG）_09897231.md`
