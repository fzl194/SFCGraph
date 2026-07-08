---
id: UDG@20.15.2@MMLCommand@SET APNIPV6INFID
type: MMLCommand
name: SET APNIPV6INFID（设置APN IPv6接口ID配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNIPV6INFID
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- IPv6接口标识管理
- APN IPv6接口标识管理
status: active
---

# SET APNIPV6INFID（设置APN IPv6接口ID配置）

## 功能

**适用NF：PGW-U、UPF**

![](设置APN IPv6接口ID配置（SET APNIPV6INFID）_71074281.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，开启本功能后，对应APN下的IPv6地址interface ID将会包含用户标识信息IMSI，请关注个人隐私保护。

该命令用于控制为用户分配IPv6地址时，APN下是否开启IMSI作为用户的IPv6地址interface ID(IPv6地址的后64位)功能。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条ApnIPv6InfId。
- 该配置应与SMF保持一致。
- 开启本功能时建议根据实际情况部署安全传输功能如IPsec，提高对个人隐私的保护能力。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| IMSI | 配置IMSI作为IPv6 interface ID | 可选必选说明：必选参数<br>参数含义：该参数用于控制开启和关闭IMSI作为用户的IPv6地址interface ID功能，在未设置IMSI值的条件下，默认继承GlbIpv6InfId的配置。<br>数据来源：本端规划<br>取值范围：枚举类型。必须全部为整数。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>- INHERIT：继承全局“SET GlbIPv6InfId: IMSI= ENABLE/DISABLE”配置。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@APNIPV6INFID]] · APN IPv6接口ID配置（APNIPV6INFID）

## 使用实例

配置APN名称为apn1，IMSI作为用户的IPv6地址interface ID(IPv6地址的后64位)功能使能：

```
SET APNIPV6INFID: APN="apn1", IMSI=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-APNIPV6INFID.md`
