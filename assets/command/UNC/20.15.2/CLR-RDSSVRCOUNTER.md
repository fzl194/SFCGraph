---
id: UNC@20.15.2@MMLCommand@CLR RDSSVRCOUNTER
type: MMLCommand
name: CLR RDSSVRCOUNTER（清除RADIUS相关消息发送接收个数的统计信息）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: RDSSVRCOUNTER
command_category: 动作类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- RADIUS维护
- 信令计数
status: active
---

# CLR RDSSVRCOUNTER（清除RADIUS相关消息发送接收个数的统计信息）

## 功能

**适用NF：PGW-C、SMF**

该命令用于清除基于RADIUS服务器的RADIUS相关消息发送接收个数的统计信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令输入的参数必须是已配置的鉴权或者计费服务器的IP地址和VPN。
- 执行该命令后，基于RADIUS服务器的IP地址和VPN的服务器接收/发送的RADIUS相关信息的个数统计将清零，并且不能恢复。具体统计信息包括：接收到的鉴权响应的个数、发送的鉴权请求的个数、收到的计费开始响应的个数、发送的计费开始请求的个数、收到的实时计费响应的个数、发送的实时计费请求的个数、收到的计费停止响应的个数、发送的计费停止请求的个数、收到的无效包的个数、收到的去活请求的个数、发送的去活ACK的个数、发送的去活NAK的个数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVERTYPE | 服务器类型 | 可选必选说明：必选参数<br>参数含义：指定RADIUS服务器类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- AUTHENTICATION：鉴权服务器。<br>- ACCOUNTING：计费服务器。<br>默认值：无<br>配置原则：无 |
| SERVERIPVER | Server IP Address Version | 可选必选说明：必选参数<br>参数含义：该参数用于指定RADIUS服务器的IP类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| SERVERIP | IP地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SERVERIPVER”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定RADIUS服务器的IP地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制。<br>默认值：无<br>配置原则：无 |
| SERVERIPV6 | Server IPv6 Address | 可选必选说明：条件必选参数<br>前提条件：该参数在“SERVERIPVER”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定RADIUS服务器的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。冒号分十六进制，格式为X:X:X:X:X:X:X:X。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RADIUS服务器的VPN实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：该参数来源为LST RDSSVR中目标Radius服务器的VPNINSTANCE参数值，如果为NULL，则可以不填，否则需要填写。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RDSSVRCOUNTER]] · RADIUS相关消息发送接收个数的统计信息（RDSSVRCOUNTER）

## 使用实例

清除基于IP地址是192.168.8.101的RADIUS服务器的RADIUS相关统计信息：

```
CLR RDSSVRCOUNTER: SERVERTYPE=ACCOUNTING, SERVERIPVER=IPV4, SERVERIP="192.168.8.101";
RETCODE = 0  Operation Success.

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-RDSSVRCOUNTER.md`
