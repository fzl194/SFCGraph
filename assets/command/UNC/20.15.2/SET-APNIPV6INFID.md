---
id: UNC@20.15.2@MMLCommand@SET APNIPV6INFID
type: MMLCommand
name: SET APNIPV6INFID（设置APN IPv6接口ID配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: APNIPV6INFID
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- IPv6接口标识管理
- APN IPv6接口标识管理
status: active
---

# SET APNIPV6INFID（设置APN IPv6接口ID配置）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用于控制为用户分配IPv6地址时，APN下是否开启IMSI作为用户的IPv6地址Interface ID功能。

## 注意事项

- 该命令执行后立即生效。

- APN的值是由ADD APN命令添加，参数IMSI的初始值为INHERIT。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无。<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| IMSI | 配置IMSI作为IPv6 Interface ID | 可选必选说明：必选参数<br>参数含义：该参数用于控制开启和关闭IMSI作为用户的IPv6地址Interface ID功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- INHERIT（继承全局）<br>- ENABLE（使能）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [APN IPv6接口ID配置（APNIPV6INFID）](configobject/UNC/20.15.2/APNIPV6INFID.md)

## 使用实例

配置APN名称为apn1，IMSI作为用户的IPv6地址Interface ID功能使能：

```
SET APNIPV6INFID: APN="apn1", IMSI=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置APN-IPv6接口ID配置（SET-APNIPV6INFID）_96243076.md`
