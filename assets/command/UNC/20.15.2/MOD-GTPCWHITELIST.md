---
id: UNC@20.15.2@MMLCommand@MOD GTPCWHITELIST
type: MMLCommand
name: MOD GTPCWHITELIST（修改GTP-C路径白名单）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD GTPCWHITELIST（修改GTP-C路径白名单）

## 功能

**适用网元：MME**

本命令用于修改GTP-C路径白名单的描述信息。

## 注意事项

- 本命令执行后对新的SRVCC流程生效。
- 对于本命令，{接口类型、本端IP、对端IP}唯一决定一条记录，只能用于定位待修改的记录，然后修改{描述}信息，这三个参数本身不能被修改。

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
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：本参数用于描述路径信息，比如描述对端IP地址所属设备名称。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [GTP-C路径白名单（GTPCWHITELIST）](configobject/UNC/20.15.2/GTPCWHITELIST.md)

## 使用实例

修改GTP-C路径白名单的描述信息。

MOD GTPCWHITELIST: INTFTP=Sv, IPT=IPV4, LIPV4="192.168.23.67", PIPV4="192.168.123.4", DESC="MSC2";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GTP-C路径白名单(MOD-GTPCWHITELIST)_72225597.md`
