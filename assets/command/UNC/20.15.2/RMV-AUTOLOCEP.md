---
id: UNC@20.15.2@MMLCommand@RMV AUTOLOCEP
type: MMLCommand
name: RMV AUTOLOCEP（删除自动上报的NSE下的本端端点）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AUTOLOCEP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb自动配置管理
- 自动配置维护功能
status: active
---

# RMV AUTOLOCEP（删除自动上报的NSE下的本端端点）

## 功能

![](删除自动上报的NSE下的本端端点(RMV AUTOLOCEP)_26145994.assets/notice_3.0-zh-cn_2.png)

- 此命令会导致删除端点的IPNSVC链路无法再承载业务。
- 删除NSE下唯一的本端端点会导致NSE相关业务不可用。

**适用网元：SGSN**

此命令用于删除自动上报的动态Gb over IP的NSE下的本端端点。自动上报的动态Gb over IP的NSE的属性和端点信息请通过 [**DSP NSE**](../../信令实体管理/显示NSE属性信息（DSP NSE）_26146030.md) 命令和 [**DSP IPNSVC**](../../Gb over IP管理/IP网络NSVC链路管理/显示IP网络NSVC配置表(DSP IPNSVC)_72345609.md) 命令查询。

## 注意事项

- 此命令执行后立即生效。
- 此命令会导致删除端点的IPNSVC链路无法再承载业务。
- 删除NSE下唯一的本端端点会导致NSE相关业务不可用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSEI | NSE标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除的本端端点的网络服务实体标识。<br>取值范围：0～65535<br>默认值：无 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除的本端端点的IP地址类型。<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无<br>配置原则：系统目前仅支持IPV4地址。 |
| LOCIPV4ADDR | 本端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待删除的本端端点的IPv4地址。<br>前提条件：该参数在<br>“ IP类型 ”<br>设置为<br>“IPV4(IPv4)”<br>时生效。<br>取值范围：0.0.0.1～255.255.255.254<br>默认值：无<br>说明：- 有效的IPv4地址不能为环回地址(127.x.y.z)。<br>- 有效的IPv4地址必须是A、B或者C类地址。 |
| LOCIPV6ADDR | 本端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待删除的本端端点的IPv6地址。<br>前提条件：该参数在<br>“ IP类型 ”<br>设置为<br>“IPV6(IPv6)”<br>时生效。<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>说明：IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| LOCPORT | 本端端口号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除的本端端点的端口号。<br>取值范围：1024～65535<br>默认值：无 |

## 操作的配置对象

- [自动上报的NSE下的本端端点（AUTOLOCEP）](configobject/UNC/20.15.2/AUTOLOCEP.md)

## 使用实例

删除一个 “NSE标识” 为 “1” “IP类型” 为 “IPV4(IPv4)” ， “本端IPv4地址” 为 “192.168.4.101” ， “本端端口号” 为 “1024” 的自动上报的NSE下的本端端点：

RMV AUTOLOCEP: NSEI=1, IPTYPE=IPV4, LOCIPV4ADDR="192.168.4.101", LOCPORT=1024;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除自动上报的NSE下的本端端点(RMV-AUTOLOCEP)_26145994.md`
