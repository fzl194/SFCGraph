---
id: UNC@20.15.2@MMLCommand@MOD LOCRPTCFG
type: MMLCommand
name: MOD LOCRPTCFG（修改位置上报配置信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: LOCRPTCFG
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- P-GW属性
status: active
---

# MOD LOCRPTCFG（修改位置上报配置信息）

## 功能

**适用网元：SGSN、MME**

该命令用于修改位置上报配置信息。

## 注意事项

- 该命令执行后对修改配置前的上报任务不影响。
- 该表的最大元组数为1024。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。
- 当P-GW的信令面地址为双栈时，优先匹配IPv4的记录，再匹配IPv6的记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 对端设备范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要位置上报配置信息的对端设备GGSN/P-GW范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_GGSN/P-GW（所有GGSN/P-GW）”<br>- “HOME_GGSN/P-GW（本网GGSN/P-GW）”<br>- “FOREIGN_GGSN/P-GW（外网GGSN/P-GW）”<br>- “SPECIFIC_GGSN/P-GW（指定IP的GGSN/P-GW）”<br>默认值： 无<br>配置原则：<br>- 系统中只能配置一条“ALL_GGSN/P-GW（所有GGSN/P-GW）”的记录。当系统中已存在一条“ALL_GGSN/P-GW（所有GGSN/P-GW）”的记录时，如果再增加一条“ALL_GGSN/P-GW（所有GGSN/P-GW）”的记录，新记录会将旧记录覆盖。<br>- 系统中只能配置一条“HOME_GGSN/P-GW（本网GGSN/P-GW）”的记录。当系统中已存在一条“HOME_GGSN/P-GW（本网GGSN/P-GW）”的记录时，如果在客户端再增加一条“HOME_GGSN/P-GW（本网GGSN/P-GW）”的记录，新记录将添加失败。<br>- 系统中只能配置一条“FOREIGN_GGSN/P-GW（外网GGSN/P-GW）”的记录。当系统中已存在一条“FOREIGN_GGSN/P-GW（外网GGSN/P-GW）”的记录时，如果在客户端再增加一条“FOREIGN_GGSN/P-GW（外网GGSN/P-GW）”的记录，新记录将添加失败。<br>- 系统中可以配置多条“SPECIFIC_GGSN/P-GW（指定IP的GGSN/P-GW）”的记录，但是IP网段区间不能重叠。<br>- 优先级关系：“SPECIFIC_GGSN/P-GW（指定IP的GGSN/P-GW）”>“HOME_GGSN/P-GW（本网GGSN/P-GW）”=“FOREIGN_GGSN/P-GW（外网GGSN/P-GW）”>“ALL_GGSN/P-GW（所有GGSN/P-GW）”。 |
| IPT | IP地址类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GGSN/P-GW信令面IP地址类型。<br>前提条件：只有在<br>“RANGE”<br>配置为<br>“SPECIFIC_GGSN/P-GW（指定IP的GGSN/P-GW）”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| GWIPV4 | GGSN/P-GW的信令面IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GGSN/P-GW信令面IPv4地址。<br>前提条件：只有在<br>“IPT”<br>配置为<br>“IPV4”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：0.0.0.1～255.255.255.254<br>默认值：无<br>说明：- 有效IPv4地址不能为0.0.0.0、255.255.255.255和环回地址（127.x.y.z）。<br>- 有效的IPv4地址必须是A、B或者C类地址。 |
| MASKV4 | 掩码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端GGSN/P-GW的信令面IPv4地址的掩码。<br>前提条件：只有在<br>“IPT”<br>配置为<br>“IPV4”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值： 无<br>说明：- “0.0.0.0”是无效掩码。<br>- 输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。 |
| GWIPV6 | GGSN/P-GW的信令面IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GGSN/P-GW信令面IPv6地址。<br>前提条件：只有在<br>“IPT”<br>配置为<br>“IPV6”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>说明：- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）和组播地址（FF00::/8）。 |
| MASKV6 | 子网前缀长度 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定子网前缀的长度。<br>前提条件：只有在<br>“IPT”<br>配置为<br>“IPV6”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：1～128（数值型）<br>默认值： 无 |
| LOCRPT | 支持位置上报功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GGSN/P-GW是否支持位置上报功能。<br>数据来源：与对端GGSN/P-GW网元协商一致<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>说明：- 当参数设置为“YES(是)”时，“小区位置信息上报功能（S11接口）”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-10640，license部件编码：LKV2LCR01）。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置上报配置信息的相关描述。<br>数据来源：整网规划<br>取值范围：1～32位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCRPTCFG]] · 位置上报配置信息（LOCRPTCFG）

## 使用实例

修改记录，修改用户范围为 “SPECIFIC_GGSN/P-GW（指定IP的GGSN/P-GW）” ，信令面IP地址为 “10.10.10.18” ，掩码为 “255.255.255.255” 的记录，将其修改成不支持实时上报，描述为 “GGSN01” ：

MOD LOCRPTCFG: RANGE=SPECIFIC_GGSN/P-GW, IPT=IPV4, GWIPV4="10.10.10.18", MASKV4="255.255.255.255", LOCRPT=NO, DESC="GGSN01";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改位置上报配置信息(MOD-LOCRPTCFG)_26145938.md`
