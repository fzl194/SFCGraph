---
id: UNC@20.15.2@MMLCommand@RMV IMSIAPNBINDUP
type: MMLCommand
name: RMV IMSIAPNBINDUP（删除APN下用户和UPF的绑定关系配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IMSIAPNBINDUP
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- 用户APN绑定UPF
status: active
---

# RMV IMSIAPNBINDUP（删除APN下用户和UPF的绑定关系配置）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于删除APN下用户和UPF的绑定关系，支持删除APN下一个用户和UPF的绑定，也支持删除同一个APN下连续IMSI号段的用户和UPF的绑定。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 起始IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI号段的起始IMSI，当ENDIMSI没有值时，起始IMSI和终止IMSI相同。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。该参数每一位只能是数字0-9。<br>默认值：无<br>配置原则：无 |
| ACCESSTYPE | 接入类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的接入类型。<br>数据来源：本端规划<br>取值范围：<br>- GUL（2/3/4G接入）<br>- NG（5G接入）<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入APN需要在ADD APN命令中配置。<br>输入的APN名称需要符合APN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSIAPNBINDUP]] · APN下用户和UPF的绑定关系配置（IMSIAPNBINDUP）

## 使用实例

删除用户“11111111111111”，APN为“huawei.com”在5G的UP绑定关系：

```
RMV IMSIAPNBINDUP: IMSI="11111111111111", ACCESSTYPE=NG, APN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APN下用户和UPF的绑定关系配置（RMV-IMSIAPNBINDUP）_21861989.md`
