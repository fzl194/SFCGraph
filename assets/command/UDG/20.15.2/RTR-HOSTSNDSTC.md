---
id: UDG@20.15.2@MMLCommand@RTR HOSTSNDSTC
type: MMLCommand
name: RTR HOSTSNDSTC（清除发送方向协议报文统计计数）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: HOSTSNDSTC
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IP协议统计
- 主机报文统计
- 发送报文统计
status: active
---

# RTR HOSTSNDSTC（清除发送方向协议报文统计计数）

## 功能

该命令用于清除发送方向协议报文统计计数。

当不指定RUNAME参数时，清除所有资源单元的统计信息；当指定RUNAME参数时，可以清除指定资源单元的统计信息。

当不指定PROTTYPE参数时，清除所有协议类型的统计信息；当指定PROTTYPE参数时，可以清除指定协议类型的统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTTYPE | 协议类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示协议类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ARP：ARP协议类型。<br>- ICMP：ICMP协议类型。<br>- OSPF：OSPF协议类型。<br>- SNMP：SNMP协议类型。<br>- UDP_OTHER：其它UDP协议类型。<br>- BGP：BGP协议类型。<br>- LDP：LDP协议类型。<br>- TCP_OTHER：其它TCP协议类型。<br>- ICMPV6：ICMPv6协议类型。<br>- OSPFV3：OSPFv3协议类型。<br>- IPV6UDP_OTHER：其它IPv6 UDP协议类型。<br>- IPV6TCP_OTHER：其它IPv6 TCP协议类型。<br>默认值：无<br>配置原则：如果不输入该参数，则表示所有协议类型。 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用DSP RU命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HOSTSNDSTC]] · 发送方向协议报文统计计数（HOSTSNDSTC）

## 使用实例

- 清除发送方向指定协议的协议报文统计计数：
  ```
  RTR HOSTSNDSTC: PROTTYPE=TCP_OTHER;
  ```
- 清除发送方向指定资源单元指定协议类型的协议报文统计计数：
  ```
  RTR HOSTSNDSTC: RUNAME="VNODE_VNRS_VNFC_OMU_0001", PROTTYPE=TCP_OTHER;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RTR-HOSTSNDSTC.md`
