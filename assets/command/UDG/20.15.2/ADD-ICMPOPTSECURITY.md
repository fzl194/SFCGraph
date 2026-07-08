---
id: UDG@20.15.2@MMLCommand@ADD ICMPOPTSECURITY
type: MMLCommand
name: ADD ICMPOPTSECURITY（增加ICMP选项安全配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ICMPOPTSECURITY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 4096
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv4管理
- ICMP选项安全配置
status: active
---

# ADD ICMPOPTSECURITY（增加ICMP选项安全配置）

## 功能

该命令用于增加ICMP选项安全配置，丢弃TTL=1的ICMP报文。

设备收到IP数据报文后，如果报文的目的地不是本地且报文的TTL字段是1，则会发送TTL超时ICMP差错报文。攻击者通常会利用这一点发送TTL=1的报文攻击设备，设备接收到大量需要发送ICMP差错报文的恶意攻击报文，会因为处理大量该类报文而导致性能降低。此时可以通过icmp ttl-exceeded drop命令丢弃TTL=1的ICMP报文，减轻设备处理ICMP报文的压力，提高网络的性能和增强网络的安全。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为4096。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICMP选项安全配置的RU名称，通过DSP RU命令可以查询资源单元信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| ICMPSECTYPE | ICMP安全类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICMP选项安全配置的ICMP安全类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TTLEXCEEDED：TTL超时报文。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ICMPOPTSECURITY]] · ICMP选项安全配置（ICMPOPTSECURITY）

## 使用实例

创建ICMP选项安全配置：

```
ADD ICMPOPTSECURITY:RUNAME="VNODE_VNRS_VNFC_OMU_0001",ICMPSECTYPE=TTLEXCEEDED;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-ICMPOPTSECURITY.md`
