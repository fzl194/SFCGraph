---
id: UDG@20.15.2@MMLCommand@NGPING
type: MMLCommand
name: NGPING
nf: UDG
version: 20.15.2
verb: NGPING
object_keyword: ''
command_category: 调测类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IP管理
- IP维护
status: active
---

# NGPING

## 功能

该命令用于排查网元间业务IP是否可以PING通。NGPING是最常见的用于检测网络设备可访问性的调试工具，它使用ICMP报文来检测远程设备是否可用、远程主机通信的来回旅程包的丢失情况，无法应用于链路时延的精确判断。

> **说明**
> - 该命令执行后立即生效。
>
> - 当前存在三类PING调测命令：PING、INNERPING、NGPING，差异如下：
>
> - PING：该命令用于排查本网元外联口IP与对端设备之间是否可以PING通。
> - INNERPING、NGPING：该命令用于排查本网元业务IP与对端设备之间是否可以PING通。INNERPING适用场景如下表所示，其他场景均使用NGPING。
> - INNERPING适用场景:
> - a. SGSN/MME的所有接口（使用ADD SERVICEIP配置）。
> - b. AMF的N2、DNS接口（使用ADD SERVICEIP配置）。
> - c. SMSF的MAP接口（使用ADD SERVICEIP配置）。
> - d. CHF的Ga（内部）Server、BI接口（使用ADD IPRESOURCE配置）。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPv4（IPv4）”：IPV4地址<br>- “IPv6（IPv6）”：IPv6地址<br>默认值：无<br>配置原则：无 |
| VPNNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：_public_<br>配置原则：无 |
| SRCIPV4ADDR | 源IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定发送ECHO-REQUEST报文的源IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| DSTIPV4ADDR | 目的IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定目的主机IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| SRCIPV6ADDR | 源IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定发送ECHO-REQUEST报文的源IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| DSTIPV6ADDR | 目的IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定目的主机IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PACKETNUM | 发包数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定发送ECHO-REQUEST报文次数。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：5<br>配置原则：无 |
| PACKETSIZE | 报文字节数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ECHO-REQUEST报文长度（不包括IP和ICMP报文头）。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是20~9600。<br>默认值：80<br>配置原则：无 |
| INTERVAL | 报文间隔(ms) | 可选必选说明：可选参数<br>参数含义：该参数用于指定发送下一个ECHO-REQUEST报文的等待时间。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~10000。<br>默认值：500<br>配置原则：无 |
| TIMEOUT | 超时时间(ms) | 可选必选说明：可选参数<br>参数含义：该参数用于指定发送完ECHO-REQUEST报文后，等待ECHO-REPLY报文的超时时间。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：2000<br>配置原则：无 |
| TTL | TTL值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TTL的值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：255<br>配置原则：无 |

## 使用实例

- 目的地址可达情景，检查IP地址为fc00:18:0:0:0:0:132:120的主机链路。
  ```
  NGPING: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:120", PACKETNUM=2;

  %%NGPING: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:120", PACKETNUM=2;%%
  RETCODE = 99999  Real Time Report Success

  128 bytes from fc00:18::132:120 icmp_seq=1 time=9.880ms ttl=127

  仍有后续报告输出
  ---    END

  %%NGPING: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:120", PACKETNUM=2;%%
  RETCODE = 99999  Real Time Report Success

  128 bytes from fc00:18::132:120 icmp_seq=2 time=2.046ms ttl=127

  仍有后续报告输出
  ---    END

  %%NGPING: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:120", PACKETNUM=2;%%
  RETCODE = 0  操作成功

  ---fc00:18::132:120 ping statistics---
   2 packet(s) transmitted
   2 packet(s) received 
   0.00% packet loss
   round-trip min/avg/max=2.046/9.880/9.880ms

  共有3个报告
  ---    END
  ```
- 目的地址不可达情景：检查IP地址为fc00:18:0:0:0:0:132:140的主机链路。
  ```
  NGPING: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:140", PACKETNUM=2;

  %%NGPING: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:140", PACKETNUM=2;%%
  RETCODE = 99999  Real Time Report Success

  Request timed out.

  仍有后续报告输出
  ---    END

  %%NGPING: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:140", PACKETNUM=2;%%
  RETCODE = 99999  Real Time Report Success

  Request timed out.

  仍有后续报告输出
  ---    END

  %%NGPING: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:140", PACKETNUM=2;%%
  RETCODE = 0  操作成功

  ---fc00:18::132:140 ping statistics---
   2 packet(s) transmitted
   0 packet(s) received 
   100.00% packet loss
   round-trip min/avg/max=0.000/0.000/0.000ms

  共有3个报告
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/NGPING.md`
