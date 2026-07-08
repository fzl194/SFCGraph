---
id: UDG@20.15.2@MMLCommand@NGTRACEROUTE
type: MMLCommand
name: NGTRACEROUTE
nf: UDG
version: 20.15.2
verb: NGTRACEROUTE
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

# NGTRACEROUTE

## 功能

该命令用来在网络连接中测试数据包从发送主机到目的地所经过的网关。对于网络中出现的故障，可以先执行 [**NGPING**](NGPING（NGPING）_09587930.md) 命令，根据回应的报文查看网络连通的情况，然后使用该命令查看网络中出现故障的位置，为故障诊断提供依据。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于描述IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPv4（IPv4）<br>- IPv6（IPv6）<br>默认值：无<br>配置原则：无 |
| VPNNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：_public_<br>配置原则：无 |
| SRCIPV4ADDR | 源IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定源IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| DSTIPV4ADDR | 目的IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定目的主机IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| SRCIPV6ADDR | 源IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定源IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| DSTIPV6ADDR | IPv6目的地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定目的主机IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| DSTPORT | 目的端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定目的主机的UDP端口号。当前不支持该参数。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：33333<br>配置原则：无 |
| TIMEOUT | 超时时间(ms) | 可选必选说明：可选参数<br>参数含义：该参数用于指定等待响应报文的超时时间。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：5000<br>配置原则：无 |
| FIRSTTTL | 初始TTL | 可选必选说明：可选参数<br>参数含义：该参数用于指定初始TTL。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：1<br>配置原则：无 |
| MAXTTL | 最大TTL | 可选必选说明：可选参数<br>参数含义：该参数用于指定最大TTL。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：30<br>配置原则：无 |
| PACKETNUM | 发包数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定每次发送的探测数据包个数。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：3<br>配置原则：无 |
| PACKETSIZE | 报文大小 | 可选必选说明：可选参数<br>参数含义：该参数用于指定报文大小。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是20~9600。<br>默认值：80<br>配置原则：无 |

## 使用实例

- 目的地址可达情景，检查从发送主机到IP地址为fc00:135:189:242:0:0:0:181的主机所经过的网关。
  ```
  NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:135:193:135:0:0:0:108", DSTIPV6ADDR="fc00:135:189:242:0:0:0:181", PACKETNUM=1; 

  %%NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:135:193:135:0:0:0:108", DSTIPV6ADDR="fc00:135:189:242:0:0:0:181", PACKETNUM=1;%%
  RETCODE = 99999  Real Time Report Success

  1  fc00:135:193:136::254 27.453ms 

  仍有后续报告输出
  ---    END

  %%NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:135:193:135:0:0:0:108", DSTIPV6ADDR="fc00:135:189:242:0:0:0:181", PACKETNUM=1;%%
  RETCODE = 99999  Real Time Report Success

  2  fc00:135:189:242:0:0:0:181 8.629ms

  仍有后续报告输出
  ---    END

  %%NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:135:193:135:0:0:0:108", DSTIPV6ADDR="fc00:135:189:242:0:0:0:181", PACKETNUM=1;%%
  RETCODE = 0  操作成功

  Trace Completed
  Total Receive :2
  round-trip min/avg/max=8.629/18.041/27.453ms

  共有3个报告
  ---    END
  ```
- 目的地址不可达情景，检查从发送主机到IP地址为fc00:18:0:0:0:0:132:140的主机所经过的网关。
  ```
  NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:140", MAXTTL=3, PACKETNUM=1;

  %%NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:140", MAXTTL=3, PACKETNUM=1;%%
  RETCODE = 99999  Real Time Report Success

  1  * 

  仍有后续报告输出
  ---    END

  %%NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:140", MAXTTL=3, PACKETNUM=1;%%
  RETCODE = 99999  Real Time Report Success

  2  * 

  仍有后续报告输出
  ---    END

  %%NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:140", MAXTTL=3, PACKETNUM=1;%%
  RETCODE = 0  操作成功

  Trace Completed
  Total Receive :0
  round-trip min/avg/max=0.000/0.000/0.000ms

  共有3个报告
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/NGTRACEROUTE（NGTRACEROUTE）_09587949.md`
