# 增加ICAP服务器（ADD ICAPSERVER）

- [命令功能](#ZH-CN_CONCEPT_0000203228751562__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203228751562__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203228751562__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203228751562__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203228751562__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203228751562)

**适用NF：PGW-U、UPF**

该命令用于增加一个ICAP Server相关的配置，包括ICAP Server的主机IP地址、端口、TCP尝试建链间隔、OPTIONS消息重发时间间隔等，用以和对端ICAP Server建立连接，并维护链路状态。

#### [注意事项](#ZH-CN_CONCEPT_0000203228751562)

- 该命令执行后立即生效。
- 该命令最大记录数为30。
- 每种类型的ICAP服务器最多可配置30个。

#### [操作用户权限](#ZH-CN_CONCEPT_0000203228751562)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203228751562)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSERVERNAME | ICAP服务器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。不区分大小写。<br>默认值：无<br>配置原则：无 |
| ICAPSERVERTYPE | ICAP服务器类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server的服务器类型。<br>数据来源：本端规划<br>取值范围：<br>- URL_FILTERING：支持URL过滤的ICAP服务器。<br>默认值：无<br>配置原则：无 |
| ICAPSVRIPTYPE | ICAP 服务器IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server的IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| ICAPSERVERIPV4 | ICAP服务器IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ICAPSVRIPTYPE”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定ICAP Server的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。采用点分十进制格式。不支持0.0.0.0和255.255.255.255。<br>默认值：无<br>配置原则：无 |
| ICAPSERVERIPV6 | ICAP服务器IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ICAPSVRIPTYPE”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定ICAP Server的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。不支持全F。<br>默认值：无<br>配置原则：无 |
| ICAPSERVERPORT | ICAP服务器端口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ICAP Server的通信TCP端口号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1~65534。<br>默认值：1344<br>配置原则：无 |
| VPNINSTANCE | VPN实例 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD VPNINST命令配置生成。 |
| TCPRETRYTIME | TCP尝试建链间隔（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“ICAPSERVERTYPE”配置为“URL_FILTERING”时为可选参数。<br>参数含义：该参数用于指定TCP尝试建链间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~3600。<br>默认值：5<br>配置原则：无 |
| OPTIONINTERVAL | OPTIONS消息的间隔（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定OPTIONS消息的间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~600。<br>默认值：10<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000203228751562)

增加一个ICAP Server相关的配置：

```
ADD ICAPSERVER: ICAPSERVERNAME="is1", ICAPSERVERTYPE=URL_FILTERING, ICAPSVRIPTYPE=IPV4, ICAPSERVERIPV4="172.16.39.136";
```
