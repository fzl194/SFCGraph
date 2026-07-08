---
id: UNC@20.15.2@MMLCommand@LCK APNALIAS
type: MMLCommand
name: LCK APNALIAS（锁定APN别名配置）
nf: UNC
version: 20.15.2
verb: LCK
object_keyword: APNALIAS
command_category: 动作类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- 别名APN
status: active
---

# LCK APNALIAS（锁定APN别名配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用来配置对指定别名APN进行锁定操作。当别名APN锁定后，后续使用该别名APN激活的用户激活失败，已经在线的用户无影响。缺省情况下别名APN未锁定。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 配置对指定别名APN进行锁定操作，会导致用户接入失败。
- 修改别名APN的锁定状态时，对后续激活的用户生效。
- 一般情况下不要锁定别名APN。只有在特殊情况下，例如需要手动去活该别名APN下的所有用户时，可以将LOCKED参数置为ENABLE，并通过DEA SMCTX命令指定“请求APN”为别名APN来去活用户。用户去活速率可以通过SET DEACTIVERATE命令控制。
- 无论2/3/4G会话是否存在切片，仅“用户范围”为“ALL_USER”取值的配置记录才会生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNTYPE | APN类型 | 可选必选说明：必选参数<br>参数含义：该参数指定输入的APN名称是别名APN还是转换APN。<br>数据来源：本端规划<br>取值范围：<br>- ALIAS_APN（别名APN）<br>- CONVERT_APN（转换APN）<br>默认值：无<br>配置原则：<br>- 如果运营商希望输入转换APN，则把APNTYPE置成CONVERT_APN。<br>- 如果运营商希望输入别名APN，则把APNTYPE置成ALIAS_APN。 |
| SUBRANGE | 用户范围 | 可选必选说明：该参数在"APNTYPE"配置为"ALIAS_APN"时为条件必选参数。<br>参数含义：该参数用于指定用户的范围。<br>数据来源：本端规划<br>取值范围：<br>- ALL_USER（所有用户）<br>- SPECIFIC_NS（指定切片）<br>默认值：无<br>配置原则：<br>“用户范围”+(“切片业务类型”“切片细分标识”组成的切片)+“别名APN”不能重复。<br>“指定切片”的优先级高于“所有用户”。 |
| SST | 切片业务类型 | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIC_NS"时为条件必选参数。<br>参数含义：该参数表示切片的业务类型，如eMBB（1）、URLLC（2）、MIoT（3）等协议定义的标准SST，或者运营商自定义的SST。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIC_NS"时为条件可选参数。<br>参数含义：该参数表示根据服务群体，对某类网络业务切片的进一步细分。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是6。只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| ALIASAPN | 别名APN | 可选必选说明：该参数在"APNTYPE"配置为"ALIAS_APN"时为条件必选参数。<br>参数含义：该参数用于指定别名APN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| CONVERTAPN | 转换APN | 可选必选说明：该参数在"APNTYPE"配置为"CONVERT_APN"时为条件必选参数。<br>参数含义：该参数用于指定转换后的APN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOCKED | 锁定别名APN | 可选必选说明：必选参数<br>参数含义：该参数用于配置是否对别名APN进行锁定操作。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNALIAS]] · APN别名配置（APNALIAS）

## 使用实例

锁定为“所有用户”配置的名为“mtest”的别名APN，执行如下命令：

```
LCK APNALIAS: APNTYPE=ALIAS_APN, SUBRANGE=ALL_USER, ALIASAPN="mtest", LOCKED=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LCK-APNALIAS.md`
