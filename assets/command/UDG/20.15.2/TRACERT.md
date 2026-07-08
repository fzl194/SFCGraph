---
id: UDG@20.15.2@MMLCommand@TRACERT
type: MMLCommand
name: TRACERT（IP Tracert）
nf: UDG
version: 20.15.2
verb: TRACERT
object_keyword: ''
command_category: 调测类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- 系统维护
- Ping和Tracert
- Tracert
status: active
---

# TRACERT（IP Tracert）

## 功能

TRACERT命令用来测试数据包从发送主机到目的地所经过的路径节点。对于网络中出现的故障，可以执行PING命令，根据回应的报文查看网络连通的情况，然后进一步使用该命令查看网络中出现故障的位置，为故障诊断提供依据。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP协议版本号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定探测报文的IP协议版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4协议族。<br>- IPv6：IPv6协议族。<br>默认值：无 |
| VPNNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| SOURCEIPV4ADDRESS | 源IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为可选参数。<br>参数含义：该参数用于指定源IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| SOURCEIPV6ADDRESS | 源IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为可选参数。<br>参数含义：该参数用于指定源IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| DESTIPV4ADDRESS | 目的IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于指定目的主机IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| DESTIPV6ADDRESS | 目的IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于指定目的主机IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| DESTPORT | 目的端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定目的主机的UDP端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：33434 |
| TIMEOUT | 超时时间（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定等待响应报文的超时时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20000，单位是毫秒。<br>默认值：5000 |
| FIRSTTTL | 初始TTL | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为可选参数。<br>参数含义：该参数用于指定初始TTL。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：1 |
| MAXTTL | 最大TTL | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为可选参数。<br>参数含义：该参数用于指定最大TTL。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：30 |
| FIRSTHOPLIMIT | 初始跳限制 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为可选参数。<br>参数含义：该参数用于指定初始跳限制。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：1 |
| MAXHOPLIMIT | 最大跳限制 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为可选参数。<br>参数含义：该参数用于指定最大跳限制。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：30 |
| IPV4PACKETSIZE | IPv4报文字节数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为可选参数。<br>参数含义：该参数用于指定IPv4报文大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为12～9600，单位是字节。<br>默认值：12 |
| IPV6PACKETSIZE | IPv6报文字节数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为可选参数。<br>参数含义：该参数用于指定IPv6报文大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为20～9600，单位是字节。<br>默认值：20 |
| PACKETCOUNT | 发包数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定每次发送的探测数据包个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535，单位是包数。<br>默认值：3 |
| MPLSLABEL | 显示MPLS标签信息 | 可选必选说明：可选参数<br>参数含义：该参数用于显示ICMP超时报文带回的MPLS标签信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：去使能。<br>默认值：无<br>配置原则：如果不输入该参数，则表示不显示MPLS标签。 |

## 使用实例

- 检查从发送主机到IP地址为10.137.144.1的主机所经过的路径节点：
  ```
  TRACERT: IPVERSION=IPv4, DESTIPV4ADDRESS="10.137.144.1";
  ```
  ```

   traceroute to 10.137.144.1(10.137.144.1), max hops: 30, packet length: 40

   1 10.137.144.1 2 ms

   1 10.137.144.1 1 ms

   1 10.137.144.1 1 ms

  共有7个报告
  ---    END
  ```
- 检查从发送主机到IPv6地址为2001:db8::1的主机所经过的路径节点：
  ```
  TRACERT: IPVERSION=IPv6, DESTIPV6ADDRESS="2001:db8::1";
  ```
  ```

    traceroute to 2001:db8::1  30 hops max, 60 bytes packet

   1 2001:db8::1 107 ms

   1 2001:db8::1 1 ms

   1 2001:db8::1 1 ms

  共有7个报告
  ---    END
  ```
- 检查从发送主机到IP地址为10.137.144.1的主机所经过的路径节点，同时显示经过节点的标签信息：
  ```
  TRACERT: IPVERSION=IPv4, DESTIPV4ADDRESS="10.137.144.1", MPLSLABEL=ENABLE;
  ```
  ```

   traceroute to 10.137.144.1(10.137.144.1), max hops: 30, packet length: 40

   1 10.137.144.1[MPLS Label=32894 Exp=0 S=1 TTL=1] 2 ms

   1 10.137.144.1[MPLS Label=32894 Exp=0 S=1 TTL=1] 1 ms

   1 10.137.144.1[MPLS Label=32894 Exp=0 S=1 TTL=1] 1 ms

  共有7个报告
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/TRACERT.md`
