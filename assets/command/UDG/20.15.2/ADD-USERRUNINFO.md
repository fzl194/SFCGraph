---
id: UDG@20.15.2@MMLCommand@ADD USERRUNINFO
type: MMLCommand
name: ADD USERRUNINFO（添加网关对IMSI/MSISDN指定的用户的运行信息进行收集配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: USERRUNINFO
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 4
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 用户运行信息收集
status: active
---

# ADD USERRUNINFO（添加网关对IMSI/MSISDN指定的用户的运行信息进行收集配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置网关添加IMSI/MSISDN指定用户的运行信息，这些信息包括用户使用的动态规则、静态规则、BWM-RULE，以及各规则匹配次数，L7Filter匹配次数，动态规则名称和flow信息，car/shaping信息。

命令可用于系统维护人员收集指定用户在线期间，匹配系统中所配置的各种规则的次数。通过这些信息，增强了网关业务调测的分析功能和定位能力。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为4。
- 此命令需要在激活用户之前进行配置。
- 对IMSI/MSISDN指定的用户生效。
- 记录用户信息后，可能会对该用户的性能产生轻微的影响。用户信息保存到该用户再次上线为止。
- 如果存在多条配置与用户匹配，则用户信息只会记录在第一条匹配的配置里。
- 最多可以指定4个用户。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERTYPE | 用户类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：表示用户的IMSI号。<br>- MSISDN：表示用户的MSISDN号。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERTYPE”配置为“IMSI”时为必选参数。<br>参数含义：表示用户的IMSI号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。必须全部为整数。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERTYPE”配置为“MSISDN”时为必选参数。<br>参数含义：表示用户的MSISDN号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。必须全部为整数，且不能为“19”。 MSISDN号的组成： 1、用户注册的国家的Country Code (CC) 2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [网关对IMSI/MSISDN指定的用户的运行信息进行收集配置（USERRUNINFO）](configobject/UDG/20.15.2/USERRUNINFO.md)

## 使用实例

- 添加imsi为460011223344551的用户的运行信息：
  ```
  ADD USERRUNINFO: USERTYPE=IMSI,IMSI="460011223344551";
  ```
- 添加msisdn为1223344551的用户的运行信息：
  ```
  ADD USERRUNINFO: USERTYPE=MSISDN,MSISDN="1223344551";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加网关对IMSI_MSISDN指定的用户的运行信息进行收集配置（ADD-USERRUNINFO）_82837071.md`
