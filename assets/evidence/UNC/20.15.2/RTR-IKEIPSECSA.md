# 恢复IPSEC安全联盟（RTR IKEIPSECSA）

- [命令功能](#ZH-CN_MMLREF_0000001225830703__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001225830703__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001225830703__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001225830703__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001225830703)

![](恢复IPSEC安全联盟（RTR IKEIPSECSA）_25830703.assets/notice_3.0-zh-cn_2.png)

恢复IPSEC安全联盟后，IPSEC安全联盟会重新协商，会导致业务短时间中断。

该命令用于恢复IPSEC安全联盟。

## [注意事项](#ZH-CN_MMLREF_0000001225830703)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001225830703)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001225830703)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESETTYPE | 清除类型 | 可选必选说明：必选参数<br>参数含义：清除类型。<br>数据来源：本端规划<br>取值范围：枚举类型。 all：指定IP版本的所有安全联盟。 ahAndIpAddr：指定IP版本的Ah SPI和ip地址。 espAndIpAddr：指定IP版本的Esp SPI和ip地址。 polName：指定IP版本的策略名称。 polNameAndSeqNum：指定IP版本的策略名称和序列号。 remAddr：指定IP版本的远端地址。<br>- “All（所有）”：所有<br>- “AhAndIpAddr（Ah SPI和IP地址）”：Ah SPI和IP地址<br>- “EspAndIpAddr（Esp SPI和IP地址）”：Esp SPI和IP地址<br>- “PolName（策略名称）”：策略名称<br>- “PolNameAndSeqNum（策略名称和序列号）”：策略名称和序列号<br>- “RemAddr（远端地址）”：远端地址<br>默认值：无<br>配置原则：<br>必选参数。 |
| AHSPI | AH SPI | 可选必选说明：该参数在"RESETTYPE"配置为"AhAndIpAddr"时为条件必选参数。<br>参数含义：AH SPI。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是256~4294967295。整数类型，取值范围为256～4294967295。<br>默认值：无<br>配置原则：<br>该参数在“RESETTYPE”配置为“ahAndIpAddr”时为必选参数。 |
| ESPSPI | ESP SPI | 可选必选说明：该参数在"RESETTYPE"配置为"EspAndIpAddr"时为条件必选参数。<br>参数含义：ESP SPI。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是256~4294967295。整数类型，取值范围为256～4294967295。<br>默认值：无<br>配置原则：<br>该参数在“RESETTYPE”配置为“espAndIpAddr”时为必选参数。 |
| IPVERSION | 远端地址IP版本 | 可选必选说明：可选参数<br>参数含义：IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- “IPv4（远端地址格式为IPv4）”：远端地址格式为IPv4<br>- “IPv6（远端地址格式为IPv6）”：远端地址格式为IPv6<br>默认值：IPv4<br>配置原则：<br>必选参数。 |
| IPADDRESS | IP地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件可选参数。<br>参数含义：IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。IPv4地址类型。<br>默认值：无<br>配置原则：<br>该参数在“RESETTYPE”配置为“ahAndIpAddr”、“espAndIpAddr”或“remAddr”并且“IPVERSION”为“IPv4”时为必选参数。 |
| IPADDRESS6 | IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件可选参数。<br>参数含义：IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。IPv6地址类型。<br>默认值：无<br>配置原则：<br>该参数在“RESETTYPE”配置为“ahAndIpAddr”、“espAndIpAddr”或“remAddr”并且“IPVERSION”为“IPv6”时为必选参数。 |
| POLICYNAME | 策略名称 | 可选必选说明：该参数在"RESETTYPE"配置为"PolName"、"PolNameAndSeqNum"时为条件必选参数。<br>参数含义：策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。字符串类型，输入长度范围为1～15。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数在“RESETTYPE”配置为“polName” 或 “polNameAndSeqNum”时为必选参数。 |
| SEQUENCENUMBER | 序列号 | 可选必选说明：该参数在"RESETTYPE"配置为"PolNameAndSeqNum"时为条件必选参数。<br>参数含义：序列号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~10000。整数类型，取值范围为1～10000。<br>默认值：无<br>配置原则：<br>该参数在“RESETTYPE”配置为“polNameAndSeqNum”时为必选参数。 |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。字符串类型，输入长度范围为0～63。<br>默认值：无<br>配置原则：<br>该参数在“RESETTYPE”配置为“all”、“ahAndIpAddr”、“espAndIpAddr”、“polName”、“polNameAndSeqNum” 或 “remAddr”时为可选参数。 |

## [使用实例](#ZH-CN_MMLREF_0000001225830703)

恢复AH SPI为3365093594，IP版本为IPv4的IPSEC SA：

```
RTR IKEIPSECSA:RESETTYPE=AhAndIpAddr,AHSPI=3365093594,IPVERSION=IPv4;
```
