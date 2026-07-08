# 增加M2M服务器（ADD M2MSERVER）

- [命令功能](#ZH-CN_MMLREF_0273321225__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0273321225__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0273321225__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0273321225__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0273321225)

**适用NF：PGW-C、SMF**

该命令用来添加M2M服务器组下的M2M服务器配置。

## [注意事项](#ZH-CN_MMLREF_0273321225)

- 该命令执行后立即生效。

- 最多可输入1000条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0273321225)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0273321225)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | M2M服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定M2M服务器所属M2M服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>GROUPNAME参数依赖M2MSERVERGRP命令的GROUPNAME参数。 |
| SERVERINDEX | M2M服务器索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定M2M服务器索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1。<br>默认值：无<br>配置原则：无 |
| SERVERIPTYPE | M2M服务器IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定M2M服务器IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：<br>SERVERIPTYPE参数依赖M2MSERVERGRP命令的SERVERIPTYPE参数。 |
| SERVERIPV4ADDR | M2M服务器IPv4地址 | 可选必选说明：该参数在"SERVERIPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定M2M服务器IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。必须是合法的单播地址。<br>默认值：无<br>配置原则：无 |
| SERVERIPV6ADDR | M2M服务器IPv6地址 | 可选必选说明：该参数在"SERVERIPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定M2M服务器IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。必须是合法的单播地址。<br>默认值：无<br>配置原则：无 |
| SERVERPORT | 服务器端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定M2M服务器的端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。该端口号应与M2M服务器的端口一致。<br>默认值：5683<br>配置原则：无 |
| REALMSWITCH | 域名配置开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否配置域名。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：DISABLE<br>配置原则：无 |
| SERVERREALM | M2M服务器域名 | 可选必选说明：该参数在"REALMSWITCH"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于指定M2M Server的域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0273321225)

在“m2msrvgroup01”M2M服务器组下新增一个M2M服务器：

```
ADD M2MSERVER: GROUPNAME="m2msrvgroup01", SERVERINDEX=1, SERVERIPTYPE=IPV4, SERVERIPV4ADDR="10.107.242.16", SERVERPORT=5858;
```
