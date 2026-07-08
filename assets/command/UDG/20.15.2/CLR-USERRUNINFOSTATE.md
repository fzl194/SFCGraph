---
id: UDG@20.15.2@MMLCommand@CLR USERRUNINFOSTATE
type: MMLCommand
name: CLR USERRUNINFOSTATE（清除指定用户全部的运行信息记录）
nf: UDG
version: 20.15.2
verb: CLR
object_keyword: USERRUNINFOSTATE
command_category: 动作类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 用户运行信息查询
status: active
---

# CLR USERRUNINFOSTATE（清除指定用户全部的运行信息记录）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于清除指定用户的全部运行信息记录，清除的记录是规则的命中次数、流量统计。后续查询只能查到清除记录之后的用户信息。

## 注意事项

- 该命令执行后立即生效。
- 一般在使用前先查询该用户的运行信息，然后清除，再进行业务，再通过查询运行信息，了解用户业务情况。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERTYPE | 用户类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：表示用户的IMSI号。<br>- MSISDN：表示用户的MSISDN号。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERTYPE”配置为“IMSI”时为必选参数。<br>参数含义：表示用户的IMSI号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。必须全部为整数。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERTYPE”配置为“MSISDN”时为必选参数。<br>参数含义：表示用户的MSISDN号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。必须全部为整数，且不能为“19”。 MSISDN号的组成： 1、用户注册的国家的Country Code (CC) 2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/USERRUNINFOSTATE]] · 指定用户的运行信息（USERRUNINFOSTATE）

## 使用实例

- 清除指定imsi用户的运行信息：
  ```
  CLR USERRUNINFOSTATE: USERTYPE=IMSI,IMSI="460011223344551";
  ```
- 清除指定msisdn用户的运行信息：
  ```
  CLR USERRUNINFOSTATE: USERTYPE=MSISDN,MSISDN="1223344551";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/CLR-USERRUNINFOSTATE.md`
