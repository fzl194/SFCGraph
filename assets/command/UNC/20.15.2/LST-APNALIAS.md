---
id: UNC@20.15.2@MMLCommand@LST APNALIAS
type: MMLCommand
name: LST APNALIAS（查询APN别名配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNALIAS
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- 别名APN
status: active
---

# LST APNALIAS（查询APN别名配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询别名APN与转换APN的映射关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNTYPE | APN类型 | 可选必选说明：可选参数<br>参数含义：该参数指定输入的APN名称是别名APN还是转换APN。<br>数据来源：本端规划<br>取值范围：<br>- ALIAS_APN（别名APN）<br>- CONVERT_APN（转换APN）<br>默认值：无<br>配置原则：<br>- 如果运营商希望输入转换APN，则把APNTYPE置成CONVERT_APN。<br>- 如果运营商希望输入别名APN，则把APNTYPE置成ALIAS_APN。 |
| SUBRANGE | 用户范围 | 参数含义：该参数用于指定用户的范围。<br>数据来源：本端规划<br>取值范围：<br>- ALL_USER（所有用户）<br>- SPECIFIC_NS（指定切片）<br>默认值：无<br>配置原则：<br>“用户范围”+(“切片业务类型”“切片细分标识”组成的切片)+“别名APN”不能重复。<br>“指定切片”的优先级高于“所有用户”。 |
| SST | 切片业务类型 | 参数含义：该参数表示切片的业务类型，如eMBB（1）、URLLC（2）、MIoT（3）等协议定义的标准SST，或者运营商自定义的SST。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 参数含义：该参数表示根据服务群体，对某类网络业务切片的进一步细分。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是6。只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| ALIASAPN | 别名APN | 参数含义：该参数用于指定别名APN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| CONVERTAPN | 转换APN | 参数含义：该参数用于指定转换后的APN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN别名配置（APNALIAS）](configobject/UNC/20.15.2/APNALIAS.md)

## 使用实例

- 当需要查询适用于“所有用户”的指定的别名APN“1”对应的转换APN时，执行如下命令：
  ```
  LST APNALIAS: APNTYPE=ALIAS_APN, SUBRANGE=ALL_USER, ALIASAPN="1";
  ```
- 当需要查询指定的转换APN“ma”对应的别名APN时，执行如下命令：
  ```
  LST APNALIAS: APNTYPE=CONVERT_APN, CONVERTAPN="ma";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN别名配置（LST-APNALIAS）_28567626.md`
