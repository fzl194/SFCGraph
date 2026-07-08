---
id: UDG@20.15.2@MMLCommand@ADD PUREFWDUSER
type: MMLCommand
name: ADD PUREFWDUSER（设置指定用户进行纯转发）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: PUREFWDUSER
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 2
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 用户纯转发配置
status: active
---

# ADD PUREFWDUSER（设置指定用户进行纯转发）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令通过MSISDN、IMSI设置指定用户进行纯转发，纯转发用户走快速转发流程。

纯转发指不对该MSISDN、IMSI进行计费或7层业务解析，直接将报文进行转发。

该命令用于提升UPF数传定位定界自证能力。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为2。
- 记录用户信息后，可能会对该用户的性能产生轻微的影响。用户信息保存到该用户再次上线为止。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERTYPE | 用户类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：表示用户的IMSI号。<br>- MSISDN：表示用户的MSISDN号。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERTYPE”配置为“IMSI”时为必选参数。<br>参数含义：表示用户的IMSI号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。必须全部为整数。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERTYPE”配置为“MSISDN”时为必选参数。<br>参数含义：表示用户的MSISDN号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。必须全部为整数，且不能为“19”。 MSISDN号的组成： 1、用户注册的国家的Country Code (CC) 2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PUREFWDUSER]] · 纯转发用户配置（PUREFWDUSER）

## 使用实例

不对IMSI为460011223344551的用户进行计费以及7层业务解析，将该用户设置为纯转发用户：

```
ADD PUREFWDUSER: USERTYPE=IMSI,IMSI="460011223344551";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-PUREFWDUSER.md`
