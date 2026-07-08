---
id: UDG@20.15.2@MMLCommand@LST APNREFPOOLGRP
type: MMLCommand
name: LST APNREFPOOLGRP（显示APN和地址池组映射关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNREFPOOLGRP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- APN和地址池组映射关系
status: active
---

# LST APNREFPOOLGRP（显示APN和地址池组映射关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示指定地址池组，若干APN通过地址池组映射关系映射到该地址池组。

## 注意事项

通过LST POOLGRPMAP可以查看地址池组映射关系，如果地址池组映射关系没有APN参数，则LST APNREFPOOLGRP命令会显示所有映射到该地址组受影响的APN信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLGROUPNAME | 地址池组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79。不支持空格及特殊字符“_”、“#”、“$”和“&”等，由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| HASVPN | 绑定VPN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN是否绑定VPN。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：<br>- 该命令ENABLE时，表示查询显示指定IP地址类型和VPN实例的APN。<br>- 该参数为DISABLE时，表示显示没有绑定指定IP地址类型的VPN实例的APN。 |
| VPNINSTANCE | VPN实例名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“HASVPN”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定VPN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNREFPOOLGRP]] · APN和地址池组映射关系（APNREFPOOLGRP）

## 使用实例

- 显示根据地址池组映射规则映射到地址池组pg1的APN，而且APN没有绑定了IPv4地址类型的VPN：
  ```
  LST APNREFPOOLGRP: POOLGROUPNAME="pg1", IPVERSION=IPV4, HASVPN=DISABLE;
  ```
  ```

  RETCODE = 0 操作成功。

  APN和地址池组映射关系
  -------------------------------------------
  APN名称 映射规则名称

  apn1 map1
  apn1 map2
  (结果个数 = 2)
  --- END
  ```
- 显示根据地址池组映射规则映射到地址池组pg1的APN，而且APN是绑定了IPv4地址类型的VPN，VPN实例名称为vpn1：
  ```
  LST APNREFPOOLGRP: POOLGROUPNAME="pg1", IPVERSION=IPV4, HASVPN=ENABLE, VPNINSTANCE="vpn1";
  ```
  ```

  RETCODE = 0 操作成功。

  APN和地址池组映射关系
  -------------------------------------------
  APN名称 映射规则名称

  apn2 map1
  apn3 map1
  apn4 map1
  (结果个数 = 3)
  --- END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNREFPOOLGRP.md`
