---
id: UNC@20.15.2@MMLCommand@SET AMFN26CPPATH
type: MMLCommand
name: SET AMFN26CPPATH（设置AMF N26消息抄送路径）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AMFN26CPPATH
command_category: 配置类
applicable_nf:
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- N26互操作管理
- N26消息抄送路径
status: active
---

# SET AMFN26CPPATH（设置AMF N26消息抄送路径）

## 功能

**适用网元：MME、AMF**

该命令用于4/5G融合部署时，对于AMF/MME内部的4/5G互操作流程，AMF/MME支持通过该命令配置的路径，抄送一条重复N26消息报文。

## 注意事项

- 该命令执行后立即生效。
- 该功能只在特定局点生效，请联系华为技术支持确认是否可以使用。

## 权限

manage-ug；system-ug。
G_1，管理员级别命令组；G_2，操作员级别命令组。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPPATHSW | 抄送路径开关 | 可选必选说明：可选参数<br>参数含义：本参数用于指示AMF/MME是否开启抄送路径功能。开关开启后，对于AMF/MME内部4/5G互操作产生的N26接口消息，AMF/MME会通过该命令配置的路径抄送一条重复N26消息报文。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”<br>- “ON（打开）”<br>系统初始设置值：“OFF（关闭）”<br>默认值：无。<br>执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过相关查询命令获取当前参数配置值。<br>配置原则：无 |
| IPTYPE | IP地址类型 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定抄送路径的IP地址类型。<br>前提条件：该参数在“抄送路径开关”参数配置为“ON（打开）”后生效。<br>数据来源：全网规划<br>取值范围：<br>- “TPTADDR_TYPE_IPV4(IPv4)”<br>- “TPTADDR_TYPE_IPV6(IPv6)”<br>- “TPTADDR_TYPE_IPV4IPV6(IPv4IPv6)”<br>默认值：无<br>说明：当本参数设置为“TPTADDR_TYPE_IPV4IPV6”时，抄送路径按照原始消息的IP地址类型选择对应的IP地址类型。 |
| MMECPIPV4 | MME侧IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定抄送路径的MME侧N26接口IPv4地址。<br>前提条件：该参数在“IP地址类型”参数配置为“TPTADDR_TYPE_IPV4(IPv4)”或“TPTADDR_TYPE_IPV4IPV6(IPv4IPv6)”后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- IP地址请确保为外部不可用地址，避免消息发给该地址后产生非预期影响。比如：收到非预期消息导致过载、拥塞、甚至复位等。 |
| MMECPIPV6 | MME侧IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定抄送路径的MME侧N26接口IPv6地址。<br>前提条件：该参数在“IP地址类型”参数配置为“TPTADDR_TYPE_IPV6(IPv6)”或“TPTADDR_TYPE_IPV4IPV6(IPv4IPv6)”后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- IP地址请确保为外部不可用地址，避免消息发给该地址后产生非预期影响。比如：收到非预期消息导致过载、拥塞、甚至复位等。 |
| AMFCPIPV4 | AMF侧IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定抄送路径的AMF侧N26接口IPv4地址。<br>前提条件：该参数在“IP地址类型”参数配置为“TPTADDR_TYPE_IPV4(IPv4)”或“TPTADDR_TYPE_IPV4IPV6(IPv4IPv6)”后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- IP地址请确保为外部不可用地址，避免消息发给该地址后产生非预期影响。比如：收到非预期消息导致过载、拥塞、甚至复位等。 |
| AMFCPIPV6 | AMF侧IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定抄送路径的AMF侧N26接口IPv6地址。<br>前提条件：该参数在“IP地址类型”参数配置为“TPTADDR_TYPE_IPV6(IPv6)”或“TPTADDR_TYPE_IPV4IPV6(IPv4IPv6)”后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- IP地址请确保为外部不可用地址，避免消息发给该地址后产生非预期影响。比如：收到非预期消息导致过载、拥塞、甚至复位等。 |
| VPNNAME | VPN名称 | 可选必选说明：条件可选参数<br>参数含义：本参数用于指定MME侧地址对应的VPN名称。<br>数据来源：全网规划<br>取值范围：0~31位字符串<br>默认值：无<br>配置原则：<br>- 本参数必须与MME侧N26接口（ADD GTPCLE）的VPN名称配置一致。<br>- 输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFN26CPPATH]] · AMF N26消息抄送路径（AMFN26CPPATH）

## 使用实例

开启AMF N26消息抄送路径功能，抄送路径使用IPv4地址，MME侧地址为192.168.1.1，AMF侧地址为192.168.2.2，VPN名称为_abc_执行如下命令：

```
SET AMFN26CPPATH: CPPATHSW=ON, IPTYPE=TPTADDR_TYPE_IPV4, MMECPIPV4="192.168.1.1", AMFCPIPV4="192.168.2.2", VPNNAME="_abc_";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置AMF-N26消息抄送路径（SET-AMFN26CPPATH）_30308792.md`
