---
id: UDG@20.15.2@MMLCommand@RMV VOLTELOOP
type: MMLCommand
name: RMV VOLTELOOP（删除VoLTE话路环回功能）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: VOLTELOOP
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- VOLTE管理
- Volte环回
status: active
---

# RMV VOLTELOOP（删除VoLTE话路环回功能）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

此命令用于删除VoLTE话路环回功能。当使用完话路环回功能，为不影响用户的正常语音业务，需要及时关闭该功能，此时需要使用该命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDTYPE | 标识类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定标识类型是用户IMSI或者MSISDN。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：按IMSI号码对用户的用户面数据报文进行重定向。<br>- MSISDN：按MSISDN号码对用户的用户面数据报文进行重定向。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“IDTYPE”配置为“IMSI”时为必选参数。<br>参数含义：该参数用于表示该IMSI号码用户的用户面数据报文进行重定向。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。不推荐单个MCC区内两个和三个数字混合编码的MNC，此种情况已经在本书之外。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“IDTYPE”配置为“MSISDN”时为必选参数。<br>参数含义：该参数用于表示该MSISDN号码用户的用户面数据报文进行重定向。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 MSISDN号的组成： 1、用户注册的国家的Country Code (CC) 2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VOLTELOOP]] · VoLTE话路环回功能（VOLTELOOP）

## 使用实例

使用完话路环回功能后，要及时关闭该功能，此时使用删除命令，删除IMSI为456645645644565用户的VoLTE话路环回功能：

```
RMV VOLTELOOP:IDTYPE=IMSI,IMSI="456645645644565";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-VOLTELOOP.md`
