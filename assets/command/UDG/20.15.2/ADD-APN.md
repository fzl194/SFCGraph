---
id: UDG@20.15.2@MMLCommand@ADD APN
type: MMLCommand
name: ADD APN（添加APN配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: APN
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- APN管理
- APN
status: active
---

# ADD APN（添加APN配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于添加一个新的APN实例。在运营商需要接入数据网络，配置APN和绑定VPN时使用此命令进行配置。GPRS/UMTS/EPC/5GC核心网中采用APN来标识系统，同时APN定义了系统可以接入的数据网络。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条APN。
- 当前版本不支持此命令的PseudoActSwitch参数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：输入的APN名称需要满足APN名称的取值范围。 |
| HASVPN | 绑定VPN | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否绑定IPv4 VPN。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：<br>- 该参数为ENABLE时，表示绑定IPv4 VPN。<br>- 该参数为DISABLE时，表示不绑定IPv4 VPN。 |
| VPNINSTANCE | VPN实例名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“HASVPN”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定IPv4 VPN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：<br>- 当参数HASVPN为ENABLE时，该参数为必选参数。<br>- 该参数通过ADD VPNINST命令配置生成。 |
| HASVPNIPV6 | 绑定IPv6 VPN | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否绑定IPv6 VPN。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：<br>- 该参数为ENABLE时，表示绑定IPv6 VPN。<br>- 该参数为DISABLE时，表示不绑定IPv6 VPN。 |
| VPNINSTANCEIPV6 | IPv6 VPN实例名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“HASVPNIPV6”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定IPv6 VPN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：<br>- 当参数HASVPNIPV6为ENABLE时，该参数为必选参数。<br>- 绑定的IPv6 VPN必须是已经配置过的。 |
| PSEUDOACTSWITCH | 支持假激活用户开关 | 可选必选说明：可选参数<br>参数含义：该参数是用来配置APN是否支持假激活用户的开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：继承全局。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：INHERIT<br>配置原则：<br>- 适用网元：UPF。<br>- 业务处理过程中优先应用APN的设置，只有当APN的配置为INHERIT 时才应用全局的设置（SET GLOBALIMS）。<br>- 参数取值ENABLE：可以避免信令风暴的发生。 |
| RESTORPGWSWITCH | 故障重启业务恢复功能PGW开关 | 可选必选说明：可选参数<br>参数含义：该参数用来设置是否打开网络侧触发的业务恢复功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：继承全局。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：INHERIT<br>配置原则：<br>- 适用网元：PGW-U。<br>- 对于具备SGW-C故障重启场景下业务恢复功能的用户，PGW-U收到PGW-C通知后会变成保留承载。<br>- 业务处理过程中优先应用APN的设置，只有当APN的配置为INHERIT 时才应用全局的设置（SET FASTRECOVERY）。 |
| PDTNSWITCH | PDTN功能开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“RESTORPGWSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置是否打开PGW触发的SGW故障重启场景下的业务恢复功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：<br>- 适用网元：PGW-U。<br>- 该参数使能的情况下，PGW-U上的保留承载在收到下行数据时触发向PGW-C发送PFCP Session Report Request消息。<br>- 该参数不使能的情况下，PGW-U上的保留承载收到下行数据时不触发PFCP Session Report Request消息。 |
| APPLAYERVOLUME | 仅统计应用层流量 | 可选必选说明：可选参数<br>参数含义：该参数用于统计应用层流量。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：DISABLE<br>配置原则：<br>- 该参数使能时，表示仅统计L7应用层流量，不统计L3/L4承载层流量。<br>- 该参数不使能时，表示统计L7应用层流量和L3/L4承载层流量。<br>- 配置该参数前，需要明确预期的流量统计方式，不同的流量统计方式，会影响最终计费话单上的流量统计结果，修改前请联系华为技术支持。 |
| HEADENGRAYLIST | 头增强灰名单 | 可选必选说明：可选参数<br>参数含义：该参数用来配置当前APN是否启用头增强灰名单功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：DISABLE<br>配置原则：<br>- 该参数使能时，当前APN启用头增强灰名单功能。<br>- 该参数不使能时，当前APN关闭头增强灰名单功能。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@APN]] · APN配置（APN）

## 关联任务

- [[UDG@20.15.2@Task@0-00020]]

## 使用实例

当运营商需要接入数据网络时，需要保障内部网络通信，这时候需要配置APN和绑定VPN：

```
ADD APN: APN="huawei.com", HASVPN=DISABLE, HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-APN.md`
