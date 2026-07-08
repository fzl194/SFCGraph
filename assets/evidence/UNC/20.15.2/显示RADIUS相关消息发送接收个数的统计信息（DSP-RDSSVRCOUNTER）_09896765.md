# 显示RADIUS相关消息发送接收个数的统计信息（DSP RDSSVRCOUNTER）

- [命令功能](#ZH-CN_CONCEPT_0209896765__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896765__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896765__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896765__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896765__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209896765__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896765)

**适用NF：SGW-C、PGW-C、SMF**

该命令用来查看基于RADIUS服务器的RADIUS相关消息发送接收个数的统计信息。

#### [注意事项](#ZH-CN_CONCEPT_0209896765)

该命令输入的参数必须是已配置的鉴权或者计费服务器的IP地址和VPN。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896765)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896765)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVERTYPE | 服务器类型 | 可选必选说明：必选参数<br>参数含义：指定RADIUS服务器类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- AUTHENTICATION：鉴权服务器。<br>- ACCOUNTING：计费服务器。<br>默认值：无<br>配置原则：无 |
| SERVERIPVER | Server IP Address Version | 可选必选说明：必选参数<br>参数含义：该参数用于指定RADIUS服务器的IP类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| SERVERIP | IP地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SERVERIPVER”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定RADIUS服务器的IP地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制。<br>默认值：无<br>配置原则：无 |
| SERVERIPV6 | Server IPv6 Address | 可选必选说明：条件必选参数<br>前提条件：该参数在“SERVERIPVER”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定RADIUS服务器的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。冒号分十六进制，格式为X:X:X:X:X:X:X:X。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RADIUS服务器的VPN实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：该参数来源为LST RDSSVR中目标Radius服务器的VPNINSTANCE参数值，如果为NULL，则可以不填，否则需要填写。 |

#### [使用实例](#ZH-CN_CONCEPT_0209896765)

查询RADIUS服务器地址为192.168.8.101的统计信息：

```
DSP RDSSVRCOUNTER: SERVERTYPE=ACCOUNTING, SERVERIPVER=IPV4, SERVERIP="192.168.8.101";
```

```

statistics about messages received and sent by a RADIUS
-------------------------------------------------------
Result  =  
              Authentication Responses Received = 1
                   Authentication Requests Sent = 1
            Accounting Start Responses received = 0
                 Accounting Start Requests Sent = 0
        Accounting Real-Time Responses Received = 0
             Accounting Real-Time Requests Sent = 0
             Accounting Stop Responses Received = 0
                  Accounting Stop Requests Sent = 0
                       Invalid Packets Received = 0
                   Disconnect Requests Received = 0
                   Disconnect ACK Messages Sent = 0
                   Disconnect NAK Messages Sent = 0
(Number of results = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209896765)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Result | 该参数用于指定基于RADIUS服务器的RADIUS相关消息发送接收个数的统计信息。 |
