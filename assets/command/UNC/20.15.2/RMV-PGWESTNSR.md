---
id: UNC@20.15.2@MMLCommand@RMV PGWESTNSR
type: MMLCommand
name: RMV PGWESTNSR（删除E-STN-SR和PGW关系配置表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PGWESTNSR
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 紧急呼叫配置
- E-STN-SR和PGW关系配置表
status: active
---

# RMV PGWESTNSR（删除E-STN-SR和PGW关系配置表）

## 功能

**适用网元：MME**

该命令用于删除SRVCC的紧急会话转移号码和P-GW关系配置表。记录删除后，在和S-GW交互的时候，将不会携带P-GW对应的“SRVCC的紧急会话转移号码”。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | PGW的IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定P-GW的IP地址类型。<br>数据来源：运营商规划<br>取值范围：<br>- IPV4(IPV4)<br>- IPV6(IPV6)<br>默认值：无 |
| PGWIPV4 | PGW的IPV4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置P-GW的IPv4地址。<br>前提条件：该参数在<br>“PGW的IP地址类型”<br>配置为<br>“IPV4(IPV4)”<br>后生效。<br>数据来源：运营商规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>- 有效IPv4地址不能配置为以0开头、255.255.255.255和环回地址（127.0.0.1）。<br>- IPv4地址必须是A、B或者C类地址。<br>- 该参数与“IPV4MSK”一起指定某个P-GW对应的GTPC地址网段。使用落于该网段的P-GW地址的UE，进行SRVCC过程中，USN会将该网段对应的E-STN-SR携带给MSC。 |
| IPV4MSK | PGW的IPV4地址掩码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置P-GW的IPv4类型的GTPC地址掩码。<br>前提条件：该参数在<br>“PGW的IP地址类型”<br>配置为<br>“IPV4(IPV4)”<br>后生效。<br>数据来源：运营商规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>说明：- “0.0.0.0”是无效掩码。<br>- 输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。 |
| PGWIPV6 | PGW的IPV6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置P-GW的IPv6地址。<br>前提条件：该参数在<br>“PGW的IP地址类型”<br>配置为<br>“IPV6(IPV6)”<br>后生效。<br>数据来源：运营商规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| IPV6MSK | IPV6地址前缀长度 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置P-GW的IPv6地址的前缀的长度。<br>前提条件：该参数在<br>“PGW的IP地址类型”<br>配置为<br>“IPV6(IPV6)”<br>后生效。<br>数据来源：运营商规划<br>取值范围： 1～128<br>默认值： 无 |

## 操作的配置对象

- [E-STN-SR和PGW关系配置表（PGWESTNSR）](configobject/UNC/20.15.2/PGWESTNSR.md)

## 使用实例

删除 “PGW的IP地址类型” 为 “IPV4” ， “PGW的IPV4地址” 为 “192.168.111.1” ， “PGW的IPV4地址掩码” 为 “255.255.255.255” 的SRVCC的紧急会话转移号码和P-GW关系配置表:

RMV PGWESTNSR: IPT=IPV4, PGWIPV4="192.168.111.1", IPV4MSK="255.255.255.255";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除E-STN-SR和PGW关系配置表(RMV-PGWESTNSR)_72225189.md`
