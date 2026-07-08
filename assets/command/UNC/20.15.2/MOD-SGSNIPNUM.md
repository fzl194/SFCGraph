---
id: UNC@20.15.2@MMLCommand@MOD SGSNIPNUM
type: MMLCommand
name: MOD SGSNIPNUM（修改SGSN控制面IP地址与SGSN号码对应关系）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SGSNIPNUM
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- SGSN地址和SGSN号码对照表
status: active
---

# MOD SGSNIPNUM（修改SGSN控制面IP地址与SGSN号码对应关系）

## 功能

**适用网元：SGSN**

此命令用于修改SGSN控制面IP地址与SGSN号码的对照关系。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| IPV4 | SGSN控制面IP地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定SGSN的控制面IPv4地址。<br>前提条件：当“IP地址类型”为“IPV4(IPV4)”时，该参数有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV6 | SGSN控制面IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定SGSN的控制面IPV6地址。<br>前提条件：当“IP地址类型”为“IPV6(IPV6)”时，该参数有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。 |
| SGSNNUM | SGSN号码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务GPRS支持节点（SGSN）号码，是SGSN的E.164地址。<br>数据来源：整网规划<br>取值范围：长度不超过16的十进制字符串<br>默认值：无 |

## 操作的配置对象

- [SGSN控制面IP地址与SGSN号码对应关系（SGSNIPNUM）](configobject/UNC/20.15.2/SGSNIPNUM.md)

## 使用实例

修改IP地址为10.10.10.16的SGSN控制面IP地址对应的SGSN号码为“861391123456789”：

MOD SGSNIPNUM: IPT=IPV4, IPV4="10.10.10.16", SGSNNUM="861391123456789";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SGSN控制面IP地址与SGSN号码对应关系(MOD-SGSNIPNUM)_26145806.md`
