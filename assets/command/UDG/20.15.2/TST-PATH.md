---
id: UDG@20.15.2@MMLCommand@TST PATH
type: MMLCommand
name: TST PATH（探测路径）
nf: UDG
version: 20.15.2
verb: TST
object_keyword: PATH
command_category: 调测类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- GTP路径管理
- GTP路径测试
- 探测路径
status: active
---

# TST PATH（探测路径）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于手动控制系统向对端网元（eNodeB、gNodeB、UPF、SGSN、SGW-U、PGW-U、SMF、SGW-C、PGW-C或可信非3GPP接入网关）发送心跳检测消息。

## 注意事项

- 该命令执行后立即生效。
- 如果路径正常，则探测信号发送一次就停止发送。
- 如果路径异常，发送探测信号后没有收到回应，则会根据设置的默认次数发送。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP地址版本类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路径IP地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| LOCALIPV4 | 本端IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定路径的本端IPV4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：无 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定路径的对端ipv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：无 |
| LOCALIPV6 | 本端IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定路径的本端ipv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定对端ipv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| VPNNAME | VPN名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：当下发探测命令时本端IP地址对应的逻辑接口未绑定VPN时，本次探测命令中不需要填写VPN参数。当下发探测命令时本端IP地址对应的逻辑接口绑定了VPN时，本次探测命令的VPN参数需要和此逻辑接口绑定的VPN保持一致。 |
| PROTOCOLTYPE | 协议版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路径的协议版本信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GTPV1：指定GTP协议版本为V1版本。<br>- PFCP：指定PFCP协议版本。<br>- TM：指定TM协议版本。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PATH]] · 探测路径（PATH）

## 使用实例

探测系统地址为10.6.6.1到MME192.168.5.33的GTPv1数据路径通信是否正常：

```
TST PATH: IPVERSION=IPV4, LOCALIPV4="10.6.6.1", PEERIPV4="192.168.5.33", PROTOCOLTYPE=GTPV1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/探测路径（TST-PATH）_82837231.md`
