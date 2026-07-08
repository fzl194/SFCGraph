---
id: UNC@20.15.2@MMLCommand@RMV RDSPFCPCTX
type: MMLCommand
name: RMV RDSPFCPCTX（删除RADIUS中转UPF会话上下文）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RDSPFCPCTX
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- RADIUS维护
- RADIUS中转UPF会话信息
status: active
---

# RMV RDSPFCPCTX（删除RADIUS中转UPF会话上下文）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除RADIUS中转UPF会话上下文。

## 注意事项

- 该命令执行后立即生效。

- 该命令会立即删除指定的Radius中转UPF会话。指定对端TEID，不指定对端IP地址时，时会删除TEID相关的所有会话。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RMVTYPE | 删除方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定删除类型。<br>数据来源：本端规划<br>取值范围：<br>- IPTYPE（Radius客户端IP类型）<br>- PEERTEID（RADIUS中转UPF会话中UPF分配的N4口TEID）<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：该参数在"RMVTYPE"配置为"IPTYPE"时为条件必选参数。<br>参数含义：表示Radius客户端的IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：无 |
| CLIENTIPV4 | Radius客户端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：表示Radius客户端的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CLIENTIPV6 | Radius客户端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：表示Radius客户端的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例名称 | 可选必选说明：该参数在"RMVTYPE"配置为"IPTYPE"时为条件可选参数。<br>参数含义：该参数用于指示VPN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。区分大小写。<br>默认值：无<br>配置原则：无 |
| PEERTEID | 对端TEID | 可选必选说明：该参数在"RMVTYPE"配置为"PEERTEID"时为条件必选参数。<br>参数含义：表示Radius中转UPF会话中UPF分配的N4口TEID。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| PEERIPTYPE | 对端IP类型 | 可选必选说明：该参数在"RMVTYPE"配置为"PEERTEID"时为条件可选参数。<br>参数含义：表示对端IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4类型的地址）<br>- IPV6（IPv6类型的地址）<br>默认值：无<br>配置原则：无 |
| PEERIPV4ADDR | 对端IPv4地址 | 可选必选说明：该参数在"PEERIPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：表示Radius中转Upf会话中Upf分配的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV6ADDR | 对端IPv6地址 | 可选必选说明：该参数在"PEERIPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：表示Radius中转Upf会话中Upf分配的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RDSPFCPCTX]] · RADIUS中转UPF会话上下文（RDSPFCPCTX）

## 使用实例

删除Radius IP为192.168.0.1的session context:

```
RMV RDSPFCPCTX: RMVTYPE=IPTYPE, IPTYPE=IPV4, CLIENTIPV4="192.168.0.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RDSPFCPCTX.md`
