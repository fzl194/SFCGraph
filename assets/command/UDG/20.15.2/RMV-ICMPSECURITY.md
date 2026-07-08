---
id: UDG@20.15.2@MMLCommand@RMV ICMPSECURITY
type: MMLCommand
name: RMV ICMPSECURITY（删除ICMP安全配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ICMPSECURITY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv4管理
- ICMP安全配置
status: active
---

# RMV ICMPSECURITY（删除ICMP安全配置）

## 功能

该命令用于删除ICMP安全配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACTION | 报文方向 | 可选必选说明：必选参数<br>参数含义：该参数表示ICMP安全配置生效的方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- rcvPkt：接收报文。<br>- sndPkt：发送报文。<br>默认值：无 |
| CONFIGTYPE | ICMP配置类型 | 可选必选说明：必选参数<br>参数含义：该参数表示对ICMP安全配置的配置方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- USER：用户自定义。<br>- PKTTYPE：报文类型。<br>默认值：无 |
| PKTTYPE | ICMP报文类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGTYPE”配置为“PKTTYPE”时为必选参数。<br>参数含义：该参数表示创建ICMP安全配置的名称。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- echo：回显请求（Type=8, Code=0）。<br>- echo_reply：ICMP回显应答报文的设置（Type=0, Code=0）。<br>- fragmentneed_dfset：需要分片但设置了不分片标志（Type=3, Code=4）。<br>- host_redirect：主机重定向（Type=5, Code=1）。<br>- host_tos_redirect：主机TOS重定向（Type=5, Code=3）。<br>- host_unreachable：主机不可达（Type=3, Code=1）。<br>- information_reply：信息应答（Type=16, Code=0）。<br>- information_request：信息请求（Type=15, Code=0）。<br>- net_redirect：对网络重定向（Type=5, Code=0）。<br>- net_tos_redirect：网络TOS重定向（Type=5, Code=2）。<br>- net_unreachable：网络不可达（Type=3, Code=0）。<br>- parameter_problem：参数问题（Type=12, Code=0）。<br>- port_unreachable：端口不可达（Type=3, Code=3）。<br>- protocol_unreachable：协议不可达（Type=3, Code=2）。<br>- reassembly_timeout：分片重组超时（Type=11, Code=1）。<br>- source_quench：源抑制报文（Type=4, Code=0）。<br>- source_route_failed：源路由失败（Type=3, Code=5）。<br>- timestamp_reply：时间戳应答（Type=14, Code=0）。<br>- timestamp_request：时间戳请求（Type=13, Code=0）。<br>- ttl_exceeded：TTL超时（Type=11, Code=0）。<br>默认值：无 |
| ICMPTYPE | 类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGTYPE”配置为“USER”时为必选参数。<br>参数含义：该参数表示ICMP安全配置的类型值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |
| ICMPCODE | 编码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONFIGTYPE”配置为“USER”时为必选参数。<br>参数含义：该参数表示ICMP安全配置的消息码值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |

## 操作的配置对象

- [ICMP安全配置（ICMPSECURITY）](configobject/UDG/20.15.2/ICMPSECURITY.md)

## 使用实例

- 指定ICMP报文名称删除系统发送ICMP Echo报文功能ICMP安全配置的配置实例：
  ```
  RMV ICMPSECURITY: ACTION=sndPkt, CONFIGTYPE=PKTTYPE, PKTTYPE=echo;
  ```
- 指定ICMP报文编码删除系统发送ICMP Echo报文功能ICMP安全配置的配置实例：
  ```
  RMV ICMPSECURITY: ACTION=sndPkt, CONFIGTYPE=USER, ICMPTYPE=8, ICMPCODE=0;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除ICMP安全配置（RMV-ICMPSECURITY）_00441301.md`
