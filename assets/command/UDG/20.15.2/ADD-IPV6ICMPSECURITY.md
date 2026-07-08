---
id: UDG@20.15.2@MMLCommand@ADD IPV6ICMPSECURITY
type: MMLCommand
name: ADD IPV6ICMPSECURITY（添加IPv6安全配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: IPV6ICMPSECURITY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 131070
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6安全配置
status: active
---

# ADD IPV6ICMPSECURITY（添加IPv6安全配置）

## 功能

该命令用于添加IPv6安全配置。在需要对ICMPv6报文控制的场景使用。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为131070。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACTION | 发送还是接收 | 可选必选说明：必选参数<br>参数含义：该参数用于表示对ICMP数据包采取的操作的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- rcvPkt：接收报文。<br>- sndPkt：发送报文。<br>默认值：无 |
| CONFIGTYPE | 配置的类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示配置的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- USER：用户自定义。<br>- PKTTYPE：报文类型。<br>默认值：无 |
| ICMPTYPE | 收发报文的TYPE | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGTYPE”配置为“USER”时为必选参数。<br>参数含义：该参数用于表示ICMP6报文类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |
| ICMPCODE | 收发报文的CODE | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGTYPE”配置为“USER”时为必选参数。<br>参数含义：该参数用于表示ICMP6报文编码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |
| SWITCHOP | 开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示是否使能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- disable：去使能。<br>- enable：使能。<br>默认值：无 |
| PKTTYPE | 报文类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGTYPE”配置为“PKTTYPE”时为必选参数。<br>参数含义：该参数用于表示报文类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ECHO：PING请求报文（Type=128, Code=0）。<br>- ECHOREPLY：PING回应报文（Type=129, Code=0）。<br>- ERR_HEADER_FIELD：错误的报头字段（Type=4, Code=0）。<br>- FRAG_TIME_EXCEED：分片重组超时（Type=3, Code=1）。<br>- HOPLIMIT_EXCEED：TTL超时（Type=3, Code=0）。<br>- HOST_ADMIN_PROHIB：与目标的通信被管理策略禁止（Type=1, Code=1）。<br>- HOST_UNREACHABLE：主机不可达（Type=1, Code=3）。<br>- NEIGHBOR_ADVERTISEMENT：邻居应答报文（Type=136, Code=0）。<br>- NEIGHBOR_SOLICITATION：邻居请求报文（Type=135, Code=0）。<br>- NETWORK_UNREACHABLE：网络不可达报文（Type=1, Code=0）。<br>- PACKET_TOOBIG：报文超大（Type=2, Code=0）。<br>- PORT_UNREACHABLE：端口不可达（Type=1, Code=4）。<br>- REDIRECT：重定向（Type=137, Code=0）。<br>- ROUTER_ADVERTISEMENT：路由器通告报文（Type=134, Code=0）。<br>- ROUTER_SOLICITATION：路由器请求报文（Type=133, Code=0）。<br>- UNKNOWN_IPV6_OPT：不识别的IPv6选项报文（Type=4, Code=2）。<br>- UNKNOWN_NEXT_HDR：不识别的下一跳报文（Type=4, Code=1）。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPV6ICMPSECURITY]] · IPv6安全配置（IPV6ICMPSECURITY）

## 使用实例

添加IPv6安全配置：

```
ADD IPV6ICMPSECURITY:SWITCHOP=enable,ACTION=sndPkt,CONFIGTYPE=USER,ICMPTYPE=0,ICMPCODE=0;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-IPV6ICMPSECURITY.md`
