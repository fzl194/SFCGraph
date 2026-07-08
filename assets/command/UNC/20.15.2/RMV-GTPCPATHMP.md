---
id: UNC@20.15.2@MMLCommand@RMV GTPCPATHMP
type: MMLCommand
name: RMV GTPCPATHMP（删除GTP-C路径管理策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GTPCPATHMP
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C路径策略管理
status: active
---

# RMV GTPCPATHMP（删除GTP-C路径管理策略）

## 功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

本命令用于删除GTP-C路径管理策略。

## 注意事项

- 该命令执行后立即生效。

- 当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 路径范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定该配置影响的GTP-C路径范围。<br>数据来源：全网规划<br>取值范围：<br>- E_HOME（本网）<br>- E_FOREIGN（外网）<br>- E_SPECI_INTF（指定接口）<br>- E_SPECI_IP（指定IP）<br>默认值：无<br>配置原则：无 |
| INTFTYPE | 接口类型 | 可选必选说明：该参数在"RANGE"配置为"E_SPECI_INTF"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的接口类型。<br>数据来源：全网规划<br>取值范围：<br>- S11（S11接口）<br>- N26（N26接口）<br>- S5（S5接口）<br>- S8（S8接口）<br>- GN（Gn接口）<br>- GP（Gp接口）<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP地址类型 | 可选必选说明：该参数在"RANGE"配置为"E_SPECI_IP"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPv4（IPv4）<br>- IPv6（IPv6）<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>业务地址必须是A、B或者C类地址。 |
| IPV4MASK | IPv4地址掩码 | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv4地址掩码。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。 |
| IPV6ADDR | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| IPV6PREFIXLEN | IPv6地址前缀长度 | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv6地址前缀长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCPATHMP]] · GTP-C路径管理策略（GTPCPATHMP）

## 使用实例

删除控制到对端地址为10.2.2.3的GTP-C路径的管理策略配置：

```
RMV GTPCPATHMP:RANGE=E_SPECI_IP,IPTYPE=IPv4,IPV4ADDR="10.2.2.3",IPV4MASK="255.255.255.255";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GTPCPATHMP.md`
