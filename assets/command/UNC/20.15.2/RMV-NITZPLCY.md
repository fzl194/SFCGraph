---
id: UNC@20.15.2@MMLCommand@RMV NITZPLCY
type: MMLCommand
name: RMV NITZPLCY（删除NITZ策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NITZPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NITZ管理
- NITZ策略管理
status: active
---

# RMV NITZPLCY（删除NITZ策略）

## 功能

**适用NF：AMF**

该命令用于删除已配置的NITZ策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREARANGE | 区域范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定AMF服务的某些区域范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_AREA（所有区域）”：所有区域<br>- “AREA_CODE（指定区域编码）”：指定区域编码<br>默认值：无<br>配置原则：无 |
| AREACODE | 区域编码 | 可选必选说明：该参数在"AREARANGE"配置为"AREA_CODE"时为条件必选参数。<br>参数含义：该参数用于唯一标识AMF服务的某个区域，该区域由一个或者若干个跟踪区组成。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。该区域编码必须已经通过ADD AREACODE命令添加成功，可执行LST AREACODE进行查看，区域编码中的成员由ADD AREAMEM添加。<br>默认值：无<br>配置原则：无 |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于表示应用NITZ策略的用户群标识。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “USER_GROUP（用户群）”：用户群<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定应用NITZ策略的用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| USRGRPID | 用户群组标识 | 可选必选说明：该参数在"SUBRANGE"配置为"USER_GROUP"时为条件必选参数。<br>参数含义：该参数用于指定应用NITZ策略的用户群标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。该用户群标识必须已经通过ADD NGUSRGRP命令添加成功，可执行LST NGUSRGRP进行查看，用户群中的用户可通过ADD NGUSRGRPMEM添加。<br>默认值：无<br>配置原则：<br>当USRGRPID未输入取值时，系统会为此参数赋无效值4294967295(0xFFFFFFFF)。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NITZPLCY]] · NITZ策略（NITZPLCY）

## 使用实例

删除区域编码为SomeCity的本网用户配置的NITZ策略，执行如下命令：

```
RMV NITZPLCY: AREARANGE=AREA_CODE, AREACODE="SomeCity", SUBRANGE=HOME_USER;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NITZ策略（RMV-NITZPLCY）_09652658.md`
