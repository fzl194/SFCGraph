---
id: UNC@20.15.2@MMLCommand@RMV GTPCWHITELIST
type: MMLCommand
name: RMV GTPCWHITELIST（删除GTP-C路径白名单）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GTPCWHITELIST
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- GTP-C路径白名单
status: active
---

# RMV GTPCWHITELIST（删除GTP-C路径白名单）

## 功能

**适用网元：MME**

本命令用于删除GTP-C路径白名单。

## 注意事项

本命令执行后对新的SRVCC流程生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTFTP | 接口类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定对端IP地址所属的接口类型。<br>数据来源：全网规划<br>取值范围：<br>- “Sv(Sv)”<br>默认值：无 |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| LIPV4 | 本端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定本端IPv4地址。<br>前提条件：本参数在"IP地址类型"参数配置为"IPV4(IPV4)"后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| PIPV4 | 对端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定对端IPv4地址。<br>前提条件：本参数在"IP地址类型"参数配置为"IPV4(IPV4)"后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| LIPV6 | 本端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定本端IPv6地址。<br>前提条件：本参数在"IP地址类型"参数配置为"IPV6(IPV6)"后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| PIPV6 | 对端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定对端IPv6地址。<br>前提条件：本参数在"IP地址类型"参数配置为"IPV6(IPV6)"后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GTPCWHITELIST]] · GTP-C路径白名单（GTPCWHITELIST）

## 使用实例

删除GTP-C路径白名单的一条配置。

RMV GTPCWHITELIST: INTFTP=Sv, IPT=IPV4, LIPV4="192.168.23.67", PIPV4="192.168.123.4";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GTPCWHITELIST.md`
