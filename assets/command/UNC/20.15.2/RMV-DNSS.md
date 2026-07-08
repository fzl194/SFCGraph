---
id: UNC@20.15.2@MMLCommand@RMV DNSS
type: MMLCommand
name: RMV DNSS（删除DNS服务器）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DNSS
command_category: 配置类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- DNS
- DNS服务器管理
status: active
---

# RMV DNSS（删除DNS服务器）

## 功能

**适用网元：SGSN、MME** **、AMF**

该命令用于删除一个DNS服务器。

网元通过向DNS服务器发送域名解析请求，获得域名所对应IP地址。

## 注意事项

- 该命令执行后立即生效。
- 删除命令执行以后，网元将不会再向此DNS服务器发送域名解析请求，可能造成某些域名无法解析，请慎用此命令。
- 当该IP为其所属服务器组的唯一IP时，删除该IP会导致其所属的服务器组的删除。如果该服务器组的ID被DNSQ表引用（使用[**LST DNSQ**](../DNS查询管理/查询DNS查询控制参数(LST DNSQ)_72225573.md)查看），则需要首先使用[**RMV DNSQ**](../DNS查询管理/删除DNS查询控制参数(RMV DNSQ)_72345493.md)删除引用该ID的DNSQ记录。但是当该服务器组ID为0时，即使不删除DNSQ记录，也可以删除该服务器组，删除该服务器组后，将导致发向该组的DNS查询失败。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPID | 服务器组ID | 可选必选说明：必选参数<br>参数含义：该参数用来指定DNS服务器所属的服务器组。<br>数据来源：整网规划<br>取值范围：0~37<br>默认值：无 |
| IPT | IP地址类型 | 可选必选说明：可选参数<br>参数含义：IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- IPV4(IPV4)<br>- IPV6(IPV6)<br>默认值：无 |
| IP | IP地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用来指定DNS服务器IP地址。<br>该参数在"IP地址类型"参数配置为"IPV4(IPV4)"后生效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：DNS服务器IPv6地址<br>该参数在"IP地址类型"参数配置为"IPV6(IPV6)"后生效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |

## 操作的配置对象

- [DNS服务器（DNSS）](configobject/UNC/20.15.2/DNSS.md)

## 使用实例

删除第一组一个IP地址为192.168.100.101的DNS服务器：

RMV DNSS: GRPID=1, IPT=IPV4, IP="192.168.100.101";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DNS服务器(RMV-DNSS)_26145898.md`
