---
id: UNC@20.15.2@MMLCommand@ADD AGENTIP
type: MMLCommand
name: ADD AGENTIP（增加远端地址池代理IP信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: AGENTIP
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
- 接入管理
- UE地址管理
- UE地址池管理
- 代理IP管理
status: active
---

# ADD AGENTIP（增加远端地址池代理IP信息）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于添加远端地址池的代理IP地址和IP地址请求消息中必须携带的代理IP地址。

DHCP服务器查找包含该代理IP地址的地址池，按照DHCP服务器上的地址分配策略分配IP地址给UNC，再由UNC下发给UE。

## 注意事项

- 该命令执行后立即生效。

- 配置代理IP前，需要先执行ADD ADDRPOOL配置远端地址池。
- 最多可输入6000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置代理IP地址的地址池名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“_”、“#”、“$”和“&”等，由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOL命令配置生成。 |
| SECTIONNUM | 地址段号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置代理IP地址的地址段号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~63，65535。<br>默认值：65535<br>配置原则：<br>当没有配置地址段时，此DHCP服务器分配的地址采用主机路由方式发布。当该参数的取值为65535时，表示该参数无效。 |
| IPVERSION | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置代理IP地址的地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4地址类型）<br>- IPV6（IPv6地址类型）<br>默认值：无<br>配置原则：无 |
| V4AGENTIP | IPv4代理地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定IPv4代理地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。只允许配置A、B、C类地址。<br>默认值：无<br>配置原则：<br>DHCPv4服务器根据此V4AGENTIP，在相应地址池中按照分配策略选取一个IP地址分配给UE。 |
| V6AGENTIP | IPv6代理地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定IPv6代理地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。除了组播地址、链路本地地址、环回地址或未指定的地址为非法地址外，其他都为合法地址。<br>默认值：无<br>配置原则：<br>DHCPv6服务器根据此V6AGENTIP，在相应地址池中按照分配策略选取一个IP地址分配给UE。 |

## 操作的配置对象

- [远端地址池代理IP信息（AGENTIP）](configobject/UNC/20.15.2/AGENTIP.md)

## 使用实例

配置远端地址池testpool的代理地址，配置完成后，DHCPv4 服务器可以从testpool编号为0的地址段中分配地址：

```
ADD AGENTIP:POOLNAME="testpool",SECTIONNUM=0,IPVERSION=IPV4,V4AGENTIP="10.10.110.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加远端地址池代理IP信息（ADD-AGENTIP）_32224047.md`
