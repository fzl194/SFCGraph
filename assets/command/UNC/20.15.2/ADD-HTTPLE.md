---
id: UNC@20.15.2@MMLCommand@ADD HTTPLE
type: MMLCommand
name: ADD HTTPLE（增加HTTP本端实体）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: HTTPLE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP本端实体管理
status: active
---

# ADD HTTPLE（增加HTTP本端实体）

## 功能

该命令用于增加HTTP本端实体。HTTP是Hyper Text Transfer Protocol协议的缩写，是一个基于TCP/IP通讯协议来传递数据的传输协议，工作于客户端-服务端架构上。NF实例既可能是客户端形态也可能是服务端形态，可通过本命令配置该协议的本端地址、端口号并指定为客户端还是服务端。

## 注意事项

- 该命令执行后立即生效。

- 客户端和服务端相同IP地址时，服务端端口号不能在[24576,32767]范围内。
- 本端实体类型配置为客户端时，同一个IP地址只能配置一条记录。如果没有配置“TLSIDX”，而实际建立的是HTTPs链路，则使用系统缺省TLS参数创建链路。如果配置了“TLSIDX”，而实际建立的是HTTP链路，则“TLSIDX”不生效。
- 本端实体类型配置为服务端时，同一个IP地址和端口号只能配置一条记录。
- IP地址相同的记录，“HTTP本端实体组标识”、“VPN名称”及“路由标记” 必须相同。
- 本端实体类型配置为客户端时，若配置了"TLSIDX"字段，则需要保证相同本端实体组内所有客户端配置的"TLSIDX"字段的值相同。
- 本端实体类型为客户端时，若相同本端实体组内，存在其他VPN的客户端配置，则需要通过[**ADD HTTPVPNMAP**](../HTTP VPN映射管理/增加HTTP VPN映射关系（ADD HTTPVPNMAP）_46111673.md)配置该本端实体组内所有VPN的映射关系。

- 最多可输入128条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | HTTPLE本端实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP本端实体的索引信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| HTTPLEGRPIDX | HTTP本端实体组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP本端实体所属的HTTP本端实体组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~64。<br>默认值：无<br>配置原则：<br>执行本命令前，需要先确认HTTPLEGRPIDX已经通过<br>[**ADD HTTPLEGRP**](../HTTP本端实体组管理/增加HTTP本端实体组（ADD HTTPLEGRP）_29213277.md)<br>添加。 |
| LETYPE | 本端实体类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP本端实体的类型。<br>数据来源：全网规划<br>取值范围：<br>- “SERVER（服务端）”：服务端<br>- “CLIENT（客户端）”：客户端<br>默认值：无<br>配置原则：<br>HTTP本端实体可以作为服务端也可以作为客户端，两者需要分别配置。 |
| PORT | 端口号 | 可选必选说明：该参数在"LETYPE"配置为"SERVER"时为条件可选参数。<br>参数含义：该参数用于指定HTTP本端实体所使用的端口号。<br>- 在"LETYPE"配置为"SERVER"时：如果配置了本端端口号，则以配置为准。如果没有配置本端端口号，则：默认不开启TLS时，使用端口号80。开启TLS时，使用端口号443。<br>- 在"LETYPE"配置为"CLIENT"时：如果HTTP链路动态生成，则端口号由系统自动生成，配置的端口号无效。如果HTTP链路为静态生成，则本端端口号以配置为准。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：无 |
| TLSFLG | 是否启用TLS | 可选必选说明：该参数在"LETYPE"配置为"SERVER"时为条件必选参数。<br>参数含义：该参数用于指定本端HTTP实体为服务端时是否开启TLS(Transport Layer Security，传输层安全协议)。开启TLS以后，基于服务化接口的HTTP层报文会基于该TLS传输加密，可提升传输的安全性。<br>数据来源：全网规划<br>取值范围：<br>- “NO（NO）”：否<br>- “YES（YES）”：是<br>默认值：YES<br>配置原则：无 |
| TLSIDX | TLS索引 | 可选必选说明：该参数在"TLSFLG"配置为"YES"时为条件必选参数。该参数在"LETYPE"配置为"CLIENT"时为条件可选参数。<br>参数含义：该参数用于指定关联的TLSPARA的索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置的地址的IP类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPv4（IPv4地址）”：IPv4地址<br>- “IPv6（IPv6地址）”：IPv6地址<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>必须配置LOGICIP中已有地址，可以通过<br>[**ADD LOGICIP**](../../../IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)<br>添加。 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>必须配置LOGICIP中已有地址，可以通过<br>[**ADD LOGICIP**](../../../IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)<br>添加。 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：<br>该参数在同一个HTTP服务实体组下需要配置一致。若用户没有输入或输入为"_public_"，则认为是公网。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP本端实体的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。 |
| RFLAG | 路由标记 | 可选必选说明：可选参数<br>参数含义：网元处于主备容灾场景下时，备网元上是否抑制该地址对外发布路由。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：<br>TRUE表示抑制备网元发布路由，FALSE表示不抑制备网元发布路由。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HTTPLE]] · HTTP本端实体（HTTPLE）

## 使用实例

若运营商要配置一条HTTP本端实体信息，索引为1，HTTP本端实体组标识为1，本端实体类型为CLIENT，IP类型为IPv4，地址为192.168.4.15，VPN名称为"_public_"，关联的TLS配置索引是1，可以用如下命令

```
ADD HTTPLE: INDEX=1, HTTPLEGRPIDX=1, LETYPE=CLIENT, IPTYPE=IPv4, IPV4="192.168.4.15", VPNNAME="_public_", TLSIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-HTTPLE.md`
