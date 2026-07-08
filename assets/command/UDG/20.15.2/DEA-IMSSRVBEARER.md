---
id: UDG@20.15.2@MMLCommand@DEA IMSSRVBEARER
type: MMLCommand
name: DEA IMSSRVBEARER（去激活指定用户的IMS Bypass状态）
nf: UDG
version: 20.15.2
verb: DEA
object_keyword: IMSSRVBEARER
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- VOLTE管理
- IMS Bypass
status: active
---

# DEA IMSSRVBEARER（去激活指定用户的IMS Bypass状态）

## 功能

**适用NF：PGW-U、UPF**

![](去激活指定用户的IMS Bypass状态（DEA IMSSRVBEARER）_94130730.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，此命令将触发对特定用户/用户组/整机的IMS Bypass用户发送QoS URR Stop消息，可能中断这些用户的语音业务。

该命令用于退出指定用户的IMS Bypass状态，触发指定的IMS Bypass用户发送QoS URR Stop消息，SMF收到此消息后会去激活IMS Bypass的专有承载。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEATYPE | 退出方式 | 可选必选说明：必选参数<br>参数含义：该参数用户设置IMS Bypass的退出方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：按IMSI退出IMS Bypass状态。<br>- MSISDN：按MSISDN退出MS Bypass状态。<br>- APN：按APN退出用户IMS Bypass状态。<br>- SYSTEM：整机用户退出IMS Bypass状态。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“DEATYPE”配置为“IMSI”时为必选参数。<br>参数含义：用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“DEATYPE”配置为“MSISDN”时为必选参数。<br>参数含义：用户的MSISDN信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 MSISDN号的组成： 1、用户注册的国家的Country Code (CC) 2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。<br>默认值：无<br>配置原则：无 |
| APN | APN | 可选必选说明：条件必选参数<br>前提条件：该参数在“DEATYPE”配置为“APN”时为必选参数。<br>参数含义：指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及部分特殊字符。可以支持的特殊字符有“.”和“-”，“.”不可以是第一个字符且不可以连续出现。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IMSSRVBEARER]] · 指定用户的IMS Bypass状态（IMSSRVBEARER）

## 使用实例

假设运营商需要退出指定用户的IMS Bypass状态，IMSI为46001123456789：

```
DEA IMSSRVBEARER: DEATYPE=IMSI, IMSI="46001123456789";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/去激活指定用户的IMS-Bypass状态（DEA-IMSSRVBEARER）_94130730.md`
