---
id: UDG@20.15.2@MMLCommand@SET APNUEMUTACC
type: MMLCommand
name: SET APNUEMUTACC（设置APN下用户互访控制配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNUEMUTACC
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- 用户互访控制
- APN用户互访控制
status: active
---

# SET APNUEMUTACC（设置APN下用户互访控制配置）

## 功能

**适用NF：UPF、PGW-U**

![](设置APN下用户互访控制配置（SET APNUEMUTACC）_82837776.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，APN下终端互访控制功能开启后，所有此APN内或者和其它APN之间的终端互访将无法进行。 当修改INNERAPNS_S5S8P、INNERAPNS_N9A、INTERAPNS_S5S8P、INTERAPNS_N9A等参数时，需要使用ADD UEMUTWLISTBIND命令绑定白名单，否则会导致UE互访业务不通。

本命令仅适用于同一UPF网元内不同UE会话的互访控制，如果需要跨UPF网元的不同UE会话的互访控制，需要在UPF上配置ACL规则。

该命令用于配置指定APN下用户互访禁止功能开关是否开启，包括APN间的用户互访及APN内的用户互访。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条。
- APN间的用户互访功能开关及APN内的用户互访功能开关缺省为继承。
- 当两个APN绑定的VPN不同时，该命令无法禁止两个APN下的终端互相访问。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | InnerAPNS | InterAPNS | InnerAPNS_S5S8P | InnerAPNS_N9A | InterAPNS_S5S8P | InterAPNS_N9A |
| --- | --- | --- | --- | --- | --- | --- |
| 初始值 | INHERIT | INHERIT | INHERIT | INHERIT | INHERIT | INHERIT |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| INNERAPNS | 同APN内的控制开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置是否开启APN内终端互访控制功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：设置后继承全局的配置。<br>- ENABLE：使能，禁止终端互访。<br>- DISABLE：不使能，允许终端互访。<br>默认值：无<br>配置原则：无 |
| INTERAPNS | 不同APN间的控制开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置是否开启和其它APN之间的终端互访控制功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：设置后继承全局的配置。<br>- ENABLE：使能，禁止终端互访。<br>- DISABLE：不使能，允许终端互访。<br>默认值：无<br>配置原则：无 |
| INNERAPNS_S5S8P | 同APN内S5S8P口互访控制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置是否开启APN内S5S8P接口流量的终端互访控制功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：设置后继承APN级的配置，不关注白名单。<br>- ENABLE：使能，禁止未命中SGW白名单的终端互访流量。<br>- DISABLE：不使能，允许终端互访。<br>默认值：无<br>配置原则：无 |
| INNERAPNS_N9A | 同APN内N9A口互访控制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置是否开启APN内N9A接口流量的终端互访控制功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：设置后继承APN级的配置，不关注白名单。<br>- ENABLE：使能，禁止未命中I-UPF白名单的终端互访流量。<br>- DISABLE：不使能，允许终端互访。<br>默认值：无<br>配置原则：无 |
| INTERAPNS_S5S8P | 不同APN间S5S8P口互访控制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置是否开启APN间S5S8P接口流量的终端互访控制功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：设置后继承APN级的配置，不关注白名单。<br>- ENABLE：使能，禁止未命中SGW白名单的终端互访流量。<br>- DISABLE：不使能，允许终端互访。<br>默认值：无<br>配置原则：无 |
| INTERAPNS_N9A | 不同APN间N9A口互访控制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置是否开启APN间N9A接口流量的终端互访控制功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：设置后继承APN级的配置，不关注白名单。<br>- ENABLE：使能，禁止未命中I-UPF白名单的终端互访流量。<br>- DISABLE：不使能，允许终端互访。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN下用户互访控制配置（APNUEMUTACC）](configobject/UDG/20.15.2/APNUEMUTACC.md)

## 使用实例

设置APN为apn1.com的APN内用户互访禁止功能开关为开启，APN间的用户互访禁止功能开关为开启，同APN内S5S8P口互访控制开关为开启，同APN内N9A口互访控制开关为开启，不同APN间S5S8P口互访控制开关为开启，不同APN间N9A口互访控制开关为开启：

```
SET APNUEMUTACC: APN="apn1.com", INNERAPNS=ENABLE, INTERAPNS=ENABLE,INNERAPNS_S5S8P=ENABLE,INNERAPNS_N9A=ENABLE, INTERAPNS_S5S8P=ENABLE, INTERAPNS_N9A=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置APN下用户互访控制配置（SET-APNUEMUTACC）_82837776.md`
