---
id: UNC@20.15.2@MMLCommand@RMV SDAPLE
type: MMLCommand
name: RMV SDAPLE（删除SDAP本地实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SDAPLE
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- Sdup接口管理
- Sdup接口业务地址管理
status: active
---

# RMV SDAPLE（删除SDAP本地实体）

## 功能

**适用网元：MME**

本命令用于删除Sdup接口的业务IP地址。

## 注意事项

- 该命令执行后立即生效。
- 若整系统的最后一条记录删除，将会导致“WSFD-201201 MME链式备份”特性不可用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DELTYPE | 删除方式 | 可选必选说明：可选参数<br>参数含义：本参数用于删除指定Sdup接口的删除方式<br>数据来源：全网规划<br>取值范围：<br>- “BYINDEX(BY INDEX)”<br>- “BYIP(BY IP)”<br>默认值：BYINDEX(BY INDEX) |
| INDEX | 记录索引 | 可选必选说明：条件必选参数<br>参数含义：本参数用于删除指定Sdup接口的业务IP地址类型。<br>前提条件：该参数在<br>“删除方式”<br>参数配置为<br>“BYINDEX(BY INDEX)”<br>后生效<br>数据来源：全网规划<br>取值范围：0~65535<br>默认值：无 |
| IPTYPE | IP地址类型 | 可选必选说明：条件必选参数<br>参数含义：本参数用于删除指定Sdup接口的业务IP地址类型。<br>前提条件：该参数在<br>“删除方式”<br>参数配置为<br>“BYIP(BY IP)”<br>后生效<br>数据来源：全网规划<br>取值范围：<br>- “ITPTADDR_TYPE_IPV4(IPV4)”<br>- “TPTADDR_TYPE_IPV6(IPV6)”<br>默认值：无 |
| LEIPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于删除指定Sdup接口的业务IP地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“TPTADDR_TYPE_IPV4(IPV4)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| LEIPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于删除指定Sdup接口的业务IP地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“TPTADDR_TYPE_IPV6(IPV6)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1/128)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SDAPLE]] · SDAP本地实体（SDAPLE）

## 使用实例

该命令用于删除Sdup接口的业务IP地址，执行如下命令：

RMV SDAPLE: DELTYPE=BYIP, IPTYPE=TPTADDR_TYPE_IPV4, LEIPV4="192.168.15.10";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SDAPLE.md`
